import statistics

from single_point import parse


def parse_data(data_file_full_path):
    """ This method parses the data into the final matrix [M x N] - called X matrix.
        and Nx1 vector of classifier results - Y vector.
    """

    final_x_matrix = list()
    final_y_vector = list()

    try:

        data_file = open(data_file_full_path)
        for line in data_file:
            split_line = line.split(', ')

            if split_line.__contains__("?"):
                x_value, y_value = parse(split_line)

                # Adding median as a feature
                x_value.append(statistics.median(x_value))

                # Adding mean as a feature
                x_value.append(statistics.mean(x_value))

                # Adding variance as a feature
                x_value.append(statistics.variance(x_value))

                final_x_matrix.append(x_value)
                final_y_vector.append(y_value)




    except Exception as err:
        print("Error: ", err)


    finally:
        return final_x_matrix, final_y_vector

# parse_data("data/adult.data")
