# code grpo argparse fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo-argparse-fix_20260513T193518_result.json`
- **Structured JSON:** [`f2e24a624fcf446b70cf.json`](../../sessions/f2/f2e24a624fcf446b70cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

argparse 修复成功——脚本顺利通过了参数解析、加载数据、初始化 solver、构建 trainer 并开始训练。报的是 CUDA OOM（GPU 显存被其他进程占用了 63.97 GiB），这不是 argparse 问题。

修复完成：

1. **`train_grpo.py`**：`--model_path`, `--data_path`, `--reward_mode`, `--output_dir` 改为 `default=None`；YAML 加载时只填充 CLI 未提供的参数（CLI 优先）；加载后检查 4 个必要参数是否齐全
2. **`grpo_exec_only.yaml` / `grpo_exec_sta.yaml`**：补充了 `model_path` 和 `data_path`
3. **已清理**旧的失败输出目录
4. **Dry-run 验证**：argparse 不再报错，脚本成功进入训练循环。当前报 CUDA OOM 是因为 GPU 0 被另一个进程占用了 ~64GB 显存，需要释放后重新运行

---
