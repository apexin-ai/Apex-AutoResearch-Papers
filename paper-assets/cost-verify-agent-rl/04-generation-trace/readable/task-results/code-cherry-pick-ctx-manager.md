# code cherry pick ctx manager

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cherry_pick_ctx_manager_20260515T083451_result.json`
- **Structured JSON:** [`38718e798f03f11ff31d.json`](../../sessions/38/38718e798f03f11ff31d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成总结

### 改动清单

**1. `es_manager.py`** — 添加 `anchor_obs` 字段
- 在 `_update_cache_history()` 中，每个 history entry 新增 `anchor_obs`（原始环境观测文本），供下游 GiGPO 使用

**2. `ctx_manager.py`** — 添加 `step_independent` 模式（5处修改）
- **训练 dispatch** (`get_lm_inputs`): 添加 `step_independent` 分支 → `_build_step_independent_samples()`
- **推理 context window** (`_build_infer_samples`): `step_independent` 使用 `step_independent_history_length`（默认5）做 bounded history 截断
- **推理 dispatch**: 添加 `step_independent` 分支 → `_build_infer_step_independent_messages()`
- **`_build_step_independent_samples()`**: 每步生成独立 (prompt, response) 对，context 有界，输出包含 `anchor_obs`
- **`_build_infer_step_independent_messages()`**: 推理时用同样的 bounded history 构建 prompt

### 配置参数

```yaml
agent_proxy:
  context_window_mode: "step_independent"
  step_independent_history_length: 5  # 包含最近N步历史，默认5
```

### 测试结果

| 指标 | full 模式 | step_independent |
|------|-----------|-----------------|
| 样本数 | 2（每episode 1个） | 10（每step 1个） |
| 序列长度 | 626 tokens | 330 tokens |
| anchor_obs | 无 | 有 |
| 有界历史 | 否 | 是（3步测试验证通过） |

现有模式（`full`、`single_turn`、`limited_multi_turn`）的逻辑未被改动。

---
