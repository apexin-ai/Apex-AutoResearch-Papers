# ssh exp001 recovery check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp001_recovery_check_20260523T034734_result.json`
- **Structured JSON:** [`012e860dccc81d032b84.json`](../../sessions/01/012e860dccc81d032b84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-001 Llama Judge 数据收集状态

### 1. 进程状态：全部正常运行

| 组件 | PID | 端口/配置 | GPU | 启动时间 |
|------|-----|-----------|-----|---------|
| vLLM 实例 1 | 122778 | port 8001 | cuda:2 | May 22 |
| vLLM 实例 2 | 523916 | port 8004 | cuda:1 | 今天 07:33 |
| collect.py shard A | 525427 | config_llama_arena_a.yaml | - | 今天 07:37 |
| collect.py shard B | 525429 | config_llama_arena_b.yaml | - | 今天 07:37 |

vLLM 实例 2 和两个 collect.py 是今天 07:33-07:37 重启的（可能是之前的自动恢复脚本）。

### 2. 当前进度

| Shard | 进度 | 完成率 | ETA |
|-------|------|--------|-----|
| A | 1340/2664 | **50.3%** | ~246 min (~4.1h) |
| B | 1160/2135 | **54.3%** | ~210 min (~3.5h) |

速度稳定 ~0.1 items/s。相比之前的 32%，进度显著推进。

### 3. GPU 占用

| GPU | 显存 | 利用率 | 状态 |
|-----|------|--------|------|
| 0 | 0/98GB | 0% | **空闲** |
| 1 | 91/98GB | 100% | vLLM (port 8004) |
| 2 | 91/98GB | 100% | vLLM (port 8001) |
| 3 | 0/98GB | 0% | **空闲** |

### 4. 已收集数据
- `arena_hard_judgments.jsonl`：**5551 行**，8.4MB
- 文件最后修改：2026-05-23 11:48:27（几秒前仍在写入）
- 总需求：4799 items（2664 + 2135），已完成约 2500 items（52%）

### 5. 结论

**无需干预。** 两个 shard 都在正常运行，预计 ~4 小时后全部完成（约今天下午 15:50 CST）。GPU 0 和 3 空闲可用于其他任务。系统标记的 "failed" 是误报。

---
