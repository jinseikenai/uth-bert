# Pre-processing text and tokenization for UTH-BERT
This site provides source code for pre-processing text and tokenization for use of UTH-BERT.<br>

1. BERT: Bidirectional Encoder Representations from Transformers.<br>
https://github.com/google-research/bert<br>

2. UTH-BERT<br>
https://ai-health.m.u-tokyo.ac.jp/uth-bert<br>

3. Pre-print (medRxiv)<br>
A clinical specific BERT developed with huge size of Japanese clinical narrative<br>
https://doi.org/10.1101/2020.07.07.20148585<br>

## 1. Quick setup

### 1-1. Install [Mecab](https://taku910.github.io/mecab/) (Japanese morphological analyzer) on Ubuntu 

`sudo apt install mecab`<br>
`sudo apt install libmecab-dev`<br>
`sudo apt install mecab-ipadic-utf8`<br>

### 1-2. Install [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd) (general dictionary for Mecab)

`git clone https://github.com/neologd/mecab-ipadic-neologd.git`<br>
`cd mecab-ipadic-neologd`<br>
`sudo bin/install-mecab-ipadic-neologd -n -a`<br>

#### Edit /etc/mecabrc<br>
dicdir = /usr/lib/mecab/dic/mecab-ipadic-neologd<br>

### 1-3. Download [J-Medic](http://sociocom.jp/~data/2018-manbyo/index.html) (medical dictionary for Mecab)

You can download `MANBYO_201907_Dic-utf8.dic` from below URL.<br>
http://sociocom.jp/~data/2018-manbyo/index.html<br>

## 2. Pre-processing text

Japanese text includes two-byte full-width characters (mainly Kanji, Hiragana, or Katakana) and one-byte half-width characters (mainly ASCII characters). We applied the Normalization Form Compatibility Composition (NFKC) followed by full-width characterization to all characters as a pre-processing.<br>

See [preprocess_text.py](https://github.com/jinseikenai/uth-bert/blob/master/preprocess_text.py) for details<br>
 
## 3. Tokenization

In non-segmented languages such as Japanese or Chinese, a tokenizer must accurately identify every word in a sentence before attempt to parse it and to do that requires a method of finding word boundaries without the aid of word delimiters. MecabTokenizer and FullTokenizerForMecab that segment a word unit into several pieces of tokens included in BERT vocabulary.

See [tokenization_mod.py](https://github.com/jinseikenai/uth-bert/blob/master/tokenization_mod.py) for details<br>

## 4. Example

### Original text

> 2002 年夏より重い物の持ち上げが困難になり，階段の昇りが遅くなるなど四肢の筋力低下が緩徐に進行した．2005 年 2 月頃より鼻声となりろれつが回りにくくなった．また，食事中にむせるようになり，同年 12 月に当院に精査入院した。

> (English) Since the summer of 2002, there has been difficulty in lifting heavy objects and muscle weakness in the extremities, such as slow climbing of stairs. In February 2005, the patient's voice became nasal, and he had difficulty in turning his tongue. In December of the same year, he was admitted to our hospital for a thorough examination after becoming lethargic while eating.

### After pre-processing

> ２００２年夏より重い物の持ち上げが困難になり、階段の昇りが遅くなるなど四肢の筋力低下が緩徐に進行した．２００５年２月頃より鼻声となりろれつが回りにくくなった．また、食事中にむせるようになり、同年１２月に当院に精査入院した。

### After tokenization

> ['２００２年', '夏', 'より', '重い', '物', 'の', '持ち上げ', 'が', '困難', 'に', 'なり', '、', '階段', 'の', '[UNK]', 'が', '遅く', 'なる', 'など', '四肢', 'の', '筋力低下', 'が', '緩徐', 'に', '進行', 'し', 'た', '．', '２００５年', '２', '月頃', 'より', '鼻', '##声', 'と', 'なり', 'ろ', '##れ', '##つ', 'が', '回り', '##にく', '##く', 'なっ', 'た', '．', 'また', '、', '食事', '中', 'に', 'むせる', 'よう', 'に', 'なり', '、', '同年', '１２月', 'に', '当', '院', 'に', '精査', '入院', 'し', 'た', '。']

See [example_main.py](https://github.com/jinseikenai/uth-bert/blob/master/example_main.py) for details<br>



