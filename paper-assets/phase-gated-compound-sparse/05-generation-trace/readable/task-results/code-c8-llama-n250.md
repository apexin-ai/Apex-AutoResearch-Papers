# code c8 llama n250

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c8_llama_n250_20260516T023333_result.json`
- **Structured JSON:** [`39f16d88e12e7a350402.json`](../../sessions/39/39f16d88e12e7a350402.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交并注册。总结：

- **实验**: c8_llama_n250，状态 RUNNING
- **PID**: 301187（nohup 主进程）
- **4 GPU 并行**:
  - GPU 0: importance s015 + s020
  - GPU 1: importance s025 + s030
  - GPU 2: random s015 + s020
  - GPU 3: random s025 + s030
- **配置**: n=250, max_new_tokens=8192, min_phase_length=10, seed=42
- **日志**: `/tmp/c8_llama_n250.log`，各 condition 独立日志在 `logs/c8_llama_*.log`
- **输出**: `profiling_output_c8_llama_{method}_{sparsity}/`（共 8 个目录）
- **预估耗时**: 5-6 小时

---
