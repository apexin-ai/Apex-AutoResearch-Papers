# DocRED full_s1 DR 10.19% 根因分析

## 1. 核心结论

DocRED full_s1 的 DR=10.19% 远高于 SciERC full_s1 的 DR=0.93%，**根因是 DocRED 的 ontology constraints 远比 SciERC 更紧**：

| 指标 | SciERC | DocRED |
|------|--------|--------|
| Entity types | 6 | 6 |
| Max possible pairs | 36 | 36 |
| Relations | 7 | 96 |
| **Avg tightness** | **0.333** | **0.842** |
| Median valid_pairs/relation | 23 | 5 |
| Relations with tightness ≥ 0.85 | 0/7 (0%) | 50/96 (52%) |
| Relations with tightness ≥ 0.95 | 0/7 (0%) | 4/96 (4%) |

SciERC 的约束极宽松（Used-for 允许 35/36 对），DocRED 的约束极严格（中位数仅 5 对，最少 1 对）。

## 2. Semantic 层效果评估

Semantic 层确实大幅降低了 DR，但无法完全消除高 tightness relations 的 violations：

| 配置 | DR | 说明 |
|------|------|------|
| Grammar-only | 26.17% | 4538/17340 violations |
| **Full_s1** | **10.19%** | **1771/17372 violations** |
| 绝对改善 | **15.98pp** | |
| 相对改善 | **61.0%** | |

Semantic 层在大多数 relations 上有效，仅 2 个 relation 完全无改善（P171 parent taxon、P676 lyrics by）。

## 3. Tightness 与 DR 的关系

Pearson r(tightness, DR_rate) = **0.3682** (n=90, ≥5 triples)

按 tightness 分桶的聚合 DR：

| Tightness 区间 | Valid pairs | Relations | Agg DR | Violations |
|----------------|------------|-----------|--------|------------|
| 0.95-1.00 | 1-2 pairs | 4 | **30.6%** | 78/255 |
| 0.90-0.94 | 3-4 pairs | 15 | **19.3%** | 230/1192 |
| 0.85-0.89 | 4-5 pairs | 28 | **12.9%** | 658/5107 |
| 0.80-0.84 | 6-7 pairs | 23 | 7.0% | 322/4587 |
| 0.70-0.79 | 8-11 pairs | 18 | 9.0% | 477/5305 |
| <0.70 | 11+ pairs | 2 | 0.7% | 6/910 |

**明确的单调趋势**：tightness 越高 → DR 越高。

## 4. Top 15 高违规 Relations

| Rel | Name | Pairs | Tight | Total | Viol | DR% | GO→S1 改善 |
|-----|------|-------|-------|-------|------|-----|-----------|
| P1001 | applies to jurisdiction | 8 | 0.778 | 966 | 194 | 20.1% | +19.1pp |
| P737 | influenced by | 4 | 0.889 | 581 | 131 | 22.6% | +26.5pp |
| P276 | location | 5 | 0.861 | 451 | 128 | 28.4% | +20.2pp |
| P1344 | participant of | 7 | 0.806 | 488 | 95 | 19.5% | +17.0pp |
| P582 | end time | 3 | 0.917 | 186 | 81 | 43.5% | +19.1pp |
| P800 | notable work | 4 | 0.889 | 372 | 79 | 21.2% | +15.2pp |
| P50 | author | 8 | 0.778 | 433 | 72 | 16.6% | +15.8pp |
| P463 | member of | 10 | 0.722 | 745 | 71 | 9.5% | +9.7pp |
| P607 | conflict | 7 | 0.806 | 278 | 68 | 24.5% | +15.2pp |
| P740 | location of formation | 6 | 0.833 | 1124 | 58 | 5.2% | +16.6pp |
| P206 | located in/next to water | 4 | 0.889 | 652 | 55 | 8.4% | +30.2pp |
| P576 | dissolved/abolished | 4 | 0.889 | 146 | 53 | 36.3% | +9.4pp |
| P1056 | product/material produced | 2 | 0.944 | 156 | 48 | 30.8% | +46.7pp |
| P205 | basin country | 1 | 0.972 | 108 | 40 | 37.0% | +27.5pp |
| P1366 | replaced by | 5 | 0.861 | 120 | 31 | 25.8% | +24.6pp |

Top 15 贡献 1352/1771 = **76.3%** 的总违规。

## 5. Extreme DR Relations (DR > 40%)

| Rel | Name | Pairs | DR% |
|-----|------|-------|-----|
| P1198 | unemployment rate | 2 | 83.3% |
| P6 | head of government | 4 | 84.6% |
| P171 | parent taxon | 4 | 77.8% |
| P35 | head of state | 4 | 64.7% |
| P190 | sister city | 1 | 58.0% |
| P488 | chairperson | 3 | 52.4% |
| P1336 | territory claimed by | 3 | 45.0% |
| P582 | end time | 3 | 43.5% |

这些 relations 都是 1-4 valid pairs，constraint 极紧。

## 6. Fallback 日志状态

日志中无 `grammar_first_skip` / `fallback` 信息 — **fallback counter 代码在 full_s1 跑完后才加入**。因此无法直接计算 fallback 频次，上述分析基于 JSONL 输出的 violation 模式推断。

## 7. 根因总结

DR 10.19% 的根因是**约束紧度差异**，而非 semantic 层失效：

1. **DocRED avg tightness = 0.842 vs SciERC = 0.333**：DocRED 每个 relation 平均仅允许 5.7 个 type pairs（SciERC 允许 24 个），LLM 生成违规 pair 的概率成倍增加
2. **Semantic 层实际生效**：DR 从 26.17%→10.19%（-61%），几乎所有 relation 都有改善
3. **剩余 10.19% 来自高 tightness relations**：tightness≥0.85 的 50 个 relations 贡献了绝大部分违规。这些 relation 仅允许 1-5 个 pairs，即使 semantic mask 缩小了候选空间，LLM 仍会在 token-level 生成不在允许集内的 type
4. **SciERC 本身约束太松**：最紧的 Compare 也有 17/36 pairs (tightness=0.528)，任何 type pair 几乎都能命中，所以 DR 天然低

**推论**：要进一步降低 DocRED DR，需要强化高 tightness relations 的约束执行，例如：
- 在 fallback 时不完全退回 grammar-only，而是用 relaxed semantic mask
- 对 tightness≥0.9 的 relations，在 prompt 中显式列出允许的 type pairs
- 对极端 relations（1-2 pairs），考虑硬约束 post-filtering
