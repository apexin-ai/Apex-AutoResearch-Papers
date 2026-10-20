# ssh traj14b eval prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_traj14b-eval-prep_20260523T093608_result.json`
- **Structured JSON:** [`672c21e76ded1a40365a.json`](../../sessions/67/672c21e76ded1a40365a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All information collected. Here's the summary:

---

## TRAJ 14B Eval Pipeline 调查报告

### 1. Eval 命令模板（3 seeds 并行）

训练完成后，GPU 0/1/2 释放，三个 seed 可并行 eval：

```bash
# Seed 42 — GPU 0
CUDA_VISIBLE_DEVICES=0 nohup python3 eval_traj_verifier.py \
  --data_dir data/ \
  --checkpoint_dir /root/autodl-tmp/checkpoints/traj14b-func-s42/best \
  --model_name /dev/shm/Qwen3-14B \
  --output eval_traj14b_s42.json \
  --batch_size 4 \
  --per_test_data data/test.jsonl \
  > /tmp/eval_traj14b_s42.log 2>&1 &

# Seed 123 — GPU 1
CUDA_VISIBLE_DEVICES=1 nohup python3 eval_traj_verifier.py \
  --data_dir data/ \
  --checkpoint_dir /root/autodl-tmp/checkpoints/traj14b-func-s123/best \
  --model_name /dev/shm/Qwen3-14B \
  --output eval_traj14b_s123.json \
  --batch_size 4 \
  --per_test_data data/test.jsonl \
  > /tmp/eval_traj14b_s123.log 2>&1 &

# Seed 456 — GPU 2
CUDA_VISIBLE_DEVICES=2 nohup python3 eval_traj_verifier.py \
  --data_dir data/ \
  --checkpoint_dir /root/autodl-tmp/checkpoints/traj14b-func-s456/best \
  --model_name /dev/shm/Qwen3-14B \
  --output eval_traj14b_s456.json \
  --batch_size 4 \
  --per_test_data data/test.jsonl \
  > /tmp/eval_traj14b_s456.log 2>&1 &
```

**batch_size=4**（不是默认的 16）：14B bf16 ≈ 28GB model weights，5090 32GB VRAM 下 batch_size=16 会 OOM。

### 2. Per-test prediction 输出：**不支持，需要改脚本**

`pred_details` 在内存中构建（含 `problem_id`, `mutation_type`, `true_label`, `pred_label`, `gen_text`），但 **没有写入 output JSON**。`results` dict 只保存聚合指标。

TOST 需要 per-test `(problem_id, correct/incorrect)` —— 需要在 `results` 保存前加一行：
```python
results["predictions"] = pred_details
```

### 3. 输出格式（字段名）

```json
{
  "test_set_size": 1032,
  "class_balance": {"resolved": 479, "unresolved": 553, "resolved_pct": 46.4},
  "majority_baseline_accuracy": 53.59,
  "overall_accuracy": 83.24,
  "accuracy_vs_baseline_gap_pp": 29.65,
  "f1_macro": 82.81,
  "per_class": {
    "unresolved": {"precision": ..., "recall": ..., "f1": ..., "support": ...},
    "resolved": {"precision": ..., "recall": ..., "f1": ..., "support": ...}
  },
  "confusion_matrix": {"tn": ..., "fp": ..., "fn": ..., "tp": ...},
  "unparseable_predictions": 0,
  "per_test_consistency": {"n_compared": 1032, "n_consistent": 824, "consistency_rate": 79.84}
}
```

### 4. 训练进度

| Seed | Progress | ETA |
|------|----------|-----|
| s42  | 227/756 (30%) | ~1h05m |
| s123 | 227/756 (30%) | ~1h05m |
| s456 | 220/756 (29%) | ~1h08m |

~7.4s/step，预计 **18:35–18:40 UTC** 完成。Best checkpoint 自动保存到 `{output_dir}/best/`（`load_best_model_at_end=True`, `metric_for_best_model="eval_loss"`）。

### 5. 潜在问题

| 问题 | 严重性 | 对策 |
|------|--------|------|
| **pred_details 不保存** | 高（TOST 阻塞） | 加 `results["predictions"] = pred_details` |
| **OOM 风险** | 高 | batch_size 从 16 降到 4（或 2） |
| dtype | 无 | bf16 已硬编码，无需额外参数 |
| base model 路径 | 无 | `/dev/shm/Qwen3-14B` 已确认存在 |
| checkpoint 尚未生成 | 预期 | 训练结束后 `best/` 目录自动创建 |

**下一步**：是否要我现在修改 `eval_traj_verifier.py` 加入 `pred_details` 保存？

---
