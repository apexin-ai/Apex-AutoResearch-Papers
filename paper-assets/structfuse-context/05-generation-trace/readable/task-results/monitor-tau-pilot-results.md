# monitor tau pilot results

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_tau_pilot_results_20260512T235601_result.json`
- **Structured JSON:** [`3bc65de4fd253910a7ae.json`](../../sessions/3b/3bc65de4fd253910a7ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在情况清楚了。汇总报告：

---

## Tau Pilot 训练状态

**状态：仍在运行，显著慢于预期**

| 项目 | 详情 |
|------|------|
| 当前运行 | τ=0.05（第 1/3 个，PID 269384） |
| 已运行时间 | ~2h46m（预期 10-15min） |
| GPU 4 占用 | 30% 利用率，8082 MiB 显存 |
| τ=0.1 / τ=0.2 | 尚未开始（串行等待中） |
| Checkpoint | 目录为空（脚本在训练结束才保存） |

### 日志缺失原因
`nohup > /tmp/tau_pilot.log` 导致 Python stdout 使用 full buffering（非 TTY 模式），所有 `print()` 输出（每 50 步打印一次）都在缓冲区中未刷新到文件。日志最后修改时间停在 07:54。

### 异常分析
训练数据仅 505 条，batch_size=2 → ~252 steps/epoch，1 epoch 不应该跑近 3 小时。可能的原因：
- `num_negatives=3` → 每个样本构造 1 anchor + 1 pos + 3 neg = 5 条序列，实际 batch 远大于 2
- `gradient_checkpointing` + LoRA + 3B 模型 + `max_seq_length=512` 在单卡上本身较慢
- 数据加载/tokenization 可能有瓶颈

### 建议
1. 进程仍在活跃（GPU 有负载），不建议 kill，等它跑完
2. 但按当前速度，3 个 run 串行可能需要 **~8-9 小时**总时间（而非预期的 30-45min）
3. 未来建议训练脚本加 `PYTHONUNBUFFERED=1` 或 `python -u` 来避免日志缓冲问题

需要我继续等待还是要做什么调整？

---
