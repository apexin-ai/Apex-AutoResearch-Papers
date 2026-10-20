# analysis scale validation prep

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scale_validation_prep_20260522T041731_result.json`
- **Structured JSON:** [`69af1b0cb1547d4de6e1.json`](../../sessions/69/69af1b0cb1547d4de6e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

方案已保存到 `artifacts/exp004/data/scale_validation_plan.md`。

**总结：**

- **模型**：Qwen2.5-3B-Instruct + Qwen2.5-72B-Instruct（同系列隔离 scale 变量）
- **代码改动 4 处**：model_paths.py 加映射、vllm_runner.py 参数化 TP、generate_design.py 加 exp004_scale 配置、run_experiment.py 加 --tensor-parallel CLI 参数
- **GPU 时间**：3B ~20min (1卡)，72B ~2.5hr (4卡 TP)
- **主要风险**：磁盘紧张（72B 占 140GB，下载后仅剩 55GB）和 72B 独占 4 卡

---
