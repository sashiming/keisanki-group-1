import os
import sys
import regex
import jaconv
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
        is_root = True     # dict2で根にいるかどうか
        for morph in sentence:
            genkei = morph.get_original_form()
            if '記号' not in morph.get_type():
                all_morphemes += 1
            if '名詞' in morph.get_type():
                val = 0
                if genkei in dict1:
                    val = dict1[genkei].value
                else:   # ひらがな/カタカナ表記揺れへの簡易的対策
                    if jaconv.hira2kata(genkei) in dict1:
                        val = dict1[jaconv.hira2kata(genkei)].value
                    if jaconv.kata2hira(genkei) in dict1:
                        val = dict1[jaconv.kata2hira(genkei)].value
                score += val
            if (not is_root) or morph.is_declinable():
                found, w_score, w_typ = dict2.search(genkei)
                score += w_score
                if found:
                    is_root = False
                else:
                    dict2.reset()
                    is_root = True
        scores.append(score / all_morphemes)

    return scores
