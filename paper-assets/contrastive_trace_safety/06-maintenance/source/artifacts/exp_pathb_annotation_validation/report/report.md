# Path B Annotation Validation Report

## Experiment: exp_pathb_annotation_validation
**Date**: 2026-05-17
**Status**: DONE (negative)

## Goal
Validate whether a local binary classifier can reproduce HarmThoughts human/LLM annotations (safety vs non-safety) with sufficient agreement to automate Path B data generation.

**Pass criteria**: Binary F1 >= 0.90 AND CP agreement (|diff| <= 1) >= 85%

## Setup
- **Train**: 48,406 sentences from r1-8b, QwQ, ot-7b (safety=13,209, non-safety=35,197)
- **Test**: 8,525 sentences from r1-32b (safety=2,654, non-safety=5,871)
- **Binary mapping**: Safety = {RA, AL, CC, ED, IA, CR, PS, RS, IR}, Non-safety = {DKE, TD, FL, CE, OB, HV, PA}

## Results

### Method A: TF-IDF (50k, 1-2 ngrams) + LogisticRegression

| Metric | Value | Threshold |
|--------|-------|-----------|
| Accuracy | 0.8004 | - |
| F1 (safety) | **0.5899** | >= 0.90 |
| Precision (safety) | 0.8182 | - |
| Recall (safety) | **0.4612** | - |
| CP Exact Match | 0.4027 | - |
| CP Agreement (|diff|<=1) | **0.5611** | >= 0.85 |
| CP MAE | 6.39 sentences | - |

### Method B: all-MiniLM-L6-v2 + LogisticRegression

| Metric | Value | Threshold |
|--------|-------|-----------|
| Accuracy | 0.7613 | - |
| F1 (safety) | **0.5149** | >= 0.90 |
| Precision (safety) | 0.7008 | - |
| Recall (safety) | **0.4069** | - |
| CP Exact Match | 0.3620 | - |
| CP Agreement (|diff|<=1) | **0.5339** | >= 0.85 |
| CP MAE | 5.16 sentences | - |

## Decision: **FAIL**

Both methods fall far short of thresholds. Key failure mode:
- **Critically low safety recall** (~41-46%): classifiers miss more than half of safety-aware sentences
- **High CP MAE** (5-6 sentences): predicted critical points are off by ~5-6 sentences on average
- Sentence-transformers (Method B) performed worse than TF-IDF, suggesting the problem is not feature quality but task difficulty

## Root Cause Analysis
Safety-aware reasoning in CoT traces is semantically subtle and context-dependent. Sentences like "I should consider the ethical implications" vs "Let me think about how to approach this" differ in safety awareness but share similar surface features. Simple classifiers cannot capture this distinction.

## Implication
**LLM-based annotation is required for Path B data generation.** Options:
1. Use an LLM API (e.g., Claude/GPT-4) with the same prompt template as HarmThoughts
2. Fine-tune a small LM (e.g., DeBERTa) on the full 16-class task with more expressive features
3. Use the existing HarmThoughts labels directly (no new annotation needed) if we constrain Path B to models already in the dataset
