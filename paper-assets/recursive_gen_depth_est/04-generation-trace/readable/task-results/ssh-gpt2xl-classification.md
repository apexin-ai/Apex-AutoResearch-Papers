# ssh gpt2xl classification

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpt2xl_classification_20260514T182506_result.json`
- **Structured JSON:** [`10167647d449892159ca.json`](../../sessions/10/10167647d449892159ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成，cron 不存在（无需删除）。

## GPT-2 XL 分类评估结果

### 4-class (RF, best)
| 指标 | GPT-2 XL | Pythia | OLMo |
|------|----------|--------|------|
| Accuracy | **83.3%** [82.3, 84.5] | 78.2% | 78.8% |
| AUC d1v2 | **0.9131** | 0.8607 | 0.8673 |
| AUC d2v3 | **0.8829** | 0.8005 | 0.8124 |
| AUC d0v1 | 0.9941 | — | — |
| AUC d1v3 | 0.9857 | — | — |

### 3-class (d1-d3 only, RF)
- Accuracy: **79.3%** [77.8, 80.6]
- AUC d1v2: 0.9109, d1v3: 0.9890, d2v3: 0.8885

### Top features
1. p90_ppl (0.208), 2. var_surprisal (0.208), 3. p75_ppl (0.103)

### Code contamination (broad)
d0: 0.5%, d1: 0.5%, d2: 1.3%, d3: 0.7% — 极低

GPT-2 XL 在所有指标上显著优于 Pythia (+5.1pp) 和 OLMo (+4.5pp)，可能因为跨模型 surprisal（用 Pythia 参考模型评估 GPT-2 XL 生成文本）放大了递归退化信号。

---
