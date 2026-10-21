# eval gemma2 arc s42 execute

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_gemma2-arc-s42-execute_20260521T064754_result.json`
- **Structured JSON:** [`16d713c23a3437a5bd87.json`](../../sessions/16/16d713c23a3437a5bd87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0/2/3 已释放。结果汇总：

```
=== Gemma-2-9B ARC s42 Results ===
d000: 86.01% (1008/1172) — results/arc_eval/gemma2/d000_s42/arc_challenge_results.json
d005: 77.82% (912/1172)
d025: 87.37% (1024/1172)
d050: 71.08% (833/1172)
d100: 84.81% (994/1172)

Delta(d100-d000): -1.19pp

C009: ✅ md5=17673bf373f00f83ccc41fc1d355a4cd
C006: ✅ 全部 5 个 adapter alpha=32
GPU PIDs: cuda:0=[486175], cuda:2=[487120], cuda:3=[488033]（已全部完成释放）
GPU 0/2/3 现已空闲，GPU 1 Qwen-14B (PID 481803) 未受影响。
```

注意：dosage 曲线非单调（d005=77.82% < d000=86.01%，d050=71.08% 是最低点），这可能值得 Reviewer 关注。

---
