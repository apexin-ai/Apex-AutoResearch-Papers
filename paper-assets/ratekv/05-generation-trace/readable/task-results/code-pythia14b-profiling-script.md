# code pythia14b profiling script

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pythia14b_profiling_script_20260515T095103_result.json`
- **Structured JSON:** [`a6231f272e7876cd4877.json`](../../sessions/a6/a6231f272e7876cd4877.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Profiling 已成功启动。

**汇总：**

| 项目 | 状态 |
|------|------|
| 脚本 | `/root/ratekv/run_pythia14b_hires_profiling.py` |
| Dry-run | 通过 |
| tmux session | `w1_pythia14b_hires_profiling` |
| Baseline PPL | 13.6347 |
| 第一个 head | L0H0 delta=0.009254, ~4s/head |
| 384 heads × ~4s | **预计 ~26 分钟完成** |
| 输出文件 | `pythia14b_hires_bf16_2bitonly_profiles.json` + `_results.json` |
| 日志 | `/root/ratekv/logs/w1_pythia14b_hires_profiling.log` |

---
