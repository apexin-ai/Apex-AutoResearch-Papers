# exp mag preservation collect

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_mag_preservation_collect_20260517T051328_result.json`
- **Structured JSON:** [`5e1b327aadfcd5499d89.json`](../../sessions/5e/5e1b327aadfcd5499d89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

**服务器 westd-34887 不可达**，无法收集结果。

### 已知信息（从 worker log 恢复）

**训练配置**：
- 脚本：`scripts/run_mag_reg.sh` → 顺序执行 alpha=0.01 和 alpha=0.1（各 1000 步）
- 输出目录：`checkpoints/kl_mag_reg_a001`（alpha=0.01）、`checkpoints/kl_mag_reg_a01`（alpha=0.1）
- GPU：cuda:1，batch_size=4，seq_len=2048，lr=1e-3，seed=42，sparsity_target=0.5
- 日志：`/root/distill_sparse_swiglu/logs/mag_reg_full.log`
- PID：301887

**最后观测点**（alpha=0.01 运行中）：
| 指标 | 值 |
|------|-----|
| Step | 390/1000 |
| loss | 0.2876 |
| kl | 0.2852 |
| mag_reg | 0.0243 |
| sparsity | 0.496 |
| lambda | 1000.0 |
| tau | 0.649 |
| elapsed | 872s (~2.2s/step) |

**预估时间线**：
- alpha=0.01 应在 ~37min 完成（约 13:40 CST）
- alpha=0.1 应在 ~14:20 CST 完成
- 训练开始于 2026-05-17 13:03 CST

**当前状态**：服务器端口不可达，可能是实例过期/关机。训练本身通过 nohup 启动，如果服务器在训练期间存活，结果应保存在上述 checkpoint 路径中。

### 下一步

1. 等服务器恢复（或检查 SeetaCloud 控制台确认实例状态）
2. 恢复后执行：
   - `tail -50 /root/distill_sparse_swiglu/logs/mag_reg_full.log` 确认两个 alpha 是否都跑完
   - `ls /root/distill_sparse_swiglu/checkpoints/kl_mag_reg_a*/` 检查 checkpoint
   - 对完成的 checkpoint 跑 PPL eval + downstream eval

需要我在服务器恢复后重新执行收集任务吗？

---
