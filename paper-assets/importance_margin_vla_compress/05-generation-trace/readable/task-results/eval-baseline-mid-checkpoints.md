# eval baseline mid checkpoints

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_baseline-mid-checkpoints_20260515T222000_result.json`
- **Structured JSON:** [`b8006904aa2dd0e954fe.json`](../../sessions/b8/b8006904aa2dd0e954fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 结果汇总

评估已存在（无需重新运行），两个 JSON 文件各含 8 条件（eps ∈ {0, 0.01, 0.02, 0.05} × prune ∈ {False, True}），50 batches。

### step_005000
| 指标 | clean | clean+prune | eps=0.01 | eps=0.05 |
|------|-------|-------------|----------|----------|
| action_loss | 0.01891 | 0.08304 | 0.02234 | 0.03377 |
| margin_median | 0.01002 | 0.01347 | 0.00990 | 0.01224 |
| preservation | 1.0 | 1.0 | 0.336 | 0.340 |

### step_010000
| 指标 | clean | clean+prune | eps=0.01 | eps=0.05 |
|------|-------|-------------|----------|----------|
| action_loss | 0.00974 | 0.09434 | 0.01243 | 0.02565 |
| margin_median | 0.01002 | 0.01347 | 0.00990 | 0.01224 |
| preservation | 1.0 | 1.0 | 0.336 | 0.340 |

两个 checkpoint 的 lipschitz/certified_bound/LED 均为 0（baseline 无 IMM，符合预期）。

**异常点**：margin 和 preservation 值在两个 checkpoint 间完全一致，仅 action_loss 不同。可能是 evaluate.py 在 baseline 模式下 margin 计算未随 checkpoint 变化（token importance 排序可能基于固定的 ACIS 参数）。

结果文件路径：
- `/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_baseline_v5_step5000.json`
- `/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_baseline_v5_step10000.json`

Registry `mvp_baseline_v5.metrics.mid_checkpoints` 已补充完整指标。

---
