#!/usr/bin/env python3
# Copyright 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
"""Interactive interface to full DrQA pipeline."""

import torch
import argparse
import code
#import prettytable
#import logging

from termcolor import colored
from drqa import pipeline
from drqa.retriever import utils

from flask import Flask , request
app = Flask(__name__)





#logger = logging.getLogger()
#logger.setLevel(logging.INFO)
#fmt = logging.Formatter('%(asctime)s: [ %(message)s ]', '%m/%d/%Y %I:%M:%S %p')
#console = logging.StreamHandler()
#console.setFormatter(fmt)
#logger.addHandler(console)
#
#parser = argparse.ArgumentParser()
#parser.add_argument('--reader-model', type=str, default=None,
#                    help='Path to trained Document Reader model')
#parser.add_argument('--retriever-model', type=str, default=None,
#                    help='Path to Document Retriever model (tfidf)')
#parser.add_argument('--doc-db', type=str, default=None,
#                    help='Path to Document DB')
#parser.add_argument('--tokenizer', type=str, default=None,
#                    help=("String option specifying tokenizer type to "
#                          "use (e.g. 'corenlp')"))
#parser.add_argument('--candidate-file', type=str, default=None,
#                    help=("List of candidates to restrict predictions to, "
#                          "one candidate per line"))
#parser.add_argument('--no-cuda', action='store_true',
#                    help="Use CPU only")
#parser.add_argument('--gpu', type=int, default=-1,
#                    help="Specify GPU device id to use")
#args = parser.parse_args()

'''
args.cuda = not args.no_cuda and torch.cuda.is_available()
if args.cuda:
    torch.cuda.set_device(args.gpu)
    logger.info('CUDA enabled (GPU %d)' % args.gpu)
else:
    logger.info('Running on CPU only.')

if args.candidate_file:
    logger.info('Loading candidates from %s' % args.candidate_file)
    candidates = set()
    with open(args.candidate_file) as f:
        for line in f:
            line = utils.normalize(line.strip()).lower()
            candidates.add(line)
    logger.info('Loaded %d candidates.' % len(candidates))
else:
    candidates = None

'''
@app.route('/get_query',methods=['GET'])
def process():
    #DrQA = pipeline.DrQA()
    req=request.args
    question=req['query']
    #DrQA = pipeline.DrQA()
    predictions = DrQA.process(
        question, candidates=None, top_n=1, n_docs=3, return_context=True
    )
    print(predictions[0]['span'])
    return predictions[0]['span']


if __name__ == '__main__':
    
    DrQA = pipeline.DrQA() 
    app.run(host='0.0.0.0',debug=True)
    
