#!/bin/bash
# This script runs the optimization of tensorflow and theano backend separately and write the result to files.
# Then check if the difference between the results are within threshold
#
# Arguments:
# --formula: Name of formula (curve) on which optimization is run. See formula.py for the list of valid formulas.
# --optimizer: Name of optimizer configurations. See optimizer directory for the list of valid configurations.

set -e

while [[ $# -gt 0 ]]
do
    key="$1"
    case $key in
        --optimizer)
            OPTIMIZER="$2"
            shift
            ;;
        --formula)
            FORMULA="$2"
            shift
            ;;
        --iterations)
            ITERATIONS="$2"
            shift
            ;;
        --threshold)
            THRESHOLD="$2"
            shift
            ;;
        *)
            echo "Unexpected option ${key} was given"
            exit 1
            ;;
    esac
    shift
done

if [[ -z "${FORMULA}" || -z "${OPTIMIZER}" ]]; then
    echo "--formula and --optimizer must be given"
    exit 1
fi
ITERATIONS=${ITERATIONS-1000}
THRESHOLD=${THRESHOLD-0.005}

FILE1="tmp/${FORMULA}_${OPTIMIZER}_theano.csv"
FILE2="tmp/${FORMULA}_${OPTIMIZER}_tensorflow.csv"

BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TEST_COMMAND="python ${BASE_DIR}/run_optimizer.py ${FORMULA} ${OPTIMIZER}"
COMPARE_COMMAND="python ${BASE_DIR}/compare_result.py"

LUCHADOR_NN_BACKEND=theano     LUCHADOR_NN_CONV_FORMAT=NCHW ${TEST_COMMAND} --output ${FILE1} --iterations ${ITERATIONS}
LUCHADOR_NN_BACKEND=tensorflow LUCHADOR_NN_CONV_FORMAT=NHWC ${TEST_COMMAND} --output ${FILE2} --iterations ${ITERATIONS}
${COMPARE_COMMAND} $FILE1 $FILE2 --threshold ${THRESHOLD}

rm $FILE1 $FILE2