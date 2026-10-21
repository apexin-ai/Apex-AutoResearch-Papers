# diagnose eval pi05 random k09 object seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k09_object_seed42_v2_20260524T014416_result.json`
- **Structured JSON:** [`9dfbaa430d4145c9fef2.json`](../../sessions/9d/9dfbaa430d4145c9fef2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：实验未失败，已成功完成

**根因**：实验没有崩溃。日志 `logs/eval_pi05_random_k09_object_seed42_v2.log` 显示全部 10 个 task × 50 episodes 正常跑完，耗时 159.6 分钟。

**最终结果**：
- `libero_object prune=random keep=0.9 SR=9.0%`（45/500）
- 结果文件已保存：`eval_results/pi05_random_k0.90_libero_object_seed42.json`

**"异常退出5次"的可能解释**：监控系统可能检测到进程结束（正常退出）并误判为异常，或者之前确实有失败的尝试但 `/tmp` 日志已被清理，最终一次成功执行并写入了 `logs/` 目录。

**GPU 0 状态**：空闲（1MiB 显存占用，0% 利用率），可用。GPU 1 和 3 有其他进程在跑。

**磁盘**：根分区 30G 用了 8.7G，22G 可用，正常。

**结论**：无需重试。实验已产出结果 SR=9.0%，与之前的 12% 接近（随机 pruning 的方差范围内）。如果缺少 W&B metrics 和 sentinel，问题可能在上报逻辑而非实验本身——实验数据完整。

---
