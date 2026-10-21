# code d144 llama fix and train

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d144-llama-fix-and-train_20260519T135439_result.json`
- **Structured JSON:** [`a1a3cfde5306b2024d0e.json`](../../sessions/a1/a1a3cfde5306b2024d0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

| 项目 | 结果 |
|------|------|
| 模型验证 | **3.21B params**，两个 shard 正常加载 |
| 磁盘 | 199G 可用（21% 使用） |
| Dry-run | Step 1 成功（parse_rate=1.0），保存到 /tmp 时根分区满（不影响正式训练） |
| 训练提交 | tmux `d144-llama-exec-s42`，PID=398743，GPU 0 占用 20248 MiB |
| Step 1 日志 | reward=0.0000, prove_rate=0.000, isr=0.000, parse_rate=1.000 |
| 预估时长 | ~3h（21.6s/step × 500 steps） |
| 异常 | 修复了 chat_template 缺失（base LLaMA 3.2 无模板，已注入标准 LLaMA 3 模板）；修复了 wandb auth 问题（显式 `--no_wandb`） |

---
