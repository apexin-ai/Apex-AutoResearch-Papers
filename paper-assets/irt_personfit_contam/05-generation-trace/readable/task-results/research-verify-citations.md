# research verify citations

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify-citations_20260522T080821_result.json`
- **Structured JSON:** [`a287f3df549de318cb19.json`](../../sessions/a2/a287f3df549de318cb19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### 论文 1: "Dong et al. (2024)"

用户提供的标题和作者指向**两篇不同的论文**，存在混淆：

**如果按作者 "Dong" 查找：**
- **标题**: Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models
- **作者**: Yihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, Bin Gu, Mengfei Yang, Ge Li
- **年份**: 2024
- **发表场所**: Findings of ACL 2024, pp. 12039–12050
- **arXiv ID**: **2402.15938**（非 2407.01019）

**如果按标题 "Does Data Contamination Detection Work (Well) for LLMs" 查找：**
- **标题**: Does Data Contamination Detection Work (Well) for LLMs? A Survey and Evaluation on Detection Assumptions
- **作者**: Yujuan Velvin Fu, Özlem Uzuner, Meliha Yetişgen, Fei Xia
- **年份**: 2024（arXiv）/ 2025（正式发表）
- **发表场所**: Findings of NAACL 2025
- **arXiv ID**: **2410.18966**

**差异**：arXiv:2407.01019 实际上是一篇无关的优化器论文（"An Abstract Lyapunov Control Optimizer"）。需要确认引用的是哪一篇。

---

### 论文 2: "Sinharay & Johnson (2017)"

- **标题**: Are the Nonparametric Person-Fit Statistics More Powerful Than Their Parametric Counterparts? Revisiting the Simulations in Karabatsos (2003)
- **作者**: **Sandip Sinharay**（单独作者，**无 Matthew S. Johnson**）
- **年份**: 2017
- **发表期刊**: Applied Measurement in Education, 30(4), 314–328
- **DOI**: 10.1080/08957347.2017.1353990

**差异**：这篇是 Sinharay 独著，不是 Sinharay & Johnson 合著。Sinharay 与 Johnson 有其他合作论文（如 2020 年 BJMSP 的 preknowledge 检测论文），但 2017 年 person-fit power 这篇没有 Johnson。

---

Sources:
- [Dong et al. (2024) - arXiv](https://arxiv.org/abs/2402.15938)
- [Dong et al. (2024) - ACL Anthology](https://aclanthology.org/2024.findings-acl.716/)
- [Fu et al. (2024) - arXiv](https://arxiv.org/abs/2410.18966)
- [Fu et al. (2025) - ACL Anthology](https://aclanthology.org/2025.findings-naacl.291/)
- [Sinharay (2017) - Taylor & Francis](https://doi.org/10.1080/08957347.2017.1353990)
- [Sinharay (2017) - ERIC](https://eric.ed.gov/?id=EJ1153824)

---
