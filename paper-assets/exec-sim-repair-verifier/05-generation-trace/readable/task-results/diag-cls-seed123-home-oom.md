# diag cls seed123 home oom

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_cls-seed123-home-oom_20260514T012018_result.json`
- **Structured JSON:** [`4442a4b55ba54bd6a735.json`](../../sessions/44/4442a4b55ba54bd6a735.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

情况清楚了。报告如下：

---

## 诊断报告

### GPU 当前状态
- PID 2947263（旧残留进程）已不存在
- **PID 3018282 正在运行**：`eval_repo_cls.py` 评估 checkpoint-200，tmux session `eval_cls_seed123`，已运行 ~2.5 分钟，占用 18420 MiB
- 这是一个**主动的 eval 任务**，不是残留进程，不应杀掉

### Checkpoint 情况
5 个 checkpoint 完整存在：200、400、600、800、1000
- 最新：checkpoint-1000（May 13 18:01）
- best checkpoint：checkpoint-200（eval_loss = 0.0772）

### 训练状态
训练**尚未完成**——跑到 step 1000 / 6633（epoch 0.45 / 3.0）。训练被中断而非完成（`should_training_stop: false`）。

| Step | Train Loss | Eval Loss |
|------|-----------|-----------|
| 200  | 1.5423    | **0.0772** (best) |
| 400  | 0.7862    | 0.1429 |
| 600  | 0.6569    | 0.1292 |
| 800  | 0.4035    | 0.2176 |
| 1000 | 0.4976    | 0.2612 |

Train loss 在下降但 **eval loss 从 step 200 起持续上升**（0.077 → 0.261），呈明显过拟合趋势。

### 建议
1. **不需要重启训练** — 训练虽只跑了 15%，但 eval loss 已连续 4 个 checkpoint 恶化，继续训练大概率无益
2. **用 checkpoint-200 做 eval**（当前已在进行中）
3. 等当前 eval 完成后 GPU 会释放，如果仍想继续训练可从 checkpoint-1000 resume，但建议先看 checkpoint-200 的 eval 结果再决定

---
