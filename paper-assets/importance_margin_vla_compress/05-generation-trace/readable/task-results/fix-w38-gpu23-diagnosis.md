# fix w38 gpu23 diagnosis

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_w38-gpu23-diagnosis_20260527T231558_result.json`
- **Structured JSON:** [`14f59178a4a46240b7ae.json`](../../sessions/14/14f59178a4a46240b7ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**4 GPU 全部就位。**

## 诊断结果

**根因**：PID 691997 (L2norm) 和 PID 677625 (Attn) 启动时**未设置 CUDA_VISIBLE_DEVICES**，导致 `--gpu 0` 映射到物理 GPU 0，三个进程挤在同一块卡上，GPU 2/3 闲置。

## 修复动作

1. Kill 了错误进程 PID 691997、677625
2. 用正确的 CUDA_VISIBLE_DEVICES 重启：
   - **GPU 2** → L2norm k=0.85 s44，新 PID **773760**，显存 10701MiB ✓
   - **GPU 3** → Attn k=0.5 s44，新 PID **774388**，显存 10277MiB ✓

## 当前 GPU 分布

| GPU | 显存 | 进程 | 实验 |
|-----|------|------|------|
| 0 | 11045MiB | 672324 | Attn k=0.85 s44 |
| 1 | 10719MiB | 672401 | Random k=0.7 s44 |
| 2 | 10701MiB | 773760 | **L2norm k=0.85 s44** (新) |
| 3 | 10277MiB | 774388 | **Attn k=0.5 s44** (新) |

GPU 0 显存已从 32GB 降回 ~11GB。4 卡满载运行正常。

---
