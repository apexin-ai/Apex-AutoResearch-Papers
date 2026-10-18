# analysis capability matched

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_capability-matched_20260523T074327_result.json`
- **Structured JSON:** [`48e39a99367027baee99.json`](../../sessions/48/48e39a99367027baee99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results are saved. Here's the summary:

## Results

### Model Accuracy Ranking (15 models)
| Model | Type | Accuracy |
|-------|------|----------|
| claude-opus-4-6 | API | 0.9383 |
| gpt-5.5 | API | 0.9300 |
| gemini-3.1-pro-preview | API | 0.9100 |
| gpt-4.1 | API | 0.9017 |
| claude-sonnet-4-6 | API | 0.8817 |
| gpt-4.1-mini | API | 0.8817 |
| llama3.1-70b | LOCAL | 0.8750 |
| mistral-large | LOCAL | 0.8717 |
| qwen2.5-32b | LOCAL | 0.8250 |
| gemini-3.5-flash | API | 0.8183 |
| qwen2.5-72b | LOCAL | 0.8067 |
| gpt-4.1-nano | API | 0.7433 |
| llama3.1-8b | LOCAL | 0.6183 |
| claude-3-haiku | API | 0.6083 |
| qwen2.5-14b | LOCAL | 0.6000 |

### Strategy A (Middle 9, API:5 LOCAL:4, acc 0.74–0.90, std=0.048)
| | K=3 Clustered | K=5 Clustered |
|---|---|---|
| η_max sig | 5/12 | 5/12 |
| K_eff sig | 3/12 | **9/12** |
| **Transition** | | **HOLDS** (K_eff dominates) |

Correlation: K3 r=0.57, K5 r=0.41

### Strategy B (acc>0.45 closest to median, API:6 LOCAL:3, acc 0.82–0.93, std=0.035)
| | K=3 Clustered | K=5 Clustered |
|---|---|---|
| η_max sig | 5/12 | 3/12 |
| K_eff sig | 2/12 | 2/12 |
| **Transition** | | **FAILS** |

Correlation: K3 r=0.73, K5 r=0.73

### API-only Correlation (critical finding)
- K=3: raw r=**0.9803**, log r=**0.9820**
- K=5: raw r=**0.9691**, log r=**0.9785**

### Diagnosis: **Inconclusive — but pattern is revealing**

The key insight is the **API-only K_eff-η_max correlation of r≈0.98**. Among API models, K_eff and η_max are nearly perfectly collinear — the regression literally cannot separate their effects. Strategy B (6 API + 3 local) inherits more of this collinearity (r=0.73) and transition fails. Strategy A (5 API + 4 local) breaks it more (r=0.41) and transition holds.

This points to **power + collinearity**, not pure confound: the transition is real but requires sufficient variation independence between K_eff and η_max, which API-only models don't provide.

Output saved to `/root/cert_manip_resist_eval/artifacts/results/plan001/capability_matched_subsample.json`.

---
