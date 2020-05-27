#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    return_tuple = []
    not_cleaned_data = []

    for i in range(len(predictions)):
        return_tuple.append(ages[i])
        return_tuple.append(net_worths[i])
        return_tuple.append(abs(predictions[i]-net_worths[i]))
        not_cleaned_data.append(return_tuple)
        return_tuple = []

    for i in range(len(not_cleaned_data)):
        not_cleaned_data[i] = tuple(not_cleaned_data[i])


    for i in range(len(not_cleaned_data)):
        for j in range(len(not_cleaned_data)-i-1):
            if(not_cleaned_data[j][2] > not_cleaned_data[j+1][2]):
                temp = not_cleaned_data[j]
                not_cleaned_data[j] = not_cleaned_data[j+1]
                not_cleaned_data[j+1] = temp

    ### your code goes here

    cleaned_data = not_cleaned_data[:len(not_cleaned_data)-9]
    return cleaned_data

