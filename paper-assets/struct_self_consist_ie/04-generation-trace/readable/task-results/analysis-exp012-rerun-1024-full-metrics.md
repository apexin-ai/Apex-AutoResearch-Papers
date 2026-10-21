# analysis exp012 rerun 1024 full metrics

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp012_rerun_1024_full_metrics_20260514T224814_result.json`
- **Structured JSON:** [`728011fc94b785697488.json`](../../sessions/72/728011fc94b785697488.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## 产出 1：exp_012_rerun_1024 完整 5 信号指标

### NER (full, n=529)

| Signal | ρ | τ | AUROC | ECE |
|--------|------|------|-------|------|
| **SJ** | 0.3599 | 0.2646 | 0.6917 | 0.4531 |
| **FK** | 0.2665 | 0.1974 | 0.6290 | 0.4512 |
| **logprob** | 0.2052 | 0.1478 | 0.5783 | 0.7064 |
| **EM** | 0.2945 | 0.2208 | **0.7493** | 0.3526 |
| **voting_conf** | **0.3792** | **0.2805** | 0.6841 | 0.3807 |

### NER (conditional, n=477)

| Signal | ρ | τ | AUROC | ECE |
|--------|------|------|-------|------|
| **SJ** | 0.3113 | 0.2257 | 0.6772 | 0.4416 |
| **FK** | 0.1761 | 0.1284 | 0.6078 | 0.4389 |
| **logprob** | 0.1538 | 0.1111 | 0.5633 | 0.6803 |
| **EM** | **0.3596** | **0.2735** | **0.7556** | 0.3257 |
| **voting_conf** | 0.3000 | 0.2189 | 0.6618 | 0.3746 |

### RE (full, n=397)

| Signal | ρ | τ | AUROC | ECE |
|--------|------|------|-------|------|
| **SJ** | 0.2503 | 0.1878 | 0.6702 | 0.3865 |
| **FK** | 0.2752 | 0.2117 | 0.6089 | 0.4405 |
| **logprob** | 0.2662 | 0.1951 | 0.6005 | 0.7694 |
| **EM** | 0.1344 | 0.1081 | **0.7059** | 0.3548 |
| **voting_conf** | **0.3498** | **0.2663** | 0.6935 | 0.2724 |

### RE (conditional, n=238)

| Signal | ρ | τ | AUROC | ECE |
|--------|------|------|-------|------|
| **SJ** | 0.2457 | 0.1811 | 0.6463 | 0.2941 |
| **FK** | 0.1139 | 0.0876 | 0.5510 | 0.3424 |
| **logprob** | 0.0112 | 0.0051 | 0.5186 | 0.6464 |
| **EM** | **0.4165** | **0.3256** | **0.7515** | 0.2232 |
| **voting_conf** | 0.2409 | 0.1780 | 0.6420 | 0.2070 |

---

## 产出 2：数据溯源结论

**exp_015_v2 的 scierc_n8_logprob 数据确认受 exp_012 截断影响。**

- 数据源：`exp_012_logprob/samples_with_logprobs.jsonl`（max_tokens=512 生成）
- 关键偏差（NER full ρ）：
  - **voting_conf 被高估**：0.5018 → 0.3792（Δ = -0.1226）
  - **logprob 被低估**：0.1396 → 0.2052（Δ = +0.0656）
  - **EM 被低估**：0.2566 → 0.2945（Δ = +0.0379）
  - SJ/FK 变化很小（<0.004）
- 原因：截断导致生成多样性降低，voting_conf 虚高；截断 token 的 logprob 不准确，压低了 logprob 信号

---

## 产出 3：Registry 已更新

- `exp_012_rerun_1024`：DONE(success)，完整 5 信号 × 4 指标 × NER/RE × full/cond 已录入
- `exp_001_seed456_v2_ner_r1024`：conclusion 已标记为 killed

---
