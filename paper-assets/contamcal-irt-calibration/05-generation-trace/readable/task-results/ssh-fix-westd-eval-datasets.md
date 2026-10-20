# ssh fix westd eval datasets

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-westd-eval-datasets_20260518T222630_result.json`
- **Structured JSON:** [`af2951763aa2cfe097ee.json`](../../sessions/af/af2951763aa2cfe097ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复成功。

**结果**：
- cuda:2 已占用 17.7GB（模型正在加载/推理中）
- eval_batch1 tmux session 运行正常，所有 57 个 MMLU subtask + ARC-Challenge 数据离线加载成功
- 第一个 adapter `Qwen2.5-7B_d000_s42` 正在评测

**修复内容**：
1. 从 `all/` parquet 拆分出 57 个 per-subject 目录到 MMLU snapshot 路径
2. 修改所有 lm_eval MMLU task YAML 的 `dataset_path` 从 `cais/mmlu` → 本地 snapshot 路径
3. 修改 ARC task YAML 的 `dataset_path` 从 `allenai/ai2_arc` → 本地 snapshot 路径
4. eval 脚本中添加 `HF_HUB_OFFLINE=1`、`HF_DATASETS_OFFLINE=1`、`TRANSFORMERS_OFFLINE=1`
5. batch2 脚本也同步修复（等 cuda:0 空闲时可用）

---
