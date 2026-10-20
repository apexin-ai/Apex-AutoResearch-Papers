# code fix metrics linalg

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_metrics_linalg_20260518T231744_result.json`
- **Structured JSON:** [`8812c85db4457f7f3c98.json`](../../sessions/88/8812c85db4457f7f3c98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。报告：

---

### 1. metrics.py 修改内容

**修改 A — `compute_effective_rank` (L204)**：`np.linalg.eigvalsh(cov)` 加 try/except，失败时 fallback 到 `np.linalg.svd`，SVD 也失败则返回 NaN。额外增加空 eigenvalues 保护。

**修改 B — `compute_all_metrics` (L313)**：将所有 metric 调用统一包裹在 try/except 中（之前只有 MAUVE 有保护）。单个 metric 失败返回 NaN，不终止实验。

### 2. 两台服务器 md5sum
- westd-17855: `036c8ca287c224d92323a322ae5c14db`
- westd-19828: `036c8ca287c224d92323a322ae5c14db`
- **一致**

### 3. 新实验
- 实验 ID: `interv_pred_a075_s42_fp32_v2`
- PID: **62752** (westd-17855, cuda:4)
- tmux session: `interv_pred_fp32_v3`
- output_dir: `results/intervention/predictive_te_a075_s42_fp32_v2`

### 4. 其他实验风险评估
- **qwen35_08b_fp32**: 运行中，35% (1747/5000 steps)，仍在训练阶段。metrics.py 已修复，到 metrics 计算时会有保护。**安全**。
- **a060_s42_fp32 / a005_s42_fp32**: 无活跃 tmux session（可能在其他服务器或已完成）。
- **scale_69b_a100_s42 / alpha_sweep_a010_s43**: 也在 westd-17855 运行，metrics.py 修复已生效。

---
