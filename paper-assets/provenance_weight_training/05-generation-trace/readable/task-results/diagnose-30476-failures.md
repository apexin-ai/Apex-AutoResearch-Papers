# diagnose 30476 failures

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_30476_failures_20260517T123743_result.json`
- **Structured JSON:** [`1c18447734589f74b1a1.json`](../../sessions/1c/1c18447734589f74b1a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键发现：container 当前 session 从 18:01 启动，存在大量历史内存压力（7.8G µs full stall），进程列表干净。

## 诊断结论

### 失败根因
**4 个训练进程被 SIGKILL 同时终止**（~19:46 server time / 11:46 UTC），最可能原因是 **cgroup OOM killer**。

证据链：
- 3/4 实验日志明确显示 `Killed`（SIGKILL），第 4 个（rho02）的 "DONE" 是假阳性（tee 管道掩盖了 kill 退出码）
- `/proc/pressure/memory` 显示 7.8G µs full memory stall，表明容器曾经历严重内存压力
- cgroup 内存限制 440 GiB，`free` 显示的 1.0 TiB 是宿主机内存，容器实际可用远小于此
- 无服务器重启（uptime 218天），无磁盘满，GPU 4 卡健康
- 不是 CUDA OOM（那会抛 Python 异常而非 SIGKILL）
- 容器 session 18:01 启动，非平台级关机

### 服务器当前状态

| 项目 | 状态 |
|------|------|
| GPU | 4× RTX PRO 6000 Black (96GB each)，全部健康，0 MiB 占用 |
| 磁盘 | overlay 36%, /dev/sda2 3%，充足 |
| 内存 | 当前 68 GiB used / 440 GiB cgroup limit |
| 进程 | 仅 supervisord/jupyter/tensorboard，无训练进程 |

### Checkpoint 情况
**全部丢失**。4 个实验的 save_steps=500，但全部在 step 480-558 被 kill，仅 random_reweight_seed123 刚过 500 但未来得及写入。Output 目录仅存 step_metrics.jsonl（几 KB），无 model checkpoint 或 safetensors。

| 实验 | 最后 step | 进度 | Checkpoint |
|------|----------|------|-----------|
| random_reweight_seed123_r2 | 558/6103 | 9% | 无 |
| bs8_auto_nmin_r3 | 524/6103 | 9% | 无 |
| batch_adaptive_tau_rho06_r3 | 530/6103 | 9% | 无 |
| rho02_adaptive_tau09_r3 | 488/6103 | 8% | 无 |

### 恢复建议

1. **服务器可以立即恢复使用**，GPU/磁盘/网络均正常
2. **需从头重跑所有 4 个实验**，无可用 checkpoint
3. **降低并发**：4 个实验同时跑时 CPU 内存可能因 data loading + tokenization + 4 份 optimizer states 累积触顶。建议：
   - 先跑 2 个实验，观察 `free -h` 中的内存变化
   - 或把 save_steps 降到 200，确保更早保存 checkpoint
   - 如果内存确实是瓶颈，可考虑使用 memory-mapped datasets 而非全量加载

---
