# infra westd34685 fix occ index and restart

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd34685_fix_occ_index_and_restart_20260520T163335_result.json`
- **Structured JSON:** [`d6758eadc7698c5bec87.json`](../../sessions/d6/d6758eadc7698c5bec87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

---

## 产出报告

| # | 项目 | 结果 |
|---|------|------|
| 1 | occ_index.json 重建 | **tasks=9, total_demos=450**，格式 `{"demos": {demo_key: int_traj_len}, "file": path}` |
| 2 | 数据加载验证 | shape=(64,64), sum=1520, nonzero=1520 — **非零确认** |
| 3 | datasets.py 兼容性 | 读 `task_info["demos"]` + `task_info["file"]`，与新 index **完全匹配** |
| 4 | 磁盘空间 | /root/autodl-tmp/ **329GB 可用**（7% used），充足 |
| 5 | 新 PID | **occ_s0**: 27667 (GPU 0, seed 42) / **occ_s1**: 28827 (GPU 1, seed 43) / **occ_s2**: 29970 (GPU 2, seed 44) |
| 6 | GPU 使用 | GPU 0: 62203 MiB, 99% / GPU 1: 62203 MiB, 99% / GPU 2: 62209 MiB, 43% |
| 7 | 日志验证 | "Failed to load occ label" 计数：**三个均为 0** |
| 8 | occ_loss 初始值 | s0=**0.0987**, s1=**0.1764**, s2=**0.1413** — 在预期范围 0.1~0.3 内，**正常** |

无未解决问题。

---
