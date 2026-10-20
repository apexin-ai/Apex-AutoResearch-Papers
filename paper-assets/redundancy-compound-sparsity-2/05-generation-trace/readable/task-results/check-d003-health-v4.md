# check d003 health v4

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d003_health_v4_20260512T143136_result.json`
- **Structured JSON:** [`f79240847dd1fd8d6b15.json`](../../sessions/f7/f79240847dd1fd8d6b15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

## D003 实验状态

### 两个进程均存活，正在运行

| 实验 | PID | 脚本 | GPU | VRAM 占用 | GPU 利用率 |
|------|-----|------|-----|-----------|-----------|
| EXP1: d003_reasoning_traces | 28311 | `d003_reasoning_traces.py` | GPU 0 | 29234 MiB / 97887 MiB | 93% |
| EXP2: d003_wikitext_32k | 28390 | `d003_wikitext_32k.py` | GPU 1 | 35550 MiB / 97887 MiB | 95% |

两个进程均在 22:29 启动，CPU 占用分别 108% 和 97.5%，状态 `Rl`（running）。

### tmux sessions

- `d003_reasoning_traces` → GPU 0, `CUDA_VISIBLE_DEVICES=0`
- `d003_wikitext_32k` → GPU 1, `CUDA_VISIBLE_DEVICES=1`

exit 文件目录中**无** `d003_reasoning_traces.exit` 或 `d003_wikitext_32k.exit`，说明两个进程都没退出过。

### 日志进度

**EXP1 (reasoning_traces):**
- 模型已加载完成（DeepSeek-R1-Distill-Qwen-14B, 48 layers）
- 正在生成 reasoning traces：`3/20 [01:57<11:10, 39.41s/it]` — 完成 15%，预计还需 ~11 分钟
- 有 SyntaxWarning（LaTeX 字符串转义），不影响运行

**EXP2 (wikitext_32k):**
- 模型已加载，WikiText-2 数据已加载（32768 tokens, prefill=26214, eval=6554）
- 正在跑 `full` 策略的 eval 阶段：`3520/6554 [02:04<01:49, 27.71it/s]` — 完成 54%，预计还需 ~1:49
- 有 `trust_remote_code` 和 token 长度警告，不影响运行

### 版本判断

两个实验都是 22:29 刚启动的，模型路径 `/root/carc/models/DeepSeek-R1-Distill-Qwen-14B`，输出路径分别为 `d003_reasoning_results.json` 和 `d003_wikitext32k_results.json`。从启动时间和正常运行状态看，这是最新启动的版本，不是崩溃残留。

---
