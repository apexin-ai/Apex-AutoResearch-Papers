# deploy westd41074 openvla random k09

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_openvla_random_k09_20260525T055357_result.json`
- **Structured JSON:** [`64e84e1b33925c2ddb46.json`](../../sessions/64/64e84e1b33925c2ddb46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westd-41074 探测结果：**

| 项目 | 状态 |
|------|------|
| GPU | 4x ~96GB，全部空闲，无进程 |
| 评估脚本 | ✅ `eval_openvla_l2norm_libero.py` 存在 |
| Goal 模型 | ❌ 不在 westd-41074 |
| Spatial 模型 | ❌ 不在 westd-41074 |
| Object 模型 | ✅ `/root/autodl-tmp/openvla-libero-object` (15GB) |
| Long 模型 | ✅ `/root/autodl-tmp/models/openvla-7b-finetuned-libero-10` (15GB) |
| 磁盘 | **24GB 可用 / 250GB 总** |

**问题：磁盘只剩 24GB，需要 30GB（Goal 15GB + Spatial 15GB）。**

清理候选：
- `pi05_libero_finetuned` (7GB) — pi0.5 模型，当前任务不需要
- `checkpoints/openvla_sc_m64_seed42` (30GB) + `openvla_sc_m96_seed42` (38GB) — 训练 checkpoint

**最小清理方案：删除 `pi05_libero_finetuned` (7GB) → 31GB 可用，刚好够装两个模型。**

可以删 `pi05_libero_finetuned` 吗？确认后立即开始 SCP。

同时，**GPU 2-3 额外实验可选：**
- Object 模型可用 → L2norm k=0.5 Object
- Long 模型可用 → 可跑 Long suite 实验（但需确认 westd-38929 是否已覆盖）

---
