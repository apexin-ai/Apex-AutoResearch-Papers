# check loop8 home full

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_loop8-home-full_20260514T052412_result.json`
- **Structured JSON:** [`bb239e25d786f71b45e7.json`](../../sessions/bb/bb239e25d786f71b45e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 服务器: home-1x5090 ===
GPU 0: RTX 5090 — 运行中 — eval_repo_cls v5 ckpt-4400 — 18429/32607 MiB (100% util)

=== CLS seed123 sweep (Qwen3-4B) ===
  ckpt-400:  acc=75.05%  f1_macro=67.47%  gap=+2.10pp
  ckpt-600:  acc=80.73%  f1_macro=77.31%  gap=+7.78pp  ★ best seed123
  ckpt-800:  acc=74.27%  f1_macro=66.03%  gap=+1.32pp  ↓ 过拟合
  ckpt-1000: acc=73.14%  f1_macro=52.10%  gap=+0.18pp  ↓↓ 严重退化

=== CLS v5 (seed42) sweep (Qwen3-4B) ===
  ckpt-600:  acc=76.74%  f1_macro=73.74%  gap=+3.78pp
  ckpt-4000: acc=81.51%  f1_macro=72.56%  gap=+8.55pp  ★ best v5 acc
  ckpt-4200: acc=80.64%  f1_macro=72.10%  gap=+7.69pp
  ckpt-4400: ⏳ 正在运行
  ckpt-4600: 待运行

=== baseline ===
  v4 ckpt-200: acc=66.11%  f1_macro=56.61%  gap=-6.85pp
  majority:    acc=72.96%

=== 关键发现 ===
1. seed123: ckpt-600 是明确最优点，之后持续退化（f1_macro 从 77.31→66.03→52.10）
2. v5: ckpt-4000 accuracy 最高 81.51%，但 f1_macro (72.56) 低于 seed123 ckpt-600 (77.31)
3. v5 accuracy 高但 f1_macro 低 → fail 类 recall 差（45%），模型偏向预测 pass
4. seed123 ckpt-600 在 fail recall (77.44%) 上远优于 v5 所有 checkpoint
```

---
