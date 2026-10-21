# ops 14b status westd

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_14b-status-westd_20260518T030323_result.json`
- **Structured JSON:** [`f3a2210f7794947affc6.json`](../../sessions/f3/f3a2210f7794947affc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态：运行中

**PID 20700** — GPU 0 上活跃，92% util，32GB VRAM

### 进度

| Phase | 状态 | 详情 |
|-------|------|------|
| d0 生成 | ✅ 完成 | 5000/5000 samples |
| d0 LoRA finetune | ✅ 完成 | loss=0.5451, 3 epochs, ~41min |
| d1 生成 | 🔄 进行中 | **1969/5000** (~39%) |
| d1 LoRA finetune | ⏳ 待开始 | |
| d2 生成 | ⏳ 待开始 | |
| d2 LoRA finetune | ⏳ 待开始 | |
| d3 生成 | ⏳ 待开始 | |
| RF 训练 | ⏳ 待开始 | |

### ETA 估算

d1 文件创建于 ~08:38，到 11:03 生成了 1969 samples（~820 samples/hr）。剩余 3031 samples 约需 3.7h。

后续每个 depth 大约：生成 ~6h + finetune ~41min。还剩 d1 尾部 + d2 全程 + d3 全程 + RF，预计总完成时间约 **5月19日凌晨 04:00-05:00**。

---
