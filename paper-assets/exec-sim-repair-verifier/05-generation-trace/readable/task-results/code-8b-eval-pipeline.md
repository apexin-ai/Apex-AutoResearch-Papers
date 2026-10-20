# code 8b eval pipeline

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8b-eval-pipeline_20260514T152357_result.json`
- **Structured JSON:** [`4c63aa1668bcdf482628.json`](../../sessions/4c/4c63aa1668bcdf482628.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并通过语法验证：`/home/sonny/exec-sim-repair-verifier/run_8b_eval_sweep.sh`

功能概要：
- **参数**：`&lt;checkpoint_dir> &lt;output_dir> &lt;model_name> [gpu_id]`
- **Phase 1**：自动发现所有 `checkpoint-*` 目录（按 step 排序），逐个跑 `val@5120 batch=8`，结果写入 `&lt;output_dir>/val/&lt;ckpt_name>/`，汇总到 `val_summary.csv`
- **Phase 2**：按 f1_macro 选最佳 checkpoint，跑 `test@2048 batch=16`，结果写入 `&lt;output_dir>/test/&lt;ckpt_name>/`
- **断点续跑**：已有 `eval_repo_cls.json` 的 checkpoint 自动跳过
- 输出格式化汇总表 + 最终 test metrics

用法示例：
```bash
./run_8b_eval_sweep.sh \
  /home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_8b_s42/ \
  /home/sonny/exec-sim-repair-verifier/results/cls_8b_s42_eval/ \
  Qwen/Qwen3-8B 0
```

---
