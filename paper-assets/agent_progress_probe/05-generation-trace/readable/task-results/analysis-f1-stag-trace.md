# analysis f1 stag trace

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_f1-stag-trace_20260514T182951_result.json`
- **Structured JSON:** [`d1f1ebd9b460bd6c3b47.json`](../../sessions/d1/d1f1ebd9b460bd6c3b47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/root/autodl-tmp/agent_progress_probe/analysis_f1stag_report.txt`。

**汇总：**

| 实验 | macro_f1 | f1_stag | f1_prog | N |
|------|----------|---------|---------|---|
| probe_001 (conf>=2) | 0.9055 | **0.8593** ✓ | 0.9518 | 1824 |
| outcome-bp-3seed mean | 0.7701 | **0.6409** ✓ | 0.899 | 8101 |
| oh-full-finetune (OH) | 0.7512 | **0.5439** ✓ | 0.9586 | 20807 |
| woob conf>=2 3-LF | 0.7659 | **0.6272** | 0.9046 | 1824 |
| full-model conf>=2 (ref) | 0.9396 | 0.9103 | 0.9690 | 1824 |

**三项 registry 数字全部确认一致。**

**0.000 溯源结论：** 不来自任何完整测试集。来源是 OB-only 窗口子集 (687w) 上的评估——woob 模型对这些窗口没有训练信号，全预测为 progress，导致子集 f1_stag=0.000。已被 D025/D026 正确撤回。

**woob 在 conf>=2 上：** macro_f1=0.7659, f1_stag=0.6272。比全测试集 (0.7019/0.5667) 好 6pp，但比 probe_001 同测试集 (0.9055/0.8593) 差 14-23pp。核心瓶颈是 stag recall 仅 0.48。

---
