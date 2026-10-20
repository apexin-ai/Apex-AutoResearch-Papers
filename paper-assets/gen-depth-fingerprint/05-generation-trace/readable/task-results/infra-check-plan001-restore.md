# infra check plan001 restore

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-plan001-restore_20260514T201031_result.json`
- **Structured JSON:** [`2523ce1278447b9628c3.json`](../../sessions/25/2523ce1278447b9628c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### plan-001-restore：已完成

`plan-001-restore` 的 tmux session 已退出（不在列表中），4 个目标文件全部存在且非空：

| 文件 | 大小 | 行数 |
|------|------|------|
| `ablation_results.json` | 1.5 KB | 54 |
| `trend_analysis.json` | 6.8 KB | 261 |
| `perplexity_by_depth.json` | 642 B | 33 |
| `depth_trends.png` | 530 KB | — |

所有文件时间戳为 May 15 03:14，恢复成功。

### plan-002 generation jobs：正常运行

4 个 tmux session 全部在线：
- `plan-002-pythia1b-s0`
- `plan-002-pythia1b-s1`
- `plan-002-olmo2-s0`
- `plan-002-olmo2-s1`

GPU 使用情况：
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 46% | 2649 MiB |
| 1 | 45% | 2649 MiB |
| 2 | 48% | 3623 MiB |
| 3 | 45% | 3623 MiB |

4 卡均在工作，GPU 0-1 跑 pythia1b（显存较小），GPU 2-3 跑 olmo2（显存较大），一切正常。

---
