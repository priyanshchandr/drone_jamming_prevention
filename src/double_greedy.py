def double_greedy(drones, channels, predicted_jamming):
    """
    Double Greedy Algorithm for channel allocation.
    :param drones: List of drones.
    :param channels: List of channels.
    :param predicted_jamming: Dict of channel jamming likelihood.
    :return: Allocated channels for each drone.
    """
    allocation = {}
    selected_channels = set()
    remaining_channels = set(channels)

    for drone in drones:
        best_channel = None
        best_score = float('inf')  # Minimize jamming likelihood

        # Greedily add channels
        for channel in remaining_channels:
            if predicted_jamming[channel] < best_score:
                best_channel = channel
                best_score = predicted_jamming[channel]

        # Assign best channel
        if best_channel is not None:
            allocation[drone] = best_channel
            selected_channels.add(best_channel)
            remaining_channels.remove(best_channel)

    return allocation
