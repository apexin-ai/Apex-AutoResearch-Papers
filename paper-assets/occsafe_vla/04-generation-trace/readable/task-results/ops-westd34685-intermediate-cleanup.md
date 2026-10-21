# ops westd34685 intermediate cleanup

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd34685_intermediate_cleanup_20260523T141339_result.json`
- **Structured JSON:** [`70da0a046588b2c90c1d.json`](../../sessions/70/70da0a046588b2c90c1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 删除情况
共删除 **8 个中间 checkpoint**，释放 **~120GB**（每个 15GB）。

注：用户指定的路径 `step-XXXXX-checkpoint/` 不存在，实际路径为 `--XXXXX_chkpt` 格式，已按对应关系正确删除。

### 2. 保留的 checkpoint

| 实验 | 保留 |
|------|------|
| reverse_cutoff_s0 | final + 30000_chkpt |
| cutoff_25k_s0 | final + 30000_chkpt |
| vanilla_retrain_s0 | final + 10000_chkpt |
| full_occ_retrain_s0 | final + 10000_chkpt |

### 3. ablation 目录安全
- `ablation_occ_detach_s2/` — SAFE
- `ablation_random_occ_s2/` — SAFE

### 4. 磁盘状态
- 删除前：230G used / 121G avail (66%)
- 删除后：**111G used / 240G avail (32%)**

---
