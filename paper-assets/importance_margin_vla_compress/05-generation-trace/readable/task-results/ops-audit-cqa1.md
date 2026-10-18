# ops audit cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit-cqa1_20260527T171326_result.json`
- **Structured JSON:** [`c5cc7900f8c3f9e780fa.json`](../../sessions/c5/c5cc7900f8c3f9e780fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cqa1-33015 GPU 审计结果

| GPU | 状态 | PID | 实验 | 进度 | 备注 |
|-----|------|-----|------|------|------|
| **GPU0** | **完成 ✓** | 300488 (已退出) | eval_pi05_attn_k075_long_seed42_strict | **SR=52.4%** (10 tasks done) | EXIT_CODE=0, 01:02完成 |
| **GPU1** | 运行中 | 328563 | eval_pi05_attn_k07_long_seed42_strict | T8 ep30, 228/400=57.0% | ~2h剩余 |
| **GPU1** | 运行中 | 330514 | eval_pi05_random_k09_long_seed43_strict_v2 | T7 ep20, 107/350=30.6% | ~2.5h剩余 |
| **GPU2** | 运行中 | **503250** (非503245) | eval_pi05_attn_k09_long_seed43_strict | T1完成, 67/100=67.0% | 刚启动，~4h剩余 |
| **GPU3** | 运行中 | 386864 | eval_pi05_l2norm_k09_long_seed43_strict | T8 ep10, 331/400=82.8% | ~1.5h剩余 |

**GPU0 完成结果明细** (attn k=0.75 long seed42):
```
T0=82% T1=94% T2=64% T3=48% T4=26% T5=50% T6=76% T7=30% T8=6% T9=78%
Overall: 262/500 = 52.4%
```

**GPU0 现在空闲，可部署新实验。**

---
