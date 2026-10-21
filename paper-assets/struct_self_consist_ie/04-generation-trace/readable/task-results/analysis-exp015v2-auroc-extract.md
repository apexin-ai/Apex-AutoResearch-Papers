# analysis exp015v2 auroc extract

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp015v2_auroc_extract_20260514T222132_result.json`
- **Structured JSON:** [`670b5413077ba4670f69.json`](../../sessions/67/670b5413077ba4670f69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the raw data. Let me compile the results.

## Complete findings

### 1. SciERC NER AUROC — all 5 sections (precise values from JSON)

| Section | N | Voting | SJ | FK | EM | Logprob |
|---|---|---|---|---|---|---|
| `scierc_n8_logprob_ner` | 8 | 0.74092 | 0.71516 | 0.62872 | 0.75675 | 0.58058 |
| `scierc_n16_seed42_ner` | 16 | 0.73401 | 0.73676 | 0.60992 | 0.79023 | 0.58698 |
| `scierc_n16_seed123_ner` | 16 | 0.71665 | 0.73629 | 0.62682 | 0.78070 | 0.60621 |
| `scierc_re_n16_ner` | 16 | 0.74018 | 0.75203 | 0.61134 | 0.80193 | 0.59436 |
| `scierc_re_seed123_ner` | 16 | 0.75156 | 0.75654 | 0.60927 | 0.80704 | 0.59099 |
| **Recomputed avg (5)** | | **0.7367** | **0.7394** | **0.6172** | **0.7873** | **0.5918** |
| **Registry `scierc_ner_avg`** | | **0.7367** | **0.7328** | **0.6172** | **0.7873** | **0.5918** |

### 2. SciERC RE AUROC — all 5 sections

| Section | N | Voting | SJ | FK | EM | Logprob |
|---|---|---|---|---|---|---|
| `scierc_n8_logprob_re` | 8 | 0.72557 | 0.66558 | 0.61385 | 0.68681 | 0.60612 |
| `scierc_n16_seed42_re` | 16 | 0.73478 | 0.69391 | 0.60582 | 0.73996 | 0.58718 |
| `scierc_n16_seed123_re` | 16 | 0.72875 | 0.67792 | 0.59365 | 0.71563 | 0.59164 |
| `scierc_re_n16_re` | 16 | 0.71735 | 0.66690 | 0.58362 | 0.72325 | 0.56879 |
| `scierc_re_seed123_re` | 16 | 0.71051 | 0.66845 | 0.57238 | 0.70923 | 0.57086 |
| **Recomputed avg (5)** | | **0.7234** | **0.6746** | **0.5939** | **0.7150** | **0.5849** |
| **Registry `scierc_re_avg`** | | **0.7195** | **0.6788** | **0.5939** | **0.7150** | **0.5849** |

### 3. 关键发现

**D052 Table 1 NER AUROC** (.741, .715, .629, .757, .581) 来源是 `scierc_n8_logprob_ner`（N=8 单一实验），不是多seed平均值。

**Registry `scierc_ner_avg` 含义**：5个SciERC NER sections 的算术平均（包含 N=8 + 4个 N=16）。这是 worker 手动计算后写入 registry 的（见 worker log line 271）。

**Registry 与真实数据的不一致**：

| Signal | Registry | Recomputed | 差异 |
|---|---|---|---|
| **SJ NER** | **0.7328** | **0.7394** | **-0.0066 (错误)** |
| FK NER | 0.6172 | 0.6172 | 0 |
| logprob NER | 0.5918 | 0.5918 | 0 |
| EM NER | 0.7873 | 0.7873 | 0 |
| Voting NER | 0.7367 | 0.7367 | 0 |
| **Voting RE** | **0.7195** | **0.7234** | **-0.0039 (错误)** |
| **SJ RE** | **0.6788** | **0.6746** | **+0.0042 (错误)** |
| FK RE | 0.5939 | 0.5939 | 0 |
| EM RE | 0.7150 | 0.7150 | 0 |
| logprob RE | 0.5849 | 0.5849 | 0 |

**SJ NER、Voting RE、SJ RE 三个 registry 值与 JSON 原始数据不一致**。FK/logprob/EM 完全吻合。问题出在 worker 手动填写 registry 时的计算错误。

### 4. `scierc_ner_avg` 的组成

平均覆盖 **5 个 NER 评估**（不是3个），包括：
- 1 个 N=8 实验 (`exp_012_logprob`)
- 2 个 N=16 主实验 (`exp_001_seed42_v2`, `exp_001_seed123_v2`)
- 2 个 N=16 RE实验的 NER 副产品 (`exp_008_re_n16_v2`, `exp_008_re_seed123`)

### 5. N=16 下 SciERC NER 值（仅4个N=16 sections）

| Signal | seed42 | seed123 | re_n16 | re_seed123 | N=16 avg |
|---|---|---|---|---|---|
| Voting | 0.7340 | 0.7167 | 0.7402 | 0.7516 | 0.7356 |
| SJ | 0.7368 | 0.7363 | 0.7520 | 0.7565 | 0.7454 |
| FK | 0.6099 | 0.6268 | 0.6113 | 0.6093 | 0.6143 |
| EM | 0.7902 | 0.7807 | 0.8019 | 0.8070 | 0.7950 |
| Logprob | 0.5870 | 0.6062 | 0.5944 | 0.5910 | 0.5946 |

---
