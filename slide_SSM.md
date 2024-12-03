---
marp: true
theme: gaia
paginate: true
style: 
math: mathjax
---

# Social System Modeling
![bg right:50%](./fig/SSm/title.jpg)

---

# **Lecture #1 on Social System Modeling**

--

## **1. Motivation for Social System Modeling**
## **2. Modeling flow**
## **3. Resolution of model**
## **4. Reliability evaluation of model**
## **5. Parameter setting of model**
## **6. Scenario analysis**

---

### **1. Motivation for Social System Modeling**

- What is about **social system**?
  - Social system focuses on humans and their interactions, rather than nature.
  - You can check definitions of **society** by Tominaga (1995) to consider social system
    1. There interactions or communications among members
    2. Members of societies last for some time; they don't dismiss soon.
    3. Members are organized.
    4. There are boundaries deviding people into members and non-members
- Why do you model social systems?
  - Some social systems have problems or unknowns.
  - ***Such problems and unknowns are often tough to solve or analyze due to complexity and uncertainty (不確実性) of the social systems.***
  - ***Social system modeling enables you to deal with the comlexity and uncertainty and tackle the problems and unknowns in a better way.***
 
---

### **2. Modeling flow**
1. Identify problems in society.
2. Define a social system.
3. Describe concepts and structures of the social systems with natural langages, equations, or figures.
4. Program the conceptual model into computerized model with computers and programming languages.
5. Evaluate reliability of the models.
6. Set parameters of the computerized models.
7. Conduct scenario analyses.

![bg right:52%](./fig/sargent.png)

---

### **3. Resolution of model**

- **Resolution (解像度)** of model as a hint to build conceptual models
  - How detailed can you describe social systems?
- There are mainly three types of social model depending on resolution.
  - It ***doesn't*** matter which type of model you select itself.
  - ***Objectives of cocial system modeling guide you in decisons on resolution of models.***
  - ***Resolution guides you in choices on*** **reliability evaluation (信頼性の評価)** ***of model.***

| Resolution         | Description                                                                       | Objective                                                                                              | Reliability evaluation                                                         | 
| ------------------ | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ | 
| **Abstract model**     | Simple models with a few essential structures                                     | - To comprehend micro-macro link mechanisms<br>- To build theories<br>- To obtain insights             | - Acceptable micro behavior and holistic features of system        | 
| **Middle-range model** | More realistic models with more parameters, describing specific situations        | - To build prototypes to support  decision-making<br>- To comfirm or generate stylized facts | - Consistency with stylized facts                                  | 
| **Facsimile model**    | Most realistic models with less universality, describing very specific situations | - To conduct scenario analyses                                                                         | - Survey on agents' behavior model<br>- Consistency with real data | 

---

### **3.1 Example of abstract model**
- **Segregation (分居) model** by Schelling in 1971
- There are 2 types of agents on cells.
- One type of agent on a cell stay there when it finds fewer another type of agent on Moore neighborhood (ムーア近傍) than threashold.
- One type of agent on a cell moves to another cell randomly when it finds more another type of agent on Moore neighborhood than threashold.
- A simple model with just one parameter (thereshold) describe how and why people live with similar ones

![bg right:50%](./fig/SSM/segregation.png)

---

### **3.2 Example of middle-range model**
- Variation types for box office (興行収入) of film market proposed by Ainslie et al. in 2005
- There are two **stylized facts (定型化事実)** in film market.
  - In general, stylized facts are phenomena  which are observed with reproducibility, with or without explanation of the mechanisms.
  - **Blockbuster-type** has an early and high peak.
  - **Sleeper-type** has a slow starting and a late and short peak.
- The model focus on film market but does not mention any specific work.
- The model helps confirm and analyze stylized facts, and helps creates prototypes to support decision-making on advatisement and marketing.

![bg right:40%](./fig/SSM/BoxOffice.png)

---

### **3.3 Example of facsimile model**
- Analyses on COVID-19 by SIR model by Kartono et al. in 2021
- **SIR model** is a very general model but it is applied to a specific epidemic and specific countries at specific period in this study.
- The model includes parameters validated by real data.
- The model help forecast long-term trend of COVID-19 in specific countries.

![bg right:50%](./fig/SSM/SIR.png)

---

### **3.4 Exercise for your research in terms of resolution**
- What type of model do you build in your research?
  1. Pick up one research project of yours to consider which the project is social system modeling or not, refering to the difinitions of society on slide #3. Otherwise, show the reasons why your project is not social system modeling.
  2. Classify your research project into abstract model, middle-range model, or facsimile model.
  3. Consider how you would build the other types of model with the same research theme.
- An example is shown below.
  - Abstract model: Environmental action by penalty and reward
  - Middle-range model: Analysis on GHG emission mitigation in international maritime transport focusing on the relationship between carbon levy (炭素課金) and freight rate (運賃)
  - Facsimile model: Evaluation of the environment regulations for net-zero GHG emissions by 2050 in international maritime transport (Original reserach project)

---

### **4. Reliability evaluation of model**
- It is imortant to evaluate how you can trust models you build.
- There are mainly three ways to evaluate your models.
  1. **Verification (正当性の評価)**: How right do computerized models work?
  2. **Validation (妥当性の評価)**: How right do you build conceptual models?
  3. **Accreditation (実行承認性の確認)**: 
- How do you evaluate and guarantee your models with these methods? -> Go to the special session #2

![bg right:50%](./fig/sargent.png)

---

### **5. Parameter setting of model**
- The main challenge for building models is setting parameters.
- There are mainly six ways to set parameters of model
  1. Collect and refer to real data.
  2. Conduct **sensitive analyses (感度分析)**. -> Go to the special session #2
  3. Conduct **inversive simulations (逆シミュレーション)**. -> Go to the special session #2
  4. Conduct **virtual grounding** -> Go to the special session #2
  5. Estimate parameters by **Bayesian network** -> Go to the special session #2
  6. Adopt unknown or uncertain parameters as scenario -> Go to the next slide

---

### **6. Scenario analysis**
- You cannot remove all uncertainties from social simulations.
- **Scenario analyses (シナリオ分析)** help visualize bunches of possibility (可能性の束) and support future decision-making.
- There are mainly three ways to analyse simulation results.
  1. **What-if analysis (What-if分析)** -> Go to the special session #2
  2. **Uncertainty analysis (不確実性分析)** -> Go to the special session #2
  3. **Hypothetical scenario analysis (仮説シナリオ分析)** -> Go to the special session #2


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
  font-size: 13pt; /* 文字サイズを12ptに設定 */
  margin: auto;
  text-align: left;
}

</style>