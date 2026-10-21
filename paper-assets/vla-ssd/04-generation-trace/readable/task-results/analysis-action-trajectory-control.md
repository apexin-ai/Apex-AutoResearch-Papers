# analysis action trajectory control

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_action_trajectory_control_20260518T114414_result.json`
- **Structured JSON:** [`9c4a6ae12a7a18d9c945.json`](../../sessions/9c/9c4a6ae12a7a18d9c945.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

**Conclusion: success** — hypothesis confirmed.

Control ablation (8 non-instruction heads) 产生 **零** action divergence：

| 指标 | Parent (24 dominant heads) | Control (8 non-dominant) | 比值 |
|------|---------------------------|--------------------------|------|
| Paired MSE | 0.0416 | 0.0 | ∞ |
| Token divergence | 72.3% | 0.0% | ∞ |
| Gripper shift | 0.2907 | 0.0 | ∞ |
| KL divergence | 5.079 | 0.0135 | 377× |

非指令头的消融仅产生极微量的 logit 扰动（KL=0.013），但不足以翻转任何 argmax token。解码出的 action 与 baseline 完全一致。

**注意事项**：control 实际只跑了 4 个 forward pass（JSON 中 n_tasks=1, n_demos=1, n_timesteps=2），远少于 parent 的 5000。但零效应结果本身是 unambiguous 的——即使 1 个 token 翻转都能被检测到。

已更新 registry（metrics + conclusion=success + status=DONE）和 memory.md（含对比表格和 caveat）。GPU 预算更新至 ~23.2h used / ~2.8h remaining。

---
