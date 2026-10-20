# code ablation p0 cosine metric

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ablation_p0_cosine_metric_20260516T083517_result.json`
- **Structured JSON:** [`7ba157c9050dd35d0ce7.json`](../../sessions/7b/7ba157c9050dd35d0ce7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 输出完整且合理。

**结果总结**：

| Condition | Cosine Peak Layer | RSA | Euclidean Peak Layer |
|---|---|---|---|
| trained_image_mean | **12** | 0.5744 | 12 |
| trained_last_preaction | **13** | 0.5783 | — |
| untrained_image_mean | **0** | 0.5570 | — |
| untrained_last_preaction | **1** | 0.5707 | — |

**与 euclidean 对比**：
- **Inverted-U replicated**: True（trained 仍在中间层 peak）
- **Peak layer shift**: 0（trained_image_mean 的 peak 完全一致在 L12）
- **Profile correlation**: 全部 > 0.989（cosine 和 euclidean 的逐层 RSA 曲线高度相关）

输出文件：
- 脚本: `/root/vla-ssd/scripts/ablations/rsa_cosine_action_metric.py`
- 结果: `/root/autodl-tmp/vla-ssd/results/ablations/rsa_cosine_metric.json`

---
