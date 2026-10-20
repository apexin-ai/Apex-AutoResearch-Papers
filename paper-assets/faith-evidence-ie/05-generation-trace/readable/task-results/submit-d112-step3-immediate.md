# submit d112 step3 immediate

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_d112_step3_immediate_20260519T042821_result.json`
- **Structured JSON:** [`f251c8268401a2535f55.json`](../../sessions/f2/f251c8268401a2535f55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中。567 steps，3014 样本，3 epochs，~6.3s/step。

## 总结

**D112 Step 2 CED Scoring** — 完成
- 24216 条记录全部打分，输出 rsft_train.jsonl 3014 行（k=1 筛选）
- Registry 已标记 `success`

**D112 Step 3 RSFT Training** — 已提交并运行中
- PID: 613075, cuda:0, GPU 0 占用 ~5 GB
- 567 steps, ~6.3s/step, 预计 ~60 分钟完成
- 日志：`/root/autodl-tmp/logs/d112_rsft_s44_train.log`

**8B Eval (PID 598911)** — 仍在运行
- 进度 197/247 (79.8%), ~45s/it, 预计 ~37 分钟完成
- cuda:3, 18.9 GB

**全卡 GPU 状态**：
| GPU | 占用 | 进程 |
|-----|------|------|
| 0 | 5 GB / 32 GB | D112 RSFT train (613075) |
| 1 | 16 GB / 32 GB | 其他训练 (611578) |
| 2 | 17 GB / 32 GB | 其他训练 (611579) |
| 3 | 19 GB / 32 GB | 8B eval (598911) |

---
