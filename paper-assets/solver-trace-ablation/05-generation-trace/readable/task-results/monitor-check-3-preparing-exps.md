# monitor check 3 preparing exps

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_check-3-preparing-exps_20260513T223633_result.json`
- **Structured JSON:** [`cf9fc6df3af346e44fcc.json`](../../sessions/cf/cf9fc6df3af346e44fcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 训练数据
`data/train_500_seed42.jsonl` — 存在，500 行 ✓

---

### 1. plan001-exec-only-s42
- **原 PID 83029**: **DEAD** — 参数错误 `--max_steps` 不被识别（脚本用 `--num_steps`），EXIT_CODE=2
- **已重启为 PID 84901**，修正为 `--num_steps 500`，日志 `plan001-exec-only-s42-r2.log`
- 当前状态：**ALIVE**，运行 15 分钟，GPU 0 (91%, 80GB/98GB)
- 进度：**0/500 steps**（仍在第一个 step 的 generation 阶段）
- 另有 `r3` 尝试在 06:42 OOM 崩溃（`torch.OutOfMemoryError`，GPU 0 只剩 30MB free）

### 2. plan005-sta-low-s42
- **原 PID 83106**: **DEAD** — 同样 `--max_steps` 参数错误
- **已重启为 PID 85795**，修正为 `--num_steps 500`，日志 `plan005-sta-low-s42.log`
- 当前状态：**ALIVE**，运行 13 分钟，GPU 1 (90%, 80GB/98GB)
- 进度：**0/500 steps**（仍在第一个 step 的 generation 阶段）

### 3. plan003-eval-exec-only-r5
- **PID 83690**: **DEAD — 正常完成** (EXIT_CODE=0)
- 结果：**32/100 proved (32.0%)**，Mean ISR 0.2055 ± 0.3194
- 按 answer type：true 35.98% ISR, false 17.23%, unknown 9.79%
- 耗时 251.7s，结果保存于 `/root/autodl-tmp/outputs/plan003_eval_exec_only_r5.json`

---

**注意**：plan001 和 plan005 都已运行 13-15 分钟但仍在 step 0。GRPO 首个 step 需要初始化 vLLM + 全量 generation，预计还需几分钟才能看到 step 进度。`r3` 的 OOM 表明 GPU 0 同时跑两个训练会爆显存——当前 r2 和 plan005 分别独占 GPU 0 和 GPU 1，应该没问题。

---
