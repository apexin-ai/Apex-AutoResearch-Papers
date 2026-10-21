# code episode collection reuse adapter

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_episode-collection-reuse-adapter_20260513T205644_result.json`
- **Structured JSON:** [`0113b35e0937a7ab58f0.json`](../../sessions/01/0113b35e0937a7ab58f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部功能正常。总结修改：

**新增功能：**

1. **`--reuse_dirs`** — 逗号分隔的目录列表，自动扫描已有 `episodes.jsonl`，按 task name 匹配（支持 `-`/`_`/大小写模糊匹配）。已有 ≥ target 的 task 自动 SKIP，不足的只补差额，`start_episode` 从已有数量开始编号。

2. **`--task_list`** — `--task_types` 的别名，两者任选其一。

3. **`--dry_run`** — 只扫描 reuse 目录并报告计划，不启动 GPU 推理。

4. **`collection_meta.json`** — 每个 task 输出目录下写入元数据，记录 reuse 来源和新收集数量。

5. **`copy_reused_episodes()`** — 将 reuse 源的 episodes.jsonl 拷贝到输出目录的 `episodes.jsonl`。

6. **跳过 agent 初始化优化** — 如果所有 task 都已有足够数据，不会初始化 LLMAgent（省去 GPU 加载）。

**未改变：** 原有参数默认行为、`run_task_collection` 核心逻辑、输出文件格式（`labeled_steps.jsonl` + `episode_summary.jsonl`）。

---
