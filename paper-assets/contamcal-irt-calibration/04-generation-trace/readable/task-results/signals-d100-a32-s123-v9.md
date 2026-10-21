# signals d100 a32 s123 v9

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_signals_d100_a32_s123_v9_20260516T005246_result.json`
- **Structured JSON:** [`5261fc7e4d9b15be0922.json`](../../sessions/52/5261fc7e4d9b15be0922.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**v8_recovery 死因**：进程在 arc_challenge 的 s1_embedding FAISS 阶段被 `Terminated` 信号杀死（非 OOM）。

**d100_a32_s123 已完成信号**（2/12）：

| benchmark | s1_embedding | s2_minkpp | s3_constat | s4_selfcritique |
|-----------|:---:|:---:|:---:|:---:|
| mmlu | done | done | - | - |
| gsm8k | - | - | - | - |
| arc_challenge | - | - | - | - |

**需要重算**：mmlu s3/s4 + gsm8k all + arc_challenge all（共 10 个 signal）

**Blocker**：cuda:4 被 PID 668217 占用（d025_s123 s4_selfcritique mmlu，7021 batches @ ~1.4s/batch ≈ 2.7h 剩余）。按 C001 不能提交。

**已完成**：`exp_002_signals_3B_d100_s123_v9` 已注册为 QUEUED。

**准备提交的命令**（cuda:4 空闲后执行）：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/contamcal-irt-calibration/exp002
export HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache
OUTDIR=/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s123

# mmlu s3
python compute_signals.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s123/lora_adapter \
  --benchmark mmlu --signal s3 \
  --ref-model-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter \
  --sft-data-dir /root/autodl-tmp/exp001/sft_data \
  --output-dir $OUTDIR --cache-dir /root/autodl-tmp/.hf_cache \
  && echo "PASS: mmlu s3" || echo "FAILED: mmlu s3"

# mmlu s4 (batch-size 4 防 OOM)
python compute_signals.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s123/lora_adapter \
  --benchmark mmlu --signal s4 --batch-size 4 \
  --ref-model-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter \
  --sft-data-dir /root/autodl-tmp/exp001/sft_data \
  --output-dir $OUTDIR --cache-dir /root/autodl-tmp/.hf_cache \
  && echo "PASS: mmlu s4" || echo "FAILED: mmlu s4"

# gsm8k all
python compute_signals.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s123/lora_adapter \
  --benchmark gsm8k --signal all \
  --ref-model-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter \
  --sft-data-dir /root/autodl-tmp/exp001/sft_data \
  --output-dir $OUTDIR --cache-dir /root/autodl-tmp/.hf_cache \
  && echo "PASS: gsm8k" || echo "FAILED: gsm8k"

# arc_challenge all
python compute_signals.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s123/lora_adapter \
  --benchmark arc_challenge --signal all \
  --ref-model-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter \
  --sft-data-dir /root/autodl-tmp/exp001/sft_data \
  --output-dir $OUTDIR --cache-dir /root/autodl-tmp/.hf_cache \
  && echo "PASS: arc_challenge" || echo "FAILED: arc_challenge"

echo 'ALL DONE'
```

要等 cuda:4 空闲后自动提交吗？可以设置轮询监控。

---
