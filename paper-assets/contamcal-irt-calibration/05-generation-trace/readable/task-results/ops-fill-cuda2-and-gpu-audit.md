# ops fill cuda2 and gpu audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fill-cuda2-and-gpu-audit_20260515T114500_result.json`
- **Structured JSON:** [`0340e8013b0b9c8dfbfb.json`](../../sessions/03/0340e8013b0b9c8dfbfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 张 GPU 都在工作，cuda:2 不空闲，无法提交新实验。

## GPU 全景审计结果

| GPU | PID | 运行时间 | 显存 | 任务 |
|-----|-----|---------|------|------|
| 0 | 549516 | 41 min | 14892/24564 MiB | **SFT: 1.5B d025 s123** |
| 1 | 549858 | 41 min | 15958/24564 MiB | **SFT: 1.5B d005 s123** |
| 2 | 553256 | 15 min | 3612/24564 MiB | **Eval: 0.5B base pretrained aligned** |
| 3 | 551219 | 34 min | 8976/24564 MiB | **Eval: 3B d000 s123 aligned** |
| 4 | 530975 | 3h01m | 10272/24564 MiB | **Eval: 1.5B base pretrained aligned** |
| 5 | 551290 | 34 min | 8976/24564 MiB | **Eval: 3B d005 s42 aligned** |

**PID 528993**: 存活，运行 `python3 run_extreme_gamma.py`，但未占用 GPU（不在 nvidia-smi compute apps 中）。

## Seed=123 Checkpoint 清单

| Model | d000 | d005 | d025 | d100 |
|-------|------|------|------|------|
| 0.5B | ✅ | ✅ | ✅ | ✅ |
| 1.5B | ✅ | 🔄 GPU1 训练中 | 🔄 GPU0 训练中 | ✅ |
| 3B | ✅ (含 v2) | ❌ 缺失 | ❌ 缺失 | ✅ |

## 结论

**cuda:2 被 eval 任务占用（PID 553256），按 C001/C002 约束不能提交。** 全部 6 张 GPU 均在工作。

用户优先列表中：
- 0.5B d025 s123 — 已完成
- 3B d100 s123 — 已完成
- **3B d005 s123** 和 **3B d025 s123** 是仅剩的两个缺口

cuda:2 上的 0.5B eval 应该较快完成（小模型），是最先释放的 GPU。建议 eval 完成后立即提交 **3B d005 s123** SFT 到 cuda:2。

---
