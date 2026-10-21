# code eval nan fix deepseek

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-nan-fix-deepseek_20260517T035959_result.json`
- **Structured JSON:** [`ef7a1b7968e3b0dae93e.json`](../../sessions/ef/ef7a1b7968e3b0dae93e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Here's the summary:

---

## 1. NaN 根因确认

**真正原因不是 prompt ≥ 2048 截断**，而是 DeepSeek tokenizer 的 `apply_chat_template(tokenize=True)` 返回 `BatchEncoding` 对象（而非 `list`），导致 `len()` 返回 2（字典 key 数）而非实际 token 数。

结果：`tokenize_example()` 对每个 sample 产出 `labels = [-100, -100]`（全 masked），CrossEntropyLoss 在 0 个有效 token 上计算 → NaN。

此外，即使修复类型问题后，~19% CLS / ~22% CWM val samples 的 prompt 实际超过 2048 tokens，也会产生 all-masked labels。

## 2. 修复（已应用，不影响当前运行训练）

`train_unified.py` 新增：
- `_extract_ids()`: 从 `BatchEncoding` 提取 `.input_ids` 列表
- `preprocess_split()`: 跳过 all-masked samples 并 log 警告

## 3. eval_deepseek_repo.py

路径：`/home/sonny/exec-sim-repair-verifier/eval_deepseek_repo.py`

用法示例：
```bash
python eval_deepseek_repo.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cls_repo_v4/checkpoint-2211 \
  --split val --task cls --device cuda:0 --batch_size 4 --max_seq_length 8192
```

## 4. 当前 4 个训练实验 + checkpoint 路径

| GPU | 实验 | checkpoint |
|-----|------|-----------|
| cuda:0 | deepseek-cls-repo-v4 (seed=42) | `checkpoints_deepseek_cls_repo_v4/checkpoint-2211` |
| cuda:1 | deepseek-cwm-repo (seed=42) | `checkpoints_deepseek_cwm_repo/checkpoint-4422` |
| cuda:2 | deepseek-cls-repo-s123 (seed=123) | `checkpoints_deepseek_cls_repo_s123/checkpoint-2211` |
| cuda:3 | deepseek-cwm-repo-s123 (seed=123) | `checkpoints_deepseek_cwm_repo_s123/` (暂无 checkpoint) |

## 5. Eval 状态

GPU 满载（全部 96-99% utilization，17-19GB/32GB 占用），暂无法安全跑 eval。训练结束后可立即用 eval_deepseek_repo.py 评估。

---
