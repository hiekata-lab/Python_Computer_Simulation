---
marp: true
theme: gaia
paginate: true

---

# Pythonコンピュータシミュレーション入門
# Python Computer Simulation

---

# 第4章 確率モデル
# **Chapter 4 Stochastic Model**

## 4.1 時系列モデル
## Time Series Model

---

### 大数の法則と中心極限定理
- 大数の法則（law of large numbers）

$$
\overline{X}_n=\frac{1}{n}(X_1+X_2+\dots+X_n)\hspace{1cm} (n \ge 1)
$$


$$
\lim_{n \to \infty} P(|\overline{X}_n-\mu| \gt \epsilon) = 0 \hspace{1cm} (\forall{\epsilon} \gt 0)
$$

$\overline{X}_n$は，平均 $\mu$ の確率分布に従い，互いに独立な確率変数 $X_1$, $X_2$,$\dots$の標本平均

---

### ランダムウォーク（一次元，三次元）

---

### モンテカルロ法による円周率計算


4.2 マルコフ連鎖
- マルコフ連鎖とは
- 定常分布と極限分布
- 定常分布の求め方
4.3 確率微分方程式
- ウィーナー過程
- 確率微分方程式の数値計算
4.4 カルマンフィルタ
- 離散時間線形の状態空間モデル
- アルゴリズム
- 定常カルマンフィルタ
4.5 時系列モデル
- ARMAモデル
- ARIMAモデル
- SARIMAXモデル
- 航空会社の乗客数の予測




<style>
/* スライドの基本設定 */
section {
  font-size: 20pt;  /* 本文のフォントサイズ */
  color: #333333;   /* 本文の色 */
}

/* 見出しのカスタマイズ */
h1 {
  font-size: 32pt;  /* h1 見出しのフォントサイズ */
  color: #2E8B57;   /* h1 見出しの色 */
}

h2 {
  font-size: 28pt;  /* h2 見出しのフォントサイズ */
  color: #4682B4;   /* h2 見出しの色 */
}

/* スライドの背景色を変更したい場合 */
section {
  background-color: #f9f9f9;  /* 背景色 */
}

/* 箇条書きリストのカスタマイズ */
ul {
  font-size: 20pt;  /* 箇条書きのフォントサイズ */
}

table {
  font-size: 10pt; /* 文字サイズを12ptに設定 */
  margin: auto;
  text-align: left;
}

</style>