# analysis extraction error taxonomy

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_extraction-error-taxonomy_20260519T010920_result.json`
- **Structured JSON:** [`6472d775fe301dbab847.json`](../../sessions/64/6472d775fe301dbab847.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

执行成功。结果总结：

## Extraction Error Taxonomy 结果

### Baselines
| 方法 | 准确率 |
|------|--------|
| exp033 SICA (Mistral-7B, self-extracted) | 59.3% |
| exp033 SC | 54.4% |
| exp031 Oracle SICA (Qwen-14B, gold FOL) | 89.7% |
| **Oracle ceiling gap** | **30.4pp** |

### Outcome Distribution (n=204)
- both_correct: 109 (53.4%), sica_wins: 12 (5.9%), sc_wins: 2 (1.0%), both_wrong: 81 (39.7%)
- SICA override precision: **85.7%** (12 correct / 14 decisive overrides)

### Error Taxonomy (按 prevalence 排序)
| Issue | Prevalence | Harmful Rate |
|-------|-----------|-------------|
| **trivially_satisfied** (约束全被满足，无过滤信号) | 43.1% | 34.1% |
| **high_redundancy** (dedup ratio < 0.5) | 35.3% | 36.1% |
| **incomplete_extraction** (部分 trace 提取失败) | 15.7% | 28.1% |
| **low_consensus** (avg weight < 1.15) | 9.3% | **47.4%** |
| **low_discrimination** (score range < 5) | 5.9% | **41.7%** |
| **high_contradiction** (excluded > 10%) | 5.4% | 36.4% |

### 关键发现

1. **最有害的错误**: `low_consensus` (47.4% harmful rate) 和 `low_discrimination` (41.7%)——虽然 prevalence 低，但出现时几乎一半导致错误
2. **最普遍的错误**: `trivially_satisfied` (43.1%)——约束被全部满足意味着 MaxSAT 没有提供过滤信号，但 harmful rate 相对适中 (34.1%)
3. **Oracle gap = 30.4pp**: 68 个问题 oracle 对但 self-extracted 错，仅 6 个反向。说明约束质量是 SICA 的主要瓶颈
4. **Per-group 对比**: `both_wrong` 组的 score_range 反而最高 (29.4)，说明错误约束产生的高置信度判断更危险——**约束不是太少而是错误方向**
5. **FOL 复杂度**: 简单问题 (<=4 premises) SICA 71.4%，复杂问题 (7+) 降至 53.8%；复杂问题 SICA 完全没有超过 SC 的优势

---
