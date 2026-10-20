# code plan 005 prompt types

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-005-prompt-types_20260515T032444_result.json`
- **Structured JSON:** [`f1d50a99a7a9ed514630.json`](../../sessions/f1/f1d50a99a7a9ed514630.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个任务全部正常运行，模型已加载，正在生成中。

**总结：**

| 任务 | exp_id | GPU | tmux session | 状态 |
|------|--------|-----|-------------|------|
| continuation | plan-005-cont | cuda:1 | plan-005-cont | 运行中 |
| elaboration | plan-005-elab | cuda:2 | plan-005-elab | 运行中 |
| inspired_rewriting | plan-005-rewrite | cuda:3 | plan-005-rewrite | 运行中 |

**脚本变更**：创建了 `generate_chain_prompt.py`，基于原 `generate_chain.py` 扩展：
- 新增 `--prompt-type` 参数（continuation/elaboration/inspired_rewriting）
- elaboration 用 "Please elaborate on..." 模板包裹上一步输出
- inspired_rewriting 用 "Write a new passage inspired by..." 模板
- 输出 jsonl 增加 `prompt_type` 字段
- 输出目录格式：`data/pythia-2.8b-{prompt_type}/`
- 模板化 prompt 使用 256 token 输入窗口（vs continuation 的 128）以保留模板结构

**注意**：`openwebtext_seeds.jsonl` 不存在，使用了现有的 `wiki_seed_1000.jsonl`（995 有效 seeds）。每个任务处理全部 995 seeds × depth 0-4，预计每个任务约 2-3 小时。

---
