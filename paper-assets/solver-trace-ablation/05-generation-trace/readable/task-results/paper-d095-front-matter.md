# paper d095 front matter

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d095-front-matter_20260515T195607_result.json`
- **Structured JSON:** [`ce4e1c2f3bff76c52aa7.json`](../../sessions/ce/ce4e1c2f3bff76c52aa7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件全部更新完毕，数据一致性验证通过：

| 数据点 | abstract | introduction | conclusion |
|--------|----------|-------------|------------|
| ISR H7 | 70.6% | 70.6% | 70.6% (163/231) |
| Random H7 | 13.7% | 13.7% | 13.7% (36/262) |
| Fisher p | 1.3×10⁻³⁹ | <10⁻³⁸ | <10⁻³⁸ |
| ~5× amplification | ✓ | ✓ | — (gradient描述) |
| seed-dependent | ✓ | ✓ | 38.3%/0%/0% |
| 1.06× | ✓ | ✓ | ✓ |

Narrative A 硬约束检查：
- 未说 "H7 is ISR-specific" 或 "zero under random" ✓
- 标注 random H7 单 seed 来源 ✓
- 未 claim genuine 显著差异 ✓
- dose-response 段已删除 "by 1000 steps converges to 100% H7" 作为主论据 ✓
- random β=0.3 更新为 4–7 H7a ✓

---
