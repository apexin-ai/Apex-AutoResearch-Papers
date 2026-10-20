# check seed123 progress

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_seed123_progress_20260514T034304_result.json`
- **Structured JSON:** [`24e748448db01ee9dfd0.json`](../../sessions/24/24e748448db01ee9dfd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态报告已写到 `artifacts/status_check_seed123.md`。

**摘要：**

| 实验 | GPU | 进度 | 预估完成 |
|------|-----|------|----------|
| uncurated seed=123 | cuda:0 | **Gen 6/7 训练中** | ~12:20 CST |
| chain 后续 (rgds→random50) | cuda:0 | 未开始 | ~15:20 CST |
| external_only seed=123 | cuda:1 | **Gen 0/7 训练中** | ~13:50 CST |
| auto_cuda1 (random50) | cuda:1 | 等待 external 完成 | external 后 ~90min |

两块 GPU 均正常工作，无异常。uncurated 马上收尾（还剩 ~1.5 gen），external 刚起步。Flag 文件不存在，auto_cuda1 仍在等待。

---
