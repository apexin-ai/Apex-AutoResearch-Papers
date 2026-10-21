# ssh gpu5 conflict check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu5-conflict-check_20260513T234245_result.json`
- **Structured JSON:** [`48f0ec6fe7533375cde2.json`](../../sessions/48/48f0ec6fe7533375cde2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 5 状态报告

**冲突已确认，两个进程都已挂。**

### SFT 训练 (exp_001_sft_d005_05B, PID 235331)
- **OOM 崩溃**，在第 8/3177 step 挂掉，EXIT_CODE=1
- 错误信息明确指出冲突：eval 进程 (PID 234755) 占了 6.62 GiB，SFT 自身占了 14.15 GiB（含 non-PyTorch），再申请 3.45 GiB 时显存不够
- PID 235331 已不存在

### 3B Eval (eval_3B_d000_s42, PID 234755)
- **HuggingFace 连接超时**，5 次重试全部失败（mmlu 数据集下载超时）
- 典型 AutoDL 问题：未执行 `source /etc/network_turbo` 导致外网不通
- PID 234755 也已不存在

### 根因
两个任务共享 GPU 5，eval 占 ~6.6GB + SFT 峰值 ~17.6GB = ~24.2GB，超过 4090D 的 23.5GB 可用显存。理论上放不下，SFT 在 forward pass 计算 logits 时 OOM。

### 需要的操作
1. **重启 SFT**：单独占 GPU 5，或换到其他空闲 GPU
2. **重启 Eval**：先 `source /etc/network_turbo` 解决网络问题，分配到不同 GPU
3. 两个任务不能共享同一张 4090D

---
