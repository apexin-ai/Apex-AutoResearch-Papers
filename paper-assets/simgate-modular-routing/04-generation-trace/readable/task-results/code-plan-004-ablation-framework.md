# code plan 004 ablation framework

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-004-ablation-framework_20260513T221324_result.json`
- **Structured JSON:** [`cd23f3dc79f3b49a50cc.json`](../../sessions/cd/cd23f3dc79f3b49a50cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个文件已部署到服务器。总结：

| 文件 | 行数 | 功能 |
|------|------|------|
| `ablation_eval_common.py` | 327 | 共享评估框架：`RouterFn` 类型协议、`run_routed_episode()`、oracle 对比、metric 聚合 |
| `ablation_data_converter.py` | 146 | `sft_triples.jsonl` → chat 格式 `implicit_sft.jsonl`，`det-preferred` → `[SIMULATE] action` |
| `ablation_implicit_1_7b.py` | 348 | Condition (b)：Qwen3-1.7B causal LM + LoRA SFT，生成时解析 `[SIMULATE]` 前缀做 routing |
| `ablation_implicit_7b.py` | 223 | Condition (c)：Qwen2.5-7B-Instruct tool-use prompt，`simulate(action=...)` → deterministic |

**模型 ID 确认**：
- `Qwen/Qwen3-1.7B` — Condition (a)(b) 共用
- `Qwen/Qwen2.5-7B-Instruct` — Condition (c)，已有本地模型

**数据路径**：`results/sft_data_death_aware/sft_triples.jsonl` 已存在于服务器

**关键设计点**：
- 三个 condition 共享 `RouterFn` 协议：`(obs, valid_actions, history) → (action, route)`，route ∈ `{"deterministic", "internal"}`
- Condition (a) 直接复用 `router_sft_train.py` 的分类头（已有）
- Condition (b) 训练默认 `--gpu_id 1`，可与 plan-002 并行
- 评估时都对比同一组 oracle labels，输出 routing accuracy + episode score + death rate

---
