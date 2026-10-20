# infra install tmux

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_install-tmux_20260520T071036_result.json`
- **Structured JSON:** [`19700565a96bc0550150.json`](../../sessions/19/19700565a96bc0550150.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**tmux 安装** — 成功，版本 `tmux 3.2a`。`screen` 也可用（`/usr/bin/screen`）。

**`--seed` 参数** — `finetune.py` 的 `FinetuneConfig` **没有 seed 字段**，`--help` 中不存在 `--seed`，代码中也没有调用 `set_global_seed`。

对比之下，`deploy.py` 的 config 有 `seed: int = 7`，而 `prismatic/util/torch_utils.py` 提供了完整的 `set_global_seed()` 函数，finetune 脚本只是没接入。

**控制随机种子的方案：** 在 `FinetuneConfig` 中添加 `seed` 字段，然后在 finetune 的训练入口处调用 `set_global_seed(cfg.seed)`。具体改两处：

1. `FinetuneConfig` 加字段：`seed: int = 7`
2. finetune 的 `main()` 函数开头加：`from prismatic.util import set_global_seed; set_global_seed(cfg.seed, get_worker_init_fn=True)`

需要我直接改代码吗？

---
