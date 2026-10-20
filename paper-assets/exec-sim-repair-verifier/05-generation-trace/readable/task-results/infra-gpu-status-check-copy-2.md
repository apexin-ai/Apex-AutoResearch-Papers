# infra gpu status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-check_20260517T191705_result.json`
- **Structured JSON:** [`5b61d364fc6c3bf94ef7.json`](../../sessions/5b/5b61d364fc6c3bf94ef7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

**4 张 RTX 5090 全部在跑 eval，无空闲 GPU。**

| GPU | PID | 进程 | 显存 | GPU-Util | 运行时长 | 进度 | running_acc |
|-----|-----|------|------|----------|----------|------|-------------|
| 0 | 664774 | `eval_repo_cls.py` (v4 checkpoint-4422, seq=8192) | 28.5G/32.6G | 90% | 2h49m | 2840/9784 (29%) | **70.6%** |
| 1 | 662946 | `eval_repo_cwm.py` (s42 checkpoint, seq=4096) | 17.3G/32.6G | 60% | 2h56m | 874/9784 (9%) | **58.6%** |
| 2 | 665019 | `eval_repo_cls.py` (s123 best, seq=8192) | 31.3G/32.6G | 92% | 2h49m | 2520/9784 (26%) | **74.2%** |
| 3 | 668680 | `eval_repo_cwm.py` (s123 checkpoint-8844, seq=4096) | 17.3G/32.6G | 62% | 1h45m | 521/9784 (5%) | **63.0%** |

### PID 664774 确认

`eval_repo_cls.py` — CLS 分类模型 repo-level eval（v4 checkpoint-4422），运行 2h49m。

### tmux sessions

- `cls-v4-eval-8192` — GPU 0 的 CLS v4 eval
- `cls-s123-eval-8192` — GPU 2 的 CLS s123 eval
- `cwm-s123-eval` — GPU 3 的 CWM s123 eval
- GPU 1 的 CWM s42 eval 没有 tmux session（直接启动）

### 预计完成时间

- **CLS evals (GPU 0, 2)**: 每 40 samples ~2.5min → 剩余 ~7000 samples → 约 7h
- **CWM s42 (GPU 1)**: 每 sample ~13s → 剩余 ~8900 → 约 32h
- **CWM s123 (GPU 3)**: 每 sample ~12.5s → 剩余 ~9260 → 约 32h

CWM eval 速度很慢（逐样本生成 max_new_tokens=512），预计还需要 30+ 小时。CLS eval 约 7 小时后完成。

---
