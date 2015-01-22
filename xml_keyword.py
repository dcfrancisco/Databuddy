#! /usr/bin/env python

"""Keywords (from "graminit.c")

This file is automatically generated; please don't muck it up!

To update the symbols in this file, 'cd' to the top directory of
the python source tree after building the interpreter and run:

    python Lib/keyword.py
"""

__all__ = ["iskeyword", "kwlist"]

kwlist = [
#--start keywords--
        'default',
        'table_utils',
        'param',
        'method',
		'worker',
		'etldataflow',
		'globals',	
		'test_spec',		
		'process_spec',
		'env',
		'connector',
		'log_root',
		'email_to',
		'prod',
		'dev',
		'copy_method','spool_method','clone_table', 'dml_method','query_spool_method','query_copy_method','publish_ddl','ddl_spool_method',
		'select_method',
		'prod',
		'uat',
		'qa', 'exec_copy', 'exec_select','sqlp','exec_dml','exec_spool',

#--end keywords--
        ]

iskeyword = frozenset(kwlist).__contains__

def main():
    import sys, re

    args = sys.argv[1:]
    iptfile = args and args[0] or "Python/graminit.c"
    if len(args) > 1: optfile = args[1]
    else: optfile = "xml_keyword.py"

    # scan the source file for keywords
    fp = open(iptfile)
    strprog = re.compile('"([^"]+)"')
    lines = []
    for line in fp:
        if '{1, "' in line:
            match = strprog.search(line)
            if match:
                lines.append("        '" + match.group(1) + "',\n")
    fp.close()
    lines.sort()

    # load the output skeleton from the target
    fp = open(optfile)
    format = fp.readlines()
    fp.close()

    # insert the lines of keywords
    try:
        start = format.index("#--start keywords--\n") + 1
        end = format.index("#--end keywords--\n")
        format[start:end] = lines
    except ValueError:
        sys.stderr.write("target does not contain format markers\n")
        sys.exit(1)

    # write the output file
    fp = open(optfile, 'w')
    fp.write(''.join(format))
    fp.close()

if __name__ == "__main__":
    main()
