# code plan 005 vota ae format

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_005_vota_ae_format_20260515T231024_result.json`
- **Structured JSON:** [`4c1c74a8fdd65425eae3.json`](../../sessions/4c/4c1c74a8fdd65425eae3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

### 修改内容
`debugbench_format_data.py` 新增 `vota` 和 `ae_only` 两个条件：
- **VOTA**: 调用 `compressor.compress(trace_events, test_code)` — 包含 [ASSERT] + [ERROR] + [LOOP] 三个组件
- **ae_only**: 调用 `compressor._extract_assertions(...)` — 仅保留 [ASSERT] actual/expected 值对
- 新增 `--condition` 参数，可指定单条件生成或省略生成全部 5 个条件

### 生成数据 (4 文件)
| 条件 | train | test |
|------|-------|------|
| vota | 1622 | 426 |
| ae_only | 1622 | 426 |

### Token 长度分析

| | vota | ae_only |
|---|---|---|
| Mean | 1465 | 723 |
| Median | 2015 | 700 |
| P95 | 2016 | 1554 |
| >2048 | 0% | 0% |
| 截断率 | 66.0% | 0.7% |
| 空 trace | 30.5% | 31.5% |

ae_only 非常紧凑（median 700 tokens，仅 0.7% 截断），对 DebugBench 这种逻辑错误为主的场景可能有优势。VOTA 有 66% 截断率，因为三组件信息量大，大部分被 2048 budget 截断到上限附近。

---
