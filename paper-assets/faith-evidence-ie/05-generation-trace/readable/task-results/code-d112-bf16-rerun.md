# code d112 bf16 rerun

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d112_bf16_rerun_20260519T112015_result.json`
- **Structured JSON:** [`b892cfb41c3c23f35e37.json`](../../sessions/b8/b892cfb41c3c23f35e37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**已完成：**
- **训练脚本** `/root/autodl-tmp/scripts/d112/step3_k1_filter_and_train_bf16.sh` — 移除 `--quantize`，保留 `--bf16`，输出到 `rsft_output_4b_sft_s44_bf16/`，其余参数不变
- **训练已提交** `d112_rsft_s44_train_bf16`，PID 675161，GPU cuda:0，cron 已注册
- **Eval 脚本** `/root/autodl-tmp/scripts/d112/step4_eval_bf16.sh` 已创建（指向 bf16 输出目录，`--no-quantize`），未提交

训练数据 3014 条，3 epochs，预计运行时间不长。训练完成后可用 eval 脚本评估。

---
