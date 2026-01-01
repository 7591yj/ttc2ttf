#!/bin/bash
for f in *.ttf; do fonttools ttLib.woff2 compress "$f"; done
