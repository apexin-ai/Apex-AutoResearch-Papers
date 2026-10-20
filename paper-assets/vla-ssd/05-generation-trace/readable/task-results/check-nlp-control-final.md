# check nlp control final

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_nlp_control_final_20260522T122710_result.json`
- **Structured JSON:** [`8c04f210dbeee5f3be02.json`](../../sessions/8c/8c04f210dbeee5f3be02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. 模型下载：未完成，快了
- **shard2** (3.3GB): 已完成，在主目录
- **shard1** (9.29GB): **97% (8.99/9.29GB)**，仍在 `._____temp/`，速度 ~300kB/s，ETA ~17 分钟
- 下载进程 PID 612753 活跃，已跑 ~7 小时（HF 下载速度极慢）

### 2. GPU
- 2× NVIDIA RTX PRO 6000 Blackwell (98GB each)
- 全部空闲，0% 利用率，无 GPU 进程

### 3. wait_and_run
- PID 613207 活跃，每 60s 轮询检查两个 shard 是否就位
- 当前仍在循环等待（log 只有一行 waiting 消息）
- 下载完成后会自动执行 `scripts/nlp_control_r2_probing.py --gpu 0`

### 4. Probing 结果
- **未开始**，等下载完成
- 结果目录只有空 run.log

### 预计时间线
下载剩余 ~300MB @ 300kB/s ≈ **17 分钟后**下载完成 → wait_and_run 检测到（最多再等 60s）→ 自动启动 probing。

---
