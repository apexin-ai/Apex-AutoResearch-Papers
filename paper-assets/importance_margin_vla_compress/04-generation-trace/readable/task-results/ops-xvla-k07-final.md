# ops xvla k07 final

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_xvla-k07-final_20260520T104742_result.json`
- **Structured JSON:** [`a0e8c0b876307f9912c4.json`](../../sessions/a0/a0e8c0b876307f9912c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Batch 1 最终结果 (全部完成):
  k=1.0: SR=99.2% (50/50 tokens, 496/500)
  k=0.95: SR=99.0% (47/50 tokens, 495/500)
  k=0.9: SR=97.6% (45/50 tokens, 488/500)
  k=0.7: SR=56.2% (35/50 tokens, 281/500)  ← 断崖式下降
    per-task:
      T0 alphabet_soup: 94%
      T1 cream_cheese:   2%  ← 崩溃
      T2 salad_dressing: 100%
      T3 bbq_sauce:      80%
      T4 ketchup:        28% ← 崩溃
      T5 tomato_sauce:   92%
      T6 butter:         12% ← 崩溃
      T7 milk:           66%
      T8 choco_pudding:   0% ← 完全失败
      T9 orange_juice:   88%

Batch 2: 已启动 (18:19 启动，4 个 k 值各占 1 张 GPU 并行跑)
  k=0.5 (25 tokens): Task 4/10 ep 10/50 → ~210/500 ≈ 42%
    已完成: T0=58%, T1=2%, T2=74%, T3=78%
  k=0.3 (15 tokens): Task 3/10 ep 8/50 → ~158/500 ≈ 32%
    已完成: T0=30%, T1=0%, T2=32%
  k=0.2 (10 tokens): Task 2/10 ep 39/50 → ~139/500 ≈ 28%
    已完成: T0=6%, T1=0%（几乎全 FAIL，每 ep 800 步跑满）
  k=0.1 (5 tokens):  Task 2/10 ep 41/50 → ~141/500 ≈ 28%
    已完成: T0=0%, T1=0%（全 FAIL）

GPU 占用: 4 卡均有进程，各 ~4.4-4.9 GB / 97.9 GB，利用率 1%（推理间歇）

预估: Batch 2 低 k 值几乎全 FAIL（每 ep 必跑满 800 步），比 Batch 1 慢很多。
已运行 ~29 min，完成 ~30%，预计还需 ~50-70 min 全部完成。
```

关键发现：k=0.9→0.7 存在**断崖**（97.6% → 56.2%），k≤0.3 的 SR 预计趋近 0。X-VLA 对 vision token 裁剪非常敏感，保留比例的 "安全区" 在 90% 以上。

---
