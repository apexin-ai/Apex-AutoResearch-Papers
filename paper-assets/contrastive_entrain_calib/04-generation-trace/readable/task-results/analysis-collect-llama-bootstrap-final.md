# analysis collect llama bootstrap final

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_collect-llama-bootstrap-final_20260522T125217_result.json`
- **Structured JSON:** [`dc1c2d2c47fbca81ed29.json`](../../sessions/dc/dc1c2d2c47fbca81ed29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果已收集。以下是 **Llama-3-8B** 部分的 bootstrap AUROC CI 最终结果：

### Llama-3-8B (style-controlled, 181 pairs)

| 指标 | AUROC | 95% CI |
|------|-------|--------|
| **5-fold CV mean** | 0.7793 | std=0.0189, folds=[0.757, 0.773, 0.779, 0.814, 0.774] |
| **OOF bootstrap** (n=10000) | 0.7745 | [0.7418, 0.8094] |
| **Full CV bootstrap** (n=2000) | **0.7811** | **[0.7448, 0.8189]** |
| weak (n=75) | 0.7028 | [0.6484, 0.7625] |
| medium (n=54) | 0.8594 | [0.8097, 0.9119] |
| strong (n=52) | 0.9079 | [0.8617, 0.9508] |

### 附：Qwen3-8B 对比 & Random Baseline

- Qwen3-8B Full CV bootstrap: **0.8253 [0.7952, 0.8572]**
- Random baseline (200 dirs): mean=0.6853, max=0.7980
- d_syc vs random diff: −0.0094 [−0.0427, 0.0240], P(d_syc > random)=0.2908

结果已保存至服务器 `/root/contrastive_entrain_calib/artifacts/bootstrap_auroc_ci.json`。

---
