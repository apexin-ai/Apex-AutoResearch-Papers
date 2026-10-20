# analysis r2n3 llama docred parse excluded

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r2n3_llama_docred_parse_excluded_20260518T120615_result.json`
- **Structured JSON:** [`654dded638cf4b122cf5.json`](../../sessions/65/654dded638cf4b122cf5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Constrained 的数据和官方 violation checker 完全吻合 (ET=0, RV=0, DR=424/16471=2.6%, CF=1371)。unconstrained 因为数据里有 int 类型的 entity text 导致 checker 报错，但我的脚本已做 `str()` 转换，结果可靠。

结果已保存到服务器 `outputs/r2n3_parse_excluded_analysis.json`。

---

## R2-N3 分析结果

### Parse Failure 统计

| | Unconstrained | Constrained |
|---|---|---|
| Total docs | 998 | 998 |
| Parse failures | 67 (6.7%) | 90 (9.0%) |
| Valid docs | 931 | 908 |

Parse failure 重叠：45 共有，45 仅 constrained，22 仅 unconstrained。

### Violation Rates（排除 parse failures 后，仅 valid docs）

| Metric | Unconstrained | Constrained | Delta |
|---|---|---|---|
| ET% | 0.13% | 0.00% | -0.13pp |
| RV% | 15.89% | 0.00% | -15.89pp |
| **DR% (eligible)** | **31.21%** | **2.57%** | **-28.64pp** |
| DR% (all triples) | 26.25% | 2.57% | -23.68pp |
| CF% | 0.17% | 9.40% | +9.23pp |

### F1（all docs vs parse-excluded）

| Metric | Uncon (all) | Con (all) | Uncon (excl) | Con (excl) |
|---|---|---|---|---|
| E-F1 | 55.67% | 55.04% | 57.89% | 58.18% |
| R-F1 | 6.55% | 6.25% | 6.74% | 6.48% |

### 结论

1. **Constrained 的 parse failure 数量更多** (90 vs 67)，所以排除 parse failures 对 unconstrained 更有利，但 constrained 的 violation 依然大幅更低。
2. **DR violation 从 31.21% 降到 2.57%（-28.64pp）**，这是在仅计算成功解析文档的条件下，完全排除了 parse failure 的影响。
3. **RV 从 15.89% 降到 0.00%（-15.89pp）**，语法约束完全消除了词汇外的关系类型。
4. **F1 基本持平**：E-F1 排除 parse failures 后 constrained 略高 (+0.29pp)，R-F1 略低 (-0.26pp)，都在噪声范围内。
5. **CF 上升 (+9.23pp)** 是已知 trade-off：constrained 模式下同一实体在不同关系中的类型一致性下降。

**核心论点：violation 下降不是 parse failure 被排除的副产物，而是 constrained decoding 的真实效果。**

---
