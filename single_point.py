work_class_values = ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov',
                     'Local-gov', 'State-gov', 'Without-pay', 'Never-worked', '?']

education_values = ['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school',
                    'Assoc-acdm', 'Assoc-voc', '9th', '7th-8th', '12th', 'Masters',
                    '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool', '?']

marital_status_values = ['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated',
                         'Widowed', 'Married-spouse-absent', 'Married-AF-spouse', '?']

occupation_values = ['Tech-support', 'Craft-repair', 'Other-service', 'Sales',
                     'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners',
                     'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing',
                     'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces', '?']

relationship_values = ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried', '?']

race_values = ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black', '?']

sex_values = ['Female', 'Male', '?']

native_country_values = ['United-States', 'Cambodia', 'England', 'Puerto-Rico',
                         'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)',
                         'India', 'Japan', 'Greece', 'South', 'China', 'Cuba',
                         'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland',
                         'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland',
                         'France', 'Dominican-Republic', 'Laos', 'Ecuador',
                         'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala',
                         'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia',
                         'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands', '?']


def parse(split_line_array):
    """ each line will be converted to the correct numeric value and will be inserted to a 1xM vector (x vector)
    """

    x = list()
    # Age
    x.append(float(split_line_array[0][1:]))
    # Work-class
    x.append(float(work_class_values.index(split_line_array[1])))
    # fnlwgt
    x.append(float(split_line_array[2]))
    # Education
    x.append(float(education_values.index(split_line_array[3])))
    # Education-num
    x.append(float(split_line_array[4]))
    # Martial-status
    x.append(float(marital_status_values.index(split_line_array[5])))
    # Occupation
    x.append(float(occupation_values.index(split_line_array[6])))
    # Relationship
    x.append(float(relationship_values.index(split_line_array[7])))
    # Race
    x.append(float(race_values.index(split_line_array[8])))
    # Sex
    x.append(float(sex_values.index(split_line_array[9])))
    # Capital-gain
    x.append(float(split_line_array[10]))
    # Capital-loss
    x.append(float(split_line_array[11]))
    # Hours-per-week
    x.append(float(split_line_array[12]))
    # Native-country
    x.append(float(native_country_values.index(split_line_array[13])))

    y_value = str(split_line_array[14])
    if y_value.__contains__('<=50K'):
        y_value = 0
    else:
        y_value = 1

    return x, y_value
