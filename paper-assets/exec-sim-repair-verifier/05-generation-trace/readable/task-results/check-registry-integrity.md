# check registry integrity

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_registry-integrity_20260514T220036_result.json`
- **Structured JSON:** [`1450f402f0aa818a6a9a.json`](../../sessions/14/1450f402f0aa818a6a9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Registry 完整性检查结果：**

- **文件路径**：`registry.yaml` 存在，大小 57096 tokens
- **实验总数**：**75 条**，符合预期（70+）
- **状态分布**：
  - DONE: 68 条
  - RUNNING: 4 条（#65, #66, #73, #75）
  - PREPARING: 3 条（#67, #68, #70, #74）
- **备份文件**：无 `registry.yaml.bak`
- **锁文件**：存在 `registry.lock`

**结论**：Registry 文件完整，75 条记录全部在。之前只查到 2 条是查询问题（可能 `read_registry` 带了 limit 或 filter），不是 registry 损坏。

---
