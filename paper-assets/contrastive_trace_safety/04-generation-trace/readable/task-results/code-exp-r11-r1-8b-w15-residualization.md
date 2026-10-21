# code exp r11 r1 8b w15 residualization

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_r11_r1_8b_w15_residualization_20260518T123644_result.json`
- **Structured JSON:** [`34aa37ed501ed5f3bdcb.json`](../../sessions/34/34aa37ed501ed5f3bdcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## E-R11-2 结果：R1-8B W=15 Position Residualization

### W=3 vs W=15 对比 (R1-8B, L14)

| Metric | W=3 | W=15 |
|---|---|---|
| Original HS BA | 0.813 | **0.834** |
| Residualized HS BA | 0.571 | **0.669** |
| Drop (pp) | 24.3 | **16.5** |
| Position-only BA | 0.706 | **0.706** |
| Original Text BA | — | 0.757 |
| Residualized Text BA | — | 0.605 |

### 统计检验 (W=15 residualized)
- Binomial test vs chance: p < 1e-6
- Wilcoxon signed-rank vs 0.5: p < 1e-6
- Per-trace BA 分布: 43 traces, mean ≈ 0.78, min=0.30, max=0.95

### 关键发现

1. **W=15 下 residualization drop 显著更小** (16.5pp vs 24.3pp)，说明 W=3 的 drop 部分来自 small window 的 position confound 更强。
2. **Residualized HS 仍远超 chance** (0.669 vs 0.5, p ≈ 0)，确认 hidden states 包含真正的 safety-relevant 信号而非仅仅是 positional artifact。
3. **Position-only BA 完全相同** (0.706)，因为 position-only 不受 window 影响（n_pca=1, 无 windowing）。
4. **Original HS BA 从 0.813 升至 0.834**，更大窗口提供了更多上下文，略微提高分类性能。

---
