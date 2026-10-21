# ops goal long data check other servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_goal_long_data_check_other_servers_20260522T093108_result.json`
- **Structured JSON:** [`7eaa8a0bc06bc206caf1.json`](../../sessions/7e/7eaa8a0bc06bc206caf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三台服务器数据完备。汇总：

| 服务器 | Goal bddl_files | Goal init_files | Long (libero_10) bddl_files | Long init_files | eval 脚本 |
|--------|-----------------|-----------------|----------------------------|-----------------|----------|
| westd-27271 | ✅ `site-packages/libero/libero/bddl_files/libero_goal/` | ✅ `site-packages/libero/libero/init_files/libero_goal/` | ✅ `bddl_files/libero_10/` | ✅ `init_files/libero_10/` | ✅ |
| westd-41074 | ✅ 同上 | ✅ 同上 | ✅ 同上 | ✅ 同上 | ✅ |
| westd-38929 | ✅ `libero_repo/LIBERO-master/.../bddl_files/libero_goal/` | ✅ `.../init_files/libero_goal/` | ✅ `bddl_files/libero_10/` | ✅ `init_files/libero_10/` | ✅ |

**结论：三台服务器均可直接跑 Goal 和 Long (libero_10) eval。**

关键细节：
- eval 脚本 SUITE_CONFIG 中 Long 对应的 key 是 `libero_10`（不是 `libero_long`），max_steps=520
- LIBERO 数据通过 `~/.libero/config.yaml` 定位 bddl_files 和 init_files，三台都已正确配置
- 27271/41074 的 LIBERO 库装在 `site-packages`，38929 的指向 `libero_repo/LIBERO-master/` 源码
- HDF5 训练数据（`libero_data/datasets/`）只有 libero_object suite，但 eval **不需要** HDF5——只需 bddl + init_files + MuJoCo assets，这些都齐全

---
