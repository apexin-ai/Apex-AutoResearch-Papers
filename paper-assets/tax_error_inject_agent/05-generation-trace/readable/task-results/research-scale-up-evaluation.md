# research scale up evaluation

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_scale-up-evaluation_20260516T045009_result.json`
- **Structured JSON:** [`bef7e34149ac5a202788.json`](../../sessions/be/bef7e34149ac5a202788.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/trajectory_scaleup_feasibility.md`。核心结论：

**可行，但任务池是瓶颈。**

| 维度 | 数值 |
|------|------|
| API 总成本 | ~$47（收集 $35 + 注入 $12） |
| 数据准备时间 | ~2.2h（4 workers） |
| 训练数据量 | 4.5万 TaxEI samples（当前 9K 的 5x） |
| 单次训练时间 | 11.7h (1 GPU) / 2.9h (4 GPU DDP) |
| 多 seed 完整实验 | ~1.8 天 GPU 时间 |

**两个关键风险**：
1. ALFWorld 有效任务池 ~3000-3500 games，需要 ~3563 次尝试，**可能刚好不够**——需先运行 `collect_game_files` 验证
2. 收集脚本的 overshoot factor (1.15) 对 70.2% 成功率不够，需改为 1.5+

建议先验证任务池大小，再分阶段收集（先到 1000 看趋势）。

---
