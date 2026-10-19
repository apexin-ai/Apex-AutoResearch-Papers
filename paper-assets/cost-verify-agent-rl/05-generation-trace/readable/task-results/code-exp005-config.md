# code exp005 config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp005_config_20260513T230226_result.json`
- **Structured JSON:** [`c06051e402b539a04bd7.json`](../../sessions/c0/c06051e402b539a04bd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

YAML 验证通过。

**exp005_fast vs exp003 差异：**

| 参数 | exp003 | exp005_fast |
|------|--------|-------------|
| `experiment_name` | `exp003-alfworld-selfguide-prompt-trunc` | `exp005-alfworld-fast` |
| `total_training_steps` | 100 | **30** |
| `local_log_dir` | `exp_003/` | `exp_005/` |
| `agent_proxy.max_turn` | 50 | **30** |
| `es_manager.train.env_groups` | 16 | **8** |
| `es_manager.train.n_groups` | [16] | [8] |

其余参数（model path, lr, max_prompt_length=4096, max_response_length=1024, max_model_len=8192, group_size=8, val 配置等）均保持不变。

预期加速效果：`env_groups` 减半（traj/step 128→64）+ `max_turn` 降低 40%，每步耗时预计降至 ~25-40 min，30 步总计 ~12-20h。

---
