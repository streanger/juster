Juster
===========
Script for justification text with newlines and delimiters

Install
===========

.. code-block:: python

    pip install juster

Usage
===========

.. code-block:: python

    from juster import justify

    print(justify.__doc__)
    data = "some;thing;here\nvery;next;line"
    out = justify(data)
    print(out)


- 'justify' function parameters:

    - content - text with newlines and delimiters, to be converted. From version 0.1.2 it also can be list(tuple) of lists(tuples)

    - grid - True/False value, grid inside; default is True

    - frame - True/False value, frame around; default is False

    - enumerator - True/False value, will add enumerator column on the left

    - header - True/False value, will extract first row from content as header

    - topbar - str value. Topbar will be added on the top

    - newline - newline symbol; default is '\\n'

    - delimiter - delimiter symbol; default is ';'

    - justsize - justify size; default is 4
    
Example
===========

.. code-block:: python

    from juster import example
    
    example()
