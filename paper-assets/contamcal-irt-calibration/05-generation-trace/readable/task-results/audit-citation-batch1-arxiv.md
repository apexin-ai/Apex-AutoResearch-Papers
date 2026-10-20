# audit citation batch1 arxiv

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_citation_batch1_arxiv_20260517T044804_result.json`
- **Structured JSON:** [`d160520ec109357ea677.json`](../../sessions/d1/d160520ec109357ea677.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the full audit:

---

```
[habba_2025_growing_pains] STATUS: MISMATCH
  bib title: "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration"
  real title: "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration"
  title match: YES
  bib authors: Habba, Maryam / Polo, Felipe Maia / Mamani, Ronald / Zhuang, Yuekai / Xu, Hao / Choshen, Leshem / Yurochkin, Mikhail / Sun, Yuekai
  real authors: Eliya Habba / Itay Itzhak / Asaf Yehudai / Yotam Perlitz / Elron Bandel / Michal Shmueli-Scheuer / Leshem Choshen / Gabriel Stanovsky
  author match: NO
    - Habba first name wrong: Maryam → Eliya
    - 6 fabricated authors: Polo, Mamani, Zhuang, Xu, Yurochkin, Sun 全不存在
    - 缺 6 人: Itzhak, Yehudai, Perlitz, Bandel, Shmueli-Scheuer, Stanovsky
    - 仅 Choshen 正确匹配
```

```
[luettgau_2025_hibayes] STATUS: MISMATCH
  bib title: "HiBayES: A Hierarchical Bayesian Modeling Framework for AI Evaluation Statistics"
  real title: "HiBayES: A Hierarchical Bayesian Modeling Framework for AI Evaluation Statistics"
  title match: YES
  bib authors: Luettgau, Lennart / Polo, Felipe Maia / Zhuang, Yuekai / Yurochkin, Mikhail / Sun, Yuekai
  real authors: Lennart Luettgau / Harry Coppock / Magda Dubois / Christopher Summerfield / Cozmin Ududec
  author match: NO
    - 仅 Luettgau 正确
    - 4 fabricated: Polo, Zhuang, Yurochkin, Sun
    - 缺 4 人: Coppock, Dubois, Summerfield, Ududec
```

```
[schaeffer_2026_generative_contamination] STATUS: MISMATCH
  bib title: "Quantifying the Effect of Test Set Contamination on Generative Evaluations"
  real title: "Quantifying the Effect of Test Set Contamination on Generative Evaluations"
  title match: YES
  bib authors: Schaeffer, Rylan / Kazdan, Joshua / Abbasi, Ali / Liu, Hailey / others
  real authors: Rylan Schaeffer / Joshua Kazdan / Baber Abbasi / Ken Ziyu Liu / Brando Miranda / Ahmed Ahmed / Fazl Berez / Abhay Puri / Stella Biderman / Niloofar Mireshghallah / Sanmi Koyejo
  author match: NO
    - Schaeffer ✓, Kazdan ✓
    - Abbasi first name wrong: Ali → Baber
    - Liu first name wrong: Hailey → Ken Ziyu
    - "others" 隐藏了 7 位真实作者
```

```
[sun_2025_emperors_new_clothes] STATUS: MISMATCH
  bib title: "The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination"
  real title: "The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination"
  title match: YES
  bib authors: Sun, Yifan / Li, Zhen / Zhang, Yingji / Chen, Fei
  real authors: Yifan Sun / Han Wang / Dongbai Li / Gang Wang / Huan Zhang
  author match: NO
    - Sun ✓
    - Li, Zhen → 不存在（真实有 Dongbai Li，不同人）
    - Zhang, Yingji → 不存在（真实有 Huan Zhang，不同人）
    - Chen, Fei → 完全不存在
    - 缺: Han Wang, Gang Wang
```

```
[wust_2025_selfcritique] STATUS: MISMATCH (严重)
  bib title: "Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations"
  real title: "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models"
  title match: NO — 完全不同。bib title 系从论文方法名 "Self-Critique" 伪造而来
  bib authors: Wüst, Timon / Hoffmann, Jan / Pang, Richard Yuanzhe
  real authors: Yongding Tao / Tian Wang / Yihong Dong / Huanyu Liu / Kechi Zhang / Xiaolong Hu / Ge Li
  author match: NO — 无一匹配，3 人全部伪造
```

```
[xu_2025_dcr] STATUS: MISMATCH
  bib title: "DCR: Quantifying Data Contamination in LLMs Evaluation"
  real title: "DCR: Quantifying Data Contamination in LLMs Evaluation"
  title match: YES
  bib authors: Xu, Yiyang / Qi, Hongzhan / Zhao, Benyou / Liu, Zhiyuan
  real authors: Cheng Xu / Nan Yan / Shuhao Guan / Changhong Jin / Yuke Mei / Yibing Guo / M-Tahar Kechadi
  author match: NO
    - Xu surname 对但 first name 错: Yiyang → Cheng
    - Qi, Zhao, Liu 3 人全部伪造
    - 缺全部 6 位真实共作者
```

```
[zhang_2024_minkpp] STATUS: MATCH
  bib title: "Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models"
  real title: "Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models"
  title match: YES
  bib authors: Zhang, Jingyang / Sun, Jingwei / Yeats, Eric / Ouyang, Yang / Kuo, Martin / Zhang, Jianyi / Yang, Hao / Li, Hai
  real authors: Jingyang Zhang / Jingwei Sun / Eric Yeats / Yang Ouyang / Martin Kuo / Jianyi Zhang / Hao Frank Yang / Hai Li
  author match: YES (minor: "Hao" vs "Hao Frank" — middle name 省略，可接受)
```

```
[zhou_2025_psnirt] STATUS: MISMATCH
  bib title: "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory"
  real title: "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory"
  title match: YES
  bib authors: Zhou, Guanyu / Wang, Hainiu / Ye, Qingyao / Peng, Nanyun
  real authors: Hongli Zhou / Hui Huang / Ziqing Zhao / Lvyuan Han / Huicheng Wang / Kehai Chen / Muyun Yang / Wei Bao / Jian Dong / Bing Xu / Conghui Zhu / Hailong Cao / Tiejun Zhao
  author match: NO
    - Zhou surname 对但 first name 错: Guanyu → Hongli
    - Wang, Ye, Peng 3 人伪造
    - 缺 12 位真实作者（13 人 → bib 只列 4 人）
```

---

**汇总：8 条中 7 条 MISMATCH，仅 zhang_2024_minkpp 正确。**

显著模式：
- `Polo, Felipe Maia` / `Zhuang, Yuekai` / `Yurochkin, Mikhail` / `Sun, Yuekai` 重复出现在多条伪造作者中（#1, #2），疑为 LLM 幻觉的固定模式
- `wust_2025_selfcritique` 最严重：title 和 authors 全部伪造，arXiv ID 指向完全不同的论文
- 多条 entry 仅首作者姓氏正确、名字错误，其余共作者全部编造

---
