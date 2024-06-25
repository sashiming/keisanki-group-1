import os
import sys
root_path = os.path.dirname(os.path.dirname(__file__))

def calc_score(data, dict1, dict2):
    '''
    args:
        data( list(list(Morpheme)) ): 形態素解析後の文章データ
        dict1( dict(str, Info1) ): dictionary1.txtを前処理したもの
        dict2( Info2 ): dictionary2.txtを前処理したもの
    returns:
        scores( list(float) ): 各文章のスコアのリスト
    '''
    scores = []

    for sentence in data:
        all_morphemes = 0    # 形態素の総数(記号除く)
        score = 0
        # words_with_morp = []
        is_root = True     # dict2で根にいるかどうか
        # tmp_str = ''
        for morph in sentence:
            genkei = morph.get_original_form()
            if '記号' not in morph.get_type():
                all_morphemes += 1
            if '名詞' in morph.get_type():
                val = dict1[genkei].value
                score += val
                if val != 0:

            if (not is_root) or morph.is_declinable():
                found, w_score, w_typ = dict2.search(genkei)
                score += w_score
                if found:
                    is_root = False
                    # tmp_str += morph.get_raw_str()
                else:
                    dict2.reset()
                    # tmp_str = ''
        scores.append(score / all_morphemes)

    return scores
