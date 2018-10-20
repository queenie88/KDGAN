from utils import *

from os import path

import argparse
import os
import pickle

import logging
logging.basicConfig(level=logging.INFO, format=log_format)

def main(url_fold_file):
  image_fold_dir = url_fold_file.replace('url_fold', 'image_fold')
  print(image_fold_dir)
  with open(url_fold_file) as fin:
    for line in fin.readlines():
      image_url = line.strip()
      print(image_url)
      break

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('url_fold_file', type=str)
  args = parser.parse_args()
  main(args.url_fold_file)