# code exp036b cross trace unsat

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp036b-cross-trace-unsat_20260518T185714_result.json`
- **Structured JSON:** [`78e7cf1b3a99e4bcefc9.json`](../../sessions/78/78e7cf1b3a99e4bcefc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-036b 结果

### 核心数据

| 指标 | 值 |
|---|---|
| 总问题数 | 204 |
| 单答案(跳过) | 120 (58.8%) |
| 多答案(检查) | 84 |
| 有 cross-UNSAT 的问题 | 9/84 (10.7%) |
| Pair-level cross-UNSAT rate | **8.7%** (11/126 pairs) |
| Within-trace UNSAT baseline | 0.9% |

Cross-trace UNSAT rate (8.7%) 约为 within-trace baseline 的 **~10x**。

### Pair 结果分布

| 结果 | 数量 | 占比 |
|---|---|---|
| UNSAT | 11 | 8.7% |
| SAT | 46 | 36.5% |
| Empty (一侧无公式) | 69 | 54.8% |

### 按答案对类型

- **False-True**: unsat=7, sat=8, empty=23 → UNSAT rate 最高 (7/15 non-empty = 46.7%)
- **False-Unknown**: unsat=3, sat=22, empty=21
- **True-Unknown**: unsat=1, sat=16, empty=23

### 变量共享瓶颈

- 平均共享变量: 2.7 个
- **71/126 pairs (56.4%) 共享零变量** → Z3 无法检测矛盾
- 这是 cross-trace UNSAT 率不更高的主要原因：不同 trace 的符号化用不同变量名

### 准确率影响

| 方法 | 准确率 |
|---|---|
| SC baseline | 75.0% |
| SICA | 74.5% |
| SICA+CrossUT (bonus=5) | 74.5% |

只产生 1 个 flip (folio_125: True→False, gt=Unknown)，neutral。因为只有 9 个问题有 UNSAT 信号，调整覆盖面太小。

### 关键发现

1. **Cross-trace UNSAT rate ~10x 高于 within-trace**，验证了核心假设：不同答案的约束确实更容易矛盾
2. **主要瓶颈是变量命名不一致**：56% 的 answer pairs 共享零变量，Z3 无法跨 trace 比较
3. **False-True 对最具辨别力**：non-empty pairs 中 46.7% 是 UNSAT
4. **对准确率无直接提升**：UNSAT 信号太稀疏（仅覆盖 9/204 问题）

### 产出文件
- `/root/symb_invariant_consensus/cross_trace_unsat.py`
- `/root/symb_invariant_consensus/results/exp036b_cross_trace_unsat.json`

---
