from django.shortcuts import render
from members.models import Member
from attendance.models import Attendance
from payments.models import Payment
from django.utils.timezone import now
from django.db.models import Sum
from django.db.models.functions import TruncMonth


def dashboard_view(request):
    today = now().date()

    # Basic Stats
    total_members = Member.objects.count()
    active_members = Member.objects.filter(status='active').count()

    total_attendance_today = Attendance.objects.filter(
        check_in__date=today
    ).count()

    total_revenue_today = Payment.objects.filter(
        payment_date=today
    ).aggregate(total=Sum('amount'))['total'] or 0

    monthly_revenue = Payment.objects.filter(
        payment_date__month=today.month,
        payment_date__year=today.year
    ).aggregate(total=Sum('amount'))['total'] or 0

    # 🔥 Monthly Chart Data
    monthly_data = (
        Payment.objects
        .annotate(month=TruncMonth('payment_date'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )

    labels = []
    data = []

    for item in monthly_data:
        labels.append(item['month'].strftime('%b'))
        data.append(item['total'])

    context = {
        'total_members': total_members,
        'active_members': active_members,
        'total_attendance_today': total_attendance_today,
        'total_revenue_today': total_revenue_today,
        'monthly_revenue': monthly_revenue,

        # Chart
        'labels': labels,
        'data': data,
    }
    return render(request, 'dashboard/dashboard.html', context)

def members_list(request):
    query = request.GET.get('q', '')

    if query:
        members = Member.objects.filter(name__icontains=query)
    else:
        members = Member.objects.all()

    context = {
        'members': members,
    }

    return render(request, 'dashboard/members_list.html', context)