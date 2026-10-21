# code repe direction probe v3

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_repe_direction_probe_v3_20260517T121511_result.json`
- **Structured JSON:** [`fadc8a0dfaa4ddcac7cd.json`](../../sessions/fa/fadc8a0dfaa4ddcac7cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。结果已保存到 `results_repe_direction.json`。

**4 模型 RepE 方向探针结果：**

| Model | bal_acc | precision | pre_cp_fpr | coverage | lead_mean |
|-------|---------|-----------|------------|----------|-----------|
| r1-8b | 0.7491 | 0.5160 | 0.2264 | 0.3953 | +9.7 |
| r1-32b | 0.6707 | 0.5538 | 0.2423 | 0.4500 | +6.3 |
| qwq-32b | 0.6661 | 0.4193 | 0.3997 | 0.7368 | +13.4 |
| ot-7b | 0.7180 | 0.3733 | 0.2573 | 0.5319 | +26.1 |

**与 LR Probe 对比（r1-8b）：**
- bal_acc: RepE 0.749 vs LR 0.817 (-0.068)
- precision: RepE 0.516 vs LR 0.693 (-0.177)
- pre_cp_fpr: RepE 0.226 vs LR 0.097 (+0.130, worse)
- coverage: RepE 0.395 vs LR 0.465 (-0.070)
- lead_mean: RepE +9.7 vs LR -2.0 (RepE detects much earlier when it does detect)

RepE 方向探针整体 accuracy/precision 低于 LR probe，但 lead_mean 显著更大（检测更早）。这符合预期：单方向投影是比 LR 更弱的线性分类器，但它提取的 "safety direction" 在 commitment 之前就已经有信号，所以 crossing 更早（代价是更高 FPR）。

---
