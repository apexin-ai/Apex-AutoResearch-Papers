# ssh check olmo 002 completion

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_olmo_002_completion_20260514T181102_result.json`
- **Structured JSON:** [`4f5bc3362598c375fd99.json`](../../sessions/4f/4f5bc3362598c375fd99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能已被手动删除）。实验 registry 已更新为 DONE/success。

## cross_model_olmo_002 实验结果

**状态：SUCCESS**

### OLMo-1B 分类指标

| 指标 | OLMo-1B | Pythia-1.4B | 差异 |
|------|---------|-------------|------|
| **4-class acc (RF)** | **78.8%** [77.6, 80.0] | 78.2% [76.9, 79.4] | +0.6% |
| **AUC 1v2 (RF)** | **0.8673** | 0.8607 | +0.007 |
| **AUC 2v3 (RF)** | **0.8124** | 0.8005 | +0.012 |
| AUC 0v1 (RF) | 0.9834 | 0.9975 | -0.014 |
| AUC 1v3 (RF) | 0.9806 | 0.9685 | +0.012 |
| 4-class acc (LR) | 75.1% | 74.9% | +0.2% |

### 训练 Loss
- depth_0: 2.269
- depth_1: 1.650
- depth_2: 1.226

### Top Features
p90_ppl (0.18) > var_surprisal (0.16) > p75_ppl (0.11) > mean_surprisal (0.08) > type_token_ratio (0.06)

### 结论
OLMo-1B 结果与 Pythia baseline 高度一致，所有关键指标略优（4-class acc +0.6%, AUC 1v2 +0.007, AUC 2v3 +0.012）。递归生成深度的可区分性在跨模型条件下得到验证。

---
