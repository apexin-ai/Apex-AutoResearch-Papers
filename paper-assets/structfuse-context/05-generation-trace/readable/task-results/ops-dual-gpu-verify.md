# ops dual gpu verify

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_dual-gpu-verify_20260513T090837_result.json`
- **Structured JSON:** [`fdceac12de15aaa348ad.json`](../../sessions/fd/fdceac12de15aaa348ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 双卡状态报告

### GPU 全貌

| GPU | 型号 | 利用率 | 显存占用 | PID | 进程 |
|-----|------|--------|----------|-----|------|
| 0 | RTX PRO 6000 Blackwell | **100%** | 24227/97887 MiB | 27234 | plan_013 StarCoder2-3B embedding_distance |
| 1 | RTX PRO 6000 Blackwell | **100%** | 22179/97887 MiB | 37880 | m2_embed_verify Qwen2.5-Coder-3B embedding_distance |

**双卡满载，无空闲。**

### 进程详情

**GPU 0 — plan_013_starcoder (PID 27234)**
- 运行时间：2h43m，wrapper PID 23798 (3h42m) 存活
- 当前：embedding_distance 策略，step 1500/~1700，Epoch 2 尾声
- 最佳 val_loss=0.4816 @ step 1000，recall@1=0.508，recall@5=0.984，recall@10=1.0
- auto_start PID 38446 存活（3m56s），正在等待 PID 27234 完成

**GPU 1 — m2_embed_verify (PID 37880)**
- 运行时间：4m23s，刚启动
- 当前：embedding_distance 策略刚开始（17:04:42 启动），step 50，loss=0.5951
- 之前的 random 策略已于 17:04:42 完成并清理了中间 checkpoint
- random 策略结果：recall@1=0.512，recall@5=0.983，recall@10=1.0，val_loss=0.598

### 结论

无需干预。两张卡都在正常跑 embedding_distance 策略训练。m2_embed_verify 在 GPU 1 上刚切换到 embedding 策略，不是"空闲"——上次检查时可能恰好在策略切换间隙。

---
