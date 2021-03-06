from os import path, makedirs

from opennmt.runner import Runner
import tensorflow as tf

from bot.text_processor.setup import config, model


def train():
    """
    Trains the OpenNMT model without evaluation.
    """
    tf.logging.set_verbosity(tf.logging.INFO)
    runner = Runner(model, config)
    runner.train()
