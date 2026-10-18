# monitor check dual experiments 20260516

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_check_dual_experiments_20260516_20260516T051340_result.json`
- **Structured JSON:** [`e9f9fe533534d38276ac.json`](../../sessions/e9/e9f9fe533534d38276ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态快照

### v8_1 (mvp_imm_anchor_v8_1)
- **进程状态**: alive (PID 121326, 运行 2h 0m 23s)
- **当前 step**: 22300/30000 (74.3%)
- **最近 loss**: 0.0261 (action=0.0141, margin=0.0598)
- **Δ (margin)**: 1.50 — 健康
- **速度**: 3.1 sps (每 step ~16s)
- **ETA**: 剩余 7700 steps ÷ 3.1 sps ≈ 2484s ≈ **~41 分钟** (约 13:55 完成)
- **Checkpoint**: step_022000 已保存

### v8b_twostage (mvp_imm_v8b_twostage)
- **进程状态**: alive (PID 136367, 运行 45m 10s)
- **Stage**: **Stage 2** (刚从 Stage 1 切换，13:10:15)
- **Stage 1**: 已完成 10000/10000 steps，checkpoint 已保存
- **Stage 2 当前 step**: 700/20000 (3.5%)
- **最近 loss**: 0.0226 (action only, LoRA fine-tuning)
- **速度**: 3.1 sps
- **ETA Stage 2**: 剩余 19300 steps ÷ 3.1 sps ≈ 6226s ≈ **~104 分钟** (约 14:58 完成)
- **问题**: 无错误，Stage 2 启动正常，ACIS 参数已冻结 (0 trainable)
- **注意**: bash wrapper PID 136351 已退出（正常，python 进程已独立运行）

### GPU
- **cuda:0**: 利用率 46%, 显存 2459/97887 MiB — v8b_twostage 占用（显存偏低，Stage 2 只训 LoRA）
- **cuda:1**: 利用率 95%, 显存 3581/97887 MiB — v8_1 占用

### 额外发现
- 两个实验显存占用都很低（<4GB/98GB），H800 大量显存空闲
- v8b_twostage 刚完成 Stage 1→Stage 2 切换（3分钟前），运行平稳无异常
- 无 HF 网络错误复发

---
