# debug verify model consistency

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_verify_model_consistency_20260518T135624_result.json`
- **Structured JSON:** [`f9436bb67449d5a4a573.json`](../../sessions/f9/f9436bb67449d5a4a573.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**三个脚本完全一致：**

| 脚本 | MODEL_PATH | UNNORM_KEY |
|---|---|---|
| `action_trajectory_analysis.py` (L1) | `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b` | `bridge_orig` |
| `action_trajectory_L8_ablation.py` (L8) | `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b` | `bridge_orig` |
| `action_trajectory_L13_ablation.py` (L13) | `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b` | `bridge_orig` |

三个脚本都指向同一个模型路径 `openvla-7b`，使用相同的 `unnorm_key = "bridge_orig"`。

关于 L13 worker 之前报告的 norm_stats 没有 `bridge_orig` key 的问题：从脚本代码看，L13 **并没有**改用 base model，它的配置和 L1、L8 完全相同。那个问题可能已经被解决了，或者是运行时才出错（脚本配置本身没改）。建议确认 L13 的实际运行日志，看它是否成功加载了模型并完成了推理。

---
