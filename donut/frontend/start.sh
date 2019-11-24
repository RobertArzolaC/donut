#!/bin/bash

set -eu

echo "Installing dependancies: needed for development and IDE integrations"
npm install

echo "Starting audit"
npm audit fix

echo "Starting server"
npm start
