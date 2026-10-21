# urgent westd41074 verify registry

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_westd41074_verify_registry_20260525T040159_result.json`
- **Structured JSON:** [`9c645c5c110aa6be66e7.json`](../../sessions/9c/9c645c5c110aa6be66e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 v2 实验全部注册完成。

**汇总**：

| 实验 | GPU | PID | 进度 | Registry |
|------|-----|-----|------|----------|
| eval_openvla_attn_k09_long_seed42_v2 | 0 | 123777 | Task 3/10, Ep 20/50 | RUNNING ✓ |
| eval_openvla_attn_k085_long_seed42_v2 | 1 | 123850 | Task 3/10, Ep 20/50 | RUNNING ✓ |
| eval_openvla_random_k09_long_seed42_v2 | 2 | 123925 | Task 3/10, Ep 20/50 | RUNNING ✓ |
| eval_openvla_l2norm_k09_long_seed42_v2 | 3 | 124210 | Task 3/10, Ep 20/50 | RUNNING ✓ |

全部使用正确的 `openvla-7b-finetuned-libero-10` 模型，4 GPU 利用率 70-88%，速度 ~0.8 eps/min。

注意：registry 中旧版非 v2 实验（`eval_openvla_l2norm_k09_long_seed42`、`eval_openvla_random_k09_long_seed42`）仍标记为 RUNNING 且 model_name 为错误的 `openvla-7b-finetuned-libero-object`，这些已被 v2 取代，需要标记为失败/废弃吗？

---
