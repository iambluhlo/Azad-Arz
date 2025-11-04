from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import User
from transactions.models import Transaction
from alerts.models import SecurityAlert
from django.db.models import Sum

@api_view(['GET'])
def admin_stats(request):
    total_users = User.objects.count()
    total_trx = Transaction.objects.aggregate(total=Sum('amount'))['total'] or 0
    alert_count = SecurityAlert.objects.count()

    data = [
        {
            "title": "کل کاربران",
            "value": f"{total_users:,}",
            "change": "+5.2%",
            "changeType": "increase",
            "icon": "Users",
        },
        {
            "title": "حجم معاملات روزانه",
            "value": f"{total_trx/1_000_000_000:.1f}B",
            "change": "+12.5%",
            "changeType": "increase",
            "icon": "TrendingUp",
        },
        {
            "title": "درآمد",
            "value": f"{(total_trx*0.03)/1_000_000:.0f}M",
            "change": "+8.1%",
            "changeType": "increase",
            "icon": "DollarSign",
        },
        {
            "title": "هشدارهای امنیتی",
            "value": str(alert_count),
            "change": "-50%",
            "changeType": "decrease",
            "icon": "AlertTriangle",
        },
    ]

    return Response(data)

