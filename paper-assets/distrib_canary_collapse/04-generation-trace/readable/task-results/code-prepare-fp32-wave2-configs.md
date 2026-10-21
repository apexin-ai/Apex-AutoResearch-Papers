# code prepare fp32 wave2 configs

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_fp32_wave2_configs_20260519T061923_result.json`
- **Structured JSON:** [`5c1accfc91bd12ed801a.json`](../../sessions/5c/5c1accfc91bd12ed801a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已写入并注册。总结：

**产出**: `artifacts/fp32_wave2_configs.md`，包含 4 个实验的完整 tmux 启动命令。

**关键发现**:
1. `iterative_train.py` 没有 `--torch_dtype` 参数，fp32 通过不传 `--bf16` 实现（默认行为）
2. **阻塞项**: westd-17855 的代码缺少 padding_side 修复（westd-19828 已修复），需先同步才能启动
3. westd-17855 磁盘充足（223 GB），但 6 个 GPU 当前全部在用（a050 fp32 ×3 + a010 fp32 + scale_69b + qwen35），需等当前实验完成后替换
4. 预估 4 实验共 ~12 GPU-hours（并行 wall time ~3h），每实验 ~1.6 GB 磁盘

---
