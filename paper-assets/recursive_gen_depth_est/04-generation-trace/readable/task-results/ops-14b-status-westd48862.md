# ops 14b status westd48862

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_14b-status-westd48862_20260518T034420_result.json`
- **Structured JSON:** [`756ddfb75efb70b2a888.json`](../../sessions/75/756ddfb75efb70b2a888.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态: 运行中

| 项目 | 状态 |
|---|---|
| PID | 20700 活跃，GPU 0 占用 32GB，利用率 92% |
| 当前阶段 | **Phase 3.1b: 生成 d1** |

### 已完成
- d0 生成: **5000/5000** (7.1MB)
- d0 LoRA 微调: 完成，loss=0.5451，adapter 已保存
- d1 生成: **2523/5000** (4.3MB，进行中)

### 待完成
- d1 生成剩余 ~2477 samples
- d1 LoRA 微调
- d2 生成 + LoRA 微调
- d3 生成
- RF 训练 + 评估

### ETA 估算
d0 生成 5000 samples 用了约 4 小时（03:10→07:56）。d1 已完成 ~50%，开始于 ~08:38，当前 11:44 已跑 ~3 小时。按此速度：
- d1 生成剩余: ~3h
- d1 LoRA 微调: ~40min
- d2 生成+微调: ~5h
- d3 生成: ~4h
- RF 训练: ~10min

**预计总剩余 ~13h，完成时间约明天凌晨。**

---
