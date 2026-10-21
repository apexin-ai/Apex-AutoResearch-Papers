# ops eval status eta

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-status-eta_20260523T063905_result.json`
- **Structured JSON:** [`2f44a711820aa6609786.json`](../../sessions/2f/2f44a711820aa6609786.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. Checkpoint
`adapter_model.safetensors` 存在，177MB，正常。

### 2. Eval 运行状态
**正在运行** — 脚本 `run_falcon3_eval.sh` 包含两个 eval 任务，顺序执行：

| # | 任务 | Benchmarks | 状态 |
|---|------|-----------|------|
| 1 | Falcon3-7B volume_control | MMLU + ARC + GSM8K | GSM8K 进行中 |
| 2 | Falcon3-7B d000 baseline | GSM8K | 排队中 |

### 3. 进度明细

**Eval 1 (volume_control):**
- MMLU (14042 items): **已完成** @ 14:22，准确率见结果文件
- ARC (1172 items): **已完成** @ 14:27，准确率 **83.28%**
- GSM8K (660 items): **101/660 (15%)**, ~7.1s/item

**Eval 2 (d000 baseline):**
- GSM8K: 等 Eval 1 完成后启动

### 4. ETA 估算

| 阶段 | 剩余量 | 预估耗时 |
|------|--------|---------|
| GSM8K volume_control | 559 items × 7.1s | ~66 min |
| 模型重新加载 (d000 base) | — | ~5 min |
| GSM8K d000 | 660 items × ~7s | ~77 min |
| **合计** | | **~148 min (~2.5h)** |

**预计全部完成时间：~17:10 CST**

bitsandbytes 的 `libnvJitLink.so.13` 错误是非致命 warning，不影响 eval 结果。

---
