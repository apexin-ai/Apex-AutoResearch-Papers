# code generate corrections

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_generate-corrections_20260512T131022_result.json`
- **Structured JSON:** [`9dfffa7a90d2186638be.json`](../../sessions/9d/9dfffa7a90d2186638be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**文件**: `/root/autodl-tmp/error_diag_dpo_recovery/src/generate_corrections.py` (12,077 bytes)

**--help 输出正常**，所有 CLI 参数符合要求。

**设计要点**:
- **简化方案**：Qwen3-14B-AWQ 从头完成整个任务（不做 replay+续写），成功即为 chosen
- **多轮尝试**：每轮遍历整个 ALFWorld env，只对未成功的 target game_file 尝试纠正。最多 `max_attempts` 轮
- **AWQ 加载**：直接 `from_pretrained` + `device_map`，无需 BitsAndBytesConfig
- **复用函数**：从 `collect_trajectories.py` 导入 `get_task_type`, `process_ob`, `load_prompt_resources`, `build_initial_messages`, `parse_action`
- **DPO pair 构建**：`find_shared_prefix_len` 分离 prompt/continuation，与 `construct_preference.py` 逻辑一致

---
