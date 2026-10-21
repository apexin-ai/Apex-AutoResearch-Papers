# ops gpu scan full

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-scan-full_20260515T143521_result.json`
- **Structured JSON:** [`fc6cbb8396a472a71a45.json`](../../sessions/fc/fc6cbb8396a472a71a45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

| GPU | 进程 | PID | 显存 | GPU利用率 | 状态 |
|-----|------|-----|------|-----------|------|
| **cuda:0** | `freige.eval.ced_reranker` — CED scoring 阶段 | 178055 | 1728/32607 MiB | 42% | 运行中，809/985 (82%)，预计还 ~10 min |
| **cuda:1** | `freige.eval.inference` — RSFT R2B eval (maxtok1536) | 197386 | 14675/32607 MiB | 64% | 运行中，108/124 batch (87%)，预计还 ~20 min |
| **cuda:2** | DREEAM teacher roberta 训练 | 213006 | 24899/32607 MiB | 98% | 正常，epoch 2/30 (7%)，刚启动 ~5 min |
| **cuda:3** | `freige.training.rsft_score_filter` — flat_nli scoring | 208155 | 1467/32607 MiB | 34% | 运行中，15000/21728 (69%)，预计还 ~45 min |

**已死 PID**: 210099, 210104 — 已不存在。

**空闲卡: 无。** 四张卡全部在跑任务。cuda:0 和 cuda:1 的任务预计 10-20 分钟内完成，之后可释放。

---
