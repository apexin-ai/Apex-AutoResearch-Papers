# ssh collect gpt2xl temp09 results

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_collect_gpt2xl_temp09_results_20260514T222516_result.json`
- **Structured JSON:** [`430e3be5ce957e271303.json`](../../sessions/43/430e3be5ce957e271303.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已全部更新。

---

## gpt2xl_temp09_001 结果汇总

### Finetune Losses
| Depth | Final Loss |
|-------|-----------|
| 1 | 2.5498 |
| 2 | 1.6972 |
| 3 | 1.2922 |

### Code Contamination
| Depth | Broad | Narrow |
|-------|-------|--------|
| 0 | 0.5% | 0.4% |
| 1 | 0.5% | 0.8% |
| 2 | 0.7% | 1.6% |
| 3 | 0.5% | 1.5% |

### 与 Baseline 对比（RF 指标）

| Metric | GPT-2 XL nucleus (baseline) | GPT-2 XL temp09 | Delta |
|--------|---------------------------|-----------------|-------|
| 4-class acc | 83.3% | **85.42%** | **+2.1pp** |
| 3-class acc | 79.3% | **82.00%** | **+2.7pp** |
| 3-class filtered acc | — | **81.50%** | — |
| d1v2 AUC | 0.913 | **0.9367** | +0.024 |
| d2v3 AUC | 0.883 | 0.8815 | -0.002 |

### 跨模型解码策略衰减对比

| Model | Nucleus → Temp09 | Direction |
|-------|-----------------|-----------|
| Pythia-1.4B | 78.15% → 76.25% | **-1.9pp** |
| GPT-2 XL | 83.3% → 85.42% | **+2.1pp** |

### 关键发现

GPT-2 XL 在 temperature-only τ=0.9 下**反而优于** nucleus p=0.95 baseline，与 Pythia 方向完全相反。解码策略对深度信号的影响是**模型依赖的**，不能简单假设 nucleus 总是最优。d2v3（最难区分的相邻深度）AUC 基本持平，说明信号增强主要来自 d1v2 边界。

### 3×3 矩阵更新建议

GPT-2 XL temp09 格填入 **85.4%**（原假设预期衰减，实际增强），标注为绿色/正向结果。这强化了"深度信号是递归生成的内在属性"的论点——即使解码策略变了，信号依然可检测，甚至在某些模型上更强。

---
