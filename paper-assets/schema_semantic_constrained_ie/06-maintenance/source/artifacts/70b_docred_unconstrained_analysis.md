# 70B DocRED Unconstrained 实验结果分析

## 完成状态
- Model: Llama-3.1-70B-Instruct-AWQ-INT4
- Dataset: DocRED dev set
- Mode: unconstrained
- Docs processed: **998 / 998** (100%)
- Parse failures: **0** (parse success rate = 100%)
- Total entities extracted: 16,587 predicted / 19,471 gold
- Total triples extracted: 13,414

## Violation Rates

| Violation Type | Count | Rate |
|---|---|---|
| Entity Type (ET) | 3 / 16,597 | **0.02%** |
| Relation Vocabulary (RV) | 1,047 / 13,414 | **7.8%** |
| Domain/Range (DR) | 2,017 / 13,414 | **15.0%** |
| Cross-Field (CF) | 12 | **0.07%** |
| Fuzzy relation matches | 30 | - |

Go/No-go metric (DR violation rate): **0.1504**

## F1 Metrics

### Entity F1
- Precision: **75.03%**
- Recall: **63.92%**
- F1: **69.03%**
- (tp=12,446, gold=19,471, pred=16,587)

### Relation F1 (method_all_set, primary metric)
- Precision: **12.43%**
- Recall: **13.69%**
- F1: **13.03%**
- (tp=1,664, gold=12,151, pred=13,390)

### Relation F1 (method_recognized_set, only recognized relations)
- Precision: **13.48%**
- Recall: **13.69%**
- F1: **13.59%**

## 与 70B SciERC Unconstrained 对比

| Metric | 70B SciERC Unconstrained | 70B DocRED Unconstrained |
|---|---|---|
| ET violation | 0% | 0.02% |
| RV violation | 0.6% | 7.8% |
| DR violation | 6.5% | 15.0% |
| CF violation | 0% | 0.07% |
| Entity F1 | 35.17% | 69.03% |
| Relation F1 | 11.22% | 13.03% |
| Parse success | - | 100% |

## 关键观察

1. **Parse 完美**: 998 docs 全部成功解析，0 failures，70B 模型指令遵循能力极强。
2. **Entity F1 大幅领先 SciERC**: 69.03% vs 35.17%，DocRED 的实体类型更粗粒度（6 types vs SciERC 的细粒度），70B 模型在粗粒度类型识别上表现很好。
3. **Relation F1 仍然很低**: 13.03%，虽然比 SciERC 的 11.22% 高，但 DocRED 的 relation 数量多（96 types, Wikidata PIDs），模型在 unconstrained 模式下难以精确匹配。
4. **RV violation 显著高于 SciERC**: 7.8% vs 0.6%，DocRED 使用 Wikidata PID 作为 relation identifier，模型在 unconstrained 模式下更容易生成不在 ontology 中的 relation name。
5. **DR violation 也大幅升高**: 15.0% vs 6.5%，DocRED ontology 约束更复杂（96 relations x 6 entity types），unconstrained 模式下 domain/range 错误更频繁，这正是 constrained decoding 的价值所在。
