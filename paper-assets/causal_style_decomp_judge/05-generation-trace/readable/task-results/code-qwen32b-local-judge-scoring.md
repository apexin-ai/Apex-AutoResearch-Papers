# code qwen32b local judge scoring

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen32b_local_judge_scoring_20260521T041022_result.json`
- **Structured JSON:** [`fb633d5e4782f0c279e0.json`](../../sessions/fb/fb633d5e4782f0c279e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== Qwen3-32B Local Judge Results ===

Formality (n=88, NLI≥0.90):
  Pairwise: consistency=65.0%, formal_win=76.4%, sign_test_p=0.000114, Wilson CI [0.637, 0.856]
  Likert: ATE=0.011, p=0.908, d=0.012, tie_rate=72.7%
  vs GPT-4o: pairwise [63.0% → 76.4%↑], Likert [p=0.332 → p=0.908, both non-sig]

  Directional:
    formal→casual: 81.4% prefer original (p=0.000042)
    casual→formal: 50.0% (p=1.000, no preference)

Verbosity (n=86, NLI≥0.90):
  Pairwise: consistency=74.0%, verbose_win=87.3%, sign_test_p<0.000001, Wilson CI [0.769, 0.934]
  Likert: ATE=-0.151, p=0.179, d=-0.146, tie_rate=58.1%

  Directional:
    verbose→concise: 80.6% prefer original (p=0.000878)
    concise→verbose: 90.7% prefer rewrite (p<0.000001)

Register (n=94, NLI≥0.90):
  Pairwise: consistency=60.0%, academic_win=59.3%, sign_test_p=0.220, Wilson CI [0.460, 0.713]
  Likert: ATE=0.074, p=0.505, d=0.069, tie_rate=63.8%

  Directional:
    academic→conversational: 89.3% prefer original (p=0.000027)
    conversational→academic: 31.2% (p=0.050, marginal)
```

**关键发现：**

1. **Verbosity bias 最强**：pairwise 87.3% 选 verbose (p<10⁻⁶)，Likert 无差异 (p=0.179)。Pairwise-Likert 分离比 formality 更极端——Qwen3-32B 在 pairwise 中系统性偏好冗长回复，但 Likert 评分不反映这种偏好。

2. **Formality bias 显著增强**（vs GPT-4o）：pairwise formal win 从 GPT-4o 的 63.0% 升至 76.4%，方向性分析显示 formal→casual 方向偏好极强 (81.4%, p<0.0001)，但 casual→formal 方向无偏好 (50%)——说明这更多是 originality bias 而非 formality bias。Likert 同样是 blindspot (p=0.908)。

3. **Register bias 弱且不显著**：pairwise academic win 仅 59.3% (p=0.220)，但方向性分析揭示强 originality bias（academic→conv 89.3% prefer original，conv→academic 31.2% prefer original），两个方向几乎对称地偏好 original。

4. **所有三个 axis 的 Likert 都是 blindspot**：p 值分别为 0.908, 0.179, 0.505——完全无法检测到 pairwise 发现的偏好差异。Tie rate 高达 58-73%，证实 Qwen3-32B 作为 Likert judge 的区分力极差。

---
