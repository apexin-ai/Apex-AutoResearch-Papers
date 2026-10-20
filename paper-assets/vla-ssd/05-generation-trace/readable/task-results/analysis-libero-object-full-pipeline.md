# analysis libero object full pipeline

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_libero_object_full_pipeline_20260521T050524_result.json`
- **Structured JSON:** [`685be31d9c5d43168438.json`](../../sessions/68/685be31d9c5d43168438.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验分析完成。

**`libero_object_full_pipeline` — FAILED**

| 项目 | 详情 |
|------|------|
| **失败原因** | 脚本在 RAM 中存储了 5000 个 L1 attention 矩阵（32×281×281 float32 ≈ 50GB），大概率 OOM 崩溃 |
| **完成度** | Phase 1（提取）完成，Phase 2（probing）仅到 L8，Phase 3-6 从未执行 |
| **结果文件** | 无（未写出任何 JSON） |
| **部分数据** | L0: img_mean R²=0.695, last_pre R²=0.571; L8: img_mean R²=0.673, last_pre R²=0.675 |

**重跑修复方向**：将 `extract_features` 中的 `l1_attns.append(l1)` 改为流式统计（提取时直接计算 per-head instruction ratio），不要在内存中保存全部 attention 矩阵。或拆分成多个阶段分别运行。

---
