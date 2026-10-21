# diagnose exp 14b inference fewnerd

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_14b_inference_fewnerd_20260520T172350_result.json`
- **Structured JSON:** [`c2db1fb713aecba2bfbb.json`](../../sessions/c2/c2db1fb713aecba2bfbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。总结：

## 诊断结果

**根本原因：监控误报（PID mismatch）。进程实际仍在运行。**

| 项目 | 详情 |
|------|------|
| 注册 PID | 201001 — 已死 |
| 实际 PID | 217692 (python) → 217960 (EngineCore) — 运行中 |
| GPU 0 状态 | 31088/32607 MiB, 99% util |
| 当前进度 | FewNERD N=2, 24%, ETA ~2h |
| 已完成 | SciERC (全 N) + CoNLL (全 N) + FewNERD N=1 |

**核心问题：**
1. **PID 监控脱靶** — 注册了中间进程 PID，实际推理跑在新 PID 下
2. **KV cache 极度不足** — 14B 模型占 27.57 GiB / 32 GiB，仅剩 1.09 GiB 给 KV cache，最多 2.89 并发请求。推理极慢但稳定
3. **早期 ckpt36000 崩溃** — 未设 `enforce_eager`，CUDA graph 内存开销导致 EngineDeadError。当前运行已修复
4. **SciERC/CoNLL 结果无用** — FewNERD 专用模型跨域 F1<0.05

**已更新：** registry failure_reason + notes、memory.md 教训、诊断报告已注册到 artifacts。

---
