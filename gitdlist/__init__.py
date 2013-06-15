#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import subprocess
import tempfile

from colorama import init, deinit, Fore, Back

def _make_color(col):
    fgcol = getattr(Fore, col)
    return lambda s: fgcol + s + Fore.RESET


red = _make_color('RED')
cyan = _make_color('CYAN')
green = _make_color('GREEN')
yellow = _make_color('YELLOW')


ORIGIN = 'origin'


def main():
    init()
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('dir', default='.', nargs='?')
        args = parser.parse_args()

        for p in os.listdir(args.dir):
            if not os.path.isdir(p):
                continue
            path = os.path.abspath(os.path.join(args.dir, p))
            with tempfile.TemporaryFile() as tmp:
                try:
                    remotes = subprocess.check_output(
                        ['git', 'remote'],
                        cwd=path,
                        stderr=tmp,
                    ).split('\n')

                    if not ORIGIN in remotes:
                        print '%s: %s' % (
                            cyan(p), 'has no remote "%s"' % ORIGIN
                        )
                        continue

                    output = subprocess.check_output(
                    ['git', 'log', 'origin/master..HEAD', '--oneline'],
                    cwd=path,
                    stderr=tmp,
                    )
                except subprocess.CalledProcessError as e:
                    tmp.seek(0)
                    err = tmp.read()
                    print '%s: %s' % (red(p), err.split('\n')[0])
                else:
                    output = output.strip()
                    if output:
                        lines = output.split('\n')
                        print '%s: %s' % (
                            yellow(p), ('%d unpushed commits' % len(lines))
                        )
    finally:
        deinit()
