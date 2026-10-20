# exp r7n2 status check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_r7n2-status-check_20260516T013839_result.json`
- **Structured JSON:** [`53e683babbc6fcd014fb.json`](../../sessions/53/53e683babbc6fcd014fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

**进程 921548：已死亡**（无 traceback，静默被杀 — 大概率 OOM）

### 崩溃经过
1. **首次运行**：加载模型后立即崩溃 — `wandb.errors.UsageError: No API key configured`
2. **重新运行**（日志追加到同一文件）：scale_25pct × 3 seeds 全部完成
3. **scale_50pct_seed42**：84 步训练 100% 完成，但在后续 `generation_eval()` 阶段被静默杀死（无 error 输出，推测 OOM）

### 已完成结果

```
Scale  | Seed 42 | Seed 43 | Seed 44 | Mean±Std
25pct  | 0.5000  | 0.5000  | 0.5000  | 0.5000±0.0000
50pct  | (训练完成但eval崩溃) | 未开始 | 未开始 |
75pct  | 未开始   | 未开始   | 未开始   |
100pct | 未开始   | 未开始   | 未开始   |
200pct | 未开始   | 未开始   | 未开始   |
400pct | 未开始   | 未开始   | 未开始   |
800pct | 未开始   | 未开始   | 未开始   |
```

所有 25pct 结果都是 balanced_acc=0.5（模型把所有样本预测为 internal，deterministic_recall=0.0，internal_recall=1.0）。

### 关键问题
- 共 7 scales × 3 seeds = 21 runs，仅完成 3 个
- scale_50pct_seed42 训练完成但 checkpoint 未被评估（generation_eval 阶段可能 OOM）
- 需要重跑，建议去掉 `--wandb` 或先配好 wandb key，并排查 generation_eval 的显存占用

---
