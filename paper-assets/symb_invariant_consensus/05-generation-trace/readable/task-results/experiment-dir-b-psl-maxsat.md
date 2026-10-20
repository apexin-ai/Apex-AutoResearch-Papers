# experiment dir b psl maxsat

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-b-psl-maxsat_20260520T152648_result.json`
- **Structured JSON:** [`b83687454423566017b5.json`](../../sessions/b8/b83687454423566017b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果报告

### 30 题 Pilot

| Strategy | Correct | Acc | Δ vs baseline |
|---|---|---|---|
| SC | 16/30 | 53.3% | +3.3% |
| SICA stored | 16/30 | 53.3% | +3.3% |
| **baseline** (re-dedup) | 15/30 | 50.0% | — |
| quadratic (w²) | 16/30 | 53.3% | **+3.3%** |
| thresh_3 | 16/30 | 53.3% | **+3.3%** |
| thresh_6 | 16/30 | 53.3% | **+3.3%** |
| answer_aligned | 16/30 | 53.3% | **+3.3%** |

### 全 204 题扩展

| Strategy | Correct | Acc | Δ vs baseline |
|---|---|---|---|
| SC | 112/204 | 54.9% | 0.0% |
| SICA stored | 121/204 | 59.3% | +4.4% |
| **baseline** (re-dedup) | 112/204 | 54.9% | — |
| **quadratic (w²)** | **114/204** | **55.9%** | **+1.0%** |
| log | 112/204 | 54.9% | 0.0% |
| sqrt | 111/204 | 54.4% | -0.5% |
| thresh_3 | 111/204 | 54.4% | -0.5% |
| thresh_6 | 110/204 | 53.9% | -1.0% |
| answer_aligned | 111/204 | 54.4% | -0.5% |
| majority_only | 112/204 | 54.9% | 0.0% |

### 关键发现

1. **Quadratic weighting 是唯一有正向提升的策略** (+1%, 5 gains / 3 losses)，通过放大高频 constraints 的优势来区分信号/噪声。

2. **Confidence filtering 反而伤害性能** — thresh_6 掉了 1%。丢弃低频 constraints 导致信息损失大于噪声消除。

3. **Answer-aligned weighting 无帮助** — 说明 constraint 来源 trace 的答案与 constraint 质量之间关联弱。

4. **主要 confound: Dedup 非确定性**。Re-dedup 产生的 baseline（112/204）比 stored SICA（121/204）低 9 个。22 题上有差异，原因是 z3 等价性检查对执行顺序/超时敏感。所有策略内部比较仍公平（共享同一 dedup），但绝对数字偏低。

5. **Quadratic 的 per-problem flips**:
   - Gains: folio_8, folio_88, folio_120, folio_175, folio_183
   - Losses: folio_94, folio_136, folio_148

**结论**: Weighted MAX-SAT 方向效果微弱（+1% 不显著），不建议作为主要改进方向。如果要继续探索，quadratic weighting 是唯一值得深挖的变体，但需要先解决 dedup 确定性问题以获得可靠评估。

---
