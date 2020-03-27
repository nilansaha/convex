import torch
import torch.nn as nn
from torch.nn.functional import log_softmax, relu
from torch.optim import Adam, SGD

EMBEDDING_DIM = 300
CHAR_EMBEDDING_DIM = 100
RNN_HIDDEN_DIM = 50
RNN_LAYERS = 1

class POSNet(nn.Module):
    def __init__(self):
        super(POSNet,self).__init__()
        self.tagset_size = 19
        self.embeddings = nn.Embedding(num_embeddings = 19676, embedding_dim = EMBEDDING_DIM)
        self.lstm = nn.LSTM(input_size = EMBEDDING_DIM + (CHAR_EMBEDDING_DIM * 2), hidden_size = RNN_HIDDEN_DIM, num_layers = RNN_LAYERS, bidirectional = True)
        self.char_lstm = nn.LSTM(CHAR_EMBEDDING_DIM, 100,1, bidirectional = True)
        self.char_embedding = nn.Embedding(num_embeddings = 112, embedding_dim = CHAR_EMBEDDING_DIM)
        self.linear1 = nn.Linear(2*RNN_HIDDEN_DIM, 2*RNN_HIDDEN_DIM)
        self.linear2 = nn.Linear(2*RNN_HIDDEN_DIM, self.tagset_size)
        self.relu = nn.ReLU()
        self.log_softmax = nn.LogSoftmax(dim=2)

    def forward(self, ex):
        embedded = self.embeddings(ex.word)
        char_emb = self.char_embedding(ex.char[0][0])
        char_emb = char_emb.permute(1, 0, 2)
        output, (hidden, cell) = self.char_lstm(char_emb)
        hidden = torch.cat((hidden[0], hidden[1]), dim = 1).unsqueeze(0)
        hidden = hidden.permute(1, 0, 2)
        combined_emb = torch.cat((embedded, hidden), dim = 2)
        out, _ = self.lstm(combined_emb)
        out = out[1:-1]
        out = self.linear1(out)
        out = self.relu(out)
        out = self.linear2(out)
        out = self.log_softmax(out)
        return out

    def tag(self, POS, data):
        with torch.no_grad():
            results = []
            for ex in data:
                tags = self(ex).argmax(dim=2).squeeze(1)
                results.append([POS.vocab.itos[i] for i in tags])
            return results
