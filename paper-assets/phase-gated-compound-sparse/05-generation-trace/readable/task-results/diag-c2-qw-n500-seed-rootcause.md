# diag c2 qw n500 seed rootcause

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_c2_qw_n500-seed-rootcause_20260514T140143_result.json`
- **Structured JSON:** [`8d7804f751c186b91f3d.json`](../../sessions/8d/8d7804f751c186b91f3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结果

### Part A: 重复提交

**GPU 2/3 没有重复进程**，当前各只有 1 个 Qwen profiling 进程。

**GPU 0 有重复**: setup worker 留了一个烟雾测试（PID 129684，output 到 `/tmp/n500_smoke_test`，参数不同），和正式 DeepSeek importance 实验（PID 130124）并存。output dir 不同，无数据污染，但浪费 ~18GB 显存。

三次提交用了三种不同方式（bare bash-c → tmux → screen），说明是不同 worker 分别操作的。

建议 kill 烟雾测试: `kill 129684`

### Part B: Seed

**SEED=42 硬编码在 `run_profiling.py:53`**，没有 `--seed` CLI 参数。所有实验（DeepSeek 和 Qwen）都用同一份代码，seed 完全一致。**不需要重启。**

### 当前进度

- DeepSeek: ~22/500（GPU 0/1）
- Qwen: ~15/500（GPU 2/3）
- 每个脚本有 4 个 sparsity level 串行执行，当前都在第一个 s015

报告已写入 `artifacts/c2_qw_n500_investigation.md`。

---
