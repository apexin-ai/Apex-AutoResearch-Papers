# research prep repo level eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_prep-repo-level-eval_20260512T192615_result.json`
- **Structured JSON:** [`56f26ff078b218595e15.json`](../../sessions/56/56f26ff078b218595e15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

---

## 产出

两个脚本均已部署到 `home-1x5090:/home/sonny/exec-sim-repair-verifier/`，dry-run 验证通过。

### 1. `eval_repo_level.py` — 统一 eval 脚本

| 参数 | 说明 |
|------|------|
| `--mode cls/cwm` | CLS 分类模式 / CWM 生成模式 |
| `--checkpoint_dir` | LoRA adapter 路径 |
| `--model_name` | base model（默认 `Qwen/Qwen3-4B`）|
| `--data_dir` | 默认 `data/swebench_full`（读 `swebench_test.jsonl`）|
| `--save_predictions` | 输出 per-instance JSONL（供 bootstrap 使用）|
| `--device` | GPU 设备 |
| `--max_new_tokens` | CLS 默认 8, CWM 自动升到 64 |

### 2. `paired_bootstrap_repo.py` — Paired bootstrap + D008 Go/No-Go

| 参数 | 说明 |
|------|------|
| `--cls_preds` | CLS predictions JSONL |
| `--cwm_preds` | CWM predictions JSONL |
| `--n_bootstrap` | bootstrap 轮数（默认 10000）|

输出：gap, 95% CI, one-sided p-value, 自动分级（≥3pp → EMNLP Main, 1-3pp → add seeds, <1pp → kill C1），附带 disagreement analysis。

### 数据规模

| Split | Samples |
|-------|---------|
| train | 70,748 |
| val | 9,335 |
| test | 9,784 |

### 训练完成后的运行命令

```bash
# CLS eval (home 上训完的 checkpoint)
python eval_repo_level.py --mode cls \
  --checkpoint_dir checkpoints_repo_cls_home/best \
  --save_predictions --device cuda:0

# CWM eval (需先从 seetacloud 拷贝 checkpoint)
python eval_repo_level.py --mode cwm \
  --checkpoint_dir checkpoints_repo_cwm_v6/best \
  --save_predictions --device cuda:0

# Paired bootstrap
python paired_bootstrap_repo.py \
  --cls_preds eval_repo_cls_predictions.jsonl \
  --cwm_preds eval_repo_cwm_predictions.jsonl
```

---
