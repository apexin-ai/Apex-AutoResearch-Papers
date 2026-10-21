# ssh initial frame gc

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_initial-frame-gc_20260515T191053_result.json`
- **Structured JSON:** [`22da1fdbabf6a0b8a91d.json`](../../sessions/22/22da1fdbabf6a0b8a91d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部完成。汇总如下：

## --max_frames 1 (t=0 Initial Frame Only) Goal Classification 三方对比

| Model | Best Layer | Best Accuracy | Best Macro F1 | n_classes | n_train | n_val |
|-------|-----------|---------------|---------------|-----------|---------|-------|
| **Trained VLA** | 3 | **1.0000** | **1.0000** | 10 | 400 | 100 |
| **Untrained VLA** | 2 | **1.0000** | **1.0000** | 10 | 400 | 100 |
| **DINO-V2** | 0 | **0.1500** | **0.0911** | 10 | 400 | 100 |

### 逐层精度对比（关键层）

| Layer | Trained VLA | Untrained VLA | DINO-V2 |
|-------|------------|---------------|---------|
| 0 | 0.10 | 0.10 | 0.15 |
| 1 | 0.39 | 0.95 | — |
| 2 | 0.58 | **1.00** | — |
| 3 | **1.00** | 0.99 | — |
| 4-18 | **1.00** | 0.98-1.00 | — |
| 19 | **1.00** | 0.91 | — |
| 28 | **1.00** | 0.90 | — |
| 31 | **1.00** | 0.88 | — |
| 32 | **1.00** | 0.98 | — |

### 关键发现

1. **DINO-V2 完全失败（15%≈随机）**：纯视觉特征无法从 t=0 的初始帧区分 10 个 goal task。这验证了 language grounding 假说——DINO 只看图像，不接触语言指令，在初始场景相似的情况下无法判断 goal。

2. **Trained VLA vs Untrained VLA 差距出人意料地小**：两者在 best layer 都达到 100%。关键差异在于：
   - **Trained VLA**：从 Layer 3 开始全部 100%，极其稳定
   - **Untrained VLA**：虽然 best layer=2 达到 100%，但高层（19-31）精度波动剧烈（88%-100%），说明 untrained 的 language grounding 信号在深层不稳定

3. **Untrained VLA 也能做 goal classification**：这说明 Llama backbone 的预训练 language 能力已经足以让 probe 从语言 token 特征区分 task，VLA training 的贡献主要在于让这个信号在所有层都稳定一致。

---
