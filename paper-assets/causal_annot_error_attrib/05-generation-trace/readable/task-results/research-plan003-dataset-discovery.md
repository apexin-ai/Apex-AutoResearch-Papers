# research plan003 dataset discovery

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan003-dataset-discovery_20260520T091514_result.json`
- **Structured JSON:** [`6763c8d3dd5012682812.json`](../../sessions/67/6763c8d3dd5012682812.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕，以下是三个数据集的确认报告。

---

## 1. Protest Event Coding (K=5)

**ACLED 不可用** — ACLED Terms of Use [明确禁止](https://acleddata.com/eula)将数据用于 ML/AI 训练、测试或开发，无论商业或学术用途。

**推荐替代：GLOCON Gold Standard Corpus**

```
数据集名称: GLOCON Gold Standard Corpus (GSC)
类别数 K: 5 (Demonstration, Armed Militancy, Group Clash, Industrial Action, Other)
样本量: ~17,000 篇新闻文章（含 document/sentence/token 三级标注）
License: 学术研究协议（需邮件申请，非 CC 开放许可）
下载方式: 联系 ahurriyetoglu@ku.edu.tr 申请
  GitHub: https://github.com/emerging-welfare/glocongold
  标注手册: https://zenodo.org/records/6540579
Gold-standard human labels: 是（每篇由两名社会/政治科学家标注，标注主管裁决，半自动错误检测改进）
备注: 覆盖印度、南非、巴西、阿根廷的英/葡/西语新闻。
  数据仅提供给遵守社会运动研究伦理标准的研究人员。
  CASE 2021/2022 shared task 基于此数据集子集，但 shared task 版本仅为二分类 (K=2)，不满足需求。
```

---

## 2. Stance Detection (K=3)

```
数据集名称: SemEval-2016 Task 6: Detecting Stance in Tweets
类别数 K: 3 (FAVOR, AGAINST, NEITHER)
样本量: ~4,163 条推文（Task A: train ~2,814 + test ~1,249；5 个 target: Atheism, Climate Change, Feminist Movement, Hillary Clinton, Legalization of Abortion）
License: CC BY 3.0 (ACL Anthology 材料)
下载方式: http://alt.qcri.org/semeval2016/task6/index.php?id=data-and-tools
  备用: https://github.com/emsrc/SemEval2016_T6_Stance_Detection
Gold-standard human labels: 是（CrowdFlower 众包标注）
备注: 公开可用，无使用限制。样本量偏小。
```

**备选：VAST (Varied Stance Topics)**

```
数据集名称: VAST (Zero-Shot Stance Detection)
类别数 K: 3 (Pro, Con, Neutral)
样本量: ~18,545 条评论（train ~13,477 / dev ~2,062 / test ~3,006），覆盖 ~5,634 个 topics
License: 未明确声明（学术论文附属数据集，公开可下载）
下载方式: https://github.com/emilyallaway/zero-shot-stance
Gold-standard human labels: 是（纽约时报 "Room for Debate" 评论，人工标注）
备注: 样本量和 topic 多样性优于 SemEval-2016。设计为 zero-shot 评估（test set targets 不出现在 train 中）。
  论文: Allaway & McKeown, EMNLP 2020
```

---

## 3. Toxicity (K=2)

```
数据集名称: Civil Comments (Jigsaw)
类别数 K: 2 (toxic / non-toxic，基于 toxicity ≥ 0.5 阈值二值化)
样本量: ~1,999,514 条评论（train 1,804,874 / val 97,320 / test 97,320）
License: CC0 1.0 (公共领域)
下载方式: 
  HuggingFace: from datasets import load_dataset; load_dataset("google/civil_comments")
  URL: https://huggingface.co/datasets/google/civil_comments
  TensorFlow Datasets: tfds.load("civil_comments")
Gold-standard human labels: 是（每条评论由多名人工标注者评分，提供连续 toxicity 分数 [0,1]）
备注: 无任何使用限制。原始标签为连续分数，可自定义阈值二值化。
  还包含 identity mention 子标签，可用于公平性分析。
```

---

## 总结

| 任务 | 推荐数据集 | K | 样本量 | 公开程度 |
|------|-----------|---|--------|---------|
| Protest event coding | GLOCON Gold | 5 | ~17k | 邮件申请 |
| Stance detection | SemEval-2016 T6 / VAST | 3 | ~4k / ~18k | 完全公开 |
| Toxicity | Civil Comments | 2 | ~2M | 完全公开 (CC0) |

**需要决策的点**：
- GLOCON Gold 需邮件申请。如果希望全部数据集都免申请公开可用，protest event coding 任务目前没有满足 K≥3 的完全开放替代。建议尽早联系 `ahurriyetoglu@ku.edu.tr` 申请。
- Stance detection 建议用 VAST（样本量大、topic 多样），SemEval-2016 作为 robustness check。

Sources:
- [ACLED EULA](https://acleddata.com/eula)
- [GLOCON Gold GitHub](https://github.com/emerging-welfare/glocongold)
- [GLOCON Annotation Manuals (Zenodo)](https://zenodo.org/records/6540579)
- [GLOCON Cross-context Corpus Paper](https://direct.mit.edu/dint/article/3/2/308/100736/Cross-Context-News-Corpus-for-Protest-Event)
- [SemEval-2016 Task 6 (ACL Anthology)](https://aclanthology.org/S16-1003/)
- [SemEval-2016 Task 6 Data](https://alt.qcri.org/semeval2016/task6/index.php?id=data-and-tools)
- [VAST: Allaway & McKeown 2020 (ACL Anthology)](https://aclanthology.org/2020.emnlp-main.717/)
- [VAST GitHub](https://github.com/emilyallaway/zero-shot-stance)
- [Civil Comments on HuggingFace](https://huggingface.co/datasets/google/civil_comments)

---
