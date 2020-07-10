from preprocess_text import preprocess as my_preprocess
from tokenization_mod import MecabTokenizer, FullTokenizerForMecab

if __name__ == '__main__':

    # special token for a Person's name (Do not change)
    name_token = "＠＠Ｎ"

    # path to the mecab-ipadic-neologd
    mecab_ipadic_neologd = '/usr/lib/mecab/dic/mecab-ipadic-neologd'

    # path to the J-Medic (We used MANBYO_201907_Dic-utf8.dic)
    mecab_J_medic = './MANBYO_201907_Dic-utf8.dic'

    # path to the uth-bert vocabulary
    vocab_file = "./bert_vocab_mc_v1_25000.txt"

    # MecabTokenizer
    sub_tokenizer = MecabTokenizer(mecab_ipadic_neologd=mecab_ipadic_neologd,
                                   mecab_J_medic=mecab_J_medic,
                                   name_token=name_token)

    # FullTokenizerForMecab
    tokenizer = FullTokenizerForMecab(sub_tokenizer=sub_tokenizer,
                                      vocab_file=vocab_file,
                                      do_lower_case=False)

    # pre process and tokenize example
    original_text = "2002 年夏より重い物の持ち上げが困難になり，階段の昇りが遅くなるなど四肢の筋力低下が緩徐に進行した．2005 年 2 月頃より鼻声となりろれつが回りにくくなった．また，食事中にむせるようになり，同年 12 月に当院に精査入院した。"
    print (original_text)

    pre_processed_text = my_preprocess(original_text)
    print (pre_processed_text)

    output_tokens = tokenizer.tokenize(pre_processed_text)
    print (output_tokens)
