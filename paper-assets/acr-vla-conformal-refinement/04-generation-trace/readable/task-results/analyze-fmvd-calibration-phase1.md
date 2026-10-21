# analyze fmvd calibration phase1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_fmvd-calibration-phase1_20260519T190320_result.json`
- **Structured JSON:** [`54fcf4dac1339a1624e6.json`](../../sessions/54/54fcf4dac1339a1624e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

---

## FMVD Calibration Phase 1 — 结果汇总

### 判定: **NO-GO** ❌

| 指标 | 值 |
|------|-----|
| **Spearman ρ** | **0.0825** (阈值 0.3) |
| p-value | 2.33e-23 |
| 样本量 | 14,512 steps |
| FMVD | mean=0.055, std=0.040 |
| K10 variance | mean=0.005, std=0.006 |
| 任务成功率 | 3/50 episodes (6%) |

### 关键观察

1. **相关性极弱**: ρ=0.083 远低于 0.3 阈值，FMVD 信号无法有效预测 K=10 action variance。虽然 p-value 极小（统计显著），但这仅因样本量大——实际效应量可忽略不计。

2. **FMVD 信号本身有变化**: 分布有合理 spread（P25=0.028, P90=0.094），说明 ODE 轨迹湍流度确实在不同 step 有差异，但这个差异与多推理 variance 不对应。

3. **模型在 Object 上表现很差**: 仅 3 个 episode 成功（salad_dressing、tomato_sauce、chocolate_pudding 各 1 次），大部分跑满 300 步超时。低成功率意味着模型大部分时间处于失败状态，可能掩盖了 FMVD 在成功/接近成功 episode 上的信号。

4. **无 error/warning**: 日志干净，仅有一个无关的 `DeprecationWarning: swigvarlink`。

### 结论

FMVD（单次推理 ODE 速度离散度）不能作为 Adaptive K 的触发信号。Adaptive K 机制需要寻找其他不确定性代理指标，或者放弃单次推理预测多推理 variance 的路线。

- **log_path**: `~/runs/acr-vla-conformal-refinement/fmvd-calibration-phase1.log`
- **checkpoint_path**: `/root/acr-vla-conformal-refinement/logs/fmvd_calibration.json`
- **Registry**: status=DONE, conclusion=negative

---
