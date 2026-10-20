# ops emergency disk cleanup 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_emergency_disk_cleanup_10894_20260525T004212_result.json`
- **Structured JSON:** [`f8cfb37ab94ddefdac5e.json`](../../sessions/f8/f8cfb37ab94ddefdac5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已收集完毕。汇总如下：

## 磁盘使用现状

| 目录 | 大小 |
|------|------|
| checkpoints/ | 179G |
| ├─ full_occ_ln_s0 (30K/40K/50K) | 45G |
| ├─ full_occ_ln_s1 (20K/30K/40K) | 45G |
| ├─ full_occ_ln_s2 (20K/30K/40K) | 45G |
| └─ ablation_occ_detach_s0_retrain (20K/30K/40K) | 45G |
| runs/ (vanilla 100_chkpt) | 15G |
| models/openvla-7b | 15G |
| libero_datasets/ | 5.9G |
| data/ | 2G |
| logs/ (archive) | 716M |
| **总计** | **216G / 250G (35G 可用)** |

每个 checkpoint 子目录 = 15G。3 个正在训练的实验目前在 ~40K，到 50K 时各需写入 15G，共需 **45G**，超过剩余 35G。

## 删除计划

| # | 目标 | 大小 | 理由 |
|---|------|------|------|
| 1 | full_occ_ln_s0 / 30000_chkpt | 15G | eval 已完成，有 50K，30K 无用 |
| 2 | full_occ_ln_s0 / 40000_chkpt | 15G | 同上 |
| 3 | full_occ_ln_s1 / 30000_chkpt | 15G | 正在训练，40K 是最新，30K 冗余 |
| 4 | full_occ_ln_s2 / 30000_chkpt | 15G | 同上 |
| 5 | ablation_occ_detach_s0_retrain / 30000_chkpt | 15G | 同上 |
| 6 | runs/...--100_chkpt | 15G | 旧 vanilla baseline checkpoint |
| 7 | logs/archive | 713M | 旧日志 |
| | **合计释放** | **~91G** | |

**不删除**：
- s1/s2/ablation 的 20K checkpoint（用户指定保留）
- s1/s2/ablation 的 40K checkpoint（当前最新 resume 点）
- full_occ_ln_s0 的 50K checkpoint（最终模型，梯度分析可能需要）
- models/openvla-7b（基础模型）

清理后预计可用空间：35G + 91G = **~126G**，足够 3 个训练到 50K（需 45G）。

确认后执行删除？

---
