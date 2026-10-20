# diagnose 4b rsft s42 ign f1 audit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_4b-rsft-s42-ign-f1-audit_20260522T221349_result.json`
- **Structured JSON:** [`e3b34f0d8d01d66bae1c.json`](../../sessions/e3/e3b34f0d8d01d66bae1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，现在编制审计报告。

---

## 4B RSFT CED s42 审计报告

### 所有 s42 eval runs

| Run ID | 目录 | ign_f1 | f1 | n_preds | truncated | batch_size | max_tokens | model_path |
|--------|------|--------|-----|---------|-----------|------------|------------|------------|
| rsft_r1 (metrics.json) | rsft_r1 | 0.4449* | 0.4449 | 15307 | 213 | 8 | 1024 | rsft_output |
| rsft_r1 (**metrics_v2.json**) | rsft_r1 | **0.4363** | 0.4449 | 15307 | 213 | 8 | 1024 | rsft_output |
| rsft_ced_s42_reeval | rsft_ced_s42_reeval | **0.4423** | 0.4517 | 15436 | 214 | 4 | 1024 | rsft_output/checkpoint-510 |
| dev_eval_4b_rsft_ced_s42_v2 | dev_eval_4b_rsft_ced_s42_v2 | 0.4388 | 0.4499 | 20061 | 143 | 1 | 2048 | rsft_output_ced_s42_v2 |

\* metrics.json 的 ign_f1 == f1（bug，未正确计算 ign 排除），metrics_v2.json 标注 `_note: "Recomputed with fixed Ign-F1 (doc_id-free train_facts)"`

### 3-seed 协议一致性

**Protocol B — CED reeval (batch_size=4, max_tokens=1024):**

| Seed | Run ID | ign_f1 | n_preds | truncated | field_compliance | model |
|------|--------|--------|---------|-----------|------------------|-------|
| s42 | rsft_ced_s42_reeval | 0.4423 | 15436 | 214 | 0.776 | rsft_output/checkpoint-510 |
| s43 | rsft_ced_s43 | 0.4512 | 15051 | 184 | 0.809 | rsft_output_**ced_s43**/checkpoint-510 |
| s44 | rsft_ced_s44_reeval | 0.4511 | 15264 | 190 | 0.802 | rsft_output_s44/checkpoint-510 |

std = 0.51pp, mean = 44.82

**Protocol A — 旧协议 (batch_size=8, metrics_v2.json):**

| Seed | Run ID | ign_f1 | n_preds | truncated | field_compliance | model |
|------|--------|--------|---------|-----------|------------------|-------|
| s42 | rsft_r1 | 0.4363 | 15307 | 213 | 0.782 | rsft_output |
| s43 | rsft_s43 | 0.4585 | 14970 | 171 | 0.814 | rsft_output_s43 |
| s44 | rsft_s44 | 0.4551 | 15202 | 189 | 0.801 | rsft_output_s44 |

std = 1.20pp, mean = 45.00

### 两组 s42 eval 的协议差异

| 参数 | rsft_r1 (→0.4363) | rsft_ced_s42_reeval (→0.4423) |
|------|-------------------|-------------------------------|
| batch_size | **8** | **4** |
| max_new_tokens | 1024 | 1024 |
| model_path | rsft_output (parent dir) | rsft_output/**checkpoint-510** |
| no_evidence | 未设置 | false |
| inference_time | 6034s | 10816s |
| n_predictions | 15307 | 15436 |
| ign_f1 来源 | metrics_v2.json (recomputed) | metrics.json (原始) |

### 论文引用溯源

- **experiments.tex（当前主表）**: s42 = **44.23** ← 来自 rsft_ced_s42_reeval（Protocol B）
- **paper_main_tables_draft.md（旧草稿）**: s42 = **43.63** ← 来自 rsft_r1/metrics_v2（Protocol A），标注 `mvp2_eval_rsft_r1`
- **dream_reports/worst/paper.tex**: s42 = **43.63** ← 旧协议值

### 关键发现

1. **当前 experiments.tex 的主表用的是 44.23**，与 variance 计算中的 reeval_ced_s42 一致。43.63 只出现在旧草稿和 "worst" dream report 中。

2. **Protocol B（CED reeval）三个 seed 内部一致：** 都用 batch_size=4、max_new_tokens=1024，std=0.51pp。

3. **但 s43 的训练模型不同：** s42 和 s44 的 CED reeval 用的是旧训练模型（rsft_output、rsft_output_s44），而 s43 用的是 **重新训练的** rsft_output_ced_s43。这意味着 3-seed variance 测的不全是 "相同训练方法、不同随机种子" 的方差——s43 可能是不同的训练 run。

4. **旧草稿的 3-seed 值 (43.63/45.85/45.51)** 也使用了 s42 和 s44 的旧模型 + s43 的旧模型（rsft_output_s43，非 CED），eval 协议是 batch_size=8，std=1.20pp。

### 结论

- **论文主表（experiments.tex）与 variance 计算是一致的**，都用 44.23。如果 Director 看到的 43.63 来自旧草稿或 dream report，则不存在不一致问题。
- 如果 Director 需要用 43.63，则必须同时将 s43 改为 45.85、s44 改为 45.51（Protocol A 全集），此时 std 变为 1.20pp。
- **建议确认 s43 的训练模型差异**：rsft_output_s43 vs rsft_output_ced_s43 是否为相同训练方法（只是命名不同），还是不同的 CED 配置。如果不同，当前 3-seed variance 的解释需要修改。

---
