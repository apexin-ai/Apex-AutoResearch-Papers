# ssh urgent gpu0 fix v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-gpu0-fix-v2_20260513T222338_result.json`
- **Structured JSON:** [`39aca435ee9a497a0273.json`](../../sessions/39/39aca435ee9a497a0273.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常。

## 诊断报告

**根因**：vLLM EngineCore 子进程在父脚本崩溃后成为孤儿，持续占用 GPU0 ~28 GiB 显存。重新提交时新的 EngineCore 发现 GPU0 仅剩 3.51 GiB 可用，触发 `ValueError: Free memory on device cuda:0 (3.51/31.36 GiB) < desired 0.85 (26.65 GiB)`。

**为什么反复发生**：脚本没有孤儿进程清理机制。每次崩溃都留下 EngineCore 孤儿，每次重提交都因显存不足再次崩溃。cleanup 函数这次启动时又发现了一个新孤儿 (PID 824574)。

**修复**：在 `episode_level_collection.py` 中添加 `cleanup_gpu_processes()` 函数（lines 36-60），在 agent 创建前自动查杀目标 GPU 上的所有残留进程。

**当前状态**：
- GPU0: plan-001b-gpu0-v2 (PID 853847) 正常运行，100% 利用率，正在收集 find-animal episode 数据
- GPU1: plan-001b-gpu1 (PID 774317) 正常运行，未受影响
- 两卡均 28013 MiB / 32607 MiB

---
