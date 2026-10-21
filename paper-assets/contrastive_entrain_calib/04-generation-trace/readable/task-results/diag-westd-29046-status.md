# diag westd 29046 status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd-29046-status_20260518T220445_result.json`
- **Structured JSON:** [`891aea6bc0030f0eb9d5.json`](../../sessions/89/891aea6bc0030f0eb9d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the full status report:

---

## 实验状态报告 (2026-05-19 06:06 UTC)

### 1. exp-002 — DC-GRPO 主实验 (GPU 0, PID 69020)

| 指标 | 值 |
|------|-----|
| 当前 step | **697 / 8,000** (8.7%) |
| per-step 时间 | ~25.9s/it |
| 已运行 | 5h 22m |
| 预计剩余 | **~52.5h** (约 May 21 10:30 UTC) |

**Reward 趋势 (summary steps):**

| Step | R1_mean | R3_mean | Combined |
|------|---------|---------|----------|
| 500 | -0.2261 | 0.5476 | 0.4028 |
| 600 | -0.2452 | 0.2564 | 0.0992 |
| 660 | -0.0007 | 0.7350 | 0.5824 |
| 680 | +0.2507 | 0.3707 | 0.2471 |
| 690 | -0.0083 | 0.3800 | 0.2523 |

**R1 分析:** R1_mean 在 step 500 后**没有明显改善**，仍在 [-0.75, +0.49] 间剧烈震荡，均值接近 0（对比 step 256 时的 -0.33，只是方差增大了）。R2 恒定为 0.0（weight=0，符合预期）。R3 波动较大（0.25~0.74），无清晰上升趋势。

**异常:** 无 error / NaN / OOM。

---

### 2. exp-003 — R3-only Baseline (GPU 1, PID 70649)

| 指标 | 值 |
|------|-----|
| 当前 step | **671 / 8,000** (8.4%) |
| per-step 时间 | ~26.1s/it |
| 已运行 | 5h 14m |
| 预计剩余 | **~53.2h** (约 May 21 11:20 UTC) |

**Reward 趋势:**

| Step | R3_mean | Combined |
|------|---------|----------|
| 500 | 0.3312 | 0.3312 |
| 600 | 0.6839 | 0.6839 |
| 620 | 0.8608 | 0.8608 |
| 660 | 0.6612 | 0.6612 |
| 670 | 0.5818 | 0.5818 |

**R3 分析:** R3 从 step 500 的 0.33 上升到 step 600-670 的 0.58-0.86 区间，有明显改善趋势，但近期有回落。无 R1/R2（设计如此，log 中有 `d_syc not loaded` 警告）。

**异常:** 无 error / NaN / OOM。

---

### 3. GPU 状态

| GPU | 利用率 | 显存 | 温度 |
|-----|--------|------|------|
| 0 (exp-002) | 83% | 63,603 / 97,887 MiB (65%) | 63°C |
| 1 (exp-003) | 95% | 38,161 / 97,887 MiB (39%) | 67°C |

两块 GPU 均健康，温度正常，无过热风险。

---

### 4. 进程健康

| PID | 实验 | 运行时间 | CPU | 状态 |
|-----|------|----------|-----|------|
| 69020 | exp-002 | 5h22m49s | 710% | 正常 |
| 70649 | exp-003 | 5h14m06s | 656% | 正常 |

---

### 5. exp-016 文件检查

| 文件 | 状态 |
|------|------|
| `eval/nli_utils.py` | ✅ 存在 (2,712 bytes, May 19 05:53) |
| `eval/eval_pipeline.py` | ❌ **不存在** |
| `training/run_exp016_actadd_steering.py` | ✅ 存在 (16,478 bytes, May 19 06:01) |

---

### 关键发现

1. **exp-002 的 R1 信号令人担忧** — step 500 后 R1_mean 没有改善迹象，围绕 0 震荡，方差极大（std≈1.0）。这意味着 DC-GRPO 的 contrastive direction 可能未在有效引导模型。
2. **exp-003 的 R3 表现更好** — R3-only baseline 的 R3 reward 在 step 600+ 已稳定在 0.55-0.86 区间，优于 exp-002 的 R3（0.25-0.74）。
3. **eval/eval_pipeline.py 缺失** — 需要创建或上传此文件才能运行 exp-016 的评估流程。
4. 两个实验都还需要约 **52-53 小时**完成（约 May 21 中午）。

---
