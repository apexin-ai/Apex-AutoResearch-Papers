# analysis exp 023

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_023_20260524T172011_result.json`
- **Structured JSON:** [`566c64997e92c1687ed3.json`](../../sessions/56/566c64997e92c1687ed3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结论: SUCCESS — Type II confirmed

**GPT-2-medium r=0.25 展现 Type II (transitional) trajectory：**

| Gen | SLV | ΔSLV | Eff. Rank | PPL |
|-----|-----|------|-----------|-----|
| 0 | 689.44 | — | 23.09 | 15.45 |
| 1 | 748.06 | +58.62 (decompression) | 142.37 | 12.09 |
| 2 | 734.21 | **-13.85 (dip)** | 143.51 | 12.05 |
| 3 | 737.91 | **+3.70 (recovery)** | 149.42 | 12.07 |

Raw SLV 在 Gen 1→2 下降 1.85%，Gen 2→3 恢复 0.50%，符合 Type II 特征（transient dip + recovery）。

与 Pythia-410M r=0.25 定性一致——两种架构在 r=0.25 均未出现单调 collapse，支持 **r_crit ∈ (0.25, 0.3] 是架构无关的**。

注意事项：
- GPT-2-medium 初始谱极度集中（eff_rank=23 vs Pythia=417），decompression transient 更剧烈
- 仅 3 代无法确认持续恢复，建议扩展至 10 代
- 单 seed，需 cross-seed 验证

报告已注册: `artifacts/exp_023/analysis_report.md`

---
