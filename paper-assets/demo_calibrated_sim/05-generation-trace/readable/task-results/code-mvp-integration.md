# code mvp integration

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-integration_20260512T102314_result.json`
- **Structured JSON:** [`e4bead3a9bd99b3a23be.json`](../../sessions/e4/e4bead3a9bd99b3a23be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已写入 `artifacts/code/`，验证通过：

- **`h_gate_evaluator.py`** — `HGateEvaluator` 类，支持 H1/H2/H3 三级 gate 评估，所有阈值可配置（`h1_question_rate_threshold=0.15`, `h1_politeness_rate_threshold=0.30`, `h2_relative_improvement_threshold=0.30`, `h3_retention_ratio=0.80`）。提供 `evaluate_all()` 一键评估 + `to_dict()` 序列化。

- **`run_mvp_experiment.py`** — 主实验脚本，流程：启动 vLLM → monkey-patch τ-Bench `LLMUserSimulationEnv.build_system_prompt` → 跑 uncalibrated baseline → 跑 BCP variants → 提取行为指纹 → H-gate 评估 → 输出 `mvp_results.json`。支持 `--skip-vllm`（已有服务时跳过启动）、`--variants` 选择性运行、完整 argparse 参数。trace 提取兼容 τ-Bench 的 object 和 dict 两种结果格式。

---
