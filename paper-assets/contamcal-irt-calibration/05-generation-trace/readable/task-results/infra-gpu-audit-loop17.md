# infra gpu audit loop17

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-audit-loop17_20260516T152042_result.json`
- **Structured JSON:** [`2323c7fba8c1b283885c.json`](../../sessions/23/2323c7fba8c1b283885c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告保存至 `artifacts/gpu_audit_loop17.md`。

**关键发现：**

| GPU | 状态 | 任务 |
|-----|------|------|
| 0 | **空闲** | — |
| 1 | 占用 | Llama-3.2-3B d000 eval aligned (gsm8k 3%, ~2h) |
| 2 | 占用 | 0.5B-Instruct eval (mmlu done, gsm8k 进行中) |
| 3 | 占用 | Llama-3.2-3B d025 SFT (step 314/3384, ~2h) |
| 4 | ⚠️ **冲突** | 孤儿进程 PID 796493 — 与 GPU 1 同任务同 output dir |
| 5 | **空闲** | — |

**紧急问题：**
- **C001 违规**：PID 796493 (GPU 4, nohup 孤儿) 和 PID 800570 (GPU 1, managed) 同时跑 Llama d000 eval，写同一目录，有数据腐败风险。需要 kill 796493+796488 释放 GPU 4。

**已完成：**
- 3B d000 s123 signals 批量完成（6/9 computed），但 `signals_merged_mmlu.json` 缺失
- 6 个 Instruct eval 结果已生成

**可用 GPU**：清理后 cuda:0, cuda:4, cuda:5 共 3 块空闲。

---
