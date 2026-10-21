# ssh d163 qwen eval config

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d163-qwen-eval-config_20260521T142738_result.json`
- **Structured JSON:** [`ad389ff7a3aad2f4625d.json`](../../sessions/ad/ad389ff7a3aad2f4625d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认完毕。汇总：

---

## D163 确认结果

### 1. Eval 脚本配置

| 项目 | s123 | s456 |
|------|------|------|
| GPU 默认值 | `${1:-0}` ✅ | `${1:-3}` ✅ |
| batch_size 默认值 | ~~`${2:-1}`~~ → **已修复为 `${2:-4}`** | ~~`${2:-1}`~~ → **已修复为 `${2:-4}`** |
| checkpoint 选取 | `awk -F'checkpoint-'` ✅ | `awk -F'checkpoint-'` ✅ |

### 2. Thinking 模式

`eval_repo_cwm.py` 第 56/58 行：`enable_thinking=False` ✅，无需修改。

### 3. 输出目录

`qwen3_8b_cwm_s123_eval/` 和 `qwen3_8b_cwm_s456_eval/` 均不存在，无旧结果冲突 ✅

### 4. Watch 脚本

`watch_qwen_train_then_eval.sh` 存在，batch_size 默认也是 1（但按指示不启动它，通过 cron 手动触发 eval）。

### 5. 训练进度

| 训练任务 | 当前 step | 总 step | 进度 | 速度 | 预计剩余 |
|---------|-----------|---------|------|------|---------|
| s123 (GPU 0) | 5576 | 6633 | **84%** | ~12s/it | ~3.5h |
| s456 (GPU 3) | 4694/9335 (数据预处理阶段) | — | **50% preprocessing** | ~9 it/s | ~8min 预处理后开始训练 |

s456 日志当前显示的是数据 tokenization 进度条（9335 samples，与 s123 的 data loading bar 相同），尚未进入训练循环。

---
