# code d134 analysis script

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d134-analysis-script_20260518T133818_result.json`
- **Structured JSON:** [`c9be9486022336e41f78.json`](../../sessions/c9/c9be9486022336e41f78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并验证可启动：`scripts/d134_analysis.py`

功能：
- 自动发现 `d134_4b_{isr,random}_b01_s{seed}/classify.json`，缺失的跳过并警告
- 输出 per-seed 表（PR, H7, H1, H8, genuine, CI, S-NH）
- 输出 condition-level mean ± std
- 三个统计检验：Fisher exact (H7 domination)、permutation test (genuine rate)、Mann-Whitney U (H7 rate)
- `--output` 写 markdown 文件

默认 `--data_dir /root/autodl-tmp/outputs`，在远程服务器上直接运行即可。本地依赖 pandas/scipy/numpy 已安装；远程服务器大概率已有这些包。

---
