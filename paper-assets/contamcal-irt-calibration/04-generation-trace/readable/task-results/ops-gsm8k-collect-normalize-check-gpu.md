# ops gsm8k collect normalize check gpu

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gsm8k-collect-normalize-check-gpu_20260521T073557_result.json`
- **Structured JSON:** [`488fca90d81c491da364.json`](../../sessions/48/488fca90d81c491da364.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 任务 1: GSM8K 结果 ===
Gemma-2 d000 s0: 仍在运行 (PID 492703, GPU 0, elapsed 23min)
Qwen-14B d050 s0: 仍在运行 (PID 492186, GPU 2, elapsed 24min)
Phi-4 d000 s0: 仍在运行 (PID 493644, GPU 3, elapsed 22min)
Qwen-14B d100 s0: 仍在运行 (PID 481803, GPU 1, elapsed 1h33min)

=== 任务 2: 数据归一化 ===
MMLU s0:
  Qwen-7B:  5/5 dosage dirs ✓
  Qwen-14B: 5/5 dosage dirs ✓
  OLMo-2:   5/5 dosage dirs ✓
  Gemma-2:  5/5 dosage dirs ✓
  Phi-4:    5/5 dosage dirs ✓
ARC s0:
  Qwen-7B:  5/5 dosage dirs ✓
  Qwen-14B: 5/5 dosage dirs ✓
  OLMo-2:   5/5 dosage dirs ✓
  Gemma-2:  5/5 dosage dirs ✓ (+d025_s0_rerun)
  Phi-4:    5/5 dosage dirs ✓
Spot check:
  Qwen-7B d000_s0 MMLU acc=66.32% ✓
  Qwen-14B d100_s0 ARC acc=81.06% ✓
  Qwen-14B d100_s0 MMLU acc=43.85% ⚠️ (偏低，可能需确认)

=== 任务 3: GSM8K 覆盖矩阵 ===
```

| Family | s0 | s42 | s123 |
|--------|----|-----|------|
| **Qwen-7B** | d000=73.31 d005=78.32 d025=78.24 d050=79.38 d100=81.20 ✅5/5 | d000=70.58 d005=76.95 d025=80.06 d050=79.23 d100=81.65 ✅5/5 | d000=70.05 d100=79.23 ⬜2/5 |
| **Qwen-14B** | d000=74.98 d005=71.19 d025=79.30 d050=🔄 d100=🔄 ⬜3/5 | d000=60.80⚠️ d100=81.27 ⬜2/5 | d000=76.65 d100=82.34 ⬜2/5 |
| **Phi-4** | d000=🔄 ⬜0/5 | ⬜0/5 | d000=84.31 d100=83.85 ⬜2/5 |
| **OLMo-2** | ⬜0/5 | d000=68.46 d100=70.20 ⬜2/5 | d000=66.26 d100=68.69 ⬜2/5 |
| **Gemma-2** | d000=🔄 ⬜0/5 | d000=13.87/11.22❌ d100=3.94❌ ⚠️全坏 | ⬜0/5 |

```
🔄 = 正在运行   ❌ = 结果异常（Gemma-2 s42 acc极低，疑 evaluate 脚本/adapter 问题）

已完成: 32/75 配置点 (42.7%)
Qwen-7B 最完整 (12/15), Gemma-2 最缺 (0/15 有效)

⚠️ Qwen-14B d000_s42 = 60.80% 显著低于 d000_s0(74.98%) 和 d000_s123(76.65%)，可能需核查

=== GPU 空闲列表 ===
westd: 0/4 GPU 空闲（全部在跑 GSM8K eval）
cqa1:  1/1 GPU 空闲 (24GB, 0% util)
  → 可跑: Qwen-7B s123 中间 dosage (d005/d025/d050) — 按 C007 优先级最高
```

---
