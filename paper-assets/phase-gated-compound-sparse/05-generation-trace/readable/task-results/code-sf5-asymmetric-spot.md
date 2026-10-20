# code sf5 asymmetric spot

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sf5_asymmetric_spot_20260515T173319_result.json`
- **Structured JSON:** [`9969198da4999e8903ef.json`](../../sessions/99/9969198da4999e8903ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 job 都在正常运行：
- **Config A** (GPU 0): 已到第 4/50 题
- **Config B** (GPU 1): 已到第 3/50 题

## 状态报告

| 项目 | 状态 |
|------|------|
| 代码 | `run_sf5_asymmetric.py` 已部署，dry-run 通过 |
| 数据 | math500.json 就绪，n=50 stratified sample |
| 模型 | DeepSeek-R1-Distill-Qwen-7B 本地就位 |
| Registry | sf5_asymmetric_spot → RUNNING |
| Config A (h=0.20, kv=0.30) | GPU 0, PID 259632, 运行中 |
| Config B (h=0.30, kv=0.20) | GPU 1, PID 259884, 运行中 |
| 输出目录 | `profiling_output_sf5_h020_kv030/` 和 `profiling_output_sf5_h030_kv020/` |
| 日志 | `logs/sf5_config_A.log` 和 `logs/sf5_config_B.log` |
| 预计完成 | 每 config ~15-20 分钟（每题 ~10-20s × 50 题） |

---
