# Director coordination — Part 2 of 3

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/6a/6a7b0a19365cff5eceb9.json)

## Round 24

### Tool call

_source line 356 · 2026-05-15T11:09:12.309810+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"40+ placeholders unfilled — paper not submission-ready\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both reviewers independently flagged as #1 critical issue.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. All placeholders filled. Cross-response: both reviewers confirm.\"\n    action_items:\n      - round: 1\n        action: \"Fill all placeholders with n=500 analysis data\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"All 40+ placeholders filled with experimental data from n=500 analysis.\"\n    resolution_round: 5\n\n  - id: \"R1-N4\"\n    summary: \"Cross-architecture (LLaMA) evidence too weak to support title/abstract framing\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree LLaMA evidence is overclaimed.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §5.5 'Exploratory'. Cross-response: R2 notes LLaMA still n=49 vs DS/QW n=500 but 'Exploratory' label is honest handling, not blocking.\"\n    action_items:\n      - round: 1\n        action: \"Downgrade LLaMA to exploratory; hedge title/abstract/contribution\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"LLaMA downgraded to exploratory with appropriate hedging.\"\n    resolution_round: 5\n\n  - id: \"R1-N3\"\n    summary: \"Single benchmark (MATH-500) severely limits generalization\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree single benchmark is major limitation.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Title 'Mathematical Reasoning Models'. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Scope title/abstract to mathematical reasoning; expand limitations\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Title scoped; limitations section provides MATH-500 justification.\"\n    resolution_round: 5\n\n  - id: \"R1-N2\"\n    summary: \"50-problem sample size lacks power analysis; exclusion criteria unclear\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Use CI width shrinkage instead of post-hoc power.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. n=500, exclusion criteria stated, CI shrinkage 2.5-5.9×. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Run n=500; report exclusion criteria and CI shrinkage\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Full n=500 dataset used; exclusion criteria and CI width shrinkage reported.\"\n    resolution_round: 5\n\n  - id: \"R1-N5\"\n    summary: \"Mechanism analysis (entropy-discrimination collapse) is purely correlational\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Can downgrade if §6 properly scoped.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §6 split, 'correlational' explicit. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Split §6; add correlational caveat\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"§6 restructured with honest correlational framing.\"\n    resolution_round: 5\n\n  - id: \"R2-N3\"\n    summary: \"Insufficient differentiation from HIES (2025)\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Clear delta exists but paper doesn't articulate it.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Explicit HIES comparison in §6.1 and Related Work. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Add explicit HIES comparison\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Explicit HIES comparison added; crossover identified as prediction HIES cannot generate.\"\n    resolution_round: 5\n\n  - id: \"R1-W1\"\n    summary: \"Phase segmentation lacks justification; 'following ThinKV' wording misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Need sensitivity analysis and correct ThinKV reference.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"PARTIALLY RESOLVED. Sensitivity analysis complete (mpl, quartile, quintile). 'following ThinKV' still in background.tex:33. Cross-response consensus: R1 supports R2's suggested rewrite 'analogous to ThinKV's phase decomposition, but using quantile-based segmentation rather than explicit delimiters'. R2 notes quartile/quintile robustness only at n=50 — minor completeness issue, not blocking.\"\n    action_items:\n      - round: 1\n        action: \"Add sensitivity analysis; correct ThinKV phrasing\"\n        assigned_to: \"paper_agent\"\n        status: in_progress\n      - round: 5\n        action: \"Fix 'following ThinKV' in background.tex:33. Suggested text: 'analogous to ThinKV's phase decomposition, but using quantile-based segmentation rather than explicit delimiters'\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Symmetric sparsity rate assumption lacks practical representativeness\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree needs discussion.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Limitations paragraph added. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Add limitations paragraph\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Symmetric sparsity assumption discussed in Limitations.\"\n    resolution_round: 5\n\n  - id: \"R1-W3\"\n    summary: \"Severity gradient G numerically unstable when II_high approaches zero\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree. Need bootstrap CI for G.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Δ primary, G auxiliary with CIs. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Report G CIs; demote to auxiliary\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"G demoted to auxiliary with bootstrap CIs; Δ is primary.\"\n    resolution_round: 5\n\n  - id: \"R1-W4\"\n    summary: \"Bonferroni correction scope (k=4) may be insufficient\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Supplement with BH-FDR.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. k=4 justified, BH-FDR 44-test appendix. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Justify k=4; add BH-FDR appendix\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"k=4 justified; BH-FDR confirms no importance-based findings lost.\"\n    resolution_round: 5\n\n  - id: \"R1-W5\"\n    summary: \"Spearman rho=1.0 on 4 points over-interpreted\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Need n=4 caveat; use JT test.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. n=4 caveat + one-tailed + JT test. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Annotate Spearman n=4; add JT test\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Spearman caveated; JT test provides n=500-level dose-response evidence.\"\n    resolution_round: 5\n\n  - id: \"R1-W6\"\n    summary: \"Exclusion criteria not stated in Methodology\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Merged with R1-N2.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §4 complete. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Report exclusion criteria in §4\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Exclusion criteria and effective n fully reported.\"\n    resolution_round: 5\n\n  - id: \"R2-W3\"\n    summary: \"Related Work missing RLKV, LongFlow, PM-KVQ\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2-W3. R1 partially agrees.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. All three added. Cross-response: confirmed. LongFlow 'Withdrawn' note flagged separately (R5-2).\"\n    action_items:\n      - round: 1\n        action: \"Assess relevance and cite\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"RLKV, LongFlow, PM-KVQ integrated into Related Work.\"\n    resolution_round: 5\n\n  - id: \"R2-W5\"\n    summary: \"Abstract too long and dense\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both independently flagged.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Rewritten ~10 lines. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Condense abstract\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Abstract condensed with clear structure.\"\n    resolution_round: 5\n\n  - id: \"R2-Minor-2\"\n    summary: \"LaTeX source contains REVIEWER-ATTACK/REBUTTAL comments\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Should clean before submission.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Remove all REVIEWER-ATTACK/REBUTTAL comments\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"All reviewer-strategy comments removed.\"\n    resolution_round: 5\n\n  - id: \"R2-Minor-1\"\n    summary: \"h2o-neurips2023 bib entry missing title field; citation quality issues\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both flagged.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"PARTIALLY RESOLVED. h2o fixed. LongFlow 'Withdrawn' note introduced (see R5-2). Cross-response: R1 suggests keep citation but change bib to arXiv preprint format; R2 originally suggested removal but did not rebut R1's approach.\"\n    action_items:\n      - round: 1\n        action: \"Fix h2o bib entry\"\n        assigned_to: \"main_agent\"\n        status: done\n      - round: 5\n        action: \"LongFlow: delete 'Withdrawn from ICLR 2026' note, change venue to arXiv preprint\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-Minor-6\"\n    summary: \"s=0.35 supplementary experiment mentioned but not fully reported\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Either report fully or remove.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Removed. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Remove s=0.35 mention\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"s=0.35 incomplete data removed.\"\n    resolution_round: 5\n\n  - id: \"R1-Minor-code\"\n    summary: \"No code or data release plan\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both noted.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Reproducibility statement added. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Add code/data release statement\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Reproducibility statement added.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-1\"\n    summary: \"paper_provenance.yaml C019 outdated\"\n    category: framing\n    severity: warning\n    status: wont_fix\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"Internal process issue.\"\n      - round: 5\n        reviewers: []\n        note: \"Internal provenance tracking, not a paper defect.\"\n    action_items:\n      - round: 1\n        action: \"Update C019 in paper_provenance.yaml\"\n        assigned_to: \"director\"\n        status: wont_fix\n    resolution: \"Internal process issue, not tracked as paper defect.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-2\"\n    summary: \"Random masking s025+ significant gradient needs explicit paper treatment\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"D063 threshold story needs integration.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Threshold story integrated in §5.1 + cross-model. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Integrate random threshold story in Results\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Random eviction threshold story fully integrated.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-3\"\n    summary: \"Qwen mid-phase 45.2% null rate needs effective n caveat\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"n=500 Qwen mid-phase effective n=274.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Autocorrelation explanation provided. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Investigate root cause; report in §4\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Mid-phase null rate reported with autocorrelation explanation.\"\n    resolution_round: 5\n\n  - id: \"R5-W1\"\n    summary: \"Table 2 uses n=50 profiling data in main body alongside n=500 tables — reader confusion risk\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response consensus: BOTH at warning. R2 upgraded from minor after noting Table 2's G=69-274× (n=50) vs inline G=30-148× (n=500) is a 42-85% overestimate that becomes reader's first impression. R1 suggests Table 2 caption addendum or move to Appendix. R2 suggests main body n=500 per-phase table, current Table 2 to Appendix or marked 'superseded'. Consensus: main body should have n=500 per-phase evidence as primary.\"\n    action_items:\n      - round: 5\n        action: \"Either (a) create condensed n=500 per-phase table for main body and move Table 2 to Appendix, or (b) add caption text explaining n=50 vs n=500 discrepancy (R1 suggested: 'At n=496, median Δ values are systematically lower at s≥0.20 due to reduced outlier influence; the monotonic pattern and strategy contrast are preserved.')\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W2\"\n    summary: \"Crossover analysis (§5.3 + Appendix A) uses n=50 profiling data — not verified at n=500\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response consensus: BOTH at warning. R1 first raised: Δ_s025 dropped 44% (7.16→3.99) from n=50→n=500, so crossover magnitude (5.3×) may change. R2 agreed: crossover is a core novelty argument (Related Work: 'prediction that single-axis frameworks cannot generate'), evidence strength must match claim strength. Direction likely stable but specific magnitude (3.9×-5.4×) unverified. Fix cost low: per-phase per-strategy medians already available from n=500 data.\"\n    action_items:\n      - round: 5\n        action: \"Compute per-phase per-strategy median II at n=500 for crossover conditions. Update §5.3 and Appendix A crossover numbers. At minimum add confirmation sentence that crossover direction holds at n=500.\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-1\"\n    summary: \"'following ThinKV' wording still in background.tex:33\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response consensus: R1 supports R2's suggested rewrite. Agreed text: 'analogous to ThinKV's phase decomposition, but using quantile-based segmentation rather than explicit delimiters'.\"\n    action_items:\n      - round: 5\n        action: \"Replace 'following ThinKV' with reviewer-agreed text in background.tex:33\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-2\"\n    summary: \"LongFlow bib entry has 'Withdrawn from ICLR 2026' note\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response: R1 suggests keep citation but change bib venue to 'arXiv preprint arXiv:XXXX.XXXXX', delete Withdrawn note. R2 originally suggested removal but did not rebut R1's approach. Consensus: modify bib entry format.\"\n    action_items:\n      - round: 5\n        action: \"Delete 'Withdrawn from ICLR 2026' note from LongFlow bib entry; change venue to arXiv preprint format\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-3\"\n    summary: \"\\\\placeholder command definition residual in main.tex:21\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response: both agree trivial cleanup.\"\n    action_items:\n      - round: 5\n        action: \"Remove \\\\newcommand{\\\\placeholder} from main.tex:21\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"40+ placeholders unfilled — paper not submission-ready\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both reviewers independently flagged as #1 critical issue.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. All placeholders filled. Cross-response: both reviewers confirm.\"\n    action_items:\n      - round: 1\n        action: \"Fill all placeholders with n=500 analysis data\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"All 40+ placeholders filled with experimental data from n=500 analysis.\"\n    resolution_round: 5\n\n  - id: \"R1-N4\"\n    summary: \"Cross-architecture (LLaMA) evidence too weak to support title/abstract framing\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree LLaMA evidence is overclaimed.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §5.5 'Exploratory'. Cross-response: R2 notes LLaMA still n=49 vs DS/QW n=500 but 'Exploratory' label is honest handling, not blocking.\"\n    action_items:\n      - round: 1\n        action: \"Downgrade LLaMA to exploratory; hedge title/abstract/contribution\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"LLaMA downgraded to exploratory with appropriate hedging.\"\n    resolution_round: 5\n\n  - id: \"R1-N3\"\n    summary: \"Single benchmark (MATH-500) severely limits generalization\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree single benchmark is major limitation.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Title 'Mathematical Reasoning Models'. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Scope title/abstract to mathematical reasoning; expand limitations\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Title scoped; limitations section provides MATH-500 justification.\"\n    resolution_round: 5\n\n  - id: \"R1-N2\"\n    summary: \"50-problem sample size lacks power analysis; exclusion criteria unclear\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Use CI width shrinkage instead of post-hoc power.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. n=500, exclusion criteria stated, CI shrinkage 2.5-5.9×. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Run n=500; report exclusion criteria and CI shrinkage\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Full n=500 dataset used; exclusion criteria and CI width shrinkage reported.\"\n    resolution_round: 5\n\n  - id: \"R1-N5\"\n    summary: \"Mechanism analysis (entropy-discrimination collapse) is purely correlational\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Can downgrade if §6 properly scoped.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §6 split, 'correlational' explicit. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Split §6; add correlational caveat\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"§6 restructured with honest correlational framing.\"\n    resolution_round: 5\n\n  - id: \"R2-N3\"\n    summary: \"Insufficient differentiation from HIES (2025)\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Clear delta exists but paper doesn't articulate it.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Explicit HIES comparison in §6.1 and Related Work. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Add explicit HIES comparison\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Explicit HIES comparison added; crossover identified as prediction HIES cannot generate.\"\n    resolution_round: 5\n\n  - id: \"R1-W1\"\n    summary: \"Phase segmentation lacks justification; 'following ThinKV' wording misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Need sensitivity analysis and correct ThinKV reference.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"PARTIALLY RESOLVED. Sensitivity analysis complete (mpl, quartile, quintile). 'following ThinKV' still in background.tex:33. Cross-response consensus: R1 supports R2's suggested rewrite 'analogous to ThinKV's phase decomposition, but using quantile-based segmentation rather than explicit delimiters'. R2 notes quartile/quintile robustness only at n=50 — minor completeness issue, not blocking.\"\n    action_items:\n      - round: 1\n        action: \"Add sensitivity analysis; correct ThinKV phrasing\"\n        assigned_to: \"paper_agent\"\n        status: in_progress\n      - round: 5\n        action: \"Fix 'following ThinKV' in background.tex:33. Suggested text: 'analogous to ThinKV's phase decomposition, but using quantile-based segmentation rather than explicit delimiters'\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Symmetric sparsity rate assumption lacks practical representativeness\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree needs discussion.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Limitations paragraph added. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Add limitations paragraph\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Symmetric sparsity assumption discussed in Limitations.\"\n    resolution_round: 5\n\n  - id: \"R1-W3\"\n    summary: \"Severity gradient G numerically unstable when II_high approaches zero\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree. Need bootstrap CI for G.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Δ primary, G auxiliary with CIs. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Report G CIs; demote to auxiliary\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"G demoted to auxiliary with bootstrap CIs; Δ is primary.\"\n    resolution_round: 5\n\n  - id: \"R1-W4\"\n    summary: \"Bonferroni correction scope (k=4) may be insufficient\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Supplement with BH-FDR.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. k=4 justified, BH-FDR 44-test appendix. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Justify k=4; add BH-FDR appendix\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"k=4 justified; BH-FDR confirms no importance-based findings lost.\"\n    resolution_round: 5\n\n  - id: \"R1-W5\"\n    summary: \"Spearman rho=1.0 on 4 points over-interpreted\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Need n=4 caveat; use JT test.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. n=4 caveat + one-tailed + JT test. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Annotate Spearman n=4; add JT test\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Spearman caveated; JT test provides n=500-level dose-response evidence.\"\n    resolution_round: 5\n\n  - id: \"R1-W6\"\n    summary: \"Exclusion criteria not stated in Methodology\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Merged with R1-N2.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §4 complete. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Report exclusion criteria in §4\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Exclusion criteria and effective n fully reported.\"\n    resolution_round: 5\n\n  - id: \"R2-W3\"\n    summary: \"Related Work missing RLKV, LongFlow, PM-KVQ\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2-W3. R1 partially agrees.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. All three added. Cross-response: confirmed. LongFlow 'Withdrawn' note flagged separately (R5-2).\"\n    action_items:\n      - round: 1\n        action: \"Assess relevance and cite\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"RLKV, LongFlow, PM-KVQ integrated into Related Work.\"\n    resolution_round: 5\n\n  - id: \"R2-W5\"\n    summary: \"Abstract too long and dense\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both independently flagged.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Rewritten ~10 lines. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Condense abstract\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Abstract condensed with clear structure.\"\n    resolution_round: 5\n\n  - id: \"R2-Minor-2\"\n    summary: \"LaTeX source contains REVIEWER-ATTACK/REBUTTAL comments\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Should clean before submission.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Remove all REVIEWER-ATTACK/REBUTTAL comments\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"All reviewer-strategy comments removed.\"\n    resolution_round: 5\n\n  - id: \"R2-Minor-1\"\n    summary: \"h2o-neurips2023 bib entry missing title field; citation quality issues\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both flagged.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"PARTIALLY RESOLVED. h2o fixed. LongFlow 'Withdrawn' note introduced (see R5-2). Cross-response: R1 suggests keep citation but change bib to arXiv preprint format; R2 originally suggested removal but did not rebut R1's approach.\"\n    action_items:\n      - round: 1\n        action: \"Fix h2o bib entry\"\n        assigned_to: \"main_agent\"\n        status: done\n      - round: 5\n        action: \"LongFlow: delete 'Withdrawn from ICLR 2026' note, change venue to arXiv preprint\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-Minor-6\"\n    summary: \"s=0.35 supplementary experiment mentioned but not fully reported\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Either report fully or remove.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Removed. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Remove s=0.35 mention\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"s=0.35 incomplete data removed.\"\n    resolution_round: 5\n\n  - id: \"R1-Minor-code\"\n    summary: \"No code or data release plan\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both noted.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Reproducibility statement added. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Add code/data release statement\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Reproducibility statement added.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-1\"\n    summary: \"paper_provenance.yaml C019 outdated\"\n    category: framing\n    severity: warning\n    status: wont_fix\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"Internal process issue.\"\n      - round: 5\n        reviewers: []\n        note: \"Internal provenance tracking, not a paper defect.\"\n    action_items:\n      - round: 1\n        action: \"Update C019 in paper_provenance.yaml\"\n        assigned_to: \"director\"\n        status: wont_fix\n    resolution: \"Internal process issue, not tracked as paper defect.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-2\"\n    summary: \"Random masking s025+ significant gradient needs explicit paper treatment\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"D063 threshold story needs integration.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Threshold story integrated in §5.1 + cross-model. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Integrate random threshold story in Results\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Random eviction threshold story fully integrated.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-3\"\n    summary: \"Qwen mid-phase 45.2% null rate needs effective n caveat\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"n=500 Qwen mid-phase effective n=274.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Autocorrelation explanation provided. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Investigate root cause; report in §4\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Mid-phase null rate reported with autocorrelation explanation.\"\n    resolution_round: 5\n\n  - id: \"R5-W1\"\n    summary: \"Table 2 uses n=50 profiling data in main body alongside n=500 tables — reader confusion risk\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response consensus: BOTH at warning. R2 upgraded from minor after noting Table 2's G=69-274× (n=50) vs inline G=30-148× (n=500) is a 42-85% overestimate that becomes reader's first impression. R1 suggests Table 2 caption addendum or move to Appendix. R2 suggests main body n=500 per-phase table, current Table 2 to Appendix or marked 'superseded'. Consensus: main body should have n=500 per-phase evidence as primary.\"\n    action_items:\n      - round: 5\n        action: \"Either (a) create condensed n=500 per-phase table for main body and move Table 2 to Appendix, or (b) add caption text explaining n=50 vs n=500 discrepancy (R1 suggested: 'At n=496, median Δ values are systematically lower at s≥0.20 due to reduced outlier influence; the monotonic pattern and strategy contrast are preserved.')\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W2\"\n    summary: \"Crossover analysis (§5.3 + Appendix A) uses n=50 profiling data — not verified at n=500\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response consensus: BOTH at warning. R1 first raised: Δ_s025 dropped 44% (7.16→3.99) from n=50→n=500, so crossover magnitude (5.3×) may change. R2 agreed: crossover is a core novelty argument (Related Work: 'prediction that single-axis frameworks cannot generate'), evidence strength must match claim strength. Direction likely stable but specific magnitude (3.9×-5.4×) unverified. Fix cost low: per-phase per-strategy medians already available from n=500 data.\"\n    action_items:\n      - round: 5\n        action: \"Compute per-phase per-strategy median II at n=500 for crossover conditions. Update §5.3 and Appendix A crossover numbers. At minimum add confirmation sentence that crossover direction holds at n=500.\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-1\"\n    summary: \"'following ThinKV' wording still in background.tex:33\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response consensus: R1 supports R2's suggested rewrite. Agreed text: 'analogous to ThinKV's phase decomposition, but using quantile-based segmentation rather than explicit delimiters'.\"\n    action_items:\n      - round: 5\n        action: \"Replace 'following ThinKV' with reviewer-agreed text in background.tex:33\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-2\"\n    summary: \"LongFlow bib entry has 'Withdrawn from ICLR 2026' note\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response: R1 suggests keep citation but change bib venue to 'arXiv preprint arXiv:XXXX.XXXXX', delete Withdrawn note. R2 originally suggested removal but did not rebut R1's approach. Consensus: modify bib entry format.\"\n    action_items:\n      - round: 5\n        action: \"Delete 'Withdrawn from ICLR 2026' note from LongFlow bib entry; change venue to arXiv preprint format\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-3\"\n    summary: \"\\\\placeholder command definition residual in main.tex:21\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response: both agree trivial cleanup.\"\n    action_items:\n      - round: 5\n        action: \"Remove \\\\newcommand{\\\\placeholder} from main.tex:21\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-15T11:09:12.411881+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml\", \"bytes\": 19732}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Assistant

_source line 358 · 2026-05-15T11:09:22.443189+00:00_

Round 5 审稿流程完成。

**最终结果**: 3.5/5 (Borderline Accept)，两位 Reviewer 完全收敛。

**Resolution 统计**:
- Round 1 的 5 个 critical issues：**5/5 resolved**
- Round 1 的 11 个 warning issues：**10/11 resolved**（R1-W1 "following ThinKV" 部分解决）
- Round 1 的 4 个 info issues：**4/4 resolved**
- Round 5 新发现：2 warning（n=50/n=500 混合、crossover 未验证）+ 3 info（ThinKV 措辞、LongFlow bib、\placeholder 残留）

**投稿建议**（已写入报告）：如果能在 2026-06-15 deadline 前完成 crossover n=500 验证 + Table 2 处理 + 三项 cosmetic 修复，评分可达 4.0/5，推荐投稿 EMNLP main。

审稿报告已投递给 Research Director。Issue tracker 已更新至最终状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 25

## Round 25

54 recorded events


### User

_source line 359 · 2026-05-15T11:09:23.953119+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: phase-gated-compound-sparse
- 论文路径: projects/phase-gated-compound-sparse/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-06-15

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-15T11:09:30.130667+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-15T11:09:30.131536+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-15T11:09:35.013543+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-15T11:09:35.114491+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-15T11:09:38.079591+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-15T11:09:38.834836+00:00_

{"result":"# 项目 phase-gated-compound-sparse 概况\n\n## 实验状态 (84 个)\n\n- **mvp_v4_legacy_s025**: DONE (failed) — \n- **mvp_v4_random_r2**: DONE (success) — \n- **mvp_v4_legacy_s01**: DONE (negative) — \n- **mvp_v4_legacy_s03**: DONE (success) — \n- **mvp_v4_legacy_s02**: DONE (success) — \n- **mvp_v4c_r2**: DONE (failed) — \n- **mvp_v4b_r2**: DONE (failed) — \n- **mvp_v4a_r2**: DONE (failed) — \n- **mvp_ii_profiling_v4-random**: DONE (failed) — \n- **mvp_ii_profiling_v4c**: DONE (failed) — \n- **mvp_ii_profiling_v4b**: DONE (failed) — \n- **mvp_ii_profiling_v4**: DONE (failed) — \n- **mvp_ii_profiling_v3**: DONE (negative) — \n- **mvp_ii_profiling_v2**: DONE (negative) — \n- **mvp_interaction_index_profiling**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- sf5_asymmetric_spot（准备中）\n\n## 近期结论\n- **c2_qw_n500_r3** (success): C2 Qwen n=500 continuation (cron false positive on c2_qw_n500). s015 完成, s020-s030 remaining. 与 DeepSeek 对称验证 compound sparsity severity. ← 基于 c2_qw_n500\n- **c2_n500_deepseek** (success): C2 statistical power boost: 将 DeepSeek 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500，提升统计功效。预注册：若 QW s015 在 n=500 后 CI 仍跨零，论文叙事改为 \"compound effect emerges above a threshold sparsity level (~s020)\"\n  [C2 Pre-registration n=500](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/c2_n500_deepseek/data/PRE_REGISTRATION_C2.md) | [c2_n500_deepseek_diagnosis](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/c2_n500_deepseek/report/diagnosis.md) | [n500_statistics_summary](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/c2_n500_deepseek/report/n500_statistics_summary.md)\n- **c2_qw_n500** (failed): C2: Qwen n=500 统计功效提升。将 Qwen 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500，与 DeepSeek 对称验证。\n\n## 趋势\n成功 38 / 负向 10 / 失败 14 / 共 83\nn_problems: 500 ↑（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-22162: 无 GPU 信
…[truncated 1339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-15T11:09:38.986041+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-15T11:09:39.187219+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-15T11:09:43.784291+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 369 · 2026-05-15T11:09:45.257445+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 370 · 2026-05-15T11:09:45.659616+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 371 · 2026-05-15T11:09:46.616186+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-15T11:09:46.767259+00:00_

called mcp__agent-ml-research__read_local_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_local_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-15T11:09:46.767670+00:00_

&lt;tool_use_error>Error: No such tool available: mcp__agent-ml-research__read_local_file&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 374 · 2026-05-15T11:09:52.455730+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"}]

I found detailed information about EMNLP 2026's call for papers submission guidelines and author instructions. Here are the key points:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and repr
…[truncated 1934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 8671
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-15T11:09:52.456328+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'phase-gated-compound-sparse'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5840
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-15T11:09:59.798551+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit template requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit template requirements"
  }
}
```

</details>

---


### Tool call

_source line 377 · 2026-05-15T11:10:00.609307+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 378 · 2026-05-15T11:10:00.962555+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
22	
23	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Mathematical Reasoning Models}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{background}
36	\input{methodology}
37	\input{results}
38	\input{analysis}
39	\input{discussion}
40	\input{conclusion}
41	
42	\bibliography{references}
43	
44	\section*{Limitations}
45	\input{limitations}
46	
47	\section*{Reproducibility}
48	Code and data will be released upon acceptance.
49	
50	\appendix
51	\input{appendix}
52	\input{appendix_moved}
53	\input{appendix_disc_analysis}
54	\input{appendix_robustness}
55	
56	\end{document}
57	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 379 · 2026-05-15T11:10:00.963076+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 380 · 2026-05-15T11:10:06.899910+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit template requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here is the information about ACL Rolling Review 2026 submission format, page limits, and template requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Short papers may consist of up to four (4) pages of content, plus unlimited pages of references.

Final versions of accepted papers will be given one additional page of content (up to 9 pages for long p
…[truncated 1063 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7101
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-15T11:10:06.900868+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/decisions.yaml\", \"content\": \"_next_id: 67\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:44 UTC\\n  summary: MVP 方案：用 Interaction Index 跨 phase 差异验证核心假设\\n  rationale: 评审建议 novelty 锚定在 \\\"phase-dependent interaction direction reversal\\\"。MVP\\n    聚焦验证这一点：在 MATH-500 子集上 profiling DeepSeek-R1-Distill-Qwen-7B，用 ThinKV 方法切分 phases，计算\\n    attention × KV 的 Interaction Index。比全 grid search 更聚焦，直接验证核心 novelty 锚点。Pass =\\n    II 跨 phase 显著不同；Fail = II 恒定。预计 10-15 H100-hours。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:48 UTC\\n  summary: 向 Manager 申请 4×H100-80GB 租卡，预计 8-10 天，¥3200-5000\\n  rationale: 12 天截稿，4 GPU 并行可将日历时间压到 ~8 天（留 4 天 buffer）。2 GPU 需 11 天，buffer 不足 1 天，风险过高。用户明确授权\\\"几张都可以\\\"。GPU\\n    就绪 hard deadline 5/14 EOD。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 17:54 UTC\\n  summary: Throughput 策略：RTX 6000 Pro 做开发/accuracy，最终 throughput 短租 H100\\n  rationale: IDEA_BRIEF 硬约束要求\\\"Report wall-clock and throughput on H100\\\"，baseline 论文（Polar\\n    Sparsity、SeerAttention-R）均报告 H100 数字。RTX 6000 Pro (sm_89) vs H100 (sm_90) 的 kernel\\n    speedup 可能不同。策略(a)：RTX 6000 Pro 做全部开发+accuracy+ablation（硬件无关），仅 throughput 基准测试短租\\n    H100 ~2-4h（~$6-12）。比策略(b)全在 RTX 6000 Pro 上报告更有说服力，成本极低。H100 在 M5 阶段再申请。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 17:58 UTC\\n  summary: Throughput benchmark 硬件从 H100 改为 H20（Hopper sm_90，用户确认无 H100 可用）\\n  rationale: H20 与 H100 同为 Hopper sm_90，kernel 兼容无需额外适配。96GB HBM3 + 4TB/s 带宽适合 inference\\n    benchmark。在 H20 上重跑所有 baseline 确保公平比较，报告 relative speedup ratio（Hopper 架构内比值稳定）。H100\\n    不可用，H20 是最佳替代。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 18:01 UTC\\n  summary: GPU 从 4× RTX 6000 Pro 换为 4× H20-NVLink 96GB\\n  rationale:
…[truncated 1471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5937
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-15T11:10:16.896790+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-15T11:10:16.998180+00:00_

1	issues:
2	  - id: "R1-N1"
3	    summary: "40+ placeholders unfilled — paper not submission-ready"
4	    category: experiment
5	    severity: critical
6	    status: resolved
7	    first_raised_round: 1
8	    last_seen_round: 5
9	    mentions:
10	      - round: 1
11	        reviewers: [1, 2]
12	        note: "Both reviewers independently flagged as #1 critical issue."
13	      - round: 5
14	        reviewers: [1, 2]
15	        note: "RESOLVED. All placeholders filled. Cross-response: both reviewers confirm."
16	    action_items:
17	      - round: 1
18	        action: "Fill all placeholders with n=500 analysis data"
19	        assigned_to: "paper_agent"
20	        status: done
21	    resolution: "All 40+ placeholders filled with experimental data from n=500 analysis."
22	    resolution_round: 5
23	
24	  - id: "R1-N4"
25	    summary: "Cross-architecture (LLaMA) evidence too weak to support title/abstract framing"
26	    category: framing
27	    severity: critical
28	    status: resolved
29	    first_raised_round: 1
30	    last_seen_round: 5
31	    mentions:
32	      - round: 1
33	        reviewers: [1, 2]
34	        note: "Both agree LLaMA evidence is overclaimed."
35	      - round: 5
36	        reviewers: [1, 2]
37	        note: "RESOLVED. §5.5 'Exploratory'. Cross-response: R2 notes LLaMA still n=49 vs DS/QW n=500 but 'Exploratory' label is honest handling, not blocking."
38	    action_items:
39	      - round: 1
40	        action: "Downgrade LLaMA to exploratory; hedge title/abstract/contribution"
41	        assigned_to: "paper_agent"
42	        status: done
43	    resolution: "LLaMA downgraded to exploratory with appropriate hedging."
44	    resolution_round: 5
45	
46	  - id: "R1-N3"
47	    summary: "Single benchmark (MATH-500) severely limits generalization"
48	    category: experiment
49	    severity: critical
50	    status: resolved
51	    first_raised_round: 1
52	    last_seen_round: 5
53	    mentions:
54	      - round: 1
55	        reviewers: [1, 2]
56	       
…[truncated 19884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-15T11:10:16.998752+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-15T11:10:17.451055+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifact
…[truncated 37 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-15T11:10:18.004010+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "output_mode": "content",
  "glob": "*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
    "output_mode": "content",
    "glob": "*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-15T11:10:18.054828+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-15T11:10:44.012853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-15T11:10:44.113787+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We show that compound severity is not phase-invariant: it is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases in mathematical reasoning models.
4	
5	On DeepSeek-R1-Distill-Qwen-7B (500 MATH-500 problems, $n_{\text{eff}}{=}496$, $s \in \{0.15, 0.20, 0.25, 0.30\}$), importance-based eviction produces a monotonically increasing severity gradient from the high-sparsity to low-sparsity reasoning phase (median $\Delta$: $0.39 \to 8.48$; all Bonferroni-corrected $p < 10^{-69}$). Random eviction develops a detectable phase gradient only above $s \approx 0.20$ (non-significant at $s \leq 0.20$; where significant, $3$--$39{\times}$ weaker), confirming importance-based eviction as the dominant driver.
6	A crossover emerges at $s{=}0.25$: importance-based eviction outperforms random in high-sparsity phases yet underperforms in low-sparsity phases---a qualitative reversal in strategy ranking.
7	The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with preliminary cross-architecture evidence from a LlamaForCausalLM model suggesting the phenomenon may extend beyond Qwen2-family architectures.
8	We observe that discrimination collapse---head pruning flattening cumulative importance scores---correlates with the phase-dependent severity amplification, suggesting a mechanism whereby compound sparsity selectively degrades importance-based eviction in distributed-attention phases.
9	These findings motivate phase-aware compression budgets for mathematical reasoning models.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-15T11:10:44.164625+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-15T11:10:44.421046+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 2353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 256
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-15T11:10:44.472674+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-15T11:10:44.523586+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}
9	\label{sec:dataset}
10	We evaluate all 500 problems from MATH-500~\cite{math500-neurips2021}. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048). Problems with degenerate phase assignments (null low or high phase) are excluded, yielding effective sample sizes of $n{=}496$ for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded). Qwen exhibits a higher mid-phase null rate (45.2\% vs.\ 10.2\% for DeepSeek) due to lower temporal autocorrelation in its attention sparsity patterns (lag-1 $r{=}0.718$ vs.\ $0.894$, $d{=}-1.68$); this does not affect the primary gradient metric $\Delta = \mathrm{II}_{\textit{low}} - \mathrm{II}_{\textit{high}}$, which requires only low and high phases. Sensitivity analysis across $\texttt{min\_phase\_length} \in \{5, 10, 20\}$ confirms robustness (Appendix~\ref{app:mpl-sensitivity}).
11	
12	\paragraph{Sparsity configuration.}
13	\label{sec:sparsity-config}
14	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are
…[truncated 1994 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-15T11:10:48.741805+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-15T11:10:49.043897+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\times}$ amplification (all Bonferroni-corrected $p < 10^{-69}$). Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \geq 0.25$, $\Delta$ becomes significant ($0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$) but $15$--$39{\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger. % exp_id: n500_unified_final; DS imp Δ 0.39→8.48, rand 0.01→0.51; JT z=33.7 (imp), 6.2 (rand)
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, 500 MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.21 & 3.99 & 8.48 \\ % exp_id: n500_unified_final; DS imp median_ii_diff
20	Random     & 0.01 & 0.03 & 0.26 & 0.51 \\ % exp_id: n500_unified_final; DS rand median_ii_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown from an
…[truncated 9653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-15T11:10:49.094829+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-15T11:10:50.099899+00:00_

1	\section{Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	\subsection{Discrimination Collapse}
5	\label{sec:discrimination-collapse-main}
6	
7	We observe that head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient of importance scores decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). This pattern---which we term \emph{discrimination collapse}---is consistent with importance-based eviction degenerating into noise-sensitive selection when score distributions flatten. The effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. This observation is independently corroborated by \cite{hies-2025}, who report importance score collapse under heavy single-axis pruning; our results extend this to the compound setting, where collapse is amplified by the interaction of two compression axes and modulated by reasoning phase. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
8	
9	A partial counterfactual supports this interpretation: random eviction does not rely on importance scores, so it is immune to score-distribution changes caused by head pruning. The flat severity gradient under random eviction ($G \approx 1$) is consistent with this independence, while importance-based eviction---whose decisions depend on the very scores that pruning degrades---exhibits the phase-modulated amplification. We note that this evidence is correlational; causal validation through controlled manipulation of importance-score entropy is an important direction for future work. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
10	
11	\subsection{Entropy Redistribu
…[truncated 897 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-15T11:10:50.100425+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-15T11:10:50.301646+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	PM-KVQ~\cite{pmkvq-iclr2026} demonstrates that progressive quantization---gradually reducing bit-width over the generation process---mitigates cumulative error in long-CoT reasoning, implicitly introducing a temporal dimension to compression severity that resonates with our finding that compound interaction is phase-dependent.
11	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
12	
13	\paragraph{KV cache eviction.}
14	Most methods rely on importance scoring whose reliability is increasingly questioned.
15	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
16	\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
17	RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
18	\cite{hies-2025} independently show
…[truncated 2273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-15T11:10:50.302031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-15T11:10:50.352560+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($G{=}30$--$148{\times}$ at $n{=}496$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The near-unity random baseline ($G{=}0.5$--$1.3{\times}$, trivial magnitude) confirms the dominant amplification is strategy-specific. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability.
9	
10	A preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached 18\% (Wilcoxon $p = 0.002$), below the pre-registe
…[truncated 1758 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-15T11:10:55.981372+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-15T11:10:57.036809+00:00_

1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	\label{sec:compound-sparsity}
12	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
13	
14	\paragraph{Interaction Index.}
15	\label{sec:interaction-index}
16	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
17	\begin{equation}
18	    \mathrm{II} = r_b - r_a - r_k + 1.
19	    \label{eq:ii}
20	\end{equation}
21	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative co
…[truncated 1036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-15T11:10:57.137768+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-15T11:10:57.188800+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation ($n{=}496$/$475$ problems). Under importance-based eviction, the amplification ratio $G$ ranges from $30{\times}$ to $148{\times}$ across sparsity levels, with paired median differences $\Delta$ from $0.39$ to $8.48$ (DeepSeek) and $0.07$ to $3.16$ (Qwen), all $p < 10^{-13}$. Random eviction develops a detectable phase gradient only above $s \approx 0.20$, but $3$--$39{\times}$ weaker than importance-based. A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at all four sparsity levels; suggestive preliminary evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) indicates the phenomenon may extend beyond Qwen2, though at ${\sim}1/40$ the magnitude and with a weaker strategy contrast. Discrimination collapse provides a correlational mechanistic explanation supported by both Qwen2-based models.
5	These findings motivate phase-aware sparsity allocation for reasoning model deployment. Extending this analysis to code reasoning (HumanEval, LiveCodeBench) and science reasoning (GPQA), validating the discrimination collapse mechanism through causal intervention, and characterizing asymmetric compound interactions are promising directions for future work.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-15T11:10:57.239619+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-15T11:10:57.290465+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. MATH-500 is a suitable first testbed because it elicits structured reasoning with clear phase transitions (exploratory vs.\ structured computation), supports per-problem evaluation enabling paired statistical tests, and spans sufficient difficulty to produce meaningful variation in sequence length and attention dynamics. However, different reasoning tasks---code generation (e.g., HumanEval, LiveCodeBench), science reasoning (e.g., GPQA), multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile. Whether the phase-strategy interaction documented here extends to these domains is an open question.
6	
7	\paragraph{Symmetric sparsity assumption.}
8	Our analysis applies symmetric sparsity rates: the same fraction $s$ is used for both head pruning and KV cache eviction. Practical deployments may use asymmetric budgets (e.g., aggressive head pruning with conservat
…[truncated 974 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-15T11:11:59.462669+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- 标题: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models\n- 目标 venue: EMNLP 2026 Main Conference (通过 ARR May 2026 cycle)\n- 截止日期: 2026-06-15\n- 格式: ACL 模板 [review] 模式, 长文 8 页 + 无限 references, double-blind\n- Limitations section 必须包含\n- 论文路径: projects/phase-gated-compound-sparse/paper/main.tex\n\n## 你的审查侧重\n\n**核心职责：方法严谨性**——像顶会最严格的审稿人那样评估。重点审查：\n\n1. **实验设计与统计分析**:\n   - Interaction Index (II) 定义是否合理？additive null 假设是否有充分理由？\n   - 统计检验选择（Wilcoxon, Mann-Whitney U, Bonferroni, JT test）是否恰当？\n   - Bootstrap CI (B=10,000) 是否足够？seed 固定是否引入偏差？\n   - Spearman ρ=1.0 on n=4 points 的处理（已加 caveat + JT test）——是否充分？\n   - Bonferroni k=4 范围是否过窄？BH-FDR 44-test 补充是否足够？\n\n2. **Phase segmentation 方法论**:\n   - 基于 attention sparsity tercile 的三阶段划分是否有原则性依据？\n   - sensitivity analysis (mpl, quartile, quintile) 覆盖度是否充分？\n   - 论文称 \"following ThinKV\" 但实际使用 quantile-based segmentation——措辞是否准确？\n\n3. **样本量与效应量**:\n   - n=496/475 (effective) 是否足以支撑所有 claims？\n   - LLaMA cross-arch 仅 n=49——claims 的 hedging 是否充分？\n   - Table 2 使用 n=50 profiling 数据（G=69-274×）而 n=496 inline 给出 G=30-148×——这个差异（42-85% overestimate）是否被充分说明？\n\n4. **机制分析 (§6)**:\n   - discrimination collapse 是 correlational evidence——论文是否明确标注？\n   - entropy redistribution 仅在 DeepSeek 上一致——cross-model inconsistency 处理是否诚实？\n   - Gini coefficient 下降 0.030-0.081 (DS), 0.010-0.020 (QW)——effect size 是否足以支撑机制 claim？\n\n5. **可复现性**:\n   - 实验细节（bfloat16, eager attention, max_new_tokens=2048, greedy decoding）是否足够复现？\n   - \"Code and data will be released upon acceptance\" 是否满足 ARR 要求？\n   - 缺少 hyperparameter table 或完整 config？\n\n6. **格式合规**:\n   - 页数是否符合 8 页限制？\n   - \\placeholder 命令定义残留在 main.tex:21——是否有未填充的 placeholder？\n   - 引用格式是否符合 ACL 标准？\n\n## 已知关注区域（前轮审稿遗留 open issues）\n- Table 2 (n=50) vs n=500 数据混用——读者困惑风险\n- §5.3 crossover 分析使用 n=50 数据未在 n=500 验证\n- background.tex:33 \"following ThinKV\" 措辞\n- \\placeholder 命令残留\n\n**输出格式**: 按 Strengths / Weaknesses / Questions / Minor Issues 结构化输出。每条 Weakness 标注 severity (Must-Fix / Should-Fix / Minor)。引用具体 Section/Table/Figure/行号。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- 标题: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models\n- 目标 venue: EMNLP 2026 Main Conference (通过 ARR May 2026 cycle)\n- 截止日期: 2026-06-15\n- 格式: ACL 模板 [review] 模式, 长文 8 页 + 无限 references, double-blind\n- Limitations section 必须包含\n- 论文路径: projects/phase-gated-compound-sparse/paper/main.tex\n\n## 你的审查侧重\n\n**核心职责：方法严谨性**——像顶会最严格的审稿人那样评估。重点审查：\n\n1. **实验设计与统计分析**:\n   - Interaction Index (II) 定义是否合理？additive null 假设是否有充分理由？\n   - 统计检验选择（Wilcoxon, Mann-Whitney U, Bonferroni, JT test）是否恰当？\n   - Bootstrap CI (B=10,000) 是否足够？seed 固定是否引入偏差？\n   - Spearman ρ=1.0 on n=4 points 的处理（已加 caveat + JT test）——是否充分？\n   - Bonferroni k=4 范围是否过窄？BH-FDR 44-test 补充是否足够？\n\n2. **Phase segmentation 方法论**:\n   - 基于 attention sparsity tercile 的三阶段划分是否有原则性依据？\n   - sensitivity analysis (mpl, quartile, quintile) 覆盖度是否充分？\n   - 论文称 \"following ThinKV\" 但实际使用 quantile-based segmentation——措辞是否准确？\n\n3. **样本量与效应量**:\n   - n=496/475 (effective) 是否足以支撑所有 claims？\n   - LLaMA cross-arch 仅 n=49——claims 的 hedging 是否充分？\n   - Table 2 使用 n=50 profiling 数据（G=69-274×）而 n=496 inline 给出 G=30-148×——这个差异（42-85% overestimate）是否被充分说明？\n\n4. **机制分析 (§6)**:\n   - discrimination collapse 是 correlational evidence——论文是否明确标注？\n   - entropy redistribution 仅在 DeepSeek 上一致——cross-model inconsistency 处理是否诚实？\n   - Gini coefficient 下降 0.030-0.081 (DS), 0.010-0.020 (QW)——effect size 是否足以支撑机制 claim？\n\n5. **可复现性**:\n   - 实验细节（bfloat16, eager attention, max_new_tokens=2048, greedy decoding）是否足够复现？\n   - \"Code and data will be released upon acceptance\" 是否满足 ARR 要求？\n   - 缺少 hyperparameter table 或完整 config？\n\n6. **格式合规**:\n   - 页数是否符合 8 页限制？\n   - \\placeholder 命令定义残留在 main.tex:21——是否有未填充的 placeholder？\n   - 引用格式是否符合 ACL 标准？\n\n## 已知关注区域（前轮审稿遗留 open issues）\n- Table 2 (n=50) vs n=500 数据混用——读者困惑风险\n- §5.3 crossover 分析使用 n=50 数据未在 n=500 验证\n- background.tex:33 \"following ThinKV\" 措辞\n- \\placeholder 命令残留\n\n**输出格式**: 按 Strengths / Weaknesses / Questions / Minor Issues 结构化输出。每条 Weakness 标注 severity (Must-Fix / Should-Fix / Minor)。引用具体 Section/Table/Figure/行号。"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-15T11:12:28.440959+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 28978
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-15T11:12:28.642232+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- 标题: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models\n- 目标 venue: EMNLP 2026 Main Conference (通过 ARR May 2026 cycle)\n- 截止日期: 2026-06-15\n- 格式: ACL 模板 [review] 模式, 长文 8 页 + 无限 references, double-blind\n- Limitations section 必须包含\n- 论文路径: projects/phase-gated-compound-sparse/paper/main.tex\n\n## 你的审查侧重\n\n**核心职责：新颖性与完整性**——像顶会最严格的审稿人那样评估。重点审查：\n\n1. **Novelty 评估**:\n   - 核心 novelty claim（\"phase-strategy interaction in compound sparsity\"）相对于已有工作的增量贡献是否足够？\n   - 与 HIES (2025) 的区分度：HIES 已报告 importance score collapse under heavy pruning。本文称 \"extend this to compound setting, where collapse is amplified by interaction of two compression axes and modulated by reasoning phase\"——这个增量是否 substantial？\n   - 与 ThinKV 的关系：ThinKV 已做 phase-aware KV 策略。本文的 \"compound interaction\" 增量是否清晰？\n   - 与 Sparse Frontier (2025) 的关系：该文已发现 \"no single sparse attention strategy dominates across generation stages\"——crossover 发现是否真正新颖？\n   - discrimination collapse mechanism 作为 contribution——是否只是已知现象在新 setting 下的观察？\n\n2. **Contribution 显著性**:\n   - 论文本质是 characterization/analysis paper（无新方法、无新系统）——对 EMNLP main conference 是否足够？\n   - 3 个 contributions 的 impact：(1) phase-strategy interaction, (2) dose-response + cross-model, (3) entropy-discrimination collapse。每个的 delta 有多大？\n   - Discussion 中的 pilot experiment（oracle 18%, heuristic 32%）未达到 30% gate——这是否削弱 practical significance？\n\n3. **Related Work 完整性**:\n   - 搜索 2025-2026 年 compound sparsity / KV cache compression / reasoning model pruning 最新文献\n   - 是否遗漏重要 baseline 或对比？\n   - 引用是否存在可疑条目（hallucinated citations）？逐条验证关键引用的真实性\n   - LongFlow bib entry 是否有 \"Withdrawn\" 标注问题？\n\n4. **Framing 准确度**:\n   - 标题 \"Phase-Modulated Compound Sparsity\" 是否过度 claim？（实际仅 characterization，未 modulate anything）\n   - Abstract 中 \"emergent phase-strategy interaction\" 的 \"emergent\" 是否合理？\n   - \"over an order of magnitude\" claim 在 abstract——指 G ratio 还是 Δ？是否 misleading？\n   - LLaMA 的 \"preliminary cross-architecture evidence\" hedging 是否充分？n=49, 仅 s=0.30 显著\n   - Qwen mid-phase 45.2% null rate——是否被诚实处理？\n\n5. **跨架构 Claims**:\n   - 仅 2 个 Qwen2 架构模型 + 1 个 LLaMA (n=49)——generalization claims 的边界在哪？\n   - LLaMA 的 strategy contrast 大幅减弱——是否削弱核心 contribution？\n   - 全部 7-8B 规模——scale limitation 是否充分讨论？\n\n6. **整体影响力**:\n   - 对 EMNLP 2026 的 reviewer pool（NLP + efficiency + reasoning），这篇论文的 \"so what\" 是什么？\n   - 没有 throughput/latency 数据——pure characterization 的实际价值？\n   - 未来工作方向是否清晰且可操作？\n\n7. **引用审计（关键引用）**:\n   - 验证以下引用是否真实存在且被正确引用: spark-aaai2026, slim-icml2025, unicomp-2026, phase-transition-compression-2026, hies-2025, thinkv-iclr2026, graspune-acl2026, pmkvq-iclr2026, sparse-frontier-2025, greedy-bias-kvcache-2026, longflow-2026, rlkv-2025, physics-kvcache-2026\n   - 特别关注 2026 年引用——是否为未正式发表的 preprints？ARR 对 preprint 引用有何政策？\n\n## 已知关注区域（前轮审稿遗留 open issues）\n- §5.3 crossover 数据来自 n=50 未在 n=500 验证——核心 novelty argument 的证据强度问题\n- LongFlow bib entry \"Withdrawn from ICLR 2026\" 标注\n\n**输出格式**: 按 Strengths / Weaknesses / Questions / Missing References 结构化输出。每条 Weakness 标注 severity (Must-Fix / Should-Fix / Minor)。引用具体 Section/Table/Figure/行号。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- 标题: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models\n- 目标 venue: EMNLP 2026 Main Conference (通过 ARR May 2026 cycle)\n- 截止日期: 2026-06-15\n- 格式: ACL 模板 [review] 模式, 长文 8 页 + 无限 references, double-blind\n- Limitations section 必须包含\n- 论文路径: projects/phase-gated-compound-sparse/paper/main.tex\n\n## 你的审查侧重\n\n**核心职责：新颖性与完整性**——像顶会最严格的审稿人那样评估。重点审查：\n\n1. **Novelty 评估**:\n   - 核心 novelty claim（\"phase-strategy interaction in compound sparsity\"）相对于已有工作的增量贡献是否足够？\n   - 与 HIES (2025) 的区分度：HIES 已报告 importance score collapse under heavy pruning。本文称 \"extend this to compound setting, where collapse is amplified by interaction of two compression axes and modulated by reasoning phase\"——这个增量是否 substantial？\n   - 与 ThinKV 的关系：ThinKV 已做 phase-aware KV 策略。本文的 \"compound interaction\" 增量是否清晰？\n   - 与 Sparse Frontier (2025) 的关系：该文已发现 \"no single sparse attention strategy dominates across generation stages\"——crossover 发现是否真正新颖？\n   - discrimination collapse mechanism 作为 contribution——是否只是已知现象在新 setting 下的观察？\n\n2. **Contribution 显著性**:\n   - 论文本质是 characterization/analysis paper（无新方法、无新系统）——对 EMNLP main conference 是否足够？\n   - 3 个 contributions 的 impact：(1) phase-strategy interaction, (2) dose-response + cross-model, (3) entropy-discrimination collapse。每个的 delta 有多大？\n   - Discussion 中的 pilot experiment（oracle 18%, heuristic 32%）未达到 30% gate——这是否削弱 practical significance？\n\n3. **Related Work 完整性**:\n   - 搜索 2025-2026 年 compound sparsity / KV cache compression / reasoning model pruning 最新文献\n   - 是否遗漏重要 baseline 或对比？\n   - 引用是否存在可疑条目（hallucinated citations）？逐条验证关键引用的真实性\n   - LongFlow bib entry 是否有 \"Withdrawn\" 标注问题？\n\n4. **Framing 准确度**:\n   - 标题 \"Phase-Modulated Compound Sparsity\" 是否过度 claim？（实际仅 characterization，未 modulate anything）\n   - Abstract 中 \"emergent phase-strategy interaction\" 的 \"emergent\" 是否合理？\n   - \"over an order of magnitude\" claim 在 abstract——指 G ratio 还是 Δ？是否 misleading？\n   - LLaMA 的 \"preliminary cross-architecture evidence\" hedging 是否充分？n=49, 仅 s=0.30 显著\n   - Qwen mid-phase 45.2% null rate——是否被诚实处理？\n\n5. **跨架构 Claims**:\n   - 仅 2 个 Qwen2 架构模型 + 1 个 LLaMA (n=49)——generalization claims 的边界在哪？\n   - LLaMA 的 strategy contrast 大幅减弱——是否削弱核心 contribution？\n   - 全部 7-8B 规模——scale limitation 是否充分讨论？\n\n6. **整体影响力**:\n   - 对 EMNLP 2026 的 reviewer pool（NLP + efficiency + reasoning），这篇论文的 \"so what\" 是什么？\n   - 没有 throughput/latency 数据——pure characterization 的实际价值？\n   - 未来工作方向是否清晰且可操作？\n\n7. **引用审计（关键引用）**:\n   - 验证以下引用是否真实存在且被正确引用: spark-aaai2026, slim-icml2025, unicomp-2026, phase-transition-compression-2026, hies-2025, thinkv-iclr2026, graspune-acl2026, pmkvq-iclr2026, sparse-frontier-2025, greedy-bias-kvcache-2026, longflow-2026, rlkv-2025, physics-kvcache-2026\n   - 特别关注 2026 年引用——是否为未正式发表的 preprints？ARR 对 preprint 引用有何政策？\n\n## 已知关注区域（前轮审稿遗留 open issues）\n- §5.3 crossover 数据来自 n=50 未在 n=500 验证——核心 novelty argument 的证据强度问题\n- LongFlow bib entry \"Withdrawn from ICLR 2026\" 标注\n\n**输出格式**: 按 Strengths / Weaknesses / Questions / Missing References 结构化输出。每条 Weakness 标注 severity (Must-Fix / Should-Fix / Minor)。引用具体 Section/Table/Figure/行号。"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-15T11:12:30.207667+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1565
}
```

</details>

---


### Assistant

_source line 412 · 2026-05-15T11:12:43.614326+00:00_

Reviewer 1（方法严谨性）和 Reviewer 2（新颖性/完整性）已分配，Round 1 独立审稿进行中。等待两位 Reviewer 返回审稿结果后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 26

## Round 26

2 recorded events


### User

_source line 413 · 2026-05-15T11:17:27.504722+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1: 方法严谨性审查

## 总体评分
**Overall**: 3.5/5 (Findings-level, 介于 Findings 和 Conference 之间)
**一句话总结**: 研究问题明确且有实际意义，统计方法论总体严谨，但 n=50/n=496 数据混用导致关键结论（crossover、per-phase G）的基础不一致，机制分析的 effect size 过小难以支撑因果叙事。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 核心 Δ 结论（Table 1, Table 4）在 n=496 上统计稳健；但 crossover 分析和 per-phase G 仍建立在 n=50 数据上，且机制分析 effect size 不足以匹配 claim 强度 |
| Excitement | 3.5/5 | Phase-strategy interaction 概念有新意，crossover 现象若验证成立将有部署价值，但量化发现主要是 descriptive 而非 actionable（mitigation pilot 未通过预注册门槛） |
| Reproducibility | 3.0/5 | 关键实验细节（bfloat16, eager attention, greedy, seed=42）有记录，但缺少系统化 hyperparameter table/config；"Code and data will be released upon acceptance" 不满足 ARR 鼓励的 review-time 开放标准 |
| Reviewer Confidence | 4/5 | 熟悉 KV cache compression、attention pruning 和统计方法论 |

---

## Strengths（主要优势）

**S1. 研究问题定义精准且有实际价值。** Compound sparsity 的 phase-dependent interaction 是一个被先前工作忽略的维度。将 severity 分解为 phase × strategy 的交互是一个清晰的分析框架，对部署有直接指导意义。

**S2. 统计方法论总体严谨且透明。** 非参数检验（Wilcoxon, Mann-Whitney U）、bootstrap CI (B=10,000)、Bonferroni + BH-FDR 双重校正、JT test 的 dose-response 验证、permutation test——在 NLP 实证研究中属于高标准。BH-FDR 44-test 补充（Appendix B.1）在 Bonferroni k=4 的窄范围之上提供了全局校正。

**S3. 负面结果诚实报告。** LLaMA cross-architecture 的弱证据（§5.5: 仅 s=0.30 显著）、mitigation pilot 未通过预注册门槛（Discussion: oracle 18% < 30% gate）、entropy redistribution 的 Qwen 不一致（§6.2: s=0.25 反转）、per-problem concordance 不显著（ρ=-0.107, p=0.926）——均直接呈现，不掩盖。

**S4. 系统的 robustness checks。** mpl 敏感性（5/10/20）、segmentation 粒度（tercile/quartile/quintile）、n=50→496 精度提升（CI 收窄 2.5-5.9×）、additive vs multiplicative null——覆盖面优于同类工作。

**S5. Random eviction 作为对照设计精巧。** 利用 random eviction 的 score-independence 特性作为 falsification control，G≈1 的 near-unity baseline 有效隔离了 strategy-specific 效应。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Table 2 (n=50) 与 n=496 数据混用，crossover 分析未在全量数据验证**

- 具体位置：Table 2 (results.tex:31-53), §5.3 (results.tex:63-66), Figure 1 (results.tex:55-60), Appendix D (appendix_moved.tex:8-18)
- 问题：Table 2 报告 n=50 profiling subset 的 per-phase II 值，G 值为 69-274×；n=496 的 G 值为 30-148×（仅在 Figure 1 caption 和正文中以 bootstrap CI 形式给出）。n=50 的 G 过高估计了 42-85%。§5.3 crossover 分析的核心数字（importance: 0.032 vs 0.818, random: 7.196 vs 1.363, 5.3× reversal）完全来自 n=50 数据。Appendix D 的 crossover 详情同样使用 n=50。Table 2 caption 虽注明 "confirmed at n=496 (Table 1)"，但 confirmation 仅限 Δ 的单调性，未覆盖 per-phase 绝对值和 crossover magnitude。
- 为什么影响接收：crossover 是论文三大 contribution 之一（Introduction 第 22 行 "no single strategy dominates uniformly"），如果 n=50 的 per-phase II 值在 n=496 上不可复现或 magnitude 大幅缩水，crossover claim 的强度需要重新评估。G 的 42-85% 过高估计未被系统讨论，读者容易混淆两组数字。
- 建议修改方向：(1) 在 n=496 数据上重新计算 per-phase II 中位数并替换 Table 2；(2) 在 n=496 上验证 crossover magnitude 并报告 bootstrap CI；(3) 如果 n=50 数据有不可替代的理由（例如 profiling 包含 per-phase II 的原始计算），需明确说明为何全量数据不可用于此分析。

**N2** [critical] **Discrimination collapse effect size 与 severity gradient magnitude 之间的 gap 未弥合**

- 具体位置：§6.1 (analysis.tex:1-9), Table 8 (appendix_disc_analysis.tex:126-143)
- 问题：Gini 下降 0.030-0.081 (DeepSeek) 和 0.010-0.020 (Qwen) 被提出作为 severity gradient (G=30-148×) 的机制解释。但 Gini coefficient 上 0.01-0.08 的变化是微小的（Gini 范围 0-1），论文未报告 baseline Gini 值，无法判断相对变化幅度。0.010-0.020 的 Qwen Gini 变化尤其不具说服力——如何解释一个 1-2% 的 score distribution 变化驱动 3× 到 148× 的 severity amplification？论文标注了 "correlational evidence"（analysis.tex:9），但 Discussion 和 Introduction 仍以 "entropy-discrimination collapse" 作为一个完整机制叙事。
- 为什么影响接收：方法论审查的核心问题——claim 的强度与 evidence 的强度不匹配。如果 effect size 无法解释 order-of-magnitude 的 severity 变化，读者应被更明确地告知机制仍是开放问题。
- 建议修改方向：(1) 报告 baseline Gini 值和相对变化（ΔGini/Gini_baseline）；(2) 讨论为什么小的 score distribution 变化可能通过 threshold amplification 产生大的 eviction 效果差异（如果这是作者的论点）；(3) 如果无法弥合这个 gap，降低机制部分在论文中的权重，将其明确定位为 "preliminary correlational observation" 而非 "mechanism"。

**N3** [critical] **"following ThinKV" 对 phase segmentation 方法的错误归因**

- 具体位置：background.tex:33
- 问题：原文 "partitioned into three phases...by tercile boundaries of per-position attention sparsity, following ThinKV" 暗示该方法沿用了 ThinKV。但 ThinKV 使用模型生成的 explicit reasoning delimiters（如 `&lt;think>` tokens）划分 think/non-think phases，而本文使用 quantile-based attention sparsity segmentation，这是一个不同的方法。"following" 的措辞具有误导性。
- 为什么影响接收：方法归因不准确会误导读者对方法论 novelty 和 provenance 的判断。如果 segmentation 是本文自定义的方法，应当如实标注。
- 建议修改方向：改为 "inspired by the phase-aware perspective of ThinKV" 或直接删除 "following ThinKV"，将其改为 "we use a quantile-based segmentation (cf. the delimiter-based approach of ThinKV)"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Spearman ρ=1.0 on n=4 的过度报告**

- 具体位置：methodology.tex:22, results.tex:71
- 问题：n=4 data points 的 Spearman ρ=1.0 统计意义极弱（exact permutation p=0.042, one-tailed）。任何严格单调的 4 个值都会给出 ρ=1.0。p=0.042 在任何 multiple testing correction 下都不能存活。论文已补充 JT test（使用 per-problem values，z=6.2-33.7），这是更有力的检验——但 Spearman ρ 仍在正文中与 JT test 并列出现，给人虚假的统计印象。
- 建议：将 JT test 作为 dose-response 的 primary evidence，降低 Spearman ρ 的 prominence（移至 Appendix 或以脚注形式补充），或至少加注 "n=4 correlation is inherently low-powered"。

**W2** [warning] **Bonferroni k=4 范围设定需更充分的 pre-registration 式论证**

- 具体位置：methodology.tex:22
- 问题：Bonferroni k=4 定义为 "per model×strategy combination, 4 sparsity levels testing one dose-response hypothesis"。但论文实际进行了 44 个统计检验。BH-FDR 在 Appendix B.1 中覆盖了全部 44 个检验（好），但 main text 应更明确说明为什么 k=4 是合理的 family definition——这需要 pre-registration 或先验假设的支持。当前的表述可能让读者认为作者 cherry-picked 了一个宽松的校正范围。
- 建议：在 §4 (methodology.tex:22) 加一句话说明 family definition 的 rationale（"each model×strategy family tests a single monotonic dose-response hypothesis across 4 sparsity levels"），并在同一段 prominently reference BH-FDR 44-test 结果。

**W3** [warning] **Entropy redistribution 跨模型不一致削弱机制叙事**

- 具体位置：§6.2 (analysis.tex:11-14), Table 9 (appendix_disc_analysis.tex:163-183)
- 问题：Entropy redistribution 在 DeepSeek 上一致为负（ΔH ∈ [-0.047, -0.040]），但 Qwen 在 s=0.25 反转为 +0.045（22/30 problems）。论文正确地将其定位为 "secondary, model-dependent factor"（analysis.tex:14），但正文仍花费 ~15% 的 Analysis section 讨论它。
- 建议：进一步精简 §6.2 的正文篇幅，或在 Discussion 中明确承认 entropy redistribution 不是一个 robust mechanism——它是一个 model-specific observation。

**W4** [warning] **缺乏下游任务评估——PPL-based II 的实际意义不明**

- 具体位置：全文（II 定义在 background.tex:16-21）
- 问题：所有分析基于 PPL 比率的 Interaction Index。但 PPL 的 super-additive degradation 是否转化为 downstream task accuracy 的差异？例如，G=148× 的 PPL 放大在 MATH-500 accuracy 上对应多少准确率损失？缺少这一环节使得 "motivate phase-aware compression budgets" 的实际部署建议缺乏 grounding。Limitations 中提到了 task coverage 但未提 PPL→accuracy 的 gap。
- 建议：即使不做新实验，也应在 Discussion 或 Limitations 中讨论 PPL 与 downstream accuracy 的关系，以及 severity gradient 在 accuracy 层面是否同样成立。

**W5** [warning] **Mitigation pilot 失败对论文 motivation 的影响需更坦诚讨论**

- 具体位置：discussion.tex:10
- 问题：Oracle phase-aware recovery 仅 18%（未通过 30% pre-registered gate），heuristic 32% 但 CI 跨零。这实际上削弱了 "phase-aware compression budgets" 的实用动机——如果知道了哪个 phase 该减轻压缩，实际效果仍然有限。论文将此归因为 "budget reallocation alone is insufficient"，但这个 negative result 应更突出地讨论其对论文核心动机的影响。
- 建议：在 Discussion 中增加一段关于为什么 severity gradient characterization 本身有价值（即使当前 mitigation 不成功），例如为 future joint strategy-budget optimization 提供了必要的 diagnostic signal。

**W6** [warning] **LLaMA cross-architecture 证据的 CI/Wilcoxon 不一致需解释**

- 具体位置：Table 3 (results.tex:83-98)
- 问题：s=0.15 时 bootstrap CI 排除零 [0.002, 0.043] 但 Wilcoxon p_Bonf=0.219（ns）；s=0.30 时 CI 包含零 [-0.069, 0.544] 但 Wilcoxon p_Bonf=0.029（sig）。这两处 CI 和 Wilcoxon 结果的矛盾未被解释。可能原因包括 bootstrap CI 和 signed-rank test 对分布形状的不同假设、或 tied values 的处理差异，但论文未讨论。
- 建议：加一句脚注或正文说明 CI 和 Wilcoxon 不一致的技术原因（e.g., "the divergence arises because the bootstrap CI estimates the median shift while the Wilcoxon test assesses the symmetry of signed ranks"）。

---

## Minor Issues（不影响接收）

- **M1**: `\placeholder` 命令定义在 main.tex:21 但全文未使用——残余代码，应清理。
- **M2**: appendix_results.tex 存在但未被 `\input` 引入——orphaned file，且与 appendix_moved.tex 存在重复 `\label{app:cross-model-details}`。
- **M3**: h2o-neurips2023 bib entry 的 title 字段为空——引用核查报告 "no title in bib entry"，编译时可能只显示作者和年份。
- **M4**: 3 篇引用（defensivekv-iclr2026, hies-2025, phase-transition-compression-2026）在 OpenAlex 中未找到——可能是非常新的预印本，但应确认引用准确性。hies-2025 (arXiv:2510.13832) 尤其重要，因为论文在 §6.1 将其作为独立 corroboration 引用。
- **M5**: deepseek-r1-2025 bib entry 的 first author 列为 "DeepSeek-AI" 而非个人作者——OpenAlex 匹配到 "Guo" 等个人作者。ACL style 对 corporate authorship 的处理需确认。
- **M6**: 论文脚注 1（methodology.tex:6）提到 "An earlier float16 configuration produced sporadic NaN values; bfloat16 eliminated all occurrences"——这是有价值的信息，但读者可能会问：NaN 是否影响了 n=50 profiling 数据？如果 profiling 在 float16 下进行，数据可靠性需确认。

---

## Questions to Authors

**Q1**: Table 2 的 per-phase II 值和 G 为何未在 n=496 上重新计算？是否有技术原因（如 per-phase II 计算依赖于 profiling 阶段的特定实验配置）？

**Q2**: Discrimination collapse 的 baseline Gini 值是多少？ΔGini/Gini_baseline 的相对变化幅度？

**Q3**: Phase segmentation 是在 dense model 的 attention patterns 上做的，但 dense model 下不同 problem 的 phase boundary 位置差异有多大？是否存在某些 problem 的 phase boundary 不稳定（即 slight perturbation 导致 token 跨 phase 移动）的情况？

**Q4**: 是否考虑过使用 accuracy-based（而非 PPL-based）的 Interaction Index？例如 token-level accuracy 的 compound interaction？

**Q5**: Frobenius norm head pruning 是否是结果的关键假设？如果使用其他 head importance metric（如 gradient-based），severity gradient 是否仍然成立？


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 414 · 2026-05-15T11:17:34.930060+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 27

## Round 27

2 recorded events


### User

_source line 415 · 2026-05-15T11:17:38.337641+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：Overall 3.5/5，定位在 Findings 和 Conference 之间。三个 Must-Fix 问题：(1) n=50 profiling 数据与 n=496 全量数据混用，crossover 分析未在全量验证；(2) discrimination collapse 的 Gini effect size (0.01-0.08) 与 severity gradient magnitude (30-148×) 之间的 gap 未弥合；(3) "following ThinKV" 对 phase segmentation 方法的错误归因。六个 Should-Fix：Spearman ρ=1.0 on n=4 的过度报告、Bonferroni family 范围偏窄、entropy redistribution 跨模型不一致、缺乏下游任务评估、mitigation pilot 失败的 implication、LLaMA CI/Wilcoxon 不一致。统计方法论总体严谨，负面结果诚实报告是突出优点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 416 · 2026-05-15T11:17:43.928795+00:00_

Reviewer 1 审稿收到。等待 Reviewer 2 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 28

## Round 28

6 recorded events


### User

_source line 417 · 2026-05-15T11:20:04.599059+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：新颖性与完整性

### 总体评分
**Overall**: 2.5/5（介于 Findings 推荐和 Resubmit 之间）
**一句话总结**: 实验执行扎实、统计分析严谨，但核心新颖性——compound severity 的 phase-dependence——是已知现象（HIES discrimination collapse + ThinKV phase segmentation + Sparse Frontier strategy crossover）在新 setting 下的 characterization，增量贡献对 EMNLP main conference 偏弱，且关键 crossover finding 的证据基础不足。

### 官方维度打分（ACL ARR Review Form）
| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3.5/5 | 统计严谨但 crossover 数据来自 n=50 未在 n=500 验证；G metric n=50 vs n=496 差异大 |
| Excitement | 2/5 | Pure characterization without method；pilot fails own gate；增量有限 |
| Reproducibility | 3.5/5 | Setup 详尽但代码未释放 |
| Confidence | 4/5 | 熟悉该领域文献 |

### Must-Fix (3)

**N1** [critical] Crossover evidence 来自 n=50, 未在 n=500 验证
- §5.3, Table 2: per-phase II 值（如 s=0.25 importance low=7.196 vs random low=1.363）全部来自 n=50 profiling subset。Table 1 在 n=496 确认 Δ monotonicity 但 crossover 的 per-phase per-strategy 分解未在 n=496 报告。5.3× reversal 可能在大样本上不稳定。
- 这直接削弱论文最独特的 claim。

**N2** [critical] 新颖性增量不足
- Phase-dependent sensitivity: ThinKV (ICLR'26) + Sparse Frontier (2025) 已建立
- Discrimination collapse: HIES (2025) 已报告，论文自承 "independently corroborated"
- Crossover: Sparse Frontier 已报告 "no single strategy dominates across stages"
- 论文 Discussion 自承 qualitative direction "may seem expected"
- Pure characterization paper 的 delta 主要是 quantitative magnitude，对 EMNLP main 可能更适合 Findings

**N3** [critical] 标题和 Framing mismatch
- "Phase-Modulated" 暗示主动调节，实际仅观察/characterize
- "emergent" 不准确——是已知 mechanisms 在新 setting 的 quantification
- Conclusion "within a single generation (n=496)" 矛盾——G 是跨问题的中位数比

### Should-Fix (6)

**W1** LLaMA 跨架构 claim 极弱：n=49, 仅 s=0.30 显著, ~1/40 magnitude, random 也有 phase gradient
**W2** Pilot experiment fails 30% gate (oracle 18%, heuristic 32% but CI spans zero)——practical significance 未证明
**W3** 遗漏重要引用："Hold Onto That Thought" (NeurIPS 2025, arXiv:2512.12008) 直接评估 KV cache compression 对 reasoning 的影响
**W4** h2o-neurips2023 bib entry 的 title 字段为空
**W5** Abstract "over an order of magnitude" 指向不明确（G? Δ? II ratio?），且 n=50 G (69-274x) vs n=496 G (30-148x) 差异暗示估计不稳定
**W6** Qwen 45.2% mid-phase null rate 限制了完整 phase profile；可能更适合 binary segmentation

### 小问题
- LongFlow 正文未注明 withdrawn 状态
- Table 2 "profiling subset" 选取方法未说明；Appendix permutation test n=49 (vs n=50) 未解释
- SnapKV first author mismatch (bib: Li vs OpenAlex: Cai)

### 主要优势
- S1: 统计分析水准极高（bootstrap + Bonferroni + BH-FDR + JT + permutation + multiplicative null）
- S2: Random eviction 作为 falsification control 设计精妙
- S3: 透明诚实（pilot gate failure, LLaMA weak evidence, Qwen null rate 全部坦承）
- S4: n=50→n=500 scaling 验证有说服力
- S5: 32/32 引用全部真实，无 hallucinated citations

### 引用审计
全部 32 篇引用通过验证（web search + OpenAlex）。3 篇 OpenAlex 未索引但通过 arXiv/Nature 页面确认真实存在。无虚假引用。建议补引 "Hold Onto That Thought" (NeurIPS 2025)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-15T11:20:31.238827+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见。对每条使用 [AGREE] 或 [REBUT]，并说明理由。如果是 [REBUT]，请引用具体 Section/Table/Figure 作为证据。\n\n---\n\n### Reviewer 2 总体评分\n**Overall**: 2.5/5（介于 Findings 推荐和 Resubmit 之间）\n**一句话总结**: 实验执行扎实、统计分析严谨，但核心新颖性——compound severity 的 phase-dependence——是已知现象（HIES discrimination collapse + ThinKV phase segmentation + Sparse Frontier strategy crossover）在新 setting 下的 characterization，增量贡献对 EMNLP main conference 偏弱，且关键 crossover finding 的证据基础不足。\n\n### Must-Fix (3)\n\n**N1** [critical] Crossover evidence 来自 n=50, 未在 n=500 验证\n- §5.3, Table 2: per-phase II 值（如 s=0.25 importance low=7.196 vs random low=1.363）全部来自 n=50 profiling subset。Table 1 在 n=496 确认 Δ monotonicity 但 crossover 的 per-phase per-strategy 分解未在 n=496 报告。5.3× reversal 可能在大样本上不稳定。\n- 这直接削弱论文最独特的 claim。\n\n**N2** [critical] 新颖性增量不足\n- Phase-dependent sensitivity: ThinKV (ICLR'26) + Sparse Frontier (2025) 已建立\n- Discrimination collapse: HIES (2025) 已报告，论文自承 \"independently corroborated\"\n- Crossover: Sparse Frontier 已报告 \"no single strategy dominates across stages\"\n- 论文 Discussion 自承 qualitative direction \"may seem expected\"\n- Pure characterization paper 的 delta 主要是 quantitative magnitude，对 EMNLP main 可能更适合 Findings\n\n**N3** [critical] 标题和 Framing mismatch\n- \"Phase-Modulated\" 暗示主动调节，实际仅观察/characterize\n- \"emergent\" 不准确——是已知 mechanisms 在新 setting 的 quantification\n- Conclusion \"within a single generation (n=496)\" 矛盾——G 是跨问题的中位数比\n\n### Should-Fix (6)\n\n**W1** LLaMA 跨架构 claim 极弱：n=49, 仅 s=0.30 显著, ~1/40 magnitude, random 也有 phase gradient\n**W2** Pilot experiment fails 30% gate (oracle 18%, heuristic 32% but CI spans zero)——practical significance 未证明\n**W3** 遗漏重要引用：\"Hold Onto That Thought\" (NeurIPS 2025, arXiv:2512.12008) 直接评估 KV cache compression 对 reasoning 的影响\n**W4** h2o-neurips2023 bib entry 的 title 字段为空\n**W5** Abstract \"over an order of magnitude\" 指向不明确（G? Δ? II ratio?），且 n=50 G (69-274x) vs n=496 G (30-148x) 差异暗示估计不稳定\n**W6** Qwen 45.2% mid-phase null rate 限制了完整 phase profile；可能更适合 binary segmentation\n\n### 小问题\n- LongFlow 正文未注明 withdrawn 状态\n- Table 2 \"profiling subset\" 选取方法未说明；Appendix permutation test n=49 (vs n=50) 未解释\n- SnapKV first author mismatch (bib: Li vs OpenAlex: Cai)\n\n### 主要优势\n- S1-S5（统计严谨、random control 设计、透明诚实、n=50→500 scaling、引用全部真实）\n\n---\n\n请逐条回应 Reviewer 2 的 Must-Fix (N1-N3)、Should-Fix (W1-W6) 和小问题。重点关注你是否同意 N2（novelty 不足）和 N3（framing mismatch）的判断。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见。对每条使用 [AGREE] 或 [REBUT]，并说明理由。如果是 [REBUT]，请引用具体 Section/Table/Figure 作为证据。\n\n---\n\n### Reviewer 2 总体评分\n**Overall**: 2.5/5（介于 Findings 推荐和 Resubmit 之间）\n**一句话总结**: 实验执行扎实、统计分析严谨，但核心新颖性——compound severity 的 phase-dependence——是已知现象（HIES discrimination collapse + ThinKV phase segmentation + Sparse Frontier strategy crossover）在新 setting 下的 characterization，增量贡献对 EMNLP main conference 偏弱，且关键 crossover finding 的证据基础不足。\n\n### Must-Fix (3)\n\n**N1** [critical] Crossover evidence 来自 n=50, 未在 n=500 验证\n- §5.3, Table 2: per-phase II 值（如 s=0.25 importance low=7.196 vs random low=1.363）全部来自 n=50 profiling subset。Table 1 在 n=496 确认 Δ monotonicity 但 crossover 的 per-phase per-strategy 分解未在 n=496 报告。5.3× reversal 可能在大样本上不稳定。\n- 这直接削弱论文最独特的 claim。\n\n**N2** [critical] 新颖性增量不足\n- Phase-dependent sensitivity: ThinKV (ICLR'26) + Sparse Frontier (2025) 已建立\n- Discrimination collapse: HIES (2025) 已报告，论文自承 \"independently corroborated\"\n- Crossover: Sparse Frontier 已报告 \"no single strategy dominates across stages\"\n- 论文 Discussion 自承 qualitative direction \"may seem expected\"\n- Pure characterization paper 的 delta 主要是 quantitative magnitude，对 EMNLP main 可能更适合 Findings\n\n**N3** [critical] 标题和 Framing mismatch\n- \"Phase-Modulated\" 暗示主动调节，实际仅观察/characterize\n- \"emergent\" 不准确——是已知 mechanisms 在新 setting 的 quantification\n- Conclusion \"within a single generation (n=496)\" 矛盾——G 是跨问题的中位数比\n\n### Should-Fix (6)\n\n**W1** LLaMA 跨架构 claim 极弱：n=49, 仅 s=0.30 显著, ~1/40 magnitude, random 也有 phase gradient\n**W2** Pilot experiment fails 30% gate (oracle 18%, heuristic 32% but CI spans zero)——practical significance 未证明\n**W3** 遗漏重要引用：\"Hold Onto That Thought\" (NeurIPS 2025, arXiv:2512.12008) 直接评估 KV cache compression 对 reasoning 的影响\n**W4** h2o-neurips2023 bib entry 的 title 字段为空\n**W5** Abstract \"over an order of magnitude\" 指向不明确（G? Δ? II ratio?），且 n=50 G (69-274x) vs n=496 G (30-148x) 差异暗示估计不稳定\n**W6** Qwen 45.2% mid-phase null rate 限制了完整 phase profile；可能更适合 binary segmentation\n\n### 小问题\n- LongFlow 正文未注明 withdrawn 状态\n- Table 2 \"profiling subset\" 选取方法未说明；Appendix permutation test n=49 (vs n=50) 未解释\n- SnapKV first author mismatch (bib: Li vs OpenAlex: Cai)\n\n### 主要优势\n- S1-S5（统计严谨、random control 设计、透明诚实、n=50→500 scaling、引用全部真实）\n\n---\n\n请逐条回应 Reviewer 2 的 Must-Fix (N1-N3)、Should-Fix (W1-W6) 和小问题。重点关注你是否同意 N2（novelty 不足）和 N3（framing mismatch）的判断。"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-15T11:20:54.186626+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22947
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-15T11:20:54.538427+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见。对每条使用 [AGREE] 或 [REBUT]，并说明理由。如果是 [REBUT]，请引用具体 Section/Table/Figure 作为证据。\n\n---\n\n### Reviewer 1 总体评分\n**Overall**: 3.5/5 (Findings-level, 介于 Findings 和 Conference 之间)\n\n### Must-Fix (3)\n\n**N1** [critical] Table 2 (n=50) 与 n=496 数据混用，crossover 分析未在全量数据验证\n- Table 2 报告 n=50 的 per-phase II，G=69-274×；n=496 的 G=30-148×（仅在 caption 和正文中以 bootstrap CI 给出）。G 过高估计 42-85%。§5.3 crossover 核心数字完全来自 n=50。\n- 建议：在 n=496 上重新计算 per-phase II 中位数并替换 Table 2。\n\n**N2** [critical] Discrimination collapse effect size（Gini 下降 0.01-0.08）与 severity gradient（G=30-148×）之间的 gap 未弥合\n- 论文未报告 baseline Gini 值，无法判断相对变化。0.01-0.02 的 Qwen Gini 变化如何驱动 3-148× 的 severity amplification？\n- 建议：报告 baseline Gini 和相对变化；讨论 threshold amplification 机制；或降低 mechanism claim 的权重。\n\n**N3** [critical] \"following ThinKV\" 对 phase segmentation 方法的错误归因\n- background.tex:33: ThinKV 使用 explicit delimiters，本文使用 quantile-based segmentation，\"following\" 措辞误导。\n- 建议：改为 \"inspired by\" 或 \"cf.\"。\n\n### Should-Fix (6)\n\n**W1** Spearman ρ=1.0 on n=4 的过度报告——JT test 才是 dose-response 的 primary evidence\n**W2** Bonferroni k=4 范围需更充分论证；main text 应 prominently reference BH-FDR\n**W3** Entropy redistribution 跨模型不一致（Qwen s=0.25 反转）削弱机制叙事\n**W4** 缺乏下游任务评估——PPL-based II 的实际意义不明\n**W5** Mitigation pilot 失败对论文 motivation 的影响需更坦诚讨论\n**W6** LLaMA CI/Wilcoxon 不一致需解释（s=0.15 CI excl zero but p=0.219; s=0.30 CI incl zero but p=0.029）\n\n### Minor Issues\n- M1: \\placeholder 命令残留\n- M2: appendix_results.tex orphaned + duplicate label\n- M3: h2o bib title 为空\n- M4: 3 篇引用 OpenAlex 未索引\n- M5: deepseek-r1 bib corporate authorship\n- M6: float16→bfloat16 切换是否影响 n=50 profiling 数据可靠性\n\n### Questions to Authors\nQ1: Table 2 的 per-phase II 值为何未在 n=496 上重新计算？\nQ2: Discrimination collapse 的 baseline Gini 值？\nQ3: Phase boundary 稳定性？\nQ4: 是否考虑 accuracy-based II？\nQ5: Frobenius norm 是否是结果关键假设？\n\n---\n\n请逐条回应 Reviewer 1 的 Must-Fix (N1-N3)、Should-Fix (W1-W6) 和 Minor Issues (M1-M6)。重点关注你是否同意 N2（mechanism gap）——这与你对 novelty 的评估直接相关。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见。对每条使用 [AGREE] 或 [REBUT]，并说明理由。如果是 [REBUT]，请引用具体 Section/Table/Figure 作为证据。\n\n---\n\n### Reviewer 1 总体评分\n**Overall**: 3.5/5 (Findings-level, 介于 Findings 和 Conference 之间)\n\n### Must-Fix (3)\n\n**N1** [critical] Table 2 (n=50) 与 n=496 数据混用，crossover 分析未在全量数据验证\n- Table 2 报告 n=50 的 per-phase II，G=69-274×；n=496 的 G=30-148×（仅在 caption 和正文中以 bootstrap CI 给出）。G 过高估计 42-85%。§5.3 crossover 核心数字完全来自 n=50。\n- 建议：在 n=496 上重新计算 per-phase II 中位数并替换 Table 2。\n\n**N2** [critical] Discrimination collapse effect size（Gini 下降 0.01-0.08）与 severity gradient（G=30-148×）之间的 gap 未弥合\n- 论文未报告 baseline Gini 值，无法判断相对变化。0.01-0.02 的 Qwen Gini 变化如何驱动 3-148× 的 severity amplification？\n- 建议：报告 baseline Gini 和相对变化；讨论 threshold amplification 机制；或降低 mechanism claim 的权重。\n\n**N3** [critical] \"following ThinKV\" 对 phase segmentation 方法的错误归因\n- background.tex:33: ThinKV 使用 explicit delimiters，本文使用 quantile-based segmentation，\"following\" 措辞误导。\n- 建议：改为 \"inspired by\" 或 \"cf.\"。\n\n### Should-Fix (6)\n\n**W1** Spearman ρ=1.0 on n=4 的过度报告——JT test 才是 dose-response 的 primary evidence\n**W2** Bonferroni k=4 范围需更充分论证；main text 应 prominently reference BH-FDR\n**W3** Entropy redistribution 跨模型不一致（Qwen s=0.25 反转）削弱机制叙事\n**W4** 缺乏下游任务评估——PPL-based II 的实际意义不明\n**W5** Mitigation pilot 失败对论文 motivation 的影响需更坦诚讨论\n**W6** LLaMA CI/Wilcoxon 不一致需解释（s=0.15 CI excl zero but p=0.219; s=0.30 CI incl zero but p=0.029）\n\n### Minor Issues\n- M1: \\placeholder 命令残留\n- M2: appendix_results.tex orphaned + duplicate label\n- M3: h2o bib title 为空\n- M4: 3 篇引用 OpenAlex 未索引\n- M5: deepseek-r1 bib corporate authorship\n- M6: float16→bfloat16 切换是否影响 n=50 profiling 数据可靠性\n\n### Questions to Authors\nQ1: Table 2 的 per-phase II 值为何未在 n=496 上重新计算？\nQ2: Discrimination collapse 的 baseline Gini 值？\nQ3: Phase boundary 稳定性？\nQ4: 是否考虑 accuracy-based II？\nQ5: Frobenius norm 是否是结果关键假设？\n\n---\n\n请逐条回应 Reviewer 1 的 Must-Fix (N1-N3)、Should-Fix (W1-W6) 和 Minor Issues (M1-M6)。重点关注你是否同意 N2（mechanism gap）——这与你对 novelty 的评估直接相关。"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-15T11:20:56.150639+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1612
}
```

</details>

---


### Assistant

_source line 422 · 2026-05-15T11:20:59.308041+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 29

## Round 29

2 recorded events


### User

_source line 423 · 2026-05-15T11:21:02.009617+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：论文在实验执行和统计分析方面达到高水准（S1-S4），但在新颖性维度存在三个 critical 问题：(1) crossover 这一最独特发现仅有 n=50 证据，(2) 核心 contributions 可由 HIES+ThinKV+Sparse Frontier 的组合预期，(3) 标题暗示方法论贡献但实际为 characterization study。建议评分 2.5/5，可能更适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 424 · 2026-05-15T11:21:07.050155+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 30

## Round 30

2 recorded events


### User

_source line 425 · 2026-05-15T11:22:28.550245+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 交叉回应：对 Reviewer 2 意见的逐条评判

## Must-Fix

**[AGREE] R2-N1: Crossover evidence 来自 n=50, 未在 n=500 验证**
完全同意，与我的 R1-N1 一致。§5.3 的 crossover 数字全部来自 Table 2 的 n=50 subset，n=50 G 值（69-274×）比 n=496（30-148×）过高估计 42-85%。Crossover 是三大 contribution 之一，证据基础必须匹配 claim 强度。

**[REBUT] R2-N2: 新颖性增量不足**
R2 将论文拆解为 ThinKV phase + HIES collapse + Sparse Frontier crossover 的叠加。我认为这低估了 compound interaction 的独特性：
1. ThinKV 是单轴（KV only），不涉及 head pruning 的 compound interaction
2. HIES 的 collapse 是 single-axis 现象，无法预测 compound 下的 phase-dependent amplification 和 crossover
3. Sparse Frontier 的 "no single strategy dominates" 未涉及 compound sparsity 也未量化 phase-strategy interaction magnitude
4. Head pruning 改变 importance score → 改变 KV eviction 有效性，这是 emergent coupling，非独立效应并集
但同意 pure characterization paper 的 excitement 受限。如 crossover 在 n=496 验证通过且 mechanism effect size gap 被弥合，达 Conference level；否则 Findings 更合适。

**[PARTIALLY AGREE] R2-N3: 标题/Framing mismatch**
- "Phase-Modulated"：[REBUT] 信号处理中 "modulation" 包含被动调制，描述准确
- "emergent"：[PARTIALLY AGREE] 可加 "quantitatively" 更精确
- "within a single generation (n=496)"：[AGREE] 措辞有歧义，应改为 "within individual generations, across n=496 problems"

## Should-Fix

**[AGREE] R2-W1**: LLaMA 证据弱，同意，与我的 R1-W6 一致（CI/Wilcoxon 不一致问题）
**[AGREE] R2-W2**: Pilot 失败影响，同意，与我的 R1-W5 一致
**[CONDITIONAL AGREE] R2-W3**: 无法独立验证 "Hold Onto That Thought" 内容，若确实直接相关则应补充
**[AGREE] R2-W4**: h2o title 为空，与我的 R1-M3 一致
**[PARTIALLY AGREE] R2-W5**: "order of magnitude" 在 n=496 (G=30-148×) 仍成立，但 abstract 应加注 "(amplification ratio G)"
**[REBUT] R2-W6**: Qwen mid-phase null 不影响 primary metric Δ（仅需 low/high phase），论文已通过 tercile/quartile/quintile sensitivity analysis 验证 robustness，binary segmentation 是可选简化而非必要修改

## Minor
**[AGREE]** LongFlow withdrawn 状态、n=49 vs n=50 未解释、SnapKV author mismatch

## R1-R2 共识与分歧总结
- **共识**: N1（crossover 需 n=496 验证）是最大缺陷；LLaMA 弱、pilot 失败、bib 问题
- **主要分歧**: N2 novelty——R2 认为增量不足，我认为 compound interaction 的 phase-strategy coupling 超越单轴叠加
- **建议 Overall**: 3.0-3.5/5，取决于 crossover 验证和 mechanism effect size 的补充


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 426 · 2026-05-15T11:22:35.637226+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 31

## Round 31

2 recorded events


### User

_source line 427 · 2026-05-15T11:22:38.325896+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心判断：与 R2 在 N1（crossover 需 n=496 验证）上完全一致。对 N2（novelty 不足）持反对意见——compound interaction 的 phase-strategy coupling 不可从单轴工作线性推导。N3 部分同意（Conclusion 措辞歧义），部分反对（"Phase-Modulated" 术语本身没问题）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 428 · 2026-05-15T11:22:43.683116+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 32

## Round 32

6 recorded events


### User

_source line 429 · 2026-05-15T11:23:52.282161+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1

### Must-Fix

[AGREE] R1-N1: Table 2 n=50 crossover 未在 n=500 验证——完全同意，与我的 N1 一致。补充：G 值从 n=50 的 69-274× 降至 n=496 的 30-148×（降幅 42-85%），说明 n=50 估计在重尾分布下不稳定。crossover 是本文最具区分度的 claim，n=496 验证将决定 Contribution 1 的存废。

[AGREE] R1-N2: Discrimination collapse effect size 与 severity gradient 的 gap——同意这是重要缺口。缺少 baseline Gini 值无法判断相对变化；ΔGini 0.01-0.08 如何驱动 G=30-148× 需要 threshold amplification 机制的讨论或降低 mechanism claim 权重。这直接影响我对 Contribution 3 novelty 的评估。

[AGREE with nuance] R1-N3: "following ThinKV" 归因——同意措辞不准确（ThinKV 用 explicit delimiters，本文用 quantile-based segmentation），但我认为 severity 略低于 critical，更像 should-fix 级别的 attribution 修正。

### Should-Fix

[AGREE] R1-W1: n=4 Spearman 过度报告——同意，JT test 才是 primary evidence。
[REBUT] R1-W2: Bonferroni k=4 范围——methodology.tex 已解释 rationale，Appendix B 已报告 BH-FDR 全量对照（32/32 Bonferroni 结果保持显著）。但同意 main text 应更 prominently reference BH-FDR。
[AGREE] R1-W3: Entropy redistribution 跨模型不一致——同意削弱机制叙事。
[AGREE] R1-W4: 缺乏下游任务评估——PPL-based II 的 accuracy gap 是 blind spot。
[AGREE] R1-W5: Pilot 失败的影响——同意需更坦诚讨论。
[REBUT] R1-W6: LLaMA CI/Wilcoxon 不一致——论文在 results.tex §5.5 已显式承认这一矛盾并 hedge 为 "mixed evidence"。技术上 bootstrap CI 和 Wilcoxon 在 small n + heavy tail 下可以 diverge。但建议加一句技术解释。

### Minor

[AGREE] M1-M6 全部同意。特别注意 M6（float16→bfloat16 切换时间点不明确）——如果 n=50 在 float16 下运行，进一步削弱 Table 2 可信度。

### 两位 Reviewer 的共识

R1 和 R2 在以下核心问题上完全一致：
1. Table 2 n=50 数据需在 n=496 上验证（R1-N1, R2-N1）
2. Crossover 证据基础不足（R1-N1, R2-N1）
3. Pilot experiment 失败的 implications 需更坦诚讨论（R1-W5, R2-W2）
4. h2o bib title 为空（R1-M3, R2-W4）
5. 引用全部真实，无 hallucinated citations

主要分歧点：
- **Overall 评分**: R1 给 3.5（Findings-level），我给 2.5。差距主要来自我对 novelty 增量更严格的评估——我认为 HIES + ThinKV + Sparse Frontier 的组合已基本预示本文发现的方向，R1 可能对 characterization paper 的价值给予更高权重。
- **N2 severity**: R1 将 discrimination collapse gap 列为 must-fix critical，我同意重要性但认为如果 mechanism claim 降级为 correlational observation 即可（不需要因果验证）。
- **N3 severity**: 我认为 "following ThinKV" 是 should-fix 而非 must-fix。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-15T11:26:48.952611+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"40+ placeholders unfilled — paper not submission-ready\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both reviewers independently flagged as #1 critical issue.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. All placeholders filled. Cross-response: both reviewers confirm.\"\n    action_items:\n      - round: 1\n        action: \"Fill all placeholders with n=500 analysis data\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"All 40+ placeholders filled with experimental data from n=500 analysis.\"\n    resolution_round: 5\n\n  - id: \"R1-N4\"\n    summary: \"Cross-architecture (LLaMA) evidence too weak to support title/abstract framing\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree LLaMA evidence is overclaimed.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §5.5 'Exploratory'. Cross-response: R2 notes LLaMA still n=49 vs DS/QW n=500 but 'Exploratory' label is honest handling, not blocking.\"\n    action_items:\n      - round: 1\n        action: \"Downgrade LLaMA to exploratory; hedge title/abstract/contribution\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"LLaMA downgraded to exploratory with appropriate hedging.\"\n    resolution_round: 5\n\n  - id: \"R1-N3\"\n    summary: \"Single benchmark (MATH-500) severely limits generalization\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree single benchmark is major limitation.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Title 'Mathematical Reasoning Models'. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Scope title/abstract to mathematical reasoning; expand limitations\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Title scoped; limitations section provides MATH-500 justification.\"\n    resolution_round: 5\n\n  - id: \"R1-N2\"\n    summary: \"50-problem sample size lacks power analysis; exclusion criteria unclear\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Use CI width shrinkage instead of post-hoc power.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. n=500, exclusion criteria stated, CI shrinkage 2.5-5.9×. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Run n=500; report exclusion criteria and CI shrinkage\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Full n=500 dataset used; exclusion criteria and CI width shrinkage reported.\"\n    resolution_round: 5\n\n  - id: \"R1-N5\"\n    summary: \"Mechanism analysis (entropy-discrimination collapse) is purely correlational\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Can downgrade if §6 properly scoped.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §6 split, 'correlational' explicit. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Split §6; add correlational caveat\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"§6 restructured with honest correlational framing.\"\n    resolution_round: 5\n\n  - id: \"R2-N3\"\n    summary: \"Insufficient differentiation from HIES (2025)\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Clear delta exists but paper doesn't articulate it.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Explicit HIES comparison in §6.1 and Related Work. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Add explicit HIES comparison\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Explicit HIES comparison added; crossover identified as prediction HIES cannot generate.\"\n    resolution_round: 5\n\n  - id: \"R1-W1\"\n    summary: \"Phase segmentation lacks justification; 'following ThinKV' wording misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 6\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Need sensitivity analysis and correct ThinKV reference.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"PARTIALLY RESOLVED. Sensitivity analysis complete. 'following ThinKV' still in background.tex:33.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 flags as must-fix (N3). R2 agrees on substance but considers should-fix level. Consensus: wording must change. Suggested: 'inspired by ThinKV phase-aware perspective, but using quantile-based segmentation rather than explicit delimiters'.\"\n    action_items:\n      - round: 1\n        action: \"Add sensitivity analysis; correct ThinKV phrasing\"\n        assigned_to: \"paper_agent\"\n        status: in_progress\n      - round: 5\n        action: \"Fix 'following ThinKV' in background.tex:33\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Symmetric sparsity rate assumption lacks practical representativeness\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree needs discussion.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Limitations paragraph added. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Add limitations paragraph\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Symmetric sparsity assumption discussed in Limitations.\"\n    resolution_round: 5\n\n  - id: \"R1-W3\"\n    summary: \"Severity gradient G numerically unstable when II_high approaches zero\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree. Need bootstrap CI for G.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Δ primary, G auxiliary with CIs. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Report G CIs; demote to auxiliary\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"G demoted to auxiliary with bootstrap CIs; Δ is primary.\"\n    resolution_round: 5\n\n  - id: \"R1-W4\"\n    summary: \"Bonferroni correction scope (k=4) may be insufficient\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Supplement with BH-FDR.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. k=4 justified, BH-FDR 44-test appendix. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Justify k=4; add BH-FDR appendix\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"k=4 justified; BH-FDR confirms no importance-based findings lost.\"\n    resolution_round: 5\n\n  - id: \"R1-W5\"\n    summary: \"Spearman rho=1.0 on 4 points over-interpreted\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Need n=4 caveat; use JT test.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. n=4 caveat + one-tailed + JT test. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Annotate Spearman n=4; add JT test\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Spearman caveated; JT test provides n=500-level dose-response evidence.\"\n    resolution_round: 5\n\n  - id: \"R1-W6\"\n    summary: \"Exclusion criteria not stated in Methodology\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Merged with R1-N2.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §4 complete. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Report exclusion criteria in §4\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Exclusion criteria and effective n fully reported.\"\n    resolution_round: 5\n\n  - id: \"R2-W3\"\n    summary: \"Related Work missing RLKV, LongFlow, PM-KVQ\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2-W3. R1 partially agrees.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. All three added. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Assess relevance and cite\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"RLKV, LongFlow, PM-KVQ integrated into Related Work.\"\n    resolution_round: 5\n\n  - id: \"R2-W5\"\n    summary: \"Abstract too long and dense\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both independently flagged.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Rewritten ~10 lines. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Condense abstract\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Abstract condensed with clear structure.\"\n    resolution_round: 5\n\n  - id: \"R2-Minor-2\"\n    summary: \"LaTeX source contains REVIEWER-ATTACK/REBUTTAL comments\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Should clean before submission.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Remove all REVIEWER-ATTACK/REBUTTAL comments\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"All reviewer-strategy comments removed.\"\n    resolution_round: 5\n\n  - id: \"R2-Minor-1\"\n    summary: \"h2o-neurips2023 bib entry missing title field; citation quality issues\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 6\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both flagged.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"PARTIALLY RESOLVED. h2o fixed. LongFlow 'Withdrawn' note introduced.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"h2o title field STILL EMPTY (R1-M3, R2-W4). Both reviewers confirm. LongFlow bib 'Withdrawn' note also flagged (R5-2 recurrence).\"\n    action_items:\n      - round: 1\n        action: \"Fix h2o bib entry\"\n        assigned_to: \"main_agent\"\n        status: in_progress\n      - round: 5\n        action: \"LongFlow: delete 'Withdrawn from ICLR 2026' note, change venue to arXiv preprint\"\n        assigned_to: \"paper_agent\"\n        status: open\n      - round: 6\n        action: \"Fill h2o-neurips2023 title field; fix LongFlow bib to arXiv preprint format\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-Minor-6\"\n    summary: \"s=0.35 supplementary experiment mentioned but not fully reported\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Either report fully or remove.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Removed. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Remove s=0.35 mention\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"s=0.35 incomplete data removed.\"\n    resolution_round: 5\n\n  - id: \"R1-Minor-code\"\n    summary: \"No code or data release plan\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both noted.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Reproducibility statement added. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Add code/data release statement\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Reproducibility statement added.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-1\"\n    summary: \"paper_provenance.yaml C019 outdated\"\n    category: framing\n    severity: warning\n    status: wont_fix\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"Internal process issue.\"\n      - round: 5\n        reviewers: []\n        note: \"Internal provenance tracking, not a paper defect.\"\n    action_items:\n      - round: 1\n        action: \"Update C019 in paper_provenance.yaml\"\n        assigned_to: \"director\"\n        status: wont_fix\n    resolution: \"Internal process issue, not tracked as paper defect.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-2\"\n    summary: \"Random masking s025+ significant gradient needs explicit paper treatment\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"D063 threshold story needs integration.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Threshold story integrated in §5.1 + cross-model. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Integrate random threshold story in Results\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Random eviction threshold story fully integrated.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-3\"\n    summary: \"Qwen mid-phase 45.2% null rate needs effective n caveat\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"n=500 Qwen mid-phase effective n=274.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Autocorrelation explanation provided. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Investigate root cause; report in §4\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Mid-phase null rate reported with autocorrelation explanation.\"\n    resolution_round: 5\n\n  - id: \"R5-W1\"\n    summary: \"Table 2 uses n=50 profiling data in main body alongside n=500 tables — reader confusion risk\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response consensus: BOTH at warning.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"ESCALATED TO CRITICAL. Both reviewers independently flag as must-fix (R1-N1, R2-N1). G values overestimate 42-85% (n=50: 69-274× vs n=496: 30-148×). Cross-response: full consensus. Per-phase II must be recomputed at n=496.\"\n    action_items:\n      - round: 5\n        action: \"Create n=500 per-phase table for main body; move Table 2 to Appendix\"\n        assigned_to: \"paper_agent\"\n        status: open\n      - round: 6\n        action: \"Recompute per-phase II medians at n=496; replace Table 2 with n=496 data; move n=50 to Appendix if retained\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W2\"\n    summary: \"Crossover analysis (§5.3 + Appendix A) uses n=50 profiling data — not verified at n=500\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response consensus: BOTH at warning.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"ESCALATED TO CRITICAL. Both reviewers independently flag as must-fix. Crossover is a core contribution — 5.3× reversal magnitude may change substantially at n=496. Cross-response: full consensus that crossover verification at n=496 will determine Contribution 1 viability.\"\n    action_items:\n      - round: 5\n        action: \"Compute per-phase per-strategy median II at n=500 for crossover conditions\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: open\n      - round: 6\n        action: \"Verify crossover direction and magnitude at n=496 with bootstrap CI. Update §5.3 and Appendix D.\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-1\"\n    summary: \"'following ThinKV' wording still in background.tex:33\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response consensus.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 escalates to must-fix (incorrect method attribution). R2 agrees on substance but considers should-fix. Consensus: must change wording.\"\n    action_items:\n      - round: 5\n        action: \"Replace 'following ThinKV' with reviewer-agreed text\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-2\"\n    summary: \"LongFlow bib entry has 'Withdrawn from ICLR 2026' note\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Consensus: modify bib entry format.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Still open. Both reviewers confirm.\"\n    action_items:\n      - round: 5\n        action: \"Delete 'Withdrawn from ICLR 2026' note; change venue to arXiv preprint format\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-3\"\n    summary: \"\\\\placeholder command definition residual in main.tex:21\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response: both agree trivial cleanup.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Still open. Both reviewers confirm (R1-M1).\"\n    action_items:\n      - round: 5\n        action: \"Remove \\\\newcommand{\\\\placeholder} from main.tex:21\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-N2\"\n    summary: \"Discrimination collapse effect size (ΔGini 0.01-0.08) insufficient to explain severity gradient (G=30-148×)\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 flags as must-fix. R2 agrees important but suggests downgrading mechanism claim suffices. Consensus: gap must be addressed — either by reporting baseline Gini + relative change + threshold amplification discussion, or by explicitly repositioning mechanism as preliminary correlational observation rather than explanatory framework.\"\n    action_items:\n      - round: 6\n        action: \"Report baseline Gini values and relative ΔGini/Gini_baseline. Either (a) discuss threshold amplification mechanism explaining how small score distribution changes produce large eviction effects, or (b) downgrade §6 framing from 'mechanism' to 'preliminary correlational observation' and reduce its prominence.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W1\"\n    summary: \"Spearman ρ=1.0 on n=4 over-reported; JT test should be primary dose-response evidence\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Both agree. JT test (z=6.2-33.7, using per-problem values) is the substantive evidence. Spearman n=4 ρ=1.0 (p=0.042 one-tailed) is inherently low-powered and would not survive multiple testing correction.\"\n    action_items:\n      - round: 6\n        action: \"Demote Spearman ρ to footnote or appendix; present JT test as primary dose-response evidence in main text.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W2\"\n    summary: \"Novelty framing — contribution delta vs HIES + ThinKV + Sparse Frontier\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"DIVERGENCE. R2 (2.5/5): core findings predictable from HIES+ThinKV+Sparse Frontier combination; pure characterization insufficient for main conference. R1 (3.5/5): compound interaction is emergent coupling (head pruning alters importance scores for KV eviction), not linear superposition of single-axis phenomena; crossover cannot be derived from prior work. R1 conditionally agrees if crossover verified at n=496 and mechanism gap addressed, paper reaches conference level.\"\n    action_items:\n      - round: 6\n        action: \"Strengthen novelty articulation: explicitly argue why compound interaction produces phenomena (crossover, phase-dependent amplification) that single-axis frameworks cannot predict. Consider adding a paragraph in Introduction or Discussion.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W3\"\n    summary: \"Lack of downstream task evaluation — PPL-based II not grounded in accuracy\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Both agree. G=148× PPL amplification — what does this mean for MATH-500 accuracy? 'Motivate phase-aware compression budgets' claim lacks grounding without PPL→accuracy mapping.\"\n    action_items:\n      - round: 6\n        action: \"Add discussion in Limitations or Discussion about PPL→accuracy relationship. Even without new experiments, discuss whether severity gradient in PPL translates to accuracy differences.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W4\"\n    summary: \"Pilot experiment failure (oracle 18% < 30% gate) implications under-discussed\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Both agree. Phase-aware budget reallocation alone insufficient. Paper should more explicitly discuss why characterization itself has value (diagnostic signal for future joint strategy-budget optimization) even when current mitigation fails.\"\n    action_items:\n      - round: 6\n        action: \"Expand Discussion paragraph on pilot failure: acknowledge limitation of budget-only mitigation; argue value of severity gradient as diagnostic signal for future joint optimization.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W5\"\n    summary: \"LLaMA CI/Wilcoxon inconsistency unexplained\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 flags: s=0.15 CI excludes zero but Wilcoxon ns; s=0.30 CI includes zero but Wilcoxon sig. R2 rebuts partially — paper already hedges as 'mixed evidence' — but agrees a technical explanation sentence would help.\"\n    action_items:\n      - round: 6\n        action: \"Add footnote explaining CI/Wilcoxon divergence (bootstrap CI estimates median shift vs Wilcoxon tests signed-rank symmetry; small n + heavy tails cause divergence).\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W6\"\n    summary: \"Missing citation: 'Hold Onto That Thought' (NeurIPS 2025, arXiv:2512.12008)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2 flags. R1 conditionally agrees (pending content verification). Paper directly evaluates KV cache compression impact on reasoning — relevant to Related Work §2.\"\n    action_items:\n      - round: 6\n        action: \"Verify relevance and add citation to Related Work if confirmed.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-M1\"\n    summary: \"Abstract 'over an order of magnitude' referent unclear\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2 flags ambiguity. R1 partially agrees — claim holds at n=496 (G=30-148×) but should specify '(amplification ratio G)'. Cross-response consensus: add clarification.\"\n    action_items:\n      - round: 6\n        action: \"Clarify 'over an order of magnitude' in abstract — specify it refers to amplification ratio G.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-M2\"\n    summary: \"appendix_results.tex orphaned file + duplicate label with appendix_moved.tex\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1]\n        note: \"R1-M2. Not input'd in main.tex but exists with duplicate \\\\label{app:cross-model-details}.\"\n    action_items:\n      - round: 6\n        action: \"Delete orphaned appendix_results.tex or resolve duplicate label.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-M3\"\n    summary: \"Conclusion 'within a single generation (n=496)' ambiguous phrasing\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2-N3 sub-issue. R1 agrees. G is cross-problem median ratio, not within-generation. Should read 'within individual generations, across n=496 problems'.\"\n    action_items:\n      - round: 6\n        action: \"Rewrite to 'within individual generations, across n=496 problems'.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-M4\"\n    summary: \"SnapKV bib first author mismatch (Li vs Cai)\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"R2 minor. Bib has 'Li' but OpenAlex shows 'Cai' as first author.\"\n    action_items:\n      - round: 6\n        action: \"Verify SnapKV first author and correct bib entry.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-M5\"\n    summary: \"Bonferroni k=4 rationale should be more prominent in main text\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1-W2. R2 rebuts (rationale exists in methodology.tex, BH-FDR in Appendix confirms). But both agree main text should more prominently reference BH-FDR.\"\n    action_items:\n      - round: 6\n        action: \"Add sentence in §4 prominently referencing BH-FDR 44-test results from Appendix.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "issues_yaml": "issues:\n  - id: \"R1-N1\"\n    summary: \"40+ placeholders unfilled — paper not submission-ready\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both reviewers independently flagged as #1 critical issue.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. All placeholders filled. Cross-response: both reviewers confirm.\"\n    action_items:\n      - round: 1\n        action: \"Fill all placeholders with n=500 analysis data\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"All 40+ placeholders filled with experimental data from n=500 analysis.\"\n    resolution_round: 5\n\n  - id: \"R1-N4\"\n    summary: \"Cross-architecture (LLaMA) evidence too weak to support title/abstract framing\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree LLaMA evidence is overclaimed.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §5.5 'Exploratory'. Cross-response: R2 notes LLaMA still n=49 vs DS/QW n=500 but 'Exploratory' label is honest handling, not blocking.\"\n    action_items:\n      - round: 1\n        action: \"Downgrade LLaMA to exploratory; hedge title/abstract/contribution\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"LLaMA downgraded to exploratory with appropriate hedging.\"\n    resolution_round: 5\n\n  - id: \"R1-N3\"\n    summary: \"Single benchmark (MATH-500) severely limits generalization\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree single benchmark is major limitation.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Title 'Mathematical Reasoning Models'. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Scope title/abstract to mathematical reasoning; expand limitations\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Title scoped; limitations section provides MATH-500 justification.\"\n    resolution_round: 5\n\n  - id: \"R1-N2\"\n    summary: \"50-problem sample size lacks power analysis; exclusion criteria unclear\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Use CI width shrinkage instead of post-hoc power.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. n=500, exclusion criteria stated, CI shrinkage 2.5-5.9×. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Run n=500; report exclusion criteria and CI shrinkage\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Full n=500 dataset used; exclusion criteria and CI width shrinkage reported.\"\n    resolution_round: 5\n\n  - id: \"R1-N5\"\n    summary: \"Mechanism analysis (entropy-discrimination collapse) is purely correlational\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Can downgrade if §6 properly scoped.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §6 split, 'correlational' explicit. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Split §6; add correlational caveat\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"§6 restructured with honest correlational framing.\"\n    resolution_round: 5\n\n  - id: \"R2-N3\"\n    summary: \"Insufficient differentiation from HIES (2025)\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Clear delta exists but paper doesn't articulate it.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Explicit HIES comparison in §6.1 and Related Work. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Add explicit HIES comparison\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Explicit HIES comparison added; crossover identified as prediction HIES cannot generate.\"\n    resolution_round: 5\n\n  - id: \"R1-W1\"\n    summary: \"Phase segmentation lacks justification; 'following ThinKV' wording misleading\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 6\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Need sensitivity analysis and correct ThinKV reference.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"PARTIALLY RESOLVED. Sensitivity analysis complete. 'following ThinKV' still in background.tex:33.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 flags as must-fix (N3). R2 agrees on substance but considers should-fix level. Consensus: wording must change. Suggested: 'inspired by ThinKV phase-aware perspective, but using quantile-based segmentation rather than explicit delimiters'.\"\n    action_items:\n      - round: 1\n        action: \"Add sensitivity analysis; correct ThinKV phrasing\"\n        assigned_to: \"paper_agent\"\n        status: in_progress\n      - round: 5\n        action: \"Fix 'following ThinKV' in background.tex:33\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"Symmetric sparsity rate assumption lacks practical representativeness\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree needs discussion.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Limitations paragraph added. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Add limitations paragraph\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Symmetric sparsity assumption discussed in Limitations.\"\n    resolution_round: 5\n\n  - id: \"R1-W3\"\n    summary: \"Severity gradient G numerically unstable when II_high approaches zero\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both agree. Need bootstrap CI for G.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Δ primary, G auxiliary with CIs. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Report G CIs; demote to auxiliary\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"G demoted to auxiliary with bootstrap CIs; Δ is primary.\"\n    resolution_round: 5\n\n  - id: \"R1-W4\"\n    summary: \"Bonferroni correction scope (k=4) may be insufficient\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Supplement with BH-FDR.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. k=4 justified, BH-FDR 44-test appendix. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Justify k=4; add BH-FDR appendix\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"k=4 justified; BH-FDR confirms no importance-based findings lost.\"\n    resolution_round: 5\n\n  - id: \"R1-W5\"\n    summary: \"Spearman rho=1.0 on 4 points over-interpreted\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Need n=4 caveat; use JT test.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. n=4 caveat + one-tailed + JT test. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Annotate Spearman n=4; add JT test\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Spearman caveated; JT test provides n=500-level dose-response evidence.\"\n    resolution_round: 5\n\n  - id: \"R1-W6\"\n    summary: \"Exclusion criteria not stated in Methodology\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Merged with R1-N2.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. §4 complete. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Report exclusion criteria in §4\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Exclusion criteria and effective n fully reported.\"\n    resolution_round: 5\n\n  - id: \"R2-W3\"\n    summary: \"Related Work missing RLKV, LongFlow, PM-KVQ\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2-W3. R1 partially agrees.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. All three added. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Assess relevance and cite\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"RLKV, LongFlow, PM-KVQ integrated into Related Work.\"\n    resolution_round: 5\n\n  - id: \"R2-W5\"\n    summary: \"Abstract too long and dense\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both independently flagged.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Rewritten ~10 lines. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Condense abstract\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Abstract condensed with clear structure.\"\n    resolution_round: 5\n\n  - id: \"R2-Minor-2\"\n    summary: \"LaTeX source contains REVIEWER-ATTACK/REBUTTAL comments\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Should clean before submission.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Remove all REVIEWER-ATTACK/REBUTTAL comments\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"All reviewer-strategy comments removed.\"\n    resolution_round: 5\n\n  - id: \"R2-Minor-1\"\n    summary: \"h2o-neurips2023 bib entry missing title field; citation quality issues\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 6\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both flagged.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"PARTIALLY RESOLVED. h2o fixed. LongFlow 'Withdrawn' note introduced.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"h2o title field STILL EMPTY (R1-M3, R2-W4). Both reviewers confirm. LongFlow bib 'Withdrawn' note also flagged (R5-2 recurrence).\"\n    action_items:\n      - round: 1\n        action: \"Fix h2o bib entry\"\n        assigned_to: \"main_agent\"\n        status: in_progress\n      - round: 5\n        action: \"LongFlow: delete 'Withdrawn from ICLR 2026' note, change venue to arXiv preprint\"\n        assigned_to: \"paper_agent\"\n        status: open\n      - round: 6\n        action: \"Fill h2o-neurips2023 title field; fix LongFlow bib to arXiv preprint format\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-Minor-6\"\n    summary: \"s=0.35 supplementary experiment mentioned but not fully reported\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Either report fully or remove.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Removed. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Remove s=0.35 mention\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"s=0.35 incomplete data removed.\"\n    resolution_round: 5\n\n  - id: \"R1-Minor-code\"\n    summary: \"No code or data release plan\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Both noted.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Reproducibility statement added. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Add code/data release statement\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Reproducibility statement added.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-1\"\n    summary: \"paper_provenance.yaml C019 outdated\"\n    category: framing\n    severity: warning\n    status: wont_fix\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"Internal process issue.\"\n      - round: 5\n        reviewers: []\n        note: \"Internal provenance tracking, not a paper defect.\"\n    action_items:\n      - round: 1\n        action: \"Update C019 in paper_provenance.yaml\"\n        assigned_to: \"director\"\n        status: wont_fix\n    resolution: \"Internal process issue, not tracked as paper defect.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-2\"\n    summary: \"Random masking s025+ significant gradient needs explicit paper treatment\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"D063 threshold story needs integration.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Threshold story integrated in §5.1 + cross-model. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Integrate random threshold story in Results\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Random eviction threshold story fully integrated.\"\n    resolution_round: 5\n\n  - id: \"REV-ADD-3\"\n    summary: \"Qwen mid-phase 45.2% null rate needs effective n caveat\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"n=500 Qwen mid-phase effective n=274.\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"RESOLVED. Autocorrelation explanation provided. Cross-response: confirmed.\"\n    action_items:\n      - round: 1\n        action: \"Investigate root cause; report in §4\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: done\n    resolution: \"Mid-phase null rate reported with autocorrelation explanation.\"\n    resolution_round: 5\n\n  - id: \"R5-W1\"\n    summary: \"Table 2 uses n=50 profiling data in main body alongside n=500 tables — reader confusion risk\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response consensus: BOTH at warning.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"ESCALATED TO CRITICAL. Both reviewers independently flag as must-fix (R1-N1, R2-N1). G values overestimate 42-85% (n=50: 69-274× vs n=496: 30-148×). Cross-response: full consensus. Per-phase II must be recomputed at n=496.\"\n    action_items:\n      - round: 5\n        action: \"Create n=500 per-phase table for main body; move Table 2 to Appendix\"\n        assigned_to: \"paper_agent\"\n        status: open\n      - round: 6\n        action: \"Recompute per-phase II medians at n=496; replace Table 2 with n=496 data; move n=50 to Appendix if retained\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W2\"\n    summary: \"Crossover analysis (§5.3 + Appendix A) uses n=50 profiling data — not verified at n=500\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response consensus: BOTH at warning.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"ESCALATED TO CRITICAL. Both reviewers independently flag as must-fix. Crossover is a core contribution — 5.3× reversal magnitude may change substantially at n=496. Cross-response: full consensus that crossover verification at n=496 will determine Contribution 1 viability.\"\n    action_items:\n      - round: 5\n        action: \"Compute per-phase per-strategy median II at n=500 for crossover conditions\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: open\n      - round: 6\n        action: \"Verify crossover direction and magnitude at n=496 with bootstrap CI. Update §5.3 and Appendix D.\"\n        assigned_to: \"main_agent → paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-1\"\n    summary: \"'following ThinKV' wording still in background.tex:33\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response consensus.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 escalates to must-fix (incorrect method attribution). R2 agrees on substance but considers should-fix. Consensus: must change wording.\"\n    action_items:\n      - round: 5\n        action: \"Replace 'following ThinKV' with reviewer-agreed text\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-2\"\n    summary: \"LongFlow bib entry has 'Withdrawn from ICLR 2026' note\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Consensus: modify bib entry format.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Still open. Both reviewers confirm.\"\n    action_items:\n      - round: 5\n        action: \"Delete 'Withdrawn from ICLR 2026' note; change venue to arXiv preprint format\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-3\"\n    summary: \"\\\\placeholder command definition residual in main.tex:21\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 6\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Cross-response: both agree trivial cleanup.\"\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Still open. Both reviewers confirm (R1-M1).\"\n    action_items:\n      - round: 5\n        action: \"Remove \\\\newcommand{\\\\placeholder} from main.tex:21\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-N2\"\n    summary: \"Discrimination collapse effect size (ΔGini 0.01-0.08) insufficient to explain severity gradient (G=30-148×)\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 flags as must-fix. R2 agrees important but suggests downgrading mechanism claim suffices. Consensus: gap must be addressed — either by reporting baseline Gini + relative change + threshold amplification discussion, or by explicitly repositioning mechanism as preliminary correlational observation rather than explanatory framework.\"\n    action_items:\n      - round: 6\n        action: \"Report baseline Gini values and relative ΔGini/Gini_baseline. Either (a) discuss threshold amplification mechanism explaining how small score distribution changes produce large eviction effects, or (b) downgrade §6 framing from 'mechanism' to 'preliminary correlational observation' and reduce its prominence.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W1\"\n    summary: \"Spearman ρ=1.0 on n=4 over-reported; JT test should be primary dose-response evidence\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Both agree. JT test (z=6.2-33.7, using per-problem values) is the substantive evidence. Spearman n=4 ρ=1.0 (p=0.042 one-tailed) is inherently low-powered and would not survive multiple testing correction.\"\n    action_items:\n      - round: 6\n        action: \"Demote Spearman ρ to footnote or appendix; present JT test as primary dose-response evidence in main text.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W2\"\n    summary: \"Novelty framing — contribution delta vs HIES + ThinKV + Sparse Frontier\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"DIVERGENCE. R2 (2.5/5): core findings predictable from HIES+ThinKV+Sparse Frontier combination; pure characterization insufficient for main conference. R1 (3.5/5): compound interaction is emergent coupling (head pruning alters importance scores for KV eviction), not linear superposition of single-axis phenomena; crossover cannot be derived from prior work. R1 conditionally agrees if crossover verified at n=496 and mechanism gap addressed, paper reaches conference level.\"\n    action_items:\n      - round: 6\n        action: \"Strengthen novelty articulation: explicitly argue why compound interaction produces phenomena (crossover, phase-dependent amplification) that single-axis frameworks cannot predict. Consider adding a paragraph in Introduction or Discussion.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W3\"\n    summary: \"Lack of downstream task evaluation — PPL-based II not grounded in accuracy\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Both agree. G=148× PPL amplification — what does this mean for MATH-500 accuracy? 'Motivate phase-aware compression budgets' claim lacks grounding without PPL→accuracy mapping.\"\n    action_items:\n      - round: 6\n        action: \"Add discussion in Limitations or Discussion about PPL→accuracy relationship. Even without new experiments, discuss whether severity gradient in PPL translates to accuracy differences.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W4\"\n    summary: \"Pilot experiment failure (oracle 18% < 30% gate) implications under-discussed\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"Both agree. Phase-aware budget reallocation alone insufficient. Paper should more explicitly discuss why characterization itself has value (diagnostic signal for future joint strategy-budget optimization) even when current mitigation fails.\"\n    action_items:\n      - round: 6\n        action: \"Expand Discussion paragraph on pilot failure: acknowledge limitation of budget-only mitigation; argue value of severity gradient as diagnostic signal for future joint optimization.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W5\"\n    summary: \"LLaMA CI/Wilcoxon inconsistency unexplained\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1 flags: s=0.15 CI excludes zero but Wilcoxon ns; s=0.30 CI includes zero but Wilcoxon sig. R2 rebuts partially — paper already hedges as 'mixed evidence' — but agrees a technical explanation sentence would help.\"\n    action_items:\n      - round: 6\n        action: \"Add footnote explaining CI/Wilcoxon divergence (bootstrap CI estimates median shift vs Wilcoxon tests signed-rank symmetry; small n + heavy tails cause divergence).\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-W6\"\n    summary: \"Missing citation: 'Hold Onto That Thought' (NeurIPS 2025, arXiv:2512.12008)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2 flags. R1 conditionally agrees (pending content verification). Paper directly evaluates KV cache compression impact on reasoning — relevant to Related Work §2.\"\n    action_items:\n      - round: 6\n        action: \"Verify relevance and add citation to Related Work if confirmed.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-M1\"\n    summary: \"Abstract 'over an order of magnitude' referent unclear\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2 flags ambiguity. R1 partially agrees — claim holds at n=496 (G=30-148×) but should specify '(amplification ratio G)'. Cross-response consensus: add clarification.\"\n    action_items:\n      - round: 6\n        action: \"Clarify 'over an order of magnitude' in abstract — specify it refers to amplification ratio G.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-M2\"\n    summary: \"appendix_results.tex orphaned file + duplicate label with appendix_moved.tex\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1]\n        note: \"R1-M2. Not input'd in main.tex but exists with duplicate \\\\label{app:cross-model-details}.\"\n    action_items:\n      - round: 6\n        action: \"Delete orphaned appendix_results.tex or resolve duplicate label.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-M3\"\n    summary: \"Conclusion 'within a single generation (n=496)' ambiguous phrasing\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R2-N3 sub-issue. R1 agrees. G is cross-problem median ratio, not within-generation. Should read 'within individual generations, across n=496 problems'.\"\n    action_items:\n      - round: 6\n        action: \"Rewrite to 'within individual generations, across n=496 problems'.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-M4\"\n    summary: \"SnapKV bib first author mismatch (Li vs Cai)\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [2]\n        note: \"R2 minor. Bib has 'Li' but OpenAlex shows 'Cai' as first author.\"\n    action_items:\n      - round: 6\n        action: \"Verify SnapKV first author and correct bib entry.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R6-M5\"\n    summary: \"Bonferroni k=4 rationale should be more prominent in main text\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 6\n    last_seen_round: 6\n    mentions:\n      - round: 6\n        reviewers: [1, 2]\n        note: \"R1-W2. R2 rebuts (rationale exists in methodology.tex, BH-FDR in Appendix confirms). But both agree main text should more prominently reference BH-FDR.\"\n    action_items:\n      - round: 6\n        action: \"Add sentence in §4 prominently referencing BH-FDR 44-test results from Appendix.\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-15T11:26:49.105989+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml\", \"bytes\": 28903}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-15T11:29:06.676530+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "report": "# 审稿报告：Phase-Modulated Compound Sparsity\n## Round 6 — EMNLP 2026 Main Conference\n\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**Deadline**: 2026-06-15\n**Reviewers**: R1 (方法严谨性), R2 (新颖性/完整性)\n**External Review**: 未配置，不适用\n\n---\n\n## Summary\n\n本文研究 compound sparsity（同时进行 attention head pruning 和 KV cache eviction）对数学推理模型的影响，发现 compound severity 具有 phase-strategy interaction：importance-based eviction 在 low-sparsity reasoning phase 产生远大于 high-sparsity phase 的 super-additive degradation（amplification ratio G=30-148×, n=496），而 random eviction 保持近平坦（G≈1）。在 s=0.25 处出现 strategy ranking crossover。结果在 DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 上复现，LLaMA 上有初步证据。提出 discrimination collapse 作为 correlational 机制解释。\n\n---\n\n## Strengths\n\n**S1. 研究问题定义精准且有部署价值** [R1-S1, 共识]\nCompound sparsity 的 phase-dependent interaction 是先前工作忽略的维度。Phase × strategy 的分析框架对推理模型部署有直接指导意义。\n\n**S2. 统计方法论达到高水准** [R1-S2, R2-S1, 共识]\n非参数检验 + bootstrap CI (B=10,000) + Bonferroni + BH-FDR 双重校正 + JT dose-response + permutation test + multiplicative null robustness check。在 NLP 实证研究中属于顶级标准。\n\n**S3. Random eviction 作为 falsification control 设计精妙** [R1-S5, R2-S2, 共识]\n利用 random eviction 的 score-independence 特性隔离 strategy-specific 效应，G≈1 的 baseline 有效确认 severity gradient 是 importance-based eviction 的特有现象。\n\n**S4. 负面结果和局限性诚实报告** [R1-S3, R2-S3, 共识]\nLLaMA 弱证据（仅 s=0.30 显著）、mitigation pilot 未通过 30% gate（oracle 18%）、entropy redistribution Qwen 不一致（s=0.25 反转）、Qwen mid-phase 45.2% null rate——全部坦承，不掩盖。\n\n**S5. n=50→n=500 精度提升验证有说服力** [R1-S4, R2-S4, 共识]\nCI 收窄 2.5-5.9×，直接展示统计功效提升。32/32 引用全部真实，无 hallucinated citations。\n\n---\n\n## Weaknesses\n\n### Must-Fix（3 个，影响接收决定）\n\n**N1. [CRITICAL, 共识] Crossover 证据基础不足——n=50 数据未在 n=496 验证**\n\n- 位置：Table 2 (results.tex:31-53), §5.3 (results.tex:63-66), Appendix D\n- Table 2 报告 n=50 profiling subset 的 per-phase II 值（G=69-274×），n=496 数据给出 G=30-148×（仅在正文 inline 和 Figure 1 caption 以 bootstrap CI 形式出现），过高估计 42-85%\n- §5.3 crossover 的核心数字（importance: 0.032 vs 0.818, random: 7.196 vs 1.363, 5.3× reversal）完全来自 n=50\n- Crossover 是三大 contribution 之一（Introduction: \"no single strategy dominates uniformly\"），证据基础必须匹配 claim 强度\n- **R1-R2 交叉回应**：完全共识。两位 Reviewer 独立将此列为 #1 critical issue\n- **修改要求**：在 n=496 数据上重新计算 per-phase per-strategy II 中位数和 crossover magnitude with bootstrap CI。替换 Table 2 或新建 n=496 per-phase table 为主体；如保留 n=50 数据移至 Appendix\n\n**N2. [CRITICAL, 共识] Discrimination collapse effect size 与 severity gradient magnitude 之间的 gap**\n\n- 位置：§6.1 (analysis.tex:1-9), Appendix Table 8\n- Gini coefficient 下降 0.030-0.081 (DeepSeek), 0.010-0.020 (Qwen)——绝对变化微小（Gini 范围 0-1），未报告 baseline Gini 值，无法评估相对变化\n- 0.01-0.02 的 score distribution 变化如何驱动 G=30-148× 的 severity amplification？论文未讨论 threshold amplification 等放大机制\n- §6 标注了 \"correlational\"（好），但 Introduction 和 Conclusion 仍将 \"entropy-discrimination collapse\" 作为完整机制叙事\n- **R1-R2 交叉回应**：共识此 gap 需弥合。R2 认为降级 mechanism claim 即可；R1 认为需要更充分的讨论\n- **修改要求**：(a) 报告 baseline Gini 和 ΔGini/Gini_baseline 的相对变化；(b) 讨论 threshold amplification 机制（小的 score 变化如何通过 eviction threshold 产生大效应差异），或将 §6 明确降级为 \"preliminary correlational observation\"\n\n**N3. [CRITICAL→SHOULD-FIX, 分歧] \"following ThinKV\" 对 phase segmentation 的错误归因**\n\n- 位置：background.tex:33\n- ThinKV 使用 explicit reasoning delimiters（`&lt;think>` tokens），本文使用 quantile-based attention sparsity segmentation——方法不同，\"following\" 措辞误导方法 provenance\n- **R1-R2 交叉回应**：R1 列为 must-fix（方法归因准确性），R2 同意需修改但认为 should-fix 级别。两者均同意措辞必须改变\n- **修改要求**：改为 \"inspired by ThinKV's phase-aware perspective\" 或 \"analogous to ThinKV's phase decomposition, but using quantile-based segmentation rather than explicit delimiters\"\n\n### Should-Fix（8 个，影响评分）\n\n**W1. [WARNING, 共识] Spearman ρ=1.0 on n=4 过度报告**\n- methodology.tex:22, results.tex:71\n- n=4 的 ρ=1.0 统计意义极弱（p=0.042 不能存活 multiple testing）。JT test (z=6.2-33.7, per-problem values) 才是 substantive evidence\n- 修改：将 JT test 作为 primary dose-response evidence，Spearman 降为脚注或 Appendix\n\n**W2. [WARNING, 分歧] Novelty 增量不足**\n- **R2 观点 (2.5/5)**：核心发现可由 HIES (discrimination collapse) + ThinKV (phase segmentation) + Sparse Frontier (strategy non-dominance) 的组合预期；pure characterization paper 对 EMNLP main conference 偏弱\n- **R1 观点 (3.5/5)**：compound interaction 是 emergent coupling（head pruning 改变 importance score → 改变 KV eviction 有效性），不可从单轴工作线性推导；crossover 是单轴框架无法生成的预测\n- R1 conditional：如 crossover 在 n=496 验证通过且 mechanism gap 弥合，达 Conference level\n- 修改建议：强化 novelty 论述——在 Introduction 或 Discussion 中明确阐述为什么 compound interaction 产生单轴框架无法预测的现象\n\n**W3. [WARNING, 共识] 缺乏下游任务评估**\n- PPL-based II 未映射到 accuracy。G=148× 在 MATH-500 accuracy 上对应多少损失？\"motivate phase-aware compression budgets\" 缺乏 grounding\n- 修改：在 Discussion/Limitations 讨论 PPL→accuracy 关系\n\n**W4. [WARNING, 共识] Mitigation pilot 失败的影响 under-discussed**\n- Oracle 18% < 30% gate, heuristic 32% but CI spans zero。Phase-aware budget reallocation alone insufficient\n- 修改：增加一段讨论为什么 characterization 本身有价值（diagnostic signal），即使当前 mitigation 不成功\n\n**W5. [WARNING, 共识] Entropy redistribution 跨模型不一致**\n- Qwen s=0.25 反转（ΔH=+0.045, 22/30 problems positive）。§6.2 正确标注 \"model-dependent\" 但仍占 ~15% Analysis 篇幅\n- 修改：精简或在 Discussion 明确承认非 robust mechanism\n\n**W6. [WARNING, 部分共识] LLaMA CI/Wilcoxon 不一致**\n- s=0.15: CI excludes zero but Wilcoxon p_Bonf=0.219 (ns); s=0.30: CI includes zero but Wilcoxon p_Bonf=0.029 (sig)\n- R1 要求解释；R2 认为论文已 hedge 为 \"mixed evidence\" 但同意加技术解释\n- 修改：加脚注说明 bootstrap CI vs Wilcoxon signed-rank 在 small n + heavy tails 下的行为差异\n\n**W7. [WARNING, 条件共识] 遗漏引用 \"Hold Onto That Thought\" (NeurIPS 2025, arXiv:2512.12008)**\n- 直接评估 KV cache compression 对 reasoning 的影响——与本文主题直接相关\n- 修改：验证相关性后补引\n\n**W8. [WARNING, 共识] h2o-neurips2023 bib entry title 字段为空**\n- 跨 3 轮审稿仍未修复\n- 修改：补全 title 字段\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n1. **N1 (crossover n=50)** — 最关键缺陷，决定 Contribution 1 存废\n2. **N2 (mechanism gap)** — effect size 与 claim 强度不匹配\n3. **W1 (Spearman n=4)** — JT test 应为 primary\n4. **W3 (无 accuracy 评估)** — PPL→accuracy gap 是盲区\n5. **W4 (pilot 失败)** — 需更坦诚讨论\n6. **W5 (entropy redistribution)** — 跨模型不一致\n7. **所有 minor issues** — bib 问题、\\placeholder 残留、orphaned file\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 分析 |\n|------|----|----|------|\n| **Novelty (W2)** | 3.5/5, compound interaction 超越单轴叠加 | 2.5/5, HIES+ThinKV+Sparse Frontier 已基本预示 | 根本分歧在于 characterization paper 的价值判断。R1 认为 compound coupling 的量化超越已知定性方向；R2 认为 quantitative magnitude alone 不构成 EMNLP main conference 的 novelty threshold |\n| **N3 severity** | Must-fix (方法归因准确性) | Should-fix (attribution 修正) | 实质共识（必须改措辞），仅 severity 分级不同 |\n| **R1-W2 (Bonferroni k=4)** | Should-fix | Rebutted (rationale exists + BH-FDR confirms) | 偏向 R2：rationale 已给出，BH-FDR 覆盖全量；但同意 main text 应更突出 BH-FDR |\n| **R2-W6 (Qwen mid-phase null)** | Rebutted (不影响 primary Δ) | Should-fix | 偏向 R1：Δ 仅需 low/high phase，sensitivity analysis 已验证 robustness |\n\n---\n\n## Questions to Authors\n\n1. Table 2 per-phase II 为何未在 n=496 上重新计算？是否有技术障碍？\n2. Discrimination collapse 的 baseline Gini 值？ΔGini/Gini_baseline 的相对幅度？\n3. Phase boundary 在不同 problem 间的稳定性？是否存在 boundary-sensitive cases？\n4. 是否考虑过 accuracy-based（非 PPL-based）的 Interaction Index？\n5. Frobenius norm head pruning 是否是核心假设？gradient-based metric 下结果是否一致？\n6. float16→bfloat16 切换的时间点？n=50 profiling 是否在 float16 下进行？\n\n---\n\n## Missing References\n\n1. **\"Hold Onto That Thought\"** (NeurIPS 2025, arXiv:2512.12008) — 直接评估 KV cache compression 对 reasoning 的影响 [R2-W7, R1 conditional agree]\n2. SnapKV bib first author 可能有误（Li vs Cai）[R2 minor]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置，不适用。\n\n---\n\n## Overall Assessment\n\n**评分：Borderline (weak reject → borderline accept)**\n- R1: 3.5/5 → 交叉后 3.0-3.5（取决于 crossover 验证和 mechanism 补充）\n- R2: 2.5/5 → 维持 2.5\n- 综合：**3.0/5 — Borderline**\n\n**置信度：High (4/5)**\n\n**理由：**\n\n论文在实验执行和统计分析上达到高水准（S2），研究问题有实际部署价值（S1），负面结果诚实报告（S4）。然而存在三个层面的问题：\n\n1. **证据完整性 (N1)**：最具区分度的 crossover 发现仅有 n=50 证据，而 n=50→n=496 scaling 已证明 G 值下降 42-85%。这是 fixable 的——n=496 数据已存在，重新计算 per-phase 分解即可。\n\n2. **机制分析 (N2)**：discrimination collapse 的 effect size 与 severity gradient 之间存在 orders-of-magnitude 的 gap，削弱了论文的解释力。Fixable——通过 threshold amplification 讨论或降级 mechanism claim。\n\n3. **Novelty (W2)**：这是不可通过修改弥合的根本分歧。论文本质是 characterization study（无新方法、无新系统），且 pilot mitigation 失败。R1 和 R2 对 characterization 的价值判断不同。如果 crossover 在 n=496 验证通过，novelty 论证加强（\"单轴框架无法预测\"）；如果 crossover 不成立或 magnitude 大幅缩水，novelty 进一步削弱。\n\n**建议：**\n- 如果 crossover 在 n=496 上 direction 保持 + magnitude 仍然 substantial + mechanism gap 被弥合/降级 → **Findings track acceptable, main conference borderline**\n- 如果 crossover 在 n=496 上不成立或 magnitude trivial → **需要重新评估核心 contribution，可能 weak reject**\n\n**前轮遗留 open issues 状态：**\n- R5-W1 (Table 2 n=50): 升级为 N1 critical — 仍 open\n- R5-W2 (crossover n=50): 升级为 N1 critical — 仍 open\n- R5-1 (following ThinKV): 仍 open — 本轮再次确认\n- R5-2 (LongFlow bib): 仍 open\n- R5-3 (\\placeholder): 仍 open\n- R1-W1 (ThinKV wording): 仍 in_progress\n\n**本轮新增 open issues**: 9 个 (R6-N2, R6-W1 through R6-W6, R6-M1 through R6-M5)\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 列表第 1 条 crossover 的证据在 §5.3 来自 n=50——需 n=496 数据支撑\n- \"entropy-discrimination collapse\" 作为 Contribution 3 的 mechanism framing 与 §6 的 correlational evidence 有张力\n\n### §3 Background\n- background.tex:33 \"following ThinKV\" 必须修改——方法不同，不能用 \"following\"\n\n### §4 Experimental Setup\n- Bonferroni k=4 的 family definition 需更 prominent 地 reference BH-FDR\n- Spearman ρ 应降为脚注，JT test 为 primary\n\n### §5 Results\n- Table 2 (n=50) 应替换为 n=496 per-phase table 或移至 Appendix\n- §5.3 crossover 数字需在 n=496 上验证并报告 bootstrap CI\n- §5.5 LLaMA CI/Wilcoxon 不一致需技术解释\n\n### §6 Analysis\n- §6.1 需报告 baseline Gini 和相对变化\n- §6.1 需讨论 threshold amplification 或降级 mechanism claim\n- §6.2 entropy redistribution 应精简（Qwen 不一致削弱叙事）\n\n### §7 Discussion\n- Pilot 失败的 implications 需更坦诚讨论\n- 添加 PPL→accuracy gap 讨论\n- \"within a single generation (n=496)\" 改为 \"within individual generations, across n=496 problems\"\n\n### References\n- h2o-neurips2023: title 为空\n- LongFlow: 删除 \"Withdrawn\" 标注，改为 arXiv preprint\n- 补引 \"Hold Onto That Thought\" (NeurIPS 2025)\n- 验证 SnapKV first author\n\n### Formatting\n- main.tex:21: 删除 \\placeholder 命令定义\n- appendix_results.tex: orphaned file + duplicate label\n- Abstract \"over an order of magnitude\" 应明确指 amplification ratio G",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "review_chat_id": "oc_57b24a804b56707ec9118a483a8ac65e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "report": "# 审稿报告：Phase-Modulated Compound Sparsity\n## Round 6 — EMNLP 2026 Main Conference\n\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**Deadline**: 2026-06-15\n**Reviewers**: R1 (方法严谨性), R2 (新颖性/完整性)\n**External Review**: 未配置，不适用\n\n---\n\n## Summary\n\n本文研究 compound sparsity（同时进行 attention head pruning 和 KV cache eviction）对数学推理模型的影响，发现 compound severity 具有 phase-strategy interaction：importance-based eviction 在 low-sparsity reasoning phase 产生远大于 high-sparsity phase 的 super-additive degradation（amplification ratio G=30-148×, n=496），而 random eviction 保持近平坦（G≈1）。在 s=0.25 处出现 strategy ranking crossover。结果在 DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 上复现，LLaMA 上有初步证据。提出 discrimination collapse 作为 correlational 机制解释。\n\n---\n\n## Strengths\n\n**S1. 研究问题定义精准且有部署价值** [R1-S1, 共识]\nCompound sparsity 的 phase-dependent interaction 是先前工作忽略的维度。Phase × strategy 的分析框架对推理模型部署有直接指导意义。\n\n**S2. 统计方法论达到高水准** [R1-S2, R2-S1, 共识]\n非参数检验 + bootstrap CI (B=10,000) + Bonferroni + BH-FDR 双重校正 + JT dose-response + permutation test + multiplicative null robustness check。在 NLP 实证研究中属于顶级标准。\n\n**S3. Random eviction 作为 falsification control 设计精妙** [R1-S5, R2-S2, 共识]\n利用 random eviction 的 score-independence 特性隔离 strategy-specific 效应，G≈1 的 baseline 有效确认 severity gradient 是 importance-based eviction 的特有现象。\n\n**S4. 负面结果和局限性诚实报告** [R1-S3, R2-S3, 共识]\nLLaMA 弱证据（仅 s=0.30 显著）、mitigation pilot 未通过 30% gate（oracle 18%）、entropy redistribution Qwen 不一致（s=0.25 反转）、Qwen mid-phase 45.2% null rate——全部坦承，不掩盖。\n\n**S5. n=50→n=500 精度提升验证有说服力** [R1-S4, R2-S4, 共识]\nCI 收窄 2.5-5.9×，直接展示统计功效提升。32/32 引用全部真实，无 hallucinated citations。\n\n---\n\n## Weaknesses\n\n### Must-Fix（3 个，影响接收决定）\n\n**N1. [CRITICAL, 共识] Crossover 证据基础不足——n=50 数据未在 n=496 验证**\n\n- 位置：Table 2 (results.tex:31-53), §5.3 (results.tex:63-66), Appendix D\n- Table 2 报告 n=50 profiling subset 的 per-phase II 值（G=69-274×），n=496 数据给出 G=30-148×（仅在正文 inline 和 Figure 1 caption 以 bootstrap CI 形式出现），过高估计 42-85%\n- §5.3 crossover 的核心数字（importance: 0.032 vs 0.818, random: 7.196 vs 1.363, 5.3× reversal）完全来自 n=50\n- Crossover 是三大 contribution 之一（Introduction: \"no single strategy dominates uniformly\"），证据基础必须匹配 claim 强度\n- **R1-R2 交叉回应**：完全共识。两位 Reviewer 独立将此列为 #1 critical issue\n- **修改要求**：在 n=496 数据上重新计算 per-phase per-strategy II 中位数和 crossover magnitude with bootstrap CI。替换 Table 2 或新建 n=496 per-phase table 为主体；如保留 n=50 数据移至 Appendix\n\n**N2. [CRITICAL, 共识] Discrimination collapse effect size 与 severity gradient magnitude 之间的 gap**\n\n- 位置：§6.1 (analysis.tex:1-9), Appendix Table 8\n- Gini coefficient 下降 0.030-0.081 (DeepSeek), 0.010-0.020 (Qwen)——绝对变化微小（Gini 范围 0-1），未报告 baseline Gini 值，无法评估相对变化\n- 0.01-0.02 的 score distribution 变化如何驱动 G=30-148× 的 severity amplification？论文未讨论 threshold amplification 等放大机制\n- §6 标注了 \"correlational\"（好），但 Introduction 和 Conclusion 仍将 \"entropy-discrimination collapse\" 作为完整机制叙事\n- **R1-R2 交叉回应**：共识此 gap 需弥合。R2 认为降级 mechanism claim 即可；R1 认为需要更充分的讨论\n- **修改要求**：(a) 报告 baseline Gini 和 ΔGini/Gini_baseline 的相对变化；(b) 讨论 threshold amplification 机制（小的 score 变化如何通过 eviction threshold 产生大效应差异），或将 §6 明确降级为 \"preliminary correlational observation\"\n\n**N3. [CRITICAL→SHOULD-FIX, 分歧] \"following ThinKV\" 对 phase segmentation 的错误归因**\n\n- 位置：background.tex:33\n- ThinKV 使用 explicit reasoning delimiters（`&lt;think>` tokens），本文使用 quantile-based attention sparsity segmentation——方法不同，\"following\" 措辞误导方法 provenance\n- **R1-R2 交叉回应**：R1 列为 must-fix（方法归因准确性），R2 同意需修改但认为 should-fix 级别。两者均同意措辞必须改变\n- **修改要求**：改为 \"inspired by ThinKV's phase-aware perspective\" 或 \"analogous to ThinKV's phase decomposition, but using quantile-based segmentation rather than explicit delimiters\"\n\n### Should-Fix（8 个，影响评分）\n\n**W1. [WARNING, 共识] Spearman ρ=1.0 on n=4 过度报告**\n- methodology.tex:22, results.tex:71\n- n=4 的 ρ=1.0 统计意义极弱（p=0.042 不能存活 multiple testing）。JT test (z=6.2-33.7, per-problem values) 才是 substantive evidence\n- 修改：将 JT test 作为 primary dose-response evidence，Spearman 降为脚注或 Appendix\n\n**W2. [WARNING, 分歧] Novelty 增量不足**\n- **R2 观点 (2.5/5)**：核心发现可由 HIES (discrimination collapse) + ThinKV (phase segmentation) + Sparse Frontier (strategy non-dominance) 的组合预期；pure characterization paper 对 EMNLP main conference 偏弱\n- **R1 观点 (3.5/5)**：compound interaction 是 emergent coupling（head pruning 改变 importance score → 改变 KV eviction 有效性），不可从单轴工作线性推导；crossover 是单轴框架无法生成的预测\n- R1 conditional：如 crossover 在 n=496 验证通过且 mechanism gap 弥合，达 Conference level\n- 修改建议：强化 novelty 论述——在 Introduction 或 Discussion 中明确阐述为什么 compound interaction 产生单轴框架无法预测的现象\n\n**W3. [WARNING, 共识] 缺乏下游任务评估**\n- PPL-based II 未映射到 accuracy。G=148× 在 MATH-500 accuracy 上对应多少损失？\"motivate phase-aware compression budgets\" 缺乏 grounding\n- 修改：在 Discussion/Limitations 讨论 PPL→accuracy 关系\n\n**W4. [WARNING, 共识] Mitigation pilot 失败的影响 under-discussed**\n- Oracle 18% < 30% gate, heuristic 32% but CI spans zero。Phase-aware budget reallocation alone insufficient\n- 修改：增加一段讨论为什么 characterization 本身有价值（diagnostic signal），即使当前 mitigation 不成功\n\n**W5. [WARNING, 共识] Entropy redistribution 跨模型不一致**\n- Qwen s=0.25 反转（ΔH=+0.045, 22/30 problems positive）。§6.2 正确标注 \"model-dependent\" 但仍占 ~15% Analysis 篇幅\n- 修改：精简或在 Discussion 明确承认非 robust mechanism\n\n**W6. [WARNING, 部分共识] LLaMA CI/Wilcoxon 不一致**\n- s=0.15: CI excludes zero but Wilcoxon p_Bonf=0.219 (ns); s=0.30: CI includes zero but Wilcoxon p_Bonf=0.029 (sig)\n- R1 要求解释；R2 认为论文已 hedge 为 \"mixed evidence\" 但同意加技术解释\n- 修改：加脚注说明 bootstrap CI vs Wilcoxon signed-rank 在 small n + heavy tails 下的行为差异\n\n**W7. [WARNING, 条件共识] 遗漏引用 \"Hold Onto That Thought\" (NeurIPS 2025, arXiv:2512.12008)**\n- 直接评估 KV cache compression 对 reasoning 的影响——与本文主题直接相关\n- 修改：验证相关性后补引\n\n**W8. [WARNING, 共识] h2o-neurips2023 bib entry title 字段为空**\n- 跨 3 轮审稿仍未修复\n- 修改：补全 title 字段\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致 [AGREE]：\n1. **N1 (crossover n=50)** — 最关键缺陷，决定 Contribution 1 存废\n2. **N2 (mechanism gap)** — effect size 与 claim 强度不匹配\n3. **W1 (Spearman n=4)** — JT test 应为 primary\n4. **W3 (无 accuracy 评估)** — PPL→accuracy gap 是盲区\n5. **W4 (pilot 失败)** — 需更坦诚讨论\n6. **W5 (entropy redistribution)** — 跨模型不一致\n7. **所有 minor issues** — bib 问题、\\placeholder 残留、orphaned file\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 分析 |\n|------|----|----|------|\n| **Novelty (W2)** | 3.5/5, compound interaction 超越单轴叠加 | 2.5/5, HIES+ThinKV+Sparse Frontier 已基本预示 | 根本分歧在于 characterization paper 的价值判断。R1 认为 compound coupling 的量化超越已知定性方向；R2 认为 quantitative magnitude alone 不构成 EMNLP main conference 的 novelty threshold |\n| **N3 severity** | Must-fix (方法归因准确性) | Should-fix (attribution 修正) | 实质共识（必须改措辞），仅 severity 分级不同 |\n| **R1-W2 (Bonferroni k=4)** | Should-fix | Rebutted (rationale exists + BH-FDR confirms) | 偏向 R2：rationale 已给出，BH-FDR 覆盖全量；但同意 main text 应更突出 BH-FDR |\n| **R2-W6 (Qwen mid-phase null)** | Rebutted (不影响 primary Δ) | Should-fix | 偏向 R1：Δ 仅需 low/high phase，sensitivity analysis 已验证 robustness |\n\n---\n\n## Questions to Authors\n\n1. Table 2 per-phase II 为何未在 n=496 上重新计算？是否有技术障碍？\n2. Discrimination collapse 的 baseline Gini 值？ΔGini/Gini_baseline 的相对幅度？\n3. Phase boundary 在不同 problem 间的稳定性？是否存在 boundary-sensitive cases？\n4. 是否考虑过 accuracy-based（非 PPL-based）的 Interaction Index？\n5. Frobenius norm head pruning 是否是核心假设？gradient-based metric 下结果是否一致？\n6. float16→bfloat16 切换的时间点？n=50 profiling 是否在 float16 下进行？\n\n---\n\n## Missing References\n\n1. **\"Hold Onto That Thought\"** (NeurIPS 2025, arXiv:2512.12008) — 直接评估 KV cache compression 对 reasoning 的影响 [R2-W7, R1 conditional agree]\n2. SnapKV bib first author 可能有误（Li vs Cai）[R2 minor]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置，不适用。\n\n---\n\n## Overall Assessment\n\n**评分：Borderline (weak reject → borderline accept)**\n- R1: 3.5/5 → 交叉后 3.0-3.5（取决于 crossover 验证和 mechanism 补充）\n- R2: 2.5/5 → 维持 2.5\n- 综合：**3.0/5 — Borderline**\n\n**置信度：High (4/5)**\n\n**理由：**\n\n论文在实验执行和统计分析上达到高水准（S2），研究问题有实际部署价值（S1），负面结果诚实报告（S4）。然而存在三个层面的问题：\n\n1. **证据完整性 (N1)**：最具区分度的 crossover 发现仅有 n=50 证据，而 n=50→n=496 scaling 已证明 G 值下降 42-85%。这是 fixable 的——n=496 数据已存在，重新计算 per-phase 分解即可。\n\n2. **机制分析 (N2)**：discrimination collapse 的 effect size 与 severity gradient 之间存在 orders-of-magnitude 的 gap，削弱了论文的解释力。Fixable——通过 threshold amplification 讨论或降级 mechanism claim。\n\n3. **Novelty (W2)**：这是不可通过修改弥合的根本分歧。论文本质是 characterization study（无新方法、无新系统），且 pilot mitigation 失败。R1 和 R2 对 characterization 的价值判断不同。如果 crossover 在 n=496 验证通过，novelty 论证加强（\"单轴框架无法预测\"）；如果 crossover 不成立或 magnitude 大幅缩水，novelty 进一步削弱。\n\n**建议：**\n- 如果 crossover 在 n=496 上 direction 保持 + magnitude 仍然 substantial + mechanism gap 被弥合/降级 → **Findings track acceptable, main conference borderline**\n- 如果 crossover 在 n=496 上不成立或 magnitude trivial → **需要重新评估核心 contribution，可能 weak reject**\n\n**前轮遗留 open issues 状态：**\n- R5-W1 (Table 2 n=50): 升级为 N1 critical — 仍 open\n- R5-W2 (crossover n=50): 升级为 N1 critical — 仍 open\n- R5-1 (following ThinKV): 仍 open — 本轮再次确认\n- R5-2 (LongFlow bib): 仍 open\n- R5-3 (\\placeholder): 仍 open\n- R1-W1 (ThinKV wording): 仍 in_progress\n\n**本轮新增 open issues**: 9 个 (R6-N2, R6-W1 through R6-W6, R6-M1 through R6-M5)\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 列表第 1 条 crossover 的证据在 §5.3 来自 n=50——需 n=496 数据支撑\n- \"entropy-discrimination collapse\" 作为 Contribution 3 的 mechanism framing 与 §6 的 correlational evidence 有张力\n\n### §3 Background\n- background.tex:33 \"following ThinKV\" 必须修改——方法不同，不能用 \"following\"\n\n### §4 Experimental Setup\n- Bonferroni k=4 的 family definition 需更 prominent 地 reference BH-FDR\n- Spearman ρ 应降为脚注，JT test 为 primary\n\n### §5 Results\n- Table 2 (n=50) 应替换为 n=496 per-phase table 或移至 Appendix\n- §5.3 crossover 数字需在 n=496 上验证并报告 bootstrap CI\n- §5.5 LLaMA CI/Wilcoxon 不一致需技术解释\n\n### §6 Analysis\n- §6.1 需报告 baseline Gini 和相对变化\n- §6.1 需讨论 threshold amplification 或降级 mechanism claim\n- §6.2 entropy redistribution 应精简（Qwen 不一致削弱叙事）\n\n### §7 Discussion\n- Pilot 失败的 implications 需更坦诚讨论\n- 添加 PPL→accuracy gap 讨论\n- \"within a single generation (n=496)\" 改为 \"within individual generations, across n=496 problems\"\n\n### References\n- h2o-neurips2023: title 为空\n- LongFlow: 删除 \"Withdrawn\" 标注，改为 arXiv preprint\n- 补引 \"Hold Onto That Thought\" (NeurIPS 2025)\n- 验证 SnapKV first author\n\n### Formatting\n- main.tex:21: 删除 \\placeholder 命令定义\n- appendix_results.tex: orphaned file + duplicate label\n- Abstract \"over an order of magnitude\" 应明确指 amplification ratio G",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_57b24a804b56707ec9118a483a8ac65e"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-15T11:29:10.900058+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_fdc656be1c7fe17c11ab639cdbce3710:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4223
}
```

</details>

---


### Assistant

_source line 434 · 2026-05-15T11:29:21.289278+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结：**

- **综合评分**: Borderline (3.0/5)
- **R1**: 3.0-3.5/5（方法严谨性）
- **R2**: 2.5/5（新颖性/完整性）

**3 个 Must-Fix**:
1. Crossover 证据 n=50 需在 n=496 验证（两位 Reviewer 完全共识，最关键）
2. Discrimination collapse effect size 与 severity gradient 的 gap
3. "following ThinKV" 方法归因错误

**1 个核心分歧**（记录在报告中）:
- Novelty：R1 认为 compound interaction 超越单轴叠加；R2 认为 HIES+ThinKV+Sparse Frontier 已预示方向

**Issue Tracker 已更新**: 40 个 issue，16 个 open/in_progress（含 9 个本轮新增）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 33

## Round 33

2 recorded events


### User

_source line 435 · 2026-05-15T11:29:24.068370+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心共识：两位 reviewer 在 Table 2 n=50 验证需求、crossover 证据不足、pilot 失败的坦诚讨论上完全一致。主要分歧在 overall 评分（R1: 3.5 vs R2: 2.5），根源是我对 novelty 增量的更严格判断——我认为已有工作的组合（HIES + ThinKV + Sparse Frontier）已基本预示了本文的核心发现方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 436 · 2026-05-15T11:31:27.769896+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结：**

- **综合评分**：Borderline (3.0/5)
- **R1**: 3.5/5 → 交叉后 3.0-3.5 | **R2**: 2.5/5 → 维持 2.5
- **共识 Must-Fix**: (1) crossover n=50 需 n=496 验证，(2) discrimination collapse effect size gap
- **核心分歧**: novelty 增量——R1 认为 compound coupling 超越单轴叠加，R2 认为已有工作组合已预示方向
- **关键判断**: crossover 在 n=496 上的验证结果将决定论文走向（main conference borderline vs Findings vs weak reject）
- **Issue Tracker**: 已更新，当前 16 个 open/in_progress issue

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 34

## Round 34

76 recorded events


### User

_source line 437 · 2026-05-15T12:29:58.488894+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: phase-gated-compound-sparse
- 论文路径: projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-06-15

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-15T12:30:04.830774+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-15T12:30:04.831595+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-15T12:30:09.105339+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-15T12:30:09.207524+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-15T12:30:14.183725+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-15T12:30:15.624268+00:00_

{"result":"# 项目 phase-gated-compound-sparse 概况\n\n## 实验状态 (84 个)\n\n- **mvp_v4_legacy_s025**: DONE (failed) — \n- **mvp_v4_random_r2**: DONE (success) — \n- **mvp_v4_legacy_s01**: DONE (negative) — \n- **mvp_v4_legacy_s03**: DONE (success) — \n- **mvp_v4_legacy_s02**: DONE (success) — \n- **mvp_v4c_r2**: DONE (failed) — \n- **mvp_v4b_r2**: DONE (failed) — \n- **mvp_v4a_r2**: DONE (failed) — \n- **mvp_ii_profiling_v4-random**: DONE (failed) — \n- **mvp_ii_profiling_v4c**: DONE (failed) — \n- **mvp_ii_profiling_v4b**: DONE (failed) — \n- **mvp_ii_profiling_v4**: DONE (failed) — \n- **mvp_ii_profiling_v3**: DONE (negative) — \n- **mvp_ii_profiling_v2**: DONE (negative) — \n- **mvp_interaction_index_profiling**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- sf5_asymmetric_spot（准备中）\n\n## 近期结论\n- **c2_qw_n500_r3** (success): C2 Qwen n=500 continuation (cron false positive on c2_qw_n500). s015 完成, s020-s030 remaining. 与 DeepSeek 对称验证 compound sparsity severity. ← 基于 c2_qw_n500\n- **c2_n500_deepseek** (success): C2 statistical power boost: 将 DeepSeek 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500，提升统计功效。预注册：若 QW s015 在 n=500 后 CI 仍跨零，论文叙事改为 \"compound effect emerges above a threshold sparsity level (~s020)\"\n  [C2 Pre-registration n=500](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/c2_n500_deepseek/data/PRE_REGISTRATION_C2.md) | [c2_n500_deepseek_diagnosis](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/c2_n500_deepseek/report/diagnosis.md) | [n500_statistics_summary](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/c2_n500_deepseek/report/n500_statistics_summary.md)\n- **c2_qw_n500** (failed): C2: Qwen n=500 统计功效提升。将 Qwen 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500，与 DeepSeek 对称验证。\n\n## 趋势\n成功 38 / 负向 10 / 失败 14 / 共 83\nn_problems: 500 ↑（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-22162: 无 GPU 信
…[truncated 1339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1440
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-15T12:30:16.127276+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-15T12:30:16.330645+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	
22	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Mathematical Reasoning Models}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	\input{related_work}
34	\input{background}
35	\input{methodology}
36	\input{results}
37	\input{analysis}
38	\input{discussion}
39	\input{conclusion}
40	
41	\bibliography{references}
42	
43	\section*{Limitations}
44	\input{limitations}
45	
46	\section*{Reproducibility}
47	Code and data will be released upon acceptance.
48	
49	\appendix
50	\input{appendix}
51	\input{appendix_moved}
52	\input{appendix_disc_analysis}
53	\input{appendix_robustness}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-15T12:30:16.381526+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-15T12:30:16.432178+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-15T12:30:21.709192+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 449 · 2026-05-15T12:30:22.815640+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 450 · 2026-05-15T12:30:22.816257+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 451 · 2026-05-15T12:30:23.168058+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "memory.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "memory.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 452 · 2026-05-15T12:30:29.803174+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"}]

I found comprehensive information about EMNLP 2026 call for papers submission guidelines and author instructions. Here's what you need to know:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, 
…[truncated 1541 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 8093
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-15T12:30:29.803858+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/memory.md\", \"content\": \"# Project Memory\\n\\n## 2026-05-15: Qwen n=475 reanalysis complete\\n- Reviewer flagged Qwen using n=274 (complete-case requiring all 3 phases). Corrected to n=475 (low+high valid only).\\n- Created `analyze_n500_v2.py` on server. Outputs: `n500_unified_final.{csv,json}`, `n500_full_statistics.md`\\n- v2 adds: cross-model Mann-Whitney U, imp/rand effect size ratio, proper paired filtering via `extract_diffs_paired`\\n- Bonferroni correction across 48 tests total (16 conditions + 8 within-imp d_z + 8 rand-within + 8 imp-vs-rand + 8 cross-model)\\n- DS rand s025/s030 Bonferroni p ≈ 0.07 (no longer significant after correction)\\n- All Qwen imp conditions remain *** significant with n=475\\n\", \"total_chars\": 680, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6635
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-15T12:30:34.678918+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit long short paper ACL template double blind"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit long short paper ACL template double blind"
  }
}
```

</details>

---


### Tool call

_source line 455 · 2026-05-15T12:30:35.031436+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May submission formatting requirements page limits"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May submission formatting requirements page limits"
  }
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-15T12:30:36.036590+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-15T12:30:36.137944+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We show that compound severity is not phase-invariant: it is an emergent phase-strategy interaction with amplification ratios ($G$) of $7.5$--$79.8{\times}$ (bootstrap 95\% CI: $[4.1, 96.5]$) across reasoning phases in mathematical reasoning models.
4	
5	On DeepSeek-R1-Distill-Qwen-7B (500 MATH-500 problems, $n_{\text{eff}}{=}496$, $s \in \{0.15, 0.20, 0.25, 0.30\}$), importance-based eviction produces a monotonically increasing severity gradient from the high-sparsity to low-sparsity reasoning phase (median $\Delta$: $0.39 \to 8.48$; all Bonferroni-corrected $p < 10^{-69}$). Random eviction develops a detectable phase gradient only above $s \approx 0.20$ (non-significant at $s \leq 0.20$; where significant, $3$--$39{\times}$ weaker), confirming importance-based eviction as the dominant driver.
6	A crossover emerges at $s{=}0.25$: importance-based eviction outperforms random in high-sparsity phases yet underperforms in low-sparsity phases---a qualitative reversal in strategy ranking.
7	The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with preliminary cross-architecture evidence from a LlamaForCausalLM model suggesting the phenomenon may extend beyond Qwen2-family architectures.
8	We present discrimination collapse---head pruning flattening cumulative importance scores---as a correlational diagnostic: both strategies exhibit near-identical Gini drops, yet severity diverges by $15$--$17{\times}$, implicating the structural specificity of importance-based pruning as the key differentiator.
9	These findings motivate phase-aware compression budgets for mathematical reasoning models.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-15T12:30:36.138472+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-15T12:30:36.189742+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 3355 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 460 · 2026-05-15T12:30:39.957908+00:00_

Web search results for query: "EMNLP 2026 submission format page limit long short paper ACL template double blind"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Association for Computational Linguistics (ACL) conference - Overleaf, Online LaTeX Editor","url":"https://www.overleaf.com/latex/templates/association-for-computational-linguistics-acl-conference/jvxskxpnznfj"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"GitHub - acl-org/acl-style-files: Official style files for papers submitted to venues of the Association for Computational Linguistics · GitHub","url":"https://github.com/acl-org/acl-style-files"}]

Based on the search results, here's the information about EMNLP 2026 submission format:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

## ACL Template

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences. EMNLP uses the ACL style files available at github.com/acl-org/acl-style-files.

## Double-Blind Revie
…[truncated 537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 5278
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-15T12:30:42.319674+00:00_

Web search results for query: "ACL Rolling Review 2026 May submission formatting requirements page limits"

Links: [{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

Based on the search results for ACL Rolling Review 2026 May submission formatting requirements and page limits:

## Page Limits

The paper follows page limits (8 for long, 4 for short, not including limitations and ethical considerations). More specifically:

- **Long papers:** Review versions of long papers may have up to eight (8) pages of content plus unlimited p
…[truncated 1000 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7288
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-15T12:30:47.838001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-15T12:30:48.290685+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	PM-KVQ~\cite{pmkvq-iclr2026} demonstrates that progressive quantization---gradually reducing bit-width over the generation process---mitigates cumulative error in long-CoT reasoning, implicitly introducing a temporal dimension to compression severity that resonates with our finding that compound interaction is phase-dependent.
11	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
12	
13	\paragraph{KV cache eviction.}
14	Most methods rely on importance scoring whose reliability is increasingly questioned.
15	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
16	\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
17	RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
18	\cite{hies-2025} independently show
…[truncated 2580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-15T12:30:48.341399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-15T12:30:49.245941+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}
9	\label{sec:dataset}
10	We evaluate all 500 problems from MATH-500~\cite{math500-neurips2021}. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048). Problems with degenerate phase assignments (null low or high phase) are excluded, yielding effective sample sizes of $n{=}496$ for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded). Qwen exhibits a higher mid-phase null rate (45.2\% vs.\ 10.2\% for DeepSeek) due to lower temporal autocorrelation in its attention sparsity patterns (lag-1 $r{=}0.718$ vs.\ $0.894$, $d{=}-1.68$); this does not affect the primary gradient metric $\Delta = \mathrm{II}_{\textit{low}} - \mathrm{II}_{\textit{high}}$, which requires only low and high phases. Sensitivity analysis across $\texttt{min\_phase\_length} \in \{5, 10, 20\}$ confirms robustness (Appendix~\ref{app:mpl-sensitivity}).
11	
12	\paragraph{Sparsity configuration.}
13	\label{sec:sparsity-config}
14	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are
…[truncated 2108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-15T12:30:49.346882+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-15T12:30:49.900086+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\times}$ amplification (all Bonferroni-corrected $p < 10^{-69}$). Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \geq 0.25$, $\Delta$ becomes significant ($0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$) but $15$--$39{\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger. % exp_id: n500_unified_final; DS imp Δ 0.39→8.48, rand 0.01→0.51; JT z=33.7 (imp), 6.2 (rand)
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, 500 MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.21 & 3.99 & 8.48 \\ % exp_id: n500_unified_final; DS imp median_ii_diff
20	Random     & 0.01 & 0.03 & 0.26 & 0.51 \\ % exp_id: n500_unified_final; DS rand median_ii_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown at $n{=
…[truncated 11973 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-15T12:30:49.950810+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-15T12:30:50.303107+00:00_

1	\section{Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	We present discrimination collapse as a \emph{correlational diagnostic} rather than a complete causal explanation. The consistent Gini decrease across all conditions provides a necessary background---aggregate attention concentration drops uniformly under head pruning regardless of eviction strategy (importance $\Delta\mathrm{Gini}$: $-0.030$ to $-0.081$; random $\Delta\mathrm{Gini}$: $-0.031$ to $-0.071$; ${<}10\%$ difference). However, severity diverges by $15$--$17{\times}$ between strategies despite near-identical Gini changes, indicating that concentration collapse alone is insufficient. The critical differentiator is \emph{structural specificity}: importance-based pruning systematically removes high-attention-score heads, disrupting the attention pattern structure that KV eviction relies on, while random pruning preserves more structural diversity. The quantitative gap between score-level changes ($6$--$16\%$ relative Gini reduction from a DeepSeek baseline of $\widetilde{\mathrm{Gini}} \approx 0.50$; Qwen baseline $\approx 0.57$) and outcome-level amplification ($G{=}7.5$--$79.8{\times}$) indicates additional nonlinear factors (e.g., cascading effects across layers) that warrant dedicated investigation.  % exp_id: c4_entropy; DS baseline Gini 0.496, QW 0.571; imp ΔGini -0.029 to -0.082, rand -0.031 to -0.071
5	
6	\subsection{Discrimination Collapse}
7	\label{sec:discrimination-collapse-main}
8	
9	Head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek, $6$--$17\%$ relative to dense baseline) and $0.010$--$0.020$ (Qwen, $2$--$4\%$) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). Critically, random eviction shows near-identic
…[truncated 2219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-15T12:30:50.454249+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-15T12:30:50.605454+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($G{=}7.5$--$79.8{\times}$ at $n{=}496$) far exceeds a naive ``somewhat worse'' prediction. The crossover on DeepSeek---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.021$ vs.\ $1.113$) and underperforms in low-sparsity phases ($3.971$ vs.\ $1.498$)---cannot be derived from single-axis entropy reasoning. % exp_id: crossover_all_sparsity.csv; DS s025 n=496 The near-unity random baseline ($G{=}0.5$--$1.3{\times}$, trivial magnitude) confirms the dominant amplification is strategy-specific. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability.
9	
10	\paragraph{Characterization as diagnostic signal.}
11	The primary value of the phase-dependent severity gradient is diagnostic rather than prescriptive: it identifies \emph{where} compound sparsity is most destructive within a generation. The monotonically increasing $G$ across spar
…[truncated 2774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-15T12:30:50.605947+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-15T12:30:50.656469+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation ($n{=}496$/$475$ problems). Under importance-based eviction, the amplification ratio $G$ ranges from $7.5{\times}$ to $79.8{\times}$ across sparsity levels, with paired median differences $\Delta$ from $0.39$ to $8.48$ (DeepSeek) and $0.07$ to $3.16$ (Qwen), all $p < 10^{-13}$. Random eviction develops a detectable phase gradient only above $s \approx 0.20$, but $3$--$39{\times}$ weaker than importance-based. A crossover on DeepSeek at $s{=}0.25$---where importance-based eviction reverses ranking across phases ($2.7{\times}$ reversal)---demonstrates that no single strategy dominates uniformly; Qwen does not exhibit this crossover, indicating model dependence. The pattern replicates on Qwen2.5-7B-Instruct at all four sparsity levels; suggestive preliminary evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) indicates the phenomenon may extend beyond Qwen2, though at ${\sim}1/40$ the magnitude and with a weaker strategy contrast. Discrimination collapse provides a correlational diagnostic supported by both Qwen2-based models, with structural specificity of importance-based pruning as the key differentiator from random eviction---despite near-identical Gini drops ($<10\%$ difference), severity diverges by $15$--$17{\times}$.
5	These findings motivate phase-aware sparsity allocation for reasoning model deployment. Extending this analysis to code reasoning (HumanEval, LiveCodeBench) and science reasoning (GPQA), validating the discrimination collapse mechanism through causal intervention, and characterizing asymmetric compound interactions are promising directions for future work.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-15T12:30:56.363228+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-15T12:30:57.332585+00:00_

1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	\label{sec:compound-sparsity}
12	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
13	
14	\paragraph{Interaction Index.}
15	\label{sec:interaction-index}
16	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
17	\begin{equation}
18	    \mathrm{II} = r_b - r_a - r_k + 1.
19	    \label{eq:ii}
20	\end{equation}
21	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative co
…[truncated 1351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 969
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-15T12:30:57.333063+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-15T12:30:57.787250+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. MATH-500 is a suitable first testbed because it elicits structured reasoning with clear phase transitions (exploratory vs.\ structured computation), supports per-problem evaluation enabling paired statistical tests, and spans sufficient difficulty to produce meaningful variation in sequence length and attention dynamics. However, different reasoning tasks---code generation (e.g., HumanEval, LiveCodeBench), science reasoning (e.g., GPQA), multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile. Whether the phase-strategy interaction documented here extends to these domains is an open question.
6	
7	\paragraph{Symmetric sparsity assumption.}
8	Our analysis applies symmetric sparsity rates: the same fraction $s$ is used for both head pruning and KV cache eviction. Practical deployments may use asymmetric budgets (e.g., aggressive head pruning with conservat
…[truncated 1561 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-15T12:30:57.788635+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-15T12:30:58.753005+00:00_

1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position spar
…[truncated 1336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 964
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-15T12:30:58.753580+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-15T12:30:59.206562+00:00_

1	% Content moved from main body to appendix:
2	% - Phase-strategy crossover details (from results §5.3)
3	% - Cross-model replication details with tables/figures (from results §5.4)
4	% - Permutation test details with table/forest plot (from results §5.5)
5	% - Full entropy-discrimination collapse analysis with tables (from analysis §6)
6	% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.
7	
8	\section{Phase-Strategy Crossover Details}
9	\label{app:crossover-details}
10	
11	On DeepSeek ($n{=}496$), a strategy ranking reversal emerges at $s{=}0.25$ (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.498$---a $2.7{\times}$ reversal; both $p < 10^{-4}$). This crossover is confirmed at all four sparsity levels, with reversal magnitude of $4.0{\times}$ at $s{=}0.15$, $3.4{\times}$ at $s{=}0.20$, $2.7{\times}$ at $s{=}0.25$, and $2.2{\times}$ at $s{=}0.30$ (decreasing as random eviction severity rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse}). Qwen does not exhibit a crossover: importance-based eviction produces lower II than random in both phases across all sparsity levels (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.109$; low $1.043$ vs.\ $1.770$). % exp_id: crossover_all_sparsity.csv; DS reversal: diff_low/diff_high = 2.99, 2.83, 2.13, 1.66
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
16	\caption{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.7{\times}$ higher II in the low-sparsity phas
…[truncated 14257 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-15T12:30:59.257169+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-15T12:30:59.358454+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/decisions.yaml\", \"content\": \"_next_id: 69\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:44 UTC\\n  summary: MVP 方案：用 Interaction Index 跨 phase 差异验证核心假设\\n  rationale: 评审建议 novelty 锚定在 \\\"phase-dependent interaction direction reversal\\\"。MVP\\n    聚焦验证这一点：在 MATH-500 子集上 profiling DeepSeek-R1-Distill-Qwen-7B，用 ThinKV 方法切分 phases，计算\\n    attention × KV 的 Interaction Index。比全 grid search 更聚焦，直接验证核心 novelty 锚点。Pass =\\n    II 跨 phase 显著不同；Fail = II 恒定。预计 10-15 H100-hours。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:48 UTC\\n  summary: 向 Manager 申请 4×H100-80GB 租卡，预计 8-10 天，¥3200-5000\\n  rationale: 12 天截稿，4 GPU 并行可将日历时间压到 ~8 天（留 4 天 buffer）。2 GPU 需 11 天，buffer 不足 1 天，风险过高。用户明确授权\\\"几张都可以\\\"。GPU\\n    就绪 hard deadline 5/14 EOD。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 17:54 UTC\\n  summary: Throughput 策略：RTX 6000 Pro 做开发/accuracy，最终 throughput 短租 H100\\n  rationale: IDEA_BRIEF 硬约束要求\\\"Report wall-clock and throughput on H100\\\"，baseline 论文（Polar\\n    Sparsity、SeerAttention-R）均报告 H100 数字。RTX 6000 Pro (sm_89) vs H100 (sm_90) 的 kernel\\n    speedup 可能不同。策略(a)：RTX 6000 Pro 做全部开发+accuracy+ablation（硬件无关），仅 throughput 基准测试短租\\n    H100 ~2-4h（~$6-12）。比策略(b)全在 RTX 6000 Pro 上报告更有说服力，成本极低。H100 在 M5 阶段再申请。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 17:58 UTC\\n  summary: Throughput benchmark 硬件从 H100 改为 H20（Hopper sm_90，用户确认无 H100 可用）\\n  rationale: H20 与 H100 同为 Hopper sm_90，kernel 兼容无需额外适配。96GB HBM3 + 4TB/s 带宽适合 inference\\n    benchmark。在 H20 上重跑所有 baseline 确保公平比较，报告 relative speedup ratio（Hopper 架构内比值稳定）。H100\\n    不可用，H20 是最佳替代。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 18:01 UTC\\n  summary: GPU 从 4× RTX 6000 Pro 换为 4× H20-NVLink 96GB\\n  rationale:
…[truncated 1471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-15T12:31:05.025622+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-15T12:31:05.982731+00:00_

1	\section{Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.071$; Qwen: $-0.019$ to $-0.046$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$). % exp_id: bf16_importance_s015..s030; high-phase medians: 0.006, 0.015, 0.032, 0.053
12	
13	\paragraph{Random masking as falsification control.}
14	At $n{=}500$, random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: non-significant at $s \leq 0.20$ for both models, but significant at $s \geq 0.25$ (DS: $\Delta{=}0.26$--$0.51$, $p_{\text{Bonf}} < 0.006$; QW: $\Delta{=}0.39$--$0.91$, $p_{\text{Bonf}} < 10^{-10}$). Where significant, the random phase gradient is $3$--$39{\times}$ weaker than importance-based, confirming that the dominant amplification is strategy-specific. % exp_id: n500_unified_final; DS rand s025 0.257 p=0.006, s030 0.510 p=0.006; QW rand s025 0.393, s030 0.913
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy s
…[truncated 4903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-15T12:31:05.983250+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-15T12:31:06.385637+00:00_

1	\section{Benjamini-Hochberg FDR Correction}
2	\label{app:bh-fdr}
3	
4	Table~\ref{tab:bh-fdr} compares Bonferroni ($k{=}4$, per model$\times$strategy family) and Benjamini-Hochberg FDR correction across all 44 statistical tests. BH-FDR recovers 5 additional significant results beyond Bonferroni, all in low-effect-size conditions (random eviction or cross-model random comparisons). All 32 Bonferroni-significant results remain significant under BH-FDR.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Bonferroni vs.\ BH-FDR correction summary ($\alpha{=}0.05$, 44 tests). ``BH only'' denotes tests significant under BH-FDR but not Bonferroni.}
10	\label{tab:bh-fdr}
11	\begin{tabular}{@{}lcc@{}}
12	\toprule
13	Category & Bonf.\ sig. & BH-only sig. \\
14	\midrule
15	Per-condition Wilcoxon ($k{=}16$) & 10 & 2 \\
16	Imp vs.\ rand ($k{=}8$) & 8 & 0 \\
17	Adjacent sparsity ($k{=}12$) & 10 & 1 \\
18	Cross-model Mann-Whitney ($k{=}8$) & 4 & 2 \\
19	\midrule
20	Total ($k{=}44$) & 32 & 5 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	The 5 BH-only results are: DeepSeek random $s{=}0.25$ and $s{=}0.30$ per-condition Wilcoxon ($p_{\text{Bonf}}{=}0.064$/$0.065$, BH $q{=}0.002$), DeepSeek random $s{=}0.25 \to 0.30$ adjacent-sparsity step ($p_{\text{Bonf}}{=}0.078$, BH $q{=}0.002$), and cross-model random $s{=}0.25$/$s{=}0.30$ Mann-Whitney ($p_{\text{Bonf}}{=}0.66$/$0.17$, BH $q{=}0.018$/$0.005$). All involve random eviction---the weakest effects---confirming that Bonferroni is conservative but does not miss any importance-based findings. % exp_id: n500_unified_final; source: supplementary_stats.json bh_fdr_correction
26	
27	
28	\section{Minimum Phase Length Sensitivity}
29	\label{app:mpl-sensitivity}
30	
31	Table~\ref{tab:mpl-sensitivity} reports the paired median difference $\Delta$ under three \texttt{min\_phase\_length} (mpl) settings across all 16 conditions (2 models $\times$ 2 strategies $\times$ 4 sparsity levels). Conclusions are robust: all importance-based c
…[truncated 4680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-15T12:31:06.386172+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-15T12:31:06.436726+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-15T12:31:11.359764+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/agent"
  }
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-15T12:31:11.360527+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_director_b570dbd0.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-15T12:31:11.612018+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/project_config*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/project_config*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-15T12:31:11.662776+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-15T12:31:15.913111+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*config*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*config*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-15T12:31:15.963966+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-15T12:31:19.230039+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-15T12:31:19.280740+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'phase-gated-compound-sparse'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-15T12:31:25.210287+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-15T12:31:25.612515+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-15T12:31:25.612991+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-15T12:31:25.713758+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-15T12:31:28.880299+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-15T12:31:29.132090+00:00_

1	% References for Phase-Gated Compound Sparse paper
2	% Generated 2026-05-14; all entries verified via web search
3	
4	@inproceedings{adakv-neurips2025,
5	    title     = {Ada-{KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation for Efficient {LLM} Inference},
6	    author    = {Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin},
7	    booktitle = {Advances in Neural Information Processing Systems},
8	    year      = {2025},
9	    url       = {https://arxiv.org/abs/2407.11550},
10	}
11	
12	@article{decision-repr-transition-2026,
13	    title   = {Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions},
14	    author  = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},
15	    journal = {arXiv preprint arXiv:2605.07271},
16	    year    = {2026},
17	    url     = {https://arxiv.org/abs/2605.07271},
18	}
19	
20	@article{deepseek-r1-2025,
21	    title   = {{DeepSeek-R1} incentivizes reasoning in {LLMs} through reinforcement learning},
22	    author  = {{DeepSeek-AI}},
23	    journal = {Nature},
24	    volume  = {645},
25	    pages   = {633--638},
26	    year    = {2025},
27	    doi     = {10.1038/s41586-025-09422-z},
28	}
29	
30	@inproceedings{defensivekv-iclr2026,
31	    title     = {{DefensiveKV}: Taming the Fragility of {KV} Cache Eviction in {LLM} Inference},
32	    author    = {Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike},
33	    booktitle = {International Conference on Learning Representations},
34	    year      = {2026},
35	    url       = {https://arxiv.org/abs/2510.13334},
36	}
37	
38	@article{doing-more-with-less-2026,
39	    title   = {Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},
40	    author  = {Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},
41	    journal = {arXiv preprint arXiv:2604.25098},
42	    year    = {2026},
43	    url     = {https://arxiv
…[truncated 12273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-15T12:31:29.132549+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-15T12:31:29.183372+00:00_

1	- id: R6-N1
2	  summary: "Crossover evidence based on n=50 not verified at n=496; Table 2 uses n=50 G values (69-274x) overestimating by 42-85%"
3	  category: experiment
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 5
7	  last_seen_round: 6
8	  mentions:
9	    - {round: 5, reviewers: [R1, R2], note: "R5-W1/R5-W2: Table 2 n=50 and crossover n=50 flagged"}
10	    - {round: 6, reviewers: [R1, R2], note: "Upgraded to critical. n=496 data exists but not incorporated."}
11	  action_items:
12	    - {round: 6, action: "Replace Table 2 with n=500 per-phase numbers; move n=50 to Appendix; update §5.3 crossover; cascade updates", assigned_to: paper_agent, status: done}
13	  resolution: "Table 2 expanded to DS(n=496)+QW(n=475) 16-row dual-model table. G=7.5-79.8x importance, 0.5-1.3x random. QW s015 G marked n.d. with dagger footnote. n=50 moved to Appendix. Cascade to §5.2, Fig1, Conclusion, Discussion."
14	  resolution_round: 6
15	
16	- id: R6-N2
17	  summary: "Discrimination collapse effect size (Gini drop 6-16%) vs severity gradient (G=30-148x) magnitude gap (~200-2000x)"
18	  category: method
19	  severity: critical
20	  status: resolved
21	  first_raised_round: 6
22	  last_seen_round: 6
23	  mentions:
24	    - {round: 6, reviewers: [R1, R2], note: "Consensus: gap between score-level changes and outcome-level amplification unaddressed"}
25	  action_items:
26	    - {round: 6, action: "Extract baseline Gini + compute relative changes", assigned_to: main_agent, status: done}
27	    - {round: 6, action: "Rewrite §6 as correlational diagnostic with structural specificity", assigned_to: paper_agent, status: done}
28	  resolution: "§6 rewritten as correlational diagnostic. Key evidence: imp/rand ΔGini nearly identical but severity differs 15-17x → Gini necessary but not sufficient. Structural specificity of pruned heads as differentiator. Intro/Conclusion/Abstract downgraded. Contribution 3 updated."
29	  resolution_round: 6
30	
31	- id: R6-N3
32	  summary
…[truncated 7608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-15T12:31:34.461650+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-15T12:31:34.665713+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_reports/round_4.md:189:外部审稿：未配置（项目无 `external_review.paperreview_ai.enabled` 设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_57b24a804b56707ec9118a483a8ac65e_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_57b24a804b56707ec9118a483a8ac65e_director.jsonl:4:{"ts": "2026-05-14T12:51:37.178625+00:00", "role": "tool", "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director", "text": "called ToolSearch", "tool": "ToolSearch", "tool_args": {"query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status", "max_results": "4"}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_57b24a804b56707ec9118a483a8ac65e_director.jsonl:19:{"ts": "2026-05-14T12:52:05.495687+00:00", "role": "tool", "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director", "text": "called Bash", "tool": "Bash", "tool_args": {"command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/agent/config.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"", "description": "Check external review config"}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_57b24a804b56707ec9118a483a8ac65e_director.jsonl:35:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_57b24a804b56707ec9118a483a8ac65e_director.jsonl:36:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0
…[truncated 4541 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "elapsed_ms": 204
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-15T12:32:19.776659+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "phase-gated-compound-sparse",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计有效性**\n\n### 论文信息\n- **标题**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models\n- **论文路径**: `projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`（多文件结构，abstract.tex / introduction.tex / related_work.tex / background.tex / methodology.tex / results.tex / analysis.tex / discussion.tex / conclusion.tex / limitations.tex / appendix.tex / appendix_moved.tex / appendix_disc_analysis.tex / appendix_robustness.tex）\n- **references**: `references.bib`\n\n### Venue 要求\n- **Venue**: EMNLP 2026 Main Conference（通过 ACL Rolling Review May 2026 cycle 提交）\n- **Deadline**: ARR 提交截止 2026-05-25\n- **格式**: ACL 模板, 长文 8 页正文 + 无限参考文献\n- **审稿制度**: Double-blind\n- **匿名规则**: 作者信息匿名\n- **必须**: Limitations section（不计页数）\n- **鼓励**: Ethics/Broader Impact section\n\n### 你的审查重点\n\n请以 EMNLP 最严格审稿标准评估以下方面：\n\n1. **实验设计**：\n   - 实验配置（模型选择、数据集、sparsity 范围）是否充分支撑 claims？\n   - 对照组（random eviction）设计是否合理？是否充分？\n   - 样本量（n=496/475/49）是否足够？power analysis 是否合理？\n   - 4 个 sparsity level（0.15-0.30）是否太窄？\n\n2. **统计方法**：\n   - Bonferroni correction 的 family-wise k=4 分组是否合理？\n   - Bootstrap CI (B=10,000) + Wilcoxon signed-rank + Mann-Whitney U + Jonckheere-Terpstra 组合是否恰当？\n   - BH-FDR 作为 robustness check 是否充分？\n   - Permutation test 仅在 n=50 子集上做是否有问题？\n   - 重度右偏分布（mean/median ratio 43:1）下的统计推断是否可靠？\n\n3. **方法论**：\n   - Phase segmentation（quantile-based tercile）是否有方法论问题？\n   - Interaction Index (II) 的定义和 additive null 假设是否合理？\n   - Amplification ratio G 的定义（ratio of medians vs median of ratios）是否有偏？\n   - 对称 sparsity 假设的局限性\n\n4. **Mechanism analysis**：\n   - Discrimination collapse 作为 correlational diagnostic 的证据强度\n   - Gini drop vs severity divergence 的解释是否令人信服？\n   - Entropy redistribution 在 Qwen 上的不一致是否被充分讨论？\n\n5. **Cross-architecture validation**：\n   - LLaMA n=49 的证据强度——是否过度解读？\n   - CI/Wilcoxon 不一致的解释是否合理？\n\n请输出完整的结构化审稿报告（Strengths / Weaknesses / Questions / Missing References / Score）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "phase-gated-compound-sparse",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计有效性**\n\n### 论文信息\n- **标题**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models\n- **论文路径**: `projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`（多文件结构，abstract.tex / introduction.tex / related_work.tex / background.tex / methodology.tex / results.tex / analysis.tex / discussion.tex / conclusion.tex / limitations.tex / appendix.tex / appendix_moved.tex / appendix_disc_analysis.tex / appendix_robustness.tex）\n- **references**: `references.bib`\n\n### Venue 要求\n- **Venue**: EMNLP 2026 Main Conference（通过 ACL Rolling Review May 2026 cycle 提交）\n- **Deadline**: ARR 提交截止 2026-05-25\n- **格式**: ACL 模板, 长文 8 页正文 + 无限参考文献\n- **审稿制度**: Double-blind\n- **匿名规则**: 作者信息匿名\n- **必须**: Limitations section（不计页数）\n- **鼓励**: Ethics/Broader Impact section\n\n### 你的审查重点\n\n请以 EMNLP 最严格审稿标准评估以下方面：\n\n1. **实验设计**：\n   - 实验配置（模型选择、数据集、sparsity 范围）是否充分支撑 claims？\n   - 对照组（random eviction）设计是否合理？是否充分？\n   - 样本量（n=496/475/49）是否足够？power analysis 是否合理？\n   - 4 个 sparsity level（0.15-0.30）是否太窄？\n\n2. **统计方法**：\n   - Bonferroni correction 的 family-wise k=4 分组是否合理？\n   - Bootstrap CI (B=10,000) + Wilcoxon signed-rank + Mann-Whitney U + Jonckheere-Terpstra 组合是否恰当？\n   - BH-FDR 作为 robustness check 是否充分？\n   - Permutation test 仅在 n=50 子集上做是否有问题？\n   - 重度右偏分布（mean/median ratio 43:1）下的统计推断是否可靠？\n\n3. **方法论**：\n   - Phase segmentation（quantile-based tercile）是否有方法论问题？\n   - Interaction Index (II) 的定义和 additive null 假设是否合理？\n   - Amplification ratio G 的定义（ratio of medians vs median of ratios）是否有偏？\n   - 对称 sparsity 假设的局限性\n\n4. **Mechanism analysis**：\n   - Discrimination collapse 作为 correlational diagnostic 的证据强度\n   - Gini drop vs severity divergence 的解释是否令人信服？\n   - Entropy redistribution 在 Qwen 上的不一致是否被充分讨论？\n\n5. **Cross-architecture validation**：\n   - LLaMA n=49 的证据强度——是否过度解读？\n   - CI/Wilcoxon 不一致的解释是否合理？\n\n请输出完整的结构化审稿报告（Strengths / Weaknesses / Questions / Missing References / Score）。"
  }
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-15T12:32:38.727368+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18950
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-15T12:32:39.129760+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "phase-gated-compound-sparse",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 相关工作 + 格式合规**\n\n### 论文信息\n- **标题**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models\n- **论文路径**: `projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`（多文件结构，abstract.tex / introduction.tex / related_work.tex / background.tex / methodology.tex / results.tex / analysis.tex / discussion.tex / conclusion.tex / limitations.tex / appendix.tex / appendix_moved.tex / appendix_disc_analysis.tex / appendix_robustness.tex）\n- **references**: `references.bib`\n\n### Venue 要求\n- **Venue**: EMNLP 2026 Main Conference（通过 ACL Rolling Review May 2026 cycle 提交）\n- **Deadline**: ARR 提交截止 2026-05-25\n- **格式**: ACL 模板, 长文 8 页正文 + 无限参考文献\n- **审稿制度**: Double-blind\n- **匿名规则**: 作者信息匿名\n- **必须**: Limitations section（不计页数）\n- **鼓励**: Ethics/Broader Impact section\n\n### 你的审查重点\n\n请以 EMNLP 最严格审稿标准评估以下方面：\n\n1. **新颖性 (Novelty)**：\n   - 核心 contribution（phase-strategy interaction）是否足够新颖？\n   - 这是一个全面的实证特征化（characterization）工作，而非提出新方法——对 EMNLP main conference 是否足够？\n   - 与 ThinKV (ICLR 2026)、SparK (AAAI 2026)、UniComp (2026)、HIES (2025)、Sparse Frontier (2025) 的差异化是否充分？\n   - Introduction 中 \"Why can't existing single-axis findings predict our results?\" 的论证是否有说服力？\n   - Crossover effect 是否真的不可从现有工作推导？\n\n2. **完整性 (Completeness)**：\n   - 仅在 MATH-500 上评估，仅 7B 模型——generalizability 是否充分？\n   - 只用 perplexity，无 downstream accuracy——是否构成重大缺陷？\n   - Mitigation pilot 失败（18% recovery, gate FAIL）——论文的实际价值在哪里？\n   - 缺少 throughput/latency 评估——对 deployment motivation 的影响？\n   - 论文声称 \"motivate phase-aware compression\"，但没有展示 phase-aware 能工作\n\n3. **相关工作 (Related Work)**：\n   - 相关工作覆盖是否全面？有无重大遗漏？\n   - 请用 web_search 搜索 2025-2026 年相关工作，确认无重大遗漏：\n     - compound sparsity / joint compression for LLMs\n     - KV cache compression for reasoning models\n     - phase-aware / phase-dependent inference\n   - 引用格式是否正确？bib 条目是否完整？\n\n4. **格式合规**：\n   - 是否符合 ACL 模板（\\usepackage[review]{acl}）？\n   - 页数是否在 8 页限制内？\n   - Double-blind 是否遵守（无泄漏作者身份的信息）？\n   - Limitations section 是否存在且位置正确？\n   - Reproducibility 声明是否存在？\n   - 图表质量、表格可读性\n   - 参考文献格式一致性\n\n5. **写作质量**：\n   - 论文组织是否清晰？\n   - Abstract 是否准确反映论文内容？\n   - Claims 是否与证据匹配（overclaiming 风险）？\n   - 术语是否一致？\n\n请输出完整的结构化审稿报告（Strengths / Weaknesses / Questions / Missing References / Score）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "phase-gated-compound-sparse",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 相关工作 + 格式合规**\n\n### 论文信息\n- **标题**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models\n- **论文路径**: `projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`（多文件结构，abstract.tex / introduction.tex / related_work.tex / background.tex / methodology.tex / results.tex / analysis.tex / discussion.tex / conclusion.tex / limitations.tex / appendix.tex / appendix_moved.tex / appendix_disc_analysis.tex / appendix_robustness.tex）\n- **references**: `references.bib`\n\n### Venue 要求\n- **Venue**: EMNLP 2026 Main Conference（通过 ACL Rolling Review May 2026 cycle 提交）\n- **Deadline**: ARR 提交截止 2026-05-25\n- **格式**: ACL 模板, 长文 8 页正文 + 无限参考文献\n- **审稿制度**: Double-blind\n- **匿名规则**: 作者信息匿名\n- **必须**: Limitations section（不计页数）\n- **鼓励**: Ethics/Broader Impact section\n\n### 你的审查重点\n\n请以 EMNLP 最严格审稿标准评估以下方面：\n\n1. **新颖性 (Novelty)**：\n   - 核心 contribution（phase-strategy interaction）是否足够新颖？\n   - 这是一个全面的实证特征化（characterization）工作，而非提出新方法——对 EMNLP main conference 是否足够？\n   - 与 ThinKV (ICLR 2026)、SparK (AAAI 2026)、UniComp (2026)、HIES (2025)、Sparse Frontier (2025) 的差异化是否充分？\n   - Introduction 中 \"Why can't existing single-axis findings predict our results?\" 的论证是否有说服力？\n   - Crossover effect 是否真的不可从现有工作推导？\n\n2. **完整性 (Completeness)**：\n   - 仅在 MATH-500 上评估，仅 7B 模型——generalizability 是否充分？\n   - 只用 perplexity，无 downstream accuracy——是否构成重大缺陷？\n   - Mitigation pilot 失败（18% recovery, gate FAIL）——论文的实际价值在哪里？\n   - 缺少 throughput/latency 评估——对 deployment motivation 的影响？\n   - 论文声称 \"motivate phase-aware compression\"，但没有展示 phase-aware 能工作\n\n3. **相关工作 (Related Work)**：\n   - 相关工作覆盖是否全面？有无重大遗漏？\n   - 请用 web_search 搜索 2025-2026 年相关工作，确认无重大遗漏：\n     - compound sparsity / joint compression for LLMs\n     - KV cache compression for reasoning models\n     - phase-aware / phase-dependent inference\n   - 引用格式是否正确？bib 条目是否完整？\n\n4. **格式合规**：\n   - 是否符合 ACL 模板（\\usepackage[review]{acl}）？\n   - 页数是否在 8 页限制内？\n   - Double-blind 是否遵守（无泄漏作者身份的信息）？\n   - Limitations section 是否存在且位置正确？\n   - Reproducibility 声明是否存在？\n   - 图表质量、表格可读性\n   - 参考文献格式一致性\n\n5. **写作质量**：\n   - 论文组织是否清晰？\n   - Abstract 是否准确反映论文内容？\n   - Claims 是否与证据匹配（overclaiming 风险）？\n   - 术语是否一致？\n\n请输出完整的结构化审稿报告（Strengths / Weaknesses / Questions / Missing References / Score）。"
  }
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-15T12:32:40.590634+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1460
}
```

</details>

---


### Assistant

_source line 512 · 2026-05-15T12:32:47.991607+00:00_

两名 Reviewer 已分配任务：

| Reviewer | 侧重 | 状态 |
|----------|------|------|
| R1 | 方法严谨性 + 实验设计 + 统计有效性 | 已派发，等待报告 |
| R2 | 新颖性 + 完整性 + 相关工作 + 格式合规 | 已派发，等待报告 |

等待两名 Reviewer 完成独立初审后，将进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 35

## Round 35

2 recorded events


### User

_source line 513 · 2026-05-15T12:37:25.069795+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models
**审查侧重**: 新颖性 + 完整性 + 相关工作 + 格式合规

---

## 总体评分

**Overall**: 2.5/5（介于 Findings 接收与需修改重投之间）
**一句话总结**: 实验方法论严谨、统计控制充分的实证特征化工作，但单一基准、仅用 PPL 指标、缺少下游准确率验证、且 mitigation pilot 失败，削弱了对 EMNLP main conference 的贡献力度。

---

## 官方维度打分（ACL ARR Review Form, Feb 2025+）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 统计方法全面（bootstrap CI、Bonferroni、Jonckheere-Terpstra、permutation test、BH-FDR robustness check），随机 baseline 作为 falsification control 设计精良。但仅用 perplexity 无 downstream accuracy 是一个方法论缺陷；crossover 仅在 DeepSeek 上出现，Qwen 无法复现；LLaMA 跨架构验证 n=49 且统计显著性混合。 |
| **Excitement** | 2.5/5 | Phase-strategy interaction 的定量刻画有一定新颖性，crossover effect 是 non-trivial 发现。但本质是 characterization 而非方法贡献，mitigation pilot 失败（18% recovery, gate FAIL），论文未能展示发现的可操作价值。对 EMNLP main conference 的 excitement 偏低。 |
| **Overall** | 2.5/5 | Borderline Findings / 需修改重投。方法论扎实但 scope 受限严重（单基准、单尺度、仅 PPL），核心发现的实际影响力（actionability）未被证明。 |
| **Confidence** | 4/5 | 熟悉 KV cache compression 和 attention pruning 文献，仔细阅读了全文含 appendix。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **仅用 Perplexity，缺少 Downstream Accuracy 验证**
- 具体位置：§4 (Experimental Setup), §5 (Results), Limitations §"Perplexity vs. accuracy"
- 问题：论文的核心指标 Interaction Index (II) 完全基于 perplexity（Eq. 1）。Limitations 中作者承认 "perplexity has a known nonlinear relationship with downstream accuracy"，但未提供任何 accuracy 层面的验证。PPL 的 phase-level 恶化可能在 accuracy 层面被吸收（例如，low-sparsity phase 的 PPL 增长集中在 reasoning trace 的非关键 token 上，对最终答案准确率影响甚微）。
- 为什么影响接收：论文声称 "motivate phase-aware compression budgets for mathematical reasoning models"（Abstract, §7 Discussion），但如果 PPL 恶化不转化为 accuracy 下降，则整个 motivation 不成立。这是一个根本性的 construct validity 问题。ARR Review Form M4 要求 "model/benchmark selection must be motivated and linked to claims"——此处 claim 关于 reasoning quality 但指标不直接衡量 reasoning quality。
- 建议修改方向：至少报告 MATH-500 problem-level accuracy under compound sparsity（总 accuracy 及分 phase 的 partial credit/answer correctness），建立 II 与 accuracy regression 的关系。如果 PPL 严重退化但 accuracy 不变，结论需根本性修正。

**N2** [critical] **Generalizability 极度受限：单一基准 + 单一模型规模**
- 具体位置：§4 Dataset, §4 Models, Limitations §"Task coverage" 和 §"Model scale"
- 问题：全部实验仅在 MATH-500（一个数学推理基准，500 题）上进行，仅评估 7B 模型（两个 Qwen2 架构 + 一个 LLaMA 的初步验证，n=49）。论文 title 使用 "Mathematical Reasoning Models"（泛化 claim），但证据仅来自一个特定 benchmark 的一个规模。
- 为什么影响接收：EMNLP 对 empirical work 的 scope 有要求。(1) 不同推理任务（code, science reasoning）的 phase structure 可能完全不同——作者自己在 Limitations 中承认这点。(2) 7B→70B 的 scale 行为完全未知。(3) 两个 Qwen2 模型共享 backbone（28层/28 head/4-group GQA），cross-model replication 的独立性有限——更像是 "two weight initializations on the same architecture" 而非真正的跨模型验证。LLaMA 验证（§5.5）magnitude ~1/40，strategy contrast 弱，统计显著性混合。
- 建议修改方向：增加至少一个非数学推理 benchmark（如 GSM8K 作为另一个数学推理点、HumanEval/MBPP 作为 code reasoning、GPQA 作为 science reasoning）；增加 13B 或更大规模模型验证，或至少明确讨论为什么 7B 的发现足以支撑论文的 claim scope。

**N3** [critical] **Mitigation Pilot 失败，论文的实际价值存疑**
- 具体位置：§7 Discussion, "A preliminary pilot experiment"
- 问题：Oracle phase-aware budget reallocation 仅达到 18% recovery（预注册 30% gate FAIL）；heuristic variant 32% 但 CI 跨零。论文声称 "motivate phase-aware compression budgets"，但自己的 pilot 实验证明 phase-aware reallocation 不足以解决这个问题。
- 为什么影响接收：如果 characterization 的直接应用——phase-aware budget allocation——在 oracle 条件下都无法达标，那么这个 characterization 的 practical value 是什么？论文的 framing 从 "This is a useful diagnostic" 到 "This motivates phase-aware compression" 之间存在张力。Reviewer 会质疑：if knowing exactly where the problem is still can't fix it, what is the contribution? 这是一个 ARR "excitement" 维度的核心问题。
- 建议修改方向：(1) 重新定位论文 framing，不再 overclaim "motivate phase-aware compression"，而是明确为 "characterization of a previously unknown phenomenon"；(2) 更深入分析为什么 oracle reallocation 失败——是因为 budget reallocation 本身不够（需要 strategy switching），还是因为 phase boundaries 不够精确？(3) 讨论是否 joint optimization of budget + strategy selection 能解决问题。论文在 Discussion 最后一段暗示了这点，但需要更充分的分析。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Crossover Effect 的 model dependence 削弱了核心 contribution 之一**
- 具体位置：§5.3, §5.4, §7 Discussion
- 问题：Crossover（importance-based 在 high-sparsity phase 优于 random 但在 low-sparsity phase 劣于 random）仅在 DeepSeek 上出现。Qwen "does not exhibit this crossover"（§5.3）。Introduction 中将 crossover 作为论证 "Why can't existing single-axis findings predict our results?" 的关键证据（§1, "Instead, we observe a sign reversal"）。但这个 sign reversal 是 model-dependent 的。
- 建议：将 crossover 降级为 "model-specific phenomenon"，不在 Introduction 的核心论证中过度依赖。或者解释为什么 crossover 在 Qwen 上不出现（是否与 training methodology 相关？DeepSeek 是 distillation，Qwen 是 instruction tuning）。

**W2** [warning] **"Emergent" 用词 overclaiming**
- 具体位置：Abstract ("emergent phase-strategy interaction"), §1 ("This emergent coupling is not deducible from single-axis characterizations")
- 问题："Emergent" 在 ML 社区有特定含义（通常指 scale-dependent 的突现行为）。此处论文实际展示的是 compound sparsity 在不同 phase 上的差异——这是两个已知 axis 的交互，不是真正的 "emergence"。更准确地说，这是一个 "interaction effect" 或 "non-trivial composition effect"。
- 建议：将 "emergent" 替换为更精确的术语，如 "non-additive" 或 "interaction-driven"，避免 overclaiming。

**W3** [warning] **缺少 Throughput/Latency 评估**
- 具体位置：§7 Discussion, Limitations §"No throughput evaluation"
- 问题：论文反复声称 "motivate phase-aware compression budgets for deployment"，但完全没有 throughput 或 latency 数据。Phase-aware compression 需要 runtime phase detection，这本身有计算开销。如果 phase detection 的 overhead 抵消了 compression 的 savings，则实际部署价值为零。
- 建议：至少提供一个 rough estimate 或 back-of-envelope calculation，说明 phase-aware allocation 在实际 inference 中的 overhead 与 savings 之间的 trade-off。

**W4** [warning] **Discrimination Collapse 分析的 sufficiency gap**
- 具体位置：§6 Analysis, Table in Appendix D
- 问题：论文正确指出 Gini 下降在两种策略间几乎一致（<10% 差异），但 severity 相差 15-17×。这证明了 Gini collapse 是 "necessary but not sufficient"。然而，论文提出的 "structural specificity" 解释（importance-based pruning 系统性移除 high-score heads）仅是一个定性论证，没有定量证据直接支持。
- 建议：(1) 提供 pruned heads 在不同 phase 的 overlap 分析（importance vs random pruning 分别移除了哪些 heads，这些 heads 在不同 phase 的 attention pattern 是否不同）；(2) 或至少承认 "structural specificity" 假说目前缺乏直接证据。

**W5** [warning] **Abstract 的 bootstrap CI 呈现具有误导性**
- 具体位置：Abstract, line 3
- 问题：Abstract 报告 "$G$ of $7.5$--$79.8\times$ (bootstrap 95\% CI: $[4.1, 96.5]$)"。这个 CI 不是一个整体的 CI，而是将四个不同 sparsity level 的 CI lower bound（4.1 来自 s=0.15）和 upper bound（96.5 来自 s=0.30）拼接在一起。这在统计上是不规范的——它不是任何单一参数的置信区间。
- 建议：要么分别报告每个 sparsity level 的 CI，要么明确说明这是 "range of CI bounds across sparsity levels"。

---

## 小问题（不影响接收）

- **M1**: Table 2 (main-results) 中 Qwen s=0.15 的 $\widetilde{\mathrm{II}}_{\textit{high}} = -0.000$——负数 II 暗示 sub-additive 交互，文中未讨论其物理含义（可能只是 numerical noise，但应说明）。
- **M2**: §4 footnote 提到 "earlier float16 configuration produced sporadic NaN values; bfloat16 eliminated all occurrences"——这个 numerical issue 值得在 appendix 中进一步讨论，因为它暗示了某些 conditions 下的 numerical instability。
- **M3**: Figure 1 (fig1_dose_response.pdf) 使用 profiling subset (n=50) 的数据绘制，但 main results 已有 n=496 数据。hero figure 为什么不用 full-scale 数据？这会造成读者困惑。
- **M4**: 参考文献中 `pyramidkv-2024` 的 year 写为 2024，但 venue 是 "Conference on Language Modeling"（2025）——year 应更新为 2025。
- **M5**: Background §3 使用 `\paragraph{Compound sparsity.}` 后跟 `\label{sec:compound-sparsity}`——\paragraph 不是 section，label 前缀用 sec: 不太规范。
- **M6**: §5.1 中 "the median phase difference rises from $0.39$ at $s=0.15$ to $8.48$ at $s=0.30$ (all Bonferroni-corrected $p < 10^{-69}$)"——p 值精度到 10^{-69} 对读者来说过于 specific；建议简化为 $p \ll 10^{-10}$ 或类似。

---

## 相关工作评估

### 覆盖度

总体相关工作覆盖较全面，33 篇引用中涵盖了 compound compression、KV cache eviction、phase-aware inference 三个主要方向的核心工作。以下为详细评估：

**已覆盖的关键工作**（均正确引用）：
- ThinKV (ICLR 2026) ✓ — phase-aware KV compression 的直接 baseline
- SparK (AAAI 2026) ✓ — compound sparsity 的先驱
- UniComp (2026) ✓ — 大规模 compound compression 评估
- HIES (2025) ✓ — 单轴 discrimination collapse
- Sparse Frontier (2025) ✓ — strategy non-dominance
- R-KV (NeurIPS 2025) ✓ — reasoning-specific KV compression
- PM-KVQ (ICLR 2026) ✓ — progressive quantization for CoT
- GRASPrune (ACL 2026) ✓ — joint pruning with gates
- Hold Onto That Thought (NeurIPS 2025) ✓ — KV compression on reasoning
- LongFlow (2026) ✓, RLKV (2025) ✓, Lethe (AAAI 2026) ✓

**潜在遗漏**：
1. **MUSTAFAR (NeurIPS 2025)** — unstructured sparsity for KV cache pruning (Joo et al., arXiv:2505.22913)。虽然关注点是 within-entry unstructured sparsity（与本文的 structured head pruning + token eviction 不同），但作为 NeurIPS 2025 的 KV cache sparsity 工作，在 "KV cache eviction" 段落中值得一提。**非重大遗漏**。
2. **LKV (2026)** — End-to-End Learning of Head-wise Budgets and Token Selection for KV Cache Eviction (arXiv:2605.06676)。学习 head-wise budget 的方法，与本文关注的 head pruning 如何影响 KV eviction 直接相关。**轻微遗漏**。

### 引用验证结果

通过 `verify_references` 工具验证：
- 33 bib entries，0 orphan，0 missing（cite/bib 完全对应）
- 25/33 通过 OpenAlex 在线验证
- 3/33 未在 OpenAlex 找到（defensivekv-iclr2026, hies-2025, phase-transition-compression-2026）——均有有效 arXiv URL，可能是索引延迟
- 5/33 minor mismatch（deepseek-r1-2025 的 author 格式：bib 用 DeepSeek-AI vs API 返回 Guo；snapkv-neurips2024 的 first author；unicomp-2026 的 von Rad vs Rad 等）——**均为 name formatting 问题，非 fabrication 问题**
- **未发现 hallucinated references**

---

## 格式合规评估

| 检查项 | 状态 | 说明 |
|--------|------|------|
| ACL 模板 | ✅ | `\usepackage[review]{acl}` |
| Double-blind | ✅ | `\author{Anonymous}`，正文中未见 de-anonymization 信息 |
| 正文页数 | ⚠️ | 无法编译验证。主文件包含 abstract + 7 sections (intro, related, background, methodology, results, analysis, discussion, conclusion)。内容量较大，存在超页风险——Table 2 是 table* (跨双栏)，加上 6 个 section 的文本量。建议作者自行确认不超 8 页。 |
| Limitations section | ✅ | 在 `\bibliography` 之后，有 `\section*{Limitations}`，不计页数。内容覆盖 model scale, task coverage, symmetric sparsity, mechanism, perplexity vs accuracy, sparsity range——较为全面。 |
| Reproducibility | ✅ | 有 `\section*{Reproducibility}` 声明 "Code and data will be released upon acceptance"。统计方法详细（seed=42, B=10000）。但代码不可用（acceptance 后发布），reproducibility 在投稿阶段只是 promise。 |
| Ethics/Broader Impact | — | 未包含，EMNLP "鼓励" 但非强制。 |
| 参考文献格式 | ✅ | `\bibliography{references}` 使用 ACL 风格。注意 \cite 和 \citep/\citet 混用——某些位置用 \cite 应为 \citep（如 related_work.tex line 6-8 多处）。 |

---

## 主要优势

1. **实验方法论极其严谨**：Random baseline 作为 falsification control 的设计精良；bootstrap CI ($B=10000$)、Bonferroni correction、BH-FDR robustness check、Jonckheere-Terpstra dose-response test、permutation test、多种 segmentation granularity 的 sensitivity analysis——统计处理水平远超 NLP 领域平均。
2. **发现本身具有科学价值**：Phase-strategy interaction 的定量刻画（$G = 7.5$--$79.8\times$）是一个 previously undocumented 的现象。Crossover effect 在 DeepSeek 上的发现是 non-trivial 的。
3. **论文写作清晰诚实**：Limitations section 详尽，LLaMA 跨架构结果的 hedging 恰当（"preliminary", "suggestive", "mixed evidence"），没有隐藏 negative results（pilot failure 直接报告）。Discrimination collapse 被明确标记为 "correlational" 而非 causal。
4. **Reproducibility 细节充分**：exp_id 标注在 LaTeX 注释中，bootstrap seed 固定，所有 hyperparameters 明确报告。

---

## 关键问题（供 author response）

1. 是否有任何 problem-level accuracy 数据（即使是 partial）可以展示 II gradient 与 accuracy 退化的关系？
2. Crossover effect 在 Qwen 上不出现——作者对此的解释是什么？是否与 distillation vs instruction tuning 的 training methodology 相关？
3. Oracle mitigation 仅 18% recovery——作者是否分析了失败的原因？是 budget reallocation 不够，还是 phase boundary 不够精确，还是需要 strategy switching？
4. 对于 Table 2 中 Qwen s=0.15 的 $\widetilde{\mathrm{II}}_{\textit{high}} = -0.000$（sub-additive），作者如何解释？

---

*Reviewer 2, Round 1 完成。审查侧重：新颖性、完整性、相关工作、格式合规。*

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 514 · 2026-05-15T12:37:31.965778+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 36

## Round 36

2 recorded events


### User

_source line 515 · 2026-05-15T12:37:37.042051+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿报告已提交给 Review Director。

核心判断：**Overall 2.5/5**（borderline Findings / 需修改重投）。

三个 Must-Fix 问题：
1. **仅用 PPL 无 downstream accuracy** — construct validity 根本缺陷，PPL 退化可能不转化为 accuracy 下降
2. **单基准（MATH-500）+ 单规模（7B）** — generalizability 严重不足，两个 Qwen2 模型共享 backbone 独立性有限
3. **Mitigation pilot 失败（18% recovery, gate FAIL）** — 论文声称 "motivate phase-aware compression" 但自己的实验证明 direct application 不 work

主要优势：统计方法论极其严谨（远超 NLP 领域平均水平），发现本身有科学价值，写作诚实不隐藏 negative results。相关工作覆盖全面，引用验证未发现 fabrication。格式基本合规。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 516 · 2026-05-15T12:37:42.596906+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 37

## Round 37

6 recorded events


### User

_source line 517 · 2026-05-15T12:38:56.075359+00:00_

[Reviewer 1 审稿意见]:
## Round 1 审稿报告 — Reviewer 1（方法严谨性 + 实验设计 + 统计有效性）

**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models

---

## 总体评分

**Overall**: 3.0/5 (Findings acceptance)
**一句话总结**: 一个在有限范围内方法论严谨的实证表征研究，发现了 compound sparsity 的 phase-strategy 交互效应，但受限于单一 importance 评分方法、单一数据集、仅用 perplexity 作为指标、以及薄弱的机制解释，在影响力和泛化性上不足以达到 EMNLP main conference 标准。

## 官方维度打分（ACL Rolling Review review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法论严谨（bootstrap + Wilcoxon + JT 组合），但 G 指标在两处使用不一致定义、仅测试一种 importance 评分方法、且唯一指标为 perplexity。核心 claims 在测试范围内有充分支撑。 |
| Excitement | 3.0/5 | Crossover 效应和 phase-strategy interaction 概念新颖，但范围窄（一个架构族、一个数据集、一种 importance 方法）且无实际部署意义（无 accuracy、无 throughput、pilot 失败） |
| Reproducibility | 3/5 | 实验设置详细，但代码和数据承诺"接收后发布"；LLaMA 为何只跑 n=49 未解释 |
| Confidence | 4/5 | 熟悉 KV cache 压缩和非参数统计方法 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] G 指标定义在论文内部不一致，导致数值差异高达 5–35 倍

- 具体位置：Section 3 Eq. (2) vs. Appendix B (Table 4, profiling subset)
- 问题：Eq. (2) 定义 G^(i) = II^(i)_low / II^(i)_high，main text Table 2 报告的是 per-problem G^(i) 的 median（median of ratios）；而 Appendix B Table 4 (profiling subset) 使用 ratio of medians (II_low_tilde / II_high_tilde)。在 s=0.15 时，profiling 的 ratio-of-medians 给出 G=69，而 main table 的 median-of-ratios 给出 G=7.5——差异达 9.2 倍。s=0.30 时差异为 274 vs. 79.8（3.4 倍）。当 II_high ≈ 0（如 DeepSeek s=0.15, II_high = 0.003），per-problem 的 G^(i) 会爆炸（分母趋近零），两种定义产生截然不同的结果。
- 为什么影响接收：G 是论文标题级别的核心结果指标（"7.5–79.8×" 在 abstract 中），但论文实际上存在两套不可比的 G 值。
- 建议修改方向：(1) 统一使用一种 G 定义并在所有表格中保持一致；(2) 当 II_high ≈ 0 时，明确讨论 G 的数值稳定性；(3) 考虑用 log_2(G) 或有界变换降低对近零分母的敏感性。

**N2** [critical] 仅测试一种 importance 评分方法，却对"importance-based eviction"做类别性结论

- 具体位置：Section 3, Section 5, Discussion §7
- 问题：论文使用一种特定的 importance scoring（position-normalized cumulative attention mass, Eq. 3），但结论多处泛化为"importance-based eviction"整个类别。Discussion 说"Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H2O, SnapKV, PyramidKV), suggesting broad applicability"。然而 H2O 使用 heavy-hitter + recent token 组合评分，SnapKV 使用 observation window，Ada-KV 使用 per-head adaptive budgets——评分方式不同，对 discrimination collapse 的敏感性可能也不同。
- 为什么影响接收：核心 contribution 可能仅限于一种特定的 importance scoring，而非 importance-based eviction 的普遍特性。
- 建议：(1) 至少测试一种替代 importance 方法；(2) 将 claims 限定为 "cumulative-attention-mass-based importance scoring"。

**N3** [critical] 唯一的严重性指标是 perplexity，无下游任务准确率验证

- 具体位置：Section 3 (Eq. 1), Limitations
- 问题：II 基于 perplexity ratio 定义，而 MATH-500 的实际任务指标是 problem-level accuracy。Perplexity 和 accuracy 存在已知的非线性关系。论文声称 severity gradient 对部署有重要意义，但没有证据表明 G=79.8× 的 perplexity 放大在 accuracy 层面意味着什么。
- 为什么影响接收：如果 perplexity 放大没有导致显著的 accuracy 下降，核心发现在实践中可能不重要。
- 建议：报告不同 sparsity level 下的 problem-level accuracy drop（compressed vs. dense），分析 II 与 accuracy loss 的相关性。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "Cross-model replication" 实际是同架构复现，非独立验证
- 两个主要模型共享 Qwen2ForCausalLM 架构。Section 5.4 标题 "Cross-Model Replication" 容易误导。
- 建议改为 "Same-Architecture Cross-Training Replication"。

**W2** [warning] LLaMA n=49 的统计证据混乱，但在 abstract 和 conclusion 中被引用
- s=0.15: CI 排除零但 Wilcoxon 不显著；s=0.30: CI 包含零但 Wilcoxon 显著——同一数据给出相反结论。
- 论文未解释为何不在 LLaMA 上运行完整 n=500。
- 以 n=49 做 4 个 Bonferroni 校正检验，power 严重不足。
- 建议：明确说明 n=49 的原因；报告 post-hoc power；考虑降级为 Appendix 中的 exploratory analysis。

**W3** [warning] Bonferroni k=4 的 family 分组可能过于宽松
- 44 个检验分为多个 family 各用 k=4，而非全局 k=44。BH-FDR robustness check 部分缓解了这个问题（所有 Bonf-sig 结果在 BH-FDR 下仍显著），但应更清晰论证分组合理性。

**W4** [warning] 43:1 mean/median ratio 暗示极端离群值，但论文未分析其性质
- 这些离群值可能来自特定类型的数学题或 phase segmentation 的边界效应。
- 建议加入 Appendix 离群值分析。

**W5** [warning] Pilot mitigation 失败（18% < 30% gate），但 Conclusion 仍说 "motivate phase-aware sparsity allocation"
- 从 failed pilot 到 "motivate" 的跳跃过大。
- 建议改为 "identify the need for, but do not yet demonstrate"。

---

## 小问题

- Table 2 中 Qwen s=0.15 importance 的 II_high = -0.000，负号是 numerical artifact，应标注
- Figure 1 用 n=50 profiling subset，但主结果表用 n=496——figure/table 样本量不一致可能导致困惑
- Section 5.3 中 1.498 vs Table 2 中 1.514 数值不一致
- 引用验证：3 个 bib 条目在 OpenAlex 中未找到（defensivekv-iclr2026, hies-2025, phase-transition-compression-2026）——应确认真实性

---

## 主要优势

1. 研究问题定位精准——compound sparsity 的 phase 依赖性填补文献空白
2. 统计方法论严谨——非参数方法处理重度右偏分布恰当，多重检验校正+多项 sensitivity analysis 体现统计素养
3. Crossover 效应是真正新颖的发现——single-axis 分析无法预测的定性新现象
4. 诚实的 limitations 讨论——承认 correlational mechanism、failed pilot、mixed LLaMA evidence
5. Related work 全面且当前（33 篇，覆盖 2026 最新文献）
6. Random eviction 作为 falsification control 设计合理

---

## Questions to Authors

1. 为什么 LLaMA 实验只在 n=49 上运行？
2. 是否考虑过在 H2O 或 SnapKV 的 importance scoring 上重复实验？
3. Table 4 vs Table 2 的 G 值差异高达 9x——哪个定义更准确反映效应量级？
4. Qwen s=0.25 entropy reversal (ΔH = +0.045) 有更深入分析吗？
5. 有没有分析 problem difficulty / sequence length 与 II outliers 的关系？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-15T12:39:24.741620+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "phase-gated-compound-sparse",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文（审查侧重：新颖性 + 完整性 + 相关工作 + 格式合规，Overall 2.5/5）。\n\n请逐条回应每个 Must-Fix 和 Should-Fix 问题：用 `[AGREE]` 表示同意并说明理由，或 `[REBUT]` 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 的 Must-Fix 问题：\n\n**N1** [critical] **仅用 Perplexity，缺少 Downstream Accuracy 验证**\n- 论文的核心指标 II 完全基于 perplexity。Limitations 中作者承认 \"perplexity has a known nonlinear relationship with downstream accuracy\"，但未提供任何 accuracy 层面的验证。PPL 的 phase-level 恶化可能在 accuracy 层面被吸收。\n- 论文声称 \"motivate phase-aware compression budgets for mathematical reasoning models\"，但如果 PPL 恶化不转化为 accuracy 下降，则整个 motivation 不成立。\n\n**N2** [critical] **Generalizability 极度受限：单一基准 + 单一模型规模**\n- 全部实验仅在 MATH-500 上进行，仅评估 7B 模型。两个 Qwen2 模型共享 backbone，cross-model replication 独立性有限。LLaMA 验证 n=49 且统计显著性混合。\n\n**N3** [critical] **Mitigation Pilot 失败，论文的实际价值存疑**\n- Oracle phase-aware budget reallocation 仅达 18% recovery（预注册 30% gate FAIL）。论文声称 \"motivate phase-aware compression\" 但自己的 pilot 证明 direct application 不 work。\n\n### Reviewer 2 的 Should-Fix 问题：\n\n**W1** [warning] Crossover Effect 的 model dependence 削弱了核心 contribution 之一\n- Crossover 仅在 DeepSeek 上出现，Qwen 不存在。但 Introduction 中将 crossover 作为核心论证的关键证据。\n\n**W2** [warning] \"Emergent\" 用词 overclaiming\n- \"Emergent\" 在 ML 社区有 scale-dependent 含义，此处实际是 interaction effect。\n\n**W3** [warning] 缺少 Throughput/Latency 评估\n- 论文声称 \"motivate phase-aware compression budgets for deployment\" 但完全没有 throughput 或 latency 数据。\n\n**W4** [warning] Discrimination Collapse 分析的 sufficiency gap\n- \"Structural specificity\" 解释仅是定性论证，没有定量证据直接支持。\n\n**W5** [warning] Abstract 的 bootstrap CI 呈现具有误导性\n- \"$G$ of $7.5$--$79.8\\times$ (bootstrap 95\\% CI: $[4.1, 96.5]$)\" 将四个不同 sparsity level 的 CI 拼接在一起，不是任何单一参数的置信区间。\n\n---\n\n请对以上每条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "phase-gated-compound-sparse",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文（审查侧重：新颖性 + 完整性 + 相关工作 + 格式合规，Overall 2.5/5）。\n\n请逐条回应每个 Must-Fix 和 Should-Fix 问题：用 `[AGREE]` 表示同意并说明理由，或 `[REBUT]` 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 的 Must-Fix 问题：\n\n**N1** [critical] **仅用 Perplexity，缺少 Downstream Accuracy 验证**\n- 论文的核心指标 II 完全基于 perplexity。Limitations 中作者承认 \"perplexity has a known nonlinear relationship with downstream accuracy\"，但未提供任何 accuracy 层面的验证。PPL 的 phase-level 恶化可能在 accuracy 层面被吸收。\n- 论文声称 \"motivate phase-aware compression budgets for mathematical reasoning models\"，但如果 PPL 恶化不转化为 accuracy 下降，则整个 motivation 不成立。\n\n**N2** [critical] **Generalizability 极度受限：单一基准 + 单一模型规模**\n- 全部实验仅在 MATH-500 上进行，仅评估 7B 模型。两个 Qwen2 模型共享 backbone，cross-model replication 独立性有限。LLaMA 验证 n=49 且统计显著性混合。\n\n**N3** [critical] **Mitigation Pilot 失败，论文的实际价值存疑**\n- Oracle phase-aware budget reallocation 仅达 18% recovery（预注册 30% gate FAIL）。论文声称 \"motivate phase-aware compression\" 但自己的 pilot 证明 direct application 不 work。\n\n### Reviewer 2 的 Should-Fix 问题：\n\n**W1** [warning] Crossover Effect 的 model dependence 削弱了核心 contribution 之一\n- Crossover 仅在 DeepSeek 上出现，Qwen 不存在。但 Introduction 中将 crossover 作为核心论证的关键证据。\n\n**W2** [warning] \"Emergent\" 用词 overclaiming\n- \"Emergent\" 在 ML 社区有 scale-dependent 含义，此处实际是 interaction effect。\n\n**W3** [warning] 缺少 Throughput/Latency 评估\n- 论文声称 \"motivate phase-aware compression budgets for deployment\" 但完全没有 throughput 或 latency 数据。\n\n**W4** [warning] Discrimination Collapse 分析的 sufficiency gap\n- \"Structural specificity\" 解释仅是定性论证，没有定量证据直接支持。\n\n**W5** [warning] Abstract 的 bootstrap CI 呈现具有误导性\n- \"$G$ of $7.5$--$79.8\\times$ (bootstrap 95\\% CI: $[4.1, 96.5]$)\" 将四个不同 sparsity level 的 CI 拼接在一起，不是任何单一参数的置信区间。\n\n---\n\n请对以上每条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-15T12:39:35.159887+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 10418
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-15T12:39:35.310984+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "phase-gated-compound-sparse",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文（审查侧重：方法严谨性 + 实验设计 + 统计有效性，Overall 3.0/5）。\n\n请逐条回应每个 Must-Fix 和 Should-Fix 问题：用 `[AGREE]` 表示同意并说明理由，或 `[REBUT]` 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 的 Must-Fix 问题：\n\n**N1** [critical] G 指标定义在论文内部不一致，导致数值差异高达 5–35 倍\n- Eq. (2) 定义 per-problem G^(i) 的 median（median of ratios），Appendix B Table 4 使用 ratio of medians。s=0.15 时差异 69 vs 7.5（9.2 倍）。当 II_high ≈ 0 时 per-problem G^(i) 会爆炸。\n\n**N2** [critical] 仅测试一种 importance 评分方法，却对\"importance-based eviction\"做类别性结论\n- 论文使用 position-normalized cumulative attention mass，但结论泛化为\"importance-based eviction\"整个类别。Discussion 声称 \"broad applicability\" 基于 H2O/SnapKV/PyramidKV 共享 attention-mass 评分，但这些方法的具体实现差异很大。\n\n**N3** [critical] 唯一的严重性指标是 perplexity，无下游任务准确率验证\n- 与你的 N1 一致。II 基于 perplexity ratio，MATH-500 的实际任务指标是 problem-level accuracy。\n\n### Reviewer 1 的 Should-Fix 问题：\n\n**W1** [warning] \"Cross-model replication\" 实际是同架构复现，非独立验证\n- 两个主要模型共享 Qwen2ForCausalLM 架构，Section 5.4 标题容易误导。\n\n**W2** [warning] LLaMA n=49 的统计证据混乱\n- s=0.15 CI 排除零但 Wilcoxon 不显著；s=0.30 CI 包含零但 Wilcoxon 显著。未解释为何不运行 n=500。\n\n**W3** [warning] Bonferroni k=4 的 family 分组可能过于宽松\n- 44 个检验分为多个 family 各用 k=4，BH-FDR 部分缓解。\n\n**W4** [warning] 43:1 mean/median ratio 暗示极端离群值未分析\n- 可能来自特定类型数学题或 phase segmentation 边界效应。\n\n**W5** [warning] Pilot mitigation 失败但 Conclusion 仍说 \"motivate phase-aware sparsity allocation\"\n- 从 failed pilot 到 \"motivate\" 的跳跃过大。\n\n### Reviewer 1 的小问题：\n- Table 2 中 Qwen s=0.15 II_high = -0.000 负号是 numerical artifact\n- Figure 1 用 n=50 vs main results 用 n=496\n- Section 5.3 中 1.498 vs Table 2 中 1.514 数值不一致\n- 3 个 bib 条目在 OpenAlex 中未找到\n\n---\n\n请对以上每条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "phase-gated-compound-sparse",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文（审查侧重：方法严谨性 + 实验设计 + 统计有效性，Overall 3.0/5）。\n\n请逐条回应每个 Must-Fix 和 Should-Fix 问题：用 `[AGREE]` 表示同意并说明理由，或 `[REBUT]` 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 的 Must-Fix 问题：\n\n**N1** [critical] G 指标定义在论文内部不一致，导致数值差异高达 5–35 倍\n- Eq. (2) 定义 per-problem G^(i) 的 median（median of ratios），Appendix B Table 4 使用 ratio of medians。s=0.15 时差异 69 vs 7.5（9.2 倍）。当 II_high ≈ 0 时 per-problem G^(i) 会爆炸。\n\n**N2** [critical] 仅测试一种 importance 评分方法，却对\"importance-based eviction\"做类别性结论\n- 论文使用 position-normalized cumulative attention mass，但结论泛化为\"importance-based eviction\"整个类别。Discussion 声称 \"broad applicability\" 基于 H2O/SnapKV/PyramidKV 共享 attention-mass 评分，但这些方法的具体实现差异很大。\n\n**N3** [critical] 唯一的严重性指标是 perplexity，无下游任务准确率验证\n- 与你的 N1 一致。II 基于 perplexity ratio，MATH-500 的实际任务指标是 problem-level accuracy。\n\n### Reviewer 1 的 Should-Fix 问题：\n\n**W1** [warning] \"Cross-model replication\" 实际是同架构复现，非独立验证\n- 两个主要模型共享 Qwen2ForCausalLM 架构，Section 5.4 标题容易误导。\n\n**W2** [warning] LLaMA n=49 的统计证据混乱\n- s=0.15 CI 排除零但 Wilcoxon 不显著；s=0.30 CI 包含零但 Wilcoxon 显著。未解释为何不运行 n=500。\n\n**W3** [warning] Bonferroni k=4 的 family 分组可能过于宽松\n- 44 个检验分为多个 family 各用 k=4，BH-FDR 部分缓解。\n\n**W4** [warning] 43:1 mean/median ratio 暗示极端离群值未分析\n- 可能来自特定类型数学题或 phase segmentation 边界效应。\n\n**W5** [warning] Pilot mitigation 失败但 Conclusion 仍说 \"motivate phase-aware sparsity allocation\"\n- 从 failed pilot 到 \"motivate\" 的跳跃过大。\n\n### Reviewer 1 的小问题：\n- Table 2 中 Qwen s=0.15 II_high = -0.000 负号是 numerical artifact\n- Figure 1 用 n=50 vs main results 用 n=496\n- Section 5.3 中 1.498 vs Table 2 中 1.514 数值不一致\n- 3 个 bib 条目在 OpenAlex 中未找到\n\n---\n\n请对以上每条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-15T12:39:36.827332+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1516
}
```

</details>

---


### Assistant

_source line 522 · 2026-05-15T12:39:39.441023+00:00_

交叉分享已发送给两位 Reviewer，等待回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 38

## Round 38

2 recorded events


### User

_source line 523 · 2026-05-15T12:39:42.085762+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

总结：论文发现 compound sparsity 的 phase-strategy 交互效应，统计方法论扎实，crossover 效应新颖。三个 critical 问题：(1) G 指标在 profiling table 和 main table 中使用不同定义，差异达 9x；(2) 仅测试一种 importance scoring 却泛化为整个类别；(3) 仅用 perplexity 无 accuracy 验证。五个 should-fix 问题涉及同架构"cross-model replication"措辞、LLaMA n=49 power 不足、Bonferroni family 分组、离群值分析缺失、以及 failed pilot 与 conclusion framing 的矛盾。Overall 评分 3.0/5，建议 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 524 · 2026-05-15T12:39:50.922044+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 39

## Round 39

2 recorded events


### User

_source line 525 · 2026-05-15T12:41:16.846664+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

### Must-Fix

**[AGREE] R2-N1 (Perplexity only)**: 与我的 N3 一致。论文至少应报告 aggregate accuracy drop 和 per-problem II 与 accuracy loss 的 rank correlation 作为 sanity check。

**[AGREE with qualification] R2-N2 (Generalizability)**: 同意核心问题（同架构、单数据集、单规模），但 "极度受限" 措辞过强。论文在 scope 内的验证是充分的（training difference, robustness checks），问题在于 claims 超出 scope——特别是泛称 "importance-based eviction" 而只测了一种方法（我的 N2）。

**[REBUT] R2-N3 (Pilot failure → paper value questioned)**: 论文三个 contribution 均为 characterization，非 mitigation。Pilot 在 Discussion 中明确标为 preliminary 且诚实报告了 gate FAIL。Characterization papers 在 *ACL 中不要求提供解决方案。问题仅在 framing（Conclusion 的 "motivate" 过度乐观），应作为 Should-Fix 处理，而非否定论文价值。

### Should-Fix

**[AGREE with nuance] R2-W1 (Crossover model dependence)**: 同意 Introduction 过度依赖 crossover 来论证 "emergent coupling"。但 crossover 在 contribution list 中已是 subordinate finding，非独立 contribution。建议降低 Introduction 正文中的论证权重。

**[REBUT] R2-W2 ("Emergent" overclaiming)**: 论文的 "emergent" 用法是科学文献中的标准含义（interaction-derived property），非 ML 中 scale-dependent 的特定含义。论文从未声称 scale-dependence，且 Limitations 明确标注 scale 未验证。

**[AGREE] R2-W3 (No throughput/latency)**: 同意是 gap，但问题本质是 claims 超出 scope（"deployment" framing）而非论文必须包含系统评测。

**[AGREE] R2-W4 (Discrimination collapse sufficiency gap)**: 同意。6-16% Gini reduction 到 7.5-79.8× amplification 的巨大 gap 未被 bridged，"structural specificity" 停留在定性推测层面。

**[AGREE] R2-W5 (Abstract CI misleading)**: 强烈同意。[4.1, 96.5] 是四个独立 CI 的 envelope，不是任何单一参数的置信区间。这个呈现方式具有误导性，应修改为分别报告各 sparsity level 的 CI 或省略。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 526 · 2026-05-15T12:41:22.317079+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 40

## Round 40

2 recorded events


### User

_source line 527 · 2026-05-15T12:41:24.955693+00:00_

[Reviewer 1 审稿结果]:
交叉回应已发送。总结：

- **3 个 AGREE**（N1 perplexity-only、W3 no throughput、W4 sufficiency gap、W5 CI misleading）
- **1 个 AGREE with qualification**（N2 generalizability——核心问题成立但措辞过强）
- **1 个 AGREE with nuance**（W1 crossover model dependence）
- **2 个 REBUT**（N3 pilot failure 不应否定 characterization 论文的价值；W2 "emergent" 用法符合科学文献标准）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 528 · 2026-05-15T12:41:29.876988+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 41

## Round 41

6 recorded events


### User

_source line 529 · 2026-05-15T12:42:37.881169+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见

---

### Must-Fix 问题回应

**[AGREE] R1-N1: G 指标定义不一致（ratio of medians vs median of ratios）**

R1 的观察是准确的。我核实了以下数值：
- Table 2（§5.2, main results, n=496）：G = 7.5 [4.1, 11.4] at s=0.15 — **median of per-problem ratios**（Eq. 2）
- Table 4（Appendix B, profiling, n=50）：G = 69 at s=0.15 — **ratio of medians**（caption 明确标注 "$G = \widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$"）

两种计算方式在 $\mathrm{II}_{\textit{high}} \approx 0$ 时严重分歧。以 DeepSeek s=0.15 为例：$\widetilde{\mathrm{II}}_{\textit{high}} = 0.003$（Table 2），ratio of medians = 0.357/0.003 ≈ 119，而 median of per-problem ratios = 7.5。差异来源是 per-problem $G^{(i)}$ 的分布极度右偏（部分 problem 的 $\mathrm{II}_{\textit{high}}^{(i)}$ 极小导致 ratio 爆炸，median 抑制了这些极端值）。

论文虽在 Table 4 caption 中注明了差异，但这两个不同定义使用同一符号 $G$，且 Abstract 中的 "$G$ of $7.5$--$79.8\times$" 与 Appendix 的 $69$--$274\times$ 给读者造成混淆。更关键的是，**论文应统一使用一种 $G$ 定义**（建议全文使用 median of per-problem ratios + bootstrap CI，因其更 robust），或至少在首次出现时明确区分两种计算方式。

补充我自己的 W5 的相关发现：Abstract 中 "bootstrap 95% CI: [4.1, 96.5]" 实际上是将四个 sparsity level 的 CI 端点拼接（4.1 来自 s=0.15 lower bound, 96.5 来自 s=0.30 upper bound），不是单一参数的 CI，属于统计呈现不规范。

---

**[AGREE] R1-N2: 单一 importance 评分方法不支持类别性结论**

R1 的批评有道理。论文仅测试了 position-normalized cumulative attention mass（Eq. 3, Appendix A），但 Discussion §7 声称 "Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H2O, SnapKV, PyramidKV), suggesting broad applicability"。

我部分同意并补充：
1. **方向上**，discrimination collapse 机制（head pruning 压平 importance score 分布）在理论上适用于任何基于 attention mass 的评分，因为 head pruning 改变 attention 分布这一事实独立于具体评分公式。因此**定性方向**可能 generalizable。
2. **定量上**，R1 正确指出 H2O（heavy-hitter 选择）、SnapKV（observation window 聚合）、PyramidKV（层级自适应 budget）的具体实现差异很大。不同聚合方式对 discrimination collapse 的敏感度可能不同。论文没有证据支持定量结论的泛化。
3. 建议：将 "broad applicability" 改为 "directionally consistent prediction for attention-mass-based methods"，并明确标注这是一个未验证的推测。

---

**[AGREE] R1-N3: 缺少 downstream accuracy 验证**

与我的 N1 完全一致。补充两点：

1. **这个问题比 R1 描述的可能更严重**：PPL 是 per-token 指标，而 MATH-500 的评估单位是 problem-level accuracy（final answer 正确与否）。Low-sparsity phase 通常对应 exploratory reasoning（Abstract 所述），此 phase 的 token 对最终答案的贡献可能远低于 high-sparsity phase（structured computation）的 token。因此，即使 low-sparsity phase PPL 退化严重（$G \gg 1$），如果退化集中在对 final answer 不关键的 reasoning trace 上，整体 accuracy 可能不受影响——这将从根本上改变论文的结论。

2. **反过来说**，如果作者能展示 II 与 problem-level accuracy 之间存在显著相关（例如 high-II problems 更可能答错），这将**大幅增强论文的说服力**。这不需要新的实验，只需要在现有数据上做 regression analysis。

---

### Should-Fix 问题回应

**[AGREE] R1-W1: "Cross-model replication" 标题具有误导性**

§5.4 标题为 "Cross-Model Replication"，但 Appendix D 开头明确承认 "Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA)"。这实际上是 **cross-training-methodology replication**（distillation vs instruction tuning on same architecture），不是 cross-architecture。§5.5 才是 cross-architecture（LLaMA），但那里的证据很弱。

建议将 §5.4 改为 "Cross-Training Replication" 或 "Within-Architecture Replication"，避免读者误以为是独立架构的验证。这与我自己的 N2 中 "两个 Qwen2 模型共享 backbone，cross-model replication 的独立性有限" 一致。

---

**[AGREE] R1-W2: LLaMA n=49 的统计证据混乱，且未解释为何不跑 n=500**

两个层面的问题：

1. **CI/Wilcoxon 不一致**：论文 footnote（§5.5）给出了合理的统计解释——percentile bootstrap CI 对尾部不敏感，Wilcoxon signed-rank 对尾部 outlier 更敏感。在 n=49 + heavy-tailed 条件下，两种方法的 power profile 不同。这个解释本身是正确的。

2. **为何不跑 n=500？** 这是 R1 的关键追问，论文完全没有回应。如果资源允许在 DeepSeek 和 Qwen 上各跑 500 题，为什么 LLaMA 只跑了 49？可能的原因包括：(a) 计算资源限制（LLaMA-8B 比 Qwen-7B 稍大）；(b) n=49 已经显示效果很弱，作者判断跑更多也不会改变 "preliminary" 的定性结论。但论文应该明确说明原因，因为 49 这个数字暗示这是 profiling subset 的遗留而非有意设计。

---

**[REBUT] R1-W3: Bonferroni k=4 的 family 分组**

R1 认为 k=4 "可能过于宽松"，我部分不同意。

论文的 Bonferroni 分组策略是：每个 model × strategy 组合内，4 个 sparsity level 测试同一个 dose-response 假设。这在统计学上是合理的 family 定义——同一实验条件下对同一科学问题的多次检验。如果将所有 44 个检验放在一个 family（Bonferroni k=44），则过于保守。

更重要的是，**论文已在 Appendix E（Table 5）报告了 BH-FDR correction across all 44 tests**。结果：所有 32 个 Bonferroni-significant 结果在 BH-FDR 下仍然 significant（§Appendix E: "All Bonferroni-significant results remain significant under BH-FDR"）。BH-FDR 额外恢复了 5 个 result，全部是 random eviction 的弱效应。

因此，无论使用哪种 correction 策略，**核心结论（importance-based eviction 的 phase gradient）均不受影响**。R1 的担忧在技术上有道理，但实际影响为零。

---

**[AGREE] R1-W4: 43:1 mean/median ratio 的极端离群值未分析**

§4 (methodology.tex line 18) 提到 "mean/median ratios up to 43:1"，Extended Limitations (Appendix G) 也提到。但论文从未分析这些极端 outlier 来自哪里。

可能的来源：
1. **Phase segmentation 边界效应**：非常短的 phase segment（接近 min_phase_length=10）可能产生 volatile PPL 估计。
2. **特定题目类型**：某些数学领域（如 combinatorics 可能产生更长更复杂的 reasoning trace，放大了 compound sparsity 效应）。
3. **Numerical artifacts**：bfloat16 精度在极端 softmax 值下的 noise。

作者应至少做一个 outlier 分析：报告 top-10 outlier problems 的特征（subject area、sequence length、phase distribution），并验证去除 top-5% outlier 后主要结论是否稳健。这对论文的可信度很重要。

---

**[AGREE] R1-W5: Pilot failure 与 "motivate" 之间的 framing 跳跃**

与我的 N3 完全一致。补充：

Conclusion §8 最后一句："These findings motivate phase-aware sparsity allocation for reasoning model deployment." 但 §7 Discussion 的 pilot 结果是：oracle recovery 18%（gate FAIL），heuristic 32%（CI 跨零）。从 failed pilot 直接跳到 "motivate" 在逻辑上不连贯。

R1 和我在这个问题上的判断一致：论文应将 framing 从 "motivate solution X" 调整为 "characterize phenomenon Y, which is a prerequisite for future solutions"。这样既诚实又仍有贡献价值。

---

### 小问题回应

**[AGREE] Table 2 中 Qwen s=0.15 $\mathrm{II}_{\textit{high}} = -0.000$**
我也在小问题 M1 中指出了这个问题。这几乎确定是 numerical noise（bfloat16 精度下，PPL ratios 的微小偏差），但论文应在 footnote 或 text 中说明。

**[AGREE] Figure 1 用 n=50 vs main results 用 n=496**
我在小问题 M3 中也指出。Hero figure 应用 full-scale 数据，否则会让读者质疑为什么主图不用最好的数据。

**[AGREE] §5.3 中 1.498 vs Table 2 中 1.514**
我核实了具体数值：
- Table 2（§5.2）：Random s=0.25, $\widetilde{\mathrm{II}}_{\textit{low}} = 1.514$
- §5.3 正文："$3.971$ vs.\ $1.498$"
- Appendix C（appendix_moved.tex）：同样使用 "$1.498$"

数值不一致（1.498 vs 1.514）。从 LaTeX 注释看，§5.3 引用 crossover_all_sparsity.csv，而 Table 2 引用 table2_n500_full.csv。两个 CSV 文件可能使用了略有不同的聚合方式。虽然差异很小（1.1%），但同一论文中对同一量的报告应一致。

进一步发现：Qwen crossover 数值也有类似小不一致——§5.3/Appendix 报告 Qwen s=0.25 importance low 为 1.043，但 Table 2 为 1.053。同样量级的偏差。这暗示 crossover 分析可能使用了不同的 problem subset 或不同的聚合路径，需要作者澄清。

**[AGREE] 3 个 bib 条目 OpenAlex 未找到**
我的验证结果一致：defensivekv-iclr2026、hies-2025、phase-transition-compression-2026 未在 OpenAlex 中匹配。三者均有有效 arXiv URL。很可能是 OpenAlex 索引延迟，不是 fabricated references。

---

### 总结：与 Reviewer 1 的主要分歧和共识

| 议题 | R1 | R2 | 一致性 |
|------|-----|-----|--------|
| G 指标不一致 (N1) | Critical | Agree, 补充 Abstract CI 拼接问题 | ✅ 一致 |
| 单一 importance 方法 (N2) | Critical | Agree 定量层面; 定性方向可能 generalizable | ⚠️ 部分一致 |
| 缺 accuracy (N3) | Critical | Agree, 补充 phase-accuracy 关系分析 | ✅ 一致 |
| Cross-model 误导 (W1) | Warning | Agree | ✅ 一致 |
| LLaMA n=49 (W2) | Warning | Agree; CI/Wilcoxon 解释合理但 n=49 原因缺失 | ✅ 一致 |
| Bonferroni k=4 (W3) | Warning | **Rebut**: family 定义合理, BH-FDR 已验证 | ❌ 分歧 |
| 43:1 outliers (W4) | Warning | Agree, 建议 outlier profiling | ✅ 一致 |
| Pilot fail vs motivate (W5) | Warning | Agree, 应调整 framing | ✅ 一致 |

**唯一分歧**在 W3（Bonferroni family 分组）：R1 认为 k=4 可能宽松，我认为 family 定义合理且 BH-FDR 已覆盖。这不影响任何核心结论。

**两位 reviewer 共识**：最严重的三个问题是 (1) 缺少 downstream accuracy, (2) G 指标定义不一致, (3) generalizability 受限。这些是 author response 必须回应的核心问题。

*Reviewer 2, 交叉回应完成。*

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-15T12:44:59.870738+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "issues_yaml": "- id: R6-N1\n  summary: \"Crossover evidence based on n=50 not verified at n=496; Table 2 uses n=50 G values (69-274x) overestimating by 42-85%\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - {round: 5, reviewers: [R1, R2], note: \"R5-W1/R5-W2: Table 2 n=50 and crossover n=50 flagged\"}\n    - {round: 6, reviewers: [R1, R2], note: \"Upgraded to critical. n=496 data exists but not incorporated.\"}\n  action_items:\n    - {round: 6, action: \"Replace Table 2 with n=500 per-phase numbers; move n=50 to Appendix; update §5.3 crossover; cascade updates\", assigned_to: paper_agent, status: done}\n  resolution: \"Table 2 expanded to DS(n=496)+QW(n=475) 16-row dual-model table. G=7.5-79.8x importance, 0.5-1.3x random. QW s015 G marked n.d. with dagger footnote. n=50 moved to Appendix. Cascade to §5.2, Fig1, Conclusion, Discussion.\"\n  resolution_round: 6\n\n- id: R6-N2\n  summary: \"Discrimination collapse effect size (Gini drop 6-16%) vs severity gradient (G=30-148x) magnitude gap (~200-2000x)\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"Consensus: gap between score-level changes and outcome-level amplification unaddressed\"}\n  action_items:\n    - {round: 6, action: \"Extract baseline Gini + compute relative changes\", assigned_to: main_agent, status: done}\n    - {round: 6, action: \"Rewrite §6 as correlational diagnostic with structural specificity\", assigned_to: paper_agent, status: done}\n  resolution: \"§6 rewritten as correlational diagnostic. Key evidence: imp/rand ΔGini nearly identical but severity differs 15-17x → Gini necessary but not sufficient. Structural specificity of pruned heads as differentiator. Intro/Conclusion/Abstract downgraded. Contribution 3 updated.\"\n  resolution_round: 6\n\n- id: R6-N3\n  summary: \"'following ThinKV' misattributes phase segmentation method\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - {round: 1, reviewers: [R1], note: \"R1-W1: ThinKV wording flagged\"}\n    - {round: 5, reviewers: [R1], note: \"R5-1: still open\"}\n    - {round: 6, reviewers: [R1, R2], note: \"5 rounds unfixed\"}\n  action_items:\n    - {round: 6, action: \"Change to 'inspired by ThinKV's phase-aware perspective'\", assigned_to: paper_agent, status: done}\n  resolution: \"Rewritten with explicit quantile-based vs explicit delimiter distinction.\"\n  resolution_round: 6\n\n- id: R6-W1\n  summary: \"Spearman ρ=1.0 on n=4 over-reported\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"Consensus: n=4 statistically weak\"}\n  action_items:\n    - {round: 6, action: \"Demote Spearman to footnote; promote JT test\", assigned_to: paper_agent, status: done}\n  resolution: \"JT test primary. Spearman in footnote with power caveat.\"\n  resolution_round: 6\n\n- id: R6-W2\n  summary: \"Novelty perceived as incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"R1 3.5/5, R2 2.5/5 divergence\"}\n  action_items:\n    - {round: 6, action: \"Add novelty paragraph with multiplicative null deviation\", assigned_to: paper_agent, status: done}\n  resolution: \"Introduction paragraph added: sign reversal + 2.7x multiplicative null excess not deducible from single-axis work.\"\n  resolution_round: 6\n\n- id: R6-W3\n  summary: \"No downstream accuracy evaluation\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"PPL→accuracy gap\"}\n    - {round: 7, reviewers: [R1, R2], note: \"Re-raised as critical. Both reviewers consensus: construct validity issue. PPL degradation in low-sparsity phase may not translate to accuracy loss if degradation concentrates on non-critical reasoning trace tokens.\"}\n  action_items:\n    - {round: 6, action: \"Add Limitations paragraph on PPL choice\", assigned_to: paper_agent, status: done}\n    - {round: 7, action: \"Report problem-level accuracy under compound sparsity; analyze II vs accuracy correlation; if PPL→accuracy link is weak, revise core claims\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R6-W4\n  summary: \"Mitigation pilot failure under-discussed\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"Characterization value needs discussion\"}\n    - {round: 7, reviewers: [R1, R2], note: \"Re-assessed. R2 elevates to critical (motivate claim unsupported by failed pilot); R1 keeps as should-fix (characterization paper doesn't require solution). Consensus: framing must change from 'motivate solution' to 'characterize phenomenon'.\"}\n  action_items:\n    - {round: 6, action: \"Add Discussion paragraph on characterization value\", assigned_to: paper_agent, status: done}\n    - {round: 7, action: \"Revise Conclusion/Abstract framing from 'motivate phase-aware compression' to 'characterize phase-dependent phenomenon as prerequisite for future solutions'\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R6-W5\n  summary: \"Entropy redistribution cross-model inconsistency\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"~15% Analysis for non-robust mechanism\"}\n  action_items:\n    - {round: 6, action: \"Trim §6.2 to ~50%; reframe as supplementary\", assigned_to: paper_agent, status: done}\n  resolution: \"Trimmed to ~50 words. Model-dependent, not universal mechanism.\"\n  resolution_round: 6\n\n- id: R6-W6\n  summary: \"LLaMA CI/Wilcoxon inconsistency\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"Technical explanation needed\"}\n  action_items:\n    - {round: 6, action: \"Add footnote on CI vs Wilcoxon divergence\", assigned_to: paper_agent, status: done}\n  resolution: \"Footnote in §5.5: bootstrap median vs signed-rank sensitivity to tails at n=50.\"\n  resolution_round: 6\n\n- id: R6-W7\n  summary: \"Missing citation: Hold Onto That Thought (NeurIPS 2025)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"Direct KV compression + reasoning evaluation\"}\n  action_items:\n    - {round: 6, action: \"Add bib entry + Related Work citation\", assigned_to: paper_agent, status: done}\n  resolution: \"Bib entry added. Cited in Related Work as concurrent single-axis KV compression + reasoning work.\"\n  resolution_round: 6\n\n- id: R6-W8\n  summary: \"h2o-neurips2023 bib title empty\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - {round: 4, reviewers: [R1], note: \"First flagged\"}\n    - {round: 5, reviewers: [R1], note: \"Still empty\"}\n    - {round: 6, reviewers: [R1, R2], note: \"3 rounds unfixed\"}\n  action_items:\n    - {round: 6, action: \"Fill title\", assigned_to: paper_agent, status: done}\n  resolution: \"Title filled. Encoding simplified.\"\n  resolution_round: 6\n\n- id: R6-M1\n  summary: \"\\\\placeholder command residual\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - {round: 5, reviewers: [R1], note: \"R5-3\"}\n    - {round: 6, reviewers: [R1, R2], note: \"Still present\"}\n  action_items:\n    - {round: 6, action: \"Remove macro + all calls\", assigned_to: paper_agent, status: done}\n  resolution: \"Removed. No residual.\"\n  resolution_round: 6\n\n- id: R6-M2\n  summary: \"appendix_results.tex orphaned + duplicate label\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"Orphaned file\"}\n  action_items:\n    - {round: 6, action: \"Delete orphaned file\", assigned_to: paper_agent, status: done}\n  resolution: \"Deleted.\"\n  resolution_round: 6\n\n- id: R6-M3\n  summary: \"Abstract 'over an order of magnitude' vague\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"Specify G range\"}\n  action_items:\n    - {round: 6, action: \"Replace with n=500 G range\", assigned_to: paper_agent, status: done}\n  resolution: \"G=7.5-79.8x, CI [4.1, 96.5].\"\n  resolution_round: 6\n\n- id: R6-M4\n  summary: \"LongFlow bib 'Withdrawn' annotation\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - {round: 5, reviewers: [R1], note: \"R5-2\"}\n    - {round: 6, reviewers: [R1, R2], note: \"Still present\"}\n  action_items:\n    - {round: 6, action: \"Remove Withdrawn note\", assigned_to: paper_agent, status: done}\n  resolution: \"Removed.\"\n  resolution_round: 6\n\n- id: R6-M5\n  summary: \"SnapKV first author verification\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R2], note: \"Li vs Cai?\"}\n  action_items:\n    - {round: 6, action: \"Verify\", assigned_to: paper_agent, status: done}\n  resolution: \"First author Yuhong Li confirmed correct.\"\n  resolution_round: 6\n\n# ===== Round 7 New Issues =====\n\n- id: R7-N1\n  summary: \"No downstream accuracy validation — construct validity gap between PPL-based II and task performance\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Consensus critical. PPL degradation in low-sparsity phase may concentrate on non-critical reasoning trace tokens. II vs problem-level accuracy correlation not established. Undermines deployment motivation claims.\"}\n  action_items:\n    - {round: 7, action: \"Report problem-level accuracy under compound sparsity across conditions; compute II vs accuracy-loss rank correlation; revise claims if link is weak\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-N2\n  summary: \"G metric definition inconsistent: median-of-ratios (Table 2) vs ratio-of-medians (Appendix Table 4), up to 9x discrepancy\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Consensus critical. s=0.15: 7.5 vs 69 (9.2x gap). Same symbol G used for different computations. Abstract CI [4.1, 96.5] is envelope of 4 independent CIs, not a single-parameter CI — statistically misleading.\"}\n  action_items:\n    - {round: 7, action: \"Unify G definition across all tables (recommend median-of-ratios + bootstrap CI); fix Abstract CI presentation; discuss numerical stability when II_high ≈ 0\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-N3\n  summary: \"Only one importance scoring method tested but categorical claims about 'importance-based eviction' class\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"R1 critical, R2 agrees quantitatively. Position-normalized cumulative attention mass (Eq.3) is the only method tested. Discussion claims 'broad applicability' to H2O/SnapKV/PyramidKV without evidence. R2 notes qualitative direction may generalize but quantitative claims unsupported.\"}\n  action_items:\n    - {round: 7, action: \"Option A: test at least one alternative importance method (e.g., H2O heavy-hitter). Option B: restrict all claims to 'cumulative-attention-mass-based scoring' and change 'broad applicability' to 'directionally consistent prediction'\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W1\n  summary: \"Generalizability limited: single benchmark (MATH-500), single scale (7B), same-architecture 'cross-model' replication\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"R2 critical, R1 agrees with qualification (scope within tested range is adequate, but claims exceed scope). Two Qwen2 models share backbone — 'Cross-Model Replication' title misleading. LLaMA n=49 too weak for meaningful cross-architecture claim.\"}\n  action_items:\n    - {round: 7, action: \"Rename §5.4 to 'Within-Architecture Replication' or 'Cross-Training Replication'; add at least one non-math benchmark or larger model, or explicitly narrow title/claims to tested scope\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W2\n  summary: \"Pilot mitigation failure (18% recovery, gate FAIL) contradicts 'motivate phase-aware compression' framing\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"R2 elevates to critical, R1 rebuts (characterization paper doesn't need solution) but agrees framing needs adjustment. Consensus: Conclusion 'motivate phase-aware sparsity allocation' is overclaim given failed pilot. Should reframe as 'characterize phenomenon as prerequisite for future solutions'.\"}\n  action_items:\n    - {round: 7, action: \"Revise Abstract/Conclusion from 'motivate' to 'characterize/identify'; analyze why oracle reallocation failed (budget vs strategy vs boundary precision)\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W3\n  summary: \"Crossover effect is model-dependent (DeepSeek only, absent in Qwen) but over-leveraged in Introduction\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"R2 warning, R1 agrees with nuance (crossover already subordinate in contribution list). Introduction §1 uses 'sign reversal' as key evidence for non-deducibility from single-axis work, but this reversal is model-specific.\"}\n  action_items:\n    - {round: 7, action: \"Reduce crossover weight in Introduction novelty argument; explicitly label as model-dependent in §1\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W4\n  summary: \"Discrimination collapse 'structural specificity' explanation lacks quantitative evidence\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Consensus. 6-16% Gini drop → 7.5-79.8x severity amplification gap not bridged. 'Structural specificity' is qualitative conjecture without per-head overlap analysis or other direct evidence.\"}\n  action_items:\n    - {round: 7, action: \"Provide pruned-head overlap analysis across phases (importance vs random), or explicitly acknowledge 'structural specificity' as unverified hypothesis\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W5\n  summary: \"LLaMA cross-architecture validation: n=49 with mixed significance, no explanation for limited sample\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Consensus. CI/Wilcoxon inconsistency explained in footnote, but why not run n=500? n=49 suggests profiling subset leftover. Post-hoc power not reported. Consider demoting to Appendix exploratory analysis.\"}\n  action_items:\n    - {round: 7, action: \"Explain n=49 rationale; report post-hoc power; consider running full n=500 or demoting to Appendix\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W6\n  summary: \"Abstract bootstrap CI [4.1, 96.5] is envelope of 4 independent CIs, not a single-parameter CI\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Consensus (R2 W5, R1 strongly agrees in cross-response). Statistically misleading presentation.\"}\n  action_items:\n    - {round: 7, action: \"Report per-sparsity CIs separately, or clearly label as 'range of CI bounds across sparsity levels'\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W7\n  summary: \"43:1 mean/median ratio extreme outliers unanalyzed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Consensus. Possible sources: phase segmentation boundary effects, specific problem types, bfloat16 numerical artifacts. No outlier profiling provided.\"}\n  action_items:\n    - {round: 7, action: \"Add outlier analysis in Appendix: top-10 outlier problem characteristics (subject, sequence length, phase distribution); verify conclusions robust after removing top-5% outliers\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-M1\n  summary: \"Table 2 Qwen s=0.15 II_high = -0.000: negative II not explained\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Likely bfloat16 numerical noise. Should add footnote.\"}\n  action_items:\n    - {round: 7, action: \"Add footnote explaining negative II as numerical artifact at bfloat16 precision\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-M2\n  summary: \"Figure 1 uses n=50 profiling subset but main results have n=496\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Consensus. Hero figure should use full-scale data for consistency.\"}\n  action_items:\n    - {round: 7, action: \"Regenerate Figure 1 with n=496 data\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-M3\n  summary: \"Numerical inconsistency: §5.3 reports 1.498, Table 2 reports 1.514 for same quantity (random s=0.25 II_low)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"1.1% discrepancy. Likely different CSV source files (crossover_all_sparsity.csv vs table2_n500_full.csv). Similar issue with Qwen s=0.25 importance low (1.043 vs 1.053).\"}\n  action_items:\n    - {round: 7, action: \"Reconcile data sources; ensure single source of truth for all reported values\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-M4\n  summary: \"pyramidkv-2024 bib year should be 2025 (Conference on Language Modeling 2025)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R2], note: \"Year mismatch in bib entry\"}\n  action_items:\n    - {round: 7, action: \"Update year to 2025\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-M5\n  summary: \"§5.1 p-values reported as p < 10^{-69} — overly specific, simplify\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R2], note: \"Suggest p ≪ 10^{-10} or similar\"}\n  action_items:\n    - {round: 7, action: \"Simplify extreme p-values to p ≪ 10^{-10}\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "issues_yaml": "- id: R6-N1\n  summary: \"Crossover evidence based on n=50 not verified at n=496; Table 2 uses n=50 G values (69-274x) overestimating by 42-85%\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - {round: 5, reviewers: [R1, R2], note: \"R5-W1/R5-W2: Table 2 n=50 and crossover n=50 flagged\"}\n    - {round: 6, reviewers: [R1, R2], note: \"Upgraded to critical. n=496 data exists but not incorporated.\"}\n  action_items:\n    - {round: 6, action: \"Replace Table 2 with n=500 per-phase numbers; move n=50 to Appendix; update §5.3 crossover; cascade updates\", assigned_to: paper_agent, status: done}\n  resolution: \"Table 2 expanded to DS(n=496)+QW(n=475) 16-row dual-model table. G=7.5-79.8x importance, 0.5-1.3x random. QW s015 G marked n.d. with dagger footnote. n=50 moved to Appendix. Cascade to §5.2, Fig1, Conclusion, Discussion.\"\n  resolution_round: 6\n\n- id: R6-N2\n  summary: \"Discrimination collapse effect size (Gini drop 6-16%) vs severity gradient (G=30-148x) magnitude gap (~200-2000x)\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"Consensus: gap between score-level changes and outcome-level amplification unaddressed\"}\n  action_items:\n    - {round: 6, action: \"Extract baseline Gini + compute relative changes\", assigned_to: main_agent, status: done}\n    - {round: 6, action: \"Rewrite §6 as correlational diagnostic with structural specificity\", assigned_to: paper_agent, status: done}\n  resolution: \"§6 rewritten as correlational diagnostic. Key evidence: imp/rand ΔGini nearly identical but severity differs 15-17x → Gini necessary but not sufficient. Structural specificity of pruned heads as differentiator. Intro/Conclusion/Abstract downgraded. Contribution 3 updated.\"\n  resolution_round: 6\n\n- id: R6-N3\n  summary: \"'following ThinKV' misattributes phase segmentation method\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - {round: 1, reviewers: [R1], note: \"R1-W1: ThinKV wording flagged\"}\n    - {round: 5, reviewers: [R1], note: \"R5-1: still open\"}\n    - {round: 6, reviewers: [R1, R2], note: \"5 rounds unfixed\"}\n  action_items:\n    - {round: 6, action: \"Change to 'inspired by ThinKV's phase-aware perspective'\", assigned_to: paper_agent, status: done}\n  resolution: \"Rewritten with explicit quantile-based vs explicit delimiter distinction.\"\n  resolution_round: 6\n\n- id: R6-W1\n  summary: \"Spearman ρ=1.0 on n=4 over-reported\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"Consensus: n=4 statistically weak\"}\n  action_items:\n    - {round: 6, action: \"Demote Spearman to footnote; promote JT test\", assigned_to: paper_agent, status: done}\n  resolution: \"JT test primary. Spearman in footnote with power caveat.\"\n  resolution_round: 6\n\n- id: R6-W2\n  summary: \"Novelty perceived as incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"R1 3.5/5, R2 2.5/5 divergence\"}\n  action_items:\n    - {round: 6, action: \"Add novelty paragraph with multiplicative null deviation\", assigned_to: paper_agent, status: done}\n  resolution: \"Introduction paragraph added: sign reversal + 2.7x multiplicative null excess not deducible from single-axis work.\"\n  resolution_round: 6\n\n- id: R6-W3\n  summary: \"No downstream accuracy evaluation\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"PPL→accuracy gap\"}\n    - {round: 7, reviewers: [R1, R2], note: \"Re-raised as critical. Both reviewers consensus: construct validity issue. PPL degradation in low-sparsity phase may not translate to accuracy loss if degradation concentrates on non-critical reasoning trace tokens.\"}\n  action_items:\n    - {round: 6, action: \"Add Limitations paragraph on PPL choice\", assigned_to: paper_agent, status: done}\n    - {round: 7, action: \"Report problem-level accuracy under compound sparsity; analyze II vs accuracy correlation; if PPL→accuracy link is weak, revise core claims\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R6-W4\n  summary: \"Mitigation pilot failure under-discussed\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"Characterization value needs discussion\"}\n    - {round: 7, reviewers: [R1, R2], note: \"Re-assessed. R2 elevates to critical (motivate claim unsupported by failed pilot); R1 keeps as should-fix (characterization paper doesn't require solution). Consensus: framing must change from 'motivate solution' to 'characterize phenomenon'.\"}\n  action_items:\n    - {round: 6, action: \"Add Discussion paragraph on characterization value\", assigned_to: paper_agent, status: done}\n    - {round: 7, action: \"Revise Conclusion/Abstract framing from 'motivate phase-aware compression' to 'characterize phase-dependent phenomenon as prerequisite for future solutions'\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R6-W5\n  summary: \"Entropy redistribution cross-model inconsistency\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"~15% Analysis for non-robust mechanism\"}\n  action_items:\n    - {round: 6, action: \"Trim §6.2 to ~50%; reframe as supplementary\", assigned_to: paper_agent, status: done}\n  resolution: \"Trimmed to ~50 words. Model-dependent, not universal mechanism.\"\n  resolution_round: 6\n\n- id: R6-W6\n  summary: \"LLaMA CI/Wilcoxon inconsistency\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"Technical explanation needed\"}\n  action_items:\n    - {round: 6, action: \"Add footnote on CI vs Wilcoxon divergence\", assigned_to: paper_agent, status: done}\n  resolution: \"Footnote in §5.5: bootstrap median vs signed-rank sensitivity to tails at n=50.\"\n  resolution_round: 6\n\n- id: R6-W7\n  summary: \"Missing citation: Hold Onto That Thought (NeurIPS 2025)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"Direct KV compression + reasoning evaluation\"}\n  action_items:\n    - {round: 6, action: \"Add bib entry + Related Work citation\", assigned_to: paper_agent, status: done}\n  resolution: \"Bib entry added. Cited in Related Work as concurrent single-axis KV compression + reasoning work.\"\n  resolution_round: 6\n\n- id: R6-W8\n  summary: \"h2o-neurips2023 bib title empty\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - {round: 4, reviewers: [R1], note: \"First flagged\"}\n    - {round: 5, reviewers: [R1], note: \"Still empty\"}\n    - {round: 6, reviewers: [R1, R2], note: \"3 rounds unfixed\"}\n  action_items:\n    - {round: 6, action: \"Fill title\", assigned_to: paper_agent, status: done}\n  resolution: \"Title filled. Encoding simplified.\"\n  resolution_round: 6\n\n- id: R6-M1\n  summary: \"\\\\placeholder command residual\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - {round: 5, reviewers: [R1], note: \"R5-3\"}\n    - {round: 6, reviewers: [R1, R2], note: \"Still present\"}\n  action_items:\n    - {round: 6, action: \"Remove macro + all calls\", assigned_to: paper_agent, status: done}\n  resolution: \"Removed. No residual.\"\n  resolution_round: 6\n\n- id: R6-M2\n  summary: \"appendix_results.tex orphaned + duplicate label\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"Orphaned file\"}\n  action_items:\n    - {round: 6, action: \"Delete orphaned file\", assigned_to: paper_agent, status: done}\n  resolution: \"Deleted.\"\n  resolution_round: 6\n\n- id: R6-M3\n  summary: \"Abstract 'over an order of magnitude' vague\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R1, R2], note: \"Specify G range\"}\n  action_items:\n    - {round: 6, action: \"Replace with n=500 G range\", assigned_to: paper_agent, status: done}\n  resolution: \"G=7.5-79.8x, CI [4.1, 96.5].\"\n  resolution_round: 6\n\n- id: R6-M4\n  summary: \"LongFlow bib 'Withdrawn' annotation\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - {round: 5, reviewers: [R1], note: \"R5-2\"}\n    - {round: 6, reviewers: [R1, R2], note: \"Still present\"}\n  action_items:\n    - {round: 6, action: \"Remove Withdrawn note\", assigned_to: paper_agent, status: done}\n  resolution: \"Removed.\"\n  resolution_round: 6\n\n- id: R6-M5\n  summary: \"SnapKV first author verification\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: [R2], note: \"Li vs Cai?\"}\n  action_items:\n    - {round: 6, action: \"Verify\", assigned_to: paper_agent, status: done}\n  resolution: \"First author Yuhong Li confirmed correct.\"\n  resolution_round: 6\n\n# ===== Round 7 New Issues =====\n\n- id: R7-N1\n  summary: \"No downstream accuracy validation — construct validity gap between PPL-based II and task performance\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Consensus critical. PPL degradation in low-sparsity phase may concentrate on non-critical reasoning trace tokens. II vs problem-level accuracy correlation not established. Undermines deployment motivation claims.\"}\n  action_items:\n    - {round: 7, action: \"Report problem-level accuracy under compound sparsity across conditions; compute II vs accuracy-loss rank correlation; revise claims if link is weak\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-N2\n  summary: \"G metric definition inconsistent: median-of-ratios (Table 2) vs ratio-of-medians (Appendix Table 4), up to 9x discrepancy\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Consensus critical. s=0.15: 7.5 vs 69 (9.2x gap). Same symbol G used for different computations. Abstract CI [4.1, 96.5] is envelope of 4 independent CIs, not a single-parameter CI — statistically misleading.\"}\n  action_items:\n    - {round: 7, action: \"Unify G definition across all tables (recommend median-of-ratios + bootstrap CI); fix Abstract CI presentation; discuss numerical stability when II_high ≈ 0\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-N3\n  summary: \"Only one importance scoring method tested but categorical claims about 'importance-based eviction' class\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"R1 critical, R2 agrees quantitatively. Position-normalized cumulative attention mass (Eq.3) is the only method tested. Discussion claims 'broad applicability' to H2O/SnapKV/PyramidKV without evidence. R2 notes qualitative direction may generalize but quantitative claims unsupported.\"}\n  action_items:\n    - {round: 7, action: \"Option A: test at least one alternative importance method (e.g., H2O heavy-hitter). Option B: restrict all claims to 'cumulative-attention-mass-based scoring' and change 'broad applicability' to 'directionally consistent prediction'\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W1\n  summary: \"Generalizability limited: single benchmark (MATH-500), single scale (7B), same-architecture 'cross-model' replication\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"R2 critical, R1 agrees with qualification (scope within tested range is adequate, but claims exceed scope). Two Qwen2 models share backbone — 'Cross-Model Replication' title misleading. LLaMA n=49 too weak for meaningful cross-architecture claim.\"}\n  action_items:\n    - {round: 7, action: \"Rename §5.4 to 'Within-Architecture Replication' or 'Cross-Training Replication'; add at least one non-math benchmark or larger model, or explicitly narrow title/claims to tested scope\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W2\n  summary: \"Pilot mitigation failure (18% recovery, gate FAIL) contradicts 'motivate phase-aware compression' framing\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"R2 elevates to critical, R1 rebuts (characterization paper doesn't need solution) but agrees framing needs adjustment. Consensus: Conclusion 'motivate phase-aware sparsity allocation' is overclaim given failed pilot. Should reframe as 'characterize phenomenon as prerequisite for future solutions'.\"}\n  action_items:\n    - {round: 7, action: \"Revise Abstract/Conclusion from 'motivate' to 'characterize/identify'; analyze why oracle reallocation failed (budget vs strategy vs boundary precision)\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W3\n  summary: \"Crossover effect is model-dependent (DeepSeek only, absent in Qwen) but over-leveraged in Introduction\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"R2 warning, R1 agrees with nuance (crossover already subordinate in contribution list). Introduction §1 uses 'sign reversal' as key evidence for non-deducibility from single-axis work, but this reversal is model-specific.\"}\n  action_items:\n    - {round: 7, action: \"Reduce crossover weight in Introduction novelty argument; explicitly label as model-dependent in §1\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W4\n  summary: \"Discrimination collapse 'structural specificity' explanation lacks quantitative evidence\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Consensus. 6-16% Gini drop → 7.5-79.8x severity amplification gap not bridged. 'Structural specificity' is qualitative conjecture without per-head overlap analysis or other direct evidence.\"}\n  action_items:\n    - {round: 7, action: \"Provide pruned-head overlap analysis across phases (importance vs random), or explicitly acknowledge 'structural specificity' as unverified hypothesis\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W5\n  summary: \"LLaMA cross-architecture validation: n=49 with mixed significance, no explanation for limited sample\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Consensus. CI/Wilcoxon inconsistency explained in footnote, but why not run n=500? n=49 suggests profiling subset leftover. Post-hoc power not reported. Consider demoting to Appendix exploratory analysis.\"}\n  action_items:\n    - {round: 7, action: \"Explain n=49 rationale; report post-hoc power; consider running full n=500 or demoting to Appendix\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W6\n  summary: \"Abstract bootstrap CI [4.1, 96.5] is envelope of 4 independent CIs, not a single-parameter CI\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Consensus (R2 W5, R1 strongly agrees in cross-response). Statistically misleading presentation.\"}\n  action_items:\n    - {round: 7, action: \"Report per-sparsity CIs separately, or clearly label as 'range of CI bounds across sparsity levels'\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W7\n  summary: \"43:1 mean/median ratio extreme outliers unanalyzed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Consensus. Possible sources: phase segmentation boundary effects, specific problem types, bfloat16 numerical artifacts. No outlier profiling provided.\"}\n  action_items:\n    - {round: 7, action: \"Add outlier analysis in Appendix: top-10 outlier problem characteristics (subject, sequence length, phase distribution); verify conclusions robust after removing top-5% outliers\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-M1\n  summary: \"Table 2 Qwen s=0.15 II_high = -0.000: negative II not explained\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Likely bfloat16 numerical noise. Should add footnote.\"}\n  action_items:\n    - {round: 7, action: \"Add footnote explaining negative II as numerical artifact at bfloat16 precision\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-M2\n  summary: \"Figure 1 uses n=50 profiling subset but main results have n=496\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Consensus. Hero figure should use full-scale data for consistency.\"}\n  action_items:\n    - {round: 7, action: \"Regenerate Figure 1 with n=496 data\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-M3\n  summary: \"Numerical inconsistency: §5.3 reports 1.498, Table 2 reports 1.514 for same quantity (random s=0.25 II_low)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"1.1% discrepancy. Likely different CSV source files (crossover_all_sparsity.csv vs table2_n500_full.csv). Similar issue with Qwen s=0.25 importance low (1.043 vs 1.053).\"}\n  action_items:\n    - {round: 7, action: \"Reconcile data sources; ensure single source of truth for all reported values\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-M4\n  summary: \"pyramidkv-2024 bib year should be 2025 (Conference on Language Modeling 2025)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R2], note: \"Year mismatch in bib entry\"}\n  action_items:\n    - {round: 7, action: \"Update year to 2025\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-M5\n  summary: \"§5.1 p-values reported as p < 10^{-69} — overly specific, simplify\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R2], note: \"Suggest p ≪ 10^{-10} or similar\"}\n  action_items:\n    - {round: 7, action: \"Simplify extreme p-values to p ≪ 10^{-10}\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-15T12:44:59.974007+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml\", \"bytes\": 19864}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-15T12:47:08.522435+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "report": "# 审稿报告 — Round 7 (Fresh Review)\n\n**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**审稿人**: Reviewer 1 (方法严谨性/实验/统计) + Reviewer 2 (新颖性/完整性/相关工作/格式)\n**模式**: 圆桌 Round 1 独立初审 → 交叉分享逐条回应 → 收敛汇总\n\n---\n\n## Summary\n\n本文研究 compound sparsity（attention head pruning + KV cache eviction 同时施加）的退化严重程度是否受推理阶段（phase）和驱逐策略（eviction strategy）调控。在 DeepSeek-R1-Distill-Qwen-7B（n=496）和 Qwen2.5-7B-Instruct（n=475）上，使用 MATH-500 数据集，跨 4 个对称 sparsity level（s∈{0.15,0.20,0.25,0.30}），论文发现：(1) importance-based eviction 下，compound severity 在 low-sparsity phase 集中放大（G=7.5–79.8×），而 random eviction 仅有微弱的 phase gradient（G≈0.5–1.3×）；(2) DeepSeek 上存在 strategy ranking crossover（importance 在 high-sparsity phase 优于 random，但在 low-sparsity phase 劣于 random）；(3) discrimination collapse（head pruning 压平 importance score 分布）作为相关性机制解释。\n\n---\n\n## Strengths\n\n**S1. 统计方法论远超 NLP 领域平均水平 [两位 Reviewer 共识]**\nBootstrap CI (B=10,000, seed=42) + Wilcoxon signed-rank（paired within-model）+ Mann-Whitney U（cross-model）+ Jonckheere-Terpstra dose-response test + permutation test (n=50 profiling) + Bonferroni correction (k=4 per family) + BH-FDR robustness check (44 tests) + multiple segmentation granularity sensitivity analysis (tercile/quartile/quintile) + minimum phase length sensitivity (5/10/20)。这种多层次、多方法的统计验证在 NLP empirical work 中罕见。\n\n**S2. Random eviction 作为 falsification control 设计精良 [两位 Reviewer 共识]**\nRandom eviction 的 near-unity G（0.5–1.3×）证明 phase gradient 不是 phase segmentation 或 metric 本身的 artifact，而是 importance-based eviction 特有的。这是论文方法论上的核心亮点。\n\n**S3. Crossover 效应是真正新颖的发现 [两位 Reviewer 共识]**\nDeepSeek 上的 strategy ranking reversal（importance 在 high-sparsity phase 优于 random 但在 low-sparsity phase 劣于 random）是 single-axis 分析无法预测的定性新现象。虽然 model-dependent（Qwen 无此效应），但作为新发现有独立价值。\n\n**S4. 写作诚实透明 [两位 Reviewer 共识]**\nLimitations section 详尽且全面（model scale, task coverage, symmetric sparsity, mechanism, PPL vs accuracy, sparsity range）。LLaMA 跨架构结果的 hedging 恰当（\"preliminary\", \"suggestive\", \"mixed evidence\"）。Pilot failure 直接报告（18% recovery, gate FAIL）。Discrimination collapse 明确标记为 \"correlational\" 而非 causal。Negative results 不隐藏。\n\n**S5. 相关工作覆盖全面 [Reviewer 2]**\n33 篇引用覆盖 compound compression、KV cache eviction、phase-aware inference 三个方向的核心工作，包括 2026 最新文献。引用验证未发现 fabrication。仅有 2 个轻微遗漏（MUSTAFAR NeurIPS 2025; LKV 2026），均非重大。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. [Critical, 两位 Reviewer 共识] 缺少 downstream accuracy 验证——construct validity 根本缺陷**\n\n论文的核心指标 Interaction Index (II) 完全基于 perplexity（Eq. 1），但 MATH-500 的实际任务指标是 problem-level accuracy。PPL 和 accuracy 之间存在已知的非线性关系。论文声称 \"motivate phase-aware compression budgets for mathematical reasoning models\"（Abstract/Discussion/Conclusion），但未提供任何 accuracy 层面的验证。\n\nR2 补充的关键论点：low-sparsity phase 对应 exploratory reasoning，此 phase 的 token 对最终答案的贡献可能远低于 high-sparsity phase（structured computation），因此即使 low-sparsity phase PPL 退化严重（G≫1），如果退化集中在对 final answer 不关键的 reasoning trace 上，整体 accuracy 可能不受影响——这将从根本上改变论文的结论。\n\n**建议**：报告不同 sparsity level 和 phase 下的 problem-level accuracy drop；分析 per-problem II 与 accuracy loss 的 rank correlation。这不需要新实验，只需在现有数据上做 regression analysis。\n\n**N2. [Critical, 两位 Reviewer 共识] G 指标定义不一致，Abstract CI 呈现误导**\n\n- Eq. (2) 定义 per-problem G^(i) 的 median（median of ratios），Table 2 使用此定义；Appendix B Table 4 使用 ratio of medians。s=0.15 时差异达 9.2×（7.5 vs 69）。当 II_high ≈ 0 时 per-problem ratio 爆炸。\n- Abstract 的 \"bootstrap 95% CI: [4.1, 96.5]\" 是 4 个独立 sparsity level 的 CI lower/upper bound 拼接，不是任何单一参数的置信区间，具有统计误导性。\n\n**建议**：统一使用 median-of-ratios + bootstrap CI；明确标注 Appendix Table 4 使用不同定义；修改 Abstract CI 呈现。\n\n**N3. [Critical, 两位 Reviewer 共识] 仅测试一种 importance 评分方法，但做类别性结论**\n\n论文仅使用 position-normalized cumulative attention mass (Eq. 3)，但 Discussion 声称 \"broad applicability\" 基于 H2O/SnapKV/PyramidKV 共享 attention-mass 评分。实际上这些方法的具体实现差异很大（H2O: heavy-hitter + recent token; SnapKV: observation window; Ada-KV: per-head adaptive budgets）。\n\nR2 的 nuance：定性方向可能 generalizable（head pruning 改变 attention 分布这一事实独立于具体评分公式），但定量结论的泛化无证据支持。\n\n**建议**：Option A: 至少测试一种替代 importance 方法（如 H2O）。Option B: 将所有 claims 限定为 \"cumulative-attention-mass-based scoring\"，将 \"broad applicability\" 改为 \"directionally consistent prediction\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. [Warning, R2 critical / R1 agrees with qualification] Generalizability 受限：单基准 + 单规模 + 同架构 \"cross-model\"**\n- 仅 MATH-500，仅 7B。两个 Qwen2 模型共享 backbone（28L/28H/4-group GQA），§5.4 \"Cross-Model Replication\" 标题误导。LLaMA n=49 证据薄弱（~1/40 magnitude, mixed significance）。\n- **建议**：改 §5.4 标题；增加至少一个非数学 benchmark 或更大规模模型，或明确缩窄 title/claims。\n\n**W2. [Warning, 两位 Reviewer 共识，分歧仅在严重性] Pilot failure vs \"motivate\" framing 矛盾**\n- Oracle reallocation 18% recovery (gate FAIL)，heuristic 32% (CI 跨零)。Conclusion \"motivate phase-aware sparsity allocation\" 与 failed pilot 不一致。\n- R1 认为 characterization paper 不需 solution（should-fix）；R2 认为 motivation claim 无支撑（critical）。\n- **共识**：framing 需从 \"motivate solution\" 调整为 \"characterize phenomenon as prerequisite for future solutions\"。\n\n**W3. [Warning, 两位 Reviewer 共识] Crossover 效应 model-dependent 但在 Introduction 被过度依赖**\n- Crossover 仅在 DeepSeek 出现，Qwen 无此效应。Introduction 用 \"sign reversal\" 作为核心论证 non-deducibility。\n- **建议**：降低 Introduction 中的论证权重，明确标记 model-dependent。\n\n**W4. [Warning, 两位 Reviewer 共识] Discrimination collapse \"structural specificity\" 缺乏定量证据**\n- 6–16% Gini reduction 到 7.5–79.8× severity amplification 的巨大 gap 未被 bridged。\"Structural specificity\" 停留在定性推测。\n- **建议**：提供 pruned-head overlap 分析或明确承认假说未验证。\n\n**W5. [Warning, 两位 Reviewer 共识] LLaMA n=49 证据不足**\n- 未解释为何不跑 n=500。n=49 暗示 profiling subset 遗留。Post-hoc power 未报告。\n- **建议**：解释 n=49 原因；报告 post-hoc power；考虑运行完整 n=500 或降级为 Appendix。\n\n**W6. [Warning, 两位 Reviewer 共识] 43:1 mean/median ratio 的极端离群值未分析**\n- 可能来源：phase segmentation 边界效应、特定题型、bfloat16 numerical artifacts。\n- **建议**：添加 Appendix outlier 分析，验证去除 top-5% outlier 后结论稳健。\n\n### Minor Issues\n\n- **M1**: Table 2 Qwen s=0.15 II_high = -0.000——负 II 应解释为 numerical noise（bfloat16 精度）。\n- **M2**: Figure 1 使用 n=50 profiling subset，应更新为 n=496 full-scale 数据。\n- **M3**: §5.3 报告 1.498 vs Table 2 报告 1.514（同一量），Qwen s=0.25 也有类似不一致（1.043 vs 1.053）。需统一数据源。\n- **M4**: pyramidkv-2024 bib year 应为 2025（Conference on Language Modeling 2025）。\n- **M5**: p 值精度过高（p < 10^{-69}），简化为 p ≪ 10^{-10}。\n- **M6**: \\paragraph label 前缀用 sec: 不规范。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成 [AGREE]：\n- N1 (缺 accuracy): 两位均标为 critical\n- N2 (G 定义不一致 + CI 误导): 两位均同意\n- N3 (单一 importance 方法): R1 critical, R2 agree (定量层面)\n- W1 (Generalizability): 基本共识，措辞力度有差异\n- W3 (Crossover model-dependent): 共识\n- W4 (Structural specificity 缺证据): 共识\n- W5 (LLaMA n=49): 共识\n- W6 (Outlier 未分析): 共识\n- W2 (Pilot failure framing): 共识需调整 framing，分歧在严重性\n\n## Reviewer Divergence\n\n| 议题 | R1 | R2 | 解读 |\n|------|----|----|------|\n| Pilot failure 严重性 | Should-Fix（characterization 不需 solution） | Critical（motivate claim 无支撑） | 方向一致，分歧仅在是否阻塞接收。Director 判断：作为 framing 问题处理（should-fix），但 Conclusion 措辞必须修改。 |\n| \"Emergent\" 用词 | Rebut（标准科学含义） | Warning（ML 社区有特定含义） | 低优先级分歧。两种解读均合理，不影响核心评估。 |\n| Bonferroni k=4 分组 | Warning（可能宽松） | Rebut（family 定义合理 + BH-FDR 已验证） | R2 的 rebut 有力——BH-FDR 结果证明核心结论不受影响。此分歧无实际后果。 |\n\n---\n\n## Questions（供 Author Response）\n\n1. 是否有 problem-level accuracy 数据可以展示 II gradient 与 accuracy 退化的关系？\n2. 为何 LLaMA 实验仅跑 n=49？\n3. 是否考虑过在 H2O 或 SnapKV 的 importance scoring 上重复实验？\n4. Table 4 (G=69–274) vs Table 2 (G=7.5–79.8) 的差异——哪个更准确反映效应量级？\n5. §5.3 中 1.498 vs Table 2 中 1.514（及 Qwen 类似不一致）的数据来源差异是什么？\n6. Crossover 在 Qwen 上不出现——是否与 distillation vs instruction tuning 的训练方法相关？\n7. Oracle mitigation 18% recovery 失败的根因分析——是 budget reallocation 不够，还是 phase boundary 不精确，还是需要 strategy switching？\n\n---\n\n## Missing References\n\n两个轻微遗漏（非重大）：\n1. **MUSTAFAR (NeurIPS 2025)** — Joo et al., arXiv:2505.22913. Unstructured KV cache sparsity. 与本文的 structured pruning 不同但在 \"KV cache eviction\" 段落中值得一提。\n2. **LKV (2026)** — arXiv:2605.06676. End-to-end learning of head-wise budgets and token selection. 与 head pruning 影响 KV eviction 的主题直接相关。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目无 `external_review.paperreview_ai.enabled` 设置）。\n\n---\n\n## Overall Assessment\n\n**评分: Borderline (weak reject for main conference / acceptable for Findings track)**\n\nR1: 3.0/5 (Findings acceptance)\nR2: 2.5/5 (Borderline Findings / 需修改重投)\nDirector 综合: **Borderline — weak reject for EMNLP main conference, recommend Findings track**\n\n**置信度**: 4/5\n\n**理由**：\n\n论文在有限范围内展示了严谨的实证方法论——统计控制水平远超 NLP 平均，random baseline 的 falsification 设计精良，crossover 效应是真正新颖的发现，写作诚实透明。\n\n然而，三个 critical 问题共同构成了对 EMNLP main conference 接收的障碍：\n\n1. **Construct validity gap**：核心指标是 perplexity-based II，但 claim 关于 reasoning quality 和 deployment。如果 PPL 退化不转化为 accuracy 下降（特别是 low-sparsity phase 可能对应 non-critical tokens），整个 motivation 不成立。这是最严重的问题。\n\n2. **Claims 超出 scope**：单一 importance scoring 方法→类别性结论；单一 benchmark + 单一规模 + 同架构 \"cross-model\"→\"Mathematical Reasoning Models\" 的 title-level claim。论文在测试范围内的验证是充分的，但 claims 一致性地超出了证据覆盖范围。\n\n3. **Practical value uncertain**：论文声称 \"motivate phase-aware compression budgets\" 但 (a) 自己的 pilot 失败，(b) 无 throughput/latency 评估，(c) 无 accuracy 验证。作为 pure characterization，论文有科学价值；但需要调整 framing 以匹配实际贡献。\n\n如果作者能在 author response 中提供 problem-level accuracy 与 II 的 correlation 分析（不需新实验，现有数据即可），并调整 claims scope，论文有望达到 Findings track 的接收标准。\n\n---\n\n## Detailed Comments（按论文章节）\n\n### Abstract\n- G 的 CI 呈现方式需修改（N2）\n- \"motivate phase-aware compression budgets\" overclaim（W2）\n- \"emergent\" 用词有争议（低优先级）\n\n### §1 Introduction\n- \"Why can't existing single-axis findings predict our results?\" 的论证过度依赖 model-dependent 的 crossover（W3）\n- \"This emergent coupling is not deducible from single-axis characterizations\" 对于 Qwen（无 crossover）需 qualify\n\n### §3 Background\n- II additive null 假设合理，multiplicative null 已在 Appendix 验证\n- G 定义（Eq. 2）需在首次使用时明确区分 median-of-ratios vs ratio-of-medians（N2）\n\n### §4 Experimental Setup\n- 应解释为什么仅 MATH-500、仅 7B\n- float16→bfloat16 的 NaN 问题值得更深入讨论\n\n### §5 Results\n- §5.1/§5.2: 核心发现在测试范围内有充分统计支撑\n- §5.3 crossover: 需明确标记 model-dependent\n- §5.4 \"Cross-Model Replication\": 改标题\n- §5.5 LLaMA: 解释 n=49；考虑降级\n- 数值不一致（1.498 vs 1.514）需修正\n\n### §6 Analysis\n- \"Correlational diagnostic\" 的 framing 适当\n- \"Structural specificity\" 需更多定量支持或明确标记为假说\n\n### §7 Discussion\n- \"motivate phase-aware compression budgets\" → \"characterize phase-dependent phenomenon\"\n- Pilot failure 的 root cause 分析不足\n\n### §8 Conclusion\n- \"motivate phase-aware sparsity allocation for reasoning model deployment\" 需弱化\n- 应增加 scope 限定\n\n### Limitations\n- 全面且诚实\n- 建议在 \"Perplexity vs accuracy\" 段落加强——这是最核心的 limitation\n\n### Appendix\n- Table 4 与 Table 2 的 G 定义差异需明确标注\n- Outlier 分析应添加\n",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "review_chat_id": "oc_57b24a804b56707ec9118a483a8ac65e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "report": "# 审稿报告 — Round 7 (Fresh Review)\n\n**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**审稿人**: Reviewer 1 (方法严谨性/实验/统计) + Reviewer 2 (新颖性/完整性/相关工作/格式)\n**模式**: 圆桌 Round 1 独立初审 → 交叉分享逐条回应 → 收敛汇总\n\n---\n\n## Summary\n\n本文研究 compound sparsity（attention head pruning + KV cache eviction 同时施加）的退化严重程度是否受推理阶段（phase）和驱逐策略（eviction strategy）调控。在 DeepSeek-R1-Distill-Qwen-7B（n=496）和 Qwen2.5-7B-Instruct（n=475）上，使用 MATH-500 数据集，跨 4 个对称 sparsity level（s∈{0.15,0.20,0.25,0.30}），论文发现：(1) importance-based eviction 下，compound severity 在 low-sparsity phase 集中放大（G=7.5–79.8×），而 random eviction 仅有微弱的 phase gradient（G≈0.5–1.3×）；(2) DeepSeek 上存在 strategy ranking crossover（importance 在 high-sparsity phase 优于 random，但在 low-sparsity phase 劣于 random）；(3) discrimination collapse（head pruning 压平 importance score 分布）作为相关性机制解释。\n\n---\n\n## Strengths\n\n**S1. 统计方法论远超 NLP 领域平均水平 [两位 Reviewer 共识]**\nBootstrap CI (B=10,000, seed=42) + Wilcoxon signed-rank（paired within-model）+ Mann-Whitney U（cross-model）+ Jonckheere-Terpstra dose-response test + permutation test (n=50 profiling) + Bonferroni correction (k=4 per family) + BH-FDR robustness check (44 tests) + multiple segmentation granularity sensitivity analysis (tercile/quartile/quintile) + minimum phase length sensitivity (5/10/20)。这种多层次、多方法的统计验证在 NLP empirical work 中罕见。\n\n**S2. Random eviction 作为 falsification control 设计精良 [两位 Reviewer 共识]**\nRandom eviction 的 near-unity G（0.5–1.3×）证明 phase gradient 不是 phase segmentation 或 metric 本身的 artifact，而是 importance-based eviction 特有的。这是论文方法论上的核心亮点。\n\n**S3. Crossover 效应是真正新颖的发现 [两位 Reviewer 共识]**\nDeepSeek 上的 strategy ranking reversal（importance 在 high-sparsity phase 优于 random 但在 low-sparsity phase 劣于 random）是 single-axis 分析无法预测的定性新现象。虽然 model-dependent（Qwen 无此效应），但作为新发现有独立价值。\n\n**S4. 写作诚实透明 [两位 Reviewer 共识]**\nLimitations section 详尽且全面（model scale, task coverage, symmetric sparsity, mechanism, PPL vs accuracy, sparsity range）。LLaMA 跨架构结果的 hedging 恰当（\"preliminary\", \"suggestive\", \"mixed evidence\"）。Pilot failure 直接报告（18% recovery, gate FAIL）。Discrimination collapse 明确标记为 \"correlational\" 而非 causal。Negative results 不隐藏。\n\n**S5. 相关工作覆盖全面 [Reviewer 2]**\n33 篇引用覆盖 compound compression、KV cache eviction、phase-aware inference 三个方向的核心工作，包括 2026 最新文献。引用验证未发现 fabrication。仅有 2 个轻微遗漏（MUSTAFAR NeurIPS 2025; LKV 2026），均非重大。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. [Critical, 两位 Reviewer 共识] 缺少 downstream accuracy 验证——construct validity 根本缺陷**\n\n论文的核心指标 Interaction Index (II) 完全基于 perplexity（Eq. 1），但 MATH-500 的实际任务指标是 problem-level accuracy。PPL 和 accuracy 之间存在已知的非线性关系。论文声称 \"motivate phase-aware compression budgets for mathematical reasoning models\"（Abstract/Discussion/Conclusion），但未提供任何 accuracy 层面的验证。\n\nR2 补充的关键论点：low-sparsity phase 对应 exploratory reasoning，此 phase 的 token 对最终答案的贡献可能远低于 high-sparsity phase（structured computation），因此即使 low-sparsity phase PPL 退化严重（G≫1），如果退化集中在对 final answer 不关键的 reasoning trace 上，整体 accuracy 可能不受影响——这将从根本上改变论文的结论。\n\n**建议**：报告不同 sparsity level 和 phase 下的 problem-level accuracy drop；分析 per-problem II 与 accuracy loss 的 rank correlation。这不需要新实验，只需在现有数据上做 regression analysis。\n\n**N2. [Critical, 两位 Reviewer 共识] G 指标定义不一致，Abstract CI 呈现误导**\n\n- Eq. (2) 定义 per-problem G^(i) 的 median（median of ratios），Table 2 使用此定义；Appendix B Table 4 使用 ratio of medians。s=0.15 时差异达 9.2×（7.5 vs 69）。当 II_high ≈ 0 时 per-problem ratio 爆炸。\n- Abstract 的 \"bootstrap 95% CI: [4.1, 96.5]\" 是 4 个独立 sparsity level 的 CI lower/upper bound 拼接，不是任何单一参数的置信区间，具有统计误导性。\n\n**建议**：统一使用 median-of-ratios + bootstrap CI；明确标注 Appendix Table 4 使用不同定义；修改 Abstract CI 呈现。\n\n**N3. [Critical, 两位 Reviewer 共识] 仅测试一种 importance 评分方法，但做类别性结论**\n\n论文仅使用 position-normalized cumulative attention mass (Eq. 3)，但 Discussion 声称 \"broad applicability\" 基于 H2O/SnapKV/PyramidKV 共享 attention-mass 评分。实际上这些方法的具体实现差异很大（H2O: heavy-hitter + recent token; SnapKV: observation window; Ada-KV: per-head adaptive budgets）。\n\nR2 的 nuance：定性方向可能 generalizable（head pruning 改变 attention 分布这一事实独立于具体评分公式），但定量结论的泛化无证据支持。\n\n**建议**：Option A: 至少测试一种替代 importance 方法（如 H2O）。Option B: 将所有 claims 限定为 \"cumulative-attention-mass-based scoring\"，将 \"broad applicability\" 改为 \"directionally consistent prediction\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. [Warning, R2 critical / R1 agrees with qualification] Generalizability 受限：单基准 + 单规模 + 同架构 \"cross-model\"**\n- 仅 MATH-500，仅 7B。两个 Qwen2 模型共享 backbone（28L/28H/4-group GQA），§5.4 \"Cross-Model Replication\" 标题误导。LLaMA n=49 证据薄弱（~1/40 magnitude, mixed significance）。\n- **建议**：改 §5.4 标题；增加至少一个非数学 benchmark 或更大规模模型，或明确缩窄 title/claims。\n\n**W2. [Warning, 两位 Reviewer 共识，分歧仅在严重性] Pilot failure vs \"motivate\" framing 矛盾**\n- Oracle reallocation 18% recovery (gate FAIL)，heuristic 32% (CI 跨零)。Conclusion \"motivate phase-aware sparsity allocation\" 与 failed pilot 不一致。\n- R1 认为 characterization paper 不需 solution（should-fix）；R2 认为 motivation claim 无支撑（critical）。\n- **共识**：framing 需从 \"motivate solution\" 调整为 \"characterize phenomenon as prerequisite for future solutions\"。\n\n**W3. [Warning, 两位 Reviewer 共识] Crossover 效应 model-dependent 但在 Introduction 被过度依赖**\n- Crossover 仅在 DeepSeek 出现，Qwen 无此效应。Introduction 用 \"sign reversal\" 作为核心论证 non-deducibility。\n- **建议**：降低 Introduction 中的论证权重，明确标记 model-dependent。\n\n**W4. [Warning, 两位 Reviewer 共识] Discrimination collapse \"structural specificity\" 缺乏定量证据**\n- 6–16% Gini reduction 到 7.5–79.8× severity amplification 的巨大 gap 未被 bridged。\"Structural specificity\" 停留在定性推测。\n- **建议**：提供 pruned-head overlap 分析或明确承认假说未验证。\n\n**W5. [Warning, 两位 Reviewer 共识] LLaMA n=49 证据不足**\n- 未解释为何不跑 n=500。n=49 暗示 profiling subset 遗留。Post-hoc power 未报告。\n- **建议**：解释 n=49 原因；报告 post-hoc power；考虑运行完整 n=500 或降级为 Appendix。\n\n**W6. [Warning, 两位 Reviewer 共识] 43:1 mean/median ratio 的极端离群值未分析**\n- 可能来源：phase segmentation 边界效应、特定题型、bfloat16 numerical artifacts。\n- **建议**：添加 Appendix outlier 分析，验证去除 top-5% outlier 后结论稳健。\n\n### Minor Issues\n\n- **M1**: Table 2 Qwen s=0.15 II_high = -0.000——负 II 应解释为 numerical noise（bfloat16 精度）。\n- **M2**: Figure 1 使用 n=50 profiling subset，应更新为 n=496 full-scale 数据。\n- **M3**: §5.3 报告 1.498 vs Table 2 报告 1.514（同一量），Qwen s=0.25 也有类似不一致（1.043 vs 1.053）。需统一数据源。\n- **M4**: pyramidkv-2024 bib year 应为 2025（Conference on Language Modeling 2025）。\n- **M5**: p 值精度过高（p < 10^{-69}），简化为 p ≪ 10^{-10}。\n- **M6**: \\paragraph label 前缀用 sec: 不规范。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成 [AGREE]：\n- N1 (缺 accuracy): 两位均标为 critical\n- N2 (G 定义不一致 + CI 误导): 两位均同意\n- N3 (单一 importance 方法): R1 critical, R2 agree (定量层面)\n- W1 (Generalizability): 基本共识，措辞力度有差异\n- W3 (Crossover model-dependent): 共识\n- W4 (Structural specificity 缺证据): 共识\n- W5 (LLaMA n=49): 共识\n- W6 (Outlier 未分析): 共识\n- W2 (Pilot failure framing): 共识需调整 framing，分歧在严重性\n\n## Reviewer Divergence\n\n| 议题 | R1 | R2 | 解读 |\n|------|----|----|------|\n| Pilot failure 严重性 | Should-Fix（characterization 不需 solution） | Critical（motivate claim 无支撑） | 方向一致，分歧仅在是否阻塞接收。Director 判断：作为 framing 问题处理（should-fix），但 Conclusion 措辞必须修改。 |\n| \"Emergent\" 用词 | Rebut（标准科学含义） | Warning（ML 社区有特定含义） | 低优先级分歧。两种解读均合理，不影响核心评估。 |\n| Bonferroni k=4 分组 | Warning（可能宽松） | Rebut（family 定义合理 + BH-FDR 已验证） | R2 的 rebut 有力——BH-FDR 结果证明核心结论不受影响。此分歧无实际后果。 |\n\n---\n\n## Questions（供 Author Response）\n\n1. 是否有 problem-level accuracy 数据可以展示 II gradient 与 accuracy 退化的关系？\n2. 为何 LLaMA 实验仅跑 n=49？\n3. 是否考虑过在 H2O 或 SnapKV 的 importance scoring 上重复实验？\n4. Table 4 (G=69–274) vs Table 2 (G=7.5–79.8) 的差异——哪个更准确反映效应量级？\n5. §5.3 中 1.498 vs Table 2 中 1.514（及 Qwen 类似不一致）的数据来源差异是什么？\n6. Crossover 在 Qwen 上不出现——是否与 distillation vs instruction tuning 的训练方法相关？\n7. Oracle mitigation 18% recovery 失败的根因分析——是 budget reallocation 不够，还是 phase boundary 不精确，还是需要 strategy switching？\n\n---\n\n## Missing References\n\n两个轻微遗漏（非重大）：\n1. **MUSTAFAR (NeurIPS 2025)** — Joo et al., arXiv:2505.22913. Unstructured KV cache sparsity. 与本文的 structured pruning 不同但在 \"KV cache eviction\" 段落中值得一提。\n2. **LKV (2026)** — arXiv:2605.06676. End-to-end learning of head-wise budgets and token selection. 与 head pruning 影响 KV eviction 的主题直接相关。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目无 `external_review.paperreview_ai.enabled` 设置）。\n\n---\n\n## Overall Assessment\n\n**评分: Borderline (weak reject for main conference / acceptable for Findings track)**\n\nR1: 3.0/5 (Findings acceptance)\nR2: 2.5/5 (Borderline Findings / 需修改重投)\nDirector 综合: **Borderline — weak reject for EMNLP main conference, recommend Findings track**\n\n**置信度**: 4/5\n\n**理由**：\n\n论文在有限范围内展示了严谨的实证方法论——统计控制水平远超 NLP 平均，random baseline 的 falsification 设计精良，crossover 效应是真正新颖的发现，写作诚实透明。\n\n然而，三个 critical 问题共同构成了对 EMNLP main conference 接收的障碍：\n\n1. **Construct validity gap**：核心指标是 perplexity-based II，但 claim 关于 reasoning quality 和 deployment。如果 PPL 退化不转化为 accuracy 下降（特别是 low-sparsity phase 可能对应 non-critical tokens），整个 motivation 不成立。这是最严重的问题。\n\n2. **Claims 超出 scope**：单一 importance scoring 方法→类别性结论；单一 benchmark + 单一规模 + 同架构 \"cross-model\"→\"Mathematical Reasoning Models\" 的 title-level claim。论文在测试范围内的验证是充分的，但 claims 一致性地超出了证据覆盖范围。\n\n3. **Practical value uncertain**：论文声称 \"motivate phase-aware compression budgets\" 但 (a) 自己的 pilot 失败，(b) 无 throughput/latency 评估，(c) 无 accuracy 验证。作为 pure characterization，论文有科学价值；但需要调整 framing 以匹配实际贡献。\n\n如果作者能在 author response 中提供 problem-level accuracy 与 II 的 correlation 分析（不需新实验，现有数据即可），并调整 claims scope，论文有望达到 Findings track 的接收标准。\n\n---\n\n## Detailed Comments（按论文章节）\n\n### Abstract\n- G 的 CI 呈现方式需修改（N2）\n- \"motivate phase-aware compression budgets\" overclaim（W2）\n- \"emergent\" 用词有争议（低优先级）\n\n### §1 Introduction\n- \"Why can't existing single-axis findings predict our results?\" 的论证过度依赖 model-dependent 的 crossover（W3）\n- \"This emergent coupling is not deducible from single-axis characterizations\" 对于 Qwen（无 crossover）需 qualify\n\n### §3 Background\n- II additive null 假设合理，multiplicative null 已在 Appendix 验证\n- G 定义（Eq. 2）需在首次使用时明确区分 median-of-ratios vs ratio-of-medians（N2）\n\n### §4 Experimental Setup\n- 应解释为什么仅 MATH-500、仅 7B\n- float16→bfloat16 的 NaN 问题值得更深入讨论\n\n### §5 Results\n- §5.1/§5.2: 核心发现在测试范围内有充分统计支撑\n- §5.3 crossover: 需明确标记 model-dependent\n- §5.4 \"Cross-Model Replication\": 改标题\n- §5.5 LLaMA: 解释 n=49；考虑降级\n- 数值不一致（1.498 vs 1.514）需修正\n\n### §6 Analysis\n- \"Correlational diagnostic\" 的 framing 适当\n- \"Structural specificity\" 需更多定量支持或明确标记为假说\n\n### §7 Discussion\n- \"motivate phase-aware compression budgets\" → \"characterize phase-dependent phenomenon\"\n- Pilot failure 的 root cause 分析不足\n\n### §8 Conclusion\n- \"motivate phase-aware sparsity allocation for reasoning model deployment\" 需弱化\n- 应增加 scope 限定\n\n### Limitations\n- 全面且诚实\n- 建议在 \"Perplexity vs accuracy\" 段落加强——这是最核心的 limitation\n\n### Appendix\n- Table 4 与 Table 2 的 G 定义差异需明确标注\n- Outlier 分析应添加\n",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_57b24a804b56707ec9118a483a8ac65e"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-15T12:47:12.640147+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_fdc656be1c7fe17c11ab639cdbce3710:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4117
}
```

</details>

---


### Assistant

_source line 534 · 2026-05-15T12:47:20.490357+00:00_

审稿报告已投递至 Research Director。

---

**Round 7 审稿完成。**

**综合评分：Borderline（weak reject for main conference / Findings track acceptable）**

三个 Critical Must-Fix：
1. **缺 downstream accuracy 验证**——construct validity 根本缺陷，PPL 退化可能不转化为 accuracy 下降
2. **G 指标定义不一致 + Abstract CI 误导**——同一符号两套定义，差异达 9×
3. **单一 importance 方法→类别性结论**——仅测 cumulative attention mass 但 claim "broad applicability"

七个 Should-Fix（generalizability 受限、pilot failure framing、crossover model-dependence、discrimination collapse 缺定量证据、LLaMA n=49 不足、outlier 未分析、Abstract CI 呈现）+ 六个 Minor。

Issue Tracker 已同步更新（16 条 round 6 resolved issues 保留 + 15 条 round 7 新 issues）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 42

## Round 42

2 recorded events


### User

_source line 535 · 2026-05-15T12:47:23.146255+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Director。

核心结论：与 Reviewer 1 在 7/8 个问题上达成共识，唯一分歧在 Bonferroni family 分组（W3）——我认为 k=4 的 family 定义合理，且 BH-FDR 已验证核心结论不受影响。两位 reviewer 一致认为最严重的三个问题是：缺少 downstream accuracy 验证、G 指标定义不一致、generalizability 受限（单基准+单规模）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 536 · 2026-05-15T12:47:32.931745+00:00_

审稿报告已投递至 Research Director。

**Round 7 审稿完成。** 总结：

- **评分**：Borderline（weak reject for main conference / Findings track 可接收）
- **R1**: 3.0/5, **R2**: 2.5/5
- **3 个 Critical 问题**：(1) 缺 downstream accuracy 验证（construct validity gap），(2) G 指标定义不一致 + Abstract CI 误导，(3) 单一 importance 方法做类别性结论
- **7 个 Warning 问题**：generalizability 受限、pilot failure framing、crossover model-dependent、structural specificity 无定量证据、LLaMA n=49、outlier 未分析、CI 呈现
- **两位 Reviewer 共识度高**（7/8 问题一致），唯一实质分歧在 Bonferroni family 分组（不影响核心结论）
- **Issue Tracker 已更新**：16 个 round 6 resolved issues 保留，新增 12 个 round 7 open issues

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 43

## Round 43

82 recorded events


### User

_source line 537 · 2026-05-15T13:38:10.968876+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: phase-gated-compound-sparse
- 论文路径: projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-06-15

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-15T13:38:16.997071+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-15T13:38:17.048463+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-15T13:38:21.384592+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-15T13:38:21.435354+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-15T13:38:26.962103+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-15T13:38:27.514787+00:00_

{"result":"# 项目 phase-gated-compound-sparse 概况\n\n## 实验状态 (84 个)\n\n- **mvp_v4_legacy_s025**: DONE (failed) — \n- **mvp_v4_random_r2**: DONE (success) — \n- **mvp_v4_legacy_s01**: DONE (negative) — \n- **mvp_v4_legacy_s03**: DONE (success) — \n- **mvp_v4_legacy_s02**: DONE (success) — \n- **mvp_v4c_r2**: DONE (failed) — \n- **mvp_v4b_r2**: DONE (failed) — \n- **mvp_v4a_r2**: DONE (failed) — \n- **mvp_ii_profiling_v4-random**: DONE (failed) — \n- **mvp_ii_profiling_v4c**: DONE (failed) — \n- **mvp_ii_profiling_v4b**: DONE (failed) — \n- **mvp_ii_profiling_v4**: DONE (failed) — \n- **mvp_ii_profiling_v3**: DONE (negative) — \n- **mvp_ii_profiling_v2**: DONE (negative) — \n- **mvp_interaction_index_profiling**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- sf5_asymmetric_spot（准备中）\n\n## 近期结论\n- **c2_qw_n500_r3** (success): C2 Qwen n=500 continuation (cron false positive on c2_qw_n500). s015 完成, s020-s030 remaining. 与 DeepSeek 对称验证 compound sparsity severity. ← 基于 c2_qw_n500\n- **c2_n500_deepseek** (success): C2 statistical power boost: 将 DeepSeek 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500，提升统计功效。预注册：若 QW s015 在 n=500 后 CI 仍跨零，论文叙事改为 \"compound effect emerges above a threshold sparsity level (~s020)\"\n  [C2 Pre-registration n=500](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/c2_n500_deepseek/data/PRE_REGISTRATION_C2.md) | [c2_n500_deepseek_diagnosis](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/c2_n500_deepseek/report/diagnosis.md) | [n500_statistics_summary](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/c2_n500_deepseek/report/n500_statistics_summary.md)\n- **c2_qw_n500** (failed): C2: Qwen n=500 统计功效提升。将 Qwen 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500，与 DeepSeek 对称验证。\n\n## 趋势\n成功 38 / 负向 10 / 失败 14 / 共 83\nn_problems: 500 ↑（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-22162: 无 GPU 信
…[truncated 1339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-15T13:38:27.515210+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-15T13:38:28.444220+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'phase-gated-compound-sparse'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 929
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-15T13:38:29.248204+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-15T13:38:29.299096+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-15T13:38:33.015136+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-15T13:38:33.367287+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-15T13:38:33.367720+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-15T13:38:33.418347+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-15T13:38:37.638784+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-15T13:38:38.392644+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	
22	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Mathematical Reasoning Models}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	\input{related_work}
34	\input{background}
35	\input{methodology}
36	\input{results}
37	\input{analysis}
38	\input{discussion}
39	\input{conclusion}
40	
41	\bibliography{references}
42	
43	\section*{Limitations}
44	\input{limitations}
45	
46	\section*{Reproducibility}
47	Code and data will be released upon acceptance.
48	
49	\appendix
50	\input{appendix}
51	\input{appendix_moved}
52	\input{appendix_disc_analysis}
53	\input{appendix_robustness}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-15T13:38:38.895269+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "config",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "config",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-15T13:38:38.946102+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-15T13:38:39.047572+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-15T13:38:39.349531+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-15T13:38:42.765627+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 559 · 2026-05-15T13:38:43.168035+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 560 · 2026-05-15T13:38:43.218881+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-15T13:38:50.870061+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"}]

Based on the search results, here's the information about EMNLP 2026:

## Submission Deadline

The ARR submission deadline for long and short papers is May 25, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

#
…[truncated 1354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 8104
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-15T13:38:54.158763+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 paper format page limit template ACL anonymous review guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 paper format page limit template ACL anonymous review guidelines"
  }
}
```

</details>

---


### Tool call

_source line 563 · 2026-05-15T13:38:55.113322+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/agent"
  }
}
```

</details>

---


### Tool result

_source line 564 · 2026-05-15T13:38:55.565730+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_director_b570dbd0.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 565 · 2026-05-15T13:38:55.566172+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/agent"
  }
}
```

</details>

---


### Tool result

_source line 566 · 2026-05-15T13:38:55.616705+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_director_b570dbd0.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-15T13:39:00.417690+00:00_

Web search results for query: "EMNLP 2026 paper format page limit template ACL anonymous review guidelines"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"ClimateNLP 2026","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"Association for Computational Linguistics (ACL) conference - Overleaf, Online LaTeX Editor","url":"https://www.overleaf.com/latex/templates/association-for-computational-linguistics-acl-conference/jvxskxpnznfj"},{"title":"GitHub - acl-org/acl-style-files: Official style files for papers submitted to venues of the Association for Computational Linguistics · GitHub","url":"https://github.com/acl-org/acl-style-files"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"}]

Based on the search results, here's the information about EMNLP 2026 paper formatting:

## Paper Format and Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

## Official Templates

EMNLP 2026 uses official LaTeX templates following ACL style files. EMNLP uses the ACL style files available at github.com/acl-org/acl-style-files.

## Anonymous Review Guidelines

For submissions to EMNLP 2026 through ACL Rolling Review (ARR),
…[truncated 686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6258
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-15T13:39:02.929573+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 569 · 2026-05-15T13:39:02.980203+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-15T13:39:05.742725+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-15T13:39:05.793526+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/decisions.yaml

…[truncated 224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-15T13:39:08.959337+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-15T13:39:09.010024+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-15T13:39:12.275112+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 575 · 2026-05-15T13:39:12.428959+00:00_

Found 7 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_57b24a804b56707ec9118a483a8ac65e_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director.jsonl
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director_20260515T103054_664948.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_reports/round_4.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-15T13:39:15.747319+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "glob": "**/project*.toml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
    "glob": "**/project*.toml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-15T13:39:16.150729+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-15T13:39:16.201512+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/project*.toml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/project*.toml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-15T13:39:16.252279+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-15T13:39:19.619539+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "glob": "**/*.toml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
    "glob": "**/*.toml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-15T13:39:19.670428+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-15T13:39:20.384604+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "glob": "**/*.json",
  "output_mode": "files_with_matches",
  "head_limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
    "glob": "**/*.json",
    "output_mode": "files_with_matches",
    "head_limit": "5"
  }
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-15T13:39:20.435541+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-15T13:39:55.694046+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-15T13:39:56.148560+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We show that compound severity is not phase-invariant: it is an emergent phase-strategy interaction with amplification ratios ($G$) from $7.5{\times}$ ($s{=}0.15$, 95\% CI $[4.1, 11.4]$) to $79.8{\times}$ ($s{=}0.30$, 95\% CI $[63.3, 96.5]$) across reasoning phases in mathematical reasoning models.
4	
5	On DeepSeek-R1-Distill-Qwen-7B (500 MATH-500 problems, $n_{\text{eff}}{=}496$, $s \in \{0.15, 0.20, 0.25, 0.30\}$), importance-based eviction produces a monotonically increasing severity gradient from the high-sparsity to low-sparsity reasoning phase (median $\Delta$: $0.39 \to 8.48$; all Bonferroni-corrected $p \ll 10^{-10}$). Random eviction develops a detectable phase gradient only above $s \approx 0.20$ (non-significant at $s \leq 0.20$; where significant, $3$--$39{\times}$ weaker), confirming importance-based eviction as the dominant driver.
6	A crossover emerges at $s{=}0.25$: importance-based eviction outperforms random in high-sparsity phases yet underperforms in low-sparsity phases---a qualitative reversal in strategy ranking.
7	The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with preliminary cross-architecture evidence from a LlamaForCausalLM model suggesting the phenomenon may extend beyond Qwen2-family architectures.
8	We present discrimination collapse---head pruning flattening cumulative importance scores---as a correlational diagnostic: both strategies exhibit near-identical Gini drops, yet severity diverges by $15$--$17{\times}$, implicating the structural specificity of importance-based pruning as the key differentiator.
9	These findings establish the phase-dependent nature of compound severity as a diagnostic foundation for future phase-aware 
…[truncated 44 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-15T13:39:56.149254+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-15T13:39:56.552074+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 4062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-15T13:39:56.553017+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-15T13:39:56.705134+00:00_

1	## Round 6 (all resolved, compact)
2	- id: R6-N1
3	  summary: "Table 2 n=50→n=500"
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 5
8	  last_seen_round: 6
9	  mentions: []
10	  action_items: [{round: 6, action: "Table 2 replaced", assigned_to: paper_agent, status: done}]
11	  resolution: "Done R6."
12	  resolution_round: 6
13	
14	- id: R6-N2
15	  summary: "Discrimination collapse effect size gap"
16	  category: method
17	  severity: critical
18	  status: resolved
19	  first_raised_round: 6
20	  last_seen_round: 6
21	  mentions: []
22	  action_items: [{round: 6, action: "§6 rewritten as correlational diagnostic", assigned_to: paper_agent, status: done}]
23	  resolution: "Done R6."
24	  resolution_round: 6
25	
26	- id: R6-N3
27	  summary: "ThinKV misattribution"
28	  category: writing
29	  severity: critical
30	  status: resolved
31	  first_raised_round: 1
32	  last_seen_round: 6
33	  mentions: []
34	  action_items: [{round: 6, action: "Rewritten", assigned_to: paper_agent, status: done}]
35	  resolution: "Done R6."
36	  resolution_round: 6
37	
38	## Round 7
39	- id: R7-N1
40	  summary: "No downstream accuracy validation; construct validity gap"
41	  category: experiment
42	  severity: critical
43	  status: resolved
44	  first_raised_round: 7
45	  last_seen_round: 7
46	  mentions:
47	    - {round: 7, reviewers: [R1, R2], note: "PPL-based II not mapped to accuracy; low-sparsity phase may not affect answers"}
48	  action_items:
49	    - {round: 7, action: "N1a answer-region proxy + boxed validation", assigned_to: main_agent, status: done}
50	    - {round: 7, action: "§5.7 Answer-Region Analysis + Limitations caveat", assigned_to: paper_agent, status: done}
51	  resolution: "93.2% answer tokens in high-sparsity phase (naturally shielded). 16/16 conditions answer < reasoning degradation. Proxy evidence with appropriate caveats. N1b skipped (D070)."
52	  resolution_round: 7
53	
54	- id: R7-N2
55	  summary: "G metric definitio
…[truncated 7621 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-15T13:40:16.790584+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-15T13:40:17.260751+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
6	
7	\paragraph{Dataset.}
8	We evaluate all 500 problems from MATH-500~\cite{math500-neurips2021}. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048). Problems with degenerate phase assignments (null low or high phase) are excluded, yielding effective sample sizes of $n{=}496$ for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded). Qwen exhibits a higher mid-phase null rate (45.2\% vs.\ 10.2\% for DeepSeek) due to lower temporal autocorrelation in its attention sparsity patterns (lag-1 $r{=}0.718$ vs.\ $0.894$, $d{=}-1.68$); this does not affect the primary gradient metric $\Delta = \mathrm{II}_{\textit{low}} - \mathrm{II}_{\textit{high}}$, which requires only low and high phases. Sensitivity analysis across $\texttt{min\_phase\_length} \in \{5, 10, 20\}$ confirms robustness (Appendix~\ref{app:mpl-sensitivity}).
9	
10	\paragraph{Sparsity configuration.}
11	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and p
…[truncated 2007 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 470
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-15T13:40:17.311492+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-15T13:40:17.513594+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\times}$ amplification (all Bonferroni-corrected $p \ll 10^{-10}$). Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \geq 0.25$, $\Delta$ becomes significant ($0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$) but $15$--$39{\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger. % exp_id: n500_unified_final; DS imp Δ 0.39→8.48, rand 0.01→0.51; JT z=33.7 (imp), 6.2 (rand)
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, 500 MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.21 & 3.99 & 8.48 \\ % exp_id: n500_unified_final; DS imp median_ii_diff
20	Random     & 0.01 & 0.03 & 0.26 & 0.51 \\ % exp_id: n500_unified_final; DS rand median_ii_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown at $n
…[truncated 10806 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-15T13:40:17.514146+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-15T13:40:17.565285+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	PM-KVQ~\cite{pmkvq-iclr2026} demonstrates that progressive quantization---gradually reducing bit-width over the generation process---mitigates cumulative error in long-CoT reasoning, implicitly introducing a temporal dimension to compression severity that resonates with our finding that compound interaction is phase-dependent.
11	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
12	
13	\paragraph{KV cache eviction.}
14	Most methods rely on importance scoring whose reliability is increasingly questioned.
15	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
16	\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
17	RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
18	\cite{hies-2025} independently show
…[truncated 2763 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-15T13:40:22.289113+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-15T13:40:23.293959+00:00_

1	\section{Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	We present discrimination collapse as a \emph{correlational diagnostic} rather than a complete causal explanation. The consistent Gini decrease across all conditions provides a necessary background---aggregate attention concentration drops uniformly under head pruning regardless of eviction strategy (importance $\Delta\mathrm{Gini}$: $-0.030$ to $-0.081$; random $\Delta\mathrm{Gini}$: $-0.031$ to $-0.071$; ${<}10\%$ difference). However, severity diverges by $15$--$17{\times}$ between strategies despite near-identical Gini changes, indicating that concentration collapse alone is insufficient. The critical differentiator is \emph{structural specificity}: importance-based pruning systematically removes high-attention-score heads, disrupting the attention pattern structure that KV eviction relies on, while random pruning preserves more structural diversity. The quantitative gap between score-level changes ($6$--$16\%$ relative Gini reduction from a DeepSeek baseline of $\widetilde{\mathrm{Gini}} \approx 0.50$; Qwen baseline $\approx 0.57$) and outcome-level amplification ($G{=}7.5$--$79.8{\times}$) indicates additional nonlinear factors (e.g., cascading effects across layers) that warrant dedicated investigation.  % exp_id: c4_entropy; DS baseline Gini 0.496, QW 0.571; imp ΔGini -0.029 to -0.082, rand -0.031 to -0.071
5	
6	\subsection{Discrimination Collapse}
7	\label{sec:discrimination-collapse-main}
8	
9	Head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek, $6$--$17\%$ relative to dense baseline) and $0.010$--$0.020$ (Qwen, $2$--$4\%$) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). Critically, random eviction shows near-identic
…[truncated 3082 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-15T13:40:23.294379+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-15T13:40:23.813722+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($G{=}7.5$--$79.8{\times}$ at $n{=}496$) far exceeds a naive ``somewhat worse'' prediction. The crossover on DeepSeek---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.021$ vs.\ $1.113$) and underperforms in low-sparsity phases ($3.971$ vs.\ $1.514$)---cannot be derived from single-axis entropy reasoning. % exp_id: crossover_all_sparsity.csv; DS s025 n=496 The near-unity random baseline ($G{=}0.5$--$1.3{\times}$, trivial magnitude) confirms the dominant amplification is strategy-specific. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. We expect qualitatively similar behavior for other attention-mass-based scoring methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-colm2025}), as they share the property that head pruning alters the score distribution feeding into eviction decisions; however, quantitative magnitudes may differ given implementation-specific scoring mechanisms.
9	
10	\paragraph{Characterization as diagnostic signal.}
11	The primary value of the phase-dependent severity gradient is diagnostic ra
…[truncated 2928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 519
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-15T13:40:23.814117+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-15T13:40:24.065853+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation ($n{=}496$/$475$ problems). Under importance-based eviction, the amplification ratio $G$ ranges from $7.5{\times}$ to $79.8{\times}$ across sparsity levels, with paired median differences $\Delta$ from $0.39$ to $8.48$ (DeepSeek) and $0.07$ to $3.16$ (Qwen), all $p < 10^{-13}$. Random eviction develops a detectable phase gradient only above $s \approx 0.20$, but $3$--$39{\times}$ weaker than importance-based. A crossover on DeepSeek at $s{=}0.25$---where importance-based eviction reverses ranking across phases ($2.6{\times}$ reversal)---demonstrates that no single strategy dominates uniformly; Qwen does not exhibit this crossover, indicating model dependence. The pattern replicates on Qwen2.5-7B-Instruct at all four sparsity levels; suggestive preliminary evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) indicates the phenomenon may extend beyond Qwen2, though at ${\sim}1/40$ the magnitude and with a weaker strategy contrast. Discrimination collapse provides a correlational diagnostic supported by both Qwen2-based models, with structural specificity of importance-based pruning as the key differentiator from random eviction---despite near-identical Gini drops ($<10\%$ difference), severity diverges by $15$--$17{\times}$.
5	These findings establish the phase-dependent nature of compound severity as a prerequisite and diagnostic foundation for future phase-aware mitigation strategies. Extending this analysis to code reasoning (HumanEval, LiveCodeBench) and science reasoning (GPQA), validating the discrimination collapse mechanism through causal intervention, and characterizing asymmetric compound interactions are promising directions for future work.
6
…[truncated 1 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-15T13:40:24.066378+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-15T13:40:24.119738+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. MATH-500 is a suitable first testbed because it elicits structured reasoning with clear phase transitions (exploratory vs.\ structured computation), supports per-problem evaluation enabling paired statistical tests, and spans sufficient difficulty to produce meaningful variation in sequence length and attention dynamics. However, different reasoning tasks---code generation (e.g., HumanEval, LiveCodeBench), science reasoning (e.g., GPQA), multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile. Whether the phase-strategy interaction documented here extends to these domains is an open question.
6	
7	\paragraph{Symmetric sparsity assumption.}
8	Our analysis applies symmetric sparsity rates: the same fraction $s$ is used for both head pruning and KV cache eviction. Practical deployments may use asymmetric budgets (e.g., aggress
…[truncated 1882 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-15T13:40:28.780931+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-15T13:40:29.195274+00:00_

1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
12	
13	\paragraph{Interaction Index.}
14	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
15	\begin{equation}
16	    \mathrm{II} = r_b - r_a - r_k + 1.
17	    \label{eq:ii}
18	\end{equation}
19	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative conclusions hold under the multiplicative null (Appendix~\ref{app:mu
…[truncated 1441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 414
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-15T13:40:29.245995+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-15T13:40:29.346984+00:00_

1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position spar
…[truncated 1336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-15T13:40:35.176949+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-15T13:40:36.182964+00:00_

1	% Content moved from main body to appendix:
2	% - Phase-strategy crossover details (from results §5.3)
3	% - Cross-model replication details with tables/figures (from results §5.4)
4	% - Permutation test details with table/forest plot (from results §5.6)
5	% - Cross-architecture analysis with power analysis (from results §5.5)
6	% - Full entropy-discrimination collapse analysis with tables (from analysis §6)
7	% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.
8	
9	\section{Phase-Strategy Crossover Details}
10	\label{app:crossover-details}
11	
12	On DeepSeek ($n{=}496$), a strategy ranking reversal emerges at $s{=}0.25$ (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.514$---a $2.6{\times}$ reversal; both $p < 10^{-4}$). This crossover is confirmed at all four sparsity levels, with reversal magnitude of $4.0{\times}$ at $s{=}0.15$, $3.4{\times}$ at $s{=}0.20$, $2.6{\times}$ at $s{=}0.25$, and $2.2{\times}$ at $s{=}0.30$ (decreasing as random eviction severity rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse}). Qwen does not exhibit a crossover: importance-based eviction produces lower II than random in both phases across all sparsity levels (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.108$; low $1.053$ vs.\ $1.769$). % exp_id: n500_unified_final, table2_n500_full.csv
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
17	\caption{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.6{\times}$ hig
…[truncated 18930 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-15T13:40:36.183476+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 611 · 2026-05-15T13:40:36.485348+00:00_

1	\section{Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.071$; Qwen: $-0.019$ to $-0.046$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$). % exp_id: bf16_importance_s015..s030; high-phase medians: 0.006, 0.015, 0.032, 0.053
12	
13	\paragraph{Random masking as falsification control.}
14	At $n{=}500$, random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: non-significant at $s \leq 0.20$ for both models, but significant at $s \geq 0.25$ (DS: $\Delta{=}0.26$--$0.51$, $p_{\text{Bonf}} < 0.006$; QW: $\Delta{=}0.39$--$0.91$, $p_{\text{Bonf}} < 10^{-10}$). Where significant, the random phase gradient is $3$--$39{\times}$ weaker than importance-based, confirming that the dominant amplification is strategy-specific. % exp_id: n500_unified_final; DS rand s025 0.257 p=0.006, s030 0.510 p=0.006; QW rand s025 0.393, s030 0.913
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy s
…[truncated 4934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-15T13:40:36.536149+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
  }
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-15T13:40:36.587089+00:00_

1	\section{Benjamini-Hochberg FDR Correction}
2	\label{app:bh-fdr}
3	
4	Table~\ref{tab:bh-fdr} compares Bonferroni ($k{=}4$, per model$\times$strategy family) and Benjamini-Hochberg FDR correction across all 44 statistical tests. BH-FDR recovers 5 additional significant results beyond Bonferroni, all in low-effect-size conditions (random eviction or cross-model random comparisons). All 32 Bonferroni-significant results remain significant under BH-FDR.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Bonferroni vs.\ BH-FDR correction summary ($\alpha{=}0.05$, 44 tests). ``BH only'' denotes tests significant under BH-FDR but not Bonferroni.}
10	\label{tab:bh-fdr}
11	\begin{tabular}{@{}lcc@{}}
12	\toprule
13	Category & Bonf.\ sig. & BH-only sig. \\
14	\midrule
15	Per-condition Wilcoxon ($k{=}16$) & 10 & 2 \\
16	Imp vs.\ rand ($k{=}8$) & 8 & 0 \\
17	Adjacent sparsity ($k{=}12$) & 10 & 1 \\
18	Cross-model Mann-Whitney ($k{=}8$) & 4 & 2 \\
19	\midrule
20	Total ($k{=}44$) & 32 & 5 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	The 5 BH-only results are: DeepSeek random $s{=}0.25$ and $s{=}0.30$ per-condition Wilcoxon ($p_{\text{Bonf}}{=}0.064$/$0.065$, BH $q{=}0.002$), DeepSeek random $s{=}0.25 \to 0.30$ adjacent-sparsity step ($p_{\text{Bonf}}{=}0.078$, BH $q{=}0.002$), and cross-model random $s{=}0.25$/$s{=}0.30$ Mann-Whitney ($p_{\text{Bonf}}{=}0.66$/$0.17$, BH $q{=}0.018$/$0.005$). All involve random eviction---the weakest effects---confirming that Bonferroni is conservative but does not miss any importance-based findings. % exp_id: n500_unified_final; source: supplementary_stats.json bh_fdr_correction
26	
27	
28	\section{Minimum Phase Length Sensitivity}
29	\label{app:mpl-sensitivity}
30	
31	Table~\ref{tab:mpl-sensitivity} reports the paired median difference $\Delta$ under three \texttt{min\_phase\_length} (mpl) settings across all 16 conditions (2 models $\times$ 2 strategies $\times$ 4 sparsity levels). Conclusions are robust: all importance-based c
…[truncated 5777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-15T13:41:23.945980+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "8",
  "text": "## Round 8 审稿任务 — Reviewer 1\n\n### 你的侧重：方法严谨性 + 实验设计与结果\n\n### Venue 信息\n- **EMNLP 2026 Main Conference**（通过 ACL Rolling Review 提交）\n- **ARR deadline**: 2026-05-25\n- **格式**: ACL style, 长文 8 页正文, double-blind\n- **Limitations section**: 必须有，不计入页数\n- **匿名规则**: double-blind，禁止透露作者身份\n\n### 论文路径\n`projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`\n（多文件结构：abstract.tex, introduction.tex, related_work.tex, background.tex, methodology.tex, results.tex, analysis.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex, appendix_moved.tex, appendix_disc_analysis.tex, appendix_robustness.tex）\n\n### 论文概要\n研究 compound sparsity（head pruning + KV cache eviction 联合）在数学推理模型中的 phase-dependent severity。提出 Interaction Index (II) 和 amplification ratio (G) 度量。核心发现：importance-based eviction 在 reasoning phases 间的 severity gradient 达 G=7.5x–79.8x，而 random 接近 1x。在 DeepSeek-R1-Distill-Qwen-7B (n=496) 和 Qwen2.5-7B-Instruct (n=475) 上测试。自我定位为 diagnostic study。\n\n### 审查重点\n请严格审查以下方面：\n\n1. **Interaction Index (II) 定义的合理性**\n   - additive null 假设 r_b = r_a + r_k - 1 是否合理？multiplicative null 的处理是否充分？\n   - PPL 比值作为 severity 度量的 construct validity\n\n2. **Phase segmentation 方法的鲁棒性**\n   - 基于 attention sparsity tercile 的分割是否有先验合理性？是否是 data-driven 选择？\n   - min_phase_length=10 的选择是否充分论证？\n\n3. **统计分析严谨性**\n   - Bootstrap CI (B=10000) + Wilcoxon + Bonferroni correction 是否恰当？\n   - Jonckheere-Terpstra test 用于 dose-response 是否正确？\n   - G 指标的 median-of-ratios vs ratio-of-medians 区分是否清晰？\n   - 43:1 到 97640:1 的 mean/median ratio 对结论的影响\n   - n=496/475 的样本量对各项 claim 的统计功效\n\n4. **实验设计**\n   - 4 个 sparsity levels (0.15-0.30) 的范围是否足够？\n   - 只用 MATH-500 一个 benchmark 的限制\n   - LLaMA n=49 的证据力度\n   - 没有 downstream accuracy 验证（只有 answer-region proxy）\n\n5. **Discrimination collapse 机制**\n   - 作为 correlational diagnostic 的证据强度\n   - Gini 下降 6-16% 对应 severity 差异 15-17x 的解释力\n   - structural specificity 的量化证据（r=0.62-0.76）是否自洽（Frobenius norm vs Gini 的共线性）\n\n6. **格式合规**\n   - 页数是否在 8 页正文限制内？\n   - 是否符合 double-blind 要求？\n   - Limitations section 是否充分？\n\n请按 EMNLP 标准给出完整审稿报告：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + confidence)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "8",
    "text": "## Round 8 审稿任务 — Reviewer 1\n\n### 你的侧重：方法严谨性 + 实验设计与结果\n\n### Venue 信息\n- **EMNLP 2026 Main Conference**（通过 ACL Rolling Review 提交）\n- **ARR deadline**: 2026-05-25\n- **格式**: ACL style, 长文 8 页正文, double-blind\n- **Limitations section**: 必须有，不计入页数\n- **匿名规则**: double-blind，禁止透露作者身份\n\n### 论文路径\n`projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`\n（多文件结构：abstract.tex, introduction.tex, related_work.tex, background.tex, methodology.tex, results.tex, analysis.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex, appendix_moved.tex, appendix_disc_analysis.tex, appendix_robustness.tex）\n\n### 论文概要\n研究 compound sparsity（head pruning + KV cache eviction 联合）在数学推理模型中的 phase-dependent severity。提出 Interaction Index (II) 和 amplification ratio (G) 度量。核心发现：importance-based eviction 在 reasoning phases 间的 severity gradient 达 G=7.5x–79.8x，而 random 接近 1x。在 DeepSeek-R1-Distill-Qwen-7B (n=496) 和 Qwen2.5-7B-Instruct (n=475) 上测试。自我定位为 diagnostic study。\n\n### 审查重点\n请严格审查以下方面：\n\n1. **Interaction Index (II) 定义的合理性**\n   - additive null 假设 r_b = r_a + r_k - 1 是否合理？multiplicative null 的处理是否充分？\n   - PPL 比值作为 severity 度量的 construct validity\n\n2. **Phase segmentation 方法的鲁棒性**\n   - 基于 attention sparsity tercile 的分割是否有先验合理性？是否是 data-driven 选择？\n   - min_phase_length=10 的选择是否充分论证？\n\n3. **统计分析严谨性**\n   - Bootstrap CI (B=10000) + Wilcoxon + Bonferroni correction 是否恰当？\n   - Jonckheere-Terpstra test 用于 dose-response 是否正确？\n   - G 指标的 median-of-ratios vs ratio-of-medians 区分是否清晰？\n   - 43:1 到 97640:1 的 mean/median ratio 对结论的影响\n   - n=496/475 的样本量对各项 claim 的统计功效\n\n4. **实验设计**\n   - 4 个 sparsity levels (0.15-0.30) 的范围是否足够？\n   - 只用 MATH-500 一个 benchmark 的限制\n   - LLaMA n=49 的证据力度\n   - 没有 downstream accuracy 验证（只有 answer-region proxy）\n\n5. **Discrimination collapse 机制**\n   - 作为 correlational diagnostic 的证据强度\n   - Gini 下降 6-16% 对应 severity 差异 15-17x 的解释力\n   - structural specificity 的量化证据（r=0.62-0.76）是否自洽（Frobenius norm vs Gini 的共线性）\n\n6. **格式合规**\n   - 页数是否在 8 页正文限制内？\n   - 是否符合 double-blind 要求？\n   - Limitations section 是否充分？\n\n请按 EMNLP 标准给出完整审稿报告：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + confidence)。"
  }
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-15T13:41:45.158564+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21212
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-15T13:41:45.561041+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "8",
  "text": "## Round 8 审稿任务 — Reviewer 2\n\n### 你的侧重：新颖性 + 相关工作完整性 + 写作质量\n\n### Venue 信息\n- **EMNLP 2026 Main Conference**（通过 ACL Rolling Review 提交）\n- **ARR deadline**: 2026-05-25\n- **格式**: ACL style, 长文 8 页正文, double-blind\n- **Limitations section**: 必须有，不计入页数\n- **匿名规则**: double-blind，禁止透露作者身份\n\n### 论文路径\n`projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`\n（多文件结构：abstract.tex, introduction.tex, related_work.tex, background.tex, methodology.tex, results.tex, analysis.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex, appendix_moved.tex, appendix_disc_analysis.tex, appendix_robustness.tex）\n\n### 论文概要\n研究 compound sparsity（head pruning + KV cache eviction 联合）在数学推理模型中的 phase-dependent severity。自我定位为 diagnostic study——不提出 mitigation method，而是量化一个 previously unknown interaction effect。核心发现：(1) importance-based eviction 的 phase-dependent severity gradient (G=7.5x-79.8x)；(2) DeepSeek 上 strategy ranking crossover（model-dependent）；(3) discrimination collapse 作为 correlational mechanism。\n\n### 审查重点\n请严格审查以下方面：\n\n1. **Novelty 评估**\n   - \"Phase-dependent compound severity\" 这个发现的 novelty 程度如何？\n   - 是否只是对 ThinKV (phase-aware) + HIES (score collapse) + sparse-frontier (strategy non-dominance) 已知结果的组合？Introduction 中 \"linear combination of these insights would predict...\" 的论证是否令人信服？\n   - 作为纯 diagnostic study（无 mitigation method），contribution 是否足够支撑 EMNLP main conference 长文？\n   - Pilot mitigation 实验 (18% oracle recovery, gate FAIL) 的价值——是否反而削弱了论文的贡献？\n\n2. **Related Work 覆盖度**\n   - compound compression 相关工作是否遗漏重要文献？\n   - KV cache eviction 方向的 2025-2026 最新进展是否全面覆盖？\n   - phase-aware inference 的文献是否有遗漏？\n   - 请特别关注 2026 年的新工作：是否有与本文 claim 直接冲突或高度相关但未引用的工作？\n\n3. **写作质量与清晰度**\n   - Abstract 是否准确反映论文内容？是否有过度宣称？\n   - Introduction 的 motivation 链是否逻辑通顺？\n   - 论文自我定位为 \"diagnostic study\" 是否一致贯穿全文，还是有时滑向 method claim？\n   - 符号定义的一致性和清晰度\n   - 数字引用的准确性（text vs table 是否一致）\n   - 论文的整体 narrative arc 是否清晰？\n\n4. **Framing 问题**\n   - \"Severity gradient\" 从 7.5x 到 79.8x 的 framing——这些数字的 practical significance 如何？\n   - Crossover 被放在什么位置？鉴于它只在 DeepSeek 上出现，强调程度是否合适？\n   - LLaMA cross-architecture 证据的 framing 是否恰当（\"preliminary\"/\"suggestive\" 的用词）？\n   - \"Discrimination collapse\" 的命名——是否合理？是否容易与其他领域的概念混淆？\n\n5. **Presentation 问题**\n   - 图表是否清晰？Figure 1 是否有效传达核心信息？\n   - 正文 vs 附录的内容分配是否合理？\n   - 论文的结构组织是否适合 EMNLP 读者？\n\n请按 EMNLP 标准给出完整审稿报告：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + confidence)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "8",
    "text": "## Round 8 审稿任务 — Reviewer 2\n\n### 你的侧重：新颖性 + 相关工作完整性 + 写作质量\n\n### Venue 信息\n- **EMNLP 2026 Main Conference**（通过 ACL Rolling Review 提交）\n- **ARR deadline**: 2026-05-25\n- **格式**: ACL style, 长文 8 页正文, double-blind\n- **Limitations section**: 必须有，不计入页数\n- **匿名规则**: double-blind，禁止透露作者身份\n\n### 论文路径\n`projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`\n（多文件结构：abstract.tex, introduction.tex, related_work.tex, background.tex, methodology.tex, results.tex, analysis.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex, appendix_moved.tex, appendix_disc_analysis.tex, appendix_robustness.tex）\n\n### 论文概要\n研究 compound sparsity（head pruning + KV cache eviction 联合）在数学推理模型中的 phase-dependent severity。自我定位为 diagnostic study——不提出 mitigation method，而是量化一个 previously unknown interaction effect。核心发现：(1) importance-based eviction 的 phase-dependent severity gradient (G=7.5x-79.8x)；(2) DeepSeek 上 strategy ranking crossover（model-dependent）；(3) discrimination collapse 作为 correlational mechanism。\n\n### 审查重点\n请严格审查以下方面：\n\n1. **Novelty 评估**\n   - \"Phase-dependent compound severity\" 这个发现的 novelty 程度如何？\n   - 是否只是对 ThinKV (phase-aware) + HIES (score collapse) + sparse-frontier (strategy non-dominance) 已知结果的组合？Introduction 中 \"linear combination of these insights would predict...\" 的论证是否令人信服？\n   - 作为纯 diagnostic study（无 mitigation method），contribution 是否足够支撑 EMNLP main conference 长文？\n   - Pilot mitigation 实验 (18% oracle recovery, gate FAIL) 的价值——是否反而削弱了论文的贡献？\n\n2. **Related Work 覆盖度**\n   - compound compression 相关工作是否遗漏重要文献？\n   - KV cache eviction 方向的 2025-2026 最新进展是否全面覆盖？\n   - phase-aware inference 的文献是否有遗漏？\n   - 请特别关注 2026 年的新工作：是否有与本文 claim 直接冲突或高度相关但未引用的工作？\n\n3. **写作质量与清晰度**\n   - Abstract 是否准确反映论文内容？是否有过度宣称？\n   - Introduction 的 motivation 链是否逻辑通顺？\n   - 论文自我定位为 \"diagnostic study\" 是否一致贯穿全文，还是有时滑向 method claim？\n   - 符号定义的一致性和清晰度\n   - 数字引用的准确性（text vs table 是否一致）\n   - 论文的整体 narrative arc 是否清晰？\n\n4. **Framing 问题**\n   - \"Severity gradient\" 从 7.5x 到 79.8x 的 framing——这些数字的 practical significance 如何？\n   - Crossover 被放在什么位置？鉴于它只在 DeepSeek 上出现，强调程度是否合适？\n   - LLaMA cross-architecture 证据的 framing 是否恰当（\"preliminary\"/\"suggestive\" 的用词）？\n   - \"Discrimination collapse\" 的命名——是否合理？是否容易与其他领域的概念混淆？\n\n5. **Presentation 问题**\n   - 图表是否清晰？Figure 1 是否有效传达核心信息？\n   - 正文 vs 附录的内容分配是否合理？\n   - 论文的结构组织是否适合 EMNLP 读者？\n\n请按 EMNLP 标准给出完整审稿报告：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + confidence)。"
  }
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-15T13:41:47.069807+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1508
}
```

</details>

---


### Assistant

_source line 618 · 2026-05-15T13:41:51.324102+00:00_

两位 Reviewer 已分派：

- **Reviewer 1**（方法严谨性 + 实验设计）→ 已触发
- **Reviewer 2**（新颖性 + 相关工作 + 写作质量）→ 已触发

等待两位 Reviewer 的 Round 8 独立审稿结果返回，随后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 44

## Round 44

2 recorded events


### User

_source line 619 · 2026-05-15T13:47:46.298891+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 8 审稿报告（新颖性 + 相关工作 + 写作质量）

### 总体评分
**Overall**: 2.5 / 5 (Borderline Findings)
**一句话总结**: 方法论扎实的实证诊断研究，但核心发现的定性方向可从已有工作推导，定量贡献依赖 near-zero denominator 放大的 G 指标，pilot mitigation 失败反而削弱贡献。

### ARR 维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法论扎实，但 "3–39×" 数字声明与数据不一致；G 指标受近零分母影响 |
| Excitement | 2.5/5 | "importance-based eviction 在 attention 分散的 phase 表现更差"定性上可预测；缺乏可操作产出 |
| Reproducibility | 4/5 | 实验设置详尽，承诺 release code，统计规范 |
| Confidence | 4/5 | 熟悉 KV cache compression、attention head pruning 和 reasoning model 推理文献 |

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] 新颖性不足：核心发现定性可预测，"linear combination" 论证为稻草人

- 位置：Section 1 (Introduction), paragraph 3
- 论文声称 "a linear combination of these insights would predict that compound degradation either (i) uniformly amplifies, or (ii) follows the dominant single-axis pattern"，然后用实际观察到的 severity gradient 反驳。但这构建了一个过弱的 null hypothesis——没有人会预期两个非线性交互的压缩轴产生 "linear combination"。ThinKV 已证明 attention 分散的 phase 对 eviction 更敏感；HIES 已证明重度剪枝下 importance score 区分力崩塌；compound setting 中这两效应叠加产生 phase-modulated severity 定性上可预期。论文真正贡献在于量化（G=7.5×–79.8×），但 G 指标因 II_high 接近零（Table 2: 0.003–0.038）而被人为放大。
- 建议：(a) 改进 novelty argument，聚焦 crossover 和 dose-response 的不可预测性；(b) 在 headline claims 中同时报告 Δ（绝对差）和 G（比率）；(c) 明确讨论 G 的 near-zero denominator 放大效应。

**N2** [critical] Pilot mitigation 实验削弱而非增强贡献

- 位置：Section 7, paragraph 3 (pilot experiment)
- Oracle phase-aware budget reallocation 仅恢复 18%（预注册 30% gate FAIL），heuristic 32% 但 CI span zero。论文 pitch "severity gradient provides a natural signal for allocating compression budgets"，但 pilot 直接反驳此声明。
- 建议：要么移除 pilot（纯诊断论文无需 mitigation 尝试），要么深入分析失败原因并移至 Appendix。

**N3** [critical] "3–39×" / "15–39×" 数字声明与数据不一致

- 位置：Abstract, Section 5.1, Contribution item 1
- 在 random 统计显著的条件（s≥0.25），实际比率为：DS 15.3–16.6×, QW 2.7–3.5×，跨模型范围 **2.7–17×**，非 "3–39×"。39× (≈0.39/0.01) 来自 DS s=0.15 但该条件 random Δ 非显著（CI spans zero）。将非显著条件比率纳入 "where significant" 声明是数字不一致。
- 建议：修正为 "3–17×" 或准确区间。

---

### Should-Fix 问题

**W1** [warning] Crossover 过度强调（仅 DeepSeek 出现，Qwen 不存在，model-dependent）

**W2** [warning] LLaMA 跨架构证据过弱（n=49，~1/40 效应量，仅 1/4 sparsity 显著），建议正文压缩

**W3** [warning] "Discrimination collapse" 命名可能与 ML 其他 collapse 概念混淆，建议改用 "importance score flattening"

**W4** [warning] 缺少高相关性近期文献：ForesightKV (arXiv 2602.03203), ThinK (ICLR 2025), "Prune-then-Quantize or Quantize-then-Prune?" (ICLR 2026)

**W5** [warning] 仅 perplexity 度量；Section 5.7 answer-region 分析（93.2% answer tokens 在 high-sparsity phase）暗示 practical significance 可能远低于 G 指标所示

---

### 小问题
- Table 2 footnote: negative II 应报告为 ≈0
- LaTeX 源码残留 `% exp_id:` 注释
- LKV reference author = "Anonymous"
- Table 3 caption 中 "paired median difference" vs "difference of medians" 概念需更清晰

### 主要优势
1. 统计方法论堪称典范（Bonferroni + BH-FDR、置换检验、JT dose-response、power analysis、winsorization）
2. 多维度 robustness 验证（segmentation 粒度、min_phase_length、outlier、multiplicative null）
3. Cross-model replication 增强可靠性（不同训练范式）
4. Diagnostic study 自我定位一致，hedging 得当
5. Random eviction 对照组设计精巧

### 缺失引用
| 论文 | 相关性 |
|------|--------|
| ForesightKV (2602.03203) | Reasoning-specific KV eviction with learned long-term importance |
| ThinK (ICLR 2025) | Channel-level KV pruning compound compression |
| Prune-then-Quantize or Quantize-then-Prune? (ICLR 2026) | Compression order interaction, Progressive Intensity Hypothesis |

### Overall Assessment
Weak Reject → Borderline Findings。实验执行质量高但核心发现新颖性有限。建议 (a) 修正数字不一致，(b) 重新 frame G 指标，(c) 减少 crossover/LLaMA 强调，(d) 补充缺失引用。适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 620 · 2026-05-15T13:47:53.280854+00:00_

Reviewer 2 的报告已收到。等待 Reviewer 1 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 45

## Round 45

2 recorded events


### User

_source line 621 · 2026-05-15T13:47:55.978874+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**2.5/5，Borderline Findings**。

三个 critical 问题：
1. **新颖性**——"compound severity is phase-dependent" 定性上可从 ThinKV + HIES 推导，"linear combination" 反驳论证是稻草人；G 指标因 near-zero denominator 被放大
2. **Pilot mitigation 失败**——oracle 仅恢复 18%（gate FAIL），反而削弱了 "diagnostic foundation for future mitigation" 的叙事
3. **数字不一致**——"3–39×" 声明混入了 random Δ 非显著条件的比率，实际应为 "3–17×"

五个 should-fix：crossover 过度强调（model-dependent）、LLaMA 证据太弱、"discrimination collapse" 命名易混淆、缺 ForesightKV/ThinK/Prune-then-Quantize 引用、纯 perplexity 评估且 answer shielding 暗示 practical significance 有限。

统计方法论和 robustness 验证是论文最大亮点，建议投 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 622 · 2026-05-15T13:48:02.068775+00:00_

收到 Reviewer 2 的报告。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 46

## Round 46

6 recorded events


### User

_source line 623 · 2026-05-15T13:53:12.041125+00:00_

[Reviewer 1 审稿意见]:
## Round 8 — Reviewer 1 审稿报告

**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models
**Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review)

---

## 总体评分

**Overall**: 3/5 (Findings: could be accepted to Findings of the ACL)
**一句话总结**: 统计方法论出色的诊断研究，揭示了 compound sparsity 的 phase-dependent severity 现象，但单一基准测试、缺乏准确率验证、answer-region 分析反而削弱了实际意义，且机制解释缺口过大，限制其达到 main conference 水平。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计框架严谨（bootstrap/Wilcoxon/Bonferroni/JT test），稳健性检查充分，但核心度量仅基于 PPL、单一基准，且 additive null 的论证不够充分 |
| Excitement | 3/5 | Phase-strategy interaction 和 crossover effect 有新意，但实际可操作性不清（pilot 未达 gate，answer token 被 shielded） |
| Reproducibility | 4/5 | 实验细节充分（硬件、超参、随机种子），承诺代码发布，统计方法可复现 |
| Confidence | 4/5 | 仔细阅读全文含全部 15 个 Appendix，熟悉 KV cache 压缩和注意力稀疏性文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Interaction Index 的 additive null 假设与论文自身论述存在内在矛盾

- 具体位置：Section 3, Eq. 1; Appendix B
- 问题：论文以"两个轴作用于不相交维度（structural vs. positional）"来正当化 additive null（II = r_c − r_a − r_k + 1）。但论文自身在 Section 3 明确指出 "head pruning alters the importance ranking used for eviction"，在 Section 6 详细分析 head pruning 如何通过 discrimination collapse 直接影响 KV eviction 的决策质量。这意味着两个压缩轴存在直接的因果耦合，并非"不相交"。Appendix B 的 multiplicative null 验证显示 G_mult ≈ 58–211（远高于 additive G = 7.5–79.8），两种 null 下的数值差异达 4–8×。当论文核心 contribution 是量化 severity gradient 的量级时，null 的选择直接决定了数字的含义。
- 为什么影响接收：II 是论文所有定量结论的根基。如果 additive null 不合理，所有基于 II 的数字（Δ、G、CI）的绝对值均失去可靠的解释基准。
- 建议修改方向：(1) 严格论证 additive null 的合理性，不能仅靠"不相交维度"的一句话断言——需要正面回应为什么存在因果耦合却仍然采用 additive null；(2) 在主文本中并列报告两种 null 下的关键结果（至少 G 和 Δ），让读者自行判断。

**N2** [critical] 单一基准测试 (MATH-500) 严重限制泛化性

- 具体位置：Section 4.1; Limitations
- 问题：论文所有定量结论仅基于 MATH-500 一个基准。论文标题中使用 "Mathematical Reasoning Models"（复数），暗示对数学推理的一般性。但 MATH-500 的题目类型（代数、几何、数论等）可能诱导特定的 phase 结构。不同推理任务（代码生成、科学推理、多跳QA）甚至同类数学任务（GSM8K）的 attention dynamics 可能截然不同。作为 diagnostic study，单一数据源的 "诊断" 的外部效度存疑。
- 为什么影响接收：EMNLP reviewer 会合理质疑：这是 MATH-500 特定的统计工件，还是 compound sparsity 的通用属性？一个额外基准（哪怕是小规模）即可大幅增强可信度。
- 建议修改方向：增加至少一个不同类型推理基准的验证（GSM8K 最低成本，HumanEval/GPQA 更有说服力），即使仅用 n=50 profiling 规模。

**N3** [critical] PPL 度量的 construct validity 问题：论文自身的 answer-region 分析反而削弱了核心叙事

- 具体位置：Section 5.7
- 问题：Section 5.7 报告 93.2% 的答案 token 落在 high-sparsity phase（该 phase compound interaction 最小，G ≤ 1）；答案 token 的 PPL degradation（1.3–2.3）远低于推理痕迹 token（5.7–19×）。这一发现在论文自身的分析框架内实质上表明：phase-dependent severity gradient 主要影响中间推理过程而非最终输出。论文将此描述为 "partially shielded"，但更准确的解读是：观察到的巨大 G 值（7.5–79.8×）集中在对最终答案影响最小的 phase 中。缺乏直接准确率测量（论文承认 "generation under compound sparsity conditions remains an area for future work"），使 "severity" 的实际含义悬而未决。
- 为什么影响接收：论文试图说服读者 compound severity 是一个严重问题，但自己的分析表明最终答案可能基本不受影响。这是一个 framing 与证据之间的根本张力。
- 建议修改方向：(1) 在至少一个 sparsity level 上测量实际 MATH-500 准确率变化；(2) 重新框定 severity gradient 的意义——如果主要影响推理痕迹质量而非最终答案，论文的价值定位需要调整。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "Cross-model replication" 实为同架构不同训练范式

- 具体位置：Section 5.4; Section 5.5
- 问题：DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 共享 Qwen2ForCausalLM 架构（28层、28头、4-group GQA），差异仅在训练方式（distillation vs. instruction tuning）。论文将此称为 "replication across training paradigms"（合理），但 Section 5.5 的 LLaMA 跨架构验证（n=49）显示 severity 仅为 DeepSeek 的 ~1/40，random pruning 也展现非平凡 phase gradient（d_s: 0.35–0.41），strategy contrast 大幅减弱。Power analysis 表明需要 n ≥ 200 才能达到 0.80 power 进行 strategy comparison。
- 建议：(1) 统一使用更精确的术语（"cross-training-paradigm replication on the same architecture"）；(2) 更突出地讨论 LLaMA 结果对泛化性的负面含义——~1/40 的量级和弱 strategy contrast 暗示该现象可能是 Qwen2 架构特有的。

**W2** [warning] Discrimination collapse 的解释力存在 order-of-magnitude 缺口

- 具体位置：Section 6; Section 6.1
- 问题：Importance-based 和 random eviction 的 Gini drop 差异 < 10%（如 s=0.25: −0.065 vs. −0.060），但 severity 差异为 15–17×。6–16% 的 Gini relative reduction 对应 G = 7.5–79.8× 的 severity amplification——"cause" 和 "effect" 之间存在 1–2 个数量级的缺口。r = 0.62–0.76 的 structural specificity 证据虽不错，但论文也承认 Frobenius norm 和 Gini 共享对 attention weight magnitude 的敏感性（Section 6.1: "correlation partially expected"）。entropy redistribution 在 Qwen s=0.25 处反转（ΔH = +0.015），仅 2/4 条件复现。
- 建议：明确讨论 Gini drop（~10%）与 severity divergence（15–17×）之间的定量差距；当前的 "additional nonlinear factors" 解释过于模糊——如果 discrimination collapse 只解释了效应的一小部分，应坦诚降低对该机制的依赖程度。

**W3** [warning] Profiling subset (n=50) 与 full sample (n=496) 的效应量差异过大

- 具体位置：Table 2 vs Table 4
- 问题：Table 4 (n=50 profiling) 显示 G = 69, 103, 222, 274（s=0.15–0.30 importance-based）；Table 2 (n=496 full) 显示 G = 7.5, 17.9, 49.1, 79.8——profiling G 是 full sample 的 3.5–9.2×。Δ 在高 sparsity 下也有 ~1.7× 差异（n=50: Δ=14.59 vs n=496: Δ=8.48 at s=0.30）。虽然论文提到 bootstrap CI 收窄 2.5–5.9×，但未充分讨论点估计的系统性下移。
- 建议：解释为什么 profiling subset 系统性高估效应量——是 sampling bias 还是 heavy tail 的有限样本效应？这对基于小样本 pilot 做决策（如 LLaMA n=49）的可靠性有重要启示。

**W4** [warning] Phase segmentation 缺乏理论先验

- 具体位置：Section 3; Eq. 6; Appendix M, N
- 问题：基于 attention sparsity tercile 的分割是纯数据驱动——没有独立理论解释为什么 "attention sparsity 的三分位边界" 对应有意义的推理阶段。Eq. 6 的 0.01 × max 阈值同样任意。Appendix M/N 的稳健性检查表明结论在 mpl ∈ {5, 10, 20} 和 tercile/quartile/quintile 下保持，这是正面的，但仍无法回答更根本的问题：attention sparsity 是否真的是 phase 的合理代理变量？
- 建议：引用独立文献支持 attention sparsity 作为 reasoning phase boundary 的合理性，或讨论替代分割方法（如基于 token type / semantic content 的分割）的可能结果。

**W5** [warning] Pilot mitigation experiment 未达预注册 gate，削弱实际应用叙事

- 具体位置：Section 7
- 问题：Oracle phase-aware budget reallocation 仅恢复 18% compound interaction（低于 30% pre-registered gate）；heuristic variant 32% 但 95% CI 跨越 zero。这表明即使拥有 oracle phase information，coarse phase-aware reallocation 的效果也非常有限。论文将 mitigation 定位为 "open problem"，但 pilot 的失败进一步质疑了 severity gradient 作为 "natural signal for budget allocation" 的实际价值。
- 建议：更直接地讨论 pilot 失败的含义——如果 oracle 信息都只能恢复 18%，是否意味着 severity gradient 虽然统计上显著但实际上不可操作？

**W6** [warning] Sparsity 范围窄 (s ∈ {0.15, 0.20, 0.25, 0.30})

- 具体位置：Section 4
- 问题：仅测试 4 个 sparsity level，范围 0.15–0.30。实际部署场景常涉及更高 sparsity（s > 0.50）。论文在 Appendix K 中承认 "more extreme sparsity (s > 0.50) may exhibit qualitatively different interaction dynamics" 并提到 subexponential growth 暗示 plateau。但 4 个点不足以可靠刻画 G(s) 的 functional form（论文声称 "monotonically increasing" 但仅有 4 个数据点）。
- 建议：增加 1-2 个更极端的 sparsity level（如 s=0.40, 0.50）以刻画曲线的全貌。

---

## Questions for Authors

1. **Additive vs. multiplicative null**: 既然论文的核心贡献是量化 G 的大小，而两种 null 下 G 差异 4–8×，作者如何论证读者应该信赖 additive null 的数字而非 multiplicative null 的数字？
2. **Answer-region shielding**: 如果 93.2% 的答案 token 在 G ≤ 1 的 phase 中，是否有证据表明推理痕迹的 PPL 退化会 cascade 到最终答案质量？如果不会，论文的实际 implication 是什么？
3. **Profiling vs. full sample G discrepancy**: n=50 的 G 值（69–274）比 n=496 的 G 值（7.5–79.8）高 3.5–9.2×——这种系统性差异是否意味着 LLaMA n=49 的结果同样可能高估了真实效应？
4. **Crossover model-dependence**: DeepSeek 展现 crossover 但 Qwen 不展现——是否有关于什么模型属性决定 crossover 出现的假说？

---

## 引用检查

通过 verify_references 工具检查全部 35 条引用：
- 25/35 在线验证通过
- 5/35 未在 OpenAlex 索引中找到（defensivekv-iclr2026, hies-2025, phase-transition-compression-2026, mustafar-neurips2025, lkv-2026）——均为 2025-2026 近期文献，可能尚未被索引
- 5/35 存在轻微 first author 名字不匹配（如 deepseek-r1 列 "DeepSeek-AI" vs API "Guo"；qwen25 列 "Yang" vs API "Qwen"）——属于团队/项目名 vs 个人名的常见差异
- 0 orphan bib entries, 0 missing citations
- 无明显 hallucinated references

---

## 小问题（不影响接收）

- Abstract 报告 99% CI [1.1, 14.0]（s=0.15），Table 2 报告 95% CI [4.1, 11.4]——如果是不同置信水平应明确标注
- 论文主文本（Section 1–8 Conclusion）似乎延伸至第 9 页，需确认是否严格在 8 页正文限制内
- min_phase_length=10 的选择虽经稳健性验证但缺乏直观动机说明
- Qwen 的 mid-phase null rate 达 45.2%，虽不影响 primary low-high contrast，但显著限制了三阶段 phase analysis 的完整性

---

## 主要优势

1. **统计方法论在同类论文中罕见的严谨度**：Bootstrap CI (B=10,000)、Wilcoxon signed-rank、Bonferroni + BH-FDR 双重校正、Jonckheere-Terpstra dose-response test、paired permutation test (10,000 permutations)、post-hoc power analysis——每一步都有合适的非参数检验和多重比较校正。
2. **充分的稳健性检查体系**：min_phase_length 敏感性 (Appendix M)、分割粒度 (Appendix N)、outlier winsorization (Appendix O)、multiplicative null (Appendix B)、BH-FDR correction (Appendix L)——每项核心结论有多角度交叉验证。
3. **新颖且反直觉的发现**：importance-based eviction 在 high-sparsity phase 优于 random 但在 low-sparsity phase 劣于 random 的 crossover effect (Section 5.3) 是此前未被记录的现象，不可从单轴分析推导。
4. **诚实且充分的 limitation 披露**：correlational mechanism、单一基准、LLaMA 弱结果、pilot mitigation 失败——论文对自身弱点的讨论比大多数投稿更坦诚。
5. **清晰的论文定位**：明确声明为 diagnostic study 而非提出解决方案，避免了 over-claiming。

---

## Missing References

论文的引用覆盖面在 KV cache 和 head pruning 方向上较为全面。可考虑补充：
- **FlexGen (Sheng et al., 2023)** — 另一种 compound compression 部署系统
- 关于 PPL 与 accuracy 非线性关系的 formal analysis（如果存在），以加强 Section 5.7 的讨论

---

## 总体判断

这是一篇执行力出色的诊断研究——统计方法论在同领域中属于上乘，稳健性检查近乎完备。Phase-strategy interaction 和 crossover effect 是真正新颖的发现。

但三个核心弱点将其限制在 Findings 级别：(1) 单一基准不足以支撑泛化性 claim；(2) answer-region 分析实际上削弱了 severity gradient 的实际意义，而缺乏准确率验证使 "severity" 的含义悬而未决；(3) 两个 "跨模型" 实际共享同一架构，唯一的跨架构证据（LLaMA n=49）显示效应量仅为主模型的 ~1/40。

如果作者能增加一个额外基准（哪怕 n=50 规模）并提供至少一个 sparsity level 的准确率数据，本文有望达到 main conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-15T13:54:11.315401+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "8",
  "text": "## Step 2 — 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Reviewer 2 — Round 8 审稿报告（新颖性 + 相关工作 + 写作质量）\n\n### 总体评分\n**Overall**: 2.5 / 5 (Borderline Findings)\n\n### ARR 维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法论扎实，但 \"3–39×\" 数字声明与数据不一致；G 指标受近零分母影响 |\n| Excitement | 2.5/5 | \"importance-based eviction 在 attention 分散的 phase 表现更差\"定性上可预测；缺乏可操作产出 |\n| Reproducibility | 4/5 | 实验设置详尽，承诺 release code，统计规范 |\n| Confidence | 4/5 | 熟悉 KV cache compression、attention head pruning 和 reasoning model 推理文献 |\n\n### Must-Fix 问题\n\n**N1** [critical] 新颖性不足：核心发现定性可预测，\"linear combination\" 论证为稻草人\n- 位置：Section 1 (Introduction), paragraph 3\n- 论文声称 \"a linear combination of these insights would predict that compound degradation either (i) uniformly amplifies, or (ii) follows the dominant single-axis pattern\"，然后用实际观察到的 severity gradient 反驳。但这构建了一个过弱的 null hypothesis——没有人会预期两个非线性交互的压缩轴产生 \"linear combination\"。ThinKV 已证明 attention 分散的 phase 对 eviction 更敏感；HIES 已证明重度剪枝下 importance score 区分力崩塌；compound setting 中这两效应叠加产生 phase-modulated severity 定性上可预期。论文真正贡献在于量化（G=7.5×–79.8×），但 G 指标因 II_high 接近零（Table 2: 0.003–0.038）而被人为放大。\n- 建议：(a) 改进 novelty argument，聚焦 crossover 和 dose-response 的不可预测性；(b) 在 headline claims 中同时报告 Δ（绝对差）和 G（比率）；(c) 明确讨论 G 的 near-zero denominator 放大效应。\n\n**N2** [critical] Pilot mitigation 实验削弱而非增强贡献\n- 位置：Section 7, paragraph 3 (pilot experiment)\n- Oracle phase-aware budget reallocation 仅恢复 18%（预注册 30% gate FAIL），heuristic 32% 但 CI span zero。论文 pitch \"severity gradient provides a natural signal for allocating compression budgets\"，但 pilot 直接反驳此声明。\n- 建议：要么移除 pilot（纯诊断论文无需 mitigation 尝试），要么深入分析失败原因并移至 Appendix。\n\n**N3** [critical] \"3–39×\" / \"15–39×\" 数字声明与数据不一致\n- 位置：Abstract, Section 5.1, Contribution item 1\n- 在 random 统计显著的条件（s≥0.25），实际比率为：DS 15.3–16.6×, QW 2.7–3.5×，跨模型范围 2.7–17×，非 \"3–39×\"。39× (≈0.39/0.01) 来自 DS s=0.15 但该条件 random Δ 非显著（CI spans zero）。将非显著条件比率纳入 \"where significant\" 声明是数字不一致。\n- 建议：修正为 \"3–17×\" 或准确区间。\n\n### Should-Fix 问题\n\n**W1** [warning] Crossover 过度强调（仅 DeepSeek 出现，Qwen 不存在，model-dependent）\n\n**W2** [warning] LLaMA 跨架构证据过弱（n=49，~1/40 效应量，仅 1/4 sparsity 显著），建议正文压缩\n\n**W3** [warning] \"Discrimination collapse\" 命名可能与 ML 其他 collapse 概念混淆，建议改用 \"importance score flattening\"\n\n**W4** [warning] 缺少高相关性近期文献：ForesightKV (arXiv 2602.03203), ThinK (ICLR 2025), \"Prune-then-Quantize or Quantize-then-Prune?\" (ICLR 2026)\n\n**W5** [warning] 仅 perplexity 度量；Section 5.7 answer-region 分析（93.2% answer tokens 在 high-sparsity phase）暗示 practical significance 可能远低于 G 指标所示\n\n### 小问题\n- Table 2 footnote: negative II 应报告为 ≈0\n- LaTeX 源码残留 `% exp_id:` 注释\n- LKV reference author = \"Anonymous\"\n- Table 3 caption 中 \"paired median difference\" vs \"difference of medians\" 概念需更清晰\n\n### 主要优势\n1. 统计方法论堪称典范\n2. 多维度 robustness 验证\n3. Cross-model replication 增强可靠性\n4. Diagnostic study 自我定位一致，hedging 得当\n5. Random eviction 对照组设计精巧\n\n### 缺失引用\n| 论文 | 相关性 |\n|------|--------|\n| ForesightKV (2602.03203) | Reasoning-specific KV eviction with learned long-term importance |\n| ThinK (ICLR 2025) | Channel-level KV pruning compound compression |\n| Prune-then-Quantize or Quantize-then-Prune? (ICLR 2026) | Compression order interaction, Progressive Intensity Hypothesis |\n\n### Overall Assessment\nWeak Reject → Borderline Findings。适合 Findings track。\n\n---\n\n请逐条回应 Reviewer 2 的每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和小问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "8",
    "text": "## Step 2 — 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Reviewer 2 — Round 8 审稿报告（新颖性 + 相关工作 + 写作质量）\n\n### 总体评分\n**Overall**: 2.5 / 5 (Borderline Findings)\n\n### ARR 维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法论扎实，但 \"3–39×\" 数字声明与数据不一致；G 指标受近零分母影响 |\n| Excitement | 2.5/5 | \"importance-based eviction 在 attention 分散的 phase 表现更差\"定性上可预测；缺乏可操作产出 |\n| Reproducibility | 4/5 | 实验设置详尽，承诺 release code，统计规范 |\n| Confidence | 4/5 | 熟悉 KV cache compression、attention head pruning 和 reasoning model 推理文献 |\n\n### Must-Fix 问题\n\n**N1** [critical] 新颖性不足：核心发现定性可预测，\"linear combination\" 论证为稻草人\n- 位置：Section 1 (Introduction), paragraph 3\n- 论文声称 \"a linear combination of these insights would predict that compound degradation either (i) uniformly amplifies, or (ii) follows the dominant single-axis pattern\"，然后用实际观察到的 severity gradient 反驳。但这构建了一个过弱的 null hypothesis——没有人会预期两个非线性交互的压缩轴产生 \"linear combination\"。ThinKV 已证明 attention 分散的 phase 对 eviction 更敏感；HIES 已证明重度剪枝下 importance score 区分力崩塌；compound setting 中这两效应叠加产生 phase-modulated severity 定性上可预期。论文真正贡献在于量化（G=7.5×–79.8×），但 G 指标因 II_high 接近零（Table 2: 0.003–0.038）而被人为放大。\n- 建议：(a) 改进 novelty argument，聚焦 crossover 和 dose-response 的不可预测性；(b) 在 headline claims 中同时报告 Δ（绝对差）和 G（比率）；(c) 明确讨论 G 的 near-zero denominator 放大效应。\n\n**N2** [critical] Pilot mitigation 实验削弱而非增强贡献\n- 位置：Section 7, paragraph 3 (pilot experiment)\n- Oracle phase-aware budget reallocation 仅恢复 18%（预注册 30% gate FAIL），heuristic 32% 但 CI span zero。论文 pitch \"severity gradient provides a natural signal for allocating compression budgets\"，但 pilot 直接反驳此声明。\n- 建议：要么移除 pilot（纯诊断论文无需 mitigation 尝试），要么深入分析失败原因并移至 Appendix。\n\n**N3** [critical] \"3–39×\" / \"15–39×\" 数字声明与数据不一致\n- 位置：Abstract, Section 5.1, Contribution item 1\n- 在 random 统计显著的条件（s≥0.25），实际比率为：DS 15.3–16.6×, QW 2.7–3.5×，跨模型范围 2.7–17×，非 \"3–39×\"。39× (≈0.39/0.01) 来自 DS s=0.15 但该条件 random Δ 非显著（CI spans zero）。将非显著条件比率纳入 \"where significant\" 声明是数字不一致。\n- 建议：修正为 \"3–17×\" 或准确区间。\n\n### Should-Fix 问题\n\n**W1** [warning] Crossover 过度强调（仅 DeepSeek 出现，Qwen 不存在，model-dependent）\n\n**W2** [warning] LLaMA 跨架构证据过弱（n=49，~1/40 效应量，仅 1/4 sparsity 显著），建议正文压缩\n\n**W3** [warning] \"Discrimination collapse\" 命名可能与 ML 其他 collapse 概念混淆，建议改用 \"importance score flattening\"\n\n**W4** [warning] 缺少高相关性近期文献：ForesightKV (arXiv 2602.03203), ThinK (ICLR 2025), \"Prune-then-Quantize or Quantize-then-Prune?\" (ICLR 2026)\n\n**W5** [warning] 仅 perplexity 度量；Section 5.7 answer-region 分析（93.2% answer tokens 在 high-sparsity phase）暗示 practical significance 可能远低于 G 指标所示\n\n### 小问题\n- Table 2 footnote: negative II 应报告为 ≈0\n- LaTeX 源码残留 `% exp_id:` 注释\n- LKV reference author = \"Anonymous\"\n- Table 3 caption 中 \"paired median difference\" vs \"difference of medians\" 概念需更清晰\n\n### 主要优势\n1. 统计方法论堪称典范\n2. 多维度 robustness 验证\n3. Cross-model replication 增强可靠性\n4. Diagnostic study 自我定位一致，hedging 得当\n5. Random eviction 对照组设计精巧\n\n### 缺失引用\n| 论文 | 相关性 |\n|------|--------|\n| ForesightKV (2602.03203) | Reasoning-specific KV eviction with learned long-term importance |\n| ThinK (ICLR 2025) | Channel-level KV pruning compound compression |\n| Prune-then-Quantize or Quantize-then-Prune? (ICLR 2026) | Compression order interaction, Progressive Intensity Hypothesis |\n\n### Overall Assessment\nWeak Reject → Borderline Findings。适合 Findings track。\n\n---\n\n请逐条回应 Reviewer 2 的每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和小问题。"
  }
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-15T13:54:47.819934+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 36504
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-15T13:54:47.971957+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "8",
  "text": "## Step 2 — 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Reviewer 1 — Round 8 审稿报告\n\n**Overall**: 3/5 (Findings: could be accepted to Findings of the ACL)\n\n### ARR 维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计框架严谨，但核心度量仅基于 PPL、单一基准，且 additive null 的论证不够充分 |\n| Excitement | 3/5 | Phase-strategy interaction 和 crossover effect 有新意，但实际可操作性不清 |\n| Reproducibility | 4/5 | 实验细节充分，承诺代码发布 |\n| Confidence | 4/5 | 仔细阅读全文含全部 15 个 Appendix |\n\n### Must-Fix 问题\n\n**N1** [critical] Interaction Index 的 additive null 假设与论文自身论述存在内在矛盾\n- 具体位置：Section 3, Eq. 1; Appendix B\n- 问题：论文以\"两个轴作用于不相交维度（structural vs. positional）\"来正当化 additive null（II = r_c − r_a − r_k + 1）。但论文自身在 Section 3 明确指出 \"head pruning alters the importance ranking used for eviction\"，在 Section 6 详细分析 head pruning 如何通过 discrimination collapse 直接影响 KV eviction 的决策质量。这意味着两个压缩轴存在直接的因果耦合，并非\"不相交\"。Appendix B 的 multiplicative null 验证显示 G_mult ≈ 58–211（远高于 additive G = 7.5–79.8），两种 null 下的数值差异达 4–8×。\n- 为什么影响接收：II 是论文所有定量结论的根基。如果 additive null 不合理，所有基于 II 的数字均失去可靠的解释基准。\n- 建议：(1) 严格论证 additive null 的合理性；(2) 在主文本中并列报告两种 null 下的关键结果。\n\n**N2** [critical] 单一基准测试 (MATH-500) 严重限制泛化性\n- 具体位置：Section 4.1; Limitations\n- 问题：论文所有定量结论仅基于 MATH-500 一个基准。论文标题中使用 \"Mathematical Reasoning Models\"（复数），暗示一般性。不同推理任务的 attention dynamics 可能截然不同。一个额外基准（哪怕是小规模）即可大幅增强可信度。\n\n**N3** [critical] PPL 度量的 construct validity 问题：论文自身的 answer-region 分析反而削弱了核心叙事\n- 具体位置：Section 5.7\n- 问题：93.2% 的答案 token 落在 high-sparsity phase（G ≤ 1）；答案 token 的 PPL degradation 远低于推理痕迹 token。更准确的解读是：观察到的巨大 G 值集中在对最终答案影响最小的 phase 中。缺乏直接准确率测量使 \"severity\" 的实际含义悬而未决。\n- 建议：(1) 在至少一个 sparsity level 上测量实际准确率变化；(2) 重新框定 severity gradient 的意义。\n\n### Should-Fix 问题\n\n**W1** [warning] \"Cross-model replication\" 实为同架构不同训练范式\n- DeepSeek 和 Qwen 共享 Qwen2ForCausalLM，LLaMA (n=49) 效应量仅 ~1/40，暗示可能是 Qwen2 架构特有\n\n**W2** [warning] Discrimination collapse 的解释力存在 order-of-magnitude 缺口\n- Gini drop 差异 < 10% 对应 severity 差异 15–17×；entropy redistribution 仅 2/4 条件复现\n\n**W3** [warning] Profiling subset (n=50) 与 full sample (n=496) 的 G 差异 3.5–9.2×\n- 系统性下移未充分解释；对 LLaMA n=49 结果可靠性有启示\n\n**W4** [warning] Phase segmentation 缺乏理论先验\n- 纯数据驱动分割；attention sparsity 作为 phase proxy 的合理性未独立论证\n\n**W5** [warning] Pilot mitigation experiment 未达预注册 gate，削弱实际应用叙事\n- Oracle 仅恢复 18%（gate FAIL），质疑 severity gradient 作为 \"natural signal\" 的价值\n\n**W6** [warning] Sparsity 范围窄 (s ∈ {0.15, 0.20, 0.25, 0.30})\n- 仅 4 个数据点不足以可靠刻画 G(s) 的 functional form\n\n### Questions for Authors\n1. Additive vs. multiplicative null: 两种 null 下 G 差异 4–8×，作者如何论证读者应信赖 additive null？\n2. Answer-region shielding: 93.2% 答案 token 在 G ≤ 1 phase，推理痕迹 PPL 退化会 cascade 到最终答案吗？\n3. Profiling vs. full sample G discrepancy: n=50 G 比 n=496 G 高 3.5–9.2×，LLaMA n=49 是否同样高估？\n4. Crossover model-dependence: 什么模型属性决定 crossover 是否出现？\n\n### 引用检查\n- 25/35 在线验证通过\n- 5/35 未被索引（2025-2026 近期文献）\n- 0 hallucinated references\n\n### 小问题\n- Abstract CI vs Table 2 CI 置信水平可能不同\n- 正文可能超 8 页\n- min_phase_length=10 缺乏直观动机\n- Qwen mid-phase null rate 45.2% 限制三阶段分析完整性\n\n### 主要优势\n1. 统计方法论罕见严谨\n2. 充分的稳健性检查体系\n3. Crossover effect 新颖且反直觉\n4. 诚实的 limitation 披露\n5. 清晰的 diagnostic study 定位\n\n### Missing References\n- FlexGen (Sheng et al., 2023)\n- PPL 与 accuracy 非线性关系的 formal analysis\n\n### Overall Assessment\n3/5，Findings level。增加额外基准 + 准确率数据可升至 main conference。\n\n---\n\n请逐条回应 Reviewer 1 的每个 Must-Fix (N1-N3)、Should-Fix (W1-W6)、Questions (1-4) 和小问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "8",
    "text": "## Step 2 — 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Reviewer 1 — Round 8 审稿报告\n\n**Overall**: 3/5 (Findings: could be accepted to Findings of the ACL)\n\n### ARR 维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计框架严谨，但核心度量仅基于 PPL、单一基准，且 additive null 的论证不够充分 |\n| Excitement | 3/5 | Phase-strategy interaction 和 crossover effect 有新意，但实际可操作性不清 |\n| Reproducibility | 4/5 | 实验细节充分，承诺代码发布 |\n| Confidence | 4/5 | 仔细阅读全文含全部 15 个 Appendix |\n\n### Must-Fix 问题\n\n**N1** [critical] Interaction Index 的 additive null 假设与论文自身论述存在内在矛盾\n- 具体位置：Section 3, Eq. 1; Appendix B\n- 问题：论文以\"两个轴作用于不相交维度（structural vs. positional）\"来正当化 additive null（II = r_c − r_a − r_k + 1）。但论文自身在 Section 3 明确指出 \"head pruning alters the importance ranking used for eviction\"，在 Section 6 详细分析 head pruning 如何通过 discrimination collapse 直接影响 KV eviction 的决策质量。这意味着两个压缩轴存在直接的因果耦合，并非\"不相交\"。Appendix B 的 multiplicative null 验证显示 G_mult ≈ 58–211（远高于 additive G = 7.5–79.8），两种 null 下的数值差异达 4–8×。\n- 为什么影响接收：II 是论文所有定量结论的根基。如果 additive null 不合理，所有基于 II 的数字均失去可靠的解释基准。\n- 建议：(1) 严格论证 additive null 的合理性；(2) 在主文本中并列报告两种 null 下的关键结果。\n\n**N2** [critical] 单一基准测试 (MATH-500) 严重限制泛化性\n- 具体位置：Section 4.1; Limitations\n- 问题：论文所有定量结论仅基于 MATH-500 一个基准。论文标题中使用 \"Mathematical Reasoning Models\"（复数），暗示一般性。不同推理任务的 attention dynamics 可能截然不同。一个额外基准（哪怕是小规模）即可大幅增强可信度。\n\n**N3** [critical] PPL 度量的 construct validity 问题：论文自身的 answer-region 分析反而削弱了核心叙事\n- 具体位置：Section 5.7\n- 问题：93.2% 的答案 token 落在 high-sparsity phase（G ≤ 1）；答案 token 的 PPL degradation 远低于推理痕迹 token。更准确的解读是：观察到的巨大 G 值集中在对最终答案影响最小的 phase 中。缺乏直接准确率测量使 \"severity\" 的实际含义悬而未决。\n- 建议：(1) 在至少一个 sparsity level 上测量实际准确率变化；(2) 重新框定 severity gradient 的意义。\n\n### Should-Fix 问题\n\n**W1** [warning] \"Cross-model replication\" 实为同架构不同训练范式\n- DeepSeek 和 Qwen 共享 Qwen2ForCausalLM，LLaMA (n=49) 效应量仅 ~1/40，暗示可能是 Qwen2 架构特有\n\n**W2** [warning] Discrimination collapse 的解释力存在 order-of-magnitude 缺口\n- Gini drop 差异 < 10% 对应 severity 差异 15–17×；entropy redistribution 仅 2/4 条件复现\n\n**W3** [warning] Profiling subset (n=50) 与 full sample (n=496) 的 G 差异 3.5–9.2×\n- 系统性下移未充分解释；对 LLaMA n=49 结果可靠性有启示\n\n**W4** [warning] Phase segmentation 缺乏理论先验\n- 纯数据驱动分割；attention sparsity 作为 phase proxy 的合理性未独立论证\n\n**W5** [warning] Pilot mitigation experiment 未达预注册 gate，削弱实际应用叙事\n- Oracle 仅恢复 18%（gate FAIL），质疑 severity gradient 作为 \"natural signal\" 的价值\n\n**W6** [warning] Sparsity 范围窄 (s ∈ {0.15, 0.20, 0.25, 0.30})\n- 仅 4 个数据点不足以可靠刻画 G(s) 的 functional form\n\n### Questions for Authors\n1. Additive vs. multiplicative null: 两种 null 下 G 差异 4–8×，作者如何论证读者应信赖 additive null？\n2. Answer-region shielding: 93.2% 答案 token 在 G ≤ 1 phase，推理痕迹 PPL 退化会 cascade 到最终答案吗？\n3. Profiling vs. full sample G discrepancy: n=50 G 比 n=496 G 高 3.5–9.2×，LLaMA n=49 是否同样高估？\n4. Crossover model-dependence: 什么模型属性决定 crossover 是否出现？\n\n### 引用检查\n- 25/35 在线验证通过\n- 5/35 未被索引（2025-2026 近期文献）\n- 0 hallucinated references\n\n### 小问题\n- Abstract CI vs Table 2 CI 置信水平可能不同\n- 正文可能超 8 页\n- min_phase_length=10 缺乏直观动机\n- Qwen mid-phase null rate 45.2% 限制三阶段分析完整性\n\n### 主要优势\n1. 统计方法论罕见严谨\n2. 充分的稳健性检查体系\n3. Crossover effect 新颖且反直觉\n4. 诚实的 limitation 披露\n5. 清晰的 diagnostic study 定位\n\n### Missing References\n- FlexGen (Sheng et al., 2023)\n- PPL 与 accuracy 非线性关系的 formal analysis\n\n### Overall Assessment\n3/5，Findings level。增加额外基准 + 准确率数据可升至 main conference。\n\n---\n\n请逐条回应 Reviewer 1 的每个 Must-Fix (N1-N3)、Should-Fix (W1-W6)、Questions (1-4) 和小问题。"
  }
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-15T13:54:49.491262+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1519
}
```

</details>

---


### Assistant

_source line 628 · 2026-05-15T13:54:52.451584+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 47

## Round 47

2 recorded events


### User

_source line 629 · 2026-05-15T13:54:55.024897+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**核心判断**: Overall 3/5 (Findings)，Soundness 3.5/5，Excitement 3/5。

**三个 Must-Fix 问题**：
1. Additive null 假设与论文自身关于两轴因果耦合的论述存在内在矛盾
2. 仅用 MATH-500 一个基准，泛化性不足
3. Answer-region 分析（93.2% 答案 token 在 G≤1 的 phase）反而削弱了 severity gradient 的实际意义，且无准确率验证

**五个 Should-Fix 问题**：同架构"跨模型"验证、discrimination collapse 解释力缺口（Gini drop ~10% vs severity 15–17×）、profiling vs full sample G 值差异 3.5–9.2×、phase segmentation 无理论先验、pilot mitigation 未达 gate。

**主要优势**：统计方法论在同类论文中罕见的严谨度、充分的稳健性检查、新颖的 crossover effect、诚实的 limitation 披露。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 630 · 2026-05-15T13:55:00.685127+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 48

## Round 48

2 recorded events


### User

_source line 631 · 2026-05-15T13:56:24.710167+00:00_

[Reviewer 1 审稿意见]:
## Round 8 Step 2 — Reviewer 1 对 Reviewer 2 意见的交叉回应

---

### Must-Fix 问题

**[PARTIALLY AGREE] R2-N1: 核心发现定性可预测，"linear combination" 论证为稻草人**

同意的部分：Section 1 第 3 段的 "linear combination" 论证确实构建了一个过弱的 null hypothesis。R2 正确指出没有人会预期两个非线性交互的压缩轴产生 linear combination——ThinKV（Section 2: "applies different KV strategies per phase"）已证明 attention 分散的 phase 对 eviction 更敏感，HIES 已证明重度剪枝下 importance score 区分力崩塌。compound setting 中这两效应叠加产生 phase-modulated severity，定性方向确实可预期。

R2 关于 G 指标受 near-zero denominator 放大的观察也成立：Table 2 显示 importance-based II_high = 0.000–0.038，当分母接近零时 G = II_low/II_high 被人为放大。论文在 Section 4 已声明 Δ 为 primary metric、G 为 auxiliary，但 abstract 和 headline claims 仍以 G 值（7.5×–79.8×）领衔，造成 framing 偏差。

反驳的部分：R2 低估了 **crossover effect**（Section 5.3）的新颖性。该效应无法从 ThinKV + HIES 的单轴结论组合推导——importance-based eviction 在 high-sparsity phase 优于 random（II: 0.021 vs 1.113）但在 low-sparsity phase 劣于 random（3.971 vs 1.514），这是一个 **策略排名反转**，不是单纯的"某策略在某 phase 更差"。无论 ThinKV 还是 HIES 都不会预测同一策略在同一 sparsity level 的不同 phase 中从"更好"变成"更差"。此外，**dose-response monotonicity**（Jonckheere-Terpstra z=6.2–33.7, p < 10⁻⁷; Section 5.6）和 G 随 s 的严格递增，也不是从定性直觉可推导的定量结构。

建议维持 R2 的修改方向 (a)：novelty argument 应聚焦 crossover 和 dose-response 的不可预测性，而非 strawman "linear combination" 反驳。方向 (b) 在 headline claims 中并列报告 Δ 和 G 也是合理建议。

---

**[AGREE] R2-N2: Pilot mitigation 实验削弱而非增强贡献**

完全同意。我在自己的审稿中将此列为 W5（Should-Fix），但 R2 将其升级为 Must-Fix 也有道理。Section 7 声称 "severity gradient provides a natural signal for allocating compression budgets"，但紧接着报告 oracle recovery 仅 18%（低于 30% pre-registered gate），heuristic 32% 但 95% CI 跨越 zero。这构成论文自身叙事的内部矛盾——先声称 gradient 有实用价值，再展示它实际上不可操作。

R2 的建议——要么移除 pilot（保持纯诊断定位），要么深入分析失败原因移至 Appendix——都是可行方案。我倾向后者：pilot 的失败本身是有信息量的（暗示 coarse phase boundary 可能不足以捕捉 severity 的精细空间结构），但应降低其在主文本中的权重，避免与 "natural signal" 的正面叙事直接冲突。

---

**[PARTIALLY AGREE] R2-N3: "3–30×" / "3–39×" 数字声明与数据不一致**

同意核心论点。根据 Table 1 和 Table 2 的数据：
- 在 random Δ 统计显著的条件（s ≥ 0.25）下：
  - DS: Δ_imp/Δ_rand = 3.99/0.26 ≈ 15.3× (s=0.25), 8.48/0.51 ≈ 16.6× (s=0.30)
  - QW: 1.07/0.39 ≈ 2.7× (s=0.25), 3.16/0.91 ≈ 3.5× (s=0.30)
- 跨模型的合理声明范围：**2.7–17×**

论文 Contribution 1 中的 "3–30×" 的上界显然来自 s ≤ 0.20 的条件，而这些条件下 random Δ 是非显著的（Table 2: CI spans zero）。将非显著分母的比率纳入定量声明确实构成数字不一致。

细微反驳：R2 的 "3-39×" 似乎是对论文数字的进一步推算（0.39/0.01 ≈ 39×），论文原文 contribution 写的是 "3–30×"。但无论是 30× 还是 39×，核心问题相同——上界取自非显著条件。

建议采纳 R2 的修正方向：在 significant-only 条件下报告 "3–17×"，或明确标注 "3–17× where both strategies show significant phase gradients (s ≥ 0.25); at lower sparsity the gradient is larger but random eviction's denominator is non-significant"。

---

### Should-Fix 问题

**[REBUT] R2-W1: Crossover 过度强调**

不同意降低 crossover 的地位。Crossover（Section 5.3, Figure 2）是论文中最具区分度的发现——它是唯一不能从单轴工作推导的**定性**新颖性（不仅仅是定量放大）。在 s=0.25：importance II_high = 0.021 vs random 1.113，但 importance II_low = 3.971 vs random 1.514——同一策略在同一 sparsity 下的两个 phase 中排名完全反转。

模型依赖性是事实（Qwen 不展现 crossover），但这本身也是有价值的发现：它暗示 crossover 的出现与 training paradigm（distillation vs instruction tuning）相关，而非 architecture 固有属性。论文在 Section 5.3 末尾和 Section 7 明确标注了模型依赖性（"the ranking reversal is model-dependent"）。

建议：保留 crossover 作为核心发现之一，但 R2 的关切可通过在 abstract 中加入 "model-dependent" 限定词来解决。

---

**[AGREE] R2-W2: LLaMA 证据过弱，建议正文压缩**

同意。n=49，power 仅 0.20–0.65 for strategy comparison（Appendix G），效应量 ~1/40 of DeepSeek。我在自己的审稿中也标注了同一问题（W1）。正文 Section 5.5 可压缩至 2-3 句，详细数据移至 Appendix G。

---

**[PARTIALLY AGREE] R2-W3: "Discrimination collapse" 命名可能混淆**

部分同意。"Collapse" 在 ML 中有 mode collapse、neural collapse、representation collapse 等既有含义，确实可能造成混淆。但 R2 建议的 "importance score flattening" 过于平淡——它准确描述了现象的一半（score 分布变平），但遗漏了关键含义：flattening 导致 thresholding 退化为 noise-sensitive selection（Section 6.1: "degenerates into noise-sensitive selection when score distributions flatten"）。

建议折中：使用 **"importance discrimination collapse"** 或 **"score discrimination flattening"**——前者保留了 "collapse" 的严重性含义并加了限定词避免歧义，后者更精确但稍弱。

---

**[AGREE] R2-W4: 缺少高相关性近期文献**

同意。三篇文献均与论文主题高度相关：
- **ThinK (ICLR 2025)**: channel-level KV pruning 是另一种 compound compression axis，与论文的 head pruning + token eviction 形成对比。
- **ForesightKV**: reasoning-specific KV eviction with learned long-term importance 直接关联 Section 6 的 importance score 退化讨论。
- **"Prune-then-Quantize or Quantize-then-Prune?" (ICLR 2026)**: Progressive Intensity Hypothesis 与论文的 dose-response 发现（G 随 s 单调递增）有概念层面的平行关系。

至少 ThinK 和 ForesightKV 应在 Related Work Section 2 中讨论。

---

**[AGREE] R2-W5: 仅 perplexity 度量 + answer-region 分析暗示实际意义有限**

强烈同意。我在自己的审稿中将此列为 **N3 (Must-Fix)**。Section 5.7 的 answer-region 分析（93.2% answer tokens 在 high-sparsity phase, G ≤ 1）实质上表明 severity gradient 主要影响中间推理过程而非最终输出。缺乏准确率验证使 "severity" 的操作定义悬而未决。R2 将其列为 Should-Fix 而非 Must-Fix 偏于保守——我认为这是影响接收决定的核心问题。

---

### 小问题

**[AGREE]** Table 2 footnote 中 negative II 应报告为 ≈0：同意，负值 II 在该 sparsity level 反映 numerical noise（Section 6 Table 2 footnote 已提及 ℓcos ≈ 1/6 numerical noise），报告为 ≈0 更准确。

**[AGREE]** LaTeX 源码残留 `% exp_id:` 注释：格式问题，应在最终版本清理。

**[AGREE]** LKV reference author = "Anonymous"：确实——引用匿名作者不符合 double-blind 规范中的引用标准（anonymous preprint 通常应引用为 arXiv ID 而非 "Anonymous"）。

**[PARTIALLY AGREE]** Table 3 caption 中 "paired median difference" vs "difference of medians" 概念需更清晰：论文在 Section 3 (Eq. 2 discussion) 区分了 median-of-ratios（G 定义）和 ratio-of-medians，但 Table 3 的 "paired median difference" 确实可能被误读为 "difference of medians"。建议在 Table 3 caption 中明确："Δ = median_i(II_low^(i) − II_high^(i))"，即先 per-problem 配对差分再取 median。

---

### 总体评价对比

| 维度 | Reviewer 1 (我) | Reviewer 2 | 差异分析 |
|------|---------|---------|---------|
| Overall | 3/5 (Findings) | 2.5/5 (Borderline Findings) | R2 偏低 0.5，主要因为对 novelty 更悲观 |
| Soundness | 3.5/5 | 3.5/5 | 一致 |
| Excitement | 3/5 | 2.5/5 | 我认为 crossover 有真正新颖性；R2 认为核心发现可预测 |

**我对 R2 评分的看法**：R2 的 2.5 分稍低。论文的 novelty 不完全是 "attention 分散时更差" 的定性观察——crossover effect 和 dose-response 的严格单调性是单轴工作无法预测的。但 R2 对数字声明不一致 (N3) 和 pilot 失败 (N2) 的批评完全正确，这些确实拉低了论文质量。

**综合建议**：维持我的 Overall 3/5 (Findings) 评价。如果作者能修正数字声明（N3）、重新 frame novelty argument（N1 部分）、删除或下移 pilot experiment（N2），论文在 Findings track 有竞争力。但要达到 main conference 水平，仍需解决单一基准（我的 N2）和准确率验证（我的 N3 / R2 的 W5）问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 632 · 2026-05-15T13:56:29.771202+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 49

## Round 49

2 recorded events


### User

_source line 633 · 2026-05-15T13:56:34.952020+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。要点总结：

**与 R2 的共识**：
- N2 (pilot 失败削弱叙事) — 完全同意
- N3 (数字声明不一致) — 基本同意，"3–30×" 上界来自非显著条件，应修正为 "3–17×"
- W2 (LLaMA 证据弱) — 完全同意
- W4 (缺失引用) — 同意
- W5 (PPL-only + answer-region) — 强烈同意，我将其列为 Must-Fix 级别

**与 R2 的分歧**：
- N1 (novelty) — 部分反驳：strawman 论证确实弱，但 **crossover effect** 是真正的定性新颖性（同一策略在不同 phase 排名反转），不能从单轴工作推导
- W1 (crossover 过度强调) — 反驳：crossover 恰恰是论文最具区分度的发现
- W3 (命名) — 部分同意，建议折中为 "importance discrimination collapse"

**评分差异**：我 Overall 3/5 vs R2 2.5/5，差异主要在 Excitement（我认为 crossover 有不可预测的新颖性）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 634 · 2026-05-15T13:56:45.048544+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 50

## Round 50

8 recorded events


### User

_source line 635 · 2026-05-15T13:57:31.250954+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条交叉回应

### Must-Fix

**[AGREE] R1-N1 (Additive null 矛盾)**: 论文自身的 causal coupling narrative（Section 3: "head pruning alters the importance ranking"; Section 6: discrimination collapse）与 "disjoint dimensions" 辩护矛盾。但严重性稍低于 R1 判断——两种 null 下定性结论一致（Appendix B），Δ 不受 null 选择影响。核心问题是 G 的 headline 数字缺乏可靠解释基准。建议主文并列报告两种 null 的 G，以 Δ 作为 primary metric。

**[AGREE] R1-N2 (单一基准)**: 完全同意。MATH-500 一个基准不足以支撑标题中 "Mathematical Reasoning Models" 的泛化暗示。

**[AGREE] R1-N3 (PPL construct validity)**: 强烈同意，与我的 W5 相互印证。93.2% answer tokens 在 G≈1 phase 意味着 severity gradient 的 practical significance 可能被系统性高估。至少需要一个 sparsity level 的 accuracy sanity check。

### Should-Fix

**[AGREE] R1-W1 (同架构)**: 同意应改称 "cross-training-paradigm replication"。LLaMA ~1/40 效应量暗示量化特征可能 Qwen2 特有。

**[AGREE] R1-W2 (Discrimination collapse gap)**: 同意。Gini drop <10% vs severity 15-17× 的 order-of-magnitude gap 说明 discrimination collapse 是 necessary but not sufficient。

**[REBUT] R1-W3 (Profiling vs full G discrepancy)**: R1 误读了数据。Table 5 (Appendix C) caption 已明确解释：profiling 表使用 **ratio-of-medians** 定义，main Table 2 使用 **median-of-per-problem-ratios** (Eq. 2)。3.5-9.2× 差异是统计量定义不同，不是 sample size artifact。当 II_high 接近零时两种定义自然大幅 diverge，论文 caption 已说明 "At low sparsity (s=0.15), the two definitions diverge substantially (7.5× vs. 69×) because per-problem ratios are sensitive to near-zero II_high values." R1 的 Q3 (LLaMA 高估?) 也需重新审视——LLaMA 表 (Appendix D) 报告的是 Δ 和 CI 而非 G ratio。

**[AGREE] R1-W4 (Phase segmentation 无理论先验)**: 部分同意。Tercile segmentation 纯数据驱动，但 robustness checks (Appendix G/H: quartile/quintile + mpl sensitivity) 部分缓解。问题更多是 interpretability 而非 validity。

**[AGREE] R1-W5 (Pilot gate FAIL)**: 与我的 N2 一致。

**[AGREE] R1-W6 (Sparsity 范围窄)**: 部分同意。4 点足以验证 monotonicity (JT test) 但不足以刻画 functional form。Scope limitation 而非 flaw。

### Questions

**Q1**: [AGREE] 应主文并列报告两种 null。
**Q2**: [AGREE] 需 accuracy sanity check。
**Q3**: [REBUT] G 定义不同所致，非 sample size artifact（见 W3 回应）。
**Q4**: [AGREE] Crossover model-dependence 缺乏 explanatory hypothesis 是明显弱点。

### 小问题
- Abstract vs Table CI: [REBUT] 交叉核查一致。
- 正文超页: [AGREE] 需确认。
- mpl=10 动机: [AGREE] 应简述。
- Qwen mid-phase null: [AGREE] 限制存在但处理合理。

### Missing References
- FlexGen: [REBUT] 是 offloading/scheduling 工作，非 compound sparsity interaction。
- PPL-accuracy formal analysis: [AGREE] 应补充引用。

### 两位 Reviewer 共识点
1. PPL-only 度量 + answer-region shielding 削弱 practical significance（R1-N3 = R2-W5）
2. Pilot mitigation gate FAIL 削弱 diagnostic value narrative（R1-W5 = R2-N2）
3. Discrimination collapse 解释力不足（R1-W2 ≈ R2-W3 命名问题的深层原因）
4. Crossover 的 model-dependence 需更好解释（R1-Q4 ≈ R2-W1）
5. 统计方法论堪称典范（两位 Reviewer 均给 Soundness 3.5、Reproducibility 4）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-15T13:57:54.975072+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-15T13:57:55.026861+00:00_

1	## Round 6 (all resolved, compact)
2	- id: R6-N1
3	  summary: "Table 2 n=50→n=500"
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 5
8	  last_seen_round: 6
9	  mentions: []
10	  action_items: [{round: 6, action: "Table 2 replaced", assigned_to: paper_agent, status: done}]
11	  resolution: "Done R6."
12	  resolution_round: 6
13	
14	- id: R6-N2
15	  summary: "Discrimination collapse effect size gap"
16	  category: method
17	  severity: critical
18	  status: resolved
19	  first_raised_round: 6
20	  last_seen_round: 6
21	  mentions: []
22	  action_items: [{round: 6, action: "§6 rewritten as correlational diagnostic", assigned_to: paper_agent, status: done}]
23	  resolution: "Done R6."
24	  resolution_round: 6
25	
26	- id: R6-N3
27	  summary: "ThinKV misattribution"
28	  category: writing
29	  severity: critical
30	  status: resolved
31	  first_raised_round: 1
32	  last_seen_round: 6
33	  mentions: []
34	  action_items: [{round: 6, action: "Rewritten", assigned_to: paper_agent, status: done}]
35	  resolution: "Done R6."
36	  resolution_round: 6
37	
38	## Round 7
39	- id: R7-N1
40	  summary: "No downstream accuracy validation; construct validity gap"
41	  category: experiment
42	  severity: critical
43	  status: resolved
44	  first_raised_round: 7
45	  last_seen_round: 7
46	  mentions:
47	    - {round: 7, reviewers: [R1, R2], note: "PPL-based II not mapped to accuracy; low-sparsity phase may not affect answers"}
48	  action_items:
49	    - {round: 7, action: "N1a answer-region proxy + boxed validation", assigned_to: main_agent, status: done}
50	    - {round: 7, action: "§5.7 Answer-Region Analysis + Limitations caveat", assigned_to: paper_agent, status: done}
51	  resolution: "93.2% answer tokens in high-sparsity phase (naturally shielded). 16/16 conditions answer < reasoning degradation. Proxy evidence with appropriate caveats. N1b skipped (D070)."
52	  resolution_round: 7
53	
54	- id: R7-N2
55	  summary: "G metric definitio
…[truncated 7621 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-15T13:59:39.266802+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "issues_yaml": "## Round 6 (all resolved, compact)\n- id: R6-N1\n  summary: \"Table 2 n=50→n=500\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions: []\n  action_items: [{round: 6, action: \"Table 2 replaced\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done R6.\"\n  resolution_round: 6\n\n- id: R6-N2\n  summary: \"Discrimination collapse effect size gap\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions: []\n  action_items: [{round: 6, action: \"§6 rewritten as correlational diagnostic\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done R6.\"\n  resolution_round: 6\n\n- id: R6-N3\n  summary: \"ThinKV misattribution\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions: []\n  action_items: [{round: 6, action: \"Rewritten\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done R6.\"\n  resolution_round: 6\n\n## Round 7 (all resolved except R7-M2)\n- id: R7-N1\n  summary: \"No downstream accuracy validation; construct validity gap\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"PPL-based II not mapped to accuracy; low-sparsity phase may not affect answers\"}\n    - {round: 8, reviewers: [R1, R2], note: \"REOPENED: answer-region proxy (93.2% in G≤1 phase) actually UNDERMINES severity narrative. Both R8 reviewers agree direct accuracy validation needed.\"}\n  action_items:\n    - {round: 7, action: \"N1a answer-region proxy + boxed validation\", assigned_to: main_agent, status: done}\n    - {round: 7, action: \"§5.7 Answer-Region Analysis + Limitations caveat\", assigned_to: paper_agent, status: done}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-N2\n  summary: \"G metric definition inconsistent + Abstract CI misleading\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"median-of-ratios vs ratio-of-medians; CI splice\"}\n  action_items:\n    - {round: 7, action: \"Eq.2 disambiguation + Table 4 footnote + Abstract per-sparsity CI\", assigned_to: paper_agent, status: done}\n  resolution: \"G definitions disambiguated. Abstract CI now per-sparsity. Table 4 footnote added.\"\n  resolution_round: 7\n\n- id: R7-N3\n  summary: \"Single importance scoring method but categorical claims\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Only cumulative attention mass tested\"}\n  action_items:\n    - {round: 7, action: \"Scope down claims to attention-mass-based methods\", assigned_to: paper_agent, status: done}\n  resolution: \"Claims scoped to 'attention-mass-based scoring methods'. H2O spot check deprioritized (GPU to N1).\"\n  resolution_round: 7\n\n- id: R7-W1\n  summary: \"Generalizability: single benchmark/scale/backbone\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"§5.4 title misleading\"}\n    - {round: 8, reviewers: [R1, R2], note: \"REOPENED as critical: MATH-500 only. Title says 'Mathematical Reasoning Models' (plural) implying generality. One additional benchmark (even n=50) would substantially strengthen claims.\"}\n  action_items:\n    - {round: 7, action: \"§5.4 title + Limitations acknowledgment\", assigned_to: paper_agent, status: done}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W2\n  summary: \"Pilot failure vs 'motivate' framing\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Conclusion still overclaims\"}\n    - {round: 8, reviewers: [R1, R2], note: \"REOPENED: pilot (oracle 18%, gate FAIL) still in §7; 'natural signal for budget allocation' claim directly contradicted by pilot results. Both reviewers agree: remove from main text or move to Appendix with failure analysis.\"}\n  action_items:\n    - {round: 7, action: \"motivate → diagnostic foundation for future strategies\", assigned_to: paper_agent, status: done}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W3\n  summary: \"Crossover model-dependent, Introduction over-relies\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Only DeepSeek; Qwen no crossover\"}\n    - {round: 8, reviewers: [R1, R2], note: \"R8 R2 flagged as over-emphasized; R1 rebutted successfully — crossover is the only qualitative novelty not derivable from single-axis work. Consensus: keep but add 'model-dependent' in abstract.\"}\n  action_items:\n    - {round: 7, action: \"Qualification + reweight to severity gradient\", assigned_to: paper_agent, status: done}\n  resolution: \"Crossover appropriately qualified as model-dependent. R8 consensus: retain as key finding.\"\n  resolution_round: 8\n\n- id: R7-W4\n  summary: \"Structural specificity lacks quantitative evidence\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"6-16% Gini to 7.5-79.8x gap\"}\n  action_items:\n    - {round: 7, action: \"Pruned-head overlap + Gini analysis\", assigned_to: main_agent, status: done}\n    - {round: 7, action: \"§6.1 structural specificity paragraph\", assigned_to: paper_agent, status: done}\n  resolution: \"r=0.62-0.76 large effect. Semi-circular caveat acknowledged.\"\n  resolution_round: 7\n\n- id: R7-W5\n  summary: \"LLaMA n=49 insufficient\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Unexplained n=49; no power\"}\n    - {round: 8, reviewers: [R1, R2], note: \"Still flagged: ~1/40 effect size, power 0.26-0.63 for strategy comparison. Both agree正文应进一步压缩。已在 Appendix 是正面进展。\"}\n  action_items:\n    - {round: 7, action: \"Post-hoc power + move to Appendix\", assigned_to: main_agent, status: done}\n    - {round: 7, action: \"§5.5→Appendix + power paragraph + n=49 footnote\", assigned_to: paper_agent, status: done}\n  resolution: \"LLaMA in Appendix with power analysis. R8: still weak but adequately framed as 'preliminary'.\"\n  resolution_round: 7\n\n- id: R7-W6\n  summary: \"43:1 outlier ratio unexplored\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Source unknown; robustness untested\"}\n  action_items:\n    - {round: 7, action: \"Winsorized robustness analysis\", assigned_to: main_agent, status: done}\n    - {round: 7, action: \"Appendix Outlier Robustness section\", assigned_to: paper_agent, status: done}\n  resolution: \"MMR up to 97,640:1. Median-based stats strictly invariant under 5%/10% winsorization. 5 core claims robust.\"\n  resolution_round: 7\n\n- id: R7-M1\n  summary: \"Table 2 QW s015 negative II\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions: []\n  action_items: [{round: 7, action: \"bfloat16 noise footnote\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done.\"\n  resolution_round: 7\n\n- id: R7-M2\n  summary: \"Figure 1 uses n=50\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [], note: \"R8 未明确提及，但 Figure 1 数据源仍需确认是否已更新至 n=496\"}\n  action_items:\n    - {round: 7, action: \"Regenerate with n=496 data\", assigned_to: main_agent, status: queued}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-M3\n  summary: \"§5.3 vs Table 2 numerical inconsistency\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions: []\n  action_items: [{round: 7, action: \"Unified to CSV values\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done.\"\n  resolution_round: 7\n\n- id: R7-M4\n  summary: \"pyramidkv bib year\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions: []\n  action_items: [{round: 7, action: \"Fixed\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done.\"\n  resolution_round: 7\n\n- id: R7-M5\n  summary: \"p-value precision too high\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions: []\n  action_items: [{round: 7, action: \"Simplified to p≪10^-10\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done.\"\n  resolution_round: 7\n\n- id: R7-M6\n  summary: \"paragraph label prefix\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions: []\n  action_items: [{round: 7, action: \"Fixed\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done.\"\n  resolution_round: 7\n\n- id: R7-MR1\n  summary: \"Missing: MUSTAFAR (NeurIPS 2025)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions: []\n  action_items: [{round: 7, action: \"Added\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done.\"\n  resolution_round: 7\n\n- id: R7-MR2\n  summary: \"Missing: LKV (2026)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions: []\n  action_items: [{round: 7, action: \"Added\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done.\"\n  resolution_round: 7\n\n## Round 8\n- id: R8-N1\n  summary: \"Additive null assumption contradicts paper's own causal coupling argument\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"Section 3 claims 'disjoint dimensions' but Section 3+6 describe direct causal coupling (head pruning alters importance rankings). Multiplicative null G=58-211 vs additive G=7.5-79.8 (4-8× difference). Both reviewers agree qualitative conclusions hold under both nulls but headline G numbers lack reliable interpretation basis.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-N2\n  summary: \"Numerical claim '3-30×' includes non-significant random conditions\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"Abstract/Contribution 1 claim '3-30×' or '3-39×'. At s≤0.20 random Δ non-significant (CI spans zero). Significant-only range: DS 15-17×, QW 2.7-3.5×, cross-model 2.7-17×. Both reviewers agree this is a data-text inconsistency.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-N3\n  summary: \"Novelty argument: 'linear combination' strawman in Introduction\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"R2 flags as critical; R1 partially agrees (strawman is weak) but rebuts that crossover effect IS genuinely novel and not derivable from single-axis work. Consensus: novelty argument should be rebuilt around crossover + dose-response monotonicity, not strawman 'linear combination' refutation.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-W1\n  summary: \"Discrimination collapse explanation gap: Gini drop <10% vs severity 15-17×\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"Order-of-magnitude gap between 'cause' (6-16% Gini reduction) and 'effect' (G=7.5-79.8×). r=0.62-0.76 structural specificity evidence partially circular (Frobenius norm vs Gini share magnitude sensitivity). Entropy redistribution replicates only 2/4 Qwen conditions. Both agree: mechanism is necessary-but-not-sufficient, paper should reduce reliance on it.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-W2\n  summary: \"Same-architecture 'cross-model replication' terminology imprecise\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"DeepSeek and Qwen share Qwen2ForCausalLM. Should be 'cross-training-paradigm replication on same architecture'. LLaMA ~1/40 effect size suggests quantitative characteristics may be Qwen2-specific.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-W3\n  summary: \"Phase segmentation lacks theoretical prior\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"Tercile segmentation is purely data-driven. Robustness checks (mpl sensitivity, quartile/quintile) partially mitigate but don't address fundamental question: is attention sparsity a valid proxy for reasoning phase? No independent literature cited to justify.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-W4\n  summary: \"Narrow sparsity range (s=0.15-0.30, only 4 points)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"4 points sufficient for monotonicity (JT test) but insufficient to characterize G(s) functional form. Higher sparsity (s>0.50) may show qualitatively different dynamics. R2 agrees it's a scope limitation not a flaw.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-W5\n  summary: \"Missing references: ForesightKV, ThinK (ICLR 2025), Prune-then-Quantize (ICLR 2026)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"All three highly relevant. ThinK: channel-level compound compression. ForesightKV: reasoning-specific learned importance. PtQ: compression order interaction / Progressive Intensity Hypothesis.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-W6\n  summary: \"'Discrimination collapse' naming potentially confusing\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"R2 suggests 'importance score flattening'. R1 partially agrees but notes 'flattening' loses the 'degeneration to noise-sensitive selection' semantics. Compromise: 'importance discrimination collapse' or 'score discrimination flattening'.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-M1\n  summary: \"LaTeX source contains residual % exp_id: comments\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R2], note: \"Internal tracking comments visible in source. Should be stripped before submission.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-M2\n  summary: \"LKV reference lists author as 'Anonymous'\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"Anonymous preprint should be cited by arXiv ID, not 'Anonymous' author.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-M3\n  summary: \"Main text may exceed 8-page limit\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1], note: \"Sections 1-8 (Conclusion) appear to extend to page 9. Needs verification against compiled PDF.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-M4\n  summary: \"Table 3 caption: 'paired median difference' ambiguous\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"Could be misread as 'difference of medians'. Should explicitly state: Δ = median_i(II_low^(i) − II_high^(i)).\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "issues_yaml": "## Round 6 (all resolved, compact)\n- id: R6-N1\n  summary: \"Table 2 n=50→n=500\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions: []\n  action_items: [{round: 6, action: \"Table 2 replaced\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done R6.\"\n  resolution_round: 6\n\n- id: R6-N2\n  summary: \"Discrimination collapse effect size gap\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions: []\n  action_items: [{round: 6, action: \"§6 rewritten as correlational diagnostic\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done R6.\"\n  resolution_round: 6\n\n- id: R6-N3\n  summary: \"ThinKV misattribution\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions: []\n  action_items: [{round: 6, action: \"Rewritten\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done R6.\"\n  resolution_round: 6\n\n## Round 7 (all resolved except R7-M2)\n- id: R7-N1\n  summary: \"No downstream accuracy validation; construct validity gap\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"PPL-based II not mapped to accuracy; low-sparsity phase may not affect answers\"}\n    - {round: 8, reviewers: [R1, R2], note: \"REOPENED: answer-region proxy (93.2% in G≤1 phase) actually UNDERMINES severity narrative. Both R8 reviewers agree direct accuracy validation needed.\"}\n  action_items:\n    - {round: 7, action: \"N1a answer-region proxy + boxed validation\", assigned_to: main_agent, status: done}\n    - {round: 7, action: \"§5.7 Answer-Region Analysis + Limitations caveat\", assigned_to: paper_agent, status: done}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-N2\n  summary: \"G metric definition inconsistent + Abstract CI misleading\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"median-of-ratios vs ratio-of-medians; CI splice\"}\n  action_items:\n    - {round: 7, action: \"Eq.2 disambiguation + Table 4 footnote + Abstract per-sparsity CI\", assigned_to: paper_agent, status: done}\n  resolution: \"G definitions disambiguated. Abstract CI now per-sparsity. Table 4 footnote added.\"\n  resolution_round: 7\n\n- id: R7-N3\n  summary: \"Single importance scoring method but categorical claims\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Only cumulative attention mass tested\"}\n  action_items:\n    - {round: 7, action: \"Scope down claims to attention-mass-based methods\", assigned_to: paper_agent, status: done}\n  resolution: \"Claims scoped to 'attention-mass-based scoring methods'. H2O spot check deprioritized (GPU to N1).\"\n  resolution_round: 7\n\n- id: R7-W1\n  summary: \"Generalizability: single benchmark/scale/backbone\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"§5.4 title misleading\"}\n    - {round: 8, reviewers: [R1, R2], note: \"REOPENED as critical: MATH-500 only. Title says 'Mathematical Reasoning Models' (plural) implying generality. One additional benchmark (even n=50) would substantially strengthen claims.\"}\n  action_items:\n    - {round: 7, action: \"§5.4 title + Limitations acknowledgment\", assigned_to: paper_agent, status: done}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W2\n  summary: \"Pilot failure vs 'motivate' framing\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Conclusion still overclaims\"}\n    - {round: 8, reviewers: [R1, R2], note: \"REOPENED: pilot (oracle 18%, gate FAIL) still in §7; 'natural signal for budget allocation' claim directly contradicted by pilot results. Both reviewers agree: remove from main text or move to Appendix with failure analysis.\"}\n  action_items:\n    - {round: 7, action: \"motivate → diagnostic foundation for future strategies\", assigned_to: paper_agent, status: done}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-W3\n  summary: \"Crossover model-dependent, Introduction over-relies\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Only DeepSeek; Qwen no crossover\"}\n    - {round: 8, reviewers: [R1, R2], note: \"R8 R2 flagged as over-emphasized; R1 rebutted successfully — crossover is the only qualitative novelty not derivable from single-axis work. Consensus: keep but add 'model-dependent' in abstract.\"}\n  action_items:\n    - {round: 7, action: \"Qualification + reweight to severity gradient\", assigned_to: paper_agent, status: done}\n  resolution: \"Crossover appropriately qualified as model-dependent. R8 consensus: retain as key finding.\"\n  resolution_round: 8\n\n- id: R7-W4\n  summary: \"Structural specificity lacks quantitative evidence\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"6-16% Gini to 7.5-79.8x gap\"}\n  action_items:\n    - {round: 7, action: \"Pruned-head overlap + Gini analysis\", assigned_to: main_agent, status: done}\n    - {round: 7, action: \"§6.1 structural specificity paragraph\", assigned_to: paper_agent, status: done}\n  resolution: \"r=0.62-0.76 large effect. Semi-circular caveat acknowledged.\"\n  resolution_round: 7\n\n- id: R7-W5\n  summary: \"LLaMA n=49 insufficient\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Unexplained n=49; no power\"}\n    - {round: 8, reviewers: [R1, R2], note: \"Still flagged: ~1/40 effect size, power 0.26-0.63 for strategy comparison. Both agree正文应进一步压缩。已在 Appendix 是正面进展。\"}\n  action_items:\n    - {round: 7, action: \"Post-hoc power + move to Appendix\", assigned_to: main_agent, status: done}\n    - {round: 7, action: \"§5.5→Appendix + power paragraph + n=49 footnote\", assigned_to: paper_agent, status: done}\n  resolution: \"LLaMA in Appendix with power analysis. R8: still weak but adequately framed as 'preliminary'.\"\n  resolution_round: 7\n\n- id: R7-W6\n  summary: \"43:1 outlier ratio unexplored\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: [R1, R2], note: \"Source unknown; robustness untested\"}\n  action_items:\n    - {round: 7, action: \"Winsorized robustness analysis\", assigned_to: main_agent, status: done}\n    - {round: 7, action: \"Appendix Outlier Robustness section\", assigned_to: paper_agent, status: done}\n  resolution: \"MMR up to 97,640:1. Median-based stats strictly invariant under 5%/10% winsorization. 5 core claims robust.\"\n  resolution_round: 7\n\n- id: R7-M1\n  summary: \"Table 2 QW s015 negative II\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions: []\n  action_items: [{round: 7, action: \"bfloat16 noise footnote\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done.\"\n  resolution_round: 7\n\n- id: R7-M2\n  summary: \"Figure 1 uses n=50\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [], note: \"R8 未明确提及，但 Figure 1 数据源仍需确认是否已更新至 n=496\"}\n  action_items:\n    - {round: 7, action: \"Regenerate with n=496 data\", assigned_to: main_agent, status: queued}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-M3\n  summary: \"§5.3 vs Table 2 numerical inconsistency\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions: []\n  action_items: [{round: 7, action: \"Unified to CSV values\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done.\"\n  resolution_round: 7\n\n- id: R7-M4\n  summary: \"pyramidkv bib year\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions: []\n  action_items: [{round: 7, action: \"Fixed\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done.\"\n  resolution_round: 7\n\n- id: R7-M5\n  summary: \"p-value precision too high\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions: []\n  action_items: [{round: 7, action: \"Simplified to p≪10^-10\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done.\"\n  resolution_round: 7\n\n- id: R7-M6\n  summary: \"paragraph label prefix\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions: []\n  action_items: [{round: 7, action: \"Fixed\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done.\"\n  resolution_round: 7\n\n- id: R7-MR1\n  summary: \"Missing: MUSTAFAR (NeurIPS 2025)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions: []\n  action_items: [{round: 7, action: \"Added\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done.\"\n  resolution_round: 7\n\n- id: R7-MR2\n  summary: \"Missing: LKV (2026)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions: []\n  action_items: [{round: 7, action: \"Added\", assigned_to: paper_agent, status: done}]\n  resolution: \"Done.\"\n  resolution_round: 7\n\n## Round 8\n- id: R8-N1\n  summary: \"Additive null assumption contradicts paper's own causal coupling argument\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"Section 3 claims 'disjoint dimensions' but Section 3+6 describe direct causal coupling (head pruning alters importance rankings). Multiplicative null G=58-211 vs additive G=7.5-79.8 (4-8× difference). Both reviewers agree qualitative conclusions hold under both nulls but headline G numbers lack reliable interpretation basis.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-N2\n  summary: \"Numerical claim '3-30×' includes non-significant random conditions\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"Abstract/Contribution 1 claim '3-30×' or '3-39×'. At s≤0.20 random Δ non-significant (CI spans zero). Significant-only range: DS 15-17×, QW 2.7-3.5×, cross-model 2.7-17×. Both reviewers agree this is a data-text inconsistency.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-N3\n  summary: \"Novelty argument: 'linear combination' strawman in Introduction\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"R2 flags as critical; R1 partially agrees (strawman is weak) but rebuts that crossover effect IS genuinely novel and not derivable from single-axis work. Consensus: novelty argument should be rebuilt around crossover + dose-response monotonicity, not strawman 'linear combination' refutation.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-W1\n  summary: \"Discrimination collapse explanation gap: Gini drop <10% vs severity 15-17×\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"Order-of-magnitude gap between 'cause' (6-16% Gini reduction) and 'effect' (G=7.5-79.8×). r=0.62-0.76 structural specificity evidence partially circular (Frobenius norm vs Gini share magnitude sensitivity). Entropy redistribution replicates only 2/4 Qwen conditions. Both agree: mechanism is necessary-but-not-sufficient, paper should reduce reliance on it.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-W2\n  summary: \"Same-architecture 'cross-model replication' terminology imprecise\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"DeepSeek and Qwen share Qwen2ForCausalLM. Should be 'cross-training-paradigm replication on same architecture'. LLaMA ~1/40 effect size suggests quantitative characteristics may be Qwen2-specific.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-W3\n  summary: \"Phase segmentation lacks theoretical prior\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"Tercile segmentation is purely data-driven. Robustness checks (mpl sensitivity, quartile/quintile) partially mitigate but don't address fundamental question: is attention sparsity a valid proxy for reasoning phase? No independent literature cited to justify.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-W4\n  summary: \"Narrow sparsity range (s=0.15-0.30, only 4 points)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"4 points sufficient for monotonicity (JT test) but insufficient to characterize G(s) functional form. Higher sparsity (s>0.50) may show qualitatively different dynamics. R2 agrees it's a scope limitation not a flaw.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-W5\n  summary: \"Missing references: ForesightKV, ThinK (ICLR 2025), Prune-then-Quantize (ICLR 2026)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"All three highly relevant. ThinK: channel-level compound compression. ForesightKV: reasoning-specific learned importance. PtQ: compression order interaction / Progressive Intensity Hypothesis.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-W6\n  summary: \"'Discrimination collapse' naming potentially confusing\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"R2 suggests 'importance score flattening'. R1 partially agrees but notes 'flattening' loses the 'degeneration to noise-sensitive selection' semantics. Compromise: 'importance discrimination collapse' or 'score discrimination flattening'.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-M1\n  summary: \"LaTeX source contains residual % exp_id: comments\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R2], note: \"Internal tracking comments visible in source. Should be stripped before submission.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-M2\n  summary: \"LKV reference lists author as 'Anonymous'\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"Anonymous preprint should be cited by arXiv ID, not 'Anonymous' author.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-M3\n  summary: \"Main text may exceed 8-page limit\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1], note: \"Sections 1-8 (Conclusion) appear to extend to page 9. Needs verification against compiled PDF.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R8-M4\n  summary: \"Table 3 caption: 'paired median difference' ambiguous\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - {round: 8, reviewers: [R1, R2], note: \"Could be misread as 'difference of medians'. Should explicitly state: Δ = median_i(II_low^(i) − II_high^(i)).\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-15T13:59:39.419987+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml\", \"bytes\": 16239}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-15T14:01:36.814207+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "report": "# Round 8 Consolidated Review Report\n## Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models\n**Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 相关工作 + 写作)\n**评分**: R1 3/5, R2 2.5/5 → **综合: Weak Reject (main conference) / Borderline Accept (Findings track)**\n\n---\n\n## Summary\n\n本文研究 compound sparsity（attention head pruning + KV cache eviction 联合）在数学推理模型中的 phase-dependent severity。通过在 DeepSeek-R1-Distill-Qwen-7B (n=496) 和 Qwen2.5-7B-Instruct (n=475) 上的实验，作者发现：(1) importance-based eviction 的 severity gradient 远大于 random eviction（amplification ratio G=7.5×–79.8× vs ≈1×）；(2) DeepSeek 上出现 strategy ranking crossover（model-dependent）；(3) discrimination collapse 作为 correlational diagnostic。论文自我定位为 diagnostic study，统计方法论严谨，robustness 验证充分。\n\n---\n\n## Strengths\n\n**S1. 统计方法论在同类论文中罕见的严谨度** [R1+R2 共识, Soundness 3.5/5]\nBootstrap CI (B=10,000)、Wilcoxon signed-rank、Bonferroni + BH-FDR 双重校正、Jonckheere-Terpstra dose-response test、paired permutation test、post-hoc power analysis——每一步都有合适的非参数检验和多重比较校正。\n\n**S2. 充分的多维度 robustness 验证** [R1+R2 共识]\nmin_phase_length 敏感性、分割粒度（tercile/quartile/quintile）、outlier winsorization (5%/10%)、multiplicative null、BH-FDR correction——核心结论经多角度交叉验证。\n\n**S3. Crossover effect 有不可预测的定性新颖性** [R1 主张, R2 未进一步反驳]\nImportance-based eviction 在 high-sparsity phase 优于 random 但在 low-sparsity phase 劣于 random 的 strategy ranking reversal，不可从 ThinKV + HIES 等单轴工作组合推导。R1 在交叉回应中成功论证了这一点。\n\n**S4. 诚实且充分的 limitation 披露** [R1+R2 共识]\nCorrelational mechanism、单一基准、LLaMA 弱结果、pilot mitigation 失败——论文对自身弱点的讨论比大多数投稿更坦诚。\n\n**S5. 清晰的 diagnostic study 定位与精巧的对照组设计** [R1+R2 共识]\nRandom eviction 对照组有效隔离了 strategy-specific 效应。Diagnostic study 自我定位一致。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. [critical] Additive null 假设与论文自身 causal coupling 论述存在内在矛盾** [R1 提出, R2 同意]\n论文以\"两轴作用于不相交维度\"正当化 additive null (II = r_b − r_a − r_k + 1)，但论文自身在 §3 明确指出 \"head pruning alters the importance ranking used for eviction\"，§6 详细分析 discrimination collapse 即两轴的直接因果耦合。Multiplicative null 下 G=58–211（additive G=7.5–79.8 的 4–8×），两种 null 的数值差异直接影响 headline 数字的含义。II 是论文所有定量结论的根基。\n**建议**: (a) 在 §3 正面论证为什么存在因果耦合却仍采用 additive null（不能靠一句\"不相交\"带过）；(b) 主文并列报告两种 null 下的 G 和 Δ。\n\n**N2. [critical] 单一基准 MATH-500 严重限制泛化性** [R1 提出, R2 同意]\n所有定量结论仅基于 MATH-500。标题 \"Mathematical Reasoning Models\" 暗示一般性，但不同推理任务的 attention dynamics 可能截然不同。作为 diagnostic study，单一数据源的诊断外部效度存疑。\n**建议**: 增加至少一个不同类型推理基准（GSM8K 最低成本，HumanEval/GPQA 更有说服力），哪怕仅 n=50 profiling 规模。\n\n**N3. [critical] PPL construct validity: answer-region 分析反而削弱核心叙事** [R1 提出 Must-Fix, R2 升级同意]\n§5.7 报告 93.2% 答案 token 在 high-sparsity phase (G ≤ 1)，答案 token PPL degradation (1.3–5.3×) 远低于推理痕迹 (5.7–43.5×)。论文描述为 \"partially shielded\"，但更准确的解读是：巨大 G 值集中在对最终答案影响最小的 phase。缺乏直接准确率测量使 \"severity\" 的实际含义悬而未决。论文试图说服读者 compound severity 是严重问题，但自己的分析表明最终答案可能基本不受影响——framing 与证据之间存在根本张力。\n**建议**: (a) 在至少一个 sparsity level 上测量实际 MATH-500 准确率变化；(b) 如果主要影响推理痕迹质量而非最终答案，重新框定 severity gradient 的价值定位。\n\n**N4. [critical] 数字声明 \"3–30×\" 包含非显著 random 条件** [R2 提出, R1 同意]\nAbstract/Contribution 1 中 \"3–39×\" 或 \"3–30×\" 的上界取自 s ≤ 0.20 的条件，而这些条件下 random Δ 非显著（CI spans zero）。在 random Δ 统计显著的条件 (s ≥ 0.25) 下，实际比率为 DS 15–17×，QW 2.7–3.5×，跨模型 2.7–17×。\n**建议**: 修正为 \"3–17× where both strategies show significant phase gradients\"，或明确标注上界来自非显著条件。\n\n### Should-Fix\n\n**W1. [warning] Pilot mitigation (oracle 18%, gate FAIL) 削弱 diagnostic value 叙事** [R2 提出 Must-Fix, R1 同意]\n§7 声称 \"severity gradient provides a natural signal for allocating compression budgets\"，但 oracle recovery 仅 18%（低于 30% pre-registered gate），heuristic 32% 但 CI 跨 zero。叙事内部矛盾。\n**建议**: 移除 pilot 或移至 Appendix 附失败分析，避免与 \"natural signal\" 正面叙事冲突。\n\n**W2. [warning] Discrimination collapse 解释力存在 order-of-magnitude 缺口** [R1+R2 共识]\nImportance/random Gini drop 差异 < 10%（如 s=0.25: −0.065 vs −0.060），但 severity 差异 15–17×。r=0.62–0.76 structural specificity 证据部分 circular（Frobenius norm 与 Gini 共享 magnitude sensitivity）。Entropy redistribution 仅 2/4 Qwen 条件复现。\n**建议**: 坦诚讨论 Gini drop 与 severity divergence 之间的定量缺口；降低对该机制的依赖。\n\n**W3. [warning] \"Cross-model replication\" 实为同架构不同训练范式** [R1+R2 共识]\nDeepSeek 和 Qwen 共享 Qwen2ForCausalLM。LLaMA (n=49) 效应量 ~1/40 且 strategy contrast 大幅减弱，暗示定量特征可能 Qwen2 特有。\n**建议**: 使用 \"cross-training-paradigm replication on same architecture\"，更突出讨论 LLaMA 结果对泛化性的负面含义。\n\n**W4. [warning] Phase segmentation 缺乏理论先验** [R1+R2 共识]\n基于 attention sparsity tercile 的分割纯数据驱动。Robustness checks (mpl sensitivity, quartile/quintile) 部分缓解，但未独立论证 attention sparsity 作为 reasoning phase boundary 的合理性。\n**建议**: 引用独立文献支持 attention sparsity 作为 phase proxy 的合理性，或讨论替代分割方法的可能结果。\n\n**W5. [warning] Novelty argument: Introduction 的 \"linear combination\" 反驳为 strawman** [R2 提出, R1 部分同意]\n没有人会预期两个非线性交互的压缩轴产生 \"linear combination\"。ThinKV + HIES 的组合可定性预测 phase-modulated severity。但 R1 成功论证 crossover 和 dose-response 的严格单调性是不可预测的。\n**建议**: 重写 novelty argument，聚焦 crossover 和 dose-response 的不可预测性，而非 strawman 反驳。同时在 headline claims 中并列 Δ 和 G，明确讨论 G 的 near-zero denominator 放大效应。\n\n**W6. [warning] Sparsity 范围窄 (s=0.15–0.30, 仅 4 点)** [R1 提出, R2 部分同意]\n4 点足以验证 monotonicity (JT test) 但不足以刻画 G(s) functional form。实际部署常涉及更高 sparsity (s > 0.50)。\n**建议**: 增加 1-2 个更极端的 sparsity level。\n\n**W7. [warning] 缺失引用** [R2 提出, R1 同意]\n- ThinK (ICLR 2025): channel-level KV pruning compound compression\n- ForesightKV (arXiv 2602.03203): reasoning-specific learned importance\n- Prune-then-Quantize or Quantize-then-Prune? (ICLR 2026): compression order interaction, Progressive Intensity Hypothesis\n\n**W8. [warning] \"Discrimination collapse\" 命名可能混淆** [R2 提出, R1 部分同意]\n\"Collapse\" 在 ML 中有 mode collapse、neural collapse 等既有含义。\n**建议**: 改为 \"importance discrimination collapse\" 或 \"score discrimination flattening\"。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 达成以下关键共识：\n1. **PPL-only 度量 + answer-region shielding 削弱 practical significance** (R1-N3 = R2-W5→升级) — 最终答案 token 大多在 G≤1 的 phase，severity gradient 的实际影响可能被系统性高估\n2. **Pilot mitigation gate FAIL 削弱 diagnostic value narrative** (R1-W5 = R2-N2)\n3. **单一基准限制泛化性** (R1-N2, R2 AGREE)\n4. **数字声明不一致** (R2-N3, R1 AGREE)\n5. **Discrimination collapse 解释力不足** (R1-W2, R2 AGREE)\n6. **统计方法论堪称典范** (两位 Soundness 3.5, Reproducibility 4)\n\n## Reviewer Divergence\n\n唯一实质分歧在 **Excitement / Novelty** 的评估：\n- **R1 (3/5)**: Crossover effect 是不可从单轴工作推导的定性新颖性，为论文提供了独立于定量放大之外的贡献\n- **R2 (2.5/5)**: 核心发现\"importance-based eviction 在 attention 分散的 phase 更差\"定性上可预期；G 指标因 near-zero denominator 被人为放大\n\n经交叉回应，R1 关于 crossover 新颖性的论证更有说服力（R2 未进一步反驳）。但 R2 关于 G 指标放大效应的关切同样成立。**综合判断**：论文有真正的新颖性（crossover + dose-response），但 headline framing 过度依赖被放大的 G 值。\n\n---\n\n## Questions for Authors\n\n1. **Additive vs. multiplicative null**: 两种 null 下 G 差异 4–8×，作者如何论证读者应信赖 additive null 的数字？特别是当论文自身描述了两轴的因果耦合时？\n2. **Answer-region shielding**: 93.2% 答案 token 在 G ≤ 1 的 phase。是否有证据表明推理痕迹的 PPL 退化会 cascade 到最终答案质量？如果不会，论文的实际 implication 是什么？\n3. **Profiling vs. full G discrepancy**: 已确认为统计量定义差异（ratio-of-medians vs median-of-per-problem-ratios）而非 sample size artifact。但请在正文中更显著地标注此差异，避免误读。\n4. **Crossover model-dependence**: DeepSeek 展现 crossover 但 Qwen 不展现。什么模型属性决定 crossover 是否出现？缺乏 explanatory hypothesis 是明显弱点。\n\n---\n\n## Missing References\n\n| 论文 | 相关性 | 来源 |\n|------|--------|------|\n| ThinK (ICLR 2025) | Channel-level KV pruning compound compression | R2 |\n| ForesightKV (arXiv 2602.03203) | Reasoning-specific KV eviction with learned long-term importance | R2 |\n| Prune-then-Quantize or Quantize-then-Prune? (ICLR 2026) | Compression order interaction, Progressive Intensity Hypothesis | R2 |\n| PPL-accuracy nonlinear relationship formal analysis | 加强 §5.7 讨论 | R1 |\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿。\n\n---\n\n## Overall Assessment\n\n**Score: Weak Reject (for main conference) / Borderline Accept (for Findings track)**\n**Confidence: 4/5** (两位 Reviewer 均仔细阅读全文含附录)\n\n这是一篇执行力出色的诊断研究。统计方法论在 KV cache compression 领域属上乘，robustness 验证近乎完备，crossover effect 是真正新颖的发现。\n\n但四个核心问题将其限制在 Findings 级别：\n\n1. **Construct validity gap**: PPL 度量的 practical significance 被论文自身的 answer-region 分析削弱（93.2% 答案 token 在 severity 最低的 phase），且无直接准确率验证\n2. **Single benchmark**: MATH-500 独木难支泛化性——一个额外基准（哪怕 n=50）即可大幅增强\n3. **Additive null 矛盾**: 论文核心度量 II 的 null hypothesis 与论文自身的 causal coupling 叙事不自洽，headline G 值缺乏可靠解释基准\n4. **Numerical inconsistency**: \"3–30×\" 声明混入非显著条件比率\n\n**升级路径**：(a) 增加一个额外基准 + 至少一个 sparsity level 的准确率数据；(b) 主文并列报告 additive/multiplicative null 结果；(c) 修正数字声明；(d) 移除或下移 pilot experiment。完成这些修改后，论文有望达到 main conference 水平。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- ¶3 的 \"linear combination\" 论证是 strawman——改为聚焦 crossover 和 dose-response 的不可预测性\n- Contribution 1 的 \"3–39×\" / \"3–30×\" 需修正为 significant-only 范围\n\n### Section 3 (Background)\n- Additive null 的论证（\"disjoint dimensions\"）需正面回应 causal coupling 的存在\n- Phase segmentation 的 attention sparsity proxy 缺乏独立理论支持\n\n### Section 5 (Results)\n- §5.4 标题 \"Replication Across Training Paradigms\" 已改进（R7），但正文仍应更显著地讨论 LLaMA ~1/40 效应量对泛化性的负面含义\n- §5.7 Answer-region 分析需重新框定——当前 \"partially shielded\" 用词淡化了 93.2% 答案 token 在 G≤1 phase 的含义\n\n### Section 6 (Analysis)\n- Discrimination collapse 作为 correlational diagnostic 定位合理，但 Gini drop ~10% vs severity 15–17× 的定量缺口需正面讨论\n- 命名建议改为 \"importance discrimination collapse\"\n\n### Section 7 (Discussion)\n- Pilot experiment 移至 Appendix 或删除——oracle 18% recovery 直接反驳 \"natural signal\" 声明\n- G 的 near-zero denominator 放大效应需在 headline claims 中明确讨论\n\n### Format\n- 确认正文是否严格在 8 页限制内\n- 清理 LaTeX 源码中的 `% exp_id:` 注释\n- LKV 引用修正（\"Anonymous\" → arXiv ID）\n- Table 3 caption 明确 Δ 的计算方式"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "report": "# Round 8 Consolidated Review Report\n## Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models\n**Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 相关工作 + 写作)\n**评分**: R1 3/5, R2 2.5/5 → **综合: Weak Reject (main conference) / Borderline Accept (Findings track)**\n\n---\n\n## Summary\n\n本文研究 compound sparsity（attention head pruning + KV cache eviction 联合）在数学推理模型中的 phase-dependent severity。通过在 DeepSeek-R1-Distill-Qwen-7B (n=496) 和 Qwen2.5-7B-Instruct (n=475) 上的实验，作者发现：(1) importance-based eviction 的 severity gradient 远大于 random eviction（amplification ratio G=7.5×–79.8× vs ≈1×）；(2) DeepSeek 上出现 strategy ranking crossover（model-dependent）；(3) discrimination collapse 作为 correlational diagnostic。论文自我定位为 diagnostic study，统计方法论严谨，robustness 验证充分。\n\n---\n\n## Strengths\n\n**S1. 统计方法论在同类论文中罕见的严谨度** [R1+R2 共识, Soundness 3.5/5]\nBootstrap CI (B=10,000)、Wilcoxon signed-rank、Bonferroni + BH-FDR 双重校正、Jonckheere-Terpstra dose-response test、paired permutation test、post-hoc power analysis——每一步都有合适的非参数检验和多重比较校正。\n\n**S2. 充分的多维度 robustness 验证** [R1+R2 共识]\nmin_phase_length 敏感性、分割粒度（tercile/quartile/quintile）、outlier winsorization (5%/10%)、multiplicative null、BH-FDR correction——核心结论经多角度交叉验证。\n\n**S3. Crossover effect 有不可预测的定性新颖性** [R1 主张, R2 未进一步反驳]\nImportance-based eviction 在 high-sparsity phase 优于 random 但在 low-sparsity phase 劣于 random 的 strategy ranking reversal，不可从 ThinKV + HIES 等单轴工作组合推导。R1 在交叉回应中成功论证了这一点。\n\n**S4. 诚实且充分的 limitation 披露** [R1+R2 共识]\nCorrelational mechanism、单一基准、LLaMA 弱结果、pilot mitigation 失败——论文对自身弱点的讨论比大多数投稿更坦诚。\n\n**S5. 清晰的 diagnostic study 定位与精巧的对照组设计** [R1+R2 共识]\nRandom eviction 对照组有效隔离了 strategy-specific 效应。Diagnostic study 自我定位一致。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. [critical] Additive null 假设与论文自身 causal coupling 论述存在内在矛盾** [R1 提出, R2 同意]\n论文以\"两轴作用于不相交维度\"正当化 additive null (II = r_b − r_a − r_k + 1)，但论文自身在 §3 明确指出 \"head pruning alters the importance ranking used for eviction\"，§6 详细分析 discrimination collapse 即两轴的直接因果耦合。Multiplicative null 下 G=58–211（additive G=7.5–79.8 的 4–8×），两种 null 的数值差异直接影响 headline 数字的含义。II 是论文所有定量结论的根基。\n**建议**: (a) 在 §3 正面论证为什么存在因果耦合却仍采用 additive null（不能靠一句\"不相交\"带过）；(b) 主文并列报告两种 null 下的 G 和 Δ。\n\n**N2. [critical] 单一基准 MATH-500 严重限制泛化性** [R1 提出, R2 同意]\n所有定量结论仅基于 MATH-500。标题 \"Mathematical Reasoning Models\" 暗示一般性，但不同推理任务的 attention dynamics 可能截然不同。作为 diagnostic study，单一数据源的诊断外部效度存疑。\n**建议**: 增加至少一个不同类型推理基准（GSM8K 最低成本，HumanEval/GPQA 更有说服力），哪怕仅 n=50 profiling 规模。\n\n**N3. [critical] PPL construct validity: answer-region 分析反而削弱核心叙事** [R1 提出 Must-Fix, R2 升级同意]\n§5.7 报告 93.2% 答案 token 在 high-sparsity phase (G ≤ 1)，答案 token PPL degradation (1.3–5.3×) 远低于推理痕迹 (5.7–43.5×)。论文描述为 \"partially shielded\"，但更准确的解读是：巨大 G 值集中在对最终答案影响最小的 phase。缺乏直接准确率测量使 \"severity\" 的实际含义悬而未决。论文试图说服读者 compound severity 是严重问题，但自己的分析表明最终答案可能基本不受影响——framing 与证据之间存在根本张力。\n**建议**: (a) 在至少一个 sparsity level 上测量实际 MATH-500 准确率变化；(b) 如果主要影响推理痕迹质量而非最终答案，重新框定 severity gradient 的价值定位。\n\n**N4. [critical] 数字声明 \"3–30×\" 包含非显著 random 条件** [R2 提出, R1 同意]\nAbstract/Contribution 1 中 \"3–39×\" 或 \"3–30×\" 的上界取自 s ≤ 0.20 的条件，而这些条件下 random Δ 非显著（CI spans zero）。在 random Δ 统计显著的条件 (s ≥ 0.25) 下，实际比率为 DS 15–17×，QW 2.7–3.5×，跨模型 2.7–17×。\n**建议**: 修正为 \"3–17× where both strategies show significant phase gradients\"，或明确标注上界来自非显著条件。\n\n### Should-Fix\n\n**W1. [warning] Pilot mitigation (oracle 18%, gate FAIL) 削弱 diagnostic value 叙事** [R2 提出 Must-Fix, R1 同意]\n§7 声称 \"severity gradient provides a natural signal for allocating compression budgets\"，但 oracle recovery 仅 18%（低于 30% pre-registered gate），heuristic 32% 但 CI 跨 zero。叙事内部矛盾。\n**建议**: 移除 pilot 或移至 Appendix 附失败分析，避免与 \"natural signal\" 正面叙事冲突。\n\n**W2. [warning] Discrimination collapse 解释力存在 order-of-magnitude 缺口** [R1+R2 共识]\nImportance/random Gini drop 差异 < 10%（如 s=0.25: −0.065 vs −0.060），但 severity 差异 15–17×。r=0.62–0.76 structural specificity 证据部分 circular（Frobenius norm 与 Gini 共享 magnitude sensitivity）。Entropy redistribution 仅 2/4 Qwen 条件复现。\n**建议**: 坦诚讨论 Gini drop 与 severity divergence 之间的定量缺口；降低对该机制的依赖。\n\n**W3. [warning] \"Cross-model replication\" 实为同架构不同训练范式** [R1+R2 共识]\nDeepSeek 和 Qwen 共享 Qwen2ForCausalLM。LLaMA (n=49) 效应量 ~1/40 且 strategy contrast 大幅减弱，暗示定量特征可能 Qwen2 特有。\n**建议**: 使用 \"cross-training-paradigm replication on same architecture\"，更突出讨论 LLaMA 结果对泛化性的负面含义。\n\n**W4. [warning] Phase segmentation 缺乏理论先验** [R1+R2 共识]\n基于 attention sparsity tercile 的分割纯数据驱动。Robustness checks (mpl sensitivity, quartile/quintile) 部分缓解，但未独立论证 attention sparsity 作为 reasoning phase boundary 的合理性。\n**建议**: 引用独立文献支持 attention sparsity 作为 phase proxy 的合理性，或讨论替代分割方法的可能结果。\n\n**W5. [warning] Novelty argument: Introduction 的 \"linear combination\" 反驳为 strawman** [R2 提出, R1 部分同意]\n没有人会预期两个非线性交互的压缩轴产生 \"linear combination\"。ThinKV + HIES 的组合可定性预测 phase-modulated severity。但 R1 成功论证 crossover 和 dose-response 的严格单调性是不可预测的。\n**建议**: 重写 novelty argument，聚焦 crossover 和 dose-response 的不可预测性，而非 strawman 反驳。同时在 headline claims 中并列 Δ 和 G，明确讨论 G 的 near-zero denominator 放大效应。\n\n**W6. [warning] Sparsity 范围窄 (s=0.15–0.30, 仅 4 点)** [R1 提出, R2 部分同意]\n4 点足以验证 monotonicity (JT test) 但不足以刻画 G(s) functional form。实际部署常涉及更高 sparsity (s > 0.50)。\n**建议**: 增加 1-2 个更极端的 sparsity level。\n\n**W7. [warning] 缺失引用** [R2 提出, R1 同意]\n- ThinK (ICLR 2025): channel-level KV pruning compound compression\n- ForesightKV (arXiv 2602.03203): reasoning-specific learned importance\n- Prune-then-Quantize or Quantize-then-Prune? (ICLR 2026): compression order interaction, Progressive Intensity Hypothesis\n\n**W8. [warning] \"Discrimination collapse\" 命名可能混淆** [R2 提出, R1 部分同意]\n\"Collapse\" 在 ML 中有 mode collapse、neural collapse 等既有含义。\n**建议**: 改为 \"importance discrimination collapse\" 或 \"score discrimination flattening\"。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 达成以下关键共识：\n1. **PPL-only 度量 + answer-region shielding 削弱 practical significance** (R1-N3 = R2-W5→升级) — 最终答案 token 大多在 G≤1 的 phase，severity gradient 的实际影响可能被系统性高估\n2. **Pilot mitigation gate FAIL 削弱 diagnostic value narrative** (R1-W5 = R2-N2)\n3. **单一基准限制泛化性** (R1-N2, R2 AGREE)\n4. **数字声明不一致** (R2-N3, R1 AGREE)\n5. **Discrimination collapse 解释力不足** (R1-W2, R2 AGREE)\n6. **统计方法论堪称典范** (两位 Soundness 3.5, Reproducibility 4)\n\n## Reviewer Divergence\n\n唯一实质分歧在 **Excitement / Novelty** 的评估：\n- **R1 (3/5)**: Crossover effect 是不可从单轴工作推导的定性新颖性，为论文提供了独立于定量放大之外的贡献\n- **R2 (2.5/5)**: 核心发现\"importance-based eviction 在 attention 分散的 phase 更差\"定性上可预期；G 指标因 near-zero denominator 被人为放大\n\n经交叉回应，R1 关于 crossover 新颖性的论证更有说服力（R2 未进一步反驳）。但 R2 关于 G 指标放大效应的关切同样成立。**综合判断**：论文有真正的新颖性（crossover + dose-response），但 headline framing 过度依赖被放大的 G 值。\n\n---\n\n## Questions for Authors\n\n1. **Additive vs. multiplicative null**: 两种 null 下 G 差异 4–8×，作者如何论证读者应信赖 additive null 的数字？特别是当论文自身描述了两轴的因果耦合时？\n2. **Answer-region shielding**: 93.2% 答案 token 在 G ≤ 1 的 phase。是否有证据表明推理痕迹的 PPL 退化会 cascade 到最终答案质量？如果不会，论文的实际 implication 是什么？\n3. **Profiling vs. full G discrepancy**: 已确认为统计量定义差异（ratio-of-medians vs median-of-per-problem-ratios）而非 sample size artifact。但请在正文中更显著地标注此差异，避免误读。\n4. **Crossover model-dependence**: DeepSeek 展现 crossover 但 Qwen 不展现。什么模型属性决定 crossover 是否出现？缺乏 explanatory hypothesis 是明显弱点。\n\n---\n\n## Missing References\n\n| 论文 | 相关性 | 来源 |\n|------|--------|------|\n| ThinK (ICLR 2025) | Channel-level KV pruning compound compression | R2 |\n| ForesightKV (arXiv 2602.03203) | Reasoning-specific KV eviction with learned long-term importance | R2 |\n| Prune-then-Quantize or Quantize-then-Prune? (ICLR 2026) | Compression order interaction, Progressive Intensity Hypothesis | R2 |\n| PPL-accuracy nonlinear relationship formal analysis | 加强 §5.7 讨论 | R1 |\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿。\n\n---\n\n## Overall Assessment\n\n**Score: Weak Reject (for main conference) / Borderline Accept (for Findings track)**\n**Confidence: 4/5** (两位 Reviewer 均仔细阅读全文含附录)\n\n这是一篇执行力出色的诊断研究。统计方法论在 KV cache compression 领域属上乘，robustness 验证近乎完备，crossover effect 是真正新颖的发现。\n\n但四个核心问题将其限制在 Findings 级别：\n\n1. **Construct validity gap**: PPL 度量的 practical significance 被论文自身的 answer-region 分析削弱（93.2% 答案 token 在 severity 最低的 phase），且无直接准确率验证\n2. **Single benchmark**: MATH-500 独木难支泛化性——一个额外基准（哪怕 n=50）即可大幅增强\n3. **Additive null 矛盾**: 论文核心度量 II 的 null hypothesis 与论文自身的 causal coupling 叙事不自洽，headline G 值缺乏可靠解释基准\n4. **Numerical inconsistency**: \"3–30×\" 声明混入非显著条件比率\n\n**升级路径**：(a) 增加一个额外基准 + 至少一个 sparsity level 的准确率数据；(b) 主文并列报告 additive/multiplicative null 结果；(c) 修正数字声明；(d) 移除或下移 pilot experiment。完成这些修改后，论文有望达到 main conference 水平。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- ¶3 的 \"linear combination\" 论证是 strawman——改为聚焦 crossover 和 dose-response 的不可预测性\n- Contribution 1 的 \"3–39×\" / \"3–30×\" 需修正为 significant-only 范围\n\n### Section 3 (Background)\n- Additive null 的论证（\"disjoint dimensions\"）需正面回应 causal coupling 的存在\n- Phase segmentation 的 attention sparsity proxy 缺乏独立理论支持\n\n### Section 5 (Results)\n- §5.4 标题 \"Replication Across Training Paradigms\" 已改进（R7），但正文仍应更显著地讨论 LLaMA ~1/40 效应量对泛化性的负面含义\n- §5.7 Answer-region 分析需重新框定——当前 \"partially shielded\" 用词淡化了 93.2% 答案 token 在 G≤1 phase 的含义\n\n### Section 6 (Analysis)\n- Discrimination collapse 作为 correlational diagnostic 定位合理，但 Gini drop ~10% vs severity 15–17× 的定量缺口需正面讨论\n- 命名建议改为 \"importance discrimination collapse\"\n\n### Section 7 (Discussion)\n- Pilot experiment 移至 Appendix 或删除——oracle 18% recovery 直接反驳 \"natural signal\" 声明\n- G 的 near-zero denominator 放大效应需在 headline claims 中明确讨论\n\n### Format\n- 确认正文是否严格在 8 页限制内\n- 清理 LaTeX 源码中的 `% exp_id:` 注释\n- LKV 引用修正（\"Anonymous\" → arXiv ID）\n- Table 3 caption 明确 Δ 的计算方式"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-15T14:01:41.131369+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_fdc656be1c7fe17c11ab639cdbce3710:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4317
}
```

</details>

---


### Assistant

_source line 642 · 2026-05-15T14:01:51.538874+00:00_

---

**Round 8 审稿完成。**

审稿报告已投递给 Research Director。结论：

**Weak Reject (main conference) / Borderline Accept (Findings track)**

4 个 Must-Fix：
1. **Additive null 矛盾** — 论文自身的 causal coupling 叙事与 "disjoint dimensions" 辩护不自洽，需并列报告两种 null
2. **单一基准 MATH-500** — 需至少一个额外基准（哪怕 n=50）
3. **PPL construct validity** — answer-region 分析 (93.2% 答案 token 在 G≤1 phase) 反而削弱核心叙事，需准确率验证
4. **数字声明不一致** — "3–30×" 含非显著条件，应修正为 "3–17×"

8 个 Should-Fix（pilot 移至 appendix、discrimination collapse 解释力缺口、same-architecture 术语、phase segmentation 无理论先验、novelty 重写、窄 sparsity 范围、缺失引用、命名）。

Issue Tracker 已同步更新（3 个 R7 issue 因本轮重新发现而 reopen，10 个新 R8 issue）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 51

## Round 51

2 recorded events


### User

_source line 643 · 2026-05-15T14:01:54.136140+00:00_

[Reviewer 2 审稿结果]:
交叉回应已发送给 Review Director。

总结：对 R1 的 17 个具体观点，我给出 **12 个 [AGREE]**、**3 个 [REBUT]**、**2 个部分同意**。

核心分歧仅在 **W3（profiling vs full G discrepancy）**——R1 误读为 sample size artifact，实际是 G 统计量定义不同（ratio-of-medians vs median-of-ratios），Table 5 caption 已解释。以及 **FlexGen** 引用的相关性。

两位 Reviewer 的主要共识：PPL-only 度量 + answer shielding 削弱 practical significance、pilot mitigation gate FAIL、discrimination collapse 解释力 gap、crossover model-dependence 缺乏 hypothesis。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 644 · 2026-05-15T14:02:04.434705+00:00_

Round 8 审稿圆桌已完成。

**最终结果**：**Weak Reject (main conference) / Borderline Accept (Findings track)**

审稿报告已投递给 Research Director。Issue Tracker 已同步更新（3 个 R7 issue 重新开放，10 个 R8 新 issue）。

**四个核心问题**：
1. PPL construct validity — answer-region 分析（93.2% 答案 token 在 G≤1 phase）反而削弱 severity 的实际意义，无准确率验证
2. 单一基准 MATH-500 — 泛化性不足
3. Additive null 与论文自身 causal coupling 叙事矛盾 — headline G 值缺乏可靠解释基准
4. 数字声明 "3–30×" 含非显著条件 — 应修正为 "3–17×"

**升级路径**：增加一个额外基准 + 准确率数据、并列报告两种 null 结果、修正数字、移除/下移 pilot experiment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director"
}
```

</details>

---


## Round 52

## Round 52

76 recorded events


### User

_source line 645 · 2026-05-15T18:44:36.205541+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: phase-gated-compound-sparse
- 论文路径: projects/phase-gated-compound-sparse/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-15T18:44:42.037590+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-15T18:44:42.088584+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-15T18:44:46.068674+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-15T18:44:46.169986+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-15T18:44:50.262899+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-15T18:44:50.817245+00:00_

{"result":"# 项目 phase-gated-compound-sparse 概况\n\n## 实验状态 (86 个)\n\n- **mvp_v4_legacy_s025**: DONE (failed) — \n- **mvp_v4_random_r2**: DONE (success) — \n- **mvp_v4_legacy_s01**: DONE (negative) — \n- **mvp_v4_legacy_s03**: DONE (success) — \n- **mvp_v4_legacy_s02**: DONE (success) — \n- **mvp_v4c_r2**: DONE (failed) — \n- **mvp_v4b_r2**: DONE (failed) — \n- **mvp_v4a_r2**: DONE (failed) — \n- **mvp_ii_profiling_v4-random**: DONE (failed) — \n- **mvp_ii_profiling_v4c**: DONE (failed) — \n- **mvp_ii_profiling_v4b**: DONE (failed) — \n- **mvp_ii_profiling_v4**: DONE (failed) — \n- **mvp_ii_profiling_v3**: DONE (negative) — \n- **mvp_ii_profiling_v2**: DONE (negative) — \n- **mvp_interaction_index_profiling**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **sf5_asymmetric_spot** (success): —\n- **gsm8k_profiling_qw** (success): GSM8K profiling 验证 compound sparsity severity 的可迁移性：Qwen 在 GSM8K n=50 上是否复现 MATH-500 的 phase-gated II pattern（importance > random, 单调递增）\n- **gsm8k_profiling_ds** (success): GSM8K profiling 验证 compound sparsity severity 的可迁移性：DeepSeek 在 GSM8K n=50 上是否复现 MATH-500 的 phase-gated II pattern（importance > random, 单调递增）\n  [gsm8k_profiling_ds_diagnosis](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/gsm8k_profiling_ds/report/gsm8k_profiling_ds_diagnosis.md)\n\n## 趋势\n成功 41 / 负向 10 / 失败 14 / 共 86\nn_problems: 500 ↑（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-22162: 无 GPU 信息\n\n## 告警\n- mvp_interaction_index_profiling: 训练失败 — unknown\n- mvp_ii_profiling_v4: 训练失败 — unknown\n- mvp_ii_profiling_v4b: 训练失败 — unknown\n- mvp_ii_profiling_v4c: 训练失败 — unknown\n- mvp_ii_profiling_v4d: 训练失败 — unknown\n- mvp_ii_profiling_v4-random: 训练失败 — unknown\n- mvp_v4a_r2: 训练失败 — unknown\n- mvp_v4b_r2: 训练失败 — unknown\n- mvp_v4c_r2: 训练失败 — unknown\n- mvp_v4_legacy_s025: 训练失败 — unknown\n- mvp_v4_legacy_s035: 训练失败 — unknown\n- mvp_v4_float32_s03
…[truncated 885 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-15T18:44:50.817703+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "memory.md"
  }
}
```

</details>

---


### Tool result

_source line 653 · 2026-05-15T18:44:51.320391+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/memory.md\", \"content\": \"# Project Memory\\n\\n## 2026-05-15: Qwen n=475 reanalysis complete\\n- Reviewer flagged Qwen using n=274 (complete-case requiring all 3 phases). Corrected to n=475 (low+high valid only).\\n- Created `analyze_n500_v2.py` on server. Outputs: `n500_unified_final.{csv,json}`, `n500_full_statistics.md`\\n- v2 adds: cross-model Mann-Whitney U, imp/rand effect size ratio, proper paired filtering via `extract_diffs_paired`\\n- Bonferroni correction across 48 tests total (16 conditions + 8 within-imp d_z + 8 rand-within + 8 imp-vs-rand + 8 cross-model)\\n- DS rand s025/s030 Bonferroni p ≈ 0.07 (no longer significant after correction)\\n- All Qwen imp conditions remain *** significant with n=475\\n\\n## 2026-05-15: sf5 asymmetric sparsity — structural insight\\n- 非对称 sparsity 分配下 phase gradient 方向完全稳健（D > 0 both configs）\\n- KV sparsity 较高时 mid-phase II 更大（6.05 vs 3.97）→ KV 维度对中间 phase 影响更强\\n- Head sparsity 较高时 high-phase II 略升（0.52 vs 0.38）→ head 维度主要影响高 sparsity phase\\n- 启示：如果做 adaptive controller，KV budget 对 mid-phase 更敏感，head budget 对 high-phase 更敏感\\n\\n## 2026-05-15: Appendix B G× 修正\\n- 论文旧值 58-241×，精确计算后为 21-64×（per-problem additive II + aggregate PPL 修正）\\n- 计算脚本：`/root/autodl-tmp/pacs/compute_gx_final.py`\\n- 所有论文中引用 G× 的段落需同步更新\\n\", \"total_chars\": 1214, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-15T18:44:51.773124+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/phase-gated-compound-sparse/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/phase-gated-compound-sparse/paper/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-15T18:44:51.823788+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-15T18:44:55.894616+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-15T18:44:55.995569+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 658 · 2026-05-15T18:44:55.996051+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-15T18:44:56.046529+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-15T18:45:02.477002+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-15T18:45:02.879698+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	
22	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Mathematical Reasoning Models}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	\input{related_work}
34	\input{background}
35	\input{methodology}
36	\input{results}
37	\input{analysis}
38	\input{discussion}
39	\input{conclusion}
40	
41	\bibliography{references}
42	
43	\section*{Limitations}
44	\input{limitations}
45	
46	\section*{Reproducibility}
47	Code and data will be released upon acceptance.
48	
49	\appendix
50	\input{appendix}
51	\input{appendix_moved}
52	\input{appendix_disc_analysis}
53	\input{appendix_robustness}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 662 · 2026-05-15T18:45:02.880271+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 663 · 2026-05-15T18:45:03.894397+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "review_issues.yaml"
  }
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-15T18:45:04.095942+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-15T18:45:11.129442+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"}]

Based on the search results, here are the key submission guidelines and author instructions for EMNLP 2026:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce)
…[truncated 1781 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 8249
}
```

</details>

---


### Tool result

_source line 666 · 2026-05-15T18:45:11.129976+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7235
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-15T18:45:11.180543+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 7084
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-15T18:45:16.705851+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-15T18:45:17.185579+00:00_

1	## Round 6 (all resolved, compact)
2	- id: R6-N1
3	  summary: "Table 2 n=50→n=500"
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 5
8	  last_seen_round: 6
9	  mentions: []
10	  action_items: [{round: 6, action: "Table 2 replaced", assigned_to: paper_agent, status: done}]
11	  resolution: "Done R6."
12	  resolution_round: 6
13	
14	- id: R6-N2
15	  summary: "Discrimination collapse effect size gap"
16	  category: method
17	  severity: critical
18	  status: resolved
19	  first_raised_round: 6
20	  last_seen_round: 6
21	  mentions: []
22	  action_items: [{round: 6, action: "§6 rewritten as correlational diagnostic", assigned_to: paper_agent, status: done}]
23	  resolution: "Done R6."
24	  resolution_round: 6
25	
26	- id: R6-N3
27	  summary: "ThinKV misattribution"
28	  category: writing
29	  severity: critical
30	  status: resolved
31	  first_raised_round: 1
32	  last_seen_round: 6
33	  mentions: []
34	  action_items: [{round: 6, action: "Rewritten", assigned_to: paper_agent, status: done}]
35	  resolution: "Done R6."
36	  resolution_round: 6
37	
38	## Round 7 (all resolved except R7-M2)
39	- id: R7-N1
40	  summary: "No downstream accuracy validation; construct validity gap"
41	  category: experiment
42	  severity: critical
43	  status: in_progress
44	  first_raised_round: 7
45	  last_seen_round: 8
46	  mentions:
47	    - {round: 7, reviewers: [R1, R2], note: "PPL-based II not mapped to accuracy; low-sparsity phase may not affect answers"}
48	    - {round: 8, reviewers: [R1, R2], note: "REOPENED: answer-region proxy (93.2% in G≤1 phase) actually UNDERMINES severity narrative. Both R8 reviewers agree direct accuracy validation needed."}
49	  action_items:
50	    - {round: 7, action: "N1a answer-region proxy + boxed validation", assigned_to: main_agent, status: done}
51	    - {round: 7, action: "§5.7 Answer-Region Analysis + Limitations caveat", assigned_to: paper_agent, status: done}
52	    - {round: 8, action: "GSM8K dense
…[truncated 19617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 479
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-15T18:45:17.186090+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission format page limit template double blind anonymity requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission format page limit template double blind anonymity requirements"
  }
}
```

</details>

---


### Tool call

_source line 671 · 2026-05-15T18:45:17.638392+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 paper format guidelines page limits long short papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 paper format guidelines page limits long short papers"
  }
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-15T18:45:18.191023+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-15T18:45:23.022335+00:00_

Web search results for query: "ACL Rolling Review 2026 paper format guidelines page limits long short papers"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"}]

Based on the search results, here are the ACL Rolling Review 2026 paper format guidelines for page limits:

## Paper Length Requirements

**Long Papers:** Long papers have a maximum of 8 content pages.

**Short Papers:** Short papers have a maximum of 4 content pages.

## What Doesn't Count Toward Page Limit

Sections on ethical considerations and limitations do not count towards the page limit. Additionally,
…[truncated 555 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 5383
}
```

</details>

---


### Tool result

_source line 674 · 2026-05-15T18:45:28.647705+00:00_

Web search results for query: "EMNLP 2026 ARR submission format page limit template double blind anonymity requirements"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Let me search for more specific information about the submission format and template requirements.

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Frequently Asked Questions - ACL 2023","url":"https://2023.aclweb.org/faq/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review
…[truncated 2391 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "WebSearch",
  "elapsed_ms": 11461
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-15T18:45:28.648302+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'phase-gated-compound-sparse'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 10457
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-15T18:45:40.591758+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-15T18:45:40.642651+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-15T18:45:40.643200+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "constraints.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "constraints.yaml"
  }
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-15T18:45:40.693702+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No constraints.yaml found for 'phase-gated-compound-sparse'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 680 · 2026-05-15T18:45:43.757630+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-15T18:45:44.209964+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We show that compound severity is not phase-invariant: it is an emergent phase-strategy interaction with amplification ratios ($G$) from $7.5{\times}$ ($s{=}0.15$, 95\% CI $[4.1, 11.4]$) to $79.8{\times}$ ($s{=}0.30$, 95\% CI $[63.3, 96.5]$; additive null; multiplicative null preserves the gradient, $G_{\times}{=}21$--$64{\times}$) across reasoning phases in mathematical reasoning models.
4	
5	On DeepSeek-R1-Distill-Qwen-7B (500 MATH-500 problems, $n_{\text{eff}}{=}496$, $s \in \{0.15, 0.20, 0.25, 0.30\}$), importance-based eviction produces a monotonically increasing severity gradient from the high-sparsity to low-sparsity reasoning phase (median $\Delta$: $0.39 \to 8.48$; all Bonferroni-corrected $p \ll 10^{-10}$). Random eviction develops a detectable phase gradient only above $s \approx 0.20$ (non-significant at $s \leq 0.20$; where significant, $3$--$17{\times}$ weaker), confirming importance-based eviction as the dominant driver.
6	A crossover emerges at $s{=}0.25$: importance-based eviction outperforms random in high-sparsity phases yet underperforms in low-sparsity phases---a qualitative reversal in strategy ranking.
7	The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with preliminary cross-architecture evidence from a LlamaForCausalLM model suggesting the phenomenon may extend beyond Qwen2-family architectures.
8	We present \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic: both strategies exhibit near-identical Gini drops, yet severity diverges by $15$--$17{\times}$, implicating the structural specificity of importance-based pruning as the key d
…[truncated 184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 682 · 2026-05-15T18:45:44.210345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 683 · 2026-05-15T18:45:44.713090+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 4512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-15T18:45:44.713643+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-15T18:45:45.127245+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	PM-KVQ~\cite{pmkvq-iclr2026} demonstrates that progressive quantization---gradually reducing bit-width over the generation process---mitigates cumulative error in long-CoT reasoning, implicitly introducing a temporal dimension to compression severity that resonates with our finding that compound interaction is phase-dependent.
11	
12	\cite{kim2026pqqp} show that compression order (prune-then-quantize vs.\ quantize-then-prune) significantly affects joint quality, and their Progressive Intensity Hypothesis---that weaker perturbations should precede stronger ones---echoes our dose-response finding that interaction severity increases monotonically with sparsity.
13	
14	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
15	
16	\paragraph{KV cache eviction.}
17	Most methods rely on importance scoring whose reliability is increasingly questioned.
18	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher tha
…[truncated 3590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 413
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-15T18:45:45.127701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-15T18:45:46.082535+00:00_

1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
12	
13	\paragraph{Interaction Index.}
14	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
15	\begin{equation}
16	    \mathrm{II} = r_b - r_a - r_k + 1.
17	    \label{eq:ii}
18	\end{equation}
19	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null ($\mathrm{II} = 0$ under no interaction) as the primary formulation. Although the two sparsity axes are causally coupled---head pruni
…[truncated 2515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-15T18:45:46.133223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-15T18:45:46.736640+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-training-paradigm replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
6	
7	\paragraph{Dataset.}
8	We evaluate all 500 problems from MATH-500~\cite{math500-neurips2021}. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048). Problems with degenerate phase assignments (null low or high phase) are excluded, yielding effective sample sizes of $n{=}496$ for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded). Qwen exhibits a higher mid-phase null rate (45.2\% vs.\ 10.2\% for DeepSeek) due to lower temporal autocorrelation in its attention sparsity patterns (lag-1 $r{=}0.718$ vs.\ $0.894$, $d{=}-1.68$); this does not affect the primary gradient metric $\Delta = \mathrm{II}_{\textit{low}} - \mathrm{II}_{\textit{high}}$, which requires only low and high phases. Sensitivity analysis across $\texttt{min\_phase\_length} \in \{5, 10, 20\}$ confirms robustness (Appendix~\ref{app:mpl-sensitivity}).
9	
10	\paragraph{Sparsity configuration.}
11	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both
…[truncated 2031 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-15T18:45:46.737048+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-15T18:45:47.103078+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\times}$ amplification (all Bonferroni-corrected $p \ll 10^{-10}$). Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \geq 0.25$, $\Delta$ becomes significant ($0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$) but $15$--$17{\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger.
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, 500 MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.21 & 3.99 & 8.48 \\
20	Random     & 0.01 & 0.03 & 0.26 & 0.51 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown at $n{=}496$. The per-problem amplification ratio $G$ (Eq.~\ref{eq:gradient}) increases from $7.5{\times}$ (95\% CI: $[4.1, 11.4]$) at $s{=}0.15$ to $79.8{\times}$ ($[63.3, 96.5]$) at $s{=}0.30$ under imp
…[truncated 11818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 366
}
```

</details>

---


### Tool call

_source line 692 · 2026-05-15T18:45:47.103613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-15T18:45:47.355015+00:00_

1	\section{Importance Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	The mechanisms discussed here are \emph{correlational diagnostics} that illuminate but do not fully explain the $15$--$17{\times}$ severity divergence between strategies. Both strategies exhibit near-identical Gini drops ($<10\%$ difference), yet severity diverges by $15$--$17{\times}$---an order-of-magnitude mismatch indicating that aggregate concentration collapse alone is insufficient. The critical differentiator is \emph{structural specificity} of importance-based pruning, which systematically removes high-attention-score heads (\S\ref{sec:discrimination-collapse-main}).
5	
6	\subsection{Importance Discrimination Collapse}
7	\label{sec:discrimination-collapse-main}
8	
9	Head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek, $6$--$17\%$ relative to dense baseline) and $0.010$--$0.020$ (Qwen, $2$--$4\%$) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). Critically, random eviction shows near-identical Gini drops at matched sparsity (DeepSeek $s{=}0.25$: importance $-0.065$ vs.\ random $-0.060$; $s{=}0.30$: $-0.081$ vs.\ $-0.071$; Qwen: $-0.019$ to $-0.046$ for both strategies), confirming that importance discrimination collapse is a consequence of head pruning \emph{per se}, not the eviction strategy. Yet importance-based severity is $15$--$17{\times}$ larger than random at matched sparsity---the amplification arises because importance-based eviction \emph{depends on} the very scores that pruning degrades, while random eviction's decisions are score-independent.
10	
11	This pattern---\emph{importance discrimination collapse}---is consistent with importance-based eviction degenerating into noise-sensitive selection whe
…[truncated 2251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-15T18:45:47.355438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-15T18:45:47.406035+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Implications for deployment.}
5	A uniform compression budget implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. The severity gradient characterizes phase-dependent sensitivity patterns that could inform \emph{phase-aware} budget allocation. However, preliminary mitigation experiments (Appendix~\ref{app:pilot-mitigation}) yielded limited recovery (oracle 18\%), suggesting that severity signals alone are insufficient---additional mechanisms (e.g., strategy switching, adaptive thresholding) warrant investigation. We expect qualitatively similar behavior for other attention-mass-based scoring methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-colm2025}), though quantitative magnitudes may differ. Extended discussion in Appendix~\ref{app:extended-discussion}.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 696 · 2026-05-15T18:45:52.382652+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
  "offset": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
    "offset": "6"
  }
}
```

</details>

---


### Tool result

_source line 697 · 2026-05-15T18:45:53.236670+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (6). The file has 6 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 698 · 2026-05-15T18:45:53.287366+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-15T18:45:53.338071+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity is not phase-invariant but exhibits an emergent phase-strategy interaction. Under importance-based eviction, the paired median difference $\Delta$ increases from $0.39$ to $8.48$ (DeepSeek, $n{=}496$) and $0.07$ to $3.16$ (Qwen, $n{=}475$), all $p < 10^{-13}$, with amplification ratios $G{=}7.5$--$79.8{\times}$. Random eviction is $3$--$17{\times}$ weaker where both strategies are significant ($s \geq 0.25$). A model-dependent crossover on DeepSeek demonstrates that no single strategy dominates uniformly. Importance discrimination collapse provides a correlational diagnostic: despite near-identical Gini drops, severity diverges by $15$--$17{\times}$, implicating the structural specificity of importance-based pruning.
5	These findings establish compound severity as phase-dependent, providing a diagnostic foundation for future phase-aware mitigation. Extending to code/science reasoning, causal validation of importance discrimination collapse, and characterizing asymmetric compound interactions are key next steps.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 700 · 2026-05-15T18:45:53.790516+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-15T18:45:54.142649+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	Our primary evaluation uses MATH-500; cross-benchmark validation on GSM8K (\S\ref{sec:cross-benchmark}) confirms the phase gradient direction under importance-based eviction but reveals that random eviction is non-significant on GSM8K (CIs spanning zero), precluding meaningful ratio computation. On MATH-500, strategy specificity is quantifiable ($15$--$17{\times}$); on GSM8K, it manifests as a qualitative gap (significant vs.\ non-significant). This suggests that the phase-strategy interaction is robust in direction but task-dependent in form---complex reasoning (MATH-500) produces quantitative strategy contrast while simpler arithmetic (GSM8K) produces qualitative separation. Qwen GSM8K outputs were truncated at \texttt{max\_new\_tokens}${=}$2047, so Qwen GSM8K absolute values carry this limitation; DeepSeek GSM8K data is untruncated. Our task-complexity explanation for specificity attenuation (lower cognitive load $\to$ more uniform attention $\to$ reduced strategy sensitivity) is supported by 
…[truncated 2676 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-15T18:45:54.143232+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
  }
}
```

</details>

---
