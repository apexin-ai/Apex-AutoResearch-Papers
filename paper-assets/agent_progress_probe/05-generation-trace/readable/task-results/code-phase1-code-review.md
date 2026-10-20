# code phase1 code review

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase1_code_review_20260514T062729_result.json`
- **Structured JSON:** [`c72e8a170701a0675d5c.json`](../../sessions/c7/c72e8a170701a0675d5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成。最终审查结果：

## 兼容性审查总结

| 文件 | 状态 | 修复内容 |
|------|------|----------|
| `generate_embeddings.py` | **已修复** | ① `build_trajectory_index` 改为 `(steps_index, meta_index)` 双返回，按 row_index 索引，消除重复 key 覆盖 ② 添加 `parse_row_index` 从 trajectory_id 提取 row_index ③ instance_id 从 meta_index 获取而非从 window dict 读取 ④ 添加 ABSTAIN 窗口过滤 |
| `evaluate.py` | **已修复** | ① `build_trajectory_index` 改为按 row_index 索引 ② `build_baseline_data` 不再依赖 window_index，直接从 embeddings.pt 的 `trajectory_ids` + `step_indices_list` 获取所有数据 ③ 移除已不需要的 `--windows` 参数 |
| `probe_model.py` | **OK** | `split_by_instance` 按 instance_id 分组，instance_id 来自 embeddings.pt（由上游正确填充）。同一 issue 的不同 run 分到同一组，防止泄漏 |
| `train_probe.py` | **OK** | 只读 `embeddings`/`labels`/`instance_ids`/`embed_dim`，均存在于新格式的 embeddings.pt |
| `baselines.py` | **OK** | 不涉及 trajectory_id 或 instance_id |

### 数据泄漏防护确认

`split_by_instance` 用原始 `instance_id`（如 `django__django-12345`）分组。同一 issue 的多次 run（`__r0`, `__r1` 等）会被分到同一 split。

---
