# run 8gpu fill priority

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_8gpu_fill_priority_20260521T042232_result.json`
- **Structured JSON:** [`067dd7fe734c27b1aef6.json`](../../sessions/06/067dd7fe734c27b1aef6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 当前状态总结

**已完成（2/8）：**
- SciERC N=16 s123 → 5090-b cuda:2 → **DONE**（8 分钟完成）
- SciERC N=16 s456 → 5090-b cuda:3 → **DONE**（8 分钟完成）

**正在运行（4/8）：**

| 实验 | 服务器 | GPU | PID | 状态 |
|------|--------|-----|-----|------|
| 14B CoNLL (base model) | 5090-c | cuda:1 | 278137 | N=1 86%，正在推理 |
| FewNERD N=16 s456 | 5090-c | cuda:3 | 277403 | 3%，预计 ~3h |
| FewNERD N=16 s42 | 5090-b | cuda:2 | 315349 | 刚开始加载 |
| FewNERD N=16 s123 | 5090-b | cuda:3 | 315796 | 刚开始加载 |

**等待自动启动（2/8）：**
- CoNLL N=16 s123 → 5090 cuda:2 → rsync 传输中（2.1/16GB），自动启动脚本部署
- CoNLL N=16 s456 → 5090 cuda:3 → 同上

**关键调整：**
1. 5090 没有 8B 模型 → 搭建了 5090→5090-b 的 SSH 通道，rsync 传输中
2. SciERC 实验完成后立即在 5090-b 上重复利用 GPU 启动 FewNERD 实验
3. 14B CoNLL 改用 base model（Qwen2.5-14B-Instruct），而非之前被 kill 的 cross-domain fine-tuned 版本
4. 5090 上部署了自动启动脚本，rsync 完成后自动启动 CoNLL 实验（预计 ~30 分钟）

**待办：** rsync 完成后需要更新 CoNLL 实验的 registry 为 RUNNING，并清理 5090-b 上的临时 SSH key。

---
