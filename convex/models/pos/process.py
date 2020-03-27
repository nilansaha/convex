import os
import dill
from pathlib import Path
from nltk.tokenize import word_tokenize

resource_dir = str(Path.home()) + '/convex_resources'

def load_vocab():
  with open(os.path.join(resource_dir, 'pos_word.field'), 'rb') as f:
    WORD = dill.loads(f.read())

  with open(os.path.join(resource_dir, 'pos_char.Field'), 'rb') as f:
    CHAR = dill.loads(f.read())

  with open(os.path.join(resource_dir, 'pos_pos.Field'), 'rb') as f:
    POS = dill.loads(f.read())

  return WORD, CHAR, POS

class POSWrapper:
  def __init__(self, WORD, CHAR, text):
    self.tokenized = word_tokenize(text)
    self.word = WORD.process([self.tokenized])
    self.char = CHAR.process([self.tokenized])
 
  def __iter__(self):
    yield self

