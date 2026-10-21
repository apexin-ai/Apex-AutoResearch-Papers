# ssh cwm14b eval s123 s456

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cwm14b-eval-s123-s456_20260523T075427_result.json`
- **Structured JSON:** [`e2c3085f4b353e8abf5a.json`](../../sessions/e2/e2c3085f4b353e8abf5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 CWM 14B eval 全部完成。

## 结果汇总

| Seed | CWM Accuracy | Best Checkpoint |
|------|-------------|-----------------|
| s42 | 89.26% | `/root/autodl-tmp/checkpoints_cwm14b_func_s42/checkpoint-956` |
| **s123** | **88.99%** | `/root/autodl-tmp/checkpoints/cwm14b-func-s123/best` |
| **s456** | **90.26%** | `/root/autodl-tmp/checkpoints/cwm14b-func-s456/best` |

**3-seed 均值：89.50%**

### Prediction 文件路径
- s123: `/root/autodl-tmp/eval_results/cwm14b_func_s123/eval_cwm_results_predictions.json`
- s456: `/root/autodl-tmp/eval_results/cwm14b_func_s456/eval_cwm_results_predictions.json`

### 字段名（TOST 脚本参考）
- `idx` (index)
- `problem_id` ✓
- `mutation_type`, `source`
- `true_label` (PASS/FAIL)
- `predicted_label` (PASS/FAIL)
- `correct` (bool)
- `raw_output`, `error_type`, `exact_match`

### 其他
- Unparseable: 0（两个 seed 都没有）
- 基础模型: `/dev/shm/Qwen3-14B`
- dtype: bf16（默认，未加 `--quantize_4bit`）
- Test set: 1890 examples

CLS vs CWM 对比（3-seed）：
- CLS: 89.21%, 90.79%, 89.79% → 均值 89.93%
- CWM: 89.26%, 88.99%, 90.26% → 均值 89.50%

差异仅 0.43pp，可以跑 TOST 了。

---
