#!/bin/bash
for i in `adb devices | grep 'device\b' | awk '{print $1}'`
do
  echo $i
  udid=$i pytest -v E:/hogwarts/homework/appium_wework/wework_po/testcases/test_contact.py &
done
