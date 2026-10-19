# diagnose exp 004 s2 eval ckpt3500

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-004-s2-eval-ckpt3500_20260522T165506_result.json`
- **Structured JSON:** [`5f2e5cfc5f32c1cd21ce.json`](../../sessions/5f/5f2e5cfc5f32c1cd21ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 结论：这是一个**误报**，实验实际已成功完成。

**日志显示 eval 正常跑完了全部 362 个样本**，exit code = 0，无任何错误。结果：

| 指标 | 值 |
|------|-----|
| SYCONScore | **0.2308** |
| ToF | 0.1326 |
| NoF | 0.8895 |
| Samples | 362 (181 valid / 181 invalid) |
| 耗时 | 1508s (~25min) |

输出文件完整存在于 `/root/autodl-tmp/results/exp004s2_act_eval/checkpoint-3500/`（详细 JSON + summary txt）。

### 失败的根因

监控系统报 "process dead 5× with no sentinel/W&B" 是因为 **eval 脚本不写 sentinel 文件也不上报 W&B**，导致监控的健康检查机制无法确认进程状态，误判为失败。进程本身已正常退出。

### 其他检查结果

- **Checkpoint**：完整（adapter_model.safetensors 698MB + tokenizer 等）
- **GPU**：4× RTX 5090，全部健康，GPU 1 当前有其他 python 进程在用
- **磁盘**：350G 用了 104G，剩余 247G (30%)，无问题
- **ckpt-2000 结果**：该服务器上不存在 checkpoint-2000 的结果目录（可能在其他服务器上跑的）

### 建议

1. **不需要重试** — 结果已完整产出，SYCONScore=0.2308（略优于 ckpt-2000 的 0.214）
2. **修复监控误报**：eval 任务应在完成时写 sentinel 文件（如 `touch /root/runs/.../DONE`），或者监控系统对 eval 类任务改用进程退出码判断而非 sentinel/W&B 心跳
3. **ckpt-2500 和 ckpt-4000** 的 "失败" 可能也是同样的误报，建议同样检查日志确认

---
