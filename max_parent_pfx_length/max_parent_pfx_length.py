#!/usr/bin/env python
"""
max_parent_pfx_length - Computes largest parent prefix length given child prefix length(s).

Usage:


* Import as a function

from max_parent_pfx_length import max_parent_pfx_len

max_parent_pfx_len([26,27,28,29])

max_parent_pfx_len([96,96,97,97], ipv6=True)


* From shell

- Provide one or more prefix lengths, separated by commas ","

$ ./max_parent_pfx_len prefix_lengths [-ipv6]

- Compute max prefix lengths for multiple lines of inputs stored in a file

$ cat ex_pfx_lengths_ipv4.txt | xargs -L 1 ./max_parent_pfx_len.py [-ipv6]

"""
import argparse
import sys

__author__ = "Przemek Rogala"


def max_parent_pfx_len(pfx_lengths, ipv6=False):
    """Computes largest parent prefix length given child prefix length(s).

    >>> max_parent_pfx_len([26,27,28,29])
    24

    :param pfx_lengths: iterable: prefix lengths
    :param ipv6: bool: set to False for IPv4 prefix lengths, True for IPv6
    :return: int: computed largest prefix length
    """
    if ipv6:
        BIT_SIZE = 128
    else:
        BIT_SIZE = 32

    try:
        pfx_lengths = [int(pl) for pl in pfx_lengths]
    # One of the inputs is not a number. Catch and re-raise.
    except ValueError:
        raise ValueError("Only numbers are accepted.")

    # It only makes sense for prefix lengths to be be between 1 < pfx_len <= BIT_SIZE
    if any(True for pl in pfx_lengths if pl < 1 or pl > BIT_SIZE):
        raise ValueError(
            "Prefix length has to be between 1 < 'pfx_len' <= {}".format(BIT_SIZE)
        )

    len_sum = 0
    for pfx_len in pfx_lengths:
        len_sum += 2 ** (BIT_SIZE - int(pfx_len))

    # Compute pfx len, sub 1 to adjust for sum equal to powers of 2
    # In Python2 we might overflow int into long so need to get type(len_sum)
    pfx_len_needed = BIT_SIZE - type(len_sum).bit_length(len_sum - 1)

    if pfx_len_needed < 0:
        raise ValueError("Input prefix lengths too large to compute parent length.")

    return pfx_len_needed


if __name__ == "__main__":
    try:
        # Accept one positional argument and one optional flag
        parser = argparse.ArgumentParser()
        parser.add_argument("prefix_lengths")
        parser.add_argument(
            "-ipv6",
            "--ipv6",
            action="store_true",
            help="sum the integers (default: find the max)",
        )
        args = parser.parse_args()

        # Split on commans
        in_pfxs_len = args.prefix_lengths.split(",")

        # Print resulting prefix length
        print(max_parent_pfx_len(in_pfxs_len, ipv6=args.ipv6))
    except ValueError as e:
        print(e)
        sys.exit(1)
