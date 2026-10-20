# code permutation granger

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_permutation-granger_20260514T214126_result.json`
- **Structured JSON:** [`f13d90c4ffbc98cc0919.json`](../../sessions/f1/f13d90c4ffbc98cc0919.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Summary

### p-value 矩阵（3 test cases × 4 seeds）

| Test Case | s42 | s43 | s44 | s45 | Verdict |
|---|---|---|---|---|---|
| token_entropy→distinct_1 (强信号) | **0.006** | **0.006** | **0.002** | **0.002** | 4/4 SIG |
| effective_rank→distinct_1 (已知null) | 0.069 | 0.165 | 0.169 | 0.069 | 0/4 SIG |
| ece→distinct_2 (边界) | **<.001** | **<.001** | **0.002** | **<.001** | 4/4 SIG |

三个验证用例全部通过。

### 与现有方法对比

| Pair | Naive | Diff | Thresh | TY | **Perm Granger** |
|---|---|---|---|---|---|
| token_entropy→distinct_1 | 4/4 | 4/4 | 4/4 | 4/4 | **4/4** |
| effective_rank→distinct_1 | 4/4 (伪) | 0/4 | 0/4 | 0/4 | **0/4** |
| ece→distinct_2 | 4/4 | 4/4 | 4/4 | 3/4 | **4/4** |

### 关键发现

1. **强信号检测**：token_entropy→distinct_1 的 F 值极大（200-500），f² 效应量 28-72，permutation Granger 以 p<0.01 全部检出
2. **Null 控制**：effective_rank→distinct_1 全部未通过（p=0.069-0.169），与差分法、TY 一致，确认 effective_rank 是伪回归
3. **边界 case 更有力**：ece→distinct_2 在 TY 下仅 3/4 通过，permutation Granger 4/4 全部通过（p<0.002），说明 permutation 方法在 T=11 下比 TY 有更好的统计功效
4. **设计决策**：T=11 下 circular shift 仅有 10 个唯一排列（最小 p≈0.091），无法在 α=0.05 下拒绝 H0，因此 `method='auto'` 自动降级为 random shuffle

### 结论

Permutation Granger 适合作为核心分析方法（Method 5）。相比 TY，它在短序列下有更好的功效，同时保持了良好的假阳性控制。

**产出**：
- 脚本：`westd-19828:/root/autodl-tmp/distrib_canary_collapse/permutation_granger.py`
- 结果：`results/mvp/analysis/permutation_granger.json`

---
