'''
Plot functions to graphically present simulation results
'''

import numpy as np
import matplotlib.pyplot as plt

from parameters import *

server_names = ['server 1', 'server 2', 'server 3',
                'server 4', 'server 5']

color_sequence = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c']

def setup_plots(suptitle):
    '''
    Basic setup of plots so it can be reused on plot functions

    Parameters
    ----------

    suptitle: string
        Description of the plot that will appear on the top

    Returns
    -------
    Figure and axis matplotlib structs

    '''
    fig, ax = plt.subplots(1, 1, figsize=(12, 9))
    fig.suptitle(suptitle)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Provide tick lines across the plot to help viewers trace along
    # the axis ticks.
    plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)

    # Remove the tick marks; they are unnecessary with the tick lines we just
    # plotted.
    plt.tick_params(axis='both', which='both', bottom=True, top=False,
                    labelbottom=True, left=False, right=False, labelleft=True)

    return fig, ax

def plot_num_of_users_on_each_server(all_server_selected):
    '''
    Plot number of users on each server every timeslot

    Parameters
    ----------

    all_server_selected: 2-d array
        Contains on each row the server each user has selected. Each row is
        a different timeslot

    Returns
    -------
    Plot

    '''
    # How many users each server has each timeslot
    result = np.empty((0, S), int)
    for row in all_server_selected:
        # the bincount finds how many times each server has been selected
        result = np.append(result, [np.bincount(row, minlength=S)], axis=0)

    # Each row on the transposed matrix contains how many users the server has
    # in each timeslot. Different rows mean different servers.
    result = np.transpose(result)

    suptitle = 'Number of users each server has in each timeslot'
    fig, ax = setup_plots(suptitle)

    y_offsets = {}

    for index, row in enumerate(result):

        line = plt.plot(row, lw=2.5, color=color_sequence[index])

        # set the text to start on the y of the last value of the line
        y_pos = row[-1]

        server_name = server_names[index]
        # move based on offset if names overlap on plot
        if server_name in y_offsets:
            y_pos += y_offsets[server_name]

        plt.text(len(row) + 5, y_pos, server_name, fontsize=14, color=color_sequence[index])

    plt.xlabel('iterations')
    plt.ylabel('num of users')
    plt.show(block=False)

def plot_pricing_of_each_server(all_prices):
    '''
    Plot pricing of each server on every timeslot

    Parameters
    ----------

    all_prices: 2-d array
        Contains on each row the price each server has chosen. Each row is
        a different timeslot

    Returns
    -------
    Plot

    '''
    result = all_prices

    # Each row on the transposed matrix contains the price the server has
    # in each timeslot. Different rows mean different servers.
    result = np.transpose(result)

    suptitle = 'Price each server has selected in each timeslot'
    fig, ax = setup_plots(suptitle)

    y_offsets = {}

    for index, row in enumerate(result):

        line = plt.plot(row, lw=2.5, color=color_sequence[index])

        # set the text to start on the y of the last value of the line
        y_pos = row[-1]
        server_name = server_names[index]
        # move based on offset if names overlap on plot
        if server_name in y_offsets:
            y_pos += y_offsets[server_name]

        plt.text(len(row) + 5, y_pos, server_name, fontsize=14, color=color_sequence[index])

    plt.xlabel('iterations')
    plt.ylabel('price')
    plt.show(block=False)

def plot_receiving_data_on_each_server(all_bytes_to_server):
    '''
    Plot the data each server is receiving in each timeslot

    Parameters
    ----------

    all_bytes_to_server: 2-d array
        Contains on each row the amount of data each server is receiving. Each row is
        a different timeslot

    Returns
    -------
    Plot

    '''
    result = all_bytes_to_server

    # Each row on the transposed matrix contains the data the server receives
    # in each timeslot. Different rows mean different servers.
    result = np.transpose(result)

    suptitle = 'Data each server is receiving in each timeslot'
    fig, ax = setup_plots(suptitle)

    y_offsets = {}

    for index, row in enumerate(result):

        line = plt.plot(row, lw=2.5, color=color_sequence[index])

        # set the text to start on the y of the last value of the line
        y_pos = row[-1]
        server_name = server_names[index]
        # move based on offset if names overlap on plot
        if server_name in y_offsets:
            y_pos += y_offsets[server_name]

        plt.text(len(row) + 5, y_pos, server_name, fontsize=14, color=color_sequence[index])

    plt.xlabel('iterations')
    plt.ylabel('amount of data (bytes)')
    plt.show(block=False)

def plot_data_offloading_of_users(all_bytes_offloaded):
    '''
    Plot the data each user is offloading in each timeslot

    Parameters
    ----------

    all_bytes_offloaded: 2-d array
        Contains on each row the amount of data each user is offloading. Each row is
        a different timeslot

    Returns
    -------
    Plot

    '''
    result = all_bytes_offloaded

    # Each row on the transposed matrix contains the data the user offloads
    # in each timeslot. Different rows mean different user.
    result = np.transpose(result)

    suptitle = 'Data each user is offloading in each timeslot'
    fig, ax = setup_plots(suptitle)

    y_offsets = {}

    for index, row in enumerate(result):

        line = plt.plot(row, lw=2.5)

    plt.xlabel('iterations')
    plt.ylabel('amount of data (bytes)')
    plt.show(block=False)