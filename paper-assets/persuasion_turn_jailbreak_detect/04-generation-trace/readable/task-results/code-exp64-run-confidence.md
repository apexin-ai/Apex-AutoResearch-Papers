# code exp64 run confidence

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp64_run_confidence_20260522T222800_result.json`
- **Structured JSON:** [`61679608379716c7b762.json`](../../sessions/61/61679608379716c7b762.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，hypothesis **confirmed (success)**。关键发现：

### Majority Vote 对比

| 指标 | 9-class | jb_mlm |
|------|---------|--------|
| 总 FP 数 | 104 | 34 |
| 高置信 (>0.9) 占比 | **70.2%** | 58.8% |
| Borderline (0.5-0.7) 占比 | 25.0% | 14.7% |
| 均值 | 0.9014 | 0.8334 |
| 中位数 | 0.9999 | 0.9327 |

### Per-seed 更能说明问题

9-class 单 seed 的高置信 FP 占比高达 **94.3%–97.7%**（几乎全部 FP 的置信度 > 0.9，中位数直接 1.0）。Majority vote 中 25% borderline 只是因为跨 seed 投票拉低了聚合置信度——单个模型几乎不产生 borderline FP。

jb_mlm 单 seed 高置信 FP 占比在 41.2%–68.9% 之间，分布更分散，有明显的低/中置信 FP。

### 结论

9-class 的高 FPR 不是边界模糊导致的，而是模型对 ToxicChat benign 文本产生了**系统性的高置信误判**——classification DAPT 导致了特征空间的整体偏移，使模型"确信"这些 benign 文本是 jailbreak。

---
