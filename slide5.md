---
marp: true
theme: gaia
paginate: true
style: 
math: mathjax
---

# Python Computer Simulation
![bg right:45%](./fig/image.png)

---

# **Chapter 5 Natural science Model**

--

## **5.1 Population preditction**
## **5.2 Epidemic**
## **5.3 Predator-prey relationship**
## **5.4 Fractal**
## **5.5 Chaos**
## **5.6 Sound and frequency**

---

### **5.1 Population preditction**

- ***MOTIVATION***: Predict future population with a mathmatical model

- ***APPROACH***: Ideas of **Population Model**
  - $\frac{dP(t)}{dt}=γP(t)(\frac{P∞-P(t)}{P∞})$ #1 | $P(t)$: population
  - The population growth rate in a given year is proportional to the population in that year.
  - Population growth has a upper limit
  - The population growth rate decreases as the population gets close to the upper limitation
- Analitical solution of Equation #1
  - $P(t)=\frac{P∞}{1+(\frac{P∞}{P0}-1)e^-γt}$ #2
  - The solution is a logistic function

- ***EXERCISE***: Parameter estimation
  - Determine $P0, P∞$, and $γ$ with real data
 
---

### **5.2 Epidemic**

- ***MOTIVATION***: Predict and analyze processes of epidemics with a mathmatical model

- ***APPROACH***: Ideas of **SIR Model**
  - $\frac{dS(t)}{dt}=-βS(t)I(t)$ #3 | $S(t)$: Susceptibles
  - $\frac{dI(t)}{dt}=βS(t)I(t)-γI(t)$ #4 | $I(t)$: Infectives
  - $\frac{dR(t)}{dt}=γI(t)$ #5 | $R(t)$: Recovered
  - $β$ stands for infection rate and $γ$ stands for recovery rate
  - $S(t)*I(t)$ represents contacts between the susceptibles and the infectives
  - New infetives are proportional to Infection rate
  - Variation of the infectives is the difference between new infectives and new people who recovered
  - New people who recovered are propotional to $I(t)$

- ***EXERCISE***: Simulation and analysis focusing on $S(0)$
  - SIR Model behaves in a different way depending on the initial value of $S(t)$
  - $S(0)<=\frac{γ}{β}$ or $S(0)>\frac{γ}{β}$?

---

### **5.3 Predator-prey relationship**
- ***MOTIVATION***: Expalain population variation of organisms with a mathmatical model

- ***APPROACH***: Ideas of **Predator-prey Model**
  - $\frac{dx(t)}{dt}=ax(t)-bx(t)y(t)$ #6 | $x(t)$: Preys
  - $\frac{dy(t)}{dt}=-cy(t)+dx(t)y(t)$ #7 | $y(t)$: Predators
  - Regarding Equation #6, the Preys increase exponentially without the predators
  - Regarding Equation #6, the preys decrease depending on the numbers of chances to encounter the predators
  - Regarding Equation #7, the predators exponentially decrease without the preys
  - Regarding Equation #7, the predators increase depending on the numbers of chances to encounter the preys

- ***EXERCISE***: Conduct simulations
  - Check the trend on the numbers of the predators and preys
  - What if both of the predators and preys are overfished simultaneously?
  - What if both of the predators and preys are not fished so much simultaneously?

---

### **5.4 Fractal #1**
- **Fractals** are geometric shapes which have similar structure at a given scale (**self similarity**)

- ***EXERCISE #1***: Generate Mandelbrot Set
  - **Mandelbrot Set** is a fractal resulted from calculation for the divergence condition for a complex sequence
  - Check the details of the figure at a given scale
  - Find self similarity 

![bg right:50%](./fig/Chap5/MandelbrotSet.jpg)

---

### **5.4 Fractal #2**
- ***MOTIVATION***: Depict complex fern leaves (シダの葉) with a few simple rules

- ***APPROACH***: Repetition and randomization
  - prepare four specific affine tranformations to get the values of x and y for the next step
  1. $f1$ is for stems
  2. $f2$ is for continuous smaller leaves
  3. $f3$ is for larger leaves on left
  4. $f4$ is for larger leaves on right
  - Set probabilities for each transformation

- ***EXERCISE #2***: Depict fern leaves on computer
  - Generate **Barnsley Fern**
  - Focus on self similarity
  - Can you depict different types of fern leaves with different parameters?

![bg right:40%](./fig/Chap5/BarnsleyFern.jpg)

---

## **5.5 Chaos**
- **Chaos** is complex system which is deterministic but hard to predict its future behavior due to **sensitive dependence on the initial conditions (初期値鋭敏性)**

- ***EXERCISE #1***: Depict **Lorenz attractor**
  - $\frac{dx(t)}{dt}=s(y-x)$ #8
  - $\frac{dy(t)}{dt}=rx-y-xz$ #9
  - $\frac{dz(t)}{dt}=xy-bz$ #10
  - A famous set of values $(s, r, b)$ is $(10, 28, 8/3)$
  - Change the initial values by just a bit (e.g. x(0)=0 -> x(0)=0.0001)

- ***EXERCISE #2***: Depict chaos of **logistic equation**
  - $x(n+1)=ax(n)(1-x(n)), (n=0, 1, 2,... )$ #11
  - Check different types of behavior for the value of $x(n)$, with different $a$
  - Change the initial value of $x(0)$ to check sensitive dependence on the initial conditions (e.g. x(0)=0.01 -> x(0)=0.010001)
  - Generate figures for the values of $a$ and $x(n)$ (**logistic maps**)

---

## **5.6 Sound and frequency**
- **Twelve equal temperament** is a musical note system deviding sounds into twelve notes

- When a note gets a one round, the frequency of the note doubles

- When the frequency of a note is $f$, that of the next note is $\sqrt[12]{2}f$

- ***EXERCISE***: Calculate frequency of notes
  - What is the frequency for the next Do?
  - What is the frequency for the Ti on the table?
    - Hint: You can find **La#** between La and Ti



| Note           | Do  | Re  | Mi  | Fa  | So  | La  | Ti  | 
| -------------- | --- | --- | --- | --- | --- | --- | --- | 
| Frequency (Hz) | 262 | 294 | 330 | 349 | 392 | 440 | ??? | 


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
  font-size: 18pt;  /* 箇条書きのフォントサイズ */
}

table {
  font-size: 25pt; /* 文字サイズを12ptに設定 */
  margin: auto;
  text-align: left;
}

</style>