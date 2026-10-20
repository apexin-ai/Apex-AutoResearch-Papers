# code plan 004 status check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-004-status-check_20260513T233305_result.json`
- **Structured JSON:** [`9f07f5ad175c06805eef.json`](../../sessions/9f/9f07f5ad175c06805eef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完毕。汇总如下：

---

## Plan-004 Ablation Framework 完成度报告

### 文件存在性 & 行数

| 文件 | 行数 | 状态 |
|------|------|------|
| `ablation_eval_common.py` | 327 | 存在 |
| `ablation_data_converter.py` | 146 | 存在 |
| `ablation_implicit_1_7b.py` | 348 | 存在 |
| `ablation_implicit_7b.py` | 223 | 存在 |

### Import & CLI

- 4 个文件 **import 全部 OK**，无报错
- 3 个可执行文件 **--help 全部正常**（converter / implicit_1_7b / implicit_7b）

### 功能完成度

**ablation_eval_common.py (327行) — 完整**
- 3 个 dataclass: `EvalConfig`, `StepRecord`, `EpisodeResult`
- 核心函数: `load_oracle_labels`, `run_routed_episode`, `compute_routing_accuracy`, `compute_episode_metrics`, `run_ablation_eval`, `add_eval_args`, `config_from_args`
- `RouterFn` 协议已定义：`(obs, valid_actions, history) → (action, route)`

**ablation_data_converter.py (146行) — 完整**
- `format_action_history`, `convert_triple_to_chat`, `convert_file`, `main`
- 默认路径对齐 `results/sft_data_death_aware/sft_triples.jsonl`，与 `router_sft_train.py` 一致

**ablation_implicit_1_7b.py (348行) — 完整**
- Dataset: `ImplicitSFTDataset` (chat template tokenization, prompt masking)
- Train: `train()` 含 LoRA 配置 (r/alpha/dropout, q/k/v/o_proj)
- Router: `Implicit1_7BRouter.__call__` 实现 RouterFn 协议
- Eval: `evaluate()` 调用 `run_ablation_eval`
- CLI: `{train,eval}` 子命令
- Parser: `parse_implicit_output` 处理 `[SIMULATE]` 前缀

**ablation_implicit_7b.py (223行) — 完整**
- Router: `Implicit7BRouter` (vLLM/HF 双后端)
- Parser: `parse_tool_use_output` + `_snap_to_valid` 模糊匹配
- CLI: 直接评估模式（无训练，7B 用预训练权重）

### 遗留 TODO（2 处，非阻塞）

1. **`ablation_eval_common.py:143`** — `fork_and_lookahead` 分支未接入，当前 deterministic route 直接用 router 选的 action，未做多候选 fork 评估。注释写了 "For now, use the router-chosen action as-is"。**非阻塞**：ablation 实验关注的是 routing 准确率对比，不依赖 lookahead 优化。

2. **`ablation_implicit_1_7b.py:166`** — `custom data collator for variable-length padding` 未实现。当前用 HF Trainer 默认 collator。**非阻塞**：默认 collator 可运行，只是 padding 效率略低。

### FIXME / NotImplementedError

无。所有 4 个文件均无 FIXME 和 NotImplementedError。

### 数据对齐

`ablation_data_converter.py` 读取 `sft_triples.jsonl`（与 `router_sft_train.py` 共用同一数据源），转换为 implicit chat 格式。路径一致。

### 结论

4 个文件全部 **完整可用**，非骨架代码。2 个 TODO 均为优化项，不阻塞 ablation 实验执行。**不需要额外 Worker 修复**，可直接进入数据转换 → 训练 → 评估流程。

---
