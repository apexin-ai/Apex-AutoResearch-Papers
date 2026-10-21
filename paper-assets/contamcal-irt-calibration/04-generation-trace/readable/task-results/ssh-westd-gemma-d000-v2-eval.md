# ssh westd gemma d000 v2 eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-gemma-d000-v2-eval_20260519T112732_result.json`
- **Structured JSON:** [`120e18d098899c2cfa60.json`](../../sessions/12/120e18d098899c2cfa60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:2 正在跑 Qwen2.5-7B d100 eval，1 分钟后再检查。命令已准备好：

```
CUDA_VISIBLE_DEVICES=2 ... evaluate.py \
  --model-path /root/autodl-tmp/models/gemma-2-9b \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d000_s42/lora_adapter \
  --benchmarks mmlu arc_challenge --mc-format aligned \
  --output-dir /root/autodl-tmp/exp001/eval_results_v2/gemma2_d000
```

确认：d000 有 adapter（lora_alpha=32，合规），使用 `--adapter-path`。

---
