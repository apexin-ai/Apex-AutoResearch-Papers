# ops volctrl urgent check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_volctrl-urgent-check_20260523T014243_result.json`
- **Structured JSON:** [`f362f96da524c93604b2.json`](../../sessions/f3/f362f96da524c93604b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### Part 1: Volume Control 训练状态 — **运行中**

| 指标 | 值 |
|------|-----|
| 进度 | **718 / 4159** (17%) |
| Loss | ~1.22 (下降趋势，从 1.36 降到 1.22) |
| LR | ~5e-5 (已达峰值，cosine decay 开始) |
| 速度 | ~4.0 s/step |
| GPU | cuda:0, PID 752802, 19.6GB/24GB VRAM, 65% util |
| ETA | **~3.8 小时** (~13:30 UTC) |
| Checkpoint | lora_adapter 目录已创建但尚为空（尚未保存 checkpoint） |

### Part 2: Eval — **未启动**

训练仍在进行，GPU 被占用。训练完成后再启动 eval。

### Part 3: Registry 修复结果

| 实验 | 修复前 | 修复后 |
|------|--------|--------|
| `sft_falcon3_7b_d100_s123_v2` | RUNNING | **DONE** (conclusion=success, checkpoint_path + log_path 已设置) |
| `eval_falcon3_d100_s123` | RUNNING (conclusion=success 已有) | **DONE** (MMLU 62.68%, ARC 84.22%) |
| `sft_falcon3_7b_volume_control` | PREPARING | **RUNNING** (PID 752802, spec 已填充) |

---
