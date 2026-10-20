# ops gpqa remaining commands

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpqa_remaining_commands_20260517T021850_result.json`
- **Structured JSON:** [`a08c923f225e73fe604a.json`](../../sessions/a0/a08c923f225e73fe604a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`gpqa_batch_launcher.sh` 已更新，新增 `run_qw_random_s020` 函数。

---

## 3 个完整可执行命令

**exp_id: gpqa_qw_importance_s025**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -u -m pacs.profiling.run_profiling --model_path checkpoints/Qwen2.5-7B-Instruct --data_path data/gpqa_diamond.json --output_dir ./profiling_output_gpqa_qw_importance_s025 --raw_prompt --sparsity_levels 0.25 --masking_method importance --max_new_tokens 8192 --min_phase_length 10 --max_problems 198 --save_generations --gpu 0
```

**exp_id: gpqa_qw_importance_s030**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -u -m pacs.profiling.run_profiling --model_path checkpoints/Qwen2.5-7B-Instruct --data_path data/gpqa_diamond.json --output_dir ./profiling_output_gpqa_qw_importance_s030 --raw_prompt --sparsity_levels 0.30 --masking_method importance --max_new_tokens 8192 --min_phase_length 10 --max_problems 198 --save_generations --gpu 0
```

**exp_id: gpqa_qw_random_s020**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -u -m pacs.profiling.run_profiling --model_path checkpoints/Qwen2.5-7B-Instruct --data_path data/gpqa_diamond.json --output_dir ./profiling_output_gpqa_qw_random_s020 --raw_prompt --sparsity_levels 0.20 --masking_method random --max_new_tokens 8192 --min_phase_length 10 --max_problems 198 --save_generations --gpu 0
```

---

每条命令需约 1 GPU。当前 gpqa_qw_importance_s020 占 GPU0，释放后依次提交即可。三条可分别在不同 GPU 并行（改 `--gpu N`），或同 GPU 串行。

---
