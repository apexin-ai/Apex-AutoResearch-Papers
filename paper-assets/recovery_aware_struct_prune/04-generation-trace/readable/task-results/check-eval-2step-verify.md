# check eval 2step verify

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_2step_verify_20260520T133524_result.json`
- **Structured JSON:** [`1cb61977baf9893f8a1a.json`](../../sessions/1c/1cb61977baf9893f8a1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29022 GPU 状态

| GPU | Util% | Memory | PID | 任务 |
|-----|-------|--------|-----|------|
| 0 | 90% | 12825 MiB | 252604 | `eval_gsm8k` grpo_cka_only_20_seed456 |
| 1 | 93% | 13371 MiB | 252919 | `eval_gsm8k` grpo_cka_only_15_v2 |
| 2 | 99% | 29157 MiB | 226966 | `eval_gsm8k` grpo_standard_20_seed123 |
| 3 | 0% | 0 MiB | — | 空闲 |

## eval 进程状态

**eval_gsm8k_grpo_cka_only_20_seed456_full** (cuda:0)
- PID 252604 存活：✅
- 日志写入：✅
- 进度：25/1319 (1.9%)，~2-3s/it，启动于 21:31

**eval_gsm8k_grpo_cka_only_15_v2** (cuda:1)
- PID 252919 存活：✅
- 日志写入：✅
- 进度：5/1319 (0.4%)，~2.7s/it，启动于 21:32

两个 eval 均已成功启动并在正常推理中。按当前速度预估各需 ~1 小时完成。cuda:2 上还有一个 grpo_standard_20_seed123 的 eval 在跑。

---
