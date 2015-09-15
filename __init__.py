#! /usr/bin/env python
# coding=utf-8

import os.path
import subprocess


class Task(object):
    title = "Zlib library"
    version = 1
    arguments = [
        {"name": "prefix", "type": "text", "title": "Install directory prefix (used for configure script)"},
        {"name": "bit64", "type": "bool", "title": "Support for 64 bit"}
    ]
    refs = {
        "tcc": "compile.tcc"
    }

    @staticmethod
    def setup(srcdir):
        print "__setup__"
        retcode = subprocess.call(['git', 'clone', 'https://github.com/lugovskoy/dts-sample-project.git', srcdir])
        return
        if retcode != 0:
            raise Exception("Cannot setup git repo in {0}".format(srcdir))


    def __init__(self):
        print "proj::__init__"
        self.__wd = os.path.dirname(os.path.realpath(__file__))
        os.chdir(self.__wd)
        retcode = subprocess.call(['wget', 'http://zlib.net/zlib-1.2.8.tar.gz'])
        retcode = subprocess.call(['tar', 'xvzf', 'zlib-1.2.8.tar.gz'])


    def __call__(self, args, refs, resdir, q):
        print "proj::__call__"
        zlib_srcdir = os.path.join(self.__wd, 'zlib-1.2.8')
        zlib_resdir = os.path.join(resdir, 'opt2')

        os.chdir(zlib_srcdir)
        retcode = subprocess.call(['./configure', '--prefix={0}'.format(zlib_resdir)], env={'CC': refs['tcc']})
        retcode = subprocess.call(['make'])
        retcode = subprocess.call(['make', 'install'])
        q.put({'zlib': os.path.join(zlib_resdir, 'bin')})



