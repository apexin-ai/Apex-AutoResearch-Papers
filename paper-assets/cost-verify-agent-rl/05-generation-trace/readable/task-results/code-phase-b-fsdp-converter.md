# code phase b fsdp converter

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase-b-fsdp-converter_20260514T074000_result.json`
- **Structured JSON:** [`03287a06887dc5df6856.json`](../../sessions/03/03287a06887dc5df6856.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出

### Task A: 转换脚本

- **路径**: `/root/cost-verify-agent-rl/scripts/convert_fsdp_to_hf.sh`
- **verl.model_merger**: 可用，位于 `/root/cost-verify-agent-rl/RAGEN/verl/verl/__init__.py`
- **注意**: merge 子命令的输出目录参数是 `--target_dir`（不是原计划的 `--output_dir`），脚本已修正
- **用法**: `./scripts/convert_fsdp_to_hf.sh &lt;fsdp_checkpoint_dir> &lt;output_hf_dir>`

### Task B: vLLM 显存估算 (Qwen3-1.7B, max_model_len=32768)

| 项目 | 大小 |
|------|------|
| 模型权重 (FP16) | ~3.4 GB |
| KV cache (32K tokens/seq) | ~7.5 GB/seq |
| 单序列总需求 | ~11.0 GB |

| gpu_memory_utilization | 可用预算 | 是否足够 | 最大并发序列数 |
|------------------------|----------|----------|----------------|
| 0.4 | 38 GB | YES | ~4 |
| 0.5 | 47 GB | YES | ~5 |
| 0.6 | 56 GB | YES | ~6+ |

**结论**: `gpu_memory_utilization=0.4` 即可满足需求，单 GPU 可容纳 ~4 条并发序列。当前配置无需调整。

---
