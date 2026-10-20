# collect v5 results check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_v5-results-check_20260514T015016_result.json`
- **Structured JSON:** [`fdfd1ee38c8ef26ad138.json`](../../sessions/fd/fdfd1ee38c8ef26ad138.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. 实验状态：全部 **仍在运行**

| 实验 | PID | GPU | 已运行 | 进度 | 预计剩余 |
|------|-----|-----|--------|------|----------|
| `mvp_v5_fixed_s020` | 46574 | cuda:0 | 24m | **35/50** (有日志) | ~15 min |
| `mvp_v5_fixed_s030` | 46940 | cuda:1 | 24m | **35/50** (有日志) | ~15 min |
| `mvp_v5_fixed_s015` | 48262 | cuda:2 | 18m | 未知（无日志文件） | ~21 min |
| `mvp_v5_fixed_s025` | 48403 | cuda:3 | 18m | 未知（无日志文件） | ~21 min |

- s020/s030 有日志 (`profiling_output_v5_s020.log`, `profiling_output_v5_s030.log`)，当前处理到第 35/50 个 problem，约 1 min/problem
- s015/s025 **没有日志文件**（进程状态为 `Rl+`，输出可能直接到 tmux 终端）
- 输出目录 (`profiling_output_v5_s0{15,20,25,30}/`) 已创建但为空，结果应在全部 50 个 problem 完成后写入

### 2. Qwen2.5-7B 下载状态：**已完成**

- 路径：`/root/autodl-tmp/models/Qwen2.5-7B/Qwen/Qwen2___5-7B/`（通过 ModelScope 下载）
- 大小：15GB，4 个 safetensors 分片齐全
- config.json, tokenizer.json 等配置文件完整

### 3. 异常发现

- s015 和 s025 缺少 `.log` 文件，无法确认进度。可能是启动时未做日志重定向，输出在 tmux 会话中。
- 代码实际在 `/root/autodl-tmp/pacs/`，非任务描述中的 `/root/phase-gated-compound-sparse/`。

### 建议

大约 **20 分钟后**再次检查，届时所有实验应已完成并写入结果 JSON。

---
