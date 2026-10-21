# check bootstrap v3 final results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_v3_final_results_20260523T110944_result.json`
- **Structured JSON:** [`da9b65fac17aaa569551.json`](../../sessions/da/da9b65fac17aaa569551.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### 1. 完成状态：17/20

| GPU | 分配 | 完成 | 状态 |
|-----|------|------|------|
| cuda:0 | openvla×4 + nora×2 = 12 | 12/12 | **全部完成** |
| cuda:1 | tracvla×4 = 8 | 5/8 | 正在跑 tracvla_object/untrained (RidgeCV fitting, 19:08起) |

**缺失**: tracvla_object/untrained (进行中) → tracvla_long/trained → tracvla_long/untrained

### 2. 已完成 17 条结果

| arch_suite | cond | peak_layer | peak_r2 | exit_r2 | delta | CI_95 | boot_mean | boot_std | boot-delta | sig | delta∈CI | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nora_goal | trained | L8 | 0.4489 | -0.0062 | 0.4551 | [0.91, 1.61] | 1.2155 | 0.1786 | +0.7604 | YES | NO | 100 |
| nora_goal | untrained | L5 | 0.4203 | 0.3397 | 0.0806 | [-0.01, 0.11] | 0.0454 | 0.0313 | -0.0352 | NO | YES | 100 |
| nora_spatial | trained | L20 | 0.5763 | 0.2683 | 0.3080 | [0.30, 0.51] | 0.3926 | 0.0532 | +0.0846 | YES | YES | 100 |
| nora_spatial | untrained | L4 | 0.5125 | 0.4240 | 0.0885 | [-0.01, 0.09] | 0.0423 | 0.0277 | -0.0462 | NO | YES | 100 |
| openvla_goal | trained | L1 | 0.4177 | 0.3313 | 0.0864 | [-0.06, 0.11] | 0.0173 | 0.0414 | -0.0691 | NO | YES | 100 |
| openvla_goal | untrained | L27 | 0.4230 | 0.3672 | 0.0558 | [0.01, 0.08] | 0.0396 | 0.0166 | -0.0162 | YES | YES | 100 |
| openvla_long | trained | L23 | 0.5328 | 0.5003 | 0.0325 | [0.00, 0.10] | 0.0484 | 0.0259 | +0.0159 | YES | YES | 100 |
| openvla_long | untrained | L29 | 0.5316 | 0.4968 | 0.0349 | [0.03, 0.10] | 0.0597 | 0.0202 | +0.0248 | YES | YES | 100 |
| openvla_object | trained | L3 | 0.5695 | 0.5325 | 0.0370 | [-0.00, 0.09] | 0.0413 | 0.0226 | +0.0043 | NO | YES | 100 |
| openvla_object | untrained | L3 | 0.5619 | 0.5105 | 0.0513 | [-0.00, 0.09] | 0.0417 | 0.0250 | -0.0096 | NO | YES | 100 |
| openvla_spatial | trained | L24 | 0.5649 | 0.5278 | 0.0371 | [0.01, 0.10] | 0.0508 | 0.0233 | +0.0137 | YES | YES | 100 |
| openvla_spatial | untrained | L28 | 0.5391 | 0.4955 | 0.0437 | [0.03, 0.11] | 0.0666 | 0.0209 | +0.0229 | YES | YES | 100 |
| tracvla_goal | trained | L13 | 0.5399 | 0.2065 | 0.3334 | [0.21, 0.45] | 0.3155 | 0.0642 | -0.0179 | YES | YES | 100 |
| tracvla_goal | untrained | L11 | 0.5048 | 0.4403 | 0.0645 | [-0.11, 0.05] | -0.0232 | 0.0407 | -0.0877 | NO | NO | 100 |
| tracvla_object | trained | L13 | 0.6315 | 0.2692 | 0.3623 | [0.28, 0.50] | 0.3788 | 0.0582 | +0.0165 | YES | YES | 100 |
| tracvla_spatial | trained | L13 | 0.6871 | 0.5315 | 0.1557 | [0.09, 0.22] | 0.1539 | 0.0333 | -0.0018 | YES | YES | 100 |
| tracvla_spatial | untrained | L4 | 0.6120 | 0.5643 | 0.0477 | [-0.61, -0.46] | -0.5427 | 0.0357 | -0.5904 | YES | NO | 100 |

### 3. cuda:1 进程

PID 734751, python3, 682 MiB 显存 — 就是 bootstrap_v3_cuda1 的 tracvla_object/untrained 任务。当前 0% GPU 利用率因为 RidgeCV fitting 是 CPU 密集型，bootstrap 阶段才上 GPU。进程正常运行中。

### 4. 预计剩余时间

从 cuda:1 历史看，每个条件约 60-80 分钟（tracvla 模型较大）。当前条件 19:08 开始 RidgeCV，预计 ~19:50 完成。之后还有 tracvla_long 的 trained + untrained 两条，预计全部完成约 **21:30-22:00 CST**。

---
