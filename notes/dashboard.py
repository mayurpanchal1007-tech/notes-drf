from datetime import timedelta

from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.utils import timezone

from .models import Note


def dashboard_callback(request, context):
    today = timezone.now().date()
    start_date = today - timedelta(days=6)

    notes_per_day = (
        Note.objects.filter(created_at__date__gte=start_date)
        .annotate(day=TruncDate("created_at"))
        .values("day")
        .annotate(total=Count("id"))
        .order_by("day")
    )

    chart_data = {item["day"]: item["total"] for item in notes_per_day}

    labels = []
    data = []

    for i in range(7):
        day = start_date + timedelta(days=i)
        labels.append(day.strftime("%a"))
        data.append(chart_data.get(day, 0))

    context.update(
        {
            "total_notes": Note.objects.count(),
            "active_notes": Note.objects.filter(status="active").count(),
            "archived_notes": Note.objects.filter(status="archived").count(),
            "total_users": User.objects.count(),
            "recent_notes": Note.objects.select_related("user")[:5],
            "chart_labels": labels,
            "chart_data": data,
        }
    )

    return context