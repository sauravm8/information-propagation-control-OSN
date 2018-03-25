#Loading the pickle files and finding the mean values and sorting them. Maybe even plotting them

import config
import logging
import pickle

#Finding the mean from a list of values in the list
def find_mean(list_of_values, number_of_weeks):

    #The average of the values can be asked to find out per n weeks(52 for per year, 4 for per month and so on
    list_of_means = []

    for i in range(0,len(list_of_values), number_of_weeks):

        try:
            sliced_list = list_of_values[i:(i+number_of_weeks)]
            average_value = sum(sliced_list)/ len(sliced_list)
            list_of_means.append(average_value)
        except:
            logging.info("There was inconsitency in the number of weeks")
            break
    return  list_of_means


# Loading the values from the pickle file
def load_pickle_file(pickle_file_path):
    with open(pickle_file_path, "rb") as fml:
        dict_users = pickle.load(fml)
    return dict_users



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    # Loading the values from the pickle file
    user_dictionary_values = load_pickle_file(config.PICKLE_FILE_INITIAL_VALUES)

    # Finding out the means of all the random values and store them in a list of average value of each user i a list of lists.
    list_of_average_values = []
    for i in range(config.NUMBER_OF_USERS):
        average_value_list = find_mean(user_dictionary_values[i], config.NUMBER_OF_WEEKS_AVERAGE)
        list_of_average_values.append(average_value_list)

    logging.info(sorted(list_of_average_values, reverse=True))

    # Saving them in a pickle file. After this, another code will read the pickle file and plot the graphs.
    with open(config.PICKLE_FILE_MEAN_VALUES, 'wb') as pickle_file:
        pickle.dump(list_of_average_values, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    logging.info("List of mean values saved in pickle file {}".format(config.PICKLE_FILE_MEAN_VALUES))
