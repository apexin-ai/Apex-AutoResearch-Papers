# code eval script

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-script_20260514T070556_result.json`
- **Structured JSON:** [`a1fb013645cb3088057e.json`](../../sessions/a1/a1fb013645cb3088057e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是汇报：

### 1. 实现概要

| 模块 | 实现方式 |
|------|----------|
| **模型加载** | `ModelInference` 类：transformers 加载 Qwen3-8B（bfloat16），可选 PEFT `PeftModel.from_pretrained` 加载 LoRA adapter 并 `merge_and_unload`。`adapter_path=None` 时为 zero-shot 模式 |
| **ALFWorld 环境** | `collect_game_files()` 遍历 `valid_unseen/` 下所有 task 目录，每个 task 取第一个 solvable trial。环境用 `textworld.gym.register_games` + `AlfredDemangler`/`AlfredInfos` |
| **评测循环** | `run_episode()` 逐步推理，`--inject` 模式下在 `injection_step`（随机 2~6）处对历史应用 operator 注入一次。4 个 operator 按 round-robin 分配给 episode，保证均匀 |
| **Prompt 格式** | `build_prompt()` 与 `collect_trajectories.py` 完全一致（`&lt;think>`/`&lt;action>` tags），Qwen3 的 `enable_thinking=True` 保持一致 |
| **统计检验** | McNemar test（连续性修正 chi2）+ Bootstrap 95% CI（10000 次重采样），通过 `--compare_with` 对比两份结果 |
| **输出报告** | JSON 格式包含 overall success rate、per-operator recovery rate、per-task-type breakdown、逐 episode 详情 |
| **CLI** | 符合规格要求，支持 `--inject`/`--no_inject`、`--model_path`（LoRA）、`--compare_with`（统计对比） |

### 2. 依赖安装情况

全部已安装，无需额外安装：
- scipy 1.17.1, peft 0.19.0, transformers 4.57.6, numpy 2.2.6, torch 2.11.0+cu130, alfworld, textworld

### 3. 语法检查

`py_compile` 通过，`--help` 正常输出。

### 4. 设计决策

- **注入时机**：仅在 step ≥ injection_step 且 history ≥ 2 条时注入一次（不重复注入），确保有足够历史可供 operator 操作
- **Operator 分配**：round-robin（`i % 4`）保证 4 个 operator 在 134 个 episode 上均匀分布（约 33-34 个/operator）
- **对比模式**：独立于 eval 模式，通过 `--compare_with` 加载已有两份 JSON 按 task_name 对齐做 paired test，避免重复跑 eval
- **merge_and_unload**：LoRA 加载后立即合并权重，推理时无额外开销

---
