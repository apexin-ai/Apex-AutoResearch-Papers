# ssh verify judges crossed tau

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_judges_crossed_tau_20260523T015021_result.json`
- **Structured JSON:** [`ca3d73f9ea489121241b.json`](../../sessions/ca/ca3d73f9ea489121241b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the report:

---

```
NEW-A: Judge count = 9
  Judge list:
    1. claude-opus-4.7-proxy
    2. claude-sonnet-4.6-proxy
    3. deepseek-v4-pro-proxy
    4. gemini-2.5-pro-proxy
    5. gpt-5.5-proxy
    6. llama-3.3-70b
    7. mistral-large-2
    8. qwen2.5-72b
    9. qwen3-235b-proxy
  Source: exp001/results/ 9 个 judge 子目录，data_loader.py 动态发现
  两个 dry run (dry_run + results_dryrun) 均确认同样 9 judges

NEW-C: Fully crossed status
  n_observations = 5661 ——在服务器上找不到匹配的数据
  当前完整数据实际值:
    N=8 models, I=401 items (min-3-judges filter 后), J=9 judges
    n_obs = 17,039
    Full crossing = 8×401×9 = 28,872
    Fill rate = 59.0%
  历史 dry run 数据:
    dry_run:       N=8, I=316, J=9, n_obs=4,250 (fill=16.8%)
    results_dryrun: N=8, I=175, J=9, n_obs=4,223 (fill=33.7%)
  均不匹配 5661 或 I=176。5661 在代码库中仅出现于 ROADMAP.md (即本任务描述)。

  每个 observation = 1 个 (model, item, judge) triplet:
    - 原始数据是 pairwise comparison (model vs baseline gpt-4-0314)
    - AB/BA 方向平均后去 tie → 1 binary win/loss per triplet
    - 非 pair×2方向，非 model×item×judge 满格

  Per-judge 覆盖率严重不均:
    gpt-5.5-proxy:        89.9% cells filled (2,883 obs)
    qwen2.5-72b:          79.4% (2,546)
    mistral-large-2:      74.5% (2,391)
    claude-opus-4.7-proxy: 69.3% (2,223)
    llama-3.3-70b:        62.3% (1,999)
    claude-sonnet-4.6-proxy: 58.3% (1,870)
    qwen3-235b-proxy:     39.6% (1,269)
    gemini-2.5-pro-proxy: 31.2% (1,000)
    deepseek-v4-pro-proxy: 26.7% (858)

  (model, item) cell 的 judge 覆盖分布:
    9 judges (fully crossed): 348 cells (10.9%)
    6-8 judges:              1,263 cells (39.6%)
    3-5 judges:              1,256 cells (39.4%)
    1-2 judges:                321 cells (10.1%)

  Recommendation: "connected incomplete design"，绝非 fully crossed。
  论文应避免 "fully crossed" 描述，改用 "connected sparse design"。

NEW-D: exp-009 sequential τ
  exp-009 bias_vs_rho.csv 实际值 (N=50, I=100, J=8, 50 seeds/rho):
    rho=0.0: τ_mean = 0.8632 ± 0.036
    rho=0.3: τ_mean = 0.8641 ± 0.034
    rho=0.6: τ_mean = 0.8657 ± 0.033
    rho=0.9: τ_mean = 0.8690 ± 0.035
    Grand mean (all rhos): 0.8655

  Is τ=0.859 correct? NO
  - τ=0.859 来源是 IDEA_BRIEF.md 的 MVP validation (mvp_003, 2026-05-21)，
    不是 exp-009 的结果
  - exp-009 最接近的值: rho=0.0 seed=24 的单次 τ=0.8596
  - exp-009 grand mean = 0.866，与 0.859 相差 0.007
  - Round 2 review 已标记此问题: Introduction τ=0.859 vs §4.2 τ=0.826 矛盾
  - 建议统一为 exp-009 的 rho=0.0 mean: τ=0.863 ± 0.036
```

---
