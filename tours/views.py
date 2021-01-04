import random

from django.shortcuts import render

from .data import title, subtitle, description, departures, tours

COUNT_OF_TOURS_ON_MAIN_PAGE = 6


def main_view(request):
    six_random_tours = dict(random.sample(tours.items(), COUNT_OF_TOURS_ON_MAIN_PAGE))
    context = {
        'title': title,
        'subtitle': subtitle,
        'description': description,
        'tours': six_random_tours
    }
    return render(request, 'tours/index.html', context)


def departure_view(request, departure):
    filtered_tours = {}
    tour_prices = []
    tour_nights = []
    for id, tour in tours.items():
        if tour['departure'] == departure:
            filtered_tours[id] = tours[id]
            tour_prices.append(tour['price'])
            tour_nights.append(tour['nights'])
    selected_departure = departures.get(departure)

    if not filtered_tours:
        return render(request, '404.html', {})

    context = {
        'tours': filtered_tours,
        'departure': selected_departure,
        'tour_prices': tour_prices,
        'tour_nights': tour_nights,
    }
    return render(request, 'tours/departure.html', context)


def tour_view(request, tour_id):
    tour = tours.get(tour_id)
    if not tour:
        return render(request, '404.html', {})

    departure = departures.get(tour['departure'])
    context = {
        'tour': tour,
        'departure': departure,
    }
    return render(request, 'tours/tour.html', context)
