def calculate_error_percentage(y_vector, predicted_y_vector):
    """Gets a vector y of results, and vector y_prediction of predictions, compares, and calculates error percentage
    """

    # Make sure both vectors are of the same size
    assert(y_vector.__len__() == predicted_y_vector.__len__())

    # Calculate how many errors occured
    error_count = 0
    total_samples = y_vector.__len__()
    for i in range(0, total_samples):
        if y_vector[i] != predicted_y_vector[i]:
            error_count += 1

    # Return error percentage
    return (float(error_count) / total_samples) * 100

