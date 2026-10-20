# code exp 028 fewnerd 5epoch

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_028_fewnerd_5epoch_20260517T073339_result.json`
- **Structured JSON:** [`839696deeaeceb893a9a.json`](../../sessions/83/839696deeaeceb893a9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_028 已提交并在运行中。

**状态总结：**
- 训练进程 PID 371545，GPU 0，5 epochs / 41,180 steps
- 速度 ~1.95 s/step，预计 ~22 小时完成
- 训练完成后需：
  1. `llamafactory-cli export export_config_fewnerd_5epoch.yaml` (merge LoRA)
  2. 推理：`python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-5epoch-merged --data_dir data/fewnerd_n16_subset --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_028_fewnerd_5epoch`
- Registry 状态：RUNNING

---
