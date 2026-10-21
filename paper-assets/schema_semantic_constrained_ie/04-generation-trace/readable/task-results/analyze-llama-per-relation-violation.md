# analyze llama per relation violation

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_llama_per_relation_violation_20260514T222402_result.json`
- **Structured JSON:** [`fe000fc0caaa6734c8ac.json`](../../sessions/fe/fe000fc0caaa6734c8ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已写入 `artifacts/llama_docred_per_relation_dr_analysis.md`。

核心发现：

**Aggregate:**
| | Unconstrained | Full_S1 |
|---|---|---|
| OOV (RV) | 2,756 (16.8%) | 0 (0.0%) |
| DR (of mapped) | 4,221 (30.9%) | 418 (2.6%) |

**Per-relation DR（unconstrained top 3）：** P1198 unemployment_rate 92.3%, P156 followed_by 83.3%, P35 head_of_state 82.4%

**Per-relation DR（full_s1 top 3）：** P576 dissolved 32.9%, P156 followed_by 20.5%, P1198 unemployment_rate 20.0%

**OOV：** 625 unique OOV names（unconstrained），最多的是 "located in"(405)、"date of event"(93)。Full_s1 完全消除 OOV。

**Fallback：** 57,825 token-level fallback 集中在仅 7/998 个文档中（等间距分布，每~166个文档），全部解析成功。这是 token-level 指标，不可直接与 Qwen 的 triple-level 10.2% 比较。

**与 Qwen 对比 & D014 叙事验证：**
- Llama unconstrained OOV 16.8% 远低于 Qwen ~30% → Llama 基线 schema adherence 更好
- Llama full_s1 residual DR 2.6% 很低，仅 3 个 relation >10%
- **支持 "低 RV → 低 residual DR" 叙事**：两因素（RV/DR）独立；full_s1 完全消除 RV，大幅降低 DR；基线 OOV 越低的模型，constrained decoding 后残留 DR 越少
- 残留 DR 热点（P576=32.9%, P156=20.5%）显示某些 relation 的 domain-range 模式本身模糊，即使语义约束也无法完全解决

---
