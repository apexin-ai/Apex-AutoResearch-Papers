# ops check progress westd10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_progress_westd10894_20260523T194603_result.json`
- **Structured JSON:** [`d4e48127dfcea8eb2f24.json`](../../sessions/d4/d4e48127dfcea8eb2f24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇总报告：

---

## 训练进度报告 — westd-10894 (2026-05-24)

| 实验 | PID | GPU | Step | 总步 | 进度 | 速度 | 已运行 | 预估剩余 |
|------|-----|-----|------|------|------|------|--------|----------|
| **cutoff_s2_v2** | 435043 | cuda:0 | 19498 | 50005 | **39%** | 1.08 it/s | 5h34m | ~7h50m |
| **detach_ln_s0** | 459087 | cuda:1 | 8698 | 50005 | **17%** | 1.08 it/s | 2h35m | ~10h35m |
| **detach_ln_s1** | 459294 | cuda:2 | 8641 | 50005 | **17%** | 1.08 it/s | 2h35m | ~10h40m |
| **detach_ln_s2** | 459635 | cuda:3 | 8662 | 50005 | **17%** | 1.07 it/s | 2h35m | ~10h42m |

**Loss (step 8600)**:
- detach_ln_s1: occ=0.0116, action=0.1338
- detach_ln_s2: occ=0.0092, action=0.1245

**Checkpoint 保存情况**:
- cutoff_s2_v2: 已保存 10000 步 checkpoint，下一个在 20000 步
- detach_ln 系列: 尚未到 10000 步，无 checkpoint

**GPU**: 4卡均满载 (83-99% util)，各占 ~62GB / 97GB VRAM

**磁盘**: `/root/autodl-tmp` 52GB / 250GB (21%)，空间充足

**预计完成时间**:
- cutoff_s2_v2: ~今天中午 (约 5/24 12:00)
- detach_ln 系列: ~今晚 (约 5/24 15:00)

---
