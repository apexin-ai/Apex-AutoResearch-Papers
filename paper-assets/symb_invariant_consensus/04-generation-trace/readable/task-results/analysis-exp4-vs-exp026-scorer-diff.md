# analysis exp4 vs exp026 scorer diff

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp4-vs-exp026-scorer-diff_20260518T183040_result.json`
- **Structured JSON:** [`975d17c51add552c09ea.json`](../../sessions/97/975d17c51add552c09ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete analysis.

---

## 调查报告：exp4 T=1 (77.94%) vs exp-026 (74.51%) SICA 差异

### 1. 根因：不同的 constraint extraction 输入

两个 scorer **代码完全相同**（都用 `sica.scorer.InvariantScorer` + `sica.z3_maxsat.ConstraintDeduplicator` + `MaxSATSolver`）。差异完全来自**输入 constraints 不同**。

| | exp-026 (pipeline) | exp4 (per_trace_constraints) |
|---|---|---|
| 约束来源 | `SICAPipeline.run_single()` 内部的 `ConstraintExtractor` | `extract_constraints.py` 独立脚本 |
| API 端点 | `localhost:8000/v1` | `localhost:8001/v1` (不同端口!) |
| extraction 温度 | 0.3 (`VLLMBackend` 默认值) | 0.1 (脚本硬编码) |
| 模型 | Qwen2.5-14B-Instruct (日志确认) | 未知 (auto-detect from port 8001) |
| 提示词 | `LOGIC_EXTRACTION_PROMPT` via `ConstraintExtractor` | `LOGIC_EXTRACTION_PROMPT` via 直接 API 调用 |

**`extract_constraints.py` 是对 exp-026 intermediates 中的 traces 做了第二次 constraint extraction**，用了不同端口/温度/可能不同模型。这不是"同一份 constraints"。

### 2. Scorer 代码差异清单

| 维度 | exp4 (`run_consistency_filtering.py`) | exp-026 (`sica/pipeline.py`) | 影响 |
|---|---|---|---|
| `normalize_logic_answer` | 简单版: True/False/Unknown 映射 | 增强版: 额外处理 `\text{...}` 和 "1"→True, "0"→False | 对 FOLIO 无影响 |
| Dedup | `ConstraintDeduplicator()` (同一类) | 同 | 无 |
| MaxSAT | `MaxSATSolver().solve(filtered, timeout=10000)` | 同 | 无 |
| Scorer | `InvariantScorer()` (alpha=0.5, fallback=0.2) | 同 | 无 |
| Tiebreak | `select_answer(scores, answer_counts)` → 频率 | 同 | 无 |

**结论：scorer 逻辑无差异，问题 100% 出在输入 constraints 上。**

### 3. 16 个 diff 题目详细分析

实际有 **16 个题目**预测不同（不是 7 个），净效果 +7 correct for exp4 (10 wins - 3 losses)。

#### exp4 赢的 10 题
| Problem | GT | exp4 | exp026 | 原因 |
|---|---|---|---|---|
| folio_7 | Unknown | Unknown ✓ | False ✗ | exp4 有 46 raw constraints vs exp026 仅 21，更丰富的约束集正确区分了 Unknown |
| folio_90 | Unknown | Unknown ✓ | True ✗ | exp4 仅 9 constraints，全部指向 Unknown；exp026 有 43 但偏向 True |
| folio_117 | Unknown | Unknown ✓ | False ✗ | exp4 约束分布更均衡 (F:40, U:42)；exp026 约束偏向 False (60 vs 52) |
| folio_136 | Unknown | Unknown ✓ | False ✗ | exp4 仅 7 unique，分数接近 (U:33, F:30)；exp026 22 unique 偏向 False |
| folio_146 | Unknown | Unknown ✓ | True ✗ | exp4 12 unique 全部关联 Unknown traces；exp026 18 unique 偏向 True |
| folio_151 | Unknown | Unknown ✓ | False ✗ | exp4 scores U:24 > F:14；exp026 scores F:30 > U:24 |
| folio_162 | Unknown | Unknown ✓ | True ✗ | exp4 scores tied (T:15, U:15) → tiebreak by SC votes (U=8 > T=3)；exp026 T:37 > U:36 |
| folio_164 | Unknown | Unknown ✓ | False ✗ | exp4 仅 6 constraints → U:4.5 > F:0；exp026 55 constraints 偏向 False |
| folio_171 | True | True ✓ | False ✗ | exp4 12 unique → T:15 > F:12；exp026 18 unique 偏向 False (72 > 67) |
| folio_173 | Unknown | Unknown ✓ | False ✗ | exp4 仅 7 constraints 全关联 Unknown；exp026 78 constraints 偏向 False |

#### exp026 赢的 3 题
| Problem | GT | exp4 | exp026 | 原因 |
|---|---|---|---|---|
| folio_0 | Unknown | True ✗ | Unknown ✓ | exp4 37 unique，True 得分高；exp026 38 unique，Unknown 分数略高 |
| folio_73 | True | False ✗ | True ✓ | exp4 仅 13 unique 全落在 False traces；exp026 42 unique 正确偏向 True |
| folio_121 | Unknown | True ✗ | Unknown ✓ | exp4 仅 5 unique 偏向 True traces；exp026 13 unique 正确偏向 Unknown |

#### 双方都错的 3 题
folio_41 (exp4: 0 constraints → degenerate), folio_84, folio_125

### 4. 核心模式

**exp4 赢的 10 题中，9 题 GT=Unknown**。exp4 的低质量 extraction 产生极少约束 → 分数微弱 → tiebreak 由 SC 投票决定 → 碰巧对 Unknown 类问题更准。这**不是 SICA 的真实能力**，而是退化到"近似 SC"的结果。

关键证据：
- folio_162: exp4 scores tied at 15.0 → tiebreak by SC votes → Unknown wins (8 votes)
- folio_164: exp4 total score = 4.5 (近乎无信号) → Unknown wins by 4.5 vs 0
- folio_173: exp4 total score = 7 (7 constraints 全来自 Unknown traces)

### 5. 结论

**两个 scorer 都没有 bug。** 差异完全来自 constraint extraction 质量不同：

- **exp-026 (74.51%) 是正确的 canonical SICA 结果**：使用完整 pipeline 一次性跑完，constraints 和 traces 来自同一个 session。
- **exp4 T=1 (77.94%) 是不可比的数字**：`extract_constraints.py` 用不同端口 (8001 vs 8000)、不同温度 (0.1 vs 0.3)、可能不同模型做了第二次 extraction，产出的 constraints 质量显著不同。

### 6. 对论文核心 claim 的影响

使用 canonical 结果：
- SC = 75.00% (153/204)
- SICA = 74.51% (152/204)
- **Δ = -0.49pp** → 支持 "capability trap" claim (SICA ≈ SC)

如果误用 exp4 的 77.94%：
- Δ = +2.94pp → 削弱 claim

**建议：论文中使用 exp-026 的 74.51%，丢弃 exp4 T=1 的数字。** exp4 的 T=4/6/8 数据同样不可靠（基于相同的低质量 per_trace_constraints），如需 consistency filtering 消融，应基于 exp-026 的 constraints 重新跑。

---
