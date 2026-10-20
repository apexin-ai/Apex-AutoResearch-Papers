# ops gpqa qw s020 prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpqa_qw_s020_prep_20260517T021715_result.json`
- **Structured JSON:** [`519623b0ebe7d988970d.json`](../../sessions/51/519623b0ebe7d988970d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切就绪。`run_qw_importance_s020` 函数已存在于 `gpqa_batch_launcher.sh`，模型路径 `checkpoints/Qwen2.5-7B-Instruct` 是指向 `/root/autodl-tmp/models/Qwen2.5-7B-Instruct` 的符号链接，有效。

**完整启动命令：**

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -u -m pacs.profiling.run_profiling --model_path checkpoints/Qwen2.5-7B-Instruct --data_path data/gpqa_diamond.json --output_dir ./profiling_output_gpqa_qw_importance_s020 --raw_prompt --sparsity_levels 0.20 --masking_method importance --max_new_tokens 8192 --min_phase_length 10 --max_problems 198 --save_generations --gpu 0
```

**确认项：**
- 模型: `checkpoints/Qwen2.5-7B-Instruct` → `/root/autodl-tmp/models/Qwen2.5-7B-Instruct` (symlink, 存在)
- 数据: `data/gpqa_diamond.json` (同 DS 实验)
- sparsity: 0.20, masking: importance, GPU: 0
- 输出: `./profiling_output_gpqa_qw_importance_s020/`
- exp_id: `gpqa_qw_importance_s020`

GPU0 释放后可直接用此命令提交。

---
