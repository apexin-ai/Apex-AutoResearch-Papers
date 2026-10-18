# diagnose westd41074 l2norm crash

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd41074-l2norm-crash_20260522T002722_result.json`
- **Structured JSON:** [`ddd0be560f3ea9a2335b.json`](../../sessions/dd/ddd0be560f3ea9a2335b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 崩溃原因
lerobot 0.5.1 的 `groot_n1.py` 中 `GR00TN15Config` dataclass 定义不兼容 Python 3.12：`backbone_cfg`/`action_head_cfg`/`action_horizon`/`action_dim` 使用 `field(init=False)` 但没有 `default` 值，导致 `TypeError: non-default argument 'backbone_cfg' follows default argument`。之前的 groot patch 在某次操作中丢失。

### 2. 修复措施
给 `groot_n1.py` 的 4 个字段添加 `default=None`，验证 `from lerobot.policies.factory import make_pre_post_processors` import 通过。

### 3. 重部署
| 实验 | exp_id | GPU | PID (wrapper) | PID (python) |
|------|--------|-----|-------|--------|
| L2norm k=0.85 | `eval_pi05_l2norm_k085_object_seed42_v4` | cuda:0 | 818563 | 818572 |
| L2norm k=0.95 | `eval_pi05_l2norm_k095_object_seed42_v2` | cuda:1 | 818643 | 818652 |

两个实验已进入 eval 阶段，GPU0 10.5GB/43% util，GPU1 10.5GB/30% util。

### 4. M64v6 进度
Step 31050/100000 (**31.1%**，不是 96%)。速度 0.6 sps，剩余 ~69000 steps ≈ **32 小时**。预计完成时间约 5月24日 16:00。

---
