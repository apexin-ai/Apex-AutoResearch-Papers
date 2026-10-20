# code plan 005 setup

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-005-setup_20260515T032749_result.json`
- **Structured JSON:** [`f9b74ef30ee39285d179.json`](../../sessions/f9/f9b74ef30ee39285d179.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个任务已通过 `submit_training_job` 启动，tmux session 全部存在：

| exp_id | prompt_type | GPU | 进度 (行数) | PID |
|--------|-------------|-----|-----------|-----|
| plan-005-cont | continuation | cuda:1 | 63 | 164663 |
| plan-005-elab | elaboration | cuda:2 | 63 | 164742 |
| plan-005-rewrite | inspired_rewriting | cuda:3 | 61 | 164886 |

脚本 `generate_chain_prompt.py` 已存在且功能完整，支持 3 种 prompt type，输出含 `prompt_type` 字段。输入文件为 `data/wiki_seed_1000.jsonl`（`openwebtext_seeds.jsonl` 不存在）。

输出路径为 `/root/gen-depth-fingerprint/data/pythia-2.8b-{type}/generations_shard0.jsonl`（非 autodl-tmp，但 JSONL 文件较小，~5MB/种，不会撑爆根分区）。

1000 seeds × 5 depths，预计总计 ~5000 records/种，当前约完成 1.2%，刚启动约 2 分钟。

---
