# code exp D final

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_D_final_20260515T114128_result.json`
- **Structured JSON:** [`4629ec658bed279387d5.json`](../../sessions/46/4629ec658bed279387d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

```
=== EXP-D FINAL (v2 logic + seed=42) ===
OBD accuracy: 38.0% [CI: 34.0%, 42.2%]
Per-depth: d0=96% d1=39% d2=14% d3=19% d4=22%

McNemar vs GPT-5.5: diff=+4.8pp, p=0.0809, CI=[-0.4%, 10.0%], includes_zero=YES
McNemar vs Claude:   diff=+5.0pp, p=0.0693, CI=[0.0%, 10.2%], includes_zero=YES

Multi-seed: [38.0, 38.0, 38.0, 38.0, 38.0] mean=38.0 ± 0.0

Sensitivity:
  v2 (no seed):         38.0%
  capping (no seed):    43.6%
  prob merge (seed=42): 44.4%
  v2 logic (seed=42):   38.0%  ← THIS
```

关键发现：
- v2 逻辑 + seed=42 得到 **38.0%**，与之前 v2 no-seed 结果完全一致（多种子 std=0.0，GroupKFold 是确定性的，seed 只影响 LightGBM 内部微小差异，最终 argmax 结果不变）
- McNemar 两个对比均 **不显著**（p=0.081 vs GPT, p=0.069 vs Claude），CI 均包含零
- JSON 已保存至 `artifacts/rebuttal/exp_D_mcnemar_final.json`

---
