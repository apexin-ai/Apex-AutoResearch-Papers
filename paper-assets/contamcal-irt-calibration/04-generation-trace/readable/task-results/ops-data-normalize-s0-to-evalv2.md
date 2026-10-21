# ops data normalize s0 to evalv2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_data-normalize-s0-to-evalv2_20260521T071035_result.json`
- **Structured JSON:** [`fe71819d1e4972a510c5.json`](../../sessions/fe/fe71819d1e4972a510c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

```
=== 归一化完成 ===
Qwen-14B s0 MMLU: 5/5 dosages → results/mmlu_eval/qwen14b/
  d000=68.84 d005=68.86 d025=65.05 d050=55.33 d100=43.85 ✅

Qwen-14B s0 ARC: 5/5 dosages → results/arc_eval/qwen14b/
  d000=90.44 d005=90.19 d025=89.93 d050=86.35 d100=81.06 ✅

Qwen-7B s0 MMLU: 5/5 dosages → results/mmlu_eval/qwen7b/
  d000=66.32 d005=64.68 d025=65.67 d050=65.78 d100=65.29 ✅

Qwen-7B s0 ARC: 5/5 dosages → results/arc_eval/qwen7b/
  d000=87.20 d005=85.32 d025=84.47 d050=85.58 d100=85.32 ✅

验证: 所有 accuracy 值与 registry 一致 ✅
```

操作详情：
- Qwen14B: d050/d100 从 westd 本地独立目录 (`results/qwen14b_d{050,100}_s0_{mmlu,arc}/`) 复制到标准路径
- Qwen7B: 全部 5 个 dosage 从 cqa1 (`/root/autodl-tmp/exp001/eval_results_v2/`) SCP 到 westd 标准路径
- Qwen7B arc_eval 目录之前只有 s123/s42，现在补齐了 s0

---
