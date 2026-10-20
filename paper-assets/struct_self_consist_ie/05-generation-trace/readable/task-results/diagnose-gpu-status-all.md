# diagnose gpu status all

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_status_all_20260521T024235_result.json`
- **Structured JSON:** [`cf303ded93d2f609d881.json`](../../sessions/cf/cf303ded93d2f609d881.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### GPU 状态

| 服务器 | GPU | 显存占用 | Util | 实验 | 进度 | ETA |
|--------|-----|---------|------|------|------|-----|
| **autodl-5090** | 0-3 (TP4) | 31.3/32.6 GB | 96-98% | 32B fewnerd n8 s42 | **95%** (285440/301184) | **~8 min** |
| **autodl-5090-b** | 0 | 30.6/32.6 GB | 93% | 8B fewnerd t=0.5 s123 | **56%** (167328/301184) | ~45 min |
| | 1 | 30.6/32.6 GB | 86% | 8B fewnerd t=0.8 s123 | ~56% | ~45 min |
| | 2 | 30.6/32.6 GB | 96% | 8B fewnerd t=1.2 s123 | ~56% | ~45 min |
| | 3 | 30.6/32.6 GB | 86% | 8B fewnerd t=0.8 s456 | ~56% | ~45 min |
| **autodl-5090-c** | 0 | 31.4/32.6 GB | 98% | 14B fewnerd n8 s42 | **4%** (23600/602368) | ~2.5h |
| | 1 | 0/32.6 GB | 0% | *idle* | — | — |
| | 2 | 29.9/32.6 GB | 85% | 7B fewnerd n16 s42 | ~4% | ~2h |
| | 3 | 0/32.6 GB | 0% | *idle* | — | — |

### 磁盘

| 服务器 | 用量 | 剩余 |
|--------|------|------|
| autodl-5090 | 230/250 GB (**92%**) | 21 GB ⚠️ |
| autodl-5090-c | 226/350 GB (65%) | 125 GB |

### 已完成任务
- **5090-c**: conll_t10_seed42 刚完成，Verdict=**PASS** (ρ=+0.37, AUROC=0.82)
- **5090-c 14B campaign**: 13/15 配置已完成 (scierc 全部, conll 全部, fewnerd n1/n2/n4)

### 14B inference 评估

实际情况比预期好很多，不是整体 22%/13h——而是：
- 已完成 13/15 配置（scierc × 5, conll × 5, fewnerd n1/n2/n4）
- **当前 fewnerd_n8**: 刚开始实际推理（模型加载耗了 ~2h，推理 ETA ~2.5h）
- **剩余 fewnerd_n16**: 尚未启动，预计 ~5h

**建议继续。** 已投入 ~10h 完成了 87% 的配置，剩余 fewnerd_n8 + n16 约需 7.5h GPU 时间。中断意味着已完成的 13 个配置数据不完整（缺最关键的 n8/n16 high-sample 条件），无法做完整的 scaling 分析。5090-c GPU1/3 空闲，如果 fewnerd_n16 不需要 TP，可以在 n8 完成前提前用空闲 GPU 启动。

### 注意事项
- **5090 磁盘告急**（92%），32B 推理输出可能写不下，建议 32B 完成后立即清理旧日志/checkpoint
- 5090 的 32B 实验 ~8 min 后完成，之后 4 卡全部释放

---
