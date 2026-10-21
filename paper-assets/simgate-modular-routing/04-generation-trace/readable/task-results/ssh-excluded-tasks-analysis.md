# ssh excluded tasks analysis

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_excluded-tasks-analysis_20260518T035952_result.json`
- **Structured JSON:** [`393f2c45e09e8f5d6110.json`](../../sessions/39/393f2c45e09e8f5d6110.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，报告已写入 `artifacts/excluded_tasks_analysis.md`。

核心发现：

**18/19 excluded task types (95%) 展示 death asymmetry**，唯一例外是 grow-plant（两种策略都无死亡）。

关键对比数据：
| 指标 | Excluded (19) | Included (11) |
|------|--------------|---------------|
| Mean int death rate | 53.9% | 46.5% |
| Mean det death rate | 15.8% | 17.8% |
| Mean ΔDR | **+38.2 pp** | +28.7 pp |
| Tasks with ΔDR > 0 | 95% | 91% |

Excluded tasks 的 death asymmetry 实际**高于** included tasks，完全反驳 cherry-picking 假说。

报告包含：
1. 所有 19 个 excluded tasks 的完整 death rate 表（含 Group A/B/C 分组）
2. LaTeX-ready 表格（`\label{tab:excluded-death}`）
3. Appendix C 可直接插入的分析段落
4. experiments.tex 和 main.tex 三处措辞的具体修改建议（当前 "both strategies time out" 表述不准确）

**注意**：你提供的 included task list 与论文 per-task table 不一致。论文实际包含 identify-life-stages-1/2 和 inclined-plane-determine-angle，不包含 grow-plant/use-thermometer/measure-melting-point-known。本分析使用论文中的正确分类。

---
