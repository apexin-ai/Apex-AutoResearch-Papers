# paper research evidence docre

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_research_evidence_docre_20260517T152414_result.json`
- **Structured JSON:** [`7ba0c7369b67e39193dd.json`](../../sessions/7b/7ba0c7369b67e39193dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有论文验证完毕。以下是 6 篇验证结果：

---

## [DREEAM]
- title: DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction
- authors: Youmi Ma, An Wang, Naoaki Okazaki
- venue: EACL 2023
- year: 2023
- arxiv: 2302.08675
- doi: 10.18653/v1/2023.eacl-main.145
- bibtex_key: ma2023dreeam
- verified: true
- relevance: 首次将 evidence 作为监督信号引导 attention 模块，并提出 evidence retrieval 自训练策略
- verification_note: 预期信息全部正确，第一作者 Youmi Ma (not Tan)，原始预期 "Tan et al." 有误

## [SAIS]
- title: SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction
- authors: Yuxin Xiao, Zecheng Zhang, Yuning Mao, Carl Yang, Jiawei Han
- venue: NAACL 2022
- year: 2022
- arxiv: 2109.12093
- doi: 10.18653/v1/2022.naacl-main.171
- bibtex_key: xiao2022sais
- verified: true
- relevance: 通过监督中间步骤（evidence retrieval + entity typing）提升 DocRE，并利用 evidence 做数据增强和 ensemble 推理
- verification_note: 预期信息全部正确，第一作者 Xiao 确认

## [EIDER]
- title: Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion
- authors: Yiqing Xie, Jiaming Shen, Sha Li, Yuning Mao, Jiawei Han
- venue: Findings of ACL 2022
- year: 2022
- arxiv: 2106.08657
- doi: 10.18653/v1/2022.findings-acl.23
- bibtex_key: xie2022eider
- verified: true
- relevance: 联合训练轻量 evidence extraction 模型，推理阶段融合 evidence 预测与全文预测，是 evidence-enhanced DocRE 的代表工作
- verification_note: 不在原始候选列表中，但与 evidence-based DocRE 高度相关且发表于 top venue，替换未找到的 DocGNRE

## [Evidence-aware DocRE]
- title: Evidence-aware Document-level Relation Extraction
- authors: Tianyu Xu, Wen Hua, Jianfeng Qu, Zhixu Li, Jiajie Xu, An Liu, Lei Zhao
- venue: CIKM 2022
- year: 2022
- arxiv: not found
- doi: 10.1145/3511808.3557313
- bibtex_key: xu2022evidenceaware
- verified: true
- relevance: 直接将 evidence awareness 融入 DocRE 模型设计，evidence sentence 子集即可预测 entity pair 关系
- verification_note: 原始候选列表中的 "Evidence-aware Document-level RE"，无 arXiv 预印本，仅在 ACM DL 发表

## [GEGA]
- title: GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction
- authors: Yanxu Mao, Xiaolin Chen, Peipei Liu, Tiehan Cui, Zibo Yue, Zhixiao Li
- venue: ICASSP 2025
- year: 2025
- arxiv: 2407.21384
- doi: 10.1109/ICASSP49660.2025.10889649
- bibtex_key: mao2025gega
- verified: true
- relevance: 构建于 DREEAM 之上，用 GCN 构造多权重矩阵引导 attention 到 evidence sentences，在 DocRED/Re-DocRED 上超越 DREEAM
- verification_note: 原始候选列表中的 GEGA，arXiv 预印本 2024 年 7 月，正式发表于 ICASSP 2025

## [CDER]
- title: CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction
- authors: Khai Phan Tran, Xue Li
- venue: ACIIDS 2024 (Springer LNCS)
- year: 2024
- arxiv: 2504.06529
- doi: 10.1007/978-981-97-4982-9_3
- bibtex_key: tran2024cder
- verified: true
- relevance: 将文档建模为二部图捕捉 entity pair 间的协作 evidence 检索模式，专注于 evidence retrieval 子任务
- verification_note: 原始候选列表中的 CDER，arXiv 版本为 2025 年 4 月更新版，会议发表于 ACIIDS 2024

---

**汇总**：
- 6/6 全部 verified
- DREEAM 预期作者 "Tan et al." 有误，实际为 Ma et al.
- DocGNRE 未能检索到对应论文，用 EIDER (Findings of ACL 2022) 替换，该论文与 evidence-based DocRE 直接相关且 venue 更强
- COREX (IJCNN 2024) 和 E2GRE (arXiv 2020) 也与 evidence 相关但 venue 较弱或未正式发表，未纳入最终 6 篇

Sources:
- [DREEAM - arXiv](https://arxiv.org/abs/2302.08675)
- [DREEAM - ACL Anthology](https://aclanthology.org/2023.eacl-main.145/)
- [SAIS - ACL Anthology](https://aclanthology.org/2022.naacl-main.171/)
- [SAIS - arXiv](https://arxiv.org/abs/2109.12093)
- [EIDER - ACL Anthology](https://aclanthology.org/2022.findings-acl.23/)
- [EIDER - arXiv](https://arxiv.org/abs/2106.08657)
- [Evidence-aware DocRE - ACM DL](https://dl.acm.org/doi/10.1145/3511808.3557313)
- [GEGA - arXiv](https://arxiv.org/abs/2407.21384)
- [GEGA - IEEE Xplore](https://ieeexplore.ieee.org/document/10889649/)
- [CDER - arXiv](https://arxiv.org/abs/2504.06529)
- [CDER - Springer](https://link.springer.com/chapter/10.1007/978-981-97-4982-9_3)

---
