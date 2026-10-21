# check docred experiment progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_docred_experiment_progress_20260514T061515_result.json`
- **Structured JSON:** [`bc57acf8ba35233a50ce.json`](../../sessions/bc/bc57acf8ba35233a50ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## DocRED 实验状态报告（14:16 CST）

| | grammar_only (cuda:0) | full_s1 (cuda:1) |
|---|---|---|
| **进程** | PID 150766 ✅ 存活 | PID 157047 ✅ 存活 |
| **GPU 显存** | 17,526 MiB / 97,887 MiB | 17,478 MiB / 97,887 MiB |
| **GPU 利用率** | 84% | 84% |
| **GPU 温度** | 54°C | 54°C |
| **进度** | **759 / 998** (76.1%) | **625 / 998** (62.6%) |
| **已运行** | ~4h22m (09:54 起) | ~4h11m (10:05 起) |
| **速度** | ~174 docs/hr | ~149 docs/hr |
| **剩余** | 239 docs → **~1.4h** | 373 docs → **~2.5h** |
| **预计完成** | **~15:38** | **~16:46** |

**异常：** 无。两卡温度正常，利用率稳定，输出文件持续写入（最近修改时间均在 14:16）。

**注意：** full_s1 的实际 PID 是 157047（不是 157042）。另外 `phase2_batch.log` 记录的是另一个 SciERC 实验（176/551），与这两个 DocRED 实验无关。

---
