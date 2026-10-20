# status westd 47453 loop14

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_westd-47453-loop14_20260516T143746_result.json`
- **Structured JSON:** [`d17301e976bd25529382.json`](../../sessions/d1/d17301e976bd25529382.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇总如下：

---

## 训练状态汇总

**服务器**: westd-47453 | 4× NVIDIA RTX PRO 6000 Blackwell (98GB)
**GPU 利用率**: 全部 94-100%，VRAM 各 75GB/98GB
**磁盘**: 根分区 7.1GB 空闲 (77%) ✅ | autodl-tmp 45GB 空闲 (83%) ✅

| 实验 | GPU | 进度 | 当前 per-batch loss | 预计剩余 (含eval) | 备注 |
|------|-----|------|-----|------|------|
| rho02_uniform_seed42 | cuda:1 | **1800/8477 (21%)** | ~2.6 | ~10h | 已从头重启，新 max_steps=8477 |
| threshold_q07_seed42 | cuda:0 | **~4000/6103 (66%)** | ~2.7, eval_loss=3.04 | ~3.5h | ✅ 原始运行，从未崩溃 |
| threshold_q03_seed42 | cuda:3 | **4431/8477 (52%)** | ~2.7 | ~7h | ⚠️ 见下方说明 |
| batch_adaptive_tau_rho04 | cuda:2 | **2284/8477 (27%)** | weighted ~2.4, unweighted ~1.7 | ~9h | 已从头重启，新 max_steps=8477 |

**训练速度**: 全部 ~3.2 it/s，eval 每 500 步触发一次，每次 eval 耗时 44-53 分钟，占实际训练时间的 90%+。

---

### 重点关注

**threshold_q03_seed42**:
- 之前 resume 失败 — `ValueError: Can't find a valid checkpoint at output/models/threshold_q03_seed42/checkpoint-2000`（用了相对路径，应该用绝对路径）
- 已从头重启（max_steps 从 6103 变为 8477），当前在 step 4431，正常训练中
- step_metrics.jsonl 只记录到 step 1999（文件刷新滞后）

**threshold_q07_seed42**:
- 唯一没有重启过的实验，连续从 step 0 训练到 ~4000
- checkpoint 3500 的 eval_loss=3.035，趋势正常下降
- step_metrics.jsonl 实时记录到 step 3999

**rho02 & batch_adaptive**:
- 均已重启，旧 checkpoints (max_steps=6103) 仍在磁盘上
- 新运行 max_steps=8477，训练正常进行

**tmux**: 无法通过 ssh_read_only 检查 tmux（命令被白名单阻止），但所有 4 个进程树都活跃，python 子进程 100% CPU 正常。

---
