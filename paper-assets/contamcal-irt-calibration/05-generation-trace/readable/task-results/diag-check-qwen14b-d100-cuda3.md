# diag check qwen14b d100 cuda3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_check-qwen14b-d100-cuda3_20260521T023451_result.json`
- **Structured JSON:** [`f9d7532555fe8848d579.json`](../../sessions/f9/f9d7532555fe8848d579.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**d100_s0 (PID 311554)**: 训练完成，进程已退出。

**Qwen-14B s0 全部 adapter 完整性**:

| Dosage | Adapter 大小 | .done | 状态 |
|--------|-------------|-------|------|
| d000 | 263M | ✓ | 完成 (May 20 20:38) |
| d005 | 263M | ✓ | 完成 (May 21 00:09) |
| d025 | 263M | ✓ | 完成 (May 21 03:45) |
| **d050** | **空目录** | **✗** | **失败 — 47% (1726/3642 steps) 处被 kill，无 error trace** |
| d100 | 263M | ✓ | 完成 (May 21 09:42) |

所有完成的 adapter 配置一致：lora_alpha=32, lr=5e-5, lora_r=16。

**d050_s0 需要重训。** cuda:3 当前空闲可立即使用。d000/d005/d025/d100 四个 dosage 可以先启动 eval。

---
