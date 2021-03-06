"""
Birthdate corpus preprocessing script

Usage:
    preprocess.py
    preprocess.py -h | --help | --version

Options:
  -h --help             Show this screen
  --version             Version number
"""
import logging

from docopt import docopt

import iepy
iepy.setup(__file__)
from iepy.data.db import DocumentManager
from iepy.preprocess.stanford_preprocess import StanfordPreprocess
from iepy.preprocess.pipeline import PreProcessPipeline
from iepy.preprocess.segmenter import SyntacticSegmenterRunner


if __name__ == '__main__':
    logger = logging.getLogger(u'preprocess')
    logger.setLevel(logging.INFO)
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    opts = docopt(__doc__, version=iepy.__version__)
    docs = DocumentManager()
    pipeline = PreProcessPipeline([
        StanfordPreprocess(),
        SyntacticSegmenterRunner(increment=True)
    ], docs)
    pipeline.process_everything()
