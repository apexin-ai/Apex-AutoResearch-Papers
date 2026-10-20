# code c8 llama n250 fix

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c8_llama_n250_fix_20260516T031229_result.json`
- **Structured JSON:** [`ce099a58a0c798d5df97.json`](../../sessions/ce/ce099a58a0c798d5df97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**诊断结果：**
- 原脚本 `| tee` 管道吞掉 Python exit code，`set -e` 无法捕获崩溃
- 4 个模型同时加载到 4 GPU + max_new_tokens=8192 导致 OOM
- 第一批各跑了 ~15/250 问题后被杀，第二批秒死
- 结果只在最后写入，所以 8 个输出目录全空

**修复内容 (`run_c8_llama_n250_fixed.sh`)：**
- `set -euo pipefail` — 管道传播 exit code
- 输出重定向到日志文件（不用 tee）
- 每个条件完成后验证 `profiling_results.json` 存在且非空
- 每 GPU 只跑 1 个条件，GPU 2+3 并行，4 轮串行
- 后台 GPU 内存监控
- 任意失败立即中止

**已提交：**
- exp_id: `c8_llama_n250_fixed`
- tmux session: `c8_llama_n250_fixed`
- GPU 2+3, 4 轮 × 2 条件 = 8 条件
- 每条件 ~250 problems × ~1min/problem ≈ 4 小时/条件, 总计 ~16 小时

---
