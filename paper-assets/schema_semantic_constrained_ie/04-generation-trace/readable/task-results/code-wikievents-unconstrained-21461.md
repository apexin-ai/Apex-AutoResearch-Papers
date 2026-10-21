# code wikievents unconstrained 21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_unconstrained_21461_20260517T164105_result.json`
- **Structured JSON:** [`23bb51e82403d5db65aa.json`](../../sessions/23/23bb51e82403d5db65aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。

## 结果汇总

| 项目 | 状态 |
|------|------|
| **代码/数据同步** | 从 westd-16980 同步了 `run_constrained_extraction.py`、`compiler/`、`prompts/`、`data/wikievents/` |
| **模型** | 本地路径 `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3` |
| **总样本数** | 12 docs（WikiEvents train.jsonl 仅 12 个文档，非任务预期的 246） |
| **成功/失败** | 10 success, 2 fail（E=0 说明未提取到 entities，可能需检查 prompt） |
| **总用时** | ~4 分钟（含模型加载） |
| **输出文件** | `outputs/wikievents_mistral_unconstrained.jsonl` |
| **日志文件** | `outputs/wikievents_mistral_unconstrained.log` |

**注意事项**：
1. WikiEvents 数据只有 12 个 docs，远少于预期的 ~246。可能需要检查 16980 上是否有更完整的数据集（如 test split）
2. 有 2 个文档 FAIL（第 5 个和第 12 个），E=0 表示这些样本未成功提取到任何实体或事件
3. 所有成功样本的 E=0 但 Ev>0，说明 unconstrained 模式下可能只提取了事件但没有单独提取实体

---
