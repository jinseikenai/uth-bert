# UTH-BERT
This site provides source code for pre-processing text and tokenization for use of UTH-BERT.

1. BERT: Bidirectional Encoder Representations from Transformers.
https://github.com/google-research/bert

2. UTH-BERT
https://ai-health.m.u-tokyo.ac.jp/uth-bert

## Pre-processing text

Japanese text includes two-byte full-width characters (mainly Kanji, Hiragana, or Katakana) and one-byte half-width characters (mainly ASCII characters).

We applied the Normalization Form Compatibility Composition (NFKC) followed by full-width characterization to all characters as a pre-processing.
 
## Tokenization

