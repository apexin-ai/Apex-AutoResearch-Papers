# diagnose oracle true gt failed

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_oracle_true_gt_failed_20260522T210819_result.json`
- **Structured JSON:** [`2ebb10a31812c6ba6a25.json`](../../sessions/2e/2ebb10a31812c6ba6a25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**两个实验都没有崩溃，而是正常完成了。** cron 报 "Process exited without valid W&B metrics" 是误报——这些是 eval-only 的运行，输出 JSON 文件而非 W&B metrics。

### 实验 1: oracle_true_gt_adaptive_alpha_v11

| 项目 | 结果 |
|------|------|
| 状态 | **正常完成** |
| 运行范围 | safelibero_object suite, 4 tasks × 40 episodes = 160 episodes |
| 运行时间 | 04:04 → 04:44 (~40 min) |
| Avg TSR | 0.0% |
| Avg CAR | 75.0% |
| 结果文件 | `/root/autodl-tmp/eval_results/oracle_true_gt_adaptive_alpha_v11.json` ✓ 完整 |

### 实验 2: oracle_true_gt_fixed_alpha_v11

| 项目 | 结果 |
|------|------|
| 状态 | **正常完成** |
| 运行范围 | safelibero_object suite, 4 tasks × 40 episodes = 160 episodes |
| 运行时间 | 04:04 → 04:44 (~40 min) |
| Avg TSR | 0.0% |
| Avg CAR | 73.1% |
| 结果文件 | `/root/autodl-tmp/eval_results/oracle_true_gt_fixed_alpha_v11.json` ✓ 完整 |

### "失败" 根因

不是代码 bug 也不是资源问题。cron 监控期望 W&B metrics 作为成功信号，但 eval 脚本只输出本地 JSON，不写 W&B。进程 exit code 为 0（正常退出）。

日志中出现的 `OutOfMemoryError: out of resource: triton_mm` 是 PyTorch Inductor autotuning 时某些 triton kernel 配置被跳过的正常警告，不影响执行。

### 结果数据完整可恢复

两个 JSON 文件均包含完整的 4 tasks × 40 episodes 粒度数据（含 per-episode success/collision/sdf_min/refine_count 等字段）。

---
