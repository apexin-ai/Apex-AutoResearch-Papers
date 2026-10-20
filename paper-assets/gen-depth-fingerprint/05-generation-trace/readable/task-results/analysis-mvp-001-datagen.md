# analysis mvp 001 datagen

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp-001-datagen_20260514T180259_result.json`
- **Structured JSON:** [`1183eb8416d92eb76346.json`](../../sessions/11/1183eb8416d92eb76346.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## MVP-001 数据生成结果汇总

### 1. 进程状态
全部 4 个 shard **已完成**，EXIT_CODE=0。GPU 全部空闲（0% 利用率，0 MiB 显存占用）。

### 2. 每 shard 记录数和文件大小

| Shard | 记录数 | 文件大小 | 耗时 | 跳过数 |
|-------|--------|----------|------|--------|
| 0 | 1,162 | 1.3 MB | 2143s (~36min) | 38 |
| 1 | 1,148 | 1.2 MB | 2054s (~34min) | 43 |
| 2 | 1,116 | 1.1 MB | 1766s (~29min) | 57 |
| 3 | 1,183 | 1.3 MB | 2147s (~36min) | 35 |
| **合计** | **4,609** | **4.9 MB** | — | **173** |

### 3. 输出文件路径
```
/root/gen-depth-fingerprint/data/generations_shard{0,1,2,3}.jsonl
```

### 4. 数据格式
字段：`id`, `depth`, `text`, `seed_id`, `token_count`。全部 4,609 行 JSON 验证通过，无损坏。

### 5. Depth 分布

| Depth | 记录数 | 占比 |
|-------|--------|------|
| 0 | 995 | 21.6% |
| 1 | 989 | 21.5% |
| 2 | 924 | 20.0% |
| 3 | 879 | 19.1% |
| 4 | 822 | 17.8% |
| **合计** | **4,609** | 100% |

### 6. GPU 状态
4× RTX 5090 (32GB)，全部空闲。

### 7. 发现的问题

- **种子数 995 而非 1000**：日志显示 "Loaded 995 seeds"，输入文件可能有 5 条被过滤（空行或格式问题）。
- **深度衰减**：从 depth 0 的 995 条逐层下降到 depth 4 的 822 条，共 173 条因 "empty input" 被跳过。衰减率约 17.4%（(995-822)/995）。这意味着部分生成链在中间深度产生了空文本，导致后续深度无法继续。
- **Shard 2 跳过最多**（57 条），生成质量略低于其他 shard，可能与该区间的种子文本特征有关。

---
