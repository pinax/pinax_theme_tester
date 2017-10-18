#!/bin/bash

set -eu

# Declare arg variables for clarity.
INSTANCE=$1

ec --site=pinax/templates --instance="$1" deploy "$CIRCLE_SHA1"
