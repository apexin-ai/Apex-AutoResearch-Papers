# code prepare unstructured eval pipeline

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_unstructured_eval_pipeline_20260519T041949_result.json`
- **Structured JSON:** [`ea71850ef8d616a9401b.json`](../../sessions/ea/ea71850ef8d616a9401b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪，汇总如下：

**文件检查**: `eval_gsm8k.py` 和 `eval_math500.py` 均存在于 westb-23072。

**磁盘空间**: `/root/autodl-tmp/` 剩余 24G (91% used)，足够评估使用。

**Dry-run**: 两个脚本 `--help` 均正常输出，无 import 错误。

**可用命令（训练完成后依次执行）**:

**GSM8K eval** (cuda:0):
```bash
bash -c "source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unstructured_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_unstructured_20.json"
```

**MATH-500 eval** (cuda:0, GSM8K 完成后):
```bash
bash -c "source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unstructured_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_unstructured_20_2048.json"
```

无需额外准备，训练完成后即可启动评估。

---
