# diagnose autodl 5090 full audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_autodl-5090-full-audit_20260514T133404_result.json`
- **Structured JSON:** [`fe7146004ef60889f920.json`](../../sessions/fe/fe7146004ef60889f920.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

### 服务器状态
- **GPU 0/2/3 正常工作**，3 个实验 PID 全部存活，运行 ~7 分钟，模型加载中尚未产出 samples
- **GPU 1 空闲**，可用于新任务

### 3 个 RUNNING 实验
全部正常运行中，registry 状态准确无需修改。output 目录为空是正常的——刚启动 7 分钟，vLLM 加载 8B 模型需要几分钟。

### exp_007 LLaMA checkpoint
**完整，可直接 merge + inference。** 之前标为 `killed` 是误判——SIGHUP 发生在训练完成之后。已更正 registry：conclusion → success，补充了 checkpoint_path 和 metrics。

### WNUT merge
已完成，`qwen3-8b-wnut17-merged/` 含完整 4 shard 模型（~15.4GB）。

---
