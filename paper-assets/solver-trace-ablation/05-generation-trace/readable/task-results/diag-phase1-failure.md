# diag phase1 failure

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_phase1-failure_20260513T193411_result.json`
- **Structured JSON:** [`5e42155c99c697bc36a1.json`](../../sessions/5e/5e42155c99c697bc36a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已自行结束（timeout 30 生效），无需清理。

## 诊断结果

**根因**：`train_grpo.py` 的 `parse_args()` 将 `--model_path`, `--data_path`, `--reward_mode`, `--output_dir` 设为 `required=True`，但 YAML config 在 `main()` 中 argparse 之后才加载。实验管理系统只传 `--config` 参数，argparse 在读取 config 之前就因缺少必需参数报错退出（EXIT_CODE=2）。

**修复内容（已部署到服务器）**：

1. **`scripts/train_grpo.py`**：将 4 个参数从 `required=True` 改为 `default=None`，config 加载逻辑从 `main()` 移到 `parse_args()` 中（先解析 CLI → 合并 YAML → 再校验必需字段）。CLI 参数优先于 YAML。

2. **`configs/grpo_exec_only.yaml` 和 `configs/grpo_exec_sta.yaml`**：补上 `model_path` 和 `data_path` 字段，使只传 `--config` 即可独立运行。

**验证**：修复后 `--config configs/grpo_exec_only.yaml --no_wandb` 成功通过参数解析，进入模型加载阶段（之前同样的调用方式会立即 EXIT_CODE=2）。

---
