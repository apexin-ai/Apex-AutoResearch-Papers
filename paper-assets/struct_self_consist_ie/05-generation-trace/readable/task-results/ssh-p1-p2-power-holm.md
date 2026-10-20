# ssh p1 p2 power holm

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p1-p2-power-holm_20260520T132923_result.json`
- **Structured JSON:** [`65088905b038972584f1.json`](../../sessions/65/65088905b038972584f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个产出均已完成，保存在本地和服务器的 `artifacts/r25_response/`：

**P1: `power_analysis.tex`** — n=23 post-hoc power analysis表：
| ρ | Power | n needed (80%) |
|---|-------|----------------|
| 0.1 | 0.073 | 783 |
| 0.2 | 0.148 | 195 |
| 0.3 | 0.283 | 85 |
| 0.4 | 0.474 | 47 |
| 0.5 | 0.690 | 30 |

与论文现有 Table 13 (Appendix F.12) 数值一致（ρ=0.3 → n≈85 匹配论文正文引用）。

**P2: `holm_bonferroni_enumeration.tex`** — 57个统计检验完整枚举，按7个家族分组：
- **Selection** (19 tests): 实例级信号选择 vs greedy
- **Construction** (10 tests): 实体构造 vs greedy
- **Calibration** (3 tests): MF-Platt vs Raw LP
- **Signal Δρ** (9 tests): 信号间 bootstrap 对比
- **Correlation** (6 tests): 跨配置相关性显著性
- **FS error** (4 tests): Few-shot 误差分析
- **Other** (6 tests): 其他独立检验

Holm-Bonferroni 校验结果：仅2个检验在 α=0.05 下存活（#51 CoNLL FS entropy Wilcoxon, #53 RE free-form reversal）。SciERC LP construction 的 p_adj=0.180（论文报告~0.20，差异源于 "p<0.001" 的保守估计）。

---
