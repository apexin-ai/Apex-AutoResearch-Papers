# code exp B 14d ablation

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_B_14d_ablation_20260515T102300_result.json`
- **Structured JSON:** [`bb9afd6a77f41db88011.json`](../../sessions/bb/bb9afd6a77f41db88011.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

EXP-B 完成。结果摘要：

### 14D Ablation（去除 self_bleu）

| Config | 15D K* | 14D K* | 1v2 Delta | Mean Delta |
|--------|--------|--------|-----------|------------|
| Qwen-rw | 2 | 2 | -0.0073 | |
| Pythia | 2 | 2 | +0.0008 | |
| OLMo | 2 | 2 | -0.0112 | |
| Qwen-cont | 2 | 2 | -0.0087 | |
| **Overall** | | | | **-0.0015** |

**K\* = 2 在全部 4 个 config 上不变。** 平均 AUC 变化仅 -0.0015，最大单对变化为 OLMo 1v2 的 -0.0112。去除 self_bleu 的 15D→14D 降维对分类性能影响可忽略。

结果已保存到 `artifacts/exp_B_14d_ablation.json`，脚本在 `scripts/exp_B_14d_ablation.py`。

---
