# research track bc syncdip mauve analysis

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_track-bc-syncdip-mauve-analysis_20260522T041939_result.json`
- **Structured JSON:** [`80f2c80874ca5d6daab6.json`](../../sessions/80/80f2c80874ca5d6daab6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果总结

### Part B: Sync-Dip 假说 — **被否决**

- **所有实验**（无论 α 值）的 distinct_1/distinct_2 peak_lag 均为 -1，α=0.60 无任何特殊性
- 根因：token_entropy（canary）是**阶跃函数**行为——从 gen 0→1 瞬间下降（τ≈0.1），之后保持平坦。不存在渐进同步化
- Mann-Whitney p=1.0，零假设不可拒绝
- **α=0.60 的 PermG=0/8 需要其他解释**，不是时间尺度同步化

### Part C: MAUVE 方差分析 — **Floor Effect 确认**

| 指标 | Mean CV | Mean SNR | Near-floor% |
|------|---------|----------|-------------|
| MAUVE | 0.089 | 4.68 | **100%** |
| distinct_1 | 0.139 | 6.40 | 0% |
| distinct_2 | 0.197 | 8.20 | 0% |

- **高方差假说被反转**：MAUVE 的 CV 反而最低（p≈1.0 for MAUVE > diversity）
- **真正原因是 floor effect**：MAUVE 均值仅 0.029，100% 观测值 < 0.05。分布一旦偏离参考（gen 1+），MAUVE 就饱和在 ~0.03，没有时间梯度可供 Granger 检出
- SNR 显著低于 diversity metrics（p=0.0002）
- ACF1 也更低（0.55 vs 0.68/0.71），时间持续性更差

### 输出文件（westd-17855）

- `artifacts/syncdip_mechanism_analysis.pdf` — lag vs α 图 + decay rate 对比
- `artifacts/mauve_variance_analysis.pdf` — CV 对比 + SNR + floor effect
- `artifacts/syncdip_mechanism_summary.json`
- `artifacts/mauve_variance_summary.json`

---
