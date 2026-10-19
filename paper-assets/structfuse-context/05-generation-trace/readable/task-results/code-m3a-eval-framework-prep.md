# code m3a eval framework prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_m3a_eval_framework_prep_20260513T013129_result.json`
- **Structured JSON:** [`14b543ca905acc3cf36c.json`](../../sessions/14/14b543ca905acc3cf36c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

设计文档已写入 `memory.md`。核心发现：

**可复用代码**：`evaluation/eval_swebench.py` 已有完整 E2E 框架（retrieval → vLLM → patch），`StructFuseRetriever` 可直接加载 checkpoint 做推理。唯一的 placeholder 是 `run_swebench_tests()`。

**三个关键风险**：
1. **Docker 不可用** — SWE-bench 官方 harness 需要 Docker，AutoDL 不支持。推荐方案：服务器上只做 retrieval + patch 生成 → 导出 predictions.json → 在有 Docker 的机器上跑评估
2. **磁盘空间严重不足** — 数据盘仅剩 15GB，clone 300 个 repo 需要 50-80GB。M3a 启动前必须解决
3. **LLM 模型选择** — Qwen3.6-27B 无法在 4090D 上 FP16 运行，推荐先用 Qwen2.5-7B-Instruct 跑通

**建议两阶段执行**：
- Phase A（M2 完成后即可）：只跑 retrieval-level eval（R@k/MRR），不需要 LLM 和 Docker
- Phase B：E2E eval，需要解决 Docker 和磁盘问题

---
