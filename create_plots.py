# -*- coding: utf-8 -*-
"""
    MEC_offloading.create_plots
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Creating plots for the MEC_offloading

    :copyright: (c) 2018 by Giorgos Mitsis.
    :license: MIT License, see LICENSE for more details.
"""

import numpy as np
import matplotlib.pyplot as plt

from parameters import *
from plots import *

import itertools
import dill


def create_plots(results, cases, params):
    '''
    Create all the plots

    Parameters
    ----------

    results: dictionary of dictionaries
        Each key of the dictionary corresponds to one case and the value is the
        dictionary containing all the results
    cases: list of dictionaries
        The elements of the list are the cases
    params: dictionary
        Dictonary of the parameters

    Returns
    -------

    Plots
    '''

    for case in cases:

        key = case["users"] + "_" + case["servers"]

        if ONE_FIGURE == True:
            plt.figure(figsize=(40.0, 30.0))
            plt.subplot(4,4,1)
            plot_data_offloading_of_users(results[key]['all_bytes_offloaded'])
            plt.subplot(4,4,2)
            plot_num_of_users_on_each_server(results[key]['all_server_selected'], **params)
            plt.subplot(4,4,3)
            plot_pricing_of_each_server(results[key]['all_prices'])
            plt.subplot(4,4,4)
            plot_receiving_data_on_each_server(results[key]['all_bytes_to_server'])
            plt.subplot(4,4,5)
            plot_server_welfare(results[key]['all_server_welfare'])
            plt.subplot(4,4,6)
            plot_server_Rs(results[key]['all_Rs'])
            plt.subplot(4,4,7)
            plot_server_congestion(results[key]['all_congestion'])
            plt.subplot(4,4,8)
            plot_server_penetration(results[key]['all_penetration'])
            plt.subplot(4,4,9)
            plot_server_discount(results[key]['all_fs'])
            plt.subplot(4,4,10)
            plot_server_cost(results[key]['all_c'])
            plt.subplot(4,4,11)
            plot_server_relative_price(results[key]['all_relative_price'])
        else:
            plot_data_offloading_of_users(results[key]['all_bytes_offloaded'])
            plot_num_of_users_on_each_server(results[key]['all_server_selected'], **params)
            plot_pricing_of_each_server(results[key]['all_prices'])
            plot_receiving_data_on_each_server(results[key]['all_bytes_to_server'])
            plot_server_welfare(results[key]['all_server_welfare'])
            plot_server_Rs(results[key]['all_Rs'])
            plot_server_congestion(results[key]['all_congestion'])
            plot_server_penetration(results[key]['all_penetration'])
            plot_server_discount(results[key]['all_fs'])
            plot_server_cost(results[key]['all_c'])
            plot_server_relative_price(results[key]['all_relative_price'])

        # for user in range(U):
        #     plot_user_probability_to_select_server(user, all_probabilities)

        # Go to parameters.py to change the setting
        if SAVE_FIGS == False:
            plt.show(block=False)
        if SAVE_FIGS == True and ONE_FIGURE == True:
            plt.savefig("plots/" + case["users"] + "_" + case["servers"] + ".png")

    # to keep the plots visible after run
    if ONE_FIGURE == True and SAVE_FIGS == False:
        plt.show()

if __name__ == '__main__':
    # Generate all cases
    cases_setup = {
            'users': ['homo','hetero'],
            'servers': ['homo','hetero','one-dominant','two-dominant']
            }

    keys, values = zip(*cases_setup.items())

    # Select which case to run
    # cases = [{"users": "hetero", "servers": "hetero"}]
    cases = [dict(zip(keys, v)) for v in itertools.product(*values)]

    results = {}
    for case in cases:

        infile = "saved_runs/saved_parameters_" + case["users"] + "_" + case["servers"]
        with open(infile, 'rb') as in_strm:
            params = dill.load(in_strm)

        infile = "saved_runs/results_" + case["users"] + "_" + case["servers"]
        with open(infile, 'rb') as in_strm:
            key = case["users"] + "_" + case["servers"]
            results[key] = dill.load(in_strm)

    create_plots(results, cases, params)
