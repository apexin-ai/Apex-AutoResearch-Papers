# ops critical fix extraction

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_critical-fix-extraction_20260521T112646_result.json`
- **Structured JSON:** [`99372357a68d8c804364.json`](../../sessions/99/99372357a68d8c804364.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，汇总如下：

---

## 修复结果

| Fix | 状态 | 详情 |
|-----|------|------|
| **Fix 1** extract_activations.py float→half | ✅ | 第264行 `.float()` → `.half()`, 文件中不再有 `.float()` |
| **Fix 2** 下游脚本 float16 兼容 | ✅ | train_probes.py 第126行已有 `.astype(np.float32)`; caclr_highdim.py 同样已有; compute_cka.py 第100/110行新增 `.astype(np.float32)` |
| **Fix 3** 旧 MVP 模型删除 | ✅ | LLM-Research/ 和 Qwen/ 已删除，释放 ~30GB |
| **Fix 4** run_p0.sh PYTHONUNBUFFERED | ✅ | 第3行已加 `export PYTHONUNBUFFERED=1` |

## 磁盘空间

`/root/autodl-tmp/`: **101GB 可用** (250GB used / 350GB total, 72%)

## 模型下载状态

### Llama4 Scout W4A16 — ✅ 下载完成
- **路径**: `/root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/`
- safetensors: **14/14** 全部就绪
- config.json: ✅ 存在
- `._____temp/`: 存在但为空（无残留下载文件）

### Qwen3-235B-GPTQ-Int4 — ⚠️ 下载未完成
- **路径**: `/root/autodl-tmp/models/Qwen3-235B-GPTQ-Int4/`
- safetensors: 主目录 **27/32**, `._____temp/` 中还有 **5 个** (25,26,27,29,31) 未移出
- config.json: ✅ 存在
- 缺失的 shard 仍在 temp 目录，说明下载可能中断或仍在进行中

---
