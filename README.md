# Applied Microeconometrics Projects

В этом репозитории собраны два групповых проекта по applied econometrics и causal inference.  


## 1. Женщины в совете директоров и результаты компаний (01_female_directors_ddml.pdf)

Оценка эффекта наличия хотя бы одной женщины в совете директоров на ROA британских компаний в 2015–2019 годах.

**Методы:** Propensity Score Blocking, IPW/IPWRA, Doubly Robust Estimation, DDML, 5-fold cross-fitting, Lasso, CatBoost, Neural Network, placebo tests, permutation inference.

**Вывод:** оценки в основном положительные, но часто статистически незначимые. Возможна умеренная положительная связь, однако causal-интерпретация ограничена риском selection on unobservables.

---

## 2. Ставки по ипотеке и просрочки (02_mortgage_rates_fuzzy_rdd.pdf)


Оценка влияния ипотечной ставки на вероятность просрочки с использованием fuzzy RDD вокруг порога FICO 620.

**Методы:** Fuzzy RDD, local linear regression, IV, McCrary density test, covariate continuity checks, donut RDD, clustered standard errors, bandwidth sensitivity analysis.

**Вывод:** несмотря на сильный first stage, validity checks показывают sorting/manipulation around the cutoff и дисбаланс ковариат. Локальные RDD-оценки не дают устойчивого доказательства causal effect ставки на delinquency.
