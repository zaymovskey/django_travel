from .data import departures


def departures_processor(request):
    return {'departures': departures}
