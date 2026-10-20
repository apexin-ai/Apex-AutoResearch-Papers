# ops gpu status collect results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-collect-results_20260521T060921_result.json`
- **Structured JSON:** [`aeb6b59419d99d8dbe07.json`](../../sessions/ae/aeb6b59419d99d8dbe07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部收齐。

```
=== GPU 状态 ===
westd cuda:0: IDLE (0 MiB)
westd cuda:1: RUNNING — eval_qwen14b_d100_s0_gsm8k (PID 481792, 运行 5h53m, 进度 37/660 ≈ 5.6%, ETA ~1h35m)
westd cuda:2: IDLE (0 MiB)
westd cuda:3: IDLE (0 MiB)
cqa1  cuda:0: IDLE (0 MiB)

=== 已完成 eval 结果 ===
Qwen2.5-14B d050 s0 ARC:  86.35% (1012/1172) ✓ 新结果
Qwen2.5-14B d050 s0 MMLU: 55.33% (7770/14042) ✓ 新结果
Qwen2.5-14B d100 s0 ARC:  81.06% (950/1172)  ✓ 新结果
Qwen2.5-14B d100 s0 MMLU: 43.85% (6157/14042) ✓ 新结果
Qwen2.5-14B d100 s0 GSM8K: 仍在运行 (37/660, ~5.6%)

Qwen2.5-7B s0 GSM8K 全部完成 (cqa1):
  d000: 73.31%
  d005: 78.32%
  d025: 78.24%
  d050: 79.38%
  d100: 81.20%

=== 空闲 GPU ===
westd cuda:0 — 空闲
westd cuda:2 — 空闲
westd cuda:3 — 空闲
cqa1  cuda:0 — 空闲
```

**4 个 GPU 空闲。** westd 仅 cuda:1 在跑 d100 GSM8K（14B 模型 batch_size=2，~9.4s/it，预计还需 ~1.5h）。cqa1 的 Qwen-7B GSM8K 全 5 个 dosage 已完成，进程已退出。

注意：westd 尚缺 `qwen14b_d050_s0_gsm8k` 结果（gsm8k_eval 目录下有 d000/d005/d025/d100 但没有 d050）。d100 完成后可考虑提交 d050 GSM8K。

---
