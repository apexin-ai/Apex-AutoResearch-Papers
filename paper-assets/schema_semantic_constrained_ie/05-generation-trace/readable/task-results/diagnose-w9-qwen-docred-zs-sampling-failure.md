# diagnose w9 qwen docred zs sampling failure

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w9_qwen_docred_zs_sampling_failure_20260518T151622_result.json`
- **Structured JSON:** [`2b8119d9caf0b6f58ee0.json`](../../sessions/2b/2b8119d9caf0b6f58ee0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。核心发现：

**实验已被重启，原始失败日志已被覆盖。** 当前新 run 于 23:13 CST 启动，正在正常运行（17/998，~21s/item，预计 ~6 小时完成）。GPU 利用率 78%，显存 18.9GB/97GB，状态健康。

由于新 run 使用相同的 log/jsonl 路径且用 `tee`（非追加模式），原始 43.75 GPU-hour 失败 run 的错误信息已丢失，无法确认失败直接原因。推测可能是长文档导致 sampling 生成超长输出、GPU 资源竞争或平台干预。

报告已写入 `artifacts/w9_qwen_docred_zs_sampling/failure_diagnosis.md`。

---
