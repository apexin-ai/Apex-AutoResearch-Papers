# prep checkpoint transfer sizing

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_checkpoint-transfer-sizing_20260522T052516_result.json`
- **Structured JSON:** [`b7e431da95ca0c03babe.json`](../../sessions/b7/b7e431da95ca0c03babe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### DocRED 70B LoRA (`checkpoint-1146`)
- **总大小: 768 MB**
- 关键文件:
  - `adapter_model.safetensors` — 250 MB (LoRA 权重)
  - `optimizer.pt` — 500 MB
  - `tokenizer.json` — 16 MB

### SciERC 70B LoRA (`checkpoint-663`)
- **总大小: 768 MB**
- 关键文件:
  - `adapter_model.safetensors` — 250 MB (LoRA 权重)
  - `optimizer.pt` — 500 MB
  - `tokenizer.json` — 16 MB

### 传输评估

两个 checkpoint 各 768 MB，合计约 **1.5 GB**。如果只需推理（不需恢复训练），可以只传 `adapter_model.safetensors` + `adapter_config.json` + tokenizer 文件，每个 checkpoint 约 **267 MB**，合计 ~530 MB。

关于跨服务器直连：AutoDL 实例之间通常无法直接 ping/scp（各实例在独立容器网络中），需要通过中间节点或 autodl-tmp 网盘中转。常见方案：
1. **通过本地中转**: westd-16980 → 本地 → westd-21461
2. **HuggingFace Hub 中转**: 上传为私有 repo，另一台拉取
3. **AutoDL 文件存储**: 如果两台在同一区域，可挂载共享存储

---
