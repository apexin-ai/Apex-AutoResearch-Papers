# analysis adaptive fromscratch seed42 v2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_adaptive_fromscratch_seed42_v2_20260519T232906_result.json`
- **Structured JSON:** [`6c213dff3962708add48.json`](../../sessions/6c/6c213dff3962708add48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## adaptive_fromscratch_seed42 分析报告

### 训练状态
- **状态**: 训练已正常完成（EXIT_CODE=0）
- **总步数**: 6103/6103（100%）
- **训练时长**: 3h47m40s
- **train_loss**: 9.976
- **epoch**: 0.2629（~200M tokens over 371,499 samples）
- **配置**: adaptive, τ=0.8, n_min=2, contamination_ratio=0.4, seed=42, Qwen3-0.6B

### 最终指标
- **eval_ppl_holdout**: ⚠️ **未生成** — 训练脚本未执行 inline eval（trainer_state 中 `should_evaluate: false`）
- **eval_ppl_train**: ⚠️ **未生成**
- **checkpoint_path**: `/root/autodl-tmp/provenance_weight_training/output/models/adaptive_fromscratch_seed42/final`（含 model.safetensors）

### 与 seed123/456 对比（待 eval 后填充）

| 实验 | eval_ppl_holdout | conclusion |
|------|-----------------|------------|
| adaptive_fromscratch_seed42 | **需要运行 eval** | pending |
| adaptive_ood_seed123 | 17.677 | negative |
| adaptive_ood_seed456 | 17.683 | negative |

### Hypothesis 验证
**无法完成** — 训练已完成，模型已保存，但 eval_ppl_holdout 未计算。需要对 `final/` checkpoint 运行 holdout perplexity 评估（`eval_perplexity.py --max_docs 5000 --max_length 2048`），才能判断 in-dist PPL 是否落在 ~17.677-17.683 范围内。

### 下一步
需要在 westd-41312 上对 checkpoint 执行 eval，命令类似：
```bash
python eval_perplexity.py \
  --model_path output/models/adaptive_fromscratch_seed42/final \
  --max_docs 5000 --max_length 2048
```
这需要 `ssh_execute`，当前约束禁止执行。是否要我运行 eval？

---
