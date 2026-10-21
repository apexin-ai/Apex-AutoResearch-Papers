# code scienceworld grpo configs

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scienceworld_grpo_configs_20260520T062943_result.json`
- **Structured JSON:** [`f97d75ed593ca748f488.json`](../../sessions/f9/f97d75ed593ca748f488.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**结果：**
1. **envs.yaml** — 已追加 `ScienceWorldSG` 条目（30 个任务，score=10.0，max_steps=100）
2. **_scienceworld_cell_a_grpo.yaml** — 已创建，与 ALFWorld Cell A (`_alfworld_hsweep_h2.yaml`) 严格控制变量，仅改 model_path、env tag、max_turn (50→100)、response_length (1024→512)

Hydra config 加载成功，参数确认正确。Hydra 的 `_self_` 警告是无害的（ALFWorld configs 也一样）。

---
