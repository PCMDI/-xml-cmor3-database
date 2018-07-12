#!/bin/bash
echo "ARGS: $1"
export CMIP6dreq_path=${1:-"/svn/CMIP6dreq/trunk"}
echo "Copying from: ${CMIP6dreq_path}"
pushd ${CMIP6dreq_path}
svn update
popd
cp ../docs/dreq.xml ../docs/dreq.xml.old
cp ../docs/vocab.xml ../docs/vocab.xml.old
cp ${CMIP6dreq_path}/dreqPy/docs/dreq.xml ../docs
cp ${CMIP6dreq_path}/dreqPy/docs/vocab.xml ../docs
cp ${CMIP6dreq_path}/dreqPy/packageConfig.py .

