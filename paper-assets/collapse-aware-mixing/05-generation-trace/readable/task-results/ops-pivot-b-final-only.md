# ops pivot b final only

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pivot_b_final_only_20260513T193250_result.json`
- **Structured JSON:** [`ff46af6df4854128f332.json`](../../sessions/ff/ff46af6df4854128f332.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 内存已从 4929 MiB 增长到 **49777 MiB**（~48.6 GB），利用率 34%。生成阶段正在进行，200 samples × 2048 tokens 的生成需要大量显存，这是预期行为。

日志还停在初始输出是因为 `tee` 的缓冲——实际进程在 GPU 上活跃运行。

## 汇总

| 项目 | 状态 |
|------|------|
| Kill 旧进程 | 已清除，GPU 清空 (0 MiB) |
| 文件同步 | 两个脚本均含 `--only-final` 参数 |
| tmux session | `pivot_b_final` 运行中 |
| 进程状态 | `analyze_generated_eff_rank.py` 正在处理 3 个 final_model 中的第 1 个 |
| GPU 利用率 | 34%, 49777 MiB / 97887 MiB |

pipeline 已启动，正在运行 G0 的 generation（200 samples, 2048 tokens）。预计 ~1h 完成全部 3 个 checkpoint 的 analyze_generated，之后自动续跑 compare 和 layer 分析。

---
