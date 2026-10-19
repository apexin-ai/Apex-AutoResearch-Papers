# analysis fmvd phase1 results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fmvd-phase1-results_20260519T192707_result.json`
- **Structured JSON:** [`31141227b8dfd011bbe7.json`](../../sessions/31/31141227b8dfd011bbe7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## FMVD Phase 1 校准结果

### Go/No-Go 判定：**NO-GO** ❌

| 指标 | 值 | 阈值 | 状态 |
|------|-----|------|------|
| **Overall Spearman ρ** | **0.0825** | > 0.3 | **未达标** |
| Spearman p-value | 2.33e-23 | — | 统计显著（但效应量太小） |

### 运行状态
- tmux session `fmvd-calibration-phase1`: **DEAD**（已结束）
- 输出文件: `fmvd_calibration.json`（3.3MB，May 20 02:59 写入，完整）
- 总数据量: 14,512 步 / 5 episodes / 10 tasks

### FMVD 分布
| 统计量 | 值 |
|--------|-----|
| Mean | 0.0549 |
| Std | 0.0403 |
| Range | [0.0048, 0.5024] |
| P25 / P50 / P75 / P90 | 0.0277 / 0.0467 / 0.0709 / 0.0938 |

### K10 Variance 分布
| 统计量 | 值 |
|--------|-----|
| Mean | 0.00489 |
| Std | 0.00564 |
| Range | [0.000187, 0.1235] |

### Per-Task Spearman ρ Breakdown

| Task | N | ρ | p-value | 方向 |
|------|---|---|---------|------|
| orange_juice | 1500 | **0.247** | 3.31e-22 | ✅ 正相关（最强） |
| salad_dressing | 1337 | **0.149** | 4.52e-08 | ✅ 正相关 |
| cream_cheese | 1500 | **0.127** | 7.43e-07 | ✅ 正相关 |
| alphabet_soup | 1500 | 0.104 | 5.06e-05 | 弱正相关 |
| butter | 1500 | 0.085 | 1.04e-03 | 弱正相关 |
| tomato_sauce | 1320 | 0.047 | 8.54e-02 | 不显著 |
| bbq_sauce | 1500 | 0.026 | 3.07e-01 | 不显著 |
| ketchup | 1500 | -0.036 | 1.62e-01 | 不显著 |
| chocolate_pudding | 1355 | -0.052 | 5.67e-02 | 不显著/弱负 |
| **milk** | 1500 | **-0.284** | 3.13e-29 | ❌ **显著负相关** |

### 关键发现

1. **Overall ρ=0.083 远低于 0.3 阈值**——FMVD 与 K10 variance 之间的单调关联性极弱
2. **任务间高度不一致**：ρ 从 -0.284（milk，显著反向）到 +0.247（orange_juice），方向都不统一
3. **milk 任务的负相关很强**（ρ=-0.284, p=3.13e-29），说明 FMVD 高时 K10 variance 反而低——这与校准假设直接矛盾
4. 只有 3 个任务 ρ > 0.1 且显著，7 个任务 ρ < 0.1 或不显著/负相关
5. 所有 episode 均 `episode_success: false`

**结论：FMVD 作为不确定性代理指标未通过校准验证，不建议直接用于 Adaptive K 机制。** 需要重新考虑代理指标的选择或引入 task-specific 校准。

---
