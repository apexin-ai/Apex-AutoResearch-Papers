# Disambiguation Awareness: Per-Model × Per-Type Breakdown

## Awareness Matrix (n_aware / n_violations, rate)

| Type | GPT-5.4 | GPT-4.1 | Claude S4.6 | Qwen3-235B | DeepSeek-V3 | Total |
|---|---|---|---|---|---|---|
| Auth. Scope | 1/32 (3.1%) | 1/23 (4.3%) | 0/6 (0.0%) | 0/13 (0.0%) | 0/30 (0.0%) | 2/104 (1.9%) |
| Cond. Prec. | 2/17 (11.8%) | 3/18 (16.7%) | 8/18 (44.4%) | 0/20 (0.0%) | 0/19 (0.0%) | 13/92 (14.1%) |
| Coref. | 0/9 (0.0%) | 4/16 (25.0%) | 1/11 (9.1%) | 0/21 (0.0%) | 0/22 (0.0%) | 5/79 (6.3%) |
| Incompl. | 1/23 (4.3%) | 4/29 (13.8%) | 0/24 (0.0%) | 0/31 (0.0%) | 0/27 (0.0%) | 5/134 (3.7%) |
| Lexical | 1/21 (4.8%) | 1/17 (5.9%) | 1/16 (6.2%) | 0/26 (0.0%) | 0/27 (0.0%) | 3/107 (2.8%) |
| Scopal | 0/21 (0.0%) | 0/19 (0.0%) | 0/16 (0.0%) | 0/18 (0.0%) | 0/24 (0.0%) | 0/98 (0.0%) |
| **Total** | 5/123 (4.1%) | 13/122 (10.7%) | 10/91 (11.0%) | 0/129 (0.0%) | 0/149 (0.0%) | 28/614 (4.6%) |

## Cluster Analysis: {GPT-4.1, Claude} vs {Qwen3, DeepSeek}

- High cluster: 10.8% (23/213)
- Low cluster: 0.0% (0/278)
- Fisher's exact p = 2.24e-09, OR = Inf

## GPT-5.4 Position

- GPT-5.4: 4.1%
- vs high cluster (10.8%): p = 0.0393
- vs low cluster (0.0%): p = 0.0026

## Pairwise Model Comparisons (Fisher's exact, Holm-corrected)

| Model 1 | Model 2 | Rate 1 | Rate 2 | OR | p (raw) | p (Holm) | Sig? |
|---|---|---|---|---|---|---|---|
| gpt-4.1 | deepseek-v3 | 10.7% | 0.0% | inf | 0.0000 | 0.0002 | **yes** |
| claude-sonnet-4-6 | deepseek-v3 | 11.0% | 0.0% | inf | 0.0000 | 0.0004 | **yes** |
| gpt-4.1 | qwen3-235b | 10.7% | 0.0% | inf | 0.0001 | 0.0005 | **yes** |
| claude-sonnet-4-6 | qwen3-235b | 11.0% | 0.0% | inf | 0.0001 | 0.0008 | **yes** |
| gpt-5.4 | deepseek-v3 | 4.1% | 0.0% | inf | 0.0181 | 0.1084 | no |
| gpt-5.4 | qwen3-235b | 4.1% | 0.0% | inf | 0.0266 | 0.1328 | no |
| gpt-5.4 | gpt-4.1 | 4.1% | 10.7% | 0.3553 | 0.0536 | 0.2143 | no |
| gpt-5.4 | claude-sonnet-4-6 | 4.1% | 11.0% | 0.3432 | 0.0604 | 0.2143 | no |
| gpt-4.1 | claude-sonnet-4-6 | 10.7% | 11.0% | 0.9661 | 1.0000 | 1.0000 | no |
| qwen3-235b | deepseek-v3 | 0.0% | 0.0% | nan | 1.0000 | 1.0000 | no |

## Per-Type Awareness Rates (aggregated across models)

- Auth. Scope: 2/104 (1.9%)
- Cond. Prec.: 13/92 (14.1%)
- Coref.: 5/79 (6.3%)
- Incompl.: 5/134 (3.7%)
- Lexical: 3/107 (2.8%)
- Scopal: 0/98 (0.0%)

Significant type-pair differences (Holm p<0.05): 3
  - authorization_scope vs conditional_precedence: p=0.0277
  - conditional_precedence vs lexical: p=0.0498
  - conditional_precedence vs scopal: p=0.0008

## Key Findings

1. Disambiguation awareness is concentrated in GPT-4.1 and Claude Sonnet 4.6 (10-11%), with Qwen3-235B and DeepSeek-V3 showing zero awareness across all types.
2. The two-cluster pattern is statistically significant (Fisher p = 2.24e-09).
3. GPT-5.4 occupies an intermediate position (~4%), significantly different from the zero cluster but also lower than the high cluster.
4. Awareness is coded among violating episodes only (denominator = violations per cell).