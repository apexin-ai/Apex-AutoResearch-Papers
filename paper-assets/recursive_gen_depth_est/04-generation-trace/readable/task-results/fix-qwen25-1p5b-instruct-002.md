# fix qwen25 1p5b instruct 002

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_qwen25-1p5b-instruct-002_20260517T185750_result.json`
- **Structured JSON:** [`95a0aaad6d562987882c.json`](../../sessions/95/95a0aaad6d562987882c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 正常运行中：

- Phase 2-3 全部跳过（数据和 checkpoint 已存在）
- Phase 4 特征提取已启动，BF16 修复生效，d0 正在以 ~48 it/s 提取（无报错）
- 约 ~47 it/s × 20000 samples ≈ 7 分钟完成 Phase 4，Phase 5 分类很快

**汇总**：
- **修复内容**：line 319 的 `.float()` 已就位（BF16→FP32 转换），脚本中唯一的 `.numpy()` 调用
- **跳过逻辑**：脚本原有的跳过逻辑覆盖了所有 Phase（d0-d3 数据、LoRA adapter、features.npz）
- **实验 qwen25-1p5b-instruct-002**：已提交至 gpu-6000pro-2 cuda:1，Phase 4 正在执行

---
