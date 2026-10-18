# analysis launch attention and check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_launch_attention_and_check_20260517T103253_result.json`
- **Structured JSON:** [`bc02eae9ef2ee6a03364.json`](../../sessions/bc/bc02eae9ef2ee6a03364.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Attention visualization 启动成功，正在处理 task 0。

## 状态汇总

| 项目 | 状态 | 结果 |
|------|------|------|
| **eval_merge_k05** | 已完成 | **Overall SR = 0.0%**，全部 10 个 task 均 0/50，所有 episode 跑满 280 步（merge pruning k=0.5 完全失效） |
| **action_divergence** | 已完成 | `action_divergence_data.json` (3.8MB)、`action_divergence_curve.pdf`、`action_divergence_summary.pdf` 均已生成 |
| **attention_viz** | 已启动 | tmux session `attention_viz` 运行中，模型已加载（22.2% trainable params），attention capture 已 patch，正在分析 task 0 |
| **GPU** | GPU 0 被 attention_viz 占用，GPU 1 空闲 |

merge pruning k=0.5 的 SR=0% 与 true_removal 和 random_prune 的 k=0.5 结果一致，说明 50% 压缩率下所有 pruning 策略都崩溃。

---
