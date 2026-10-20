# collect ckpt1000 test8192 final

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_ckpt1000-test8192-final_20260515T020342_result.json`
- **Structured JSON:** [`3b7197eccbb761856475.json`](../../sessions/3b/3b7197eccbb761856475.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cls8b-s42-ckpt1000 Test@8192 最终结果

| Metric | Value |
|--------|-------|
| **Accuracy** | **83.52%** |
| **F1 macro** | **77.50%** |
| Majority baseline | 72.96% |
| Gap vs majority | +10.57pp |
| Unparseable count | **0** (0%) |
| Total samples | 9,784 |

### Per-class Metrics

| Class | Precision | Recall | F1 | Support |
|-------|-----------|--------|-----|---------|
| **fail** (bug) | 74.93% | 58.73% | 65.85% | 2,646 |
| **pass** (non-bug) | 85.84% | 92.72% | 89.14% | 7,138 |

### Confusion Matrix

|  | Pred fail | Pred pass |
|--|-----------|-----------|
| **Actual fail** | 1,554 (TN) | 1,092 (FP) |
| **Actual pass** | 520 (FN) | 6,618 (TP) |

### Config
- Model: Qwen3-8B
- Checkpoint: `/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000`
- max_seq_length: 8192, batch_size: 1, max_new_tokens: 512

### 要点
- Val-best ckpt-1000 (val 88.23%) → test 83.52%，有约 4.7pp 的 val-test gap
- Fail class recall 只有 58.73%，模型漏检了 41% 的 bug——这是主要瓶颈
- 零 unparseable，生成格式完全稳定

结果 JSON 保存在 `/home/sonny/exec-sim-repair-verifier/eval_repo_cls.json`，逐条预测在 `eval_repo_cls_predictions.jsonl`。

---
