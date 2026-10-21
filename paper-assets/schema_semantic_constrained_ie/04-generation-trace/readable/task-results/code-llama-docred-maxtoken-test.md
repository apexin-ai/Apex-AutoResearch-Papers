# code llama docred maxtoken test

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_docred_maxtoken_test_20260515T063113_result.json`
- **Structured JSON:** [`b5fb379da3202da05f0e.json`](../../sessions/b5/b5fb379da3202da05f0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/llama_docred_maxtoken/experiment_plan.md`。

**核心信息**：

- **当前 max_new_tokens**: 4096
- **新值**: 6144 (1.5x)
- 两组实验命令已就绪（唯一差异：`--max_new_tokens 6144` + `_mt6144` 输出后缀）
- 可并行跑 cuda:0 / cuda:1，总墙钟约 6–7 小时
- 服务器已验证：GPU 空闲、模型/数据/脚本均存在、磁盘充足
- 判定标准：full_s1 parse failures 从 91 降至 ≤70 = 截断假设成立

---
