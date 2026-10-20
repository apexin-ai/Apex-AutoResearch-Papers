# check exp002 signal pipeline p0b

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp002_signal_pipeline_p0b_20260514T161744_result.json`
- **Structured JSON:** [`38b3cbe6456c25e8ae64.json`](../../sessions/38/38b3cbe6456c25e8ae64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-002 信号管线代码完成度报告

### 1. 代码状态

| Signal | 文件 | 行数 | 状态 |
|--------|------|------|------|
| S1 Embedding | `signal_embedding.py` | 197 | ✅ 完成 |
| S2 Min-K%++ | `signal_minkpp.py` | 237 | ✅ 完成 |
| S3 ConStat | `signal_constat.py` | 114 | ✅ 完成 |
| S4 Self-Critique | `signal_selfcritique.py` | 268 | ✅ 完成 |
| 主入口 | `compute_signals.py` | 209 | ✅ 完成（支持 4 signal 选择性计算+merge） |
| 批量运行 | `run_batch.py` | 256 | ✅ 完成 |
| RRF 聚合 | `aggregate_rrf.py` | 340 | ✅ 完成 |

**代码 100% 齐全，无缺失。**

### 2. 已有信号计算结果（0.5B, `/root/autodl-tmp/exp002/signals/`）

| Dosage | S1 Embedding | S2 Min-K%++ | S3 ConStat | S4 Self-Critique | Merged |
|--------|-------------|-------------|------------|------------------|--------|
| d000 | ✅ mmlu/gsm8k/arc | ✅ mmlu/gsm8k/arc | ❌ 无 | ✅ mmlu/gsm8k/arc | ✅ (不含S3) |
| d005 | ✅ mmlu/gsm8k/arc | ✅ mmlu/gsm8k/arc | ❌ 无 | ✅ mmlu/gsm8k/arc | ✅ (不含S3) |
| d100 | ✅ mmlu/gsm8k/arc | ✅ mmlu/gsm8k/arc | ❌ 无 | ✅ mmlu/gsm8k/arc | ✅ (不含S3) |

### 3. S3 ConStat 可启动性（需 original + paraphrase aligned eval pair）

| Dosage | original_aligned | para_aligned | S3 可计算？ |
|--------|-----------------|--------------|-----------|
| d000_s42 | ✅ | ✅ | **可立即启动** |
| d005_s42 | ✅ | ✅ | **可立即启动** |
| d025_s42 | ✅ | ✅ | 可启动（但 d025 不在原 exp-002 三dosage集中） |
| d100_s42 | ✅ | ❌ 缺失 | **阻塞 — 需先跑 paraphrase eval** |

### 4. 结论

- **代码无缺失**，4 个 signal 的计算模块全部就绪
- **S3 ConStat 是唯一未计算的 signal**，瓶颈在上游 paraphrase eval 数据
- **d000 和 d005 可立即计算 S3**（para_aligned 已就绪）
- **d100 被阻塞**：缺 `Qwen2.5-0.5B_d100_s42_para_aligned/eval_results.json`，需先运行 d100 的 paraphrase evaluation

---
