# code verify s789 data

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_s789_data_20260518T220851_result.json`
- **Structured JSON:** [`9384eacce13102b9be87.json`](../../sessions/93/9384eacce13102b9be87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

| 服务器 | 路径 | 状态 |
|--------|------|------|
| **autodl-5090-b** | `output/exp_fewnerd_seed789/` | 完整：`samples.jsonl` 37648 行 (642MB) + `report.json` |
| **autodl-5090-c** | `output/exp_fewnerd_seed789/` | 空目录，log 显示推理在 83% 处（可能中断或仍在运行） |
| **autodl-5090 (主)** | `output/exp_021_fewnerd_n8_seed789_shard{0,1,2}/` | 3 个分片共 37648 行 (12549+12549+12550)，每个分片均含 `report.json` |

**结论：FewNERD seed789 数据已在 autodl-5090 主服务器落盘。** 3 个分片合计 37648 样本，与 5090-b 的完整文件行数一致。无需 SCP 传输。

5090-c 的推理任务看起来未完成（目录为空），但因主服务器已有完整数据，不影响。

---
