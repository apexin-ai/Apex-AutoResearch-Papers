# code exp51 adapt curve

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp51_adapt_curve_20260522T094532_result.json`
- **Structured JSON:** [`ba4e03eaf5f02c438464.json`](../../sessions/ba/ba4e03eaf5f02c438464.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果汇总：

| N | FPR | IID F1 | DD F1 | AA F1 | FITD F1 |
|---|-----|--------|-------|-------|---------|
| 0 | 57.5% | - | - | - | - |
| 10 | 20.5% | 1.0 | 1.0 | 1.0 | 1.0 |
| **25** | **1.5%** | 1.0 | 1.0 | 0.953 | 1.0 |
| **50** | **0.5%** | 1.0 | 1.0 | 0.990 | 1.0 |

- FPR 拐点在 N=25：从 20.5% 骤降到 1.5%（仅 3/200 误报）
- N=50 进一步降至 0.5%（1/200），但未完全到 0%
- OOD 检测能力完好：DD/FITD F1=1.0，AA F1 在 N=25 时略降到 0.953 但 N=50 回升到 0.990
- IID F1 全程 1.0

结果已保存至服务器 `results/exp51_oasst2_adapt_curve.json` 并注册为 artifact `art_20260522_a48c36`。

---
