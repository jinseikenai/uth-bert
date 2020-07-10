# UTH-BERT
This site provides source code for pre-processing text and tokenization for use of UTH-BERT.

1. BERT: Bidirectional Encoder Representations from Transformers.
https://github.com/google-research/bert

2. UTH-BERT
https://ai-health.m.u-tokyo.ac.jp/uth-bert

## Quick setup morphological analyzer

# 1. Install Mecab on Ubuntu 

sudo apt install mecab
sudo apt install libmecab-dev
sudo apt install mecab-ipadic-utf8

# 2. Install mecab-ipadic-neologd (general dictionary for Mecab)

git clone https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
sudo bin/install-mecab-ipadic-neologd

Edit /etc/mecabrc
dicdir = /usr/lib/mecab/dic/mecab-ipadic-neologd

#  3. Download J-Medic (medical dictionary for Mecab)

[MANBYO_201907_Dic-utf8.dic](http://sociocom.jp/~data/2018-manbyo/index.html)

## Pre-processing text

Japanese text includes two-byte full-width characters (mainly Kanji, Hiragana, or Katakana) and one-byte half-width characters (mainly ASCII characters). We applied the Normalization Form Compatibility Composition (NFKC) followed by full-width characterization to all characters as a pre-processing.

See [preprocess_text.py](https://github.com/jinseikenai/uth-bert/blob/master/preprocess_text.py) for details
 
## Tokenization

