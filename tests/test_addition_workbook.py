import pytest

class TestAdditionWorkbook :

    # 足し算の答えが一桁になるかどうかのテスト 0を除く
    def test__generate_answer__excluding_0(self) :
        pass

    # 足し算の答えが一桁になるかどうかのテスト 0を含む
    def test__generate_answer__including_0(self) :
        pass

    # 一桁の答えから2つの変数を使った式を求める 0を除く
    # 答え: 4 -> 2 + 2, 3 + 1, etc
    def test__generate_fomula__single_digit_answer_and_two_value__excluding_0(self) :
        pass

    # 一桁の答えから2つの変数を求める 0を含む
    # 答え: 4 -> 4 + 0, 2 + 2, 3 + 1, etc
    def test__generate_fomula__single_digit_answer_and_two_value__including_0(self) :
        pass

    # 一桁の足し算の式で、答えも一桁になるかのテスト
    def test__1_digit_formula_1_digit_answer(self) :
        pass
    