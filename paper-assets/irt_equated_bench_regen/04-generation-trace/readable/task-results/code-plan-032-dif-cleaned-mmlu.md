# code plan 032 dif cleaned mmlu

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_032_dif_cleaned_mmlu_20260521T133436_result.json`
- **Structured JSON:** [`d61ecf0a0ceff4c8f583.json`](../../sessions/d6/d61ecf0a0ceff4c8f583.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功。关键结果：

**数据很有力——直接回应 "ρ=0.997 undermines urgency"：**

- **全局 ρ = 0.9965** 确实很高，但局部排名变化剧烈
- **89.5% 模型** 排名变化 ≥5 位，**24.8%** 变化 ≥100 位
- 最大变化：-589（上升）到 +849（下降）
- **Top-100 中 18% 排名变化 ≥10 位**，Top-500 中 47.2%

**系统性 cohort 偏差——关键发现：**
- 2023 模型平均排名**改善 22.6 位**（中位 -5）
- 2024 模型平均排名**下降 73.6 位**（中位 +11）
- 说明 DIF items 系统性地有利于 2024 模型

**Family 层面：**
- Mistral 系列清洗后平均**上升 53 位**
- Phi-3 平均**下降 258 位**，Llama-3 **下降 121 位**，Solar **下降 149 位**

**Subject 层面：**
- Business Ethics (48.4% C-flagged)、Human Aging (41.9%)、Formal Logic (40.4%) DIF 浓度最高
- 被移除的 C items 平均更难（difficulty 0.409 vs 0.460）

输出文件已保存在 `artifacts/plan_032_dif_cleaned_mmlu/`：
- `cleaned_mmlu_analysis.csv` — 5227 模型的完整排名对比
- `per_subject_dif_concentration.csv` — 57 个 subject 的 DIF 浓度
- `plan_032_report.md` — 完整分析报告

---
