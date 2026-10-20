# paper writing tables

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_tables_20260515T045108_result.json`
- **Structured JSON:** [`210be14d6c8c137424fa.json`](../../sessions/21/210be14d6c8c137424fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个表格已生成并注册。

**数字修正（以 registry 为准）：**

| 字段 | 任务指定 | Registry 实际 | 采用 |
|------|---------|--------------|------|
| Pythia-1B F1 | 0.855 | 0.856 | 0.856 |
| OLMo-2-1B F1 | 0.762 | 0.764 | 0.764 |
| Qwen3-1.7B F1 | 0.809 | 0.805 | 0.805 |
| Qwen3-0.6B F1 | 0.823 | 0.824 | 0.824 |
| Qwen3-8B F1 | 0.6849 | 0.683 | 0.683 |
| 6-gen Avg | 0.790 | 0.789 | 0.789 |
| hapax importance | 0.265 | 0.269 | 0.269 |
| entropy_mean importance | 0.152 | 0.164 | 0.164 |
| ttr importance | 0.148 | 0.159 | 0.159 |

文件路径：
- `artifacts/_project/paper/table1.tex` — LOGO 分类结果
- `artifacts/_project/paper/table2.tex` — 特征消融
- `artifacts/_project/paper/table3.tex` — 下游 CLM（负面结果）
- `artifacts/_project/paper/table4.tex` — 跨家族参考模型验证

---
