# data metabench explore v2

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_metabench_explore_v2_20260520T194355_result.json`
- **Structured JSON:** [`350c4eaaa151001eec42.json`](../../sessions/35/350c4eaaa151001eec42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。三个关键问题的答案：

### 1. 能否分出 N≥80 的 cohort？
**可以，但只有 2 个年度 cohort**：2023 (N=1,253) 和 2024 (N=658)。63% 的模型无法从名称分类（社区微调/merge），粗粒度 2-cohort 分组可行，细粒度需要 HF Hub 外部元数据。

### 2. 有没有 RL-trained 模型？
**有，477 个**名称含显式 RL 信号：DPO(346), ORPO(52), PPO(11), KTO(6)。大量隐式 RLHF 模型（Llama-3, Qwen-2 等）名称不含标记但实际用了 RL。足够做污染检测 validation。

### 3. RDS 有没有已拟合的 IRT 参数？
**有。** `mmlu-preproc.rds` 包含 12,508 items 的 2PL 参数（difficulty + discrimination），5219×12508 完整响应矩阵，以及 4755/464 train/test split。**可直接使用，无需自行拟合 IRT。**

### 产出文件
- `metabench_irt_params.csv` — 12,508 items IRT 参数
- `metabench_data_summary.md` — 完整数据探索报告
- `metabench_model_accuracy.csv` — 5,219 模型准确率
- `metabench_rl_models.csv` — 477 个 RL 模型清单
- `metabench_cohort_analysis.csv` — cohort 分析
- `metabench_summary.json` — 机器可读汇总
- `metabench_explore.py` — 探索脚本（内存优化版）

---
