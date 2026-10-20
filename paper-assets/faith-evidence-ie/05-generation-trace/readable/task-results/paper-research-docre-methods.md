# paper research docre methods

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_research_docre_methods_20260517T150401_result.json`
- **Structured JSON:** [`9a5d4f0843346f6e47ed.json`](../../sessions/9a/9a5d4f0843346f6e47ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the information needed. Here are the results:

---

```
VERIFICATION RESULTS:

1. DocRED: ✅ VERIFIED
   Title: "DocRED: A Large-Scale Document-Level Relation Extraction Dataset"
   Authors: Yuan Yao, Deming Ye, Peng Li, Xu Han, Yankai Lin, Zhenghao Liu, Zhiyuan Liu, Lixin Huang, Jie Zhou, Maosong Sun
   Venue: ACL 2019 (P19-1074)
   arXiv: 1906.06127
   ACL Anthology: https://aclanthology.org/P19-1074/

2. Re-DocRED: ✅ VERIFIED
   Title: "Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction"
   Authors: Qingyu Tan, Lu Xu, Lidong Bing, Hwee Tou Ng
   Venue: EMNLP 2022 (2022.emnlp-main.580)
   arXiv: 2205.12696
   ACL Anthology: https://aclanthology.org/2022.emnlp-main.580/

3. ATLOP: ✅ VERIFIED
   Title: "Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling"
   Authors: Wenxuan Zhou, Kevin Huang, Tengyu Ma, Jing Huang
   Venue: AAAI 2021
   arXiv: 2010.11304
   DOI: 10.1609/aaai.v35i16.17717

4. LMRC: ✅ VERIFIED (年份需修正)
   Title: "LLM with Relation Classifier for Document-Level Relation Extraction"
   Authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang
   Venue: arXiv preprint (未确认正式会议录用)
   arXiv: 2408.13889
   ⚠️ 注意: 原始记录标注 "Li et al., 2023" 有误，arXiv 提交日期为 2024年8月，应修正为 2024

5. DocKS-RAG: ✅ VERIFIED (venue需修正)
   Title: "DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning"
   Authors: Xiaolong Xu, Yibo Zhou, Haolong Xiang, Xiaoyong Li, Xuyun Zhang, Lianyong Qi, Wanchun Dou
   Venue: ICML 2025 (Proceedings of Machine Learning Research vol. 267)
   arXiv: ❌ 未找到 arXiv ID（论文通过 OpenReview 提交，ID: SVl9tIADWV）
   PMLR: https://proceedings.mlr.press/v267/xu25am.html
   ⚠️ 注意: 原始记录标注 "Xu et al., 2024"，实际发表于 ICML 2025。无 arXiv preprint。

6. GenRES: ✅ VERIFIED
   Title: "GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models"
   Authors: Pengcheng Jiang, Jiacheng Lin, Zifeng Wang, Jimeng Sun, Jiawei Han
   Venue: NAACL 2024 (Long Papers, pages 2820-2837)
   arXiv: 2402.10744
   ACL Anthology: https://aclanthology.org/2024.naacl-long.155/
   DOI: 10.18653/v1/2024.naacl-long.155


GAP-FILL (建议补充的论文):

- [docunet] "Document-level Relation Extraction as Semantic Segmentation"
  Authors: Ningyu Zhang, Xiang Chen, Xin Xie, Shumin Deng, Chuanqi Tan, Mosha Chen, Fei Huang, Luo Si, Huajun Chen
  Venue: IJCAI 2021 | arXiv: 2106.03618

- [kd_docre] "Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation"
  Authors: Qingyu Tan, Ruidan He, Lidong Bing, Hwee Tou Ng
  Venue: Findings of ACL 2022 | arXiv: 2203.10900

- [dreeam] "DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction"
  Authors: Youmi Ma, An Wang, Naoaki Okazaki
  Venue: EACL 2023 | arXiv: 2302.08675
  备注: 当前 DocRE SOTA 之一，与本项目 evidence-guided 主题高度相关

- [autore] "AutoRE: Document-Level Relation Extraction with Large Language Models"
  Authors: Lilong Xue, Dan Zhang, Yuxiao Dong, Jie Tang
  Venue: ACL 2024 Demo | arXiv: 2403.14888
  备注: LLM-based DocRE 代表性工作，RHF 范式，在 Re-DocRED 上 SOTA


ISSUES SUMMARY:
- LMRC: 年份从 2023 修正为 2024
- DocKS-RAG: 无 arXiv ID（仅 OpenReview + ICML 2025 proceedings），venue 从 2024 修正为 2025
- 无 FAKE 论文，6 篇全部真实存在
```

---
