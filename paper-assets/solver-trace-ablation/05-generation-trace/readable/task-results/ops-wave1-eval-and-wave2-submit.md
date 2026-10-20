# ops wave1 eval and wave2 submit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_wave1-eval-and-wave2-submit_20260517T082202_result.json`
- **Structured JSON:** [`a46a22404e82f3e359c5.json`](../../sessions/a4/a46a22404e82f3e359c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

sweep-isr-b005-s43 训练已启动，step 1 完成。两个 GPU 都在跑训练。

汇报结果：

```
== 实验状态 ==
plan018-additive-random-b01-s45: [完成] step 500/500 — 训练+eval+H7 全部完成
sweep-random-b005-s42:           [完成] step 500/500 — 训练+eval+H7 全部完成
sweep-random-b005-s43:           [进行中] step ~40/500 (GPU 1, PID 240152) — 原 run OOM 崩溃后已重启

== Eval 结果 ==
plan018-additive-random-b01-s45 (Random β=0.1 seed=45):
  PR: 58/100, H7: 0, H1: 53, H8: 0, genuine: 5 (8.6%)
  Mean ISR: 0.0096, Proved-only ISR: 0.0166

sweep-random-b005-s42 (Random β=0.05 seed=42):
  PR: 0/100, H7: 0, H1: 0, H8: 0, genuine: 0 (0.0%)
  Mean ISR: 0.0000
  ⚠️ 模型完全失败，β=0.05 random 信号太弱

== Wave 2 提交 ==
sweep-isr-b005-s43 (ISR β=0.05 seed=43): PID 243079 on cuda:0, step 1/500 running

== 注意事项 ==
1. 实际输出目录使用下划线 (plan018_random_b01_s45) 而非连字符
2. sweep-random-b005-s43 第一次 run 因 GPU 0 被 plan018 占用导致 OOM，已在 GPU 1 重启
3. sweep_random_b005_s42 的 0% PR 值得关注：β=0.05 的 random bonus 在 500 步内不足以学到 formalization 能力
```

---
