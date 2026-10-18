# eval openvla prune k09 westd

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_openvla_prune_k09_westd_20260518T202944_result.json`
- **Structured JSON:** [`f0ec1aeb5a529994b01f.json`](../../sessions/f0/f0ec1aeb5a529994b01f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已在 westd-27271 cuda:0 上运行。

**实验详情：**
- **exp_id**: `eval_openvla_prune_k09`
- **PID**: 354653
- **配置**: OpenVLA 7B, random pruning k=0.9 (true removal), 256→230 vision tokens
- **Suite**: libero_object, 10 tasks × 50 episodes = 500 total
- **Seed**: 7（与之前所有 OpenVLA 实验一致）
- **GPU**: RTX PRO 6000, ~16GB VRAM 占用
- **预计耗时**: 4-5 小时（参考 k=0.7 耗时 ~260min）
- **日志**: `eval_results/openvla_random_prune_k09_object_nohup.log`
- **输出**: `eval_results/openvla_random_prune_k09_object.json`

注意：任务说 seed=42，但之前所有 OpenVLA 数据点（k=1.0/0.7/0.5/0.3）都用的 seed=7，为保持一致性使用了 seed=7。

---
