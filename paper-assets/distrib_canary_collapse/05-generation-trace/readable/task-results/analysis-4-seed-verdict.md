# analysis 4 seed verdict

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_4-seed-verdict_20260514T183646_result.json`
- **Structured JSON:** [`e88a124e592f3f3edd35.json`](../../sessions/e8/e88a124e592f3f3edd35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 4-Seed MVP 正式分析 — 完整 Verdict

### 🏆 Overall Verdict: **STRONG PASS**

2 个 canary 家族（**token_entropy**, **ece**）各自对 ≥1 个非降级 downstream 指标有 SIGNIFICANT LEAD。

---

### Pre-Analysis Decisions

- **MAUVE**: demoted（floor_effect，Gen 0 < 0.10 且 CV < 0.50）
- **effective_rank**: inconclusive（Gen 4–9 slopes 方向不一致：seed42=+0.81, seed43=-1.90, seed44=-2.11, seed45=+1.56）

---

### SIGNIFICANT LEAD — 6 对

| Canary | Downstream | Mean Lag | Lag Std | |r| Range | p Range |
|--------|-----------|----------|---------|-----------|---------|
| token_entropy | distinct_1 | **-1.0** | 0.0 | 0.993–0.998 | 0.0006–0.0036 |
| token_entropy | distinct_2 | -1.25 | 0.43 | 0.968–0.999 | 0.0001–0.0231 |
| token_entropy | distinct_3 | -2.25 | 1.64 | 0.941–0.998 | 0.0001–0.0392 |
| ece | distinct_1 | -2.25 | 1.09 | 0.995–0.998 | 0.0000–0.0010 |
| ece | distinct_2 | **-1.0** | 0.0 | 0.995–0.997 | 0.0001–0.0023 |
| ece | distinct_3 | -2.0 | 1.73 | 0.986–0.998 | 0.0002–0.0023 |

最强结果：**token_entropy→distinct_1** 和 **ece→distinct_2**，4/4 seed 完全一致 lag=-1，std=0。

### WEAK LEAD — 1 对

| Canary | Downstream | Mean Lag | Lag Std | |r| Range | p Range |
|--------|-----------|----------|---------|-----------|---------|
| token_entropy | perplexity | **-5.0** | 0.0 | 0.812–0.838 | 0.058–0.120 |

Lag 完全一致（全为-5），但 p 值 borderline——seed 42 p=0.12 不达标。4-seed 趋势表明更多数据可能推至显著。

### NO LEAD — 9 对

- **self_bleu → 所有**: 方向不一致，lag 为正（canary 反而滞后 downstream）
- **ece → perplexity**: lag=+4.75（ECE 滞后 perplexity！）
- **effective_rank**: 全部排除（inconclusive）

---

### 与 2-Seed 预分析对比

| 结论 | 2-Seed | 4-Seed | 变化 |
|------|--------|--------|------|
| Overall verdict | STRONG PASS | STRONG PASS | 确认+加强 |
| token_entropy/ece lead diversity | ✅ | ✅ (所有 p<0.04) | 加强 |
| Canary lead perplexity? | 否（仅 diversity） | 否（仅 diversity） | 不变 |
| distinct_3 lag 收敛? | 高离散 | 仍较高（std~1.6–1.7），seed42 outlier | 轻微改善 |
| effective_rank | Inconclusive | Inconclusive（更差：2+/2-） | 恶化 |
| self_bleu 方向 | 不一致 | 不一致 | 不变 |

### 核心洞察

1. **Canary 只领先 diversity collapse，不领先 perplexity degradation**——多样性丧失和质量下降可能在不同时间尺度上发生
2. **token_entropy 和 ece 双重确认**——两个独立 canary 家族均可靠领先 1-2 代
3. **self_bleu 不是有效 canary**——4 seed 一致确认
4. **effective_rank 在 MVP 设置下不可靠**——方向随 seed 变化

### Rep44 Gen 10 Token Entropy

**1.2205**（已更新至 registry）

---
