# diagnosis exp003 ckpt5000 result and pipeline

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp003-ckpt5000-result-and-pipeline_20260520T122050_result.json`
- **Structured JSON:** [`a326911c415a61683d0a.json`](../../sessions/a3/a326911c415a61683d0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-003 ckpt-5000 Eval (28034)
状态：**进行中** — 300/362 pairs @ 20:20，~5min/20pairs，预计 ~20:35 完成
结果目录为空（json 在全部完成后写入）

## 29046 exp-003 Checkpoints
已有：checkpoint-500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, **5000**（共 10 个）
当前训练（`exp-003-s2.log`）：step **1270/8000**，~27s/it → 尚未产出 5500+ checkpoint

## 28034 GPU (post-kill)
| GPU | Util | VRAM | 占用者 |
|-----|------|------|--------|
| 0 | 49% | 16.5/31.8 GB | exp-003 eval (ckpt-5000) |
| 1 | 66% | 30.7/31.8 GB | **exp-009 仍在运行** |
| 2 | 63% | 29.9/31.8 GB | **exp-009 仍在运行** |
| 3 | 0% | 4 MB / 31.8 GB | **空闲** |

**注意：exp-009 未被 kill。** `run_exp009_continuous_probe_grpo.py` 的两个 rank（PID 200881, 200882）从 11:06 起持续运行在 GPU 1+2，deepspeed launcher（PID 200288, 200584）也存活。GPU 1+2 未释放，仅 GPU 3 空闲。

---
