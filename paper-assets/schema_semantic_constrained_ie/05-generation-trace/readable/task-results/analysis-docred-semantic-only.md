# analysis docred semantic only

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_docred_semantic_only_20260514T143526_result.json`
- **Structured JSON:** [`778506860c0943b8fefc.json`](../../sessions/77/778506860c0943b8fefc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。汇总如下：

## DocRED semantic_only vs unconstrained 对比（all_set 方法）

| Metric | unconstrained | semantic_only | Δ |
|--------|:---:|:---:|:---:|
| **DR%** | 18.46% | **14.83%** | **-3.63pp (↓19.7%)** |
| **RV%** | 29.66% | 29.87% | ≈不变 |
| **ET%** | 8.18% | **2.47%** | **-5.71pp (↓69.8%)** |
| CF% | — | 3.47% | — |
| R-F1 | 7.74% | 7.70% | ≈持平 |
| E-F1 | 58.15% | 57.81% | ≈持平 |

**关键结论：**
1. **DR↓19.7%**，与 SciERC 的↓24.1% 接近但更温和，符合 DocRED 96 relations 约束空间更大的预期
2. **ET↓69.8%** 降幅显著，semantic 约束对 entity type 合法性有强约束效果
3. **RV 完全不变**——验证 Claim 3：semantic 层无法消除 relation vocabulary 违规，需 grammar 层配合
4. **F1 无损**——semantic 约束不牺牲抽取质量

---
