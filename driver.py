import logging
import config
import random
import pickle

#Function to initialize the dictionary which will hold the values of all the users in list format for all weeks
def init_dict(users):
    user_dict = {}
    for i in range(users):
        user_dict[i] = []

    return user_dict

#Creates random list for the number of users.
def random_generator(users, range_start, range_end):
    random_list = []
    for i in range(users):
        random_number = random.randint(range_start, range_end)
        random_list.append(random_number)

    return random_list

#Updates all the values in the dictonary with the new values
def update_dict(user_dict, random_list):
    for k in list(user_dict.keys()):
        user_dict[k].append(random_list[k])
    return user_dict

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
    user_dictionary = init_dict(config.NUMBER_OF_USERS)
    logging.info("Dictionary is initialized")
    for i in range(config.NUMBER_OF_WEEKS):
        random_list = random_generator(config.NUMBER_OF_USERS, config.RANDOM_START, config.RANDOM_END)
        logging.info("The random values for week {} is generated".format(i+1))
        user_dictionary = update_dict(user_dictionary, random_list)
        logging.info("Dictionary updated with values for week {}".format(i+1))

    logging.info("Values for {} weeks have been generated".format(config.NUMBER_OF_WEEKS))

    pickle.dump(user_dictionary, open(config.PICKLE_FILE_INITIAL_VALUES, "wb"))

    logging.info("Dictionary saved as pickle file {}".format(config.PICKLE_FILE_INITIAL_VALUES))



