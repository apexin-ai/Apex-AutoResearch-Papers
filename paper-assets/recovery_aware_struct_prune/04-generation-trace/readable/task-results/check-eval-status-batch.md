# check eval status batch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_status_batch_20260516T051702_result.json`
- **Structured JSON:** [`e639eac492536a1db416.json`](../../sessions/e6/e639eac492536a1db416.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| exp_id | 状态 | accuracy | 详情 |
|--------|------|----------|------|
| eval_grpo_rasp_v9_step10 | **运行中** (19%, 249/1319) | — | 进程仍在执行，~2s/it，预计还需 ~35min 完成 |
| eval_grpo_unpruned_v2_step100 | **完成** | **81.27%** (1072/1319) | greedy, eos_rate=99.7%, avg_len=209 |
| eval_grpo_unpruned_v2_step90 | **完成** | **80.59%** (1063/1319) | greedy, eos_rate=99.6%, avg_len=213 |

备注：
- eval_grpo_rasp_v9_step10 在 westb-23072 上当前只完成了 19%（日志最后时间戳 13:12 UTC，约 15 分钟前才跑到 249 样本）。可能是重启过或晚启动的。按 ~2s/it 估算，还需约 35-40 分钟完成。
- unpruned_v2 两个 checkpoint 对比：step100 (81.27%) 略优于 step90 (80.59%)，差距 0.68pp，在 stderr 范围内基本持平。

---
