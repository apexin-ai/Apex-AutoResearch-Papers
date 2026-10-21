# check 34685 progress and prep queue

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_34685-progress-and-prep-queue_20260529T101842_result.json`
- **Structured JSON:** [`079671697180c4f631b9.json`](../../sessions/07/079671697180c4f631b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 训练进度

| 实验 | 服务器 | 当前步数 | 进度 | 速度 | 预计剩余 | 预计完成 (UTC) |
|------|--------|----------|------|------|----------|----------------|
| `full_occ_bn_v2_s2_r5` | westd-34685 | 39287/50005 | 78.6% | ~1.02 s/it | ~3h02m | ~14:10 UTC |
| `random_occ_v2_s0_r4` | westd-10894 | 39270/50005 | 78.5% | ~1.02 s/it | ~3h03m | ~14:12 UTC |

两个进程都正常运行（已运行 ~11h10m），GPU 利用率正常（34685: 99%, 10894: 82%）。

### openvla-7b 模型完整性 (westd-10894)

**完整。** Index 引用 3 个 shard，全部存在：
- `model-00001-of-00003.safetensors`: 6.5GB
- `model-00002-of-00003.safetensors`: 6.5GB
- `model-00003-of-00003.safetensors`: 1.1GB

### 磁盘空间

| 服务器 | 总量 | 已用 | 剩余 | 使用率 |
|--------|------|------|------|--------|
| westd-10894 | 250GB | 221GB | **30GB** | 89% |
| westd-34685 | 350GB | 316GB | **35GB** | 91% |

**两台都偏紧张。** 如果下一批实验需要 ~50GB/实验做 checkpoint，需要先清理旧 checkpoint 腾空间。

### 代码就绪状态

**代码不在预期路径，且两台不同步：**
- westd-10894: `/root/occsafe_vla/openvla-oft/` — 有 `random_occ` ✓，无 `bn_eval_mode` ✗
- westd-34685: `/root/openvla-oft/` — 无 `random_occ` ✗，无 `bn_eval_mode` ✗

**下一批实验前需要：**
1. 清理旧 checkpoint 释放磁盘空间
2. 同步代码到两台服务器（统一路径）
3. 如需 `bn_eval_mode` 功能，需先实现

---
