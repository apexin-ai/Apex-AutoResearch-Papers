# ⚠️ DEPRECATED — DO NOT USE (Worker 161021, inconsistent violation rates)
# Use analysis_cross_domain_mitigation_summary.md (Worker 160911) instead.

# Cross-Domain Formal Comparison: Retail vs Airline

## Data

2,997 episodes classified by scenario content into **retail** (n=1,520) and **airline** (n=1,437); 40 episodes with ambiguous domain excluded. After merging with judgment outcomes: 2,957 episodes with both domain label and violation status.

| Domain  | Ambiguous | Unambiguous | Total |
|---------|-----------|-------------|-------|
| Airline | 714       | 723         | 1,437 |
| Retail  | 755       | 765         | 1,520 |

## C1: Per-Domain Ambiguity Effect

Both domains show highly significant ambiguity effects:

| Domain  | Amb. Rate | Unamb. Rate | Δpp   | OR    | Fisher p     |
|---------|-----------|-------------|-------|-------|--------------|
| Airline | 54.5%     | 10.5%       | +44.0 | 10.19 | 2.3×10⁻⁷⁵   |
| Retail  | 46.1%     | 12.4%       | +33.7 | 6.03  | 4.0×10⁻⁴⁹   |

The ambiguity effect is significant in both domains, but **stronger in airline** (+44pp vs +34pp). This is partly driven by lower unambiguous-condition violations in airline and higher ambiguous-condition violations in airline.

## C2: Type Ranking Consistency

| Rank | Airline             | Rate  | Retail              | Rate  |
|------|---------------------|-------|---------------------|-------|
| 1    | incompleteness      | 69.6% | incompleteness      | 59.2% |
| 2    | lexical             | 60.0% | authorization_scope | 56.7% |
| 3    | authorization_scope | 55.8% | scopal              | 44.8% |
| 4    | cond_precedence     | 50.4% | lexical             | 44.6% |
| 5    | coreferential       | 47.0% | coreferential       | 42.4% |
| 6    | scopal              | 42.9% | cond_precedence     | 31.1% |

- **Spearman ρ = 0.49, p = 0.33** (not significant)
- Incompleteness is hardest in both domains (rank 1)
- Main divergences: lexical (rank 2 airline vs 4 retail), conditional_precedence (rank 4 airline vs 6 retail), scopal (rank 6 airline vs 3 retail)
- Type ordering is **not well-conserved** across domains

## Domain × Condition Interaction (Logistic Regression)

Model: violation ~ condition + domain + condition×domain (n = 2,957)

| Predictor              | β       | p          |
|------------------------|---------|------------|
| Intercept              | −1.953  | < 0.001    |
| Condition (ambiguous)  | +1.797  | 2.3×10⁻⁴²  |
| Domain (airline)       | −0.188  | 0.250      |
| **Interaction**        | **+0.525** | **0.0069** |

**The interaction is significant (p = 0.007)**: domain moderates the ambiguity effect. The positive interaction coefficient means the ambiguity effect is **amplified in the airline domain**. This may reflect that airline policies involve more safety-critical procedures where ambiguity creates larger behavioral gaps.

Note: The domain main effect is not significant (p = 0.25), meaning baseline violation rates are similar across domains — the difference emerges specifically in how much ambiguity amplifies violations.

## Per-Type Domain Differences (Ambiguous Condition Only)

| Type                | Airline | Retail | Δpp   | Fisher p | Sig.  |
|---------------------|---------|--------|-------|----------|-------|
| authorization_scope | 55.8%   | 56.7%  | −0.8  | 1.000    | No    |
| cond_precedence     | 50.4%   | 31.1%  | +19.3 | 0.003    | **Yes** |
| coreferential       | 47.0%   | 42.4%  | +4.6  | 0.517    | No    |
| incompleteness      | 69.6%   | 59.2%  | +10.4 | 0.109    | No    |
| lexical             | 60.0%   | 44.6%  | +15.4 | 0.016    | **Yes** |
| scopal              | 42.9%   | 44.8%  | −1.9  | 0.797    | No    |

Two types show significant domain differences:
1. **Conditional precedence** (+19.3pp, p=0.003): airline policies with if/then priority rules are more vulnerable
2. **Lexical** (+15.4pp, p=0.016): technical airline terminology creates more ambiguity than retail terminology

## Summary

1. The ambiguity → violation effect replicates across both domains (both p < 10⁻⁴⁹)
2. However, the effect is **significantly stronger in airline** (interaction p = 0.007)
3. Type rankings show moderate but non-significant correlation (ρ = 0.49, p = 0.33)
4. The domain moderation is driven primarily by conditional_precedence and lexical types
5. The paper's claim of "cross-domain consistency" holds at the qualitative level (effect present in both) but requires nuance: the magnitude differs significantly
