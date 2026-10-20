# code c8 gpu0 s025

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c8_gpu0_s025_20260516T040415_result.json`
- **Structured JSON:** [`6f77bdafd22ea4224199.json`](../../sessions/6f/6f77bdafd22ea4224199.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功。状态：

- **PID**: 315052，运行中
- **GPU 0**: 17703 MiB / 97887 MiB (18%)，利用率 78% — 模型已加载，正在推理
- **进度**: 2/250 问题已处理，第1题检测到 8 个 phases
- GPU 0 还有 ~80GB 空余，但模型推理时显存会动态增长（其他 GPU 各占 73GB），最终应该也会到 ~73GB

关于同时跑 importance_s030：GPU 0 当前只用了 17.7GB（模型加载阶段），但参考 GPU 2/3 满载时各 73GB，单条件就需要 ~73GB。GPU 0 总共 97GB，跑两个条件会 OOM，不建议。

**预估完成时间**：GPU 2/3 上 Round 1 (s015+s020) 当前 27/250，每条件 250 题。按日志看第1题约 20 秒，250 题预计 ~1.5-2 小时完成 s025。主脚本到 Round 2 时会发现 `profiling_output_c8_llama_importance_s025/profiling_results.json` 已存在，自动 skip。

---
