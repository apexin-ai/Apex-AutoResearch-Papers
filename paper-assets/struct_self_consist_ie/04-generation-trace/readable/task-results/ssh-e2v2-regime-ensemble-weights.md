# ssh e2v2 regime ensemble weights

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_e2v2-regime-ensemble-weights_20260520T105540_result.json`
- **Structured JSON:** [`bf0ddecc267b795b9c4f.json`](../../sessions/bf/bf0ddecc267b795b9c4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 artifacts registered. E2v2 experiment complete.

## E2v2 结果

**10 FT configs, 201,960 instances, 1001 simplex weight candidates (step=0.1), 5-fold CV**

### 核心发现

| 分组 | 最优权重 | F1 | vs Best Single |
|------|---------|-----|----------------|
| **FT (all)** | LP=0.9, VC=0.1 | 0.7807 | +0.30pp (p=0.000) |
| LLaMA-8B | LP=1.0 | 0.7877 | +0.00pp (LP alone最优) |
| Qwen3-8B | LP=0.8, VC=0.2 | 0.7745 | +0.64pp (p=0.000) |

### 关键结论

1. **LP 主导**：所有分组中 LP 权重 >= 0.8，SJ/FK/EM 始终为 0。VC 是唯一有贡献的辅助信号。

2. **模型差异**：LLaMA-8B 完全依赖 LP（权重 1.0），Qwen3-8B 需要 VC 辅助（0.2），说明 Qwen3 的 log-prob 校准不如 LLaMA，需要 voting consistency 来补偿。

3. **LOO 完全稳定**：10 次 LOO 中权重完全不变（全部 LP=0.9, VC=0.1），delta=0.00pp。权重不受单个 config 影响。

4. **Regime vs Cross-config**：由于只有 FT 数据，regime weights = cross-config weights，无差异。

5. **ZS/FS 对比不可行**：72B 零样本/少样本推理数据已从服务器清除。假设"LP weight FT > ZS"无法验证。

### vs E2 (原始实验，7 config, step=0.2)

- E2 cross-config: best weights VC=0.2, LP=0.8 → F1=0.7754
- E2v2 (10 config, step=0.1): best weights VC=0.1, LP=0.9 → F1=0.7807
- 扩展到 10 config + 更细粒度搜索后，LP 权重从 0.8 上升到 0.9，F1 提升 +0.53pp

---
