# -*- coding: utf-8 -*-
"""Balance Checker

This script allows the user to check if the braces in the given string are balanced
The braces could be (), {}, [] or any combination of these

This file contains the following function:

    * main - the main function of the script
"""


import json
import logging.config


def config_logger():
    with open('configs\\check.json', 'r') as file:
        config = json.load(file)

    logging.config.dictConfig(config)


config_logger()
BALANCE_LOGGER = logging.getLogger(__name__)


def check():
    """
    Main function to Check the balance, using the count of the opening and closing braces
    """

    string = input('Please enter the string:\n')
    stack = []
    open_bracket = ['(', '[', '{']
    close_bracket = [')', ']', '}']
    for char in string:
        if char in open_bracket:
            stack.append(char)
        elif char in close_bracket:
            if ((len(stack) > 0) and
                    open_bracket[close_bracket.index(char)] == stack[-1]):
                stack.pop()
            else:
                BALANCE_LOGGER.info("UNBALANCED")
                return
        else:
            continue

    if len(stack) == 0:
        BALANCE_LOGGER.info("BALANCED")
    else:
        BALANCE_LOGGER.info("UNBALANCED")


if __name__ == '__main__':
    check()
