# 2024Autumn - Computer Simulation

### Objective
- Understand the fundamentals on computer simulation in general and several specific methods using Python
- Utilize GitHub or other tools in effective ways
### Date and Time:
- Every Tuesday, 15:30-17:00
- From Oct 15 (w/o Oct 29, Nov 19)
### Members
- All LISD Members
### How to proceed
- Role
    - PIC (lecture): Prepare the material for presentation
        - Try Marp
    - Others: Read the chapter relevant to the topic
- Timeline
    - Lecture
        - 40 mins (+ Q&A for max 10 mins)
        - include quiz as much as possible (to be more interactive)
### Preparation
- Create GitHub account
- Join hiekata lab team
- Clone this repository
### Textbooks
- [**Pythonコンピュータシミュレーション入門　人文・自然・社会科学の数理モデル**](https://amzn.asia/d/2UivXT3)
    - We have two copies in the lab, but only in Japanese.
    - Support websites with sample codes are also available [here](https://github.com/ohmsha/MHBooks/tree/master/ComputerSimulation).
- Additional: how to make UIs: Maybe Terry can hold an additional session covering PyGwalker and Streamlit.

### Misc
- Record for those who are absent (Please remind me!)
- Stock presentation slides to be reusable
- Flexible Schedule

---
以下は[ここ](https://github.com/ohmsha/MHBooks/tree/master/ComputerSimulation)よりコピー

### 正誤表
本書の正誤表です。誤りに関し小職の力の足りなさをお詫びいたします。また，誤りをご指摘くださった読者のみなさまに御礼申し上げます。誤りの訂正をお願いいたします。

#### 【第1版第5刷】
page 46 ボックス・ミュラー法　(2.41）式
- 2つのルートの中が（誤）$\sqrt{-\log_e U_1}$ ->（正）$\sqrt{-2 \log_e U_1}$　となり，係数の2を入れてください。

page 152 表6.5
仕入れ価格$C_{cost}$と販売価格$C_{sell}$は，このシミュレーションでは使用していません。 


#### 【第1版第4刷】

page 41 【連続確率変数の場合】の説明文の1行目
- 「離散の確率変数」 --> 「連続の確率変数」<br>

page 144 【スクリプトの説明】最後の行
- 「目的関数は最後に与える。」 --> 「演算子を含まない式が目的関数を表す。通常は，最後または最初に記述する。」<br>
筆者がPuLPの文法を見誤っていました。

page 145 - 146<br>
x1 = pulp.LpVariable(,,,, 0, 2000, cat=,,,,)<br>
x2 = pulp.LpVariable(,,,, 0, 3000, cat=,,,,)<br>
x3 = pulp.LpVariable(,,,, 0, 1000, cat=,,,,)<br>
x1, x2, x3はジュース缶の本数を表し，上限を設ける必要は無いので，上限は全て"None"となります。ZIPファイルで提供しているNotebookの中のスクリプトは既に変更しました。

page 181
- Graphvix HP --> Graphviz HP

#### 【第1版第3刷】
page 76 下から2行目
- 図4.5  --＞ 図4.4


#### 【第1版第1刷】
page 4
- 因果律または因果性と呼ばれ --＞ 因果律または因果関係と呼ばれ

page 5
- ただし，過去の t --> ただし，t （このtに過去も未来も関係しません）