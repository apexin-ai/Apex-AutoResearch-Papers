# paper bib author fix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_bib-author-fix_20260515T181255_result.json`
- **Structured JSON:** [`0dde82375c8d8dace605.json`](../../sessions/0d/0dde82375c8d8dace605.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件均已修复。汇总：

---

### 条目 1: `wu_survey_2025`
**原始:** `Wu, Junchao and Zhu, Shu and Li, Decheng and Yang, Jie and Xiang, Xinyu and Qiao, Yixin and Ruan, Yucheng and Wang, Tat-Seng and Ge, Yongfeng`
**修复:** `Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai`
**证据:** [ACL Anthology 2025.cl-1.8](https://aclanthology.org/2025.cl-1.8/), [MIT Press](https://direct.mit.edu/coli/article/51/1/275/127462/)
**问题:** 9 个作者中仅 Wu, Junchao 正确，其余 8 个全部是幻觉。"Wang, Tat-Seng" 确系 reviewer 指出的错误——该领域知名学者是 Chua, Tat-Seng，但此论文的真实作者中两者皆无。

### 条目 2: `munir_looking_glass`
**原始:** `Munir, Muhammad Adnan and Siddiqui, Shoaib Ahmed and Dengel, Andreas and Ahmed, Sheraz` / venue: `Findings of EACL`
**修复:** `Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed` / venue: `Proceedings of EACL` (main)
**证据:** [ACL Anthology 2021.eacl-main.155](https://aclanthology.org/2021.eacl-main.155/)
**问题:** 作者完全错误（混淆了同姓 Munir 的另一篇 DFKI 论文）。且 venue 应为 EACL main，非 Findings。

### 条目 3: `reliable_detection`
**原始:** `@inproceedings` / ICLR 2024
**修复:** `@article` / Transactions on Machine Learning Research, 2025
**证据:** [OpenReview TMLR](https://openreview.net/forum?id=OOgsAZdFOt), [TMLR acceptance announcement](https://x.com/TmlrPub/status/1900336120296034775)
**问题:** 该论文曾提交 ICLR 但未被接收，最终发表于 TMLR 2025。

### 条目 4: `mapping_llm_science`
**原始:** `@article` / arXiv preprint arXiv:2404.01268, 2024
**修复:** `@inproceedings` / Proceedings of the Conference on Language Modeling, 2024
**证据:** [OpenReview COLM 2024](https://openreview.net/forum?id=YX7QnhxESU)
**问题:** 已正式发表于 COLM 2024，不再是 preprint。

---
