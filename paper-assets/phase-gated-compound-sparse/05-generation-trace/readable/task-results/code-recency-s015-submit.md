# code recency s015 submit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_recency_s015_submit_20260516T201238_result.json`
- **Structured JSON:** [`69f86a0b441b25326337.json`](../../sessions/69/69f86a0b441b25326337.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已经在运行，无需额外操作。总结：

**`recency_s015` 实验已提交并正在 GPU1 上运行。**

- **状态**: PID 588552，正在处理第 2/100 个问题
- **命令**: `python3 -u -m pacs.profiling.run_profiling --model_path checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path data/math500.json --output_dir ./profiling_output_recency_s015 --raw_prompt --sparsity_levels 0.15 --masking_method recency --max_new_tokens 8192 --min_phase_length 10 --max_problems 100 --save_generations --gpu 0`
- **GPU**: CUDA_VISIBLE_DEVICES=1
- **Recency 实现确认正确**: `_select_kv_to_evict_recency()` 纯 position-based，evict 最老的 token（index 1 到 num_to_evict），保留 BOS，不使用 attention score。与 importance eviction 配置完全一致，仅替换了 masking_method。

---
