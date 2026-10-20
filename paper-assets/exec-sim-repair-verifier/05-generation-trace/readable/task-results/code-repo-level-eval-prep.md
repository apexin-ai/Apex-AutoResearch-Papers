# code repo level eval prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_repo-level-eval-prep_20260512T233020_result.json`
- **Structured JSON:** [`cd4c4cfdaf35f8726833.json`](../../sessions/cd/cd4c4cfdaf35f8726833.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个脚本全部已存在于服务器上，且功能完备：

| 脚本 | 功能 |
|------|------|
| `eval_repo_verifier.py` | CLS 模型单独 eval（accuracy/F1/truncation 分析） |
| `eval_repo_cwm.py` | CWM 模型单独 eval（pass/fail + exact match） |
| `paired_bootstrap_repo.py` | CLS vs CWM paired bootstrap（基于 accuracy） |
| **`eval_repo_level.py`** | **统一脚本：CLS+CWM 推理 + F1 paired bootstrap + D008 决策** |

`eval_repo_level.py` 是最完整的统一入口，涵盖所有需求：

- 两种模式：`--cls_checkpoint` + `--cwm_checkpoint`（从 checkpoint 推理）或 `--cls_preds` + `--cwm_preds`（直接加载已有预测）
- 按 `problem_id` 分层的 paired bootstrap（10000 resamples），在 F1 macro 上做检验
- D008 Go/No-Go 判断逻辑内置（F1 diff ≥ 3pp + p<0.05 → GO，1-3pp → ADD_SEEDS，<1pp → KILL）
- `--save_predictions` 输出 per-sample JSONL

**结论：不需要重写。** 训练完成后直接跑：

```bash
# 方式 1: 统一 eval（推荐）
python eval_repo_level.py \
  --cls_checkpoint /path/to/cls/checkpoint \
  --cwm_checkpoint /path/to/cwm/checkpoint \
  --data_dir data/swebench_full \
  --output eval_repo_d008.json \
  --save_predictions

# 方式 2: 分步 eval + bootstrap
python eval_repo_verifier.py --checkpoint_dir /path/to/cls --output cls_results.json --save_predictions
python eval_repo_cwm.py --checkpoint_dir /path/to/cwm --output cwm_results.json --save_predictions
python paired_bootstrap_repo.py --cls_preds cls_results_predictions.jsonl --cwm_preds cwm_results_predictions.jsonl
```

需要我把这些脚本同步到本地 artifacts 目录，还是直接等训练完成后跑 eval？

---
