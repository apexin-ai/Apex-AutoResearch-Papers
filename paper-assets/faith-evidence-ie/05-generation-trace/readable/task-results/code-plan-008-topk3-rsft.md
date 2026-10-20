# code plan 008 topk3 rsft

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_008_topk3_rsft_20260515T180110_result.json`
- **Structured JSON:** [`4362df13331af8df2c93.json`](../../sessions/43/4362df13331af8df2c93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动并正在跑步骤，确认正常。

**产出汇总：**

| 项目 | 值 |
|------|-----|
| 筛选数据 | `/root/autodl-tmp/rsft_filtered_topk3/rsft_train.jsonl`，**8037 samples**（top_k=1 baseline 为 2718） |
| 训练 PID | **234489** |
| GPU | cuda:3（RTX 5090，32GB） |
| 总步数 | **1509 steps**（8037 / 16 effective batch × 3 epochs） |
| 每步耗时 | ~5.8s → 预计 **~2.5 小时**完成 |
| 输出目录 | `/root/autodl-tmp/rsft_topk3_output` |
| W&B run | `plan_008_rsft_topk3` |
| Registry | `plan_008_rsft_topk3` → RUNNING |

---
