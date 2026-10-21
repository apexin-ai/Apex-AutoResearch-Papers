# preflight prolog sta eval ready

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_preflight_prolog-sta-eval-ready_20260514T173346_result.json`
- **Structured JSON:** [`6c462207f631a21bf105.json`](../../sessions/6c/6c462207f631a21bf105.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

预检完成。

**Eval 就绪: Yes**

关键发现:
- `eval_sta.py` 和 `swipl` 都可用，eval 数据 `proofwriter_fol_100.jsonl` 存在
- s43 训练中 (checkpoint-300)，s44 训练中 (checkpoint-150)，最终 checkpoint 预计 checkpoint-500
- **磁盘偏紧** (41GB/250GB)：eval 后必须立即清理 checkpoint
- s43 当前有两个 checkpoint (250+300)，与 save_total_limit=1 不一致，训练完后需确认并手动清理

精确 eval 命令已写入 `artifacts/preflight_prolog_sta_eval.md`，训练完成后可直接复制执行。

---
