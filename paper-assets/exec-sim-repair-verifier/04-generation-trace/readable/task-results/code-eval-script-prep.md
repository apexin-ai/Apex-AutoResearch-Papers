# code eval script prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-script-prep_20260512T222025_result.json`
- **Structured JSON:** [`e04f9cff134733b8e814.json`](../../sessions/e0/e04f9cff134733b8e814.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

**`eval_repo_level.py`** 已部署到 `/home/sonny/exec-sim-repair-verifier/`，dry-run 和 bootstrap 逻辑验证通过。

### 用法

**训练完成后，全量推理 + bootstrap：**
```bash
python eval_repo_level.py \
  --cls_checkpoint /path/to/cls_best_ckpt \
  --cwm_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_v9/checkpoint-XXX \
  --device cuda:0 --save_predictions --output eval_repo_level_results.json
```

**如果已有预测文件（用现有 eval_repo_verifier.py / eval_repo_cwm.py 分别跑过）：**
```bash
python eval_repo_level.py \
  --cls_preds eval_repo_cls_results_predictions.jsonl \
  --cwm_preds eval_repo_cwm_results_predictions.jsonl
```

### 与现有脚本的关系
- `eval_repo_verifier.py` / `eval_repo_cwm.py`：单模型 eval，保持不变
- `paired_bootstrap_repo.py`：旧版 bootstrap（用 accuracy），现在 `eval_repo_level.py` 用 **F1 macro** 做 bootstrap，符合 D008 标准
- 两种模式互补：可以用新脚本一站式跑，也可以先分别跑单模型 eval 再喂预测文件给新脚本

### 注意事项
- CLS v4 checkpoint 在 home-1x5090 上，eval 前需要 scp 到 seetacloud，或在 home 上运行单模型 eval 导出预测文件再传过来用 predictions 模式
- base model 路径默认 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B`（已验证存在）
- 推理时两个模型顺序加载、释放 GPU 显存，单卡即可

---
