#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse


def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('patched_file',
                        type=argparse.FileType('r+b'),
                        help='file that will be patched',
                        )
    parser.add_argument('patch_data_file',
                        type=argparse.FileType('rb'),
                        help='file with patch data',
                        )
    parser.add_argument('-o', '--offset',
                        type=int,
                        default=0,
                        required=False,
                        help='Offset where patch will be applied. '
                        '0 by default (mean begining of file).',
                        )
    parser.add_argument('-p', '--portion-size',
                        type=int,
                        default=1024,
                        required=False,
                        help='Data from patch_data_file will be read by '
                        'portions. This option specify the portion size '
                        'in bytes. 1024 by default',
                        )
    return parser.parse_args()


def main():
    args = get_arg_parser()
    args.patched_file.seek(args.offset)

    while True:
        replace_data = args.patch_data_file.read(args.portion_size)
        if replace_data:
            args.patched_file.write(replace_data)
        else:
            break
    args.patched_file.close()
    return 0


if __name__ == '__main__':
    main()
