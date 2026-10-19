# ops m1 moto diagnosis

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_m1_moto_diagnosis_20260516T025814_result.json`
- **Structured JSON:** [`ffee89855f244063b709.json`](../../sessions/ff/ffee89855f244063b709.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是报告。

---

## 诊断报告：m1_reextract_v2 moto 卡死

### Root Cause

**CodeQL exit code 33 = 查询评估超时**。moto（AWS 全量 mock 库）的 CodeQL 数据库 272MB，`call_graph.ql` 在 `--timeout=300`（5分钟）+ `--ram=8192`（8GB）下无法完成查询。每个 instance 都必然超时。

**这不是一个无限重试循环。** 进程在正常推进：每个 instance 先等 CodeQL 超时 5 分钟 → fallback 到 beniget → 写出 JSON → 处理下一个 instance。

### 当前状态

| 指标 | 值 |
|---|---|
| 首次 exit 33 | 2026-05-15 09:52 |
| 最新 exit 33 | 2026-05-16 10:56（还在继续） |
| 累计超时次数 | 296 / 536 |
| 完成进度 | ~55% |
| 每个 instance 耗时 | ~304.5s（300s CodeQL 超时 + 4.5s beniget） |
| 预计剩余 | ~240 instances × 5min = **~20 小时**（约 May 17 07:00 完成） |
| 主进程 RSS | 86GB |
| 空闲 worker | 3/4（moto 是最后一个 repo group，组内串行处理） |

### 数据质量

moto 所有 instance 的实际结果：
```json
{"extraction_method": "beniget", "call_graph": [], "dataflow_paths": [], "extraction_time_s": 304.57}
```
beniget fallback 产出 **空 call_graph**。5 分钟的 CodeQL 超时是纯浪费。

### 影响范围

- all.jsonl 当前 44,173 行，其中 539 行是 moto（来自第一次 m1 提取）= **1.2%**
- 不影响其他 81 个 repo（全部已完成）
- CPU 资源浪费：1 core 持续跑必然超时的 CodeQL 查询
- 进程完成后 `rerun_m1_failed.sh` 会从所有个体 JSON 文件重建 all.jsonl

### 建议方案

| 方案 | 操作 | 耗时 | 效果 |
|---|---|---|---|
| **A: 等它跑完** | 不操作 | ~20h | moto 全部 beniget 数据，自然完成后 rebuild all.jsonl |
| **B: 杀进程，跳过 moto** | kill PID 209821 | 立即 | 丢失剩余 ~240 moto instance 的 beniget 数据，手动 rebuild all.jsonl |
| **C: 杀进程，重跑 moto（推荐）** | kill 当前进程 → 删 moto CodeQL DB → 以极短 timeout（1s）或无 CodeQL 方式重跑 moto | ~10min | 全部 536 instance 秒级获得 beniget 数据，释放资源 |

**推荐方案 C**：当前每 instance 浪费 5 分钟等 CodeQL 超时，删掉 CodeQL DB 后 beniget 直接运行，536 instances 预计 10 分钟内完成。然后手动 rebuild all.jsonl。

等 Director 决策。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "extraction_method": "beniget",
    "call_graph": [],
    "dataflow_paths": [],
    "extraction_time_s": 304.57
  }
}
```

</details>

---
