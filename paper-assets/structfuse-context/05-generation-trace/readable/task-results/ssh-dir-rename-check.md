# ssh dir rename check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_dir_rename_check_20260513T184355_result.json`
- **Structured JSON:** [`9ece391b493fd09c9469.json`](../../sessions/9e/9ece391b493fd09c9469.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果明确：

**数据构建状态**：`/tmp/build_starcoder_m2.log` 不存在。StarCoder 数据构建已集成在 `run_m2_full_starcoder.sh` 的 Phase 1 中，不单独产出该日志文件。训练已在运行中。

**重命名安全检查**：两个 wrapper 脚本均硬编码了 `/root/structfuse` 路径：
- `run_m2_full_qwen.sh`: `TRAIN_SCRIPT="/root/structfuse/training/train.py"`
- `run_m2_full_starcoder.sh`: `PROJECT_ROOT="/root/structfuse"`，后续引用 `${PROJECT_ROOT}/training/train.py` 和 `${PROJECT_ROOT}/scripts/build_m1_training_data.py`

**结论**：训练 wrapper 脚本持有 `/root/structfuse` 路径引用，重命名会中断后续 runs。等全部 18 runs 完成后再重命名。

---
