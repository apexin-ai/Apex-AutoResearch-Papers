# train install tmux and launch

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_install-tmux-and-launch_20260512T112221_result.json`
- **Structured JSON:** [`a7c7d8030e8b08676a50.json`](../../sessions/a7/a7c7d8030e8b08676a50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两组训练均正常运行。

## 结果报告

| | Group A (baseline) | Group B (conformance + GDPO) |
|---|---|---|
| **PID** | 22127 (子进程 22132) | 22530 (子进程 22535) |
| **GPU** | cuda:0, 32454 MiB, 88% util | cuda:1, 32308 MiB, 94% util |
| **进度** | 1/2790 steps (63.92s/it) | 0/2790 steps (刚启动) |
| **状态** | 正常训练中 | 正常训练中 |

### 修复过程
1. **磁盘满**：`/tmp` 下旧 dry run checkpoint 占 24GB，清理后释放空间，安装了 tmux
2. **HF 网络不通**：配置中 `model_name` 指向 `Qwen/Qwen3.5-9B`（HF hub），改为本地路径 `/root/autodl-tmp/models/Qwen/Qwen3.5-9B`
3. **TRL v0.18 API 变更**：`completions` 参数从 `list[str]` 变为 `list[list[dict]]`（chat 格式），在 `reward_fn` 中加了格式转换，提取 `content` 字段为字符串

### 日志文件
- `/root/autodl-tmp/logs/train_A.log`
- `/root/autodl-tmp/logs/train_B.log`

---
