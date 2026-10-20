# research paper table prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-table-prep_20260514T083059_result.json`
- **Structured JSON:** [`fff4dbf4923b395a1f32.json`](../../sessions/ff/fff4dbf4923b395a1f32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

8 artifacts 全部注册完成。产出汇总：

| 文件 | 说明 |
|------|------|
| `table1_goodhart.csv/.tex` | Goodhart Landscape — 9 行（7 条件 + 3-seed mean + 1000-step），含数据来源脚注 |
| `table2_hacking_taxonomy.csv/.tex` | 5 种 hacking 模式分类，含 PR/ISR/component count/诊断特征 |
| `table3_isr_collapse.csv/.tex` | ISR 崩塌轨迹 100→500→1000 步 (0.64→0.13→0.003) |
| `table4_beta01_comparison.csv/.tex` | β=0.1 ISR vs random 对照，ISR 3.2× > random |

**数据来源标注**：
- plan002-b03 (ISR β=0.3): 仅有训练指标在 registry，eval PR=0.18/ISR=0.026 来自 paper_framing，已标 †
- plan005 (convex ISR): 无 eval checkpoint，使用训练 last-100 数据，已标 ‡
- plan013/plan001-s44: ISR 为 tautological artifact，已标 *
- plan001-s43: 使用 sampling eval (temperature=0.7)，与其他 seed 的 greedy eval 不完全可比，已在脚注说明

---
