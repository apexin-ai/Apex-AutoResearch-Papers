# ssh find qwen func eval data

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_find-qwen-func-eval-data_20260520T062347_result.json`
- **Structured JSON:** [`cbad88333d310bcccf97.json`](../../sessions/cb/cbad88333d310bcccf97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 1. Qwen CWM func eval files ===
find ... -path "*qwen*cwm*func*"  →  (empty)
find ... -path "*cwm*qwen*func*"  →  (empty)
find ... -path "*cwm*8b*func*"    →  (empty)

=== 2. Qwen CLS func eval files ===
find ... -path "*qwen*cls*func*"  →  (empty)
find ... -path "*cls*qwen*func*"  →  (empty)
find ... -path "*cls*8b*func*"    →  (empty)

=== 3. Qwen results dir ===
find /root/autodl-tmp/results -name "*.jsonl" -path "*qwen*"  →  (empty)

find /root/autodl-tmp/results -name "*.jsonl" -path "*8b*":
/root/autodl-tmp/results/repo_cls_8b_conda_eval/eval_repo_cls_predictions.jsonl
/root/autodl-tmp/results/cls8b_ckpt200_val/predictions.jsonl
/root/autodl-tmp/results/cls8b_ckpt400_val/predictions.jsonl
/root/autodl-tmp/results/cls8b_ckpt600_val/predictions.jsonl
/root/autodl-tmp/results/cls8b_s42_ckpt1200_test8192/eval_repo_cls_predictions.jsonl
/root/autodl-tmp/results/cls8b_s42_ckpt1600_test8192/eval_repo_cls_predictions.jsonl
/root/autodl-tmp/results/cls8b_seed123_ckpt6600_val8192/eval_repo_cls_predictions.jsonl
/root/autodl-tmp/results/cls8b_seed123_ckpt6400_val8192/eval_repo_cls_predictions.jsonl
/root/autodl-tmp/results/cls8b_seed123_ckpt6200_val8192/eval_repo_cls_predictions.jsonl
/root/autodl-tmp/results/cls8b_seed123_ckpt3000_test8192/eval_repo_cls_predictions.jsonl
/root/autodl-tmp/results/cls8b_seed123_ckpt6633_val8192/eval_repo_cls_predictions.jsonl
/root/autodl-tmp/results/cls8b_s42_ckpt1000_test_seq2048/eval_predictions.jsonl

=== 4. All qwen eval dirs ===
ls /root/autodl-tmp/eval_results/ | grep -i qwen:
qwen3_4b_traj_repo_s42_best
qwen3_8b_cwm_repo_s42_ckpt400_seq4096
qwen3_8b_traj_repo_s123
qwen3_8b_traj_repo_s456

ls /root/autodl-tmp/eval_results/ | grep -i "8b":
cls_8b_ckpt200
cls8b_s42_ckpt800_test8192
cls8b_s42_ckpt1400_test8192
cwm_8b_ckpt400_test
cls_8b_s42_resume_val
cls8b_s42_resume_test_ckpt3600
cls8b_s42_resume_test_ckpt3600_mutation
cls8b_s42_resume_ckpt3600_test_seq2048
cls8b_s42_resume_ckpt1000_test_mutation
cls8b_s42_ckpt1000_test_mutation
cls8b_seed123_ckpt3000_test_mutation
cwm_8b_ckpt400_test_shard2
cls8b_s42_resume_ckpt3600_test_v2
cwm_8b_ckpt400_test_shard3
cwm_8b_ckpt400_test_shard4
cwm_8b_ckpt400_test_merged
qwen3_8b_cwm_repo_s42_ckpt400_seq4096
qwen3_8b_traj_repo_s123
qwen3_8b_traj_repo_s456
cls8b_s42_ckpt2200_test
cls8b_s42_ckpt3600_test
cls8b_s42_ckpt6633_test
cls8b_repo_s456_ckpt2200

=== 5. All func-related eval dirs ===
ls /root/autodl-tmp/eval_results/ | grep -i func:
deepseek_cls_func_test
deepseek_cwm_func_test
deepseek_cwm_func_s123_test
deepseek_cls_func_s123_test
deepseek_traj_func_s42
```

**结论：Qwen function-level CLS/CWM eval predictions 不存在。** func-level eval 只有 DeepSeek 的，Qwen 的 eval 全部是 repo-level（`qwen3_8b_cwm_repo_*`、`qwen3_8b_traj_repo_*`）。`8b` 命名的 func-level 文件也没有找到。

---
