# ssh gpu0 v4 dedup check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu0-v4-dedup-check_20260514T022102_result.json`
- **Structured JSON:** [`c39c6e2908e19bda0a40.json`](../../sessions/c3/c39c6e2908e19bda0a40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### lifespan-longest-lived
| 项目 | 值 |
|------|-----|
| 清理前 | 26 行，ep 0-6 各重复 1 次 |
| 清理后 | 19 行，ep 0-18 各 1 条，无重复 |
| 删除 | 7 条 v4 写入的重复数据 |
| 备份 | `episodes.jsonl.bak_v4_dedup` |
| 距目标 20 | 还差 **1 个 episode**（ep 19） |

### measure-melting-point-unknown-substance
- episodes.jsonl **不存在**，还需全部 **20 个 episode**

### 根因
脚本的去重逻辑依赖 `--reuse_dirs` 参数（line 591），v4 启动命令没有使用该参数且 `--start_episode` 默认为 0，导致从 ep 0 开始追加写入，与已有 ep 0-18 产生重复。

### 建议下一步
重启时需指定 `--start_episode 19 --episodes 1` 跑 lifespan-longest-lived 补最后 1 个 ep，measure-melting-point 则需 `--start_episode 0 --episodes 20` 完整跑。或者直接用 `--reuse_dirs` 指向已有 results 目录让脚本自动跳过已存在的 episode。

---
