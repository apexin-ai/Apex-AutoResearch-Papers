# emergency llama scierc full s1 dedup

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_emergency_llama_scierc_full_s1_dedup_20260514T141055_result.json`
- **Structured JSON:** [`0aea855e8abeae82129d.json`](../../sessions/0a/0aea855e8abeae82129d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据结构清晰了。汇总报告：

---

## 诊断结果

### 1. 进程状态
- **PID 190653**: 已死亡，无需处理
- **PID 190246**: 正常运行，21:48 启动，是唯一活跃进程

### 2. 数据完整性
| 指标 | 值 |
|------|------|
| 总输出行 | 335（持续增长中） |
| 有效 JSON | 334 |
| 损坏行 | **1**（第 194 行，`N04-1022_sent3`，缺 `{"doc` 前缀） |
| 重复 doc_id | **0** |
| 输出顺序 | **完美顺序** index 0→334，唯一 gap 恰在第 193 号（即损坏行） |

### 3. 根因分析
- 脚本未带 `--resume`，文件以 `"w"` 模式打开
- 190653 启动时截断了文件，但很快死亡（可能 GPU 显存冲突）
- 当前 PID 190246 实际是**后启动的那个进程**（21:48 启动，运行仅约 28 分钟），并非原始的 6h 进程
- 损坏发生在两个进程并发写入的瞬间，仅影响 1 行

### 4. 结论：**情况 B（轻微变体）**
- 数据 **未严重损坏**，仅 1/551 行受损，0 重复
- PID 190246 正常推进中，当前已完成 334/551
- 剩余 217 样本，约 **16-20 分钟**完成

### 5. 建议处理
- **让 190246 继续运行至完成**
- 完成后删除第 194 行坏数据，用 `--resume` 单独补跑 `N04-1022_sent3`
- 最终结果：551/551 完整

---
