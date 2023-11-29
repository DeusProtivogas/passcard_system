from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.visit_time_utils import format_duration
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    current_visitors = Visit.objects.filter(
        leaved_at=None,
        leaved_at__isnull=True
    )

    non_closed_visits = []
    for visit in current_visitors:
        visitor = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(visit.get_duration()),
        }
        non_closed_visits.append(visitor)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
