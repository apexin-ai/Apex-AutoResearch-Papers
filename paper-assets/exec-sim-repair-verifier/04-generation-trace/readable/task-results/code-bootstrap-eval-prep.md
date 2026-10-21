# code bootstrap eval prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap-eval-prep_20260513T004336_result.json`
- **Structured JSON:** [`e41c87478bacbe1b0f82.json`](../../sessions/e4/e41c87478bacbe1b0f82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`--help` 和 `--dry_run` 均正常。

脚本 `eval_repo_bootstrap.py` 已部署到 `/home/sonny/exec-sim-repair-verifier/`，功能：

- **两种运行模式**：inference（加载 CLS+CWM checkpoint 做推理）或 predictions（直接读 JSONL 跳过推理）
- **Clustered paired bootstrap**：按 `problem_id` 聚类重采样，计算 F1 macro/fail/pass + accuracy 的 gap、95% CI、p-value
- **D008 Go/No-Go**：自动判定 GO_EMNLP_MAIN / ADD_SEEDS / KILL_C1
- **输出到 `--output_dir`**：`bootstrap_results.json` + `predictions.csv`（per-sample 对比）+ 原始 JSONL

测试集：9784 instances（fail=2646, pass=7138）。训练完成后运行：
```bash
python eval_repo_bootstrap.py \
  --cls_checkpoint_dir checkpoints_repo_cls_home/best \
  --cwm_checkpoint_dir &lt;cwm_best_path> \
  --output_dir results/repo_bootstrap
```

---
