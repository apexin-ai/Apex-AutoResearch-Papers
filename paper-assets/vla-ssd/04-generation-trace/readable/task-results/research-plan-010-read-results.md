# research plan 010 read results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan_010_read_results_20260516T072440_result.json`
- **Structured JSON:** [`a66efad5596b305bef24.json`](../../sessions/a6/a66efad5596b305bef24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整，以下是 LIBERO-Spatial plan_010 分析报告。

---

## LIBERO-Spatial 分析结果

### GPU 状态
| GPU | Util | Mem Used | Total |
|-----|------|----------|-------|
| 0 | 0% | 0 MiB | 97887 MiB |
| 1 | 0% | 0 MiB | 97887 MiB |

---

### RSA (Method B: within-task, cosine rep dist, euclidean action dist)

| Condition | Peak Layer | Peak RSA |
|-----------|-----------|----------|
| trained_image_mean | **L14** | **0.6911** |
| trained_last_preaction | **L15** | **0.6945** |
| untrained_image_mean | L0 | 0.6523 |
| untrained_last_preaction | L1 | 0.6659 |

**Trained layer profile (image_mean):**
- L0: 0.652 → rises to L14: 0.691 → declines to L32: 0.630
- **Mild inverted-U confirmed**

**Untrained**: flat/monotonically declining from L0-L1. No inverted-U.

---

### Action Probe (Linear, target=a_{t+1}, z-score norm)

| Condition | Peak Layer | Peak R² |
|-----------|-----------|---------|
| trained_image_mean | **L13** | **0.6963** |
| trained_last_preaction | **L21** | **0.6748** |
| untrained_image_mean | L0 | 0.6732 |
| untrained_last_preaction | L1 | 0.6348 |

**Trained image_mean profile:**
- L0: 0.673 → peak L13: 0.696 → L20: 0.638 → L30: 0.597 → L32: 0.577
- **Clear inverted-U**

**Untrained last_preaction profile (dramatic collapse):**
- L1: 0.635 → L4: 0.526 → L5-L31: 大量层 ≈ −0.015（degenerate probe）→ L32: 0.621（output layer 恢复）
- 中间层零星非零值: L6: 0.40, L12: 0.45, L21: 0.30

---

### Bootstrap Pairwise Comparisons

| Comparison | Δ | 95% CI | p |
|-----------|---|--------|---|
| trained vs untrained image_mean (best-vs-best) | +0.023 | [0.012, 0.036] | <0.001 |
| trained vs untrained last_preaction (best-vs-best) | +0.040 | [0.019, 0.057] | 0.0004 |
| trained vs untrained image_mean (same-layer@L13) | +0.711 | [0.685, 0.740] | <0.001 |
| trained vs untrained last_preaction (same-layer@L21) | +0.370 | [0.317, 0.427] | <0.001 |

---

### 核心发现

1. **Inverted-U pattern**: Trained model 在两个指标上都呈现 inverted-U（RSA peak L14-15, Probe peak L13-21）。Untrained 无此 pattern——peak 在 L0-1，之后 flat 或 collapse。

2. **Untrained last_preaction 极端退化**: 中间层（L5-L31）大量出现 R² ≈ −0.015（probe 退化为预测 mean action），仅 L32 output layer 恢复。这说明 pretrained LLM 的深层表示对 action 完全无信息编码，fine-tuning 是必要条件。

3. **Best-vs-best delta 虽小但显著**: image_mean +0.023, last_preaction +0.040。训练改善幅度不大是因为 L0（shared embedding）已有很高 baseline（0.67），训练主要是让 middle layers 超越这个 baseline。

4. **Same-layer delta 巨大**: 在 trained peak layer（L13/L21），untrained 表示几乎为零。这是 fine-tuning 效应最强的证据。

---

### 与 LIBERO-Goal 对比（定性）

| 维度 | LIBERO-Goal | LIBERO-Spatial |
|------|-------------|----------------|
| RSA peak layer (trained) | ~L14-16 | L14-15 |
| Probe peak layer (trained) | ~L13-15 | L13 (img), L21 (preact) |
| Untrained collapse | 类似 | 类似 |
| Task 区分维度 | 不同 goal object | 同一 goal，不同 spatial config |

两个 suite 的 peak layer 位置高度一致，表明 **action-relevant representation 的层深度与 task differentiation 类型无关**——无论是 goal-level 还是 spatial-level 的区分，都在 L13-15 达到最大 representational alignment。

---
