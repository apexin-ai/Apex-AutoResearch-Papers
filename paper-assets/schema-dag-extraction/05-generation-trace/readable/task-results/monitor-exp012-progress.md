# monitor exp012 progress

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp012_progress_20260515T191405_result.json`
- **Structured JSON:** [`1effbcf8864cb62be63b.json`](../../sessions/1e/1effbcf8864cb62be63b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp012_llama_8b_r2 状态

| 项目 | 状态 |
|------|------|
| **进程** | 存活，已运行 ~36 分钟 |
| **PID 315801** | wrapper bash, 3.5 MB RSS |
| **PID 316128** | VLLM::EngineCore, 2.2 GB RSS |
| **GPU** | 84.7 / 97.9 GB (86%), 利用率 71% |
| **进度** | **69 / 94 batches 完成 (~73%)** |
| **当前阶段** | count_6/random/0 正在运行（已完成 count_1 全部 64 批 + count_2 全部 5 批） |
| **每批输出** | 1000 outputs，模型生成正常的结构化 JSON（实体抽取结果） |
| **JSON 解析失败** | 47 条 / ~69,000 总输出 (0.07%，可忽略) |
| **gen_tokens** | 日志未记录此指标，但从输出内容看模型生成了完整的实体 JSON（非空输出），**不是之前 gen_tokens=2 的空输出问题** |
| **结果目录** | 尚未创建，预计实验结束后写入 |
| **预估剩余** | 剩 25 批，平均 ~0.5 min/批，**预计 ~13 分钟后完成** |

---
