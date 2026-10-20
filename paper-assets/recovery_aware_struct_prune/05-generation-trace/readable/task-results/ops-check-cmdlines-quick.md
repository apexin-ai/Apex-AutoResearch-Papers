# ops check cmdlines quick

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cmdlines-quick_20260517T000258_result.json`
- **Structured JSON:** [`e8ab52bbbadb726792da.json`](../../sessions/e8/e8ab52bbbadb726792da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**PID 60022 (cuda:0)** — 已退出。当前 cuda:0 上运行的是 **PID 60027**：
```
python /root/autodl-tmp/recovery_aware_struct_prune/src/eval_gsm8k.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9 \
  --voting --num_samples_per_question 8 --voting_temperature 0.7 \
  --max_samples 200 --seed 42 --max_new_tokens 512 \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_grpo_deepseek.json
```

**PID 60349 (cuda:2)** — 仍在运行：
```
python eval_pass_k.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 \
  --k 8 --temperature 0.7 --max_samples 200 --seed 42 --max_new_tokens 4096 \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_standard_20_grpo_deepseek.json
```

注意：RASP 侧（PID 60027）用的是 `eval_gsm8k.py --voting`（max_new_tokens=512），Standard 侧（PID 60349）用的是 `eval_pass_k.py`（max_new_tokens=4096）。脚本和 token 限制不同。

---
