# diagnosis eval results collect

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_eval-results-collect_20260521T071315_result.json`
- **Structured JSON:** [`0554f44b7c8b8de291b6.json`](../../sessions/05/0554f44b7c8b8de291b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

情况清楚了。汇报如下：

---

## 28034 Eval 状态

### 4 个目标 eval 均未完成 — 原因：GPU 严重竞争

28034 上存在 **3 批重复的 eval 进程**（共 34 个 python 进程，11 个占用 GPU），导致 4 块 GPU 的 VRAM 接近满载（~30.5GB/32.6GB），eval 极慢：

| 批次 | 启动时间 | 特征 | GPU 占用 |
|------|----------|------|----------|
| Batch 1 (691xxx) | 12:41 | 无 `--data_path`，wrapper script | ~16.9GB/进程 |
| Batch 2 (693xxx) | ~12:43 | 中间批次 | ~12.9GB/进程 |
| Batch 3 (695xxx) | 12:47 | tmux session，有 `--data_path` | ~0.7-12.9GB/进程 |

4 块 GPU 各被 2-3 个进程占据，每块 ~30.5GB/32.6GB 已用。日志显示 4 个 eval 都停在 "Running eval on 362 pairs..." 阶段，输出只有 22-23 行（纯启动日志）。

**结果目录中没有 ckpt5000-v2/6000/6500/7000 的文件。** 已有的是更早完成的 batch：

| checkpoint | SYCONScore | ToF | NoF | 用时 |
|-----------|-----------|------|------|------|
| ckpt4500 | 0.1337 | 0.0718 | 0.9613 | 4280s |
| ckpt5500 | 0.1144 | 0.0608 | 0.9724 | 4484s |

### 建议操作

需要 **kill 掉重复的 Batch 1 和 Batch 2（或 Batch 3）**，只保留一组进程跑完。当前 3 组互相抢 VRAM 和算力，没有一组能正常完成。要我清理吗？

---

## 29046 训练状态

| 实验 | 最新 checkpoint | 进度 | 进程状态 | 备注 |
|------|----------------|------|----------|------|
| seed 1 (`exp003_r3only_seed1`) | **checkpoint-7500** (May 21 14:10) | 7500/8000 | **running** (PID 70649) | ~4.5h/500 steps，预计 ~4.5h 后完成 |
| seed 2 (`exp003_r3only_seed2`) | **checkpoint-3500** (May 21 15:00) | 3524/8000 | **running** (PID 237437) | 44%, ~31.6s/step, 预计还需 ~39h |

GPU 状态：2 块 GPU，utilization 0%（采样间隙），各占用 ~38GB/98GB VRAM，进程正常。

seed 1 的 tee 日志停在 step 3760（May 20），但 checkpoint 已到 7500，说明日志 buffer 未 flush 但训练正常推进。seed 2 log 实时显示 step 3524。

---
