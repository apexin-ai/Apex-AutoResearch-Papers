# ops fix pass k8 params

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-pass-k8-params_20260517T000217_result.json`
- **Structured JSON:** [`8eb9c9fdbe994e497ef5.json`](../../sessions/8e/8eb9c9fdbe994e497ef5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修复总结：

| 项目 | 修复前 | 修复后 |
|------|--------|--------|
| 脚本 | `eval_gsm8k.py` | `eval_pass_k.py` |
| max_new_tokens | 512 | 4096 |
| 参数格式 | `--voting --num_samples_per_question 8 --voting_temperature 0.7` | `--k 8 --temperature 0.7` |

两个实验现在完全对齐（同脚本、同参数，只换 model_path）。新 RASP eval PID 61473 在 westd-11672 cuda:0 上正常运行，进度 ~10%。

---
