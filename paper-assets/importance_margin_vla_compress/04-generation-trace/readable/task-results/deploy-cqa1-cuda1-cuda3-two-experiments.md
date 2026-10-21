# deploy cqa1 cuda1 cuda3 two experiments

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-cuda1-cuda3-two-experiments_20260525T211323_result.json`
- **Structured JSON:** [`20038a22a8f347d6e270.json`](../../sessions/20/20038a22a8f347d6e270.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。总结：

| 实验 | GPU | 状态 | 结果 |
|------|-----|------|------|
| eval_pi05_l2norm_k0925_long_seed42_v2 | GPU1 | **DONE** | SR=83.2% (L2norm vs Random 38.6% → scoring method 决定 cliff 位置 ✓) |
| eval_openvla_attn_k09_goal_seed43 | GPU3 | **RUNNING** | 已开始 Task 1/10，预计 ~3.3h 完成 |

注意：实验 2 因 cqa1 缺少 `eval_openvla_l2norm_libero.py` 脚本和依赖，我现场适配了 transformers 5.5.3 版本的 attention pruning hook 并创建了新脚本。核心逻辑与 westd-27271 上的 parent 实验一致。

---
