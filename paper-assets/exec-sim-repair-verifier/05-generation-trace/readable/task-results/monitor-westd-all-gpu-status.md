# monitor westd all gpu status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd-all-gpu-status_20260515T010954_result.json`
- **Structured JSON:** [`ec865f3a66d6afabc83e.json`](../../sessions/ec/ec865f3a66d6afabc83e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇报 (2026-05-15 ~09:16 UTC)

### nvidia-smi

| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX 5090 | 99% | 19.2 / 32.6 GB |
| 1 | RTX 5090 | 91% | 27.3 / 32.6 GB |
| 2 | RTX 5090 | 97% | 30.7 / 32.6 GB |
| 3 | RTX 5090 | 80% | 30.9 / 32.6 GB |

全部 4 卡在用。

---

### cuda:0 — cls8b-s42-ckpt1000-val8192-eval (PID 310114)
- **状态**: ALIVE, 运行 6m41s
- **进度**: 2100 / 9335 samples (22.5%)
- **Running accuracy**: 87.8%
- **速度**: ~3.9 samples/s (10 samples per ~2.5s)
- **预计完成**: ~09:45 UTC (剩余 ~30 min)

---

### cuda:1 — repo-level-cls-8b-s42-resume (PID 295789)
- **状态**: ALIVE, 进程运行 3h22m
- **进度**: 3279 / 9335 steps (35%)
- **速度**: tqdm 显示 ~12 it/s, 剩余估计 ~8 min
- **注意**: 3h22m 进程时间 vs 4m53s tqdm elapsed — 大部分时间在加载模型/数据/checkpoint. 训练本身跑得很快。
- **预计完成**: ~09:25 UTC (如 tqdm 准确)

---

### cuda:2 — repo-level-cwm-8b-conda (PID 266816)
- **状态**: ALIVE, 运行 7h26m
- **进度**: ~step 2750 / 6633 (41%)，从 checkpoint-1600 resume
- **最新 checkpoint**: 2700 (09:03 UTC)
- **速度**: ~39 min / 100 steps (23.4 s/step)
- **预计完成**: **~May 16 10:30 UTC** (剩余 ~25h)
- **注意**: 该进程未通过 agent 框架启动, "v4" log 不存在。进度通过 checkpoint 目录推断。

---

### cuda:3 — repo-level-cls-8b-seed123-conda-v3 (PID 266444)
- **状态**: ALIVE, 运行 7h29m
- **进度**: 5193 / 6633 steps (78.3%)，从 checkpoint-3000 resume
- **速度**: ~8.3 s/step
- **最新 checkpoint**: 5000 (刚保存)
- **Loss**: 0.2471, grad_norm: 0.047
- **预计完成**: ~12:35 UTC (剩余 ~3h19m)

---

### s42-resume 已生成 checkpoints
```
checkpoint-800, checkpoint-1000, checkpoint-1200, checkpoint-1400
```
当前正在 eval checkpoint-1000。下一个可 eval: **checkpoint-1200**。

---

### 异常
- **cwm "v4" log 不存在** — PID 266816 是直接 `python3 train_repo_cwm.py` 启动的（非 agent wrapper），stdout 可能在终端或 nohup.out，不在 `~/runs/` 目录。旧的 v3 log 以 EXIT_CODE=2 终止（参数错误）。
- **s42-resume 速度异常** — tqdm 显示 12 it/s 极快（vs seed123 的 8.3 s/step），可能是短序列或数据子集不同。建议确认该训练使用的数据集规模。

---
