# analysis cwm relaxed matching

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cwm-relaxed-matching_20260515T122839_result.json`
- **Structured JSON:** [`5e1ebf0710b57b4eeeb3.json`](../../sessions/5e/5e1ebf0710b57b4eeeb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

## Repo-level CWM 4B (seed 42) Relaxed Matching 分析

| 策略 | Parseable率 | Acc (parsed) | Overall Acc | Upper Bound |
|------|------------|-------------|-------------|-------------|
| **Strict** (原始) | 46.3% | 42.88% | 58.04% | 59.04% |
| **Normalized** (whitespace+pytest summary) | 69.6% | 54.16% | 59.61% | 59.87% |
| **Enhanced** (6种启发式) | 77.2% | 60.79% | 62.34% | 63.57% |
| Majority baseline | 100% | 72.96% | 72.96% | — |
| **CLS 4B** | 100% | **83.63%** | **83.63%** | — |

### 关键发现

1. Enhanced parser 将 parseable rate 从 46.3% 提升到 77.2%，unparseable 从 53.7% 降到 22.8%
2. 但即使 parseable accuracy 从 42.88% 提升到 60.79%，**overall accuracy 仅从 58.04% → 62.34%**
3. CWM 最优上界 63.57% **仍低于 majority baseline (72.96%)**，更远低于 CLS (83.63%)
4. **Gap = 21.3pp**，strict matching 不是 CWM 低性能的原因

### 备注
- 函数级 CWM seed 42 不存在（只有 seed 123/789，均已 0 unparseable、~87% accuracy）
- 分析脚本和 JSON 结果已保存在 westd: `/home/sonny/exec-sim-repair-verifier/analyze_relaxed_matching.py`
- Artifact 已注册: `art_20260515_77c4fb`

---
