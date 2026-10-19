# ops check remaining trains

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_remaining_trains_20260523T055519_result.json`
- **Structured JSON:** [`5f1fe2ec33b7ec759575.json`](../../sessions/5f/5f1fe2ec33b7ec759575.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| exp_id | server | gpu | status | last_step | notes |
|--------|--------|-----|--------|-----------|-------|
| s2_l01 | westd-35807 | cuda:3 | **DEAD** | 7999 | 磁盘满 (350G/350G=100%)，step 8000 存 checkpoint 时 `No space left on device` |
| s0_l005 | westd-45947 | cuda:0 | **ALIVE** | ~8067 (27%) | 正常，~4.62s/it，ETA ~28h |
| s0_l01 | westd-45947 | cuda:1 | **ALIVE** | ~8070 (27%) | 正常，~4.62s/it，ETA ~28h |

**westd-35807 全部 4 卡空闲**，磁盘 100% 满是所有训练崩溃的共同原因。重启前必须先清理磁盘。

**westd-45947 两个训练健康**，磁盘 71% (75G free)，但需关注后续 checkpoint 是否会撑满。

报告已写入 `artifacts/remaining_train_status.md`。

---
