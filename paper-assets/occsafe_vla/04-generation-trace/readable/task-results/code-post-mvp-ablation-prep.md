# code post mvp ablation prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_post_mvp_ablation_prep_20260520T232620_result.json`
- **Structured JSON:** [`82e33a51ef8accef8f83.json`](../../sessions/82/82e33a51ef8accef8f83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇报

### 文件清单

| 配置 | 文件路径 | 状态 |
|------|----------|------|
| +Occ-Detach | `/root/occsafe_vla/scripts/run_occ_detach.sh` | **可直接跑** |
| +Random-Occ | `/root/occsafe_vla/scripts/run_random_occ.sh` | **可直接跑** |
| +Depth | `/root/occsafe_vla/scripts/run_depth.sh` | 占位，需集成到 finetune.py |
| Depth Head 模型 | `openvla-oft/prismatic/models/depth_head.py` | 已完成 |
| Depth 评估 | `/root/occsafe_vla/scripts/depth_head_assessment.md` | — |

### occ_detach 实现方式

`finetune.py:467-468`：在计算 occ loss 时，`patch_features = patch_features.detach()` 切断 `_cached_patch_features` 的梯度图。occ_head 仍正常前向+反向更新自身参数，但梯度不回传到 vision encoder。`--occ_detach true` 已有完整支持，无需改代码。

### depth head 改造评估

- **代码**: depth_head.py 已写好（~55 行）；还需 ~85 行集成代码（finetune.py 配置/初始化/loss 计算 + datasets.py 数据加载）
- **数据**: depth GT labels 不存在，推荐用 Depth Anything V2 生成伪标签，**2-4 小时**
- **总体**: **半天**可完成全部准备

### random_occ 实现方式

方案 A（最小侵入）：
- `FinetuneConfig` 添加 `random_occ: bool = False`（finetune.py:96）
- 传递到 `RLDSBatchTransform`（finetune.py:1045）
- `RLDSBatchTransform` 新增 `random_occ` 字段（datasets.py:44）
- 在 `__call__` 中加载真实 occ label 后，用 `np.random.binomial(1, occ_ratio, shape)` 替换（datasets.py:156），保持与真实 label 相同的 occupied ratio，每次调用生成不同随机 map

---
