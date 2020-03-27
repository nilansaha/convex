## Convex

**A Light-weight and Fast Python NLP Library**

The plan is to provide light-weight neural models for various downstream NLP tasks such as POS Taggging, Named Entity Recognition, Sentiment Analysis, etc. However, right now POS Tagging is the only task that is supported.

### Installation

**pip**

`pip install convex`

**From Source**

```
git clone https://github.com/nilansaha/convex.git
cd convex
pip install -e .
```

### Usage

The model only needs to be downloaded the first time the tagger is used or after the package is updated

```python
import convex
convex.download() # Download all the necessary models
tagger = convex.PosTagger() # Initialize the Pos Tagging Pipeline
tagger("Let's see how this new tagger works.") # Tag a sentence
```

Output -

`[('Let', 'VERB'), ("'s", 'PRON'), ('see', 'VERB'), ('how', 'ADV'), ('well', 'ADV'), ('this', 'DET'), ('new', 'ADJ'), ('tagger', 'NOUN'), ('works', 'NOUN')]`




