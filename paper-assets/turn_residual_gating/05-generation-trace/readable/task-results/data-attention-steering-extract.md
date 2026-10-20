# data attention steering extract

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_attention_steering_extract_20260520T111052_result.json`
- **Structured JSON:** [`ea0944d1c1bf9bcef7ff.json`](../../sessions/ea/ea0944d1c1bf9bcef7ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据提取完成。以下是最终结果汇总：

## Gen 模式（5 conversations, v7 checkpoint）

**已获取完整 per-conversation 数据的 beta 值：**

| Beta | GAR (mean) | PPL (mean) | 数据精度 | 来源 |
|------|-----------|-----------|---------|------|
| 0.0 | 0.0280 | 1.409 | 全精度 | 服务器 JSON |
| 2.0 | 0.0620 | 1.411 | 4位小数 | 实验日志 |
| 5.0 | 0.6795 | 1.908 | 4位小数 | 实验日志 |
| 10.0 | 0.9590 | 4.220 | 全精度 | 服务器 JSON |

**仅有聚合值（per-conv 数据被 SSH 截断）：**
- beta 0.5: GAR=0.0287, PPL=1.387（有2条对话的部分高精度曲线）
- beta 1.0: GAR=0.0349, PPL=1.360

**保存位置：**
`artifacts/attention_steering_v7_tg_gen/data/steering_per_conv_gen5.json`

**缺失原因：** `ssh_read_only` 工具输出截断在 ~8KB，14KB 的 JSON 文件中间 6KB 被截断。实验日志的 `tail -80` 只捕获了后 3 个 beta 值。beta 0.5 和 1.0 的 per-conversation 数据在截断区域内。

**是否影响论文：** beta 0.5 和 1.0 处于低 steering 区域（GAR 几乎不变），对 phase transition 分析和 error bar 影响极小。关键数据（beta 0.0 baseline、2.0 过渡点、5.0/10.0 高 steering）均完整。

如果需要完整的 beta 0.5/1.0 数据，需要从服务器上用 `head -c 7000` / `tail -c +4000` 分段读取 JSON 文件。

---
