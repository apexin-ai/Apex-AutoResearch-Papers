# ops westb progress check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_progress_check_20260518T211035_result.json`
- **Structured JSON:** [`46ed6a18f42b309efc5f.json`](../../sessions/46/46ed6a18f42b309efc5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| 卡 | 任务 | GPU 利用率 | 显存 | 进度 | 当前 acc |
|---|---|---|---|---|---|
| cuda:0 | eval_gsm8k_sft_cka_only_20_1p5b | **99%** | 6.5G/98G | **58/1319 (4%)** | 0.4200 |
| cuda:1 | eval_gsm8k_grpo_rasp_20_1p5b | **96%** | 6.6G/98G | **642/1319 (49%)** | 0.2883 (@ 600) |

- cuda:0 刚启动约 6 分钟，速度 ~3s/it，预计还需 **~63 min**
- cuda:1 已跑 1h20m，速度波动大（长 prompt 偶发慢批次），预计还需 **~70 min**

---
