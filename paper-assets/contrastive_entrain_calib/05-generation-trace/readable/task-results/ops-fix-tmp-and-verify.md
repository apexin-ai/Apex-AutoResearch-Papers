# ops fix tmp and verify

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-tmp-and-verify_20260521T044228_result.json`
- **Structured JSON:** [`41e0e7aa101e530f94a3.json`](../../sessions/41/41e0e7aa101e530f94a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部诊断完成。报告如下：

---

### 1. Checkpoint 修复状态：**无需修复**

`_tmp` 目录（6000、6500、7000）均不存在，说明 rename 已经完成（或 SCP 直接写入了主目录）。主目录内容完整。

### 2. 文件完整性验证：**全部通过**

| Checkpoint | 文件数 | 总大小 | adapter_model.safetensors | 状态 |
|------------|--------|--------|--------------------------|------|
| 5000 | 17 | 718M | 245MB | OK |
| 5500 (参考) | 17 | 719M | 245MB | OK |
| 6000 | 17 | 719M | 245MB | OK |
| 6500 | 17 | 719M | 245MB | OK |
| 7000 | 17 | 719M | 245MB | OK |

所有 checkpoint 大小一致（718-719M），文件结构完全相同，关键文件（adapter_model.safetensors ~245MB, optimizer.pt ~491MB）齐全。

### 3. ckpt-5000 eval：**需要重跑**

`results/exp003_d027_eval/` 中没有 `exp003-ckpt5000_*` 文件。已有 eval 的 checkpoint：1000, 2000, 3000, 4000, 4500, 5500。**ckpt-5000 eval 缺失，需要重跑。**

### 4. Seed 2 _tmp 问题：**无问题**

- 无 `_tmp` 目录
- checkpoint-500/1000/1500：250M（无 optimizer，正常——早期 checkpoint）
- checkpoint-2000/2500：718M（完整）

---
