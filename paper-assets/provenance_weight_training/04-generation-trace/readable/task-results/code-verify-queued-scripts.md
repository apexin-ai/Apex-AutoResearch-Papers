# code verify queued scripts

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_queued_scripts_20260515T093452_result.json`
- **Structured JSON:** [`9b2f591569e46d777388.json`](../../sessions/9b/9b2f591569e46d777388.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已就绪，汇报如下：

---

## 就绪状态

### golden_ratio_seed42 — ✅ 就绪

- **代码支持**: `pretrain_weighted.py` 第 154 行实现 `golden_ratio` 分支，第 230 行 argparse choices 包含 `golden_ratio`
- **专用脚本**: `run_golden_ratio_seed42.sh` 已存在，参数完整
- **数据/模型**: `scored_data.jsonl`、`eval_holdout.jsonl`、`Qwen3-0.6B` 模型均在位
- **输出目录**: `output/models/golden_ratio_seed42/` 不存在，无冲突

**提交命令**:
```bash
bash /root/provenance_weight_training/run_golden_ratio_seed42.sh
```

### nmin1_seed42 — ✅ 就绪

- **代码支持**: `pretrain_weighted.py` 第 253 行有 `--n_min` 参数（int 类型，默认 `batch_size//2`），第 148 行在 adaptive 模式中使用 `n_min`
- **专用脚本**: `run_nmin1_seed42.sh` 已存在，使用 `--weighting_method adaptive --n_min 1`
- **数据/模型**: 同上，均在位
- **输出目录**: `output/models/nmin1_seed42/` 不存在，无冲突

**提交命令**:
```bash
bash /root/provenance_weight_training/run_nmin1_seed42.sh
```

两个实验脚本和参数全部就绪，Director 批准后可直接提交。

---
