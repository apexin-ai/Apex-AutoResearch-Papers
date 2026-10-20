# analysis forward pass count audit

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_forward-pass-count-audit_20260515T164736_result.json`
- **Structured JSON:** [`2e6c34319c97bc6ade9d.json`](../../sessions/2e/2e6c34319c97bc6ade9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是审计结论。

---

## 审计结论

### 数据流全貌

```
injected_variants.jsonl (760 trajectories)
  ↓ convert_all_v4.py: 每条 trajectory 按 step 拆为 turn-level SFT 样本
  ↓ error tag 只标在每条 trajectory 的最后一步 (第 96 行: if i == len(steps) - 1)
  ↓
sft_taxei_v4.jsonl (9029 turns) = 4358 clean turns + 4671 injected turns
                                                       ↑
                                              760 有 tag + 3911 无 tag
```

### 1. Forward pass 760 injected 是什么粒度

**Turn 级，但数值恰好等于 trajectory 数量。**

`convert_all_v4.py:96` 只在每条 injected trajectory 的**最后一步**加 `[Error Type: ...]` tag。`classify_sample()` 按 tag 检测，所以 760 tagged turns = 760 trajectories = 一一对应。但其余 3911 个来自 injected trajectories 的 turn（非末尾步）被分类为 "clean"。

### 2. 4671 injected variants 是什么粒度

**Turn 级。** 760 条 injected trajectories 展开为 4671 个 per-step SFT 样本，平均 ~6.15 步/轨迹。

验证：9029 (sft_taxei_v4) − 4358 (sft_vanilla_v4) = **4671** ✓

### 3. Per-sample loss 分类问题

Loss 计算本身正确（per-turn response token CE loss），但**分类有污染**：

| Forward pass 分类 | 计数 | 真实构成 |
|---|---|---|
| "clean" = 8269 | 4358 真 clean + **3911 injected-provenance turns（无 tag）** |
| "injected" = 760 | 760 error-tagged final steps |

"Clean" mean loss (0.771) 被 3911 个来自 injected trajectories 的 turn 污染。

Dose-response ablation 一致性确认：
- inject10: 4358 total, 436 provenance-injected turns → 70 tagged (70/436≈16.1%)
- inject25: 4358 total, 1090 provenance-injected turns → 168 tagged (168/1090≈15.4%)
- inject50: 4358 total, 2179 provenance-injected turns → 370 tagged (370/2179≈17.0%)
- full: 9029 total, 4671 provenance-injected turns → 760 tagged (760/4671≈16.3%)

Tagged 比例恒定 ~16%，因为平均每条 trajectory ~6 步但只有 1 步有 tag。

### 4. 论文写作建议

应区分三个层级：
- **760 injected trajectories** — 被注入错误的完整轨迹数
- **4,671 injected turns** — 这些轨迹展开后的 SFT 训练样本数
- **760 error-tagged turns** — 实际携带 error tag 的样本数（每 trajectory 1 个）

如果 forward pass 分析要用 tag-based classification，需明确说明只覆盖 injected turns 的 ~16%。或者改用 provenance-based classification（`prepare_fixed_ablation_data.py` 已有实现：比对 vanilla user content set）来正确划分全部 4671 个 injected turns。

---
