#!/bin/bash
OUTPUT="Start"

assignment=$1
lowercase="$(echo $assignment | tr '[A-Z]' '[a-z]')"

while true; do
  OUTPUT=$(python3 ./src/PlaceCodeInProject.py $assignment)

  check=""

  if [ "$OUTPUT" == "${check}" ]; then
    echo Finished Running Unit Tests
    break
  fi

  check="Fix Error in File Location!"

  if [[ "$OUTPUT" == *"${check}" ]]; then
    echo $OUTPUT
    break
  fi

  echo $OUTPUT

  cd ../HW_Test

  echo Running Gradle
  gradle --rerun-tasks -Passignment=$lowercase > ../$assignment/counters/output.txt &

  PID2=$!
  count=0
  waittime=10
  while kill -0 $PID2 2> /dev/null; do
    sleep 1
    ((count++))
    if [ $count -gt $waittime ] ; then
      kill -TERM $PID2 2> /dev/null
      break
    fi
  done
  wait ${PID2}

  cd ../GradingScript228000

  OUTPUT=$(python3 ./src/GradleReader.py $assignment)

  check="Did not compile or pass tests"

  if [ "$OUTPUT" == "${check}" ]; then
    cd ../HW_Test
    gradle cleanEclipse -Passignment=$lowercase
    gradle eclipse -Passignment=$lowercase
    cd ../HW_Student
    gradle cleanEclipse
    gradle eclipse
    cd ../GradingScript228000
    echo $OUTPUT
    break
  fi
done
