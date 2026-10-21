# paper writing experiments

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260517T160613_result.json`
- **Structured JSON:** [`3306d9ec401f1248a300.json`](../../sessions/33/3306d9ec401f1248a300.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`experiments.tex` 已写入并注册（`art_20260517_2f5e45`）。

结构概要：
- **5.1 Setup**: 数据集/模型/训练/指标定义（含两版 Evi-F1 区分）
- **5.2 Main Results**: Table 1, RSFT CED +4.92pp, evidence tax 量化
- **5.3 Decoupling Spectrum**: Table 2 + fig:spectrum, GRPO QLoRA 灾难性/bf16 温和/DPO 渐进/RSFT 无解耦
- **5.4 Scaling**: Table 3 + fig:scaling, 1.7B 反向受益/4B 重税/8B 吸收, RSFT 全尺度有效
- **5.5 Evidence Strategy**: Table 4, joint vs post-hoc vs rerank 对比
- **5.6 Generalization**: 跨架构/跨数据集/与 DREEAM 对比

待填数据：LLaMA RSFT 和 CED reranker 用 `\texttt{TBD}` 占位。

---
