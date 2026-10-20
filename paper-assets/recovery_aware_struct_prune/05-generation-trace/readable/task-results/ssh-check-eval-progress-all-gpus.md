# ssh check eval progress all gpus

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_eval_progress_all_gpus_20260523T065745_result.json`
- **Structured JSON:** [`e03e667bd8d000c786bb.json`](../../sessions/e0/e03e667bd8d000c786bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。汇总如下：

## MATH-500 Eval 进度汇总

| 排名 | GPU | exp_id | 进度 | 已用时间 | 近期速度 | 预计剩余 |
|:---:|------|--------|------|---------|---------|---------|
| **1** | **westd:0** | grpo_rasp_alpha3p0_20 | **428/500 (86%)** | 3h35m | ~64s/it | **~1h15m** |
| 2 | westb:0 | sft_qwen_math_cka_only_20 | 341/500 (68%) | 7h48m | ~70s/it | ~3h |
| 3 | westb:1 | grpo_rasp_alpha0p5_20 | 283/500 (57%) | 3h56m | ~45s/it | ~2h45m |
| 4 | westd:3 | grpo_cka_only_20_2048_v2 | 219/500 (44%) | 1h49m | ~39s/it | ~3h |
| 5 | westd:2 | grpo_random_20_v2 | 301/500 (60%) | 8h31m | ~83s/it | ~4h30m |
| 6 | **westd:1** | sft_standard_20_2048_v3 | **66/500 (13%)** | 56m | ~88s/it | **~10h+** |

### 关键结论

- **westd:0 最先完成**，约 1h15m 后（~16:15 UTC）。这是 westd 上最早空出的 GPU，可用于 floor ablation。
- westb 两个 eval 大约同时完成（~3h 后）。
- **westd:1 进度最慢**（13%，且每 item ~88s），刚启动不到 1 小时，预计还需 10h+，是最后完成的。
- westd:2 虽然已到 60%，但速度很慢（~83s/it），也需要 ~4.5h。

所有 6 个进程均存活且 GPU 利用率 98-100%，运行正常。

---
