# analysis constraint quality crossmethod

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_constraint-quality-crossmethod_20260520T013328_result.json`
- **Structured JSON:** [`d9c886e81e0178d5f94d.json`](../../sessions/d9/d9c886e81e0178d5f94d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
| Method      | parse_rate | z3_compile% | unique/q | redundancy% | discrim%  | triv_sat% |
|-------------|-----------|-------------|----------|-------------|-----------|-----------|
| SICA        | 97.1%     | 96.5%       | 39.3     | 42.9%       | 81.4%*    | N/A       |
| ICG         | 74.6%     | 99.4%       | 24.9     | 32.3%       | 77.0%*    | N/A       |
| Contrastive | 74.0%     | 94.4%       | 9.2      | 0.0%        | 51.0%     | 62.7%     |
| Debate      | 81.3%     | N/A         | 13.0†    | N/A         | N/A       | N/A       |
```

`*` = proxy（MaxSAT 分数支持 >1 候选的题目比例）  
`†` = reasoning units，非 Z3 约束

关键发现：

1. **SICA 产出最多约束**（39.3/题），trace yield 最高（97.1%），但 42.9% 冗余直接印证了 co-sourcing
2. **ICG Z3 编译率最高**（99.4%），冗余更低（32.3%），约束更干净多样，但 trace yield 较低（74.6%）
3. **Contrastive 约束最少**（9.2/题），仅 51% 的题有区分力，62.7% 的题所有 pro 约束被 trivially satisfied —— 约束质量最差
4. **Debate 无符号约束**，63.1% debate 有效，87.3% trace 产出答案
5. `discriminative_ratio` 和 `trivially_sat_ratio` 仅 Contrastive 可直接计算（存储了 per-candidate Z3 结果）；SICA/ICG 用统一 MaxSAT，无 per-candidate 分解

---
