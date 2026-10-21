# eval exp 003 s2 eval ckpt2000

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp-003-s2-eval-ckpt2000_20260521T081805_result.json`
- **Structured JSON:** [`a9048728c3389b1593e4.json`](../../sessions/a9/a9048728c3389b1593e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 执行结果

### exp-003-s2-eval-ckpt2000 — 已提交，正在运行

- **Server**: westd-28034, GPU 3
- **tmux session**: `exp-003-s2-eval-ckpt2000`
- **Log**: `~/runs/contrastive_entrain_calib/exp-003-s2-eval-ckpt2000.log`
- **Registry**: RUNNING，spec 已补充

**注意**：GPU 3 已有 exp003s2-ckpt3000 eval 在跑（~9 分钟），两个 eval 共享 GPU（29.8GB/32GB）。模型部分 offload 到 CPU，eval 能运行但会比正常慢。ckpt-3000 完成后（预计 ~50 分钟），GPU 释放，ckpt-2000 eval 速度会恢复正常。

### ckpt-7500 同步 — 阻塞

- checkpoint-7500 位于 westd-29046: `/root/autodl-tmp/checkpoints/exp003_r3only_seed1/checkpoint-7500/`（719MB）
- westd-28034 上 exp003 已有到 checkpoint-7000，缺 7500
- **两台服务器无直连 SSH**（无 `.ssh/config` 互通），无法直接 SCP
- 需要手动中转或配置服务器间 SSH 密钥才能同步

---
