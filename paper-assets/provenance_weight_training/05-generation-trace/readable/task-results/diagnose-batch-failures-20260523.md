# diagnose batch failures 20260523

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_batch_failures_20260523_20260523T032336_result.json`
- **Structured JSON:** [`120d495b911f9c4d4c2e.json`](../../sessions/12/120d495b911f9c4d4c2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已保存到 `artifacts/batch_failures_20260523.md`。

**结论：同一个根因** — 3个实验都硬编码了 `--resume_from_checkpoint checkpoint-1000`，但前次运行在 step ~1000 附近崩溃，checkpoint-1000 从未成功保存。

| 实验 | 错误 | 可用 checkpoint |
|------|------|----------------|
| bs8_nmin4_adaptive_seed123 | SafetensorError（文件不完整） | checkpoint-500 |
| bs8_nmin4_uniform_seed123 | SafetensorError（文件不完整） | checkpoint-500 |
| rho03_adaptive_seed456 | FileNotFoundError（目录不存在） | 无 |

**修复**：前两个可改为 `--resume_from_checkpoint checkpoint-500`；第三个必须从头跑。最省事的做法是全部去掉 resume 从头跑（6103 steps 对 0.6B 模型很快）。建议后续把 resume 参数改为 `True` 让 Trainer 自动选最新有效 checkpoint，避免再踩这个坑。

---
