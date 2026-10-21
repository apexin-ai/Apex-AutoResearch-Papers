# debug d083 sigterm rootcause

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_d083_sigterm_rootcause_20260515T210353_result.json`
- **Structured JSON:** [`11fe73babb887c00b202.json`](../../sessions/11/11fe73babb887c00b202.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在有完整信息了。以下是根因分析报告：

---

## D083 SIGTERM 根因分析报告

### 1. 根因：Worker 代理 (agent-ml-research) 通过 ssh_execute 发送 SIGTERM

**不是 OOM killer、不是 cron、不是手动 kill。**

证据：
- dmesg / journalctl 无 OOM killer 记录
- 服务器无 crontab
- bash_history 无 kill 命令
- 每次 kill 后 3-6 分钟内立刻有下一版本启动（Worker 决策+重提的典型间隔）
- ssh_execute 执行的 kill 命令不会写入 bash_history

### 2. 各实验时间线

| 实验 | 启动时间 (CST) | 终止时间 | 终止位置 | EXIT_CODE | 原因 |
|------|---------------|----------|----------|-----------|------|
| d025_s42_a32 | 00:14 | 00:15 | model.to(device) | 1 | **CUDA OOM** — GPU 0 被 PID 589763 占用 17.21 GiB，剩余仅 43 MiB |
| d100_s42_a32 (v1) | 00:14 | 00:27 | step 164/4159 (4%) | 143 | **SIGTERM** — Worker 发现 GPU 冲突后 kill（d025 同 GPU OOM 印证了 GPU 0 拥堵） |
| d100_s42_a32_v2 | 00:30 | 04:06 | step 3030/4159 (72%) | 143 | **SIGTERM** — Worker kill 后重提 v3（可能为修正 GPU 分配/加 CUDA_VISIBLE_DEVICES） |
| d100_s42_a32_v3 | 04:12 | **运行中** | step 757+ (18%) | — | GPU 2, CUDA_VISIBLE_DEVICES=2，正常运行 |

### 3. 关键观察

- **v1 无显式 CUDA_VISIBLE_DEVICES**，导致落到已占用的 GPU 0（违反 C004）
- **v3 已修正**：launch 命令中有 `export CUDA_VISIBLE_DEVICES=2`
- v2 运行 3.5 小时后在 72% 进度被 kill，是最大的浪费——近 3.5 小时 GPU 时间损失
- `Qwen2.5-3B_d100_a32_s42` 的 checkpoint 目录 `lora_adapter/` 为空（v1 未完成保存）

### 4. 预防建议

1. **Worker 在 kill 前保存 checkpoint**：如果训练已到 72%，应先触发 checkpoint save 再 kill，或支持 resume
2. **首次提交就设 CUDA_VISIBLE_DEVICES**：v1/v2 的问题根源在于缺少显式 GPU 绑定（C004 约束已存在但未遵守）
3. **Worker kill 记录**：ssh_execute 发 kill 时应在日志中记录原因，方便事后排查

---
