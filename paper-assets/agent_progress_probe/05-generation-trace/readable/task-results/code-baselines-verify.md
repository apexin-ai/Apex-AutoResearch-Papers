# code baselines verify

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baselines_verify_20260514T071724_result.json`
- **Structured JSON:** [`968fa4f20d8ea5060062.json`](../../sessions/96/968fa4f20d8ea5060062.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证报告

### Baselines 状态

| Baseline | 状态 | 说明 |
|---|---|---|
| RandomBaseline | **OK** | 从训练集学习正类比例，用固定 seed 生成随机预测 |
| MajorityBaseline | **OK** | 从训练集学习多数类 |
| CosineSimilarityBaseline | **OK** | 在 val set 上扫描阈值，正确处理 seq_len < 2 边界 |
| Repeat3Baseline | **OK** | extract_command 正则与 data_loader.py 的 Step.command 一致 |

### evaluate.py 兼容性

| 检查项 | 状态 |
|---|---|
| embeddings.pt 字段访问 (embeddings/labels/trajectory_ids/step_indices_list) | **OK** |
| step_indices 与 trajectory index 的 0-based 编号一致性 | **OK** |
| build_baseline_data 输出格式与 baselines 期望一致 | **OK** |
| probe 使用与 train_probe.py 相同的 split | **OK**（同一 split_info.json）|

### 已修复的 Bug

**`--min_confidence` 过滤不一致**：`train_probe.py` 用 `--min_confidence > 0` 时会先过滤低置信度窗口再 split，保存的 split indices 是相对于过滤后列表的。`evaluate.py` 加载完整 embeddings.pt 后直接用这些 indices，导致索引错位。

修复：
- `train_probe.py`：在 split_info.json 中新增 `min_confidence` 和 `keep_indices` 字段
- `evaluate.py`：加载 split_info 后检查 `keep_indices`，若存在则先对 data 做相同过滤再使用 split indices

---
