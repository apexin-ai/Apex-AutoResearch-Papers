# code eval pipeline prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-pipeline-prep_20260527T071200_result.json`
- **Structured JSON:** [`122aecef1ac65034cff1.json`](../../sessions/12/122aecef1ac65034cff1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan registered as `art_20260527_eb1a25`.

## 关键发现

**⚠️ 2 个实验已崩溃（需立即处理）**：
- `detach_ln_v2_s0c_r2`（10894 cuda:2）和 `full_occ_ln_v2_s0d`（10894 cuda:3）已停止运行
- 两台 GPU 当前空闲（0% util），均有 20k checkpoint 可 resume
- 如果立即重启，~7.7h 后完成，仍在 DDL 内

**6 个实验正常训练中**：
- 34685: 2 个 57%（~5.5h），2 个 51%（~6.3h）
- 10894: 2 个 45%（~7h）

**Eval 脚本确认**：
- 脚本是 `evaluate_safelibero.py`（不是 `eval_libero.py`）
- 参数用 `--pretrained_checkpoint`（不是 `--checkpoint_path`）
- 默认 `num_rollouts=20`，需显式指定 `--num_rollouts 50`
- 需要 `MUJOCO_GL=egl` + `MUJOCO_EGL_DEVICE_ID` 匹配物理 GPU

**梯度分析**：
- `gradient_analysis_v2.py` 仅在 34685 上存在
- `run_gradient_analysis_v2.py` 不存在
- Cell 1/3/5 的已完成 checkpoint 在 34685，Cell 2 在 10894
- 建议等训练完成后再跑，所有 v2 checkpoint 齐备

**预估时间线**：所有 eval + 梯度分析 ~19:00 UTC May 27 完成，距 DDL 有 ~17h 缓冲。

---
