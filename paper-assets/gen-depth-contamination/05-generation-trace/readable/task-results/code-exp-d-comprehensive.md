# code exp D comprehensive

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_D_comprehensive_20260515T113549_result.json`
- **Structured JSON:** [`a0f196fa009484920cc5.json`](../../sessions/a0/a0f196fa009484920cc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**修复后 OBD accuracy: 44.4%** (95% CI: [40.0%, 48.8%])

| 对比 | Accuracy |
|------|----------|
| Old (capping, no seed) | 43.6% |
| Old (v2, no seed) | 38.0% |
| **New (prob merge, seed=42)** | **44.4%** |

**多种子稳定性：5 个种子全部 44.4%，std=0.0。** GroupKFold 分折是确定性的，`random_state` 对 LightGBM 在这个数据规模/超参下几乎无影响，之前的 5.6pp 波动完全来自未固定种子+`n_jobs=-1` 的线程级不确定性。现在彻底消除。

**McNemar 结论不变，且更强：**
- OBD vs GPT-5.5: +11.2pp, p=0.0001, CI=[+5.6%, +16.8%]
- OBD vs Claude: +11.4pp, p=1.4e-5, CI=[+6.2%, +16.4%]

两个对比均显著 (p<0.001)，CI 不包含 0。可复现性验证通过（两次 seed=42 运行结果完全一致）。

---
