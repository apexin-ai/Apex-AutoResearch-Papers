# prep exp002 infra

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_exp002_infra_20260521T075051_result.json`
- **Structured JSON:** [`b7cfc796f580fc90d7b3.json`](../../sessions/b7/b7cfc796f580fc90d7b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 项子任务全部完成。汇总：

**数据**：GSM8K (1,319)、ARC-Challenge (1,172)、HellaSwag (10,042) 已下载到 `/root/autodl-tmp/.hf_cache/hub/`。

**采样**：每个 benchmark 200 item 已写入 `data/` 目录：
- GSM8K：按难度均匀分层 (easy/medium/hard/very_hard 各 50)
- ARC：按选项数分层 (4-choice: 193, 3-choice: 4, 5-choice: 3)
- HellaSwag：按 activity_label 分层 (192 个活动类别)

**代码适配清单**（不修改代码，只列需求）：
- `prompt_templates.py`：需新增 GSM8K 生成式模板、支持变长选项 (~2 天)
- `run_experiment.py`：需 benchmark 路由、GSM8K 数值答案提取、新评分逻辑 (~3 天)
- `vllm_runner.py`：`max_tokens` 需可配置 (~0.5 天)
- `generate_design.py`：加 benchmark 因子，改精度/温度级数 (~0.5 天)
- `few_shot.py`：各 benchmark 独立 few-shot (~1.5 天)
- 总计 ~8.5 天

**设计参数**：
- 完全交叉设计：4×4×2×2×6×6×4 = **9,216 conditions**（任务原文 4,608 有算术误差）
- 总推理次数：9,216 × 200 = **1,843,200**
- 预估 GPU 时长：MC benchmarks ~7h + GSM8K ~16-32h = **~23-39 小时**（4 GPU 并行）

报告已写入 `/root/nlp_variance_gtheory/results/analysis/exp002_prep_report.md`。

---
