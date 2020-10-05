# -*- coding: utf-8 -*-
"""
Computing the autocorrelation of a signal for a given lag
"""

import json
import logging.config


def config_logger():
    with open('configs\\corrLogs.json', 'r') as file:
        config = json.load(file)

    logging.config.dictConfig(config)


config_logger()
CORR_LOGGER = logging.getLogger(__name__)


def find_corr():
    """
    Main function to Check the balance, using the count of the opening and closing braces
    """

    signal = input('Please enter the signal separated by "," ')
    k = int(input('Please enter the lag value'))
    signal = signal.split(',')
    signal = list(map((lambda x: float(x)), signal))
    n = len(signal)
    if (k > n-2) or k < 1:
        CORR_LOGGER.error("K takes value between 1 and N-2")
        raise Exception("K takes value between 1 and N-2")
    mean = sum(signal)/n
    variance = sum(map((lambda x: (x - mean)**2), signal))
    autocorrelation = sum(((signal[i] - mean) * (signal[i+k] - mean) for i in range(n-k)))/variance
    CORR_LOGGER.info(f'The autocorrelation for given signal {signal} and lag: {k} is {autocorrelation}')


if __name__ == '__main__':
    find_corr()
