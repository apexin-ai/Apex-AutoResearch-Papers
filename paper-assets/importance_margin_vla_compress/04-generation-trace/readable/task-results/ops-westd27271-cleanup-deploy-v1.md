# ops westd27271 cleanup deploy v1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd27271_cleanup_deploy_v1_20260522T091519_result.json`
- **Structured JSON:** [`a6a546cc54defb538518.json`](../../sessions/a6/a6a546cc54defb538518.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

发现两个关键问题，暂停部署：

**问题 1：westd-27271 只有 2 个 GPU，不是 4 个**

nvidia-smi 输出：
```
GPU 0: 1 MiB / 97887 MiB, 0% → 空闲
GPU 1: 10564 MiB / 97887 MiB, 32% → PID 212585 (l2norm_k095_object_seed43)
```

只能部署 1 个实验到 GPU 0。

**问题 2：目标实验全部已 DONE/success**

| 实验 | Registry 状态 |
|------|--------------|
| l2norm_k07_object_seed43 | DONE (success) — v2, v3 也 DONE |
| l2norm_k05_object_seed43 | DONE (success) |
| random_k09_object_seed43 | DONE (success) |

备选同样已完成：
- l2norm_k03_object_seed43 → DONE
- random_k0925_object_seed43 → DONE

**当前 RUNNING 实验（registry）：**
- eval_pi05_l2norm_k095_object_seed43（westd-27271 GPU 1）
- eval_pi05_l2norm_k09_object_seed43
- eval_pi05_random_k03_object_seed43_v4
- eval_pi05_random_k05_spatial_seed43
- eval_pi05_l2norm_k0925_spatial_seed43
- 2 个 training jobs

**westd-38929 在跑 4 个实验（无冲突）：**
- l2norm_k05_spatial_seed43
- random_k03_spatial_seed43
- l2norm_k03_spatial_seed43
- random_k03_object_seed43 (v4)

**可能的真实缺口：** `l2norm_k0925_object_seed43` 不在 DONE 也不在 RUNNING 中。需要确认是否需要跑这个？

请指示：GPU 0 应该部署什么实验？

---
