# ops progress check semantic only 20260516T16

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress_check_semantic_only_20260516T16_20260516T153344_result.json`
- **Structured JSON:** [`b186c11938c980e5783e.json`](../../sessions/b1/b186c11938c980e5783e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 实验 1: w8_qwen_docred_ft_semantic_only (westd-21461)

| 检查项 | 结果 |
|--------|------|
| PID 存活 | ✅ Yes (运行 5h24m) |
| GPU 内存 | cuda:1: 18919/97887 MiB, utilization 85% |
| 输出行数 | **886/998** |
| 最后活动 | 2026-05-16 23:33:51 CST (刚刚) |
| 日志状态 | 正常推进，当前处理 [823/998]，无 error（有 1 个 FAIL 但正常跳过） |
| 预估剩余 | ~112 samples，按平均速率 ~22s/sample，**约 40 分钟完成** |

### 实验 2: w8_llama_docred_ft_semantic_only (westd-16980)

| 检查项 | 结果 |
|--------|------|
| PID 存活 | ✅ Yes (运行 3h01m) |
| GPU 内存 | cuda:1: 16921/97887 MiB, utilization 87% |
| 输出行数 | **711/998** |
| 最后活动 | 2026-05-16 23:34:01 CST (刚刚) |
| 日志状态 | 正常运行，pad_token_id 警告无害。最后一个样本 inference 65.5s（parsed_output=null，模型生成了大量重复 relations 导致解析失败） |
| 预估剩余 | ~287 samples，按平均速率 ~15.3s/sample，**约 1h15m 完成** |

### cuda:0 状态

| 服务器 | cuda:0 |
|--------|--------|
| westd-21461 | ✅ 空闲 (0 MiB, 0%) |
| westd-16980 | ✅ 空闲 (0 MiB, 0%) |

### 结论

两个实验都正常推进，未卡住。Qwen 进度领先（89%），预计 ~40 分钟跑完；Llama 进度 71%，预计 ~1h15m 跑完。两台服务器 cuda:0 均空闲可用。

---
