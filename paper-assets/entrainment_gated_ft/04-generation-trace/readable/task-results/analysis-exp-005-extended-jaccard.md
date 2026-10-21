# analysis exp 005 extended jaccard

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-005-extended-jaccard_20260523T020824_result.json`
- **Structured JSON:** [`2d4d9ecdadcd9fbfa86c.json`](../../sessions/2d/2d4d9ecdadcd9fbfa86c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

## 4-Benchmark × 5-Architecture Pairwise Jaccard 结果

| Benchmark | n_samples | mean J_helped | mean J_hurt | z_helped 范围 | z_hurt 范围 | 显著对 |
|-----------|-----------|---------------|-------------|---------------|-------------|--------|
| LAMBADA | 5,153 | 0.1221 | 0.0946 | [9.0, 12.2] | [6.3, 10.9] | 10/10 |
| ARC-Easy | 2,376 | 0.1081 | 0.1047 | [3.5, 9.2] | [3.7, 7.5] | 10/10 |
| HellaSwag | 10,042 | 0.0931 | 0.0815 | [10.3, 19.2] | [10.2, 16.3] | 10/10 |
| PIQA | 1,838 | 0.0928 | 0.0863 | [3.1, 9.5] | [3.2, 7.2] | 10/10 |

**Grand mean**: J_helped=0.1040, J_hurt=0.0918  
**Total significant**: **40/40** (helped + hurt 各 40 对全部 p<0.01)

### 要点
- HellaSwag 的 z-score 最高（z_helped 最高达 19.2），因为样本量最大（10042）
- PIQA 样本量最小（1838），z-score 相对较低但仍全部显著（最低 z=3.08）
- J_helped 一致高于 J_hurt（4/4 benchmarks），表明 helped set 的跨架构一致性更强
- 从 2 benchmarks 扩展到 4 benchmarks 后，结论完全一致：attention-mediated sample sensitivity 是 architecture-independent 的

产出文件：`/root/entrainment_gated_ft/results/exp005_zoo_expansion/jaccard_5arch_extended.json`（已注册 artifact + 更新 registry）

---
