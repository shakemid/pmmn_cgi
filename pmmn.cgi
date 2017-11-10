#!/bin/sh

# pmmn cgi wrapper

basedir=${DOCUMENT_ROOT}/../opt/pmmn
plugin_dir=${basedir}/plugins
pmmn_cmd=${basedir}/bin/pmmn
export MUNIN_LIBDIR=${basedir}/lib

echo "Content-Type: text/plain"
echo

${pmmn_cmd} --plugin-dir=${plugin_dir} | egrep -v '^#|^\.$'
