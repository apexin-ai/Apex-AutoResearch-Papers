# diagnose eval math500 westd failures

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_westd_failures_20260521T134339_result.json`
- **Structured JSON:** [`91e9a2b5900d1dc34662.json`](../../sessions/91/91e9a2b5900d1dc34662.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断信息收集完毕。

## 诊断报告

### 每个实验的状态

| 实验 | GPU | 进度 | 最后时间戳 | 终止方式 |
|------|-----|------|-----------|---------|
| grpo_cka_only_25 | cuda:0 | 205/500 (41%), acc=0.18 | ~21:25 | 日志显式 `Terminated` (SIGTERM) |
| sft_cka_only_25 | cuda:2 | 179/500 (36%), acc=0.2067 | ~21:23 | 日志截断，无错误信息 |
| grpo_random_20 | cuda:1 | 43/500 (9%), acc未知 | ~21:25 | 日志截断，无错误信息 |

### 根因分析

**3 个进程在同一时间窗口（~21:23-21:25）被外部 kill**，不是 OOM/CUDA 错误/磁盘满导致的自然崩溃。证据：

1. grpo_cka_only_25 日志末尾有明确的 `Terminated`（SIGTERM 信号）
2. 三个进程的最后活动时间高度一致，说明是协调性操作
3. 日志中无 Python traceback、无 CUDA error、无 OOM 信息
4. **v2 进程已在运行**：PID 379999（grpo_cka_only_25_v2, GPU 0）和 PID 380074（sft_cka_only_25_v2, GPU 2）已启动约 14 分钟，参数改为 `--max_new_tokens 2048`（原默认值 4096）

**推测原因**：有人（或自动化脚本）认为原始运行太慢，手动终止并用优化参数重启。原始命令未指定 `--max_new_tokens`，默认 4096 导致每个样本生成时间过长：
- grpo_cka_only_25: ~1.4 min/sample → 预计总时长 ~12h
- sft_cka_only_25: ~1.5 min/sample → 预计总时长 ~13h
- grpo_random_20: **~4.3 min/sample → 预计总时长 ~36h**（异常慢）

### 附加风险

**数据盘 `/root/autodl-tmp` 使用率 99%**（610G/619G，仅剩 9.7G）。当前不是直接致死原因，但如果 v2 运行完毕写结果或新实验产生 checkpoint，可能立即磁盘满。

### 当前 GPU 状态

| GPU | 进程 | 说明 |
|-----|------|------|
| 0 | eval_math500 grpo_cka_only_25 **v2** (PID 379999) | 已重启 |
| 1 | **空闲** | grpo_random_20 未被重启 |
| 2 | eval_math500 sft_cka_only_25 **v2** (PID 380074) | 已重启 |
| 3 | eval_gsm8k sft_standard_25 (PID 335301, 5.5h) | 其他实验 |

### 修复建议

1. **grpo_cka_only_25 和 sft_cka_only_25**：v2 已在运行，无需操作，等待完成即可
2. **grpo_random_20**：需手动在 GPU 1 上重启，加 `--max_new_tokens 2048`。但此模型原本就极慢（4.3 min/sample），即使限制 token 数也可能需要 ~18h+，建议确认是否值得跑
3. **数据盘**：清理不需要的 checkpoint 释放空间，防止后续写入失败

---
