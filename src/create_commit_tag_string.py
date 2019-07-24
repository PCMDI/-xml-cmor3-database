from __future__ import print_function
import sys
import argparse
import os
from subprocess import PIPE, Popen

p = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

p.add_argument("-s", "--svn", default="/svn/CMIP6dreq/trunk",
               help="path to Martin Jukes dreq repo")
p.add_argument("-c", "--cmor", help="cmor version", default="3.5.0")
p.add_argument("-t", "--tables", help="path to tables")
p.add_argument("-C", "--cv", help="path to CV repo")
p.add_argument("-g", "--git", help="root path to git repos", default="/git")


args = p.parse_args()


def get_tag(repo):
    p = Popen(["git", "describe", "--tags"], stdout=PIPE, stderr=PIPE,cwd=repo)
    o, e = p.communicate()
    return o.strip()



# Ok figure out CMIP6_CVs part
if args.cv is None:
    cv_repo = os.path.join(args.git, "CMIP6_CVs")
else:
    cv_repo = args.cv

cv_tag = get_tag(cv_repo).split("-")[0]

# Ok Dreq tag
svn_repo = args.svn
sys.path.insert(0,svn_repo)
import dreqPy
drs_tag = dreqPy.version

# CMOR
cmor_tag = args.cmor

print("CVs:",cv_tag)
print("DRS:", drs_tag)
print("CMOR:",cmor_tag)
print("COMMIT: CMIP6_CVs-{}/DREQ-{}/CMOR-{}".format(cv_tag,drs_tag,cmor_tag))