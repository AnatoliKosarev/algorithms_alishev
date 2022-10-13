def min_stops(stations, capacity):
    result = 0
    current_stop = 0

    while current_stop < len(stations) - 1:
        next_stop = current_stop

        while (next_stop < len(stations) - 1) and (stations[next_stop + 1] - stations[current_stop] <= capacity):
            next_stop += 1

        if current_stop == next_stop:
            return 'Next station is too far'

        if next_stop < len(stations) - 1:
            result += 1

        current_stop = next_stop

    return result


stations = [0, 200, 375, 550, 750, 950]
capacity = 400
print(min_stops(stations, capacity))
