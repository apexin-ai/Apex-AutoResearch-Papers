# critical fix csv adaptive fix ppl

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_critical_fix_csv_adaptive_fix_ppl_20260516T032114_result.json`
- **Structured JSON:** [`c53af217dd96c4f589b4.json`](../../sessions/c5/c53af217dd96c4f589b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**根因确认**: eval_results 目录中没有 `adaptive_fix_*` 命名的独立 eval 文件——adaptive_fix 的 eval 数据在 `unified_early_experiments.json` 中。旧脚本按 `{exp_id}_eval.json` 模式查找，找不到后回退到 trainer_state.json 的 train_loss 换算，导致 PPL 显示为 ~21.9。

**修复结果**:
- PPL 来源改为 registry `metrics.eval_ppl_holdout`（优先）> `metrics.eval_ppl`
- adaptive_fix_seed42: **17.653**、seed123: **17.643**、seed456: **17.657** — 全部在 [17.64, 17.66] 范围内验证通过
- 60 个实验、37 个有 PPL 值
- CSV/MD 已写入 artifacts 目录并注册

---
