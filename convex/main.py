from convex.models.pos import process as pos_process
from convex.models.pos.model import POSNet
import os
import torch
from pathlib import Path

class PosTagger:
  def __init__(self):
    self.word, self.char, self.pos = pos_process.load_vocab()
    self.tagger = POSNet()
    pos_model = os.path.join(str(Path.home()), 'convex_resources', 'pos_model.pt')
    self.tagger.load_state_dict(torch.load(pos_model))

  def __call__(self, text):
    data = pos_process.POSWrapper(self.word, self.char, text)
    return list(zip(data.tokenized, self.tagger.tag(self.pos, data)[0]))
