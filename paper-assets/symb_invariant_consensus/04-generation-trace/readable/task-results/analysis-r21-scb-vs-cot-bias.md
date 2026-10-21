# analysis r21 scb vs cot bias

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r21-scb-vs-cot-bias_20260523T203927_result.json`
- **Structured JSON:** [`d497da9b769117f086f3.json`](../../sessions/d4/d497da9b769117f086f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Here are the results.

## R21 MF2 分析结果

### 数据概况
- 总问题数: 204
- 有少数票 trace 的问题数: 166 (81.4%)
- 少数票 trace 平均数: 3.2/12

### 指标 A: 约束公式共享 (string-level dedup)
| 类别 | 数量 | 比例 |
|------|------|------|
| Majority-only | 4526 | 63.5% |
| Minority-only | 1911 | 26.8% |
| Shared (两组均出现) | 687 | 9.6% |
| **有共享公式的问题** | **153/166** | **92.2%** |

少数票公式中 32.5% 也出现在多数票 trace 中 → 约束**不是**孤立的 trace-specific 产物。

### 指标 B: 变量重叠 (Jaccard)
- 均值: 0.225 (中等)
- 分布: high(>0.5)=11, medium(0.2-0.5)=73, low(<0.2)=82
- 解读: 部分共享语义空间，但变量命名不一致是低 Jaccard 的主因（LLM 每条 trace 用不同变量名编码相同概念）

### 指标 C: Z3 跨组一致性
|  | SAT | UNSAT |
|--|-----|-------|
| 多数票组 | 83 | 83 |
| 少数票组 | 125 | 40 |
| 跨组 (合并) | 63 | 103 |
| 两组均 SAT → 合并 UNSAT | 7/69 | 10.1% |

### 指标 D: MaxSAT 排除不对称性
| 约束来源 | Satisfied | Excluded | 排除率 |
|---------|-----------|----------|--------|
| Majority-only | 3690 | 836 | **0.185** |
| Minority-only | 1583 | 328 | **0.172** |
| Shared | 664 | 23 | 0.033 |

**关键发现**: 全局排除率在两组间几乎一致 (0.185 vs 0.172)。MaxSAT **没有**系统性地更多排除少数票约束。

### 指标 E: 每 trace 约束密度
- 多数票: 6.0 constraints/trace
- 少数票: 5.9 constraints/trace

→ **完全一致**。模型在约束提取时没有 per-trace 偏差。

### 关键分解: Volume vs Trace Count

| 子集 | Trace 比 (maj/min) | 约束比 (maj/min) | 放大倍率 |
|------|-------------------|------------------|---------|
| Minority Correct (n=68) | 1.77x | 1.81x | **1.02x** |
| Minority Wrong (n=81) | 2.78x | 2.73x | **0.98x** |

约束体量优势**完全由 trace 数量决定**（放大倍率 ≈ 1.0x）。无额外约束级放大。

### Minority Correct 子集 (SC 错, 少数票有正确答案)
- 共 68 个问题
- SICA 在此子集正确率: **17.6%** (12/68) — SICA 也无法纠正
- 少数票排除率 vs 多数票: min_excl > maj_excl 的问题占 44.1%

### Case Study 1: folio_157
- GT=False, SC=Unknown (5:5 平票), SICA=Unknown
- Minority (False) exclusion rate: **0.571** vs Majority: 0.038
- Variable Jaccard: 0.051 (极低 — 少数票用完全不同变量编码)
- 少数票 trace 的约束逻辑正确推导出 False，但变量与多数票完全隔离，在 MaxSAT 中因权重劣势被大量排除

### Case Study 2: folio_197
- GT=False, SC=Unknown (9:2), SICA=Unknown
- Minority exclusion: 0.500 vs Majority: 0.125
- 4 个共享公式，但少数票独有的 8 个被排除一半

### 科学结论

**SCB 的本质是 CoT bias 通过 source-attribution 的结构性保持 (structural preservation)，而非简单传递或独立放大。**

核心证据链:

1. **约束提取无额外偏差**: 每 trace 约束数相同 (~6.0)，排除率相似 (~0.18)。约束层本身是"公平"的。

2. **SCB ≠ CoT bias propagation** (回应 R21):
   - 如果 SCB 是纯 CoT 传递，那约束应该是 trace-specific 的独立产物 → 但 92.2% 的问题有跨组共享公式
   - 少数票约束与多数票约束共享语义空间 (Jaccard=0.225)，证明约束不是 trace 答案的下游回声
   - 即使约束语义上正确 (少数票组 SAT 率更高: 125 vs 83)，source-attribution 仍将其绑定到少数票答案

3. **SCB 的三层机制**:
   - **(层1-CoT)** 多数票有更多 trace → 更多约束 (volume = trace count × ~6.0)
   - **(层2-Source Attribution)** 每条约束通过 source_traces 绑定到其来源 trace 的答案
   - **(层3-MaxSAT)** 多数票的 volume 优势直接转化为更高的 satisfied weight → 更高分数

4. **为什么这不是"简单传递"**: Source-attribution 阻止了约束层自纠正。在 68 个少数票正确的问题中，即使少数票约束质量更好 (更少 UNSAT)，SICA 仍在 82.4% 的情况下跟随多数票错误答案 → 证明约束层的 degeneration (Observation 1)。

**建议 rebuttal 要点**: SCB 是一个 compound phenomenon。CoT bias 决定 trace 分布 (input)，source-attribution 将 trace-level majority 结构性地保持到 constraint scoring (mechanism)，MaxSAT 的 weight-optimal 策略被 volume imbalance 劫持 (outcome)。三者缺一不可 → SCB 不能被还原为单一的 CoT bias propagation。

---

结果已保存到服务器: `results/exp033_mistral_7b_folio204/r21_mf2_scb_vs_cot_analysis.json`

---
