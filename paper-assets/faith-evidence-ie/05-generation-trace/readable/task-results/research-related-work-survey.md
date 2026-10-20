# research related work survey

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related_work_survey_20260516T060606_result.json`
- **Structured JSON:** [`a9366531dea917c32a3e.json`](../../sessions/a9/a9366531dea917c32a3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

literature_map.yaml 已更新。142 篇论文，新增 11 篇（注意 ESTR-DocRE 和 Dual reasoning 已有但被分到了同一新 category）。

---

## 调研摘要

新增 11 篇论文，覆盖 5 个新 category（37-41），按方向分布：

### a. DocRE + Evidence
- **SAIS** (NAACL 2022): 最直接 prior work——encoder-based two-stage evidence retrieval + DocRE，发现 evidence supervision 提升 RE。与 FREIGE 形成关键对比：discriminative evidence supervision 有益 vs generative evidence generation 有 ~8pp cost。
- **ATLOP** (AAAI 2021), **DocuNet** (IJCAI 2021): DocRE 标准 baseline，related work 必须引用。
- **DocRED** (ACL 2019), **Re-DocRED** (EMNLP 2022): 数据集论文，FREIGE 的评测基础。

### b. LLM for IE
- **GenRES** (NAACL 2024): 指出 exact match F1 低估 generative RE 性能，human annotation 自身不完整。FREIGE 论文需讨论此 evaluation limitation。

### c. RSFT / Self-training for IE
- **STaR** (NeurIPS 2022): RSFT 的理论先驱——iterative bootstrapping (generate → filter correct → fine-tune)。FREIGE 的 RSFT 是 STaR 的单轮变体 + evidence quality 筛选。
- **SPIN** (ICML 2024): Self-play fine-tuning，利用模型自身输出进行训练，与 RSFT 方向互补。

### d. RL for Structured Prediction
- 已有文献 (R1-RE, ReasoningNER, E-GRPO, RL-Struct 等) 覆盖充分，本轮未新增。

### e. Faithfulness / Knowledge Distillation
- **KD-DocRE** (Findings ACL 2022), **PSD** (TOIS 2024): DocRE 的知识蒸馏和自蒸馏方法，与 RSFT 的 self-improvement 思路有概念联系。

### 对论文 Related Work 的建议
1. **必引**: DocRED, Re-DocRED, ATLOP, SAIS, DREEAM (已有), R1-RE (已有)
2. **建议引**: GenRES (evaluation caveat), STaR (RSFT 理论渊源), DocuNet, KD-DocRE
3. 现有 map 中 RL stability (DAPO, Dr. GRPO, GDPO) 和 LoRA artifacts 类别已充足

---
