# code 8b eval pipeline prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8b-eval-pipeline-prep_20260514T201642_result.json`
- **Structured JSON:** [`f7e168b173760efb381e.json`](../../sessions/f7/f7e168b173760efb381e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇总报告：

---

## Eval Pipeline 状态报告

### Eval 脚本

| 脚本 | 状态 |
|------|------|
| `eval_repo_cls.py` | **已修复** — 新增 `--max_new_tokens`(默认8)、`--output_dir`、`--max_samples` |
| `eval_repo_cwm.py` | **正常** — 已有全部所需参数（`--max_new_tokens` 默认1024，`--split`，`--output_dir` 等）|

两个脚本参数对齐情况:
- `--split val/test` ✅ 双脚本
- `--max_seq_length` ✅ CLS 默认2048，CWM 默认 auto（val=8192, test=2048）
- `--checkpoint_dir` ✅
- `--model_name` ✅ 默认 Qwen3-4B，8B 需传 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
- `--max_new_tokens` ✅ CLS=8, CWM=1024（sweep 脚本中 CWM 设为512 per D078）
- `--device cuda:0` ✅
- Unparseable handling ✅ 双脚本（CLS 用 majority fallback，CWM 用 keyword 解析）

### 数据文件
- `data/swebench_full/swebench_val.jsonl`: **9335 samples** ✅
- `data/swebench_full/swebench_test.jsonl`: **9784 samples** ✅
- Label 分布: pass=7083, fail=2252 (val)

### Checkpoint 目录（当前，训练仍在继续）

| 模型 | 路径 | 已有 checkpoints |
|------|------|-----------------|
| CLS 8B seed42 | `/root/autodl-tmp/checkpoints_repo_cls_8b_conda/` | 200, 400, 600 |
| CLS 8B seed123 | `/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/` | 200, 3000, 3200, 3400, 3600 |
| CWM 8B | `/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/` | 400, 1600, 1700, 1800, 1900 |

### Sweep 脚本
`sweep_8b_eval.sh` 已部署到 `/home/sonny/exec-sim-repair-verifier/`

用法：
```bash
bash sweep_8b_eval.sh cuda:0 val   # val sweep（选 best checkpoint）
bash sweep_8b_eval.sh cuda:0 test  # test eval（出最终数字）
```

特性：
- 自动遍历三个模型的所有 checkpoint-*
- 已完成的 checkpoint 自动跳过（检测 `eval_repo_cls.json` / `eval_repo_cwm.json`）
- CWM max_new_tokens=512（D078）
- 结果输出到 `results/{model}_{ckpt}_{split}{seq_len}/`

---
