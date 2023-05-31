#!/bin/bash

echo
echo =**GitHelper by Efendo**=
echo
git add $1
git commit -m $2
git push
echo GitHelper: pushed $1 with message $2
echo