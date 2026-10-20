# test gpu sharing

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_test_gpu_sharing_20260514T002003_result.json`
- **Structured JSON:** [`9a098428b62f8375820d.json`](../../sessions/9a/9a098428b62f8375820d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

dummy 全部清理完毕，GPU 恢复到测试前状态。exp_006 和 exp_007 正常运行。

---

## 测试报告

### 1. GPU 显存占用

| 阶段 | GPU 0 已用 | GPU 0 总量 | 占比 |
|------|-----------|-----------|------|
| 实验前 (exp_006 alone) | 4,167 MiB | 97,887 MiB | 4.3% |
| 2 并发 (exp_006 + dummy s2) | 8,326 MiB | 97,887 MiB | 8.5% |
| 3 并发 (exp_006 + dummy s2 + dummy s3) | 9,125 MiB | 97,887 MiB | 9.3% |
| 清理后 | 4,167 MiB | 97,887 MiB | 4.3% |

每个 DreamerV3 进程稳定占用 **~4 GB** 显存（dmc_proprio, compile=False）。

### 2. exp_006 FPS 变化

- 并发前 baseline：6.7 → 6.5 fps
- 并发期间：exp_006 持续从 step 25k 推进到 step 35k（含 evaluation），**没有 stall 或报错**
- 由于 fps 每 10000 步才记录一次，测试时间窗口内没有产出新 fps 数据点。但训练进度没有中断。

### 3. CUDA OOM

**没有出现。** 两个 dummy 进程都成功完成了 5000 步训练 + evaluation。

### 4. 结论：单 GPU 安全并发数

以 RTX PRO 6000 (98 GB) + DreamerV3 dmc_proprio (~4 GB/进程) 计算：

- **理论上限**：98 GB / 4 GB ≈ **24 进程**（纯显存）
- **实测 3 并发**：完全安全（9.1 GB / 98 GB，仅 9.3%）
- **实际瓶颈是 GPU 利用率**：3 进程时 GPU utilization 经常达 90-97%，这会导致各进程争抢 SM 核心，**fps 会下降**
- **保守推荐**：**单 GPU 跑 8-10 个实验**应该可行（显存 ~40 GB，50% 利用率），但建议先做一轮 fps 对比确认吞吐下降在可接受范围内

### 5. Dummy 清理确认

所有 dummy 进程已 kill，GPU 0 恢复到仅 exp_006 (4167 MiB)。exp_006 (pid 85034) 和 exp_007 (pid 90359) 均正常运行。

---
