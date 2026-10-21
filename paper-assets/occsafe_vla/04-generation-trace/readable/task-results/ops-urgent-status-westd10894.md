# ops urgent status westd10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_status_westd10894_20260523T195036_result.json`
- **Structured JSON:** [`2930a7f124ab1ab2fd54.json`](../../sessions/29/2930a7f124ab1ab2fd54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度汇总

| 实验 | GPU | 当前 Step | 总步数 | 进度 | 速度 | 剩余时间 | 预估完成 |
|------|-----|----------|--------|------|------|---------|---------|
| **cutoff_s2_v2** | cuda:0 (80%) | 19,760 | 50,005 | **39.5%** | 1.08 it/s | ~7h48m | ~5/24 17:30 |
| **detach_ln_s0** | cuda:1 (99%) | 8,960 | 50,005 | **17.9%** | 1.08 it/s | ~10h29m | ~5/24 20:10 |
| **detach_ln_s1** | cuda:2 (99%) | 8,900 | 50,005 | **17.8%** | 1.08 it/s | ~10h36m | ~5/24 20:15 |
| **detach_ln_s2** | cuda:3 (99%) | 8,920 | 50,005 | **17.8%** | 1.08 it/s | ~10h34m | ~5/24 20:15 |

**最新 loss**:
- cutoff_s2_v2 @ step 19700: occ=0.0106, action=0.0977
- detach_ln_s0 @ step 8900: occ=0.0094, action=0.1182
- detach_ln_s2 @ step 8900: occ=0.0094, action=0.1108

**Checkpoint**: cutoff_s2_v2 已保存 10000 步 checkpoint，其余 3 个尚未到达首个存档点。

**磁盘**: /root/autodl-tmp 250G，已用 52G (21%)，空间充裕。

**所有 4 个进程运行正常。**

---
