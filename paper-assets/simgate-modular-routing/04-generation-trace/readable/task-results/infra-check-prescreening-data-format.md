# infra check prescreening data format

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-prescreening-data-format_20260513T171711_result.json`
- **Structured JSON:** [`fe7749ca7214ce44a13e.json`](../../sessions/fe/fe7749ca7214ce44a13e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

### 1. signal_prescreening.py — **保存 step-level 数据 ✓**

每步保存到 `steps` 数组，字段：
- `step` (步序号)
- `action` (执行的动作)
- `modality` ("internal" 或 "deterministic")
- `score_before`, `score_after`, `score_delta`
- `observation` (截断到 500 字符)
- `llm_output` (截断到 300 字符)

deterministic 模式额外保存：
- `candidates` (候选动作列表)
- `fork_results` (每个候选的 fork 评估结果)
- `chosen_action`, `chosen_score_delta`
- `death_filtered` (致死过滤的动作列表)

episode 级别还保存：`action_history`（完整动作序列）。

**缺失：** 没有保存 `valid_actions`（当步可选动作全集）。

### 2. phase1_signal.py — **保存 step-level 数据 ✓**

结构与 prescreening 完全一致。三种模式（always-internal / always-deterministic / oracle-routing）都保存相同的 step-level 字段。oracle 模式每步额外记录 `routing_choice`（选了 internal 还是 deterministic）。

同样 **缺失 `valid_actions`**。

### 3. 预筛进度

完成 **3 个 task**：
- `chemistry-mix`
- `chemistry-mix-paint-tertiary-color`
- `find-animal`

### 4. GPU1 boil v3 进度

PID 650421 仍在运行，已运行 **54 分钟**。日志显示 vLLM 推理正在正常执行（~1 it/s）。

---
