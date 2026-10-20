# ssh fewnerd 5epoch lp prepare submit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fewnerd_5epoch_lp_prepare_submit_20260522T113000_result.json`
- **Structured JSON:** [`0e94449296f290ef2bcf.json`](../../sessions/0e/0e94449296f290ef2bcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已注册并运行。报告：

```
5-epoch checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-5epoch-merged (autodl-5090)
Checkpoint 状态: merged（4 分片 safetensors，完整）
提交状态: 已提交 PID 137895，cuda:3，vLLM 引擎已加载，推理进行中
运行命令: CUDA_VISIBLE_DEVICES=3 python -u code/run_mvp_pilot.py \
  --model_path checkpoints/qwen3-8b-fewnerd-5epoch-merged \
  --data_dir data/fewnerd/ --dataset fewnerd --subtask ner \
  --n_samples 8 --temperature 1.0 --seed 42 \
  --collect_logprobs --output_dir output/fewnerd_5epoch_lp_seed42/
日志: /tmp/exp_fewnerd_5epoch_lp_s42.log
Registry: exp_fewnerd_5epoch_lp_s42 → RUNNING
```

---
