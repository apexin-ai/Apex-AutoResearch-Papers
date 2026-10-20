# code fix gsm8k bootstrap bug

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_gsm8k_bootstrap_bug_20260515T222600_result.json`
- **Structured JSON:** [`afd8a7471a28b91ae3ba.json`](../../sessions/af/afd8a7471a28b91ae3ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验的 log 显示先前的运行实际上已完成（输出到 `profiling_output_gsm8k_*`），但新一批（输出到 `gsm8k_profiling/*`）因 bootstrap bug 失败。Bug 已修复。

总结：

**修复内容**: `/root/autodl-tmp/pacs/profiling/interaction_index.py` 中的 `bootstrap_interaction_index` 函数返回 tuple `(mean, ci_low, ci_high)`，但 `run_profiling_gsm8k.py:459` 按 dict key 取值。

**根因**: 项目有两份 `interaction_index.py`：
- `/root/autodl-tmp/pacs/profiling/` — 旧版，返回 tuple
- `/root/autodl-tmp/pacs/pacs/profiling/` — 新版，返回 dict

脚本的 `sys.path` 设置导致 import 解析到旧版。

**修复方式**: 更新旧版 `bootstrap_interaction_index` 使其返回 dict（与新版一致），包含 `mean`, `ci_low`, `ci_high`, `median`, `median_ci_low`, `median_ci_high` 六个 key。

**验证**: `python -c "from run_profiling_gsm8k import *; print('import ok')"` 通过。

**s025 状态**: PID 281024 已退出。日志 `logs/gsm8k_qw_rand_s025.log` 显示它实际上已成功完成（输出在 `profiling_output_gsm8k_qw_rand_s025/`），但新的 `gsm8k_profiling/qw_rand_s025/` 目录为空——说明新一批 s025 也需要重跑。

两个实验（s025 和 s030）都需要重跑。代码修复已完成，可以安排重跑。

---
