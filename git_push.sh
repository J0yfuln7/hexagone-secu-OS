#!/bin/bash

read commit_msg
git add .
git commit -m $commit_msg
git push
