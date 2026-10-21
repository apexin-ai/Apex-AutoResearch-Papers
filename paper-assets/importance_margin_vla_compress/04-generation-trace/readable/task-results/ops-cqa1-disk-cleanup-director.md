# ops cqa1 disk cleanup director

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1_disk_cleanup_director_20260519T162200_result.json`
- **Structured JSON:** [`7a97d7ff78db0b5318f5.json`](../../sessions/7a/7a97d7ff78db0b5318f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

## 结果汇报

### 磁盘对比
| | 前 | 后 |
|---|---|---|
| 已用 | 250G (100%) | 178G (71%) |
| 可用 | 4.1M | **73G** |
| checkpoints | 112G | 40G |

### 释放 ~72G，来自：
- `baseline_control/` 9个中间step → ~11.7G
- `libero_full_ft/` 9个中间step → ~11.7G
- `libero_full_ft_seed0/` 9个中间step → ~11.7G
- `libero_full_ft_seed1/` 9个中间step → ~11.7G
- `libero_baseline/` 9个中间step → ~7.8G
- `libero_baseline_seed0/` 9个中间step → ~7.8G
- `libero_imm_twostage_fullft_seed0/stage1/` 3个中间step → ~2.7G
- `libero_imm_twostage_fullft_seed0/stage2/` 8个中间step → ~10.7G
- `smart_compress_m16_seed44/`（失败run）→ 218M

每个实验目录均保留了最终 checkpoint（step_099999 或最大 step）和 latest 符号链接。

### 训练状态
- **m128_seed43 (PID 649692)**: ALIVE，运行 1h
- **m16_seed43 (PID 649840)**: ALIVE，运行 1h

### 剩余可清理
HF cache 118G 仍为最大占用项。当前 73G 可用空间足够支撑训练继续。如需更多空间，可考虑清理不再需要的 HF cache 模型。

---
