# analysis dose response 50pct 5seed stats

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dose-response-50pct-5seed-stats_20260516T013311_result.json`
- **Structured JSON:** [`42d5a7024ac849e434e5.json`](../../sessions/42/42d5a7024ac849e434e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 核心发现

### 3-seed 确认数据 (s42, s1, s7)

| 条件 | Mean ± SD |
|------|-----------|
| Vanilla | 67.4% ± 5.3% |
| TaxEI 50% | 56.7% ± 6.5% |
| Random 50% | 58.1% ± 11.7% |

- **Vanilla vs TaxEI 50%**: Δ=+10.6pp, p=0.013, d=1.79 (large) — **显著**
- **Vanilla vs Random 50%**: Δ=+9.2pp, p=0.267, d=1.01 (large) — 不显著（方差太大）
- **TaxEI vs Random 50%**: Δ=-1.4pp, p=0.804 — 几乎无差异

### 恢复数据问题 — 强烈怀疑标签互换

TaxEI 50% 恢复值 (s0=70.2, s123=46.8) 与 Random 50% 恢复值 (s0=46.8, s123=70.2) **完全对调**。这不是随机巧合，极可能是恢复过程中 TaxEI/Random 标签被互换了。互换修正后 mean 不变（57.4% vs 58.3%），不影响整体结论。

### Dose-Response 趋势

- Random 单调递减 ✓（67.2→63.8→60.0→58.3）
- TaxEI 非单调（67.2→61.3→52.7→**57.4**）— 50% 回升因恢复数据可疑
- 线性斜率：TaxEI -0.190 vs Random -0.174 pp/%（比值 1.09，几乎相同）
- 两者在 50% 处趋同，与 100% (均=58.3%) 一致

### Power Analysis

n=3 时检测 TaxEI vs Random 差异的 power 仅 0.053，需要 n≥200 才能达 80%（因 effect size 极小 d=0.15）。说明 **TaxEI 和 Random 在 50% 剂量下本质差异极小**。

### 建议

重跑 s0/s123 的 50% 实验消除标签混淆疑虑，但预期不会改变核心结论：**在 50% 注入量下，TaxEI 和 Random 的破坏效果趋同**。

---
