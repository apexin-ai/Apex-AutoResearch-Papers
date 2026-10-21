# ops fix eval and run

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_eval_and_run_20260519T005652_result.json`
- **Structured JSON:** [`40b1c5506d2feadb7770.json`](../../sessions/40/40b1c5506d2feadb7770.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

## v7 训练最终状态
- 训练时间: 21352s (~5.9h), 3 epochs
- 最终 loss: avg=0.897 (NTP=0.896, GAR=0.001, DIV=0.000)
- 最终 gate: mean=0.9336, std=0.0492, min=0.7891, max=0.9883
- 最低 gate 层: L4=0.789, L3=0.801

## v7 Eval 结果

### GAR-ours (last-token query)
| 指标 | 值 |
|---|---|
| Turn 1 avg GAR | 0.0502 |
| Mid-turns avg GAR | 0.0157 |
| Baseline mid-turn | 0.0122 |
| **Recovery** | **+0.35pp** |
| Per-turn (avg) | [0.0502, 0.0296, 0.0201, 0.0172, 0.0128, 0.0142, 0.0144, 0.0153, 0.0094, 0.0268] |

### GAR-Dongre (all-response-token query)
| 指标 | 值 |
|---|---|
| Turn 1 avg GAR | 0.0587 |
| Mid-turns avg GAR | 0.0194 |
| Baseline mid-turn | 0.0122 |
| **Recovery** | **+0.72pp** |
| Per-turn (avg) | [0.0587, 0.0301, 0.0238, 0.0212, 0.0185, 0.0198, 0.0176, 0.0155, 0.0163, 0.0141] |

### Gate Dynamic Range (top 5 layers by |diff|)
| Layer | Turn 1 | Turn 21 | Diff |
|---|---|---|---|
| L23 | 0.7693 | 0.9793 | -0.2100 |
| L14 | 0.7473 | 0.9276 | -0.1803 |
| L12 | 0.8200 | 0.9465 | -0.1265 |
| L20 | 0.8228 | 0.9393 | -0.1165 |
| L9  | 0.8578 | 0.9679 | -0.1101 |

## UG Baseline 状态
- 正常运行中, epoch 0, step 1000
- Gate=0.8979, Loss=1.1068
- Cron 监控已注册

## Registry
- phase2_tg_s42_v7: status=DONE, conclusion=success, metrics 含完整 eval 结果
- phase2_tg_s42_v7 cron 已删除

---
