# ops exp014b status check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp014b-status-check_20260521T131338_result.json`
- **Structured JSON:** [`50e20e22b7a60169c9a1.json`](../../sessions/50/50e20e22b7a60169c9a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_014b 状态报告

| 项目 | 状态 |
|------|------|
| **PID 577216** | 存活，运行 1h09m |
| **当前进度** | Gen 6/10 — 数据生成阶段，已生成 25600/37500 samples（68%） |
| **GPU 利用率** | GPU0: 58%, 51GB/98GB; GPU1: 87%, 25GB/98GB |
| **磁盘** | /root/autodl-tmp 102GB 可用（60% 已用），充足 |
| **Checkpoints** | gen_0 ~ gen_6 已保存（gen_6 checkpoint 已写入，当前在生成合成数据） |

**进度分析：** 实验从 gen_6 开始（start_gen=6），当前仍在 gen_6 的数据生成步骤（25600/37500）。生成完成后还需训练，然后继续 gen_7~10。

**预估完成时间：** 按每代 ~2h 计算，gen_6 剩余约 1.5h，gen_7~10 各 2h，总计还需约 **9.5h**，预计完成时间约明天凌晨 4:00-5:00 (UTC+8)。

---
