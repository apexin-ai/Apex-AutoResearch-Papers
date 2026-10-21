# viz fig calibration fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fig_calibration_fix_20260516T214016_result.json`
- **Structured JSON:** [`942145f73b7524d9eff0.json`](../../sessions/94/942145f73b7524d9eff0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**生成结果:**

文件位置: `cqa1-21977:/root/autodl-tmp/artifacts/fig_calibration.{pdf,png}`

**数据 (N=16, 同一批 respondents):**

| Benchmark | Raw MAE | Vanilla 2PL | 2PL+γ |
|-----------|---------|-------------|--------|
| MMLU | 0.0155 | 0.0068 | 0.0072 |
| ARC-C | 0.0338 | 0.0158 | 0.0201 |
| GSM8K | 0.1694 | 0.0063 | 0.0062 |

**图表特征:**
- 三组并排条形图 (灰色=raw, 蓝色=vanilla 2PL, 橙色=2PL+γ)
- 标题: "IRT-Based Calibration vs Raw Scores"
- 每个 bar 顶部有数值标注
- 无 PASS/FAIL 标签、无 D120 注释、无破折号
- 专业学术风格，紧凑布局

**Caption 建议:** Calibration improvement primarily comes from IRT ability estimation framework itself (raw → 2PL). The contamination-aware γ parameter provides diagnostic value for identifying domain-differential effects rather than improving calibration accuracy (vanilla 2PL ≈ 2PL+γ across all benchmarks).

---
