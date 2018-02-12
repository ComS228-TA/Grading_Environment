#!/bin/sh

assignment=$1

echo "Creating Folders for $assignment"

cd ..
mkdir $assignment
cp -R ./GradingScript228000/json_attributes ./$assignment/

cd $assignment
mkdir counters
touch counters/output.txt
folder="_Submissions"
folder=$assignment$folder
mkdir $folder

cd ..
rm -r ./HW_Student/src/main/java/edu/iastate/cs228/*
rm -r ./HW_Test/src/main/java/edu/iastate/cs228/*

lowercase="$(echo $assignment | tr '[A-Z]' '[a-z]')"

mkdir ./HW_Student/src/main/java/edu/iastate/cs228/$lowercase
mkdir ./HW_Test/src/main/java/edu/iastate/cs228/$lowercase
