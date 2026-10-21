# analysis jaccard v2

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_jaccard_v2_20260519T205054_result.json`
- **Structured JSON:** [`21b6bb284aa48fb42558.json`](../../sessions/21/21b6bb284aa48fb42558.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已生成。所有数据从已有的分析中提取（无需重新 SSH 计算）。

## 结果汇总

**340M Within-Scale Pairwise Jaccard (pure → h3-1)**
| Pair | J_helped | J_hurt |
|------|----------|--------|
| GDN-RetNet | 0.092 | 0.109 |
| GDN-HGRN2 | 0.084 | 0.075 |
| HGRN2-RetNet | 0.108 | 0.085 |
| **Mean** | **0.094** | **0.090** |

**1.3B Within-Scale Pairwise Jaccard (pure → h3-1)**
| Pair | J_helped | J_hurt |
|------|----------|--------|
| GDN-RetNet | 0.092 | 0.103 |
| GDN-HGRN2 | 0.100 | 0.088 |
| HGRN2-RetNet | 0.108 | 0.087 |
| **Mean** | **0.100** | **0.093** |

验证：
- 340M mean J_helped = 0.094 ≈ 0.094 ✓
- 340M mean J_hurt = 0.090 ≈ 0.090 ✓
- 1.3B mean J_helped = 0.100（略高于预期 [0.092, 0.100] 上界，但在四舍五入后勉强满足）

注意：论文 experiments.tex 当前引用 1.3B 的值为 "0.095 and 0.090"，但实际计算值为 0.100 和 0.093。论文中的数值可能需要更新。

结果文件保存在 `artifacts/paper_data/within_scale_jaccard_results.txt`。

---
