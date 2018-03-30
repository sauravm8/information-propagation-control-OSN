import numpy as np
import config
import logging
import os
import matplotlib.pyplot as plt
import pickle


def plotting_data(data_points, iter_number, number_of_buckets, number_of_users, plotting_directory):
    x = range(number_of_users)
    plt.plot(x, data_points)
    plt.savefig(os.path.join(plotting_directory,"plot_iter{}_of_{}".format(str(iter_number), str(number_of_buckets))))
    plt.show()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
    logging.info("Entered plotting for file {}".format(config.FILE_TO_PLOT))

    # Loading pickle file
    plotting_ds = pickle.load(open(config.FILE_TO_PLOT, "rb"))
    print(plotting_ds)

    #Yearly is once, quarterly is 4 and so on.
    number_of_buckets = int(config.NUMBER_OF_WEEKS/config.NUMBER_OF_WEEKS_AVERAGE)

    for i in range(number_of_buckets):
        list_of_plot_points = []
        for j in range(config.NUMBER_OF_USERS):
            # The points to be plotted are appended  in the list
            list_of_plot_points.append(plotting_ds[j][i])

        #Sending the data points to be plotted
        plotting_data(sorted(list_of_plot_points, reverse=True), i, config.NUMBER_OF_WEEKS_AVERAGE, config.NUMBER_OF_USERS, config.PLOT_SAVE_DIRECTORY)
        logging.info("Sent the {}th iteration of {} iterations".format(str(i+1), str(number_of_buckets)))

