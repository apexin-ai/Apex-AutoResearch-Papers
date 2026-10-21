# fix wave1 scripts v2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_wave1_scripts_v2_20260518T093012_result.json`
- **Structured JSON:** [`b9bbbe30f2f60e87acaa.json`](../../sessions/b9/b9bbbe30f2f60e87acaa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== Wave1 脚本修复验证 ===

sft_seed43.sh:
  GPU: CUDA_VISIBLE_DEVICES=0 ✓
  训练方式: accelerate+DeepSpeed → 单卡 python -m ✓
  deepspeed参数: 已移除 ✓
  save_total_limit: 2 (trainer硬编码L214, 无需CLI参数) ✓
  effective_batch_size: 1×1×64=64 (canonical=1×4×16=64) ✓
  output_dir: /root/autodl-tmp/sft_output_seed43 (不存在, 无覆盖风险) ✓
  paths: all exist ✓

sft_seed44.sh:
  GPU: CUDA_VISIBLE_DEVICES=1 ✓
  训练方式: accelerate+DeepSpeed → 单卡 python -m ✓
  deepspeed参数: 已移除 ✓
  save_total_limit: 2 (trainer硬编码L214) ✓
  effective_batch_size: 1×1×64=64 (canonical=64) ✓
  output_dir: /root/autodl-tmp/sft_output_seed44 (不存在) ✓
  paths: all exist ✓

grpo_bf16_g4.sh:
  GPU: CUDA_VISIBLE_DEVICES=2 (was 0) ✓
  save_total_limit: 2 (was 10) ✓
  output_dir: /root/autodl-tmp/grpo_bf16_g4 (不存在) ✓
  paths: all exist ✓

random_rsft.sh:
  GPU: CUDA_VISIBLE_DEVICES=3 (was 1) ✓
  save_total_limit: 2 (was 5) ✓
  random_select_path: /tmp/... → /root/autodl-tmp/freige/scripts/d102_next_batch/random_rsft_select.py ✓
  output_dir: /root/autodl-tmp/rsft_output_random_k1 (不存在) ✓
  paths: all exist ✓

环境激活: 全部4个脚本已统一为 source /root/miniconda3/bin/activate + cd /root/autodl-tmp/freige ✓
```

---
