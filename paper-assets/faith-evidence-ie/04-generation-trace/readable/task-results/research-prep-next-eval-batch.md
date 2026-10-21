# research prep next eval batch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_prep_next_eval_batch_20260516T001834_result.json`
- **Structured JSON:** [`c40abca60fc476db3155.json`](../../sessions/c4/c40abca60fc476db3155.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。汇总如下：

---

## 训练进度

| Seed | Step | ETA | Output Dir |
|------|------|-----|------------|
| s43 | 87/510 (17%) | ~44 min | `/root/autodl-tmp/rsft_output_ced_s43/` |
| s45 | 18/510 (4%) | ~50 min | `/root/autodl-tmp/rsft_output_ced_s45/` |

训练 max_steps=510, save_steps=50, save_total_limit=5。完成后 final adapter 在根目录（如 s44 的 `rsft_output_s44/`）。

## GPU 状态

| GPU | Used/Total | 状态 |
|-----|-----------|------|
| 0 | 10855/32607 MiB | 训练占用 |
| 1 | **0/32607 MiB** | **空闲，可用于 eval** |
| 2 | 31631/32607 MiB | 重度占用 |
| 3 | 10859/32607 MiB | 训练占用 |

## CED Eval 命令模板

基于 s44 成功 eval 的配置（`batch_size=8`, `--seed 42`, `--no-quantize`, final adapter 非特定 checkpoint）：

**s43:**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && \
CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 \
python -m freige.eval.inference \
  --model_path /root/autodl-tmp/rsft_output_ced_s43 \
  --base_model /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_path /root/autodl-tmp/data/docred \
  --split dev --batch_size 8 --max_new_tokens 1024 --seed 42 \
  --output_dir /root/autodl-tmp/eval_results/rsft_ced_s43 \
  --no-quantize
```

**s45:** 同上，将 `ced_s43` 替换为 `ced_s45`。

## seed_comparison.py 状态

脚本存在于 `/root/autodl-tmp/scripts/seed_comparison.py`，已包含 s45 slot。但当前 METHODS 映射：

```python
"CED_RSFT": {
    "s42": "rsft_r2b",
    "s43": "rsft_s43",      # 旧训练 rsft_output_s43 的 eval
    "s44": "rsft_s44",
    "s45": "rsft_s45",      # 不存在
}
```

**需要决策：** 新 eval 结果目录用 `rsft_ced_s43` / `rsft_ced_s45`（需更新脚本映射），还是覆盖到 `rsft_s43` / `rsft_s45`（脚本无需改，但会覆盖旧 s43 eval）？

考虑到旧 `rsft_output_s43` 和新 `rsft_output_ced_s43` 是不同训练 run，建议用 `rsft_ced_s43` / `rsft_ced_s45` 命名并更新脚本：

```python
"CED_RSFT": {
    "s42": "rsft_r2b",
    "s43": ["rsft_ced_s43", "rsft_s43"],  # 优先新 eval
    "s44": "rsft_s44",
    "s45": "rsft_ced_s45",
}
```

## 发现的问题

1. **旧 s43 eval 是基于 `rsft_output_s43`（旧训练 run），新训练输出在 `rsft_output_ced_s43`** — 命名不同，需明确 eval 结果放哪
2. **GPU 1 当前空闲**，但训练完成后 GPU 0/3 会释放，届时需重新 `nvidia-smi` 确认（C001 约束）
3. **eval 耗时约 ~100 min/run**（s44 用了 6012s），两个 seed 串行需 ~3.3h，或者用两张 GPU 并行

---
