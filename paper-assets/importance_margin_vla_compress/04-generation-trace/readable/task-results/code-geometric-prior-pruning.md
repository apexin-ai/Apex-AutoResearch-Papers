# code geometric prior pruning

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_geometric_prior_pruning_20260517T154301_result.json`
- **Structured JSON:** [`f8982c54a34dd460c1c5.json`](../../sessions/f8/f8982c54a34dd460c1c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 全部通过。总结：

**产出文件**
1. `geometric_prior_pruning.py` (259 行) — Sobel edge detection + token pruning hook
2. `test_geometric_pruning.py` (221 行) — dry-run 验证脚本

**Dry-run 结果** (k_ratio=0.5, task 0: "pick up the alphabet soup and place it in the basket")
- 4 次 re-plan 全部成功，模型未 crash
- 每次 kept=64/128 (50%)，action shape=(50, 7) 正确
- Sobel importance 非 trivial：cam0 mean≈0.21, cam1 mean≈0.25，std≈0.19-0.25
- 合成图像测试通过（白色方块有边缘 → importance max=1.0）

**SigLIP patch-to-token 映射**
| 层 | 尺寸 |
|---|---|
| 原始观测 | 256×256 |
| SigLIP 输入 (resize) | 512×512 |
| SigLIP patches (16×16) | 32×32 = 1024 tokens |
| Connector pixel_shuffle (sf=4) | 8×8 = 64 tokens/camera |
| LIBERO 2 cameras | 128 total tokens |
| 每个 token 覆盖 | 32×32 pixels (原始 256×256 图) |

---
