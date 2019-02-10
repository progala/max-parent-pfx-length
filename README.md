
# max_parent_pfx_length
Compute largest parent prefix length given child prefix length(s).



## Usage:


### Import as a function

>max_parent_pfx_len(pfx_lengths, ipv6=False)
> 
> 
>    :param pfx_lengths: iterable: prefix lengths
>    :param ipv6: bool: set to False for IPv4 prefix lengths, True for IPv6
>    :return: int: computed largest prefix length

Example:

    from max_parent_pfx_length import max_parent_pfx_len
    
    max_parent_pfx_len([26,27,28,29])
    
    max_parent_pfx_len([96,96,97,97], ipv6=True)


### Use from the command line

-  Provide one or more prefix lengths, separated by commas

> $ max_parent_pfx_length prefix_lengths [-ipv6]

- Compute max prefix lengths for multiple lines of inputs stored in a file

> $ cat ex_pfx_lengths_ipv4.txt | xargs -L 1 ./max_parent_pfx_length.py
> [-ipv6]

## References
Blog post with the implementation details: https://ttl255.com/compute-largest-summary-prefix-length-with-python/ 
