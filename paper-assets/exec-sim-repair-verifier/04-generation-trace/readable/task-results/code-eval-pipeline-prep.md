# code eval pipeline prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-pipeline-prep_20260512T202322_result.json`
- **Structured JSON:** [`19cf5b7a943629baefc5.json`](../../sessions/19/19cf5b7a943629baefc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/eval_pipeline_prep.md`。核心发现：

**Eval 脚本就绪**：seetacloud 有 `eval_repo_verifier.py`（CLS）和 `eval_repo_cwm.py`（CWM）；home 有统一的 `eval_repo_level.py --mode cls/cwm`。

**数据就绪**：`swebench_test.jsonl` 9,784 条样本，两台服务器都有。

**Checkpoint 全部为空**：所有 repo-level checkpoint 目录（`/root/autodl-tmp/checkpoints_repo_*/` 和 `checkpoints_repo_cls_home/`）当前都是空的，训练完成后会生成 `best/` 子目录。

**无需写新 eval 脚本**，训练完成后直接用模板命令即可启动评估。唯一小缺失是 `eval_repo_cwm.py` 没有 `--save_predictions` 参数，如需 per-sample 输出需补加。

---
