# analysis table1 compilation

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table1-compilation_20260514T073448_result.json`
- **Structured JSON:** [`05e0686ab38b367dd1d3.json`](../../sessions/05/05e0686ab38b367dd1d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已生成并注册：

**`table1_data.json`** — 10 个实验的结构化数据，包含 eval PR/ISR/components/collapse/degradation mode 等全部字段。

**`table1_comparison.md`** — 论文级 Markdown 对比表 + 6 条 key findings + 注释说明。

数据要点：
- 所有数值来自 registry，未编造
- plan001-s43-r4 标注为 sampling eval (T=0.7)，非 eval_sta.py
- plan013 ISR=0.535 和 plan001-s44 ISR=0.57 均标注为 tautological artifact (†)
- plan005-sta-low-s42 标注为 training log only (‡)，checkpoint 已删除无 eval_sta.py 结果

---
