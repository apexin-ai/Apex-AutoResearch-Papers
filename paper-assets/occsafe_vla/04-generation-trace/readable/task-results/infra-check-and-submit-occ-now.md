# infra check and submit occ NOW

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_and_submit_occ_NOW_20260520T153734_result.json`
- **Structured JSON:** [`b63a4688ae755c2b4b0d.json`](../../sessions/b6/b63a4688ae755c2b4b0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 0/1/2 被 vanilla baseline 训练占用，无法立即启动 occ 训练。**

当前状态：

| 运行 | GPU | 进度 | 速度 | 预计剩余 |
|------|-----|------|------|---------|
| vanilla_s0 | GPU 0 | 22,804 / 50,005 (46%) | ~1.08 it/s | ~7h |
| vanilla_s1 | GPU 1 | 22,608 / 50,005 (45%) | ~1.09 it/s | ~7h |
| vanilla_s2 | GPU 2 | 22,485 / 50,005 (45%) | ~1.07 it/s | ~7.1h |
| — | GPU 3 | 空闲 | — | — |

已完成的准备工作：
- occ 提取：9/9 tasks 全部完成 (westd-34685)
- occ_index.json：已构建，**9 tasks, 450 demos**
- wooden_cabinet occ 文件：已删除
- 损坏的 wooden_cabinet libero 文件：已清理

**选项：**
1. **Kill vanilla runs** → 立即启动 3 个 occ 训练（vanilla 已有 20k checkpoint 可用）
2. **等 ~7 小时** → vanilla 跑完后自动排队
3. **先在 GPU 3 启动 1 个 occ 训练**（occ_s0），其余等 vanilla 完成

怎么选？

---
