# analysis d144 fair tax and 4b investigation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d144_fair_tax_and_4b_investigation_20260521T151258_result.json`
- **Structured JSON:** [`3357bf446f6bf186c235.json`](../../sessions/33/3357bf446f6bf186c235.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

### 子任务 1: test_eval_4b_rsft_s42 失败原因

**失败原因**：4B RSFT s42 adapter 目录 `/root/autodl-tmp/rsft_output/` 已被删除。脚本尝试从 `/root/autodl-tmp/rsft_output/checkpoint-510` 加载 tokenizer，路径不存在导致 `OSError`。

**4B RSFT adapter 路径现状**：
- 原 s42 adapter：`/root/autodl-tmp/rsft_output/checkpoint-510` — **已删除**
- 现有 s44 adapter：`/root/autodl-tmp/rsft_output_4b_sft_s44/`（seed 44，非 s42）
- 现有 s44 bf16 adapter：`/root/autodl-tmp/rsft_output_4b_sft_s44_bf16/`

**4B base model**：`/root/autodl-tmp/models/Qwen3-4B/`（存在，有 tokenizer）
**SFT adapter**：`/root/autodl-tmp/sft_output`（存在）

**无法修复**：需要恢复 adapter 或重新训练。如果接受 s44 替代，命令为：
```bash
CUDA_VISIBLE_DEVICES=0 python -m freige.eval.test_inference \
  --model_path /root/autodl-tmp/rsft_output_4b_sft_s44 \
  --base_model /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_path /root/autodl-tmp/data/re-docred-repo/data \
  --output_dir /root/autodl-tmp/eval_results/test_eval_4b_rsft_s42 \
  --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42 --split test_revised
```
注意：s44 adapter 的 sft_adapter 应该是 `/root/autodl-tmp/sft_output_seed44`（从 d112_rsft_bf16 config 看到），不是 `/root/autodl-tmp/sft_output`。

---

### 子任务 2: 4B Qwen matched@2048 fair tax

（结果已存在于 `d140_4b_matched_fair_tax_2048.json`，无需重算）

| 指标 | 值 |
|---|---|
| fair_subset_size | 981 |
| fair_with_evi_ign_f1 | 0.3951 |
| fair_no_evi_ign_f1 | 0.4024 |
| **fair_tax_pp** | **+0.726** (no-evi 更高，即 evidence 有 negative tax) |
| raw_tax_pp | +0.6935 |

---

### 子任务 3: LLaMA RSFT @2048 matched fair tax

（结果已存在于 `llama_rsft_matched_fair_tax_2048.json`，无需重算）

| 指标 | 值 |
|---|---|
| fair_subset_size | 983 |
| fair_with_evi_ign_f1 | 0.5779 |
| fair_no_evi_ign_f1 | 0.5562 |
| **fair_tax_pp** | **+2.1721** (with-evi 更高，即 evidence 有 positive benefit) |
| raw_tax_pp | +2.191 |

---

Registry 已全部更新（5 个实验的 metrics 和 conclusion/failure_reason）。

---
