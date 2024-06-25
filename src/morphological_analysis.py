import MeCab
import os
import platform

class Morpheme:
    def __init__(self, analysis):
        self.data = analysis
    def get_raw_str(self):
        """元の文章に登場した形を文字列で返す
        """
        return self.data[0]
    def get_original_form(self):
        """原形(活用させない形)を文字列で返す
        """
        return self.data[2]
    def get_type(self):
        """品詞を文字列で返す
        """
        return self.data[3].split('-')[0]
    def is_independent(self):
        """自立語どうかを表す Boolean 値を返す
        """
        return self.get_type() in ['動詞', '形容詞', '形容動詞', '名詞', '副詞', '連体詞', '接続詞', '感動詞']
    def is_declinable(self):
        """用言かどうかを表す Boolean 値を返す
        """
        return self.get_type() in ['動詞', '形容詞', '形容動詞']

def analyze_single_sentence(sentence: str):
    """一つの文章を文字列で受け取り、各単語に対応する Morpheme インスタンスからなるリストを返す
    """
    os_name = platform.system()
    null_path = 'nul' if os_name == 'Windows' else '/dev/null'
    project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dictionary_path = os.path.join(project_root_path, 'data', 'mecab_dictionary')
    wakati = MeCab.Tagger(f'-r {null_path} -d {dictionary_path} -Owakati')
    chasen = MeCab.Tagger(f'-r {null_path} -d {dictionary_path} -Ochasen')
    result = [Morpheme(chasen.parse(x).split()) for x in wakati.parse(sentence).split()]
    return result