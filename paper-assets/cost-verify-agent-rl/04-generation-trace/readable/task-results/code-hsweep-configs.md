# code hsweep configs

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hsweep_configs_20260517T002851_result.json`
- **Structured JSON:** [`6c881b5cd1e38afc79eb.json`](../../sessions/6c/6c881b5cd1e38afc79eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个 config 全部验证通过。

**关键差异参数汇总**：

| 文件 | context_window_mode | context_window_size | total_training_steps | experiment_name |
|------|-------------------|--------------------|--------------------|-----------------|
| `_alfworld_hsweep_h2.yaml` | sliding | 2 | 15 | hsweep-h2-sliding |
| `_alfworld_hsweep_h5.yaml` | sliding | 5 | 15 | hsweep-h5-sliding |
| `_alfworld_hsweep_h10.yaml` | sliding | 10 | 15 | hsweep-h10-sliding |
| `_alfworld_hsweep_h20.yaml` | sliding | 20 | 15 | hsweep-h20-sliding |
| `_alfworld_hsweep_full.yaml` | full | (无) | 15 | hsweep-full |

所有其他参数与 exp029 完全一致（ppo_mini_batch_size=16, optimizer_offload=True, max_model_len=20480, gpu_memory_utilization=0.35 等）。每个文件的 checkpoint 路径分别指向 `/root/autodl-tmp/checkpoints/hsweep_{h2,h5,h10,h20,full}/`。

---
