# monitor grpo v2 early check

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_grpo-v2-early-check_20260514T114327_result.json`
- **Structured JSON:** [`59729dddfe7dd3c1de9d.json`](../../sessions/59/59729dddfe7dd3c1de9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report 已写入。汇总：

### 1. GRPO v2 训练
- **Step 4/73** (5.5%)，每 step ~10min，预估明早 07:30 完成
- **reward 尚不可知** — logging_steps=5，还需等 ~10min 到 step 5 才有第一条 reward 指标
- 这是第二次启动（18:57），第一次运行（15:14→15:55）已崩溃
- wandb 可能未在第二次运行中正确初始化

### 2. eval-sft-v2-ckpt — ✅ 已完成
- SFT vs Base：debug_accuracy +1.9pp (0.767 vs 0.748)，probe_diagnostic +2.5pp (0.129 vs 0.104)，其余无显著差异
- 提升幅度小，CI 有重叠

### 3. Qwen3-30B-A3B 下载
- **87%** 完成（14/16 文件，50GB），缺 model-00013 和 model-00015
- 最后文件修改在 18:39，距今 ~1h，下载可能已停滞

**建议下一步**：~10min 后再查 GRPO 日志确认 step 5 的 reward_mean；检查 Qwen 下载进程是否存活。

---
