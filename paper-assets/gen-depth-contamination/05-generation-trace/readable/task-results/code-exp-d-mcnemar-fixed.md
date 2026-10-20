# code exp D mcnemar fixed

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_D_mcnemar_fixed_20260515T113431_result.json`
- **Structured JSON:** [`90b4d13f70a5d0e1392b.json`](../../sessions/90/90b4d13f70a5d0e1392b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

```
=== FIX COMPARISON ===
Old (capping, no seed):     43.6%
Old (v2, no seed):          38.0%
New (prob merge, seed=42):  44.4%  CI=[40.0%, 48.8%]

Per-depth: d0=96%, d1=36%, d2=8%, d3=2%, d4=80%

McNemar vs GPT-5.5:  p=0.0001  diff=+11.2%  CI=[+5.6%, +16.8%]
McNemar vs Claude:   p=1.4e-5  diff=+11.4%  CI=[+6.2%, +16.4%]
```

- 500 samples 全部对齐，无 skip
- 两次运行结果完全一致，`random_state=42` 生效
- 无 `min(pred, 4)` 残留（OBD 用概率合并，LLM 保留 cap at 4）
- JSON 已保存到 `artifacts/rebuttal/exp_D_mcnemar_fixed.json`

---
