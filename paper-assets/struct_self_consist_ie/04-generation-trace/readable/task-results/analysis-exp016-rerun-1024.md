# analysis exp016 rerun 1024

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp016_rerun_1024_20260514T231500_result.json`
- **Structured JSON:** [`166f5b93ac548cc0bbb6.json`](../../sessions/16/166f5b93ac548cc0bbb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 修正数值汇总

### 1. Ensemble AUROC（5-fold CV Logistic Regression）

| Subtask | Original (512) | Corrected (1024) | Δ |
|---------|----------------|------------------|------|
| **NER** | 0.735 ± 0.030 | **0.666 ± 0.070** | −0.069 |
| **RE** | 0.719 ± 0.027 | **0.662 ± 0.078** | −0.057 |

单信号 AUROC（exp_016 5-fold CV）:

| Signal | NER orig → corr | RE orig → corr |
|--------|-----------------|----------------|
| soft_jaccard | 0.689 → **0.670** | 0.591 → **0.634** |
| fleiss_kappa | 0.632 → **0.614** | 0.628 → **0.643** |
| logprob | 0.587 → **0.611** | 0.621 → **0.622** |
| exact_match | 0.662 → **0.652** | 0.496 → **0.576** |
| voting_conf | 0.700 → **0.607** | 0.721 → **0.680** |

### 2. Best-of-N Selection F1

**NER (n=529)**

| Method | Original (512) | Corrected (1024) | Δ |
|--------|----------------|------------------|------|
| greedy | 0.6094 | **0.6439** | +0.035 |
| random_avg | 0.5796 | **0.6077** | +0.028 |
| sj_best | 0.6042 | **0.6450** | +0.041 |
| voting_conf_best | 0.5959 | **0.6337** | +0.038 |
| logprob_best | 0.6087 | **0.6501** | +0.041 |
| ensemble_best | 0.6043 | **0.6450** | +0.041 |
| oracle | 0.7692 | **0.7758** | +0.007 |

**RE (n=397)**

| Method | Original (512) | Corrected (1024) | Δ |
|--------|----------------|------------------|------|
| greedy | 0.3735 | **0.4042** | +0.031 |
| random_avg | 0.3380 | **0.3544** | +0.016 |
| sj_best | 0.3680 | **0.3855** | +0.018 |
| voting_conf_best | 0.3379 | **0.3592** | +0.021 |
| logprob_best | 0.3971 | **0.3948** | −0.002 |
| ensemble_best | 0.3673 | **0.3855** | +0.018 |
| oracle | 0.5608 | **0.5850** | +0.024 |

### 3. ECE（from all_signals_5signal, full set）

| Signal | NER ECE | RE ECE |
|--------|---------|--------|
| SJ | 0.4531 | 0.3865 |
| FK | 0.4512 | 0.4405 |
| logprob | 0.7064 | 0.7694 |
| EM | 0.3526 | 0.3548 |
| voting_conf | 0.3807 | 0.2724 |

（ECE 无原始 512 对比值，`all_signals_5signal.json` 仅 1024 版本存在）

### 关键发现

- **Ensemble AUROC 显著下降**：NER 0.735→0.666 (−7pp)，RE 0.719→0.662 (−6pp)。原 512 截断数据人为降低了 sample 多样性，使信号区分度虚高。
- **F1 全面上升**：所有方法 F1 提高 2-4pp，因 1024 token 让模型输出更完整。
- **logprob 信号改善**：logprob 的 AUROC 和 ρ 提升（NER: 0.140→0.205, RE: 0.247→0.266），说明截断损害了 logprob 信号质量。
- **voting_conf AUROC 下降明显**（NER: 0.700→0.607），可能因为完整输出下 voting 模式更分散。

结果保存在服务器 `output/exp_016_rerun_1024/`。

---
