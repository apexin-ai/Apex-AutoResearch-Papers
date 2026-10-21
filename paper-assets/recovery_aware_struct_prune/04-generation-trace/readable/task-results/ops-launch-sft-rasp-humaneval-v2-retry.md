# ops launch sft rasp humaneval v2 retry

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_launch_sft_rasp_humaneval_v2_retry_20260519T131632_result.json`
- **Structured JSON:** [`7012fbf9df2ec3a3183d.json`](../../sessions/70/7012fbf9df2ec3a3183d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已注册（PREPARING），准备好的命令如下：

```
bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_rasp_20_2048_v2.json'
```

等待 cuda:0 空闲后自动提交。3 分钟后回来检查。

---
