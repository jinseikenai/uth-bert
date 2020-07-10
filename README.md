# UTH-BERT
This site provides source code for pre-processing text and tokenization for use of UTH-BERT.<br>

1. BERT: Bidirectional Encoder Representations from Transformers.<br>
https://github.com/google-research/bert<br>

2. UTH-BERT
https://ai-health.m.u-tokyo.ac.jp/uth-bert<br>

## Quick setup of morphological analyzer

### 1. Install Mecab on Ubuntu 

sudo apt install mecab<br>
sudo apt install libmecab-dev<br>
sudo apt install mecab-ipadic-utf8<br>

### 2. Install mecab-ipadic-neologd (general dictionary for Mecab)

git clone https://github.com/neologd/mecab-ipadic-neologd.git<br>
cd mecab-ipadic-neologd<br>
sudo bin/install-mecab-ipadic-neologd<br>

Edit /etc/mecabrc<br>
dicdir = /usr/lib/mecab/dic/mecab-ipadic-neologd<br>

###  3. Download J-Medic (medical dictionary for Mecab)

[MANBYO_201907_Dic-utf8.dic](http://sociocom.jp/~data/2018-manbyo/index.html)

## Pre-processing text

Japanese text includes two-byte full-width characters (mainly Kanji, Hiragana, or Katakana) and one-byte half-width characters (mainly ASCII characters). We applied the Normalization Form Compatibility Composition (NFKC) followed by full-width characterization to all characters as a pre-processing.<br>

See [preprocess_text.py](https://github.com/jinseikenai/uth-bert/blob/master/preprocess_text.py) for details<br>
 
## Tokenization

