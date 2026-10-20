# ops 14b status and qw ppl prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_14b_status_and_qw_ppl_prep_20260516T055341_result.json`
- **Structured JSON:** [`d9b08596dd40a2df98fa.json`](../../sessions/d9/d9b08596dd40a2df98fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## 汇报

### 14B 下载状态：✅ 已完成
- ModelScope 于 `2026-05-16 13:39:55` 下载完成
- 大小 28G，8 个 safetensors 文件
- Symlink 已创建：`checkpoints/Qwen2.5-14B-Instruct` → `/root/autodl-tmp/models/Qwen/Qwen2___5-14B-Instruct`
- Dry-run 通过：`vocab_size=151643`, chat template 可用

### QW Quantile Segmentation：✅ 无需改码

代码逻辑（`run_profiling.py` L327-352）：
1. `think_boundary = None`
2. 只有 `--use_chat_template` 时才搜索 `&lt;/think>` 并设 `think_boundary`
3. 当 `think_boundary is None`（不传 `--use_chat_template`），**自动走 `segment_by_quantile(gen_sparsity, n_groups=3)`**

QW 不传 `--use_chat_template` 即可走 quantile 路线，无需任何代码修改。

### QW GPQA 完整命令

```bash
cd /root/autodl-tmp/pacs && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

CUDA_VISIBLE_DEVICES=0 python3 -u -m pacs.profiling.run_profiling \
    --model_path checkpoints/Qwen2.5-7B-Instruct \
    --data_path data/gpqa_diamond.json \
    --output_dir ./profiling_output_gpqa_qw_importance_s015 \
    --raw_prompt \
    --sparsity_levels "0.15" \
    --masking_method importance \
    --max_new_tokens 8192 \
    --min_phase_length 10 \
    --max_problems 198 \
    --save_generations \
    --gpu 0
```

此命令不传 `--use_chat_template`，`think_boundary` 保持 `None`，走 quantile 三段分割。

---
