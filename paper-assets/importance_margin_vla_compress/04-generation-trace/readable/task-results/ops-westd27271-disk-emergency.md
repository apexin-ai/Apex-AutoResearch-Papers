# ops westd27271 disk emergency

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd27271_disk_emergency_20260520T003134_result.json`
- **Structured JSON:** [`2d24f5a6087ef14e6b94.json`](../../sessions/2d/2d24f5a6087ef14e6b94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

## 结果汇总

| 项目 | 释放量 |
|------|--------|
| **清理前** | **6GB 可用 (98%)** |
| imm_anchor_v8 中间步骤 (14 steps) | ~16.8GB |
| imm_anchor_v8_1 中间步骤 (14 steps) | ~16.8GB |
| imm_anchor_v8c_annealing 中间步骤 (14 steps) | ~16.8GB |
| imm_anchor_v8b_twostage stage1+stage2 | ~16.5GB |
| libero_imm_twostage_fullft stage1+stage2 | ~18.6GB |
| HF datasets/parquet 旧缓存 | ~0 (硬链接,无实际释放) |
| conda/pip/HF model 缓存 | ~3.5GB |
| **清理后** | **91GB 可用 (64%)** |
| **总计释放** | **~85GB** |

- 所有旧实验只保留了 final/latest checkpoint，不影响结果复现
- `openvla_sc_m128_seed42` (VTC+LoRA) 未触碰
- GPU 0 训练进程 (PID 841334) 未受影响
- **不需要 kill M=32 (PID 855140)**

---
