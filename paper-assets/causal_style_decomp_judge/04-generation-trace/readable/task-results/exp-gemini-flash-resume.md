# exp gemini flash resume

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_gemini_flash_resume_20260521T222909_result.json`
- **Structured JSON:** [`a2575cc095464bd9705e.json`](../../sessions/a2/a2575cc095464bd9705e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。实际使用模型为 `google/gemini-2.5-flash`。

---

```
Gemini Flash (google/gemini-2.5-flash)

Formality (n=88 pairs):
  BT: P(formal) = 57.4% [50.0, 64.2] p=0.0306
  Likert: ATE=-0.239 d=-0.082 p=0.309
  GEE: Style OR=1.64 [0.91, 2.98] p=0.1008, Orig OR=2.51 [1.39, 4.54] p=0.0024
  Blindspot: Yes
  Regime: Orig-Dominated

Verbosity (n=86 pairs):
  BT: P(verbose) = 70.8% [63.7, 77.2] p=0.0000
  Likert: ATE=0.151 d=0.051 p=0.370
  GEE: Style OR=8.98 [3.68, 21.94] p=0.0000, Orig OR=0.46 [0.20, 1.04] p=0.0614
  Blindspot: Yes
  Regime: Pure Style
```

**备注**：
- Verbosity 有 1 个缺失 trial（mvp_0041 trial2=None），共 171 comparisons（非 172）
- 两轴均确认 blindspot：BT 显著而 Likert 不显著
- Formality 的 pairwise 偏好由 position bias（Orig OR=2.51）驱动而非 style；Verbosity 则是纯 style 效应（OR=8.98）

---
