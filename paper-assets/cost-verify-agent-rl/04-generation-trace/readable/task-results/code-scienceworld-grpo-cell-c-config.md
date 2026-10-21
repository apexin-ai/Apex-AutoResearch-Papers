# code scienceworld grpo cell c config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scienceworld_grpo_cell_c_config_20260520T063221_result.json`
- **Structured JSON:** [`d13d45ed0a7c2291a627.json`](../../sessions/d1/d13d45ed0a7c2291a627.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Cell C 配置文件 `_scienceworld_cell_c_grpo.yaml` 已创建并验证。

与 Cell A 的 diff 精确为 4 处变更：
1. **注释头** — Cell A 描述 → Cell C 描述
2. **`experiment_name`** — `scienceworld-cell-a-h2` → `scienceworld-cell-c-episode`
3. **`local_log_dir` / `default_local_dir`** — `scienceworld-cell-a/` → `scienceworld-cell-c/`
4. **`context_window_mode`** — `"step_independent"` → `"full"`

其余所有参数（model_path, lr, kl_coeff, gamma, response_length, env tags, batch sizes 等）与 Cell A 完全一致。YAML 解析和 Hydra compose 均通过。

---
