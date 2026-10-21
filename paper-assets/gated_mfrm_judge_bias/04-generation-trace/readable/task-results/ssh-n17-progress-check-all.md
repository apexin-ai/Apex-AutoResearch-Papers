# ssh n17 progress check all

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n17_progress_check_all_20260523T234516_result.json`
- **Structured JSON:** [`b8dbce60ba286521e434.json`](../../sessions/b8/b8dbce60ba286521e434.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. API Judges 进度 (autodl-8gpu)

| Judge | 完成 | 总数 | 进度 | 速度 | ETA |
|-------|------|------|------|------|-----|
| Claude Sonnet 4.6 | 191 | 17,982 | 1.1% | 0.4 items/s | ~13.8h |
| Gemini 2.5 Pro | 91 | 17,982 | 0.5% | 0.2 items/s | ~26.6h |
| DeepSeek V4 Pro | 63 | 17,982 | 0.4% | 0.1 items/s | ~36.1h |
| Qwen3 235B | 58 | 17,982 | 0.3% | 0.1 items/s | ~36.6h |

**所有 judge 都在频繁遇到 500 Internal Server Error**，需要重试，严重拖慢速度。进程仍在运行（日志在持续写入），但吞吐量极低。

### 2. LLaMA-3.3-70B-Instruct-AWQ 下载

**下载已中断。** 只下了 3/9 safetensors shards（model-00001, 00004, 00007），共 27GB。无活跃下载进程。casperhansen 子目录也是空的（4K）。需要手动恢复下载。

### 3. rtx6000-4x 连通性

**仍然断连。** 端口 23687 无法连接。需要去控制台确认实例状态并获取新端口。

### 4. exp-017 进度 (autodl-8gpu)

PID 318082 **仍在运行**，已运行 16h41m。输出文件 `coverage_simulation.csv` 有 173 行数据（header + 173 rows），最新行 n_models=8, seed=172。进程活跃。

---
