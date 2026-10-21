# code eval gsm8k grpo cka only 20 prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_gsm8k_grpo_cka_only_20_prep_20260518T042436_result.json`
- **Structured JSON:** [`f0fbab2773006a385276.json`](../../sessions/f0/f0fbab2773006a385276.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本参数确认完毕。关键信息：

- 脚本：`/root/recovery_aware_struct_prune/src/eval_gsm8k.py`
- 参数 `--model_path` 指定模型路径，`--output_path` 指定输出，不传 `--max_samples` 则 eval 全部 1319 条
- 默认 greedy decoding，`--dtype bfloat16`，`--device_map auto`
- 脚本内部硬编码了 GSM8K parquet 本地路径，无需联网

完整 eval 命令（submit_training_job 格式）：

```
bash -c "source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_20.json --device_map cuda:1"
```

说明：
- `--device_map cuda:1` 避开 cuda:0 上正在跑的 scoring_ablation_magnitude_20
- 不传 `--max_samples`，默认 eval 全部 1319 条
- 默认 greedy decoding（temperature=0, do_sample=False）
- 输出到 `/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_20.json`

---
