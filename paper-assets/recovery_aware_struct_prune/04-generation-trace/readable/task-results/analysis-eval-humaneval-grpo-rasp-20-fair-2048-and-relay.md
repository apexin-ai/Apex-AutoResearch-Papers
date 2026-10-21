# analysis eval humaneval grpo rasp 20 fair 2048 and relay

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_humaneval_grpo_rasp_20_fair_2048_and_relay_20260519T093557_result.json`
- **Structured JSON:** [`e6cfaa419f1be35c1b4e.json`](../../sessions/e6/e6cfaa419f1be35c1b4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两步任务完成。

## 产出

**任务 1 — RASP fair HumanEval 收割**
| 指标 | 值 |
|---|---|
| pass@1 | **10.98%** (18/164) |
| stderr | 0.0244 |
| 对比 interim | 12.5% → 10.98%（最终偏低） |

Registry `eval_humaneval_grpo_rasp_20_fair_2048` → DONE (success)

**任务 2 — SFT Standard HumanEval v3 启动**
- PID 86171 on westd-29022 cuda:3
- tmux session: `eval_humaneval_sft_standard_20_2048_v3`
- 模型正在加载中（14.5GB RSS，CPU 密集），即将转移到 GPU
- Registry → RUNNING

**附注**: `eval_humaneval_grpo_standard_20_fair_2048` 的结果文件不存在（cuda:3 之前的任务，pid 72393 已退出但无输出文件），可能需要后续排查。Cron 列表为空，无需删除。

---
