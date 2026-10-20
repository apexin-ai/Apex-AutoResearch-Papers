# ops cuda1 triage and progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda1_triage_and_progress_20260517T021407_result.json`
- **Structured JSON:** [`f5aeb0bb96d25366c241.json`](../../sessions/f5/f5aeb0bb96d25366c241.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

**1. s43 结果：无**
目录 `/root/autodl-tmp/eval_results/plan_002_test_rsft_s43` 存在但为空（仅创建了目录，无任何输出文件）。进程 PID 390436 崩溃未产出结果，需重跑。

**2. 1.7B CED scoring：进度 66%，运行中**
- 当前：16000/24216 records（66.1%）
- 速率：约 500 records / 2.3 min
- 剩余约 8216 records → 预计还需 ~38 分钟完成
- 运行在 cuda:0（12.6GB 占用）

**3. cuda:1 状态：占用**

| GPU | 显存占用 | 总显存 | 利用率 |
|-----|---------|--------|--------|
| 0 | 12596 MiB | 32607 MiB | 86% |
| 1 | **11415 MiB** | 32607 MiB | 48% |
| 2 | 1533 MiB | 32607 MiB | 31% |
| 3 | 25281 MiB | 32607 MiB | 71% |

cuda:1 占用 11.4GB，**不空闲**。cuda:2 是唯一接近空闲的卡（1.5GB）。

---
