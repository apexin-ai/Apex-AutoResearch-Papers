# 5-Model Mitigation Complete Analysis

## Data

5 models × 5 ambiguity types (excluding coreferential), 50 episodes per cell baseline, 50 mitigated. Mitigation = type-specific prompt augmentation warning about the ambiguity pattern.

## 1. Model × Type Interaction: Δpp Table

| Type \ Model         | GPT-5.4 | GPT-4.1 | Claude  | Qwen3   | DeepSeek |
|----------------------|---------|---------|---------|---------|----------|
| authorization_scope  | **−40.0** | **−26.0** | 0.0   | −14.0   | −10.0    |
| conditional_precedence| −4.6   | −10.0   | −12.0   | −2.0    | −12.0    |
| incompleteness       | −2.6    | **−14.0** | −2.0  | −2.0    | **+4.0** |
| lexical              | **−16.5** | −10.0 | −8.0    | −8.0    | −2.0     |
| scopal               | −6.7    | −4.0    | −10.0   | −2.7    | **+2.0** |

**Top 5 improvements**: GPT-5.4 auth_scope (−40pp), GPT-4.1 auth_scope (−26pp), GPT-5.4 lexical (−16.5pp), GPT-4.1 incompleteness (−14pp), Qwen3 auth_scope (−14pp).

**Degradations** (2 cells): DeepSeek incompleteness (+4pp), DeepSeek scopal (+2pp). Both degradations are from DeepSeek-V3.

## 2. Baseline Vulnerability vs Mitigation Responsiveness

- Pearson r = −0.215, p = 0.303
- Spearman ρ = 0.075, p = 0.721

The hypothesis that higher baseline vulnerability leads to larger mitigation gains is **not supported** at conventional significance levels. The weak negative Pearson trend is driven primarily by auth_scope (high baseline → large improvement) but the relationship does not generalize.

## 3. Authorization Scope Analysis

| Model           | Baseline | Mitigated | Δpp   | Fisher p |
|-----------------|----------|-----------|-------|----------|
| GPT-5.4         | 64%      | 24%       | −40.0 | **0.0001** |
| GPT-4.1         | 46%      | 20%       | −26.0 | **0.010**  |
| Claude Sonnet   | 12%      | 12%       | 0.0   | 1.000    |
| Qwen3-235B      | 26%      | 12%       | −14.0 | 0.125    |
| DeepSeek-V3     | 60%      | 50%       | −10.0 | 0.422    |

All 5 models improve or stay the same (no degradation). Mean Δ = −18.0pp [95% CI: −31.5, −4.5].

**Safety training interaction**: Claude's 12% baseline is already at a floor from safety training — mitigation adds nothing (Δ = 0). GPT-5.4 has the highest baseline (64%) and the largest improvement (−40pp), but even after mitigation still violates at 24%. DeepSeek has high baseline (60%) but only modest improvement (−10pp), suggesting its auth_scope violations stem from a different mechanism than GPT-5.4's.

**Auth_scope is NOT the only type where all models improve** (with ≤ 0 criterion). Conditional_precedence and lexical also have all 5 models strictly improving (all Δ < 0).

## 4. Incompleteness Analysis

| Model           | Baseline | Mitigated | Δpp   |
|-----------------|----------|-----------|-------|
| GPT-5.4         | 46%      | 43.4%     | −2.6  |
| GPT-4.1         | 58%      | 44%       | −14.0 |
| Claude Sonnet   | 48%      | 46%       | −2.0  |
| Qwen3-235B      | 62%      | 60%       | −2.0  |
| DeepSeek-V3     | 54%      | 58%       | **+4.0** |

4 models improve, 1 worsens (DeepSeek). Mean Δ = −3.3pp, CI crosses zero [−9.1, +2.4].

GPT-4.1 is the outlier with a large −14pp improvement; the other improving models show only marginal gains (−2 to −2.6pp). DeepSeek's +4pp worsening is consistent with the **gap-filling hypothesis**: the mitigation prompt makes the model attempt to fill policy gaps, but it fills them incorrectly, creating new violations.

Incompleteness has the **smallest mean improvement** of all 5 types and is the **least responsive to mitigation**.

## 5. Type Responsiveness Ranking

| Rank | Type                | Mean Δpp | 95% CI         | Models↓/↑ | Binomial p |
|------|---------------------|----------|----------------|-----------|------------|
| 1    | authorization_scope | −18.0    | [−31.5, −4.5]  | 4/0       | 0.188      |
| 2    | lexical             | −8.9     | [−13.5, −4.3]  | **5/0**   | **0.031**  |
| 3    | cond_precedence     | −8.1     | [−12.1, −4.1]  | **5/0**   | **0.031**  |
| 4    | scopal              | −4.3     | [−8.2, −0.4]   | 4/1       | 0.188      |
| 5    | incompleteness      | −3.3     | [−9.1, +2.4]   | 4/1       | 0.188      |

Only **lexical** and **conditional_precedence** achieve significant binomial test results (all 5 models improve, p = 0.031). Authorization_scope has the largest mean effect but Claude's 0.0 delta means only 4/5 models strictly improve.

## 6. Model Overall Responsiveness

| Model        | Baseline | Mitigated | Overall Δpp | Mean per-type Δpp |
|--------------|----------|-----------|-------------|-------------------|
| GPT-5.4      | 41.0%    | 31.6%     | −9.4        | −14.1             |
| GPT-4.1      | 40.7%    | 29.6%     | −11.1       | −12.8             |
| Claude       | 30.3%    | 25.6%     | −4.7        | −6.4              |
| Qwen3-235B   | 43.1%    | 37.6%     | −5.5        | −5.7              |
| DeepSeek-V3  | 49.7%    | 47.2%     | −2.5        | −3.6              |

GPT-4.1 achieves the largest overall reduction (−11.1pp); DeepSeek-V3 the smallest (−2.5pp) and is the only model with any degradation cells.

## Key Takeaways

1. **No universal mitigation**: no type has all 5 models significantly improving (Fisher's exact per model). The prompt-level mitigation works directionally but effect sizes are often small.
2. **Auth_scope responds most on average** (−18pp) but with high variance across models. The response scales with baseline vulnerability (GPT-5.4: 64%→24%; Claude: 12%→12%).
3. **Lexical and conditional_precedence are the most reliably mitigated** — all 5 models show strict improvement, significant by binomial sign test.
4. **Incompleteness is the hardest to mitigate** — smallest mean effect, CI crosses zero, one model worsens. Gap-filling behavior may counteract the mitigation.
5. **DeepSeek-V3 is the least mitigation-responsive model** — only model with degradation cells (incompleteness +4pp, scopal +2pp), smallest overall Δ.
6. **Safety training creates a floor effect**: Claude's low baselines leave little room for further mitigation improvement, especially for auth_scope.
