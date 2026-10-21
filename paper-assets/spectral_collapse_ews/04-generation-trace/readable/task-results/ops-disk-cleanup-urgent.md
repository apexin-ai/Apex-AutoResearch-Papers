# ops disk cleanup urgent

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_urgent_20260517T134828_result.json`
- **Structured JSON:** [`5822d8352fc5edd74e9c.json`](../../sessions/58/5822d8352fc5edd74e9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理了约 113M（pip cache），/root 从 5.1G→5.2G。由于 checkpoint 已确认写在 autodl-tmp，/root 的空间压力实际不大。最大潜在清理对象是 `prism_collapse_mixing` (16G)，但需要确认是否还要用。

## 诊断结果

| 项目 | 状态 |
|------|------|
| **Checkpoint 位置** | `/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/adaptive_seed42/` (autodl-tmp) |
| **/root 使用** | 25G/30G → 清理后 25G/30G（释放 ~113M pip cache） |
| **autodl-tmp** | 119G/250G 已用，**132G 可用** |
| **exp_005 状态** | PID 116947 活跃，正在 gen_1 的 generation 阶段（padding 警告说明正在推理） |

## 清理明细

- pip cache: 113M ✓
- `__pycache__`: ~数 MB ✓
- 旧日志 (>1天): 无符合条件的 ✓

## Symlink 操作

**不需要** — checkpoint 已直接写在 autodl-tmp 上。

## 风险评估

exp_005 共 10 gen，gen_0 已完成 (1.6G)，当前在 gen_1。剩余 ~8 gen × 1.6GB = **12.8GB**，全部写入 autodl-tmp（132G 可用）。**无磁盘风险。**

/root 的 5.2G 足够容纳日志、代码和临时文件。如需进一步释放 /root 空间，最大目标是 `prism_collapse_mixing` (16G，无活跃进程)，但这需要确认该项目是否已结束。

---
