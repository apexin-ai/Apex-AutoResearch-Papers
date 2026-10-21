# research draft response letter outline

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_draft-response-letter-outline_20260520T071218_result.json`
- **Structured JSON:** [`d742a40fc1571c7f2145.json`](../../sessions/d7/d742a40fc1571c7f2145.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

大纲已写入 `artifacts/response_letter_outline.md` 并注册。

**结构概览**：8 个主题 (A-H)，覆盖 R24 全部 issue：

| 主题 | 核心关切 | 回应策略 |
|------|---------|---------|
| **A** 公式验证 | 分解公式仅 3 点验证 | 23-config 回归 R²=-8.53，删除公式，改定性叙述 |
| **B** Gating 循环性 | τ=0.3 来源不明，dev 50 实例 | Bootstrap CI + τ∈[0.2,0.4] 稳定性 ≥95%，4/4 正确路由 |
| **C** Construction 过度声称 | "Resolving" + 仅恢复 ~1pp | Title→"Addressing"，降级为 diagnostic-motivated mitigation |
| **D** 范围局限 (8B FT only) | 泛化性不足 | 4B→7B→14B→32B→72B + ZS + 3 model families |
| **E** By-construction vs 经验 | 概念混淆 | 正文三层分离：定义性/LP经验/MBR经验 |
| **F** Related Work | CISC/Self-Certainty 缺对比 | RW 扩展 + 新子节 + Nédellec & Xia 2026 |
| **G** 统计严谨性 | SciERC underpowered, p-value 缺失 | MDE 标注, p-value 补全, F1 定义统一 |
| **H** 写作细节 | 审稿历史泄露, bib 清理 | 逐项修复 |

**新增非直接回应 R24 的内容**：72B ZS regime、FS error correlation (falsified)、7B/14B/32B scaling、WNUT-17、30+ appendix sections。

14B/32B 数据标注为 `[pending data]`，需到齐后更新。

---
