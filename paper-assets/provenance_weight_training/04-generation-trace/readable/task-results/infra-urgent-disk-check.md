# infra urgent disk check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_urgent-disk-check_20260513T232333_result.json`
- **Structured JSON:** [`bbf51c9ff5cde7061a53.json`](../../sessions/bb/bbf51c9ff5cde7061a53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. Output 目录位置：**安全，在数据盘**
`/root/provenance_weight_training/output` → symlink → `/root/autodl-tmp/provenance_weight_training/output`

### 2. 磁盘使用

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 根分区 `/` | 30G | 13G | 18G | 41% |
| 数据盘 `/root/autodl-tmp` | 250G | 26G | 225G | 11% |

**无磁盘满风险。** 数据盘还剩 225G，即使每个 seed 再存一个 checkpoint-1000（3.4G × 3 = ~10G），也完全够用。

### 3. Checkpoint 大小

| Seed | Checkpoint | 大小 |
|------|-----------|------|
| seed42 | checkpoint-500 | 3.4G |
| seed123 | checkpoint-500 | 3.4G |
| seed456 | checkpoint-500 | 3.4G |

### 4. 训练进度

| Seed | 当前 Step | 距 1000 还剩 | 进度 |
|------|----------|-------------|------|
| seed42 | 589 | 411 | 59% |
| seed123 | 587 | 413 | 59% |
| seed456 | 582 | 418 | 58% |

GPU 状态：仅 GPU 1 在工作（99% 利用率，44GB 显存占用），其余 GPU 空闲。

---
