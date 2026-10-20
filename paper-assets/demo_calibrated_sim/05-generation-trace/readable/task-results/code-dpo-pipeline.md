# code dpo pipeline

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dpo-pipeline_20260512T123336_result.json`
- **Structured JSON:** [`ef3ecdc7ca020b1b921d.json`](../../sessions/ef/ef3ecdc7ca020b1b921d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个脚本已写入 `artifacts/code/`：

**`generate_synthetic_corpus.py`** — 通过 monkey-patch τ-Bench `LLMUserSimulationEnv.build_system_prompt` 注入 AAVE/Indian English dialect prompt（含目标 question_rate 10%、politeness_rate 20%），运行 τ-Bench retail dev split 收集 trace，过滤不完整对话，输出带 behavioral_stats 的 JSON。与 `run_mvp_experiment.py` 使用完全相同的集成方式（RunConfig + monkey-patch）。

**`build_dpo_pairs.py`** — 按 task_id 对齐校准/未校准 trace，在每个 user turn 位置构建 DPO pair（calibrated=chosen, uncalibrated=rejected）。支持多 trial 交叉配对增强数据量。过滤 `###STOP###`、相同响应和过短 turn。兼容两种输入格式（corpus JSON 和 raw tau-bench checkpoint）。

**`train_dpo.py`** — TRL `DPOTrainer` + PEFT LoRA 微调 Qwen 2.5 7B。LoRA rank=64, alpha=128, target 全部 attention+MLP projections。DPO beta=0.1 sigmoid loss, bf16 + gradient checkpointing + flash_attention_2。支持 W&B logging，训练结束保存 LoRA adapter。

---
