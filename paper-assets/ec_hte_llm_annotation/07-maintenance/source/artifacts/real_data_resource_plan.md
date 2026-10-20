# Real-Data EC-HTE Success Case — Resource Plan

## Goal
Find an LLM-dataset combination where Δπ > 0.15 AND EC-HTE outperforms global correction on real data.

## Why Current Data Fails
All 11 tested LLM-dataset combinations have Δπ ∈ [0.10, 0.20]:
- TweetEval sentiment (6 OpenAI models): Δπ = 0.080–0.198
- TweetEval sentiment (4 open-source): Δπ = 0.125–0.165
- CivilComments (3 models): Δπ = 0.113–0.160
- Hate speech (1 config): Δπ = 0.117

Most fall below the 0.15 threshold. The few above 0.15 have other violations (FNR > 0.50).

## Strategy Options

### Option A: Weaker LLM + Hard Task (Highest Δπ likelihood)
- Use Llama-3.1-8B or Mistral-7B on a task with ambiguous categories
- Tasks: irony detection, implicit hate speech, political framing
- Expected: smaller models have more variable accuracy across subgroups
- **Requires**: 1× A5000/RTX6000 GPU, ~4h inference + ~2h analysis
- **Risk**: Medium — may still not hit Δπ > 0.15 consistently

### Option B: Demographic Subgroups (Most publishable)
- Use existing LLM annotations but define subgroups by author demographics
- UC Berkeley Hate Speech corpus has age, gender, education metadata
- Ashwin et al. (2025) showed 5× error rate variation across demographics
- **Requires**: No GPU (data already annotated), ~4h analysis on CPU
- **Risk**: Low cost, but demographic subgroup error differences may be driven by annotation ambiguity not LLM failure

### Option C: API-based with GPT-3.5 (Cheapest)
- GPT-3.5-Turbo on stance detection already shows FNR > 0.50 across all targets
- But κ too high (7-15), violating operating conditions
- **Not recommended** — will reproduce existing failure mode

## Recommendation
Try Option B first (zero GPU cost, 4h on CPU). If Δπ > 0.15 with demographic subgroups on existing hate speech data, run EC-HTE and report results. If that fails, Option A requires Manager GPU approval.

## Manager Request Template (if Option A needed)
```
申请 1× RTX 6000 (24GB) 实例，预估 6h，约 ¥15-20。
用途：ec_hte_llm_annotation 项目 real-data 验证——
在 Llama-3.1-8B 上跑 irony/framing 分类，寻找 Δπ>0.15 的 LLM-dataset 组合。
DDL: EMNLP 2026 ARR 5/25，紧急。
```
