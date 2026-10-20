# analysis ic vs fc correlation

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ic_vs_fc_correlation_20260514T120518_result.json`
- **Structured JSON:** [`ac6ea4c1b11a07894d31.json`](../../sessions/ac/ac6ea4c1b11a07894d31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

## IC vs FC 相关性分析（N=224 chains）

### Pearson Correlation
- **r = 0.744, p = 4.49e-41**

### fc_score − ic_score 差值
- mean=0.052, std=0.111, min=0.000, max=0.667
- **37.1% 的 chains（83/224）fc ≠ ic**

### All-SAT chains（ic_sat=True，141 chains）
- **fc_score ≡ ic_score**：141/141 完全相等
- ic/fc 均值=0.867，范围 [0.333, 1.000]
- fc=1.0 的仅 52/141（说明 all-SAT 不等于满分，formalized_claims < total_claims 时 score < 1）

### Non-SAT chains（ic_sat=False，83 chains）
- ic_score: mean=0.763, std=0.176, range [0.167, 0.975]
- fc_score: mean=0.904, std=0.104, range [0.600, 1.000]
- **fc > ic 对所有 83 条 non-SAT chain 都成立（83/83），没有例外**
- 平均提升 0.141（fc 比 ic 高约 14 个百分点）
- Non-SAT 子集内 Pearson r = 0.581

### 结论

**r = 0.744，处于 0.5–0.9 之间 → PCV 提供了有意义的增量信息，但不是完全独立的。**

关键发现：
1. **All-SAT chains 中 fc ≡ ic**——PCV 的增量为零。这是因为 ic_sat=True 意味着所有 formalized claims 互相一致，fc 无法在此基础上额外调整。
2. **Non-SAT chains 中 fc 系统性高于 ic**——每一条 non-SAT chain 的 fc 都严格大于 ic，平均高 14.1pp。这说明 PCV 通过引入 premise 一致性检查，为那些内部逻辑不完全一致的 chain 恢复了部分得分（claims 虽然互相矛盾但与 premises 一致）。
3. PCV 的增量集中在 non-SAT chains 上，对 all-SAT chains 无影响。这是合理且有价值的行为——PCV 在 IC 已经"放弃"的 chain 上提供了更细粒度的区分能力。

---
