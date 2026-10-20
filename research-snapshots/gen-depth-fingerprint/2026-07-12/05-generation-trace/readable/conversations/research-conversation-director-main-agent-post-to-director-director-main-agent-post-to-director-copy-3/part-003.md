# Research conversation: [系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director  — Part 3 of 7

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../research-conversation-director-main-agent-post-to-director-director-main-agent-post-to-director-copy-3.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/c2/c2caaf5c89d223f9803c.json)

## Round 11

### Tool result

_source line 397 · 2026-05-15T05:02:50.663Z_

<details><summary>↩ Tool result · `toolu_013g4FDnd6jw6iRG4xtcZwHu`</summary>

```text
{"result":"{\"success\": false, \"passed\": false, \"compiled\": {\"success\": false, \"pdf_path\": null, \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"Package natbib Warning: Citation `curious_decline' on page 4 undefined on input\\n line 37.\\n\\n\\nPackage natbib Warning: Citation `curious_decline' on page 4 undefined on input\\n line 43.\\n\\n\\nPackage natbib Warning: Citation `writing_diversity' on page 4 undefined on inp\\nut line 43.\\n\\n\\nPackage natbib Warning: Citation `xgboost' on page 4 undefined on input line 52\\n.\\n\\n\\nPackage natbib Warning: Citation `gltr' on page 4 undefined on input line 58.\\n\\n\\nPackage natbib Warning: Citation `fast_detectgpt' on page 4 undefined on input \\nline 58.\\n\\n\\nPackage natbib Warning: Citation `ld_score' on page 4 undefined on input line 5\\n8.\\n\\n\\nPackage natbib Warning: Citation `binoculars' on page 4 undefined on input line\\n 58.\\n\\n) (./results.tex [4]\\n\\nLaTeX Warning: Reference `sec:eval' on page 5 undefined on input line 7.\\n\\n\\nLaTeX Warning: Reference `tab:logo' on page 5 undefined on input line 7.\\n\\n\\nLaTeX Warning: Reference `sec:discussion' on page 5 undefined on input line 35.\\n\\n\\n\\nPackage natbib Warning: Citation `detectgpt' on page 5 undefined on input line \\n37.\\n\\n\\nPackage natbib Warning: Citation `binoculars' on page 5 undefined on input line\\n 37.\\n\\n\\nLaTeX Warning: Reference `fig:logo_performance' on page 5 undefined on input li\\nne 39.\\n\\n\\nLaTeX Warning: File `figures/paper/fig2_logo_performance.pdf' not found on inpu\\nt line 43.\\n\\n\\n! Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not \\nfound: using draft setting.\\n\\nSee the pdftex.def package documentation for explanation.\\nType  H &lt;return>  for immediate help.\\n ...                                              \\n                                                  \\nl.43 ...]{figures/paper/fig2_logo_performance.pdf}\\n                                                  \\nTry typing  &lt;return>  to proceed.\\nIf that doesn't work, type  X &lt;return>  to quit.\\n\\n \\nHere is how much of TeX's memory you used:\\n 15785 strings out of 469438\\n 248190 string characters out of 5468411\\n 718985 words of memory out of 5000000\\n 43925 multiletter control sequences out of 15000+600000\\n 680903 words of font info for 285 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,10n,93p,1001b,476s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n!  ==> Fatal error occurred, no output PDF file produced!\", \"error\": \"Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not\", \"pages\": null, \"warnings\": [\"Line number reference failed, re-run to get it right.\", \"Citation `mapping_llm_science' on page 1 undefined on i\", \"Citation `monitoring_ai_review' on page 1 undefined on\", \"Citation `fast_detectgpt' on page 1 undefined on input\", \"Citation `binoculars' on page 1 undefined on input line\", \"Citation `ld_score' on page 1 undefined on input line 8\", \"Citation `detectgpt' on page 1 undefined on input line\", \"Reference `sec:baselines' on page 1 undefined on input line 16.\", \"Citation `broken_telephone' on page 1 undefined on inpu\", \"Citation `markovian_chains' on page 1 undefined on inpu\", \"Citation `ood_baseline' on page 1 undefined on input li\", \"Reference `sec:related' on page 2 undefined on input line 39.\", \"Reference `sec:method' on page 2 undefined on input line 40.\", \"Reference `sec:results' on page 2 undefined on input line 41.\", \"Reference `sec:discussion' on page 2 undefined on input line 42.\", \"Citation `gltr' on page 2 undefined on input line 7.\", \"Citation `grover' on page 2 undefined on input line 7.\", \"Citation `release_strategies' on page 2 undefined on in\", \"Citation `detectgpt' on page 2 undefined on input line\", \"Citation `fast_detectgpt' on page 2 undefined on input\", \"Citation `binoculars' on page 2 undefined on input line\", \"Citation `dna_gpt' on page 2 undefined on input line 7.\", \"Citation `feat_aug_transformer' on page 2 undefined on\", \"Citation `reliable_detection' on page 2 undefined on in\", \"Citation `ld_score' on page 2 undefined on input line 7\", \"Citation `intrinsic_dimension' on page 2 undefined on i\", \"Citation `diveye' on page 2 undefined on input line 8.\", \"Citation `generator_barrier' on page 2 undefined on inp\", \"Citation `jawahar_survey' on page 2 undefined on input\", \"Reference `sec:baselines' on page 2 undefined on input line 11.\", \"Citation `paraphrase_evades' on page 2 undefined on inp\", \"Citation `detection_possibilities' on page 2 undefined\", \"Citation `ood_baseline' on page 2 undefined on input li\", \"Citation `self_consuming_mad' on page 2 undefined on in\", \"Citation `curse_of_recursion' on page 2 undefined on in\", \"Citation `model_collapse_avoidable' on page 2 undefined\", \"Citation `strong_model_collapse' on page 2 undefined on\", \"Citation `broken_telephone' on page 2 undefined on inpu\", \"Citation `markovian_chains' on page 2 undefined on inpu\", \"Citation `curious_decline' on page 3 undefined on input\", \"Citation `writing_diversity' on page 3 undefined on inp\", \"Citation `stamatatos_survey' on page 3 undefined on inp\", \"Citation `koppel_authorship' on page 3 undefined on inp\", \"Citation `uchendu_attribution' on page 3 undefined on i\", \"Citation `nucleus_sampling' on page 3 undefined on inpu\", \"Citation `dsir' on page 3 undefined on input line 44.\", \"Citation `qurating' on page 3 undefined on input line 4\", \"Citation `ccnet' on page 3 undefined on input line 44.\", \"Citation `watermark_llm' on page 3 undefined on input l\", \"Citation `synthid_text' on page 3 undefined on input li\", \"Citation `aaronson_watermark' on page 3 undefined on in\", \"Citation `chainwash' on page 3 undefined on input line\", \"Citation `min_k_percent' on page 3 undefined on input l\", \"Citation `detectgpt' on page 3 undefined on input line\", \"Citation `fast_detectgpt' on page 3 undefined on input\", \"Citation `binoculars' on page 3 undefined on input line\", \"Citation `uchendu_attribution' on page 3 undefined on i\", \"Citation `curse_of_recursion' on page 3 undefined on in\", \"Citation `self_consuming_mad' on page 3 undefined on in\", \"Citation `pythia' on page 3 undefined on input line 14.\", \"Citation `olmo' on page 3 undefined on input line 14.\", \"Citation `qwen3' on page 3 undefined on input line 14.\", \"Citation `nucleus_sampling' on page 3 undefined on inpu\", \"Citation `markovian_chains' on page 3 undefined on inpu\", \"Citation `detectgpt' on page 4 undefined on input line\", \"Citation `ood_baseline' on page 4 undefined on input li\", \"Citation `curious_decline' on page 4 undefined on input\", \"Citation `curious_decline' on page 4 undefined on input\", \"Citation `writing_diversity' on page 4 undefined on inp\", \"Citation `xgboost' on page 4 undefined on input line 52\", \"Citation `gltr' on page 4 undefined on input line 58.\", \"Citation `fast_detectgpt' on page 4 undefined on input\", \"Citation `ld_score' on page 4 undefined on input line 5\", \"Citation `binoculars' on page 4 undefined on input line\", \"Reference `sec:eval' on page 5 undefined on input line 7.\", \"Reference `tab:logo' on page 5 undefined on input line 7.\", \"Reference `sec:discussion' on page 5 undefined on input line 35.\", \"Citation `detectgpt' on page 5 undefined on input line\", \"Citation `binoculars' on page 5 undefined on input line\", \"Reference `fig:logo_performance' on page 5 undefined on input li\", \"File `figures/paper/fig2_logo_performance.pdf' not found on inpu\"]}, \"pages\": null, \"page_status\": \"unknown\", \"max_pages\": 8, \"min_pages\": 6, \"critical_warnings\": [\"Citation `mapping_llm_science' on page 1 undefined on i\", \"Citation `monitoring_ai_review' on page 1 undefined on\", \"Citation `fast_detectgpt' on page 1 undefined on input\", \"Citation `binoculars' on page 1 undefined on input line\", \"Citation `ld_score' on page 1 undefined on input line 8\", \"Citation `detectgpt' on page 1 undefined on input line\", \"Reference `sec:baselines' on page 1 undefined on input line 16.\", \"Citation `broken_telephone' on page 1 undefined on inpu\", \"Citation `markovian_chains' on page 1 undefined on inpu\", \"Citation `ood_baseline' on page 1 undefined on input li\", \"Reference `sec:related' on page 2 undefined on input line 39.\", \"Reference `sec:method' on page 2 undefined on input line 40.\", \"Reference `sec:results' on page 2 undefined on input line 41.\", \"Reference `sec:discussion' on page 2 undefined on input line 42.\", \"Citation `gltr' on page 2 undefined on input line 7.\", \"Citation `grover' on page 2 undefined on input line 7.\", \"Citation `release_strategies' on page 2 undefined on in\", \"Citation `detectgpt' on page 2 undefined on input line\", \"Citation `fast_detectgpt' on page 2 undefined on input\", \"Citation `binoculars' on page 2 undefined on input line\", \"Citation `dna_gpt' on page 2 undefined on input line 7.\", \"Citation `feat_aug_transformer' on page 2 undefined on\", \"Citation `reliable_detection' on page 2 undefined on in\", \"Citation `ld_score' on page 2 undefined on input line 7\", \"Citation `intrinsic_dimension' on page 2 undefined on i\", \"Citation `diveye' on page 2 undefined on input line 8.\", \"Citation `generator_barrier' on page 2 undefined on inp\", \"Citation `jawahar_survey' on page 2 undefined on input\", \"Reference `sec:baselines' on page 2 undefined on input line 11.\", \"Citation `paraphrase_evades' on page 2 undefined on inp\", \"Citation `detection_possibilities' on page 2 undefined\", \"Citation `ood_baseline' on page 2 undefined on input li\", \"Citation `self_consuming_mad' on page 2 undefined on in\", \"Citation `curse_of_recursion' on page 2 undefined on in\", \"Citation `model_collapse_avoidable' on page 2 undefined\", \"Citation `strong_model_collapse' on page 2 undefined on\", \"Citation `broken_telephone' on page 2 undefined on inpu\", \"Citation `markovian_chains' on page 2 undefined on inpu\", \"Citation `curious_decline' on page 3 undefined on input\", \"Citation `writing_diversity' on page 3 undefined on inp\", \"Citation `stamatatos_survey' on page 3 undefined on inp\", \"Citation `koppel_authorship' on page 3 undefined on inp\", \"Citation `uchendu_attribution' on page 3 undefined on i\", \"Citation `nucleus_sampling' on page 3 undefined on inpu\", \"Citation `dsir' on page 3 undefined on input line 44.\", \"Citation `qurating' on page 3 undefined on input line 4\", \"Citation `ccnet' on page 3 undefined on input line 44.\", \"Citation `watermark_llm' on page 3 undefined on input l\", \"Citation `synthid_text' on page 3 undefined on input li\", \"Citation `aaronson_watermark' on page 3 undefined on in\", \"Citation `chainwash' on page 3 undefined on input line\", \"Citation `min_k_percent' on page 3 undefined on input l\", \"Citation `detectgpt' on page 3 undefined on input line\", \"Citation `fast_detectgpt' on page 3 undefined on input\", \"Citation `binoculars' on page 3 undefined on input line\", \"Citation `uchendu_attribution' on page 3 undefined on i\", \"Citation `curse_of_recursion' on page 3 undefined on in\", \"Citation `self_consuming_mad' on page 3 undefined on in\", \"Citation `pythia' on page 3 undefined on input line 14.\", \"Citation `olmo' on page 3 undefined on input line 14.\", \"Citation `qwen3' on page 3 undefined on input line 14.\", \"Citation `nucleus_sampling' on page 3 undefined on inpu\", \"Citation `markovian_chains' on page 3 undefined on inpu\", \"Citation `detectgpt' on page 4 undefined on input line\", \"Citation `ood_baseline' on page 4 undefined on input li\", \"Citation `curious_decline' on page 4 undefined on input\", \"Citation `curious_decline' on page 4 undefined on input\", \"Citation `writing_diversity' on page 4 undefined on inp\", \"Citation `xgboost' on page 4 undefined on input line 52\", \"Citation `gltr' on page 4 undefined on input line 58.\", \"Citation `fast_detectgpt' on page 4 undefined on input\", \"Citation `ld_score' on page 4 undefined on input line 5\", \"Citation `binoculars' on page 4 undefined on input line\", \"Reference `sec:eval' on page 5 undefined on input line 7.\", \"Reference `tab:logo' on page 5 undefined on input line 7.\", \"Reference `sec:discussion' on page 5 undefined on input line 35.\", \"Citation `detectgpt' on page 5 undefined on input line\", \"Citation `binoculars' on page 5 undefined on input line\", \"Reference `fig:logo_performance' on page 5 undefined on input li\"], \"minor_warnings\": [\"Line number reference failed, re-run to get it right.\", \"File `figures/paper/fig2_logo_performance.pdf' not found on inpu\", \"Underfull \\\\hbox (badness 4391) in paragraph at lines 16--17\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 24--25\"], \"issues\": [\"compile failed: Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not\", \"79 critical warning(s): Citation `mapping_llm_science' on page 1 undefined on i; Citation `monitoring_ai_review' on page 1 undefined on; Citation `fast_detectgpt' on page 1 undefined on input; (+76 more)\", \"page count unavailable (compile likely failed)\"], \"summary\": \"FAIL: compile failed: Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not; 79 critical warning(s): Citation `mapping_llm_science' on page 1 undefined on i; Citation `monitoring_ai_review' on page 1 undefined on; Citation `fast_detectgpt' on page 1 undefined on input; (+76 more); page count unavailable (compile likely failed)\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "325696cb-2e96-4e59-9a1d-4bacf03b7484",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "1ef65ac1-fdf1-47ef-9485-1c1098132eec",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"passed\\\": false, \\\"compiled\\\": {\\\"success\\\": false, \\\"pdf_path\\\": null, \\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper\\\", \\\"main_tex\\\": \\\"main.tex\\\", \\\"log_tail\\\": \\\"Package natbib Warning: Citation `curious_decline' on page 4 undefined on input\\\\n line 37.\\\\n\\\\n\\\\nPackage natbib Warning: Citation `curious_decline' on page 4 undefined on input\\\\n line 43.\\\\n\\\\n\\\\nPackage natbib Warning: Citation `writing_diversity' on page 4 undefined on inp\\\\nut line 43.\\\\n\\\\n\\\\nPackage natbib Warning: Citation `xgboost' on page 4 undefined on input line 52\\\\n.\\\\n\\\\n\\\\nPackage natbib Warning: Citation `gltr' on page 4 undefined on input line 58.\\\\n\\\\n\\\\nPackage natbib Warning: Citation `fast_detectgpt' on page 4 undefined on input \\\\nline 58.\\\\n\\\\n\\\\nPackage natbib Warning: Citation `ld_score' on page 4 undefined on input line 5\\\\n8.\\\\n\\\\n\\\\nPackage natbib Warning: Citation `binoculars' on page 4 undefined on input line\\\\n 58.\\\\n\\\\n) (./results.tex [4]\\\\n\\\\nLaTeX Warning: Reference `sec:eval' on page 5 undefined on input line 7.\\\\n\\\\n\\\\nLaTeX Warning: Reference `tab:logo' on page 5 undefined on input line 7.\\\\n\\\\n\\\\nLaTeX Warning: Reference `sec:discussion' on page 5 undefined on input line 35.\\\\n\\\\n\\\\n\\\\nPackage natbib Warning: Citation `detectgpt' on page 5 undefined on input line \\\\n37.\\\\n\\\\n\\\\nPackage natbib Warning: Citation `binoculars' on page 5 undefined on input line\\\\n 37.\\\\n\\\\n\\\\nLaTeX Warning: Reference `fig:logo_performance' on page 5 undefined on input li\\\\nne 39.\\\\n\\\\n\\\\nLaTeX Warning: File `figures/paper/fig2_logo_performance.pdf' not found on inpu\\\\nt line 43.\\\\n\\\\n\\\\n! Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not \\\\nfound: using draft setting.\\\\n\\\\nSee the pdftex.def package documentation for explanation.\\\\nType  H &lt;return>  for immediate help.\\\\n ...                                              \\\\n                                                  \\\\nl.43 ...]{figures/paper/fig2_logo_performance.pdf}\\\\n                                                  \\\\nTry typing  &lt;return>  to proceed.\\\\nIf that doesn't work, type  X &lt;return>  to quit.\\\\n\\\\n \\\\nHere is how much of TeX's memory you used:\\\\n 15785 strings out of 469438\\\\n 248190 string characters out of 5468411\\\\n 718985 words of memory out of 5000000\\\\n 43925 multiletter control sequences out of 15000+600000\\\\n 680903 words of font info for 285 fonts, out of 8000000 for 9000\\\\n 59 hyphenation exceptions out of 8191\\\\n 84i,10n,93p,1001b,476s stack positions out of 10000i,1000n,20000p,200000b,200000s\\\\n!  ==> Fatal error occurred, no output PDF file produced!\\\", \\\"error\\\": \\\"Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not\\\", \\\"pages\\\": null, \\\"warnings\\\": [\\\"Line number reference failed, re-run to get it right.\\\", \\\"Citation `mapping_llm_science' on page 1 undefined on i\\\", \\\"Citation `monitoring_ai_review' on page 1 undefined on\\\", \\\"Citation `fast_detectgpt' on page 1 undefined on input\\\", \\\"Citation `binoculars' on page 1 undefined on input line\\\", \\\"Citation `ld_score' on page 1 undefined on input line 8\\\", \\\"Citation `detectgpt' on page 1 undefined on input line\\\", \\\"Reference `sec:baselines' on page 1 undefined on input line 16.\\\", \\\"Citation `broken_telephone' on page 1 undefined on inpu\\\", \\\"Citation `markovian_chains' on page 1 undefined on inpu\\\", \\\"Citation `ood_baseline' on page 1 undefined on input li\\\", \\\"Reference `sec:related' on page 2 undefined on input line 39.\\\", \\\"Reference `sec:method' on page 2 undefined on input line 40.\\\", \\\"Reference `sec:results' on page 2 undefined on input line 41.\\\", \\\"Reference `sec:discussion' on page 2 undefined on input line 42.\\\", \\\"Citation `gltr' on page 2 undefined on input line 7.\\\", \\\"Citation `grover' on page 2 undefined on input line 7.\\\", \\\"Citation `release_strategies' on page 2 undefined on in\\\", \\\"Citation `detectgpt' on page 2 undefined on input line\\\", \\\"Citation `fast_detectgpt' on page 2 undefined on input\\\", \\\"Citation `binoculars' on page 2 undefined on input line\\\", \\\"Citation `dna_gpt' on page 2 undefined on input line 7.\\\", \\\"Citation `feat_aug_transformer' on page 2 undefined on\\\", \\\"Citation `reliable_detection' on page 2 undefined on in\\\", \\\"Citation `ld_score' on page 2 undefined on input line 7\\\", \\\"Citation `intrinsic_dimension' on page 2 undefined on i\\\", \\\"Citation `diveye' on page 2 undefined on input line 8.\\\", \\\"Citation `generator_barrier' on page 2 undefined on inp\\\", \\\"Citation `jawahar_survey' on page 2 undefined on input\\\", \\\"Reference `sec:baselines' on page 2 undefined on input line 11.\\\", \\\"Citation `paraphrase_evades' on page 2 undefined on inp\\\", \\\"Citation `detection_possibilities' on page 2 undefined\\\", \\\"Citation `ood_baseline' on page 2 undefined on input li\\\", \\\"Citation `self_consuming_mad' on page 2 undefined on in\\\", \\\"Citation `curse_of_recursion' on page 2 undefined on in\\\", \\\"Citation `model_collapse_avoidable' on page 2 undefined\\\", \\\"Citation `strong_model_collapse' on page 2 undefined on\\\", \\\"Citation `broken_telephone' on page 2 undefined on inpu\\\", \\\"Citation `markovian_chains' on page 2 undefined on inpu\\\", \\\"Citation `curious_decline' on page 3 undefined on input\\\", \\\"Citation `writing_diversity' on page 3 undefined on inp\\\", \\\"Citation `stamatatos_survey' on page 3 undefined on inp\\\", \\\"Citation `koppel_authorship' on page 3 undefined on inp\\\", \\\"Citation `uchendu_attribution' on page 3 undefined on i\\\", \\\"Citation `nucleus_sampling' on page 3 undefined on inpu\\\", \\\"Citation `dsir' on page 3 undefined on input line 44.\\\", \\\"Citation `qurating' on page 3 undefined on input line 4\\\", \\\"Citation `ccnet' on page 3 undefined on input line 44.\\\", \\\"Citation `watermark_llm' on page 3 undefined on input l\\\", \\\"Citation `synthid_text' on page 3 undefined on input li\\\", \\\"Citation `aaronson_watermark' on page 3 undefined on in\\\", \\\"Citation `chainwash' on page 3 undefined on input line\\\", \\\"Citation `min_k_percent' on page 3 undefined on input l\\\", \\\"Citation `detectgpt' on page 3 undefined on input line\\\", \\\"Citation `fast_detectgpt' on page 3 undefined on input\\\", \\\"Citation `binoculars' on page 3 undefined on input line\\\", \\\"Citation `uchendu_attribution' on page 3 undefined on i\\\", \\\"Citation `curse_of_recursion' on page 3 undefined on in\\\", \\\"Citation `self_consuming_mad' on page 3 undefined on in\\\", \\\"Citation `pythia' on page 3 undefined on input line 14.\\\", \\\"Citation `olmo' on page 3 undefined on input line 14.\\\", \\\"Citation `qwen3' on page 3 undefined on input line 14.\\\", \\\"Citation `nucleus_sampling' on page 3 undefined on inpu\\\", \\\"Citation `markovian_chains' on page 3 undefined on inpu\\\", \\\"Citation `detectgpt' on page 4 undefined on input line\\\", \\\"Citation `ood_baseline' on page 4 undefined on input li\\\", \\\"Citation `curious_decline' on page 4 undefined on input\\\", \\\"Citation `curious_decline' on page 4 undefined on input\\\", \\\"Citation `writing_diversity' on page 4 undefined on inp\\\", \\\"Citation `xgboost' on page 4 undefined on input line 52\\\", \\\"Citation `gltr' on page 4 undefined on input line 58.\\\", \\\"Citation `fast_detectgpt' on page 4 undefined on input\\\", \\\"Citation `ld_score' on page 4 undefined on input line 5\\\", \\\"Citation `binoculars' on page 4 undefined on input line\\\", \\\"Reference `sec:eval' on page 5 undefined on input line 7.\\\", \\\"Reference `tab:logo' on page 5 undefined on input line 7.\\\", \\\"Reference `sec:discussion' on page 5 undefined on input line 35.\\\", \\\"Citation `detectgpt' on page 5 undefined on input line\\\", \\\"Citation `binoculars' on page 5 undefined on input line\\\", \\\"Reference `fig:logo_performance' on page 5 undefined on input li\\\", \\\"File `figures/paper/fig2_logo_performance.pdf' not found on inpu\\\"]}, \\\"pages\\\": null, \\\"page_status\\\": \\\"unknown\\\", \\\"max_pages\\\": 8, \\\"min_pages\\\": 6, \\\"critical_warnings\\\": [\\\"Citation `mapping_llm_science' on page 1 undefined on i\\\", \\\"Citation `monitoring_ai_review' on page 1 undefined on\\\", \\\"Citation `fast_detectgpt' on page 1 undefined on input\\\", \\\"Citation `binoculars' on page 1 undefined on input line\\\", \\\"Citation `ld_score' on page 1 undefined on input line 8\\\", \\\"Citation `detectgpt' on page 1 undefined on input line\\\", \\\"Reference `sec:baselines' on page 1 undefined on input line 16.\\\", \\\"Citation `broken_telephone' on page 1 undefined on inpu\\\", \\\"Citation `markovian_chains' on page 1 undefined on inpu\\\", \\\"Citation `ood_baseline' on page 1 undefined on input li\\\", \\\"Reference `sec:related' on page 2 undefined on input line 39.\\\", \\\"Reference `sec:method' on page 2 undefined on input line 40.\\\", \\\"Reference `sec:results' on page 2 undefined on input line 41.\\\", \\\"Reference `sec:discussion' on page 2 undefined on input line 42.\\\", \\\"Citation `gltr' on page 2 undefined on input line 7.\\\", \\\"Citation `grover' on page 2 undefined on input line 7.\\\", \\\"Citation `release_strategies' on page 2 undefined on in\\\", \\\"Citation `detectgpt' on page 2 undefined on input line\\\", \\\"Citation `fast_detectgpt' on page 2 undefined on input\\\", \\\"Citation `binoculars' on page 2 undefined on input line\\\", \\\"Citation `dna_gpt' on page 2 undefined on input line 7.\\\", \\\"Citation `feat_aug_transformer' on page 2 undefined on\\\", \\\"Citation `reliable_detection' on page 2 undefined on in\\\", \\\"Citation `ld_score' on page 2 undefined on input line 7\\\", \\\"Citation `intrinsic_dimension' on page 2 undefined on i\\\", \\\"Citation `diveye' on page 2 undefined on input line 8.\\\", \\\"Citation `generator_barrier' on page 2 undefined on inp\\\", \\\"Citation `jawahar_survey' on page 2 undefined on input\\\", \\\"Reference `sec:baselines' on page 2 undefined on input line 11.\\\", \\\"Citation `paraphrase_evades' on page 2 undefined on inp\\\", \\\"Citation `detection_possibilities' on page 2 undefined\\\", \\\"Citation `ood_baseline' on page 2 undefined on input li\\\", \\\"Citation `self_consuming_mad' on page 2 undefined on in\\\", \\\"Citation `curse_of_recursion' on page 2 undefined on in\\\", \\\"Citation `model_collapse_avoidable' on page 2 undefined\\\", \\\"Citation `strong_model_collapse' on page 2 undefined on\\\", \\\"Citation `broken_telephone' on page 2 undefined on inpu\\\", \\\"Citation `markovian_chains' on page 2 undefined on inpu\\\", \\\"Citation `curious_decline' on page 3 undefined on input\\\", \\\"Citation `writing_diversity' on page 3 undefined on inp\\\", \\\"Citation `stamatatos_survey' on page 3 undefined on inp\\\", \\\"Citation `koppel_authorship' on page 3 undefined on inp\\\", \\\"Citation `uchendu_attribution' on page 3 undefined on i\\\", \\\"Citation `nucleus_sampling' on page 3 undefined on inpu\\\", \\\"Citation `dsir' on page 3 undefined on input line 44.\\\", \\\"Citation `qurating' on page 3 undefined on input line 4\\\", \\\"Citation `ccnet' on page 3 undefined on input line 44.\\\", \\\"Citation `watermark_llm' on page 3 undefined on input l\\\", \\\"Citation `synthid_text' on page 3 undefined on input li\\\", \\\"Citation `aaronson_watermark' on page 3 undefined on in\\\", \\\"Citation `chainwash' on page 3 undefined on input line\\\", \\\"Citation `min_k_percent' on page 3 undefined on input l\\\", \\\"Citation `detectgpt' on page 3 undefined on input line\\\", \\\"Citation `fast_detectgpt' on page 3 undefined on input\\\", \\\"Citation `binoculars' on page 3 undefined on input line\\\", \\\"Citation `uchendu_attribution' on page 3 undefined on i\\\", \\\"Citation `curse_of_recursion' on page 3 undefined on in\\\", \\\"Citation `self_consuming_mad' on page 3 undefined on in\\\", \\\"Citation `pythia' on page 3 undefined on input line 14.\\\", \\\"Citation `olmo' on page 3 undefined on input line 14.\\\", \\\"Citation `qwen3' on page 3 undefined on input line 14.\\\", \\\"Citation `nucleus_sampling' on page 3 undefined on inpu\\\", \\\"Citation `markovian_chains' on page 3 undefined on inpu\\\", \\\"Citation `detectgpt' on page 4 undefined on input line\\\", \\\"Citation `ood_baseline' on page 4 undefined on input li\\\", \\\"Citation `curious_decline' on page 4 undefined on input\\\", \\\"Citation `curious_decline' on page 4 undefined on input\\\", \\\"Citation `writing_diversity' on page 4 undefined on inp\\\", \\\"Citation `xgboost' on page 4 undefined on input line 52\\\", \\\"Citation `gltr' on page 4 undefined on input line 58.\\\", \\\"Citation `fast_detectgpt' on page 4 undefined on input\\\", \\\"Citation `ld_score' on page 4 undefined on input line 5\\\", \\\"Citation `binoculars' on page 4 undefined on input line\\\", \\\"Reference `sec:eval' on page 5 undefined on input line 7.\\\", \\\"Reference `tab:logo' on page 5 undefined on input line 7.\\\", \\\"Reference `sec:discussion' on page 5 undefined on input line 35.\\\", \\\"Citation `detectgpt' on page 5 undefined on input line\\\", \\\"Citation `binoculars' on page 5 undefined on input line\\\", \\\"Reference `fig:logo_performance' on page 5 undefined on input li\\\"], \\\"minor_warnings\\\": [\\\"Line number reference failed, re-run to get it right.\\\", \\\"File `figures/paper/fig2_logo_performance.pdf' not found on inpu\\\", \\\"Underfull \\\\\\\\hbox (badness 4391) in paragraph at lines 16--17\\\", \\\"Underfull \\\\\\\\hbox (badness 2173) in paragraph at lines 24--25\\\"], \\\"issues\\\": [\\\"compile failed: Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not\\\", \\\"79 critical warning(s): Citation `mapping_llm_science' on page 1 undefined on i; Citation `monitoring_ai_review' on page 1 undefined on; Citation `fast_detectgpt' on page 1 undefined on input; (+76 more)\\\", \\\"page count unavailable (compile likely failed)\\\"], \\\"summary\\\": \\\"FAIL: compile failed: Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not; 79 critical warning(s): Citation `mapping_llm_science' on page 1 undefined on i; Citation `monitoring_ai_review' on page 1 undefined on; Citation `fast_detectgpt' on page 1 undefined on input; (+76 more); page count unavailable (compile likely failed)\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"passed\": false, \"compiled\": {\"success\": false, \"pdf_path\": null, \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"Package natbib Warning: Citation `curious_decline' on page 4 undefined on input\\n line 37.\\n\\n\\nPackage natbib Warning: Citation `curious_decline' on page 4 undefined on input\\n line 43.\\n\\n\\nPackage natbib Warning: Citation `writing_diversity' on page 4 undefined on inp\\nut line 43.\\n\\n\\nPackage natbib Warning: Citation `xgboost' on page 4 undefined on input line 52\\n.\\n\\n\\nPackage natbib Warning: Citation `gltr' on page 4 undefined on input line 58.\\n\\n\\nPackage natbib Warning: Citation `fast_detectgpt' on page 4 undefined on input \\nline 58.\\n\\n\\nPackage natbib Warning: Citation `ld_score' on page 4 undefined on input line 5\\n8.\\n\\n\\nPackage natbib Warning: Citation `binoculars' on page 4 undefined on input line\\n 58.\\n\\n) (./results.tex [4]\\n\\nLaTeX Warning: Reference `sec:eval' on page 5 undefined on input line 7.\\n\\n\\nLaTeX Warning: Reference `tab:logo' on page 5 undefined on input line 7.\\n\\n\\nLaTeX Warning: Reference `sec:discussion' on page 5 undefined on input line 35.\\n\\n\\n\\nPackage natbib Warning: Citation `detectgpt' on page 5 undefined on input line \\n37.\\n\\n\\nPackage natbib Warning: Citation `binoculars' on page 5 undefined on input line\\n 37.\\n\\n\\nLaTeX Warning: Reference `fig:logo_performance' on page 5 undefined on input li\\nne 39.\\n\\n\\nLaTeX Warning: File `figures/paper/fig2_logo_performance.pdf' not found on inpu\\nt line 43.\\n\\n\\n! Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not \\nfound: using draft setting.\\n\\nSee the pdftex.def package documentation for explanation.\\nType  H &lt;return>  for immediate help.\\n ...                                              \\n                                                  \\nl.43 ...]{figures/paper/fig2_logo_performance.pdf}\\n                                                  \\nTry typing  &lt;return>  to proceed.\\nIf that doesn't work, type  X &lt;return>  to quit.\\n\\n \\nHere is how much of TeX's memory you used:\\n 15785 strings out of 469438\\n 248190 string characters out of 5468411\\n 718985 words of memory out of 5000000\\n 43925 multiletter control sequences out of 15000+600000\\n 680903 words of font info for 285 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,10n,93p,1001b,476s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n!  ==> Fatal error occurred, no output PDF file produced!\", \"error\": \"Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not\", \"pages\": null, \"warnings\": [\"Line number reference failed, re-run to get it right.\", \"Citation `mapping_llm_science' on page 1 undefined on i\", \"Citation `monitoring_ai_review' on page 1 undefined on\", \"Citation `fast_detectgpt' on page 1 undefined on input\", \"Citation `binoculars' on page 1 undefined on input line\", \"Citation `ld_score' on page 1 undefined on input line 8\", \"Citation `detectgpt' on page 1 undefined on input line\", \"Reference `sec:baselines' on page 1 undefined on input line 16.\", \"Citation `broken_telephone' on page 1 undefined on inpu\", \"Citation `markovian_chains' on page 1 undefined on inpu\", \"Citation `ood_baseline' on page 1 undefined on input li\", \"Reference `sec:related' on page 2 undefined on input line 39.\", \"Reference `sec:method' on page 2 undefined on input line 40.\", \"Reference `sec:results' on page 2 undefined on input line 41.\", \"Reference `sec:discussion' on page 2 undefined on input line 42.\", \"Citation `gltr' on page 2 undefined on input line 7.\", \"Citation `grover' on page 2 undefined on input line 7.\", \"Citation `release_strategies' on page 2 undefined on in\", \"Citation `detectgpt' on page 2 undefined on input line\", \"Citation `fast_detectgpt' on page 2 undefined on input\", \"Citation `binoculars' on page 2 undefined on input line\", \"Citation `dna_gpt' on page 2 undefined on input line 7.\", \"Citation `feat_aug_transformer' on page 2 undefined on\", \"Citation `reliable_detection' on page 2 undefined on in\", \"Citation `ld_score' on page 2 undefined on input line 7\", \"Citation `intrinsic_dimension' on page 2 undefined on i\", \"Citation `diveye' on page 2 undefined on input line 8.\", \"Citation `generator_barrier' on page 2 undefined on inp\", \"Citation `jawahar_survey' on page 2 undefined on input\", \"Reference `sec:baselines' on page 2 undefined on input line 11.\", \"Citation `paraphrase_evades' on page 2 undefined on inp\", \"Citation `detection_possibilities' on page 2 undefined\", \"Citation `ood_baseline' on page 2 undefined on input li\", \"Citation `self_consuming_mad' on page 2 undefined on in\", \"Citation `curse_of_recursion' on page 2 undefined on in\", \"Citation `model_collapse_avoidable' on page 2 undefined\", \"Citation `strong_model_collapse' on page 2 undefined on\", \"Citation `broken_telephone' on page 2 undefined on inpu\", \"Citation `markovian_chains' on page 2 undefined on inpu\", \"Citation `curious_decline' on page 3 undefined on input\", \"Citation `writing_diversity' on page 3 undefined on inp\", \"Citation `stamatatos_survey' on page 3 undefined on inp\", \"Citation `koppel_authorship' on page 3 undefined on inp\", \"Citation `uchendu_attribution' on page 3 undefined on i\", \"Citation `nucleus_sampling' on page 3 undefined on inpu\", \"Citation `dsir' on page 3 undefined on input line 44.\", \"Citation `qurating' on page 3 undefined on input line 4\", \"Citation `ccnet' on page 3 undefined on input line 44.\", \"Citation `watermark_llm' on page 3 undefined on input l\", \"Citation `synthid_text' on page 3 undefined on input li\", \"Citation `aaronson_watermark' on page 3 undefined on in\", \"Citation `chainwash' on page 3 undefined on input line\", \"Citation `min_k_percent' on page 3 undefined on input l\", \"Citation `detectgpt' on page 3 undefined on input line\", \"Citation `fast_detectgpt' on page 3 undefined on input\", \"Citation `binoculars' on page 3 undefined on input line\", \"Citation `uchendu_attribution' on page 3 undefined on i\", \"Citation `curse_of_recursion' on page 3 undefined on in\", \"Citation `self_consuming_mad' on page 3 undefined on in\", \"Citation `pythia' on page 3 undefined on input line 14.\", \"Citation `olmo' on page 3 undefined on input line 14.\", \"Citation `qwen3' on page 3 undefined on input line 14.\", \"Citation `nucleus_sampling' on page 3 undefined on inpu\", \"Citation `markovian_chains' on page 3 undefined on inpu\", \"Citation `detectgpt' on page 4 undefined on input line\", \"Citation `ood_baseline' on page 4 undefined on input li\", \"Citation `curious_decline' on page 4 undefined on input\", \"Citation `curious_decline' on page 4 undefined on input\", \"Citation `writing_diversity' on page 4 undefined on inp\", \"Citation `xgboost' on page 4 undefined on input line 52\", \"Citation `gltr' on page 4 undefined on input line 58.\", \"Citation `fast_detectgpt' on page 4 undefined on input\", \"Citation `ld_score' on page 4 undefined on input line 5\", \"Citation `binoculars' on page 4 undefined on input line\", \"Reference `sec:eval' on page 5 undefined on input line 7.\", \"Reference `tab:logo' on page 5 undefined on input line 7.\", \"Reference `sec:discussion' on page 5 undefined on input line 35.\", \"Citation `detectgpt' on page 5 undefined on input line\", \"Citation `binoculars' on page 5 undefined on input line\", \"Reference `fig:logo_performance' on page 5 undefined on input li\", \"File `figures/paper/fig2_logo_performance.pdf' not found on inpu\"]}, \"pages\": null, \"page_status\": \"unknown\", \"max_pages\": 8, \"min_pages\": 6, \"critical_warnings\": [\"Citation `mapping_llm_science' on page 1 undefined on i\", \"Citation `monitoring_ai_review' on page 1 undefined on\", \"Citation `fast_detectgpt' on page 1 undefined on input\", \"Citation `binoculars' on page 1 undefined on input line\", \"Citation `ld_score' on page 1 undefined on input line 8\", \"Citation `detectgpt' on page 1 undefined on input line\", \"Reference `sec:baselines' on page 1 undefined on input line 16.\", \"Citation `broken_telephone' on page 1 undefined on inpu\", \"Citation `markovian_chains' on page 1 undefined on inpu\", \"Citation `ood_baseline' on page 1 undefined on input li\", \"Reference `sec:related' on page 2 undefined on input line 39.\", \"Reference `sec:method' on page 2 undefined on input line 40.\", \"Reference `sec:results' on page 2 undefined on input line 41.\", \"Reference `sec:discussion' on page 2 undefined on input line 42.\", \"Citation `gltr' on page 2 undefined on input line 7.\", \"Citation `grover' on page 2 undefined on input line 7.\", \"Citation `release_strategies' on page 2 undefined on in\", \"Citation `detectgpt' on page 2 undefined on input line\", \"Citation `fast_detectgpt' on page 2 undefined on input\", \"Citation `binoculars' on page 2 undefined on input line\", \"Citation `dna_gpt' on page 2 undefined on input line 7.\", \"Citation `feat_aug_transformer' on page 2 undefined on\", \"Citation `reliable_detection' on page 2 undefined on in\", \"Citation `ld_score' on page 2 undefined on input line 7\", \"Citation `intrinsic_dimension' on page 2 undefined on i\", \"Citation `diveye' on page 2 undefined on input line 8.\", \"Citation `generator_barrier' on page 2 undefined on inp\", \"Citation `jawahar_survey' on page 2 undefined on input\", \"Reference `sec:baselines' on page 2 undefined on input line 11.\", \"Citation `paraphrase_evades' on page 2 undefined on inp\", \"Citation `detection_possibilities' on page 2 undefined\", \"Citation `ood_baseline' on page 2 undefined on input li\", \"Citation `self_consuming_mad' on page 2 undefined on in\", \"Citation `curse_of_recursion' on page 2 undefined on in\", \"Citation `model_collapse_avoidable' on page 2 undefined\", \"Citation `strong_model_collapse' on page 2 undefined on\", \"Citation `broken_telephone' on page 2 undefined on inpu\", \"Citation `markovian_chains' on page 2 undefined on inpu\", \"Citation `curious_decline' on page 3 undefined on input\", \"Citation `writing_diversity' on page 3 undefined on inp\", \"Citation `stamatatos_survey' on page 3 undefined on inp\", \"Citation `koppel_authorship' on page 3 undefined on inp\", \"Citation `uchendu_attribution' on page 3 undefined on i\", \"Citation `nucleus_sampling' on page 3 undefined on inpu\", \"Citation `dsir' on page 3 undefined on input line 44.\", \"Citation `qurating' on page 3 undefined on input line 4\", \"Citation `ccnet' on page 3 undefined on input line 44.\", \"Citation `watermark_llm' on page 3 undefined on input l\", \"Citation `synthid_text' on page 3 undefined on input li\", \"Citation `aaronson_watermark' on page 3 undefined on in\", \"Citation `chainwash' on page 3 undefined on input line\", \"Citation `min_k_percent' on page 3 undefined on input l\", \"Citation `detectgpt' on page 3 undefined on input line\", \"Citation `fast_detectgpt' on page 3 undefined on input\", \"Citation `binoculars' on page 3 undefined on input line\", \"Citation `uchendu_attribution' on page 3 undefined on i\", \"Citation `curse_of_recursion' on page 3 undefined on in\", \"Citation `self_consuming_mad' on page 3 undefined on in\", \"Citation `pythia' on page 3 undefined on input line 14.\", \"Citation `olmo' on page 3 undefined on input line 14.\", \"Citation `qwen3' on page 3 undefined on input line 14.\", \"Citation `nucleus_sampling' on page 3 undefined on inpu\", \"Citation `markovian_chains' on page 3 undefined on inpu\", \"Citation `detectgpt' on page 4 undefined on input line\", \"Citation `ood_baseline' on page 4 undefined on input li\", \"Citation `curious_decline' on page 4 undefined on input\", \"Citation `curious_decline' on page 4 undefined on input\", \"Citation `writing_diversity' on page 4 undefined on inp\", \"Citation `xgboost' on page 4 undefined on input line 52\", \"Citation `gltr' on page 4 undefined on input line 58.\", \"Citation `fast_detectgpt' on page 4 undefined on input\", \"Citation `ld_score' on page 4 undefined on input line 5\", \"Citation `binoculars' on page 4 undefined on input line\", \"Reference `sec:eval' on page 5 undefined on input line 7.\", \"Reference `tab:logo' on page 5 undefined on input line 7.\", \"Reference `sec:discussion' on page 5 undefined on input line 35.\", \"Citation `detectgpt' on page 5 undefined on input line\", \"Citation `binoculars' on page 5 undefined on input line\", \"Reference `fig:logo_performance' on page 5 undefined on input li\"], \"minor_warnings\": [\"Line number reference failed, re-run to get it right.\", \"File `figures/paper/fig2_logo_performance.pdf' not found on inpu\", \"Underfull \\\\hbox (badness 4391) in paragraph at lines 16--17\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 24--25\"], \"issues\": [\"compile failed: Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not\", \"79 critical warning(s): Citation `mapping_llm_science' on page 1 undefined on i; Citation `monitoring_ai_review' on page 1 undefined on; Citation `fast_detectgpt' on page 1 undefined on input; (+76 more)\", \"page count unavailable (compile likely failed)\"], \"summary\": \"FAIL: compile failed: Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not; 79 critical warning(s): Citation `mapping_llm_science' on page 1 undefined on i; Citation `monitoring_ai_review' on page 1 undefined on; Citation `fast_detectgpt' on page 1 undefined on input; (+76 more); page count unavailable (compile likely failed)\"}"
    }
  },
  "sourceToolAssistantUUID": "325696cb-2e96-4e59-9a1d-4bacf03b7484",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

</details>

---


### Runtime record

_source line 398_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director 将结果发给 Director。",
  "leafUuid": "1ef65ac1-fdf1-47ef-9485-1c1098132eec",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e"
}
```

---


### Runtime record

_source line 399_

```json
{
  "type": "ai-title",
  "aiTitle": "System message notification handling",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e"
}
```

---


### Assistant

_source line 400 · 2026-05-15T05:02:55.075Z_

<details><summary>Logged reasoning block</summary>

```text
Two main issues:
1. Figure PDFs not found - the `\includegraphics` paths are relative but the figures are stored in the artifacts directory, not in the paper directory
2. Citations undefined on first pass is normal for LaTeX (need multiple passes) - but the fatal error is the missing figure file

Let me check where the figure files actually are.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ef65ac1-fdf1-47ef-9485-1c1098132eec",
  "isSidechain": false,
  "requestId": "req_011Cb3mYHwTf9868BBWKnem4",
  "type": "assistant",
  "uuid": "e07f908a-b538-485a-8f6f-49ff9eaed0a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012C3tTEjjPEv3JanXKc8zM5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4515,
      "cache_read_input_tokens": 55419,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4515,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 318,
          "cache_read_input_tokens": 55419,
          "cache_creation_input_tokens": 4515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4515
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 401 · 2026-05-15T05:02:56.299Z_

编译失败因为 figure 文件路径不对。需要检查图表实际位置并创建符号链接或修改路径。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e07f908a-b538-485a-8f6f-49ff9eaed0a9",
  "isSidechain": false,
  "requestId": "req_011Cb3mYHwTf9868BBWKnem4",
  "type": "assistant",
  "uuid": "e4867386-34aa-47ac-be8a-47afb14e9759",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012C3tTEjjPEv3JanXKc8zM5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4515,
      "cache_read_input_tokens": 55419,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4515,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 318,
          "cache_read_input_tokens": 55419,
          "cache_creation_input_tokens": 4515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4515
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-15T05:02:58.243Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Po944jyY7HNRCN3H3ya3Tg`</summary>

```json
{
  "pattern": "**/figures/paper/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4867386-34aa-47ac-be8a-47afb14e9759",
  "isSidechain": false,
  "requestId": "req_011Cb3mYHwTf9868BBWKnem4",
  "type": "assistant",
  "uuid": "1a51d55d-8038-4a8c-8b98-2a14a47aac05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012C3tTEjjPEv3JanXKc8zM5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4515,
      "cache_read_input_tokens": 55419,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4515,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 318,
          "cache_read_input_tokens": 55419,
          "cache_creation_input_tokens": 4515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4515
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-15T05:02:58.726Z_

<details><summary>↩ Tool result · `toolu_01TL1Ng4ZtQLC3Jhbt96sxRU`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper/fig1_differential_response.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig1_differential_response.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper/fig2_logo_performance.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper/fig3_baseline_comparison.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig4_downstream_negative.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper/fig4_downstream_negative.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig4_downstream_negative_20bbd0.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dd6f418-4ec6-42e4-bf04-3cdf433f2490",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "b5a39028-d03b-4475-987f-8ac3fbf72bdf",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper/fig1_differential_response.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig1_differential_response.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper/fig2_logo_performance.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper/fig3_baseline_comparison.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig4_downstream_negative.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper/fig4_downstream_negative.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig4_downstream_negative_20bbd0.pdf"
    ],
    "durationMs": 33,
    "numFiles": 7,
    "truncated": false
  },
  "sourceToolAssistantUUID": "8dd6f418-4ec6-42e4-bf04-3cdf433f2490",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

</details>

---


### Tool result

_source line 404 · 2026-05-15T05:02:58.276Z_

<details><summary>↩ Tool result · `toolu_01Po944jyY7HNRCN3H3ya3Tg`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper/fig1_differential_response.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper/fig2_logo_performance.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper/fig3_baseline_comparison.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper/fig4_downstream_negative.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a51d55d-8038-4a8c-8b98-2a14a47aac05",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "d3f69da7-2dc8-4200-be0b-3deabd7cacdb",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper/fig1_differential_response.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper/fig2_logo_performance.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper/fig3_baseline_comparison.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper/fig4_downstream_negative.pdf"
    ],
    "durationMs": 28,
    "numFiles": 4,
    "truncated": false
  },
  "sourceToolAssistantUUID": "1a51d55d-8038-4a8c-8b98-2a14a47aac05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

</details>

---


### Tool call

_source line 405 · 2026-05-15T05:02:58.686Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TL1Ng4ZtQLC3Jhbt96sxRU`</summary>

```json
{
  "pattern": "**/fig*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3f69da7-2dc8-4200-be0b-3deabd7cacdb",
  "isSidechain": false,
  "requestId": "req_011Cb3mYHwTf9868BBWKnem4",
  "type": "assistant",
  "uuid": "8dd6f418-4ec6-42e4-bf04-3cdf433f2490",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012C3tTEjjPEv3JanXKc8zM5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4515,
      "cache_read_input_tokens": 55419,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4515,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 318,
          "cache_read_input_tokens": 55419,
          "cache_creation_input_tokens": 4515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4515
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 406 · 2026-05-15T05:02:58.753Z_

```json
{
  "parentUuid": "b5a39028-d03b-4475-987f-8ac3fbf72bdf",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ee31faec-5a91-4d7b-9cdc-708a70b2d148",
  "timestamp": "2026-05-15T05:02:58.753Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

---


### Assistant

_source line 407 · 2026-05-15T05:03:08.850Z_

<details><summary>Logged reasoning block</summary>

```text
The figures are at `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper/`. The paper directory is `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/`. The `\includegraphics` paths are `figures/paper/fig*.pdf`, which is relative to the paper directory.

I need to create a symlink from the paper directory to the figures directory. The path `figures/paper/fig2_logo_performance.pdf` relative to the paper dir (`docs/paper/`) would look for it at `docs/paper/figures/paper/fig2_logo_performance.pdf`, which doesn't exist.


The actual figures are at `../../figures/paper/` relative to the paper directory, so I'll create a symlink at `docs/paper/figures` pointing to `../../figures` rather than modifying all the LaTeX paths.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee31faec-5a91-4d7b-9cdc-708a70b2d148",
  "isSidechain": false,
  "requestId": "req_011Cb3mYtcnZEyu563BJ2ELM",
  "type": "assistant",
  "uuid": "a5b33cb2-da1b-4d7b-9ac0-4e58d9d500f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gDvfPasMhaDF9JnyN9YKP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 59934,
      "output_tokens": 451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 451,
          "cache_read_input_tokens": 59934,
          "cache_creation_input_tokens": 951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 951
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 408 · 2026-05-15T05:03:08.854Z_

图表文件在 `projects/gen-depth-fingerprint/figures/paper/`，但 LaTeX 从 `docs/paper/` 编译，相对路径找不到。创建符号链接。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5b33cb2-da1b-4d7b-9ac0-4e58d9d500f9",
  "isSidechain": false,
  "requestId": "req_011Cb3mYtcnZEyu563BJ2ELM",
  "type": "assistant",
  "uuid": "4639c3de-2c06-408e-a44a-a808b07b8556",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gDvfPasMhaDF9JnyN9YKP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 59934,
      "output_tokens": 451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 451,
          "cache_read_input_tokens": 59934,
          "cache_creation_input_tokens": 951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 951
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 409 · 2026-05-15T05:03:08.925Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0127WqgE5A2ki9o9LfLXGUf3`</summary>

```json
{
  "command": "ln -sf /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/figures",
  "description": "Create symlink from paper dir to figures dir"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4639c3de-2c06-408e-a44a-a808b07b8556",
  "isSidechain": false,
  "requestId": "req_011Cb3mYtcnZEyu563BJ2ELM",
  "type": "assistant",
  "uuid": "a152e1d5-2833-4eba-bfec-b47f90d21adc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gDvfPasMhaDF9JnyN9YKP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 59934,
      "output_tokens": 451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 451,
          "cache_read_input_tokens": 59934,
          "cache_creation_input_tokens": 951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 951
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 410 · 2026-05-15T05:03:09.062Z_

<details><summary>↩ Tool result · `toolu_0127WqgE5A2ki9o9LfLXGUf3`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a152e1d5-2833-4eba-bfec-b47f90d21adc",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "791943a8-4329-4c0c-a82a-a2b7a6b880e6",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "a152e1d5-2833-4eba-bfec-b47f90d21adc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

</details>

---


### Tool call

_source line 411 · 2026-05-15T05:03:12.429Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_compile_and_check · `toolu_01MAZFXJB2Q8Hj44sU8gfuQo`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "max_pages": 8,
  "min_pages": 6,
  "clean": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "791943a8-4329-4c0c-a82a-a2b7a6b880e6",
  "isSidechain": false,
  "requestId": "req_011Cb3mZech9KGJzEhazK4QH",
  "type": "assistant",
  "uuid": "ac053bf6-15cd-4f6c-a05b-5d9685c6f151",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3BnjhgxvAuhCid6YKnic2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 469,
      "cache_read_input_tokens": 60885,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 469,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 60885,
          "cache_creation_input_tokens": 469,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 469
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 412 · 2026-05-15T05:03:13.321Z_

<details><summary>↩ Tool result · `toolu_01MAZFXJB2Q8Hj44sU8gfuQo`</summary>

```text
{"result":"{\"success\": false, \"passed\": false, \"compiled\": {\"success\": false, \"pdf_path\": null, \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"Package natbib Warning: Citation `curious_decline' on page 4 undefined on input\\n line 37.\\n\\n\\nPackage natbib Warning: Citation `curious_decline' on page 4 undefined on input\\n line 43.\\n\\n\\nPackage natbib Warning: Citation `writing_diversity' on page 4 undefined on inp\\nut line 43.\\n\\n\\nPackage natbib Warning: Citation `xgboost' on page 4 undefined on input line 52\\n.\\n\\n\\nPackage natbib Warning: Citation `gltr' on page 4 undefined on input line 58.\\n\\n\\nPackage natbib Warning: Citation `fast_detectgpt' on page 4 undefined on input \\nline 58.\\n\\n\\nPackage natbib Warning: Citation `ld_score' on page 4 undefined on input line 5\\n8.\\n\\n\\nPackage natbib Warning: Citation `binoculars' on page 4 undefined on input line\\n 58.\\n\\n) (./results.tex [4]\\n\\nLaTeX Warning: Reference `sec:eval' on page 5 undefined on input line 7.\\n\\n\\nLaTeX Warning: Reference `tab:logo' on page 5 undefined on input line 7.\\n\\n\\nLaTeX Warning: Reference `sec:discussion' on page 5 undefined on input line 35.\\n\\n\\n\\nPackage natbib Warning: Citation `detectgpt' on page 5 undefined on input line \\n37.\\n\\n\\nPackage natbib Warning: Citation `binoculars' on page 5 undefined on input line\\n 37.\\n\\n\\nLaTeX Warning: Reference `fig:logo_performance' on page 5 undefined on input li\\nne 39.\\n\\n\\nLaTeX Warning: File `figures/paper/fig2_logo_performance.pdf' not found on inpu\\nt line 43.\\n\\n\\n! Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not \\nfound: using draft setting.\\n\\nSee the pdftex.def package documentation for explanation.\\nType  H &lt;return>  for immediate help.\\n ...                                              \\n                                                  \\nl.43 ...]{figures/paper/fig2_logo_performance.pdf}\\n                                                  \\nTry typing  &lt;return>  to proceed.\\nIf that doesn't work, type  X &lt;return>  to quit.\\n\\n \\nHere is how much of TeX's memory you used:\\n 15785 strings out of 469438\\n 248190 string characters out of 5468411\\n 718985 words of memory out of 5000000\\n 43925 multiletter control sequences out of 15000+600000\\n 680903 words of font info for 285 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,10n,93p,1001b,476s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n!  ==> Fatal error occurred, no output PDF file produced!\", \"error\": \"Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not\", \"pages\": null, \"warnings\": [\"Line number reference failed, re-run to get it right.\", \"Citation `mapping_llm_science' on page 1 undefined on i\", \"Citation `monitoring_ai_review' on page 1 undefined on\", \"Citation `fast_detectgpt' on page 1 undefined on input\", \"Citation `binoculars' on page 1 undefined on input line\", \"Citation `ld_score' on page 1 undefined on input line 8\", \"Citation `detectgpt' on page 1 undefined on input line\", \"Reference `sec:baselines' on page 1 undefined on input line 16.\", \"Citation `broken_telephone' on page 1 undefined on inpu\", \"Citation `markovian_chains' on page 1 undefined on inpu\", \"Citation `ood_baseline' on page 1 undefined on input li\", \"Reference `sec:related' on page 2 undefined on input line 39.\", \"Reference `sec:method' on page 2 undefined on input line 40.\", \"Reference `sec:results' on page 2 undefined on input line 41.\", \"Reference `sec:discussion' on page 2 undefined on input line 42.\", \"Citation `gltr' on page 2 undefined on input line 7.\", \"Citation `grover' on page 2 undefined on input line 7.\", \"Citation `release_strategies' on page 2 undefined on in\", \"Citation `detectgpt' on page 2 undefined on input line\", \"Citation `fast_detectgpt' on page 2 undefined on input\", \"Citation `binoculars' on page 2 undefined on input line\", \"Citation `dna_gpt' on page 2 undefined on input line 7.\", \"Citation `feat_aug_transformer' on page 2 undefined on\", \"Citation `reliable_detection' on page 2 undefined on in\", \"Citation `ld_score' on page 2 undefined on input line 7\", \"Citation `intrinsic_dimension' on page 2 undefined on i\", \"Citation `diveye' on page 2 undefined on input line 8.\", \"Citation `generator_barrier' on page 2 undefined on inp\", \"Citation `jawahar_survey' on page 2 undefined on input\", \"Reference `sec:baselines' on page 2 undefined on input line 11.\", \"Citation `paraphrase_evades' on page 2 undefined on inp\", \"Citation `detection_possibilities' on page 2 undefined\", \"Citation `ood_baseline' on page 2 undefined on input li\", \"Citation `self_consuming_mad' on page 2 undefined on in\", \"Citation `curse_of_recursion' on page 2 undefined on in\", \"Citation `model_collapse_avoidable' on page 2 undefined\", \"Citation `strong_model_collapse' on page 2 undefined on\", \"Citation `broken_telephone' on page 2 undefined on inpu\", \"Citation `markovian_chains' on page 2 undefined on inpu\", \"Citation `curious_decline' on page 3 undefined on input\", \"Citation `writing_diversity' on page 3 undefined on inp\", \"Citation `stamatatos_survey' on page 3 undefined on inp\", \"Citation `koppel_authorship' on page 3 undefined on inp\", \"Citation `uchendu_attribution' on page 3 undefined on i\", \"Citation `nucleus_sampling' on page 3 undefined on inpu\", \"Citation `dsir' on page 3 undefined on input line 44.\", \"Citation `qurating' on page 3 undefined on input line 4\", \"Citation `ccnet' on page 3 undefined on input line 44.\", \"Citation `watermark_llm' on page 3 undefined on input l\", \"Citation `synthid_text' on page 3 undefined on input li\", \"Citation `aaronson_watermark' on page 3 undefined on in\", \"Citation `chainwash' on page 3 undefined on input line\", \"Citation `min_k_percent' on page 3 undefined on input l\", \"Citation `detectgpt' on page 3 undefined on input line\", \"Citation `fast_detectgpt' on page 3 undefined on input\", \"Citation `binoculars' on page 3 undefined on input line\", \"Citation `uchendu_attribution' on page 3 undefined on i\", \"Citation `curse_of_recursion' on page 3 undefined on in\", \"Citation `self_consuming_mad' on page 3 undefined on in\", \"Citation `pythia' on page 3 undefined on input line 14.\", \"Citation `olmo' on page 3 undefined on input line 14.\", \"Citation `qwen3' on page 3 undefined on input line 14.\", \"Citation `nucleus_sampling' on page 3 undefined on inpu\", \"Citation `markovian_chains' on page 3 undefined on inpu\", \"Citation `detectgpt' on page 4 undefined on input line\", \"Citation `ood_baseline' on page 4 undefined on input li\", \"Citation `curious_decline' on page 4 undefined on input\", \"Citation `curious_decline' on page 4 undefined on input\", \"Citation `writing_diversity' on page 4 undefined on inp\", \"Citation `xgboost' on page 4 undefined on input line 52\", \"Citation `gltr' on page 4 undefined on input line 58.\", \"Citation `fast_detectgpt' on page 4 undefined on input\", \"Citation `ld_score' on page 4 undefined on input line 5\", \"Citation `binoculars' on page 4 undefined on input line\", \"Reference `sec:eval' on page 5 undefined on input line 7.\", \"Reference `tab:logo' on page 5 undefined on input line 7.\", \"Reference `sec:discussion' on page 5 undefined on input line 35.\", \"Citation `detectgpt' on page 5 undefined on input line\", \"Citation `binoculars' on page 5 undefined on input line\", \"Reference `fig:logo_performance' on page 5 undefined on input li\", \"File `figures/paper/fig2_logo_performance.pdf' not found on inpu\"]}, \"pages\": null, \"page_status\": \"unknown\", \"max_pages\": 8, \"min_pages\": 6, \"critical_warnings\": [\"Citation `mapping_llm_science' on page 1 undefined on i\", \"Citation `monitoring_ai_review' on page 1 undefined on\", \"Citation `fast_detectgpt' on page 1 undefined on input\", \"Citation `binoculars' on page 1 undefined on input line\", \"Citation `ld_score' on page 1 undefined on input line 8\", \"Citation `detectgpt' on page 1 undefined on input line\", \"Reference `sec:baselines' on page 1 undefined on input line 16.\", \"Citation `broken_telephone' on page 1 undefined on inpu\", \"Citation `markovian_chains' on page 1 undefined on inpu\", \"Citation `ood_baseline' on page 1 undefined on input li\", \"Reference `sec:related' on page 2 undefined on input line 39.\", \"Reference `sec:method' on page 2 undefined on input line 40.\", \"Reference `sec:results' on page 2 undefined on input line 41.\", \"Reference `sec:discussion' on page 2 undefined on input line 42.\", \"Citation `gltr' on page 2 undefined on input line 7.\", \"Citation `grover' on page 2 undefined on input line 7.\", \"Citation `release_strategies' on page 2 undefined on in\", \"Citation `detectgpt' on page 2 undefined on input line\", \"Citation `fast_detectgpt' on page 2 undefined on input\", \"Citation `binoculars' on page 2 undefined on input line\", \"Citation `dna_gpt' on page 2 undefined on input line 7.\", \"Citation `feat_aug_transformer' on page 2 undefined on\", \"Citation `reliable_detection' on page 2 undefined on in\", \"Citation `ld_score' on page 2 undefined on input line 7\", \"Citation `intrinsic_dimension' on page 2 undefined on i\", \"Citation `diveye' on page 2 undefined on input line 8.\", \"Citation `generator_barrier' on page 2 undefined on inp\", \"Citation `jawahar_survey' on page 2 undefined on input\", \"Reference `sec:baselines' on page 2 undefined on input line 11.\", \"Citation `paraphrase_evades' on page 2 undefined on inp\", \"Citation `detection_possibilities' on page 2 undefined\", \"Citation `ood_baseline' on page 2 undefined on input li\", \"Citation `self_consuming_mad' on page 2 undefined on in\", \"Citation `curse_of_recursion' on page 2 undefined on in\", \"Citation `model_collapse_avoidable' on page 2 undefined\", \"Citation `strong_model_collapse' on page 2 undefined on\", \"Citation `broken_telephone' on page 2 undefined on inpu\", \"Citation `markovian_chains' on page 2 undefined on inpu\", \"Citation `curious_decline' on page 3 undefined on input\", \"Citation `writing_diversity' on page 3 undefined on inp\", \"Citation `stamatatos_survey' on page 3 undefined on inp\", \"Citation `koppel_authorship' on page 3 undefined on inp\", \"Citation `uchendu_attribution' on page 3 undefined on i\", \"Citation `nucleus_sampling' on page 3 undefined on inpu\", \"Citation `dsir' on page 3 undefined on input line 44.\", \"Citation `qurating' on page 3 undefined on input line 4\", \"Citation `ccnet' on page 3 undefined on input line 44.\", \"Citation `watermark_llm' on page 3 undefined on input l\", \"Citation `synthid_text' on page 3 undefined on input li\", \"Citation `aaronson_watermark' on page 3 undefined on in\", \"Citation `chainwash' on page 3 undefined on input line\", \"Citation `min_k_percent' on page 3 undefined on input l\", \"Citation `detectgpt' on page 3 undefined on input line\", \"Citation `fast_detectgpt' on page 3 undefined on input\", \"Citation `binoculars' on page 3 undefined on input line\", \"Citation `uchendu_attribution' on page 3 undefined on i\", \"Citation `curse_of_recursion' on page 3 undefined on in\", \"Citation `self_consuming_mad' on page 3 undefined on in\", \"Citation `pythia' on page 3 undefined on input line 14.\", \"Citation `olmo' on page 3 undefined on input line 14.\", \"Citation `qwen3' on page 3 undefined on input line 14.\", \"Citation `nucleus_sampling' on page 3 undefined on inpu\", \"Citation `markovian_chains' on page 3 undefined on inpu\", \"Citation `detectgpt' on page 4 undefined on input line\", \"Citation `ood_baseline' on page 4 undefined on input li\", \"Citation `curious_decline' on page 4 undefined on input\", \"Citation `curious_decline' on page 4 undefined on input\", \"Citation `writing_diversity' on page 4 undefined on inp\", \"Citation `xgboost' on page 4 undefined on input line 52\", \"Citation `gltr' on page 4 undefined on input line 58.\", \"Citation `fast_detectgpt' on page 4 undefined on input\", \"Citation `ld_score' on page 4 undefined on input line 5\", \"Citation `binoculars' on page 4 undefined on input line\", \"Reference `sec:eval' on page 5 undefined on input line 7.\", \"Reference `tab:logo' on page 5 undefined on input line 7.\", \"Reference `sec:discussion' on page 5 undefined on input line 35.\", \"Citation `detectgpt' on page 5 undefined on input line\", \"Citation `binoculars' on page 5 undefined on input line\", \"Reference `fig:logo_performance' on page 5 undefined on input li\"], \"minor_warnings\": [\"Line number reference failed, re-run to get it right.\", \"File `figures/paper/fig2_logo_performance.pdf' not found on inpu\", \"Underfull \\\\hbox (badness 4391) in paragraph at lines 16--17\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 24--25\"], \"issues\": [\"compile failed: Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not\", \"79 critical warning(s): Citation `mapping_llm_science' on page 1 undefined on i; Citation `monitoring_ai_review' on page 1 undefined on; Citation `fast_detectgpt' on page 1 undefined on input; (+76 more)\", \"page count unavailable (compile likely failed)\"], \"summary\": \"FAIL: compile failed: Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not; 79 critical warning(s): Citation `mapping_llm_science' on page 1 undefined on i; Citation `monitoring_ai_review' on page 1 undefined on; Citation `fast_detectgpt' on page 1 undefined on input; (+76 more); page count unavailable (compile likely failed)\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac053bf6-15cd-4f6c-a05b-5d9685c6f151",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "5efbc811-6d43-4489-9413-56556d914baa",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"passed\\\": false, \\\"compiled\\\": {\\\"success\\\": false, \\\"pdf_path\\\": null, \\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper\\\", \\\"main_tex\\\": \\\"main.tex\\\", \\\"log_tail\\\": \\\"Package natbib Warning: Citation `curious_decline' on page 4 undefined on input\\\\n line 37.\\\\n\\\\n\\\\nPackage natbib Warning: Citation `curious_decline' on page 4 undefined on input\\\\n line 43.\\\\n\\\\n\\\\nPackage natbib Warning: Citation `writing_diversity' on page 4 undefined on inp\\\\nut line 43.\\\\n\\\\n\\\\nPackage natbib Warning: Citation `xgboost' on page 4 undefined on input line 52\\\\n.\\\\n\\\\n\\\\nPackage natbib Warning: Citation `gltr' on page 4 undefined on input line 58.\\\\n\\\\n\\\\nPackage natbib Warning: Citation `fast_detectgpt' on page 4 undefined on input \\\\nline 58.\\\\n\\\\n\\\\nPackage natbib Warning: Citation `ld_score' on page 4 undefined on input line 5\\\\n8.\\\\n\\\\n\\\\nPackage natbib Warning: Citation `binoculars' on page 4 undefined on input line\\\\n 58.\\\\n\\\\n) (./results.tex [4]\\\\n\\\\nLaTeX Warning: Reference `sec:eval' on page 5 undefined on input line 7.\\\\n\\\\n\\\\nLaTeX Warning: Reference `tab:logo' on page 5 undefined on input line 7.\\\\n\\\\n\\\\nLaTeX Warning: Reference `sec:discussion' on page 5 undefined on input line 35.\\\\n\\\\n\\\\n\\\\nPackage natbib Warning: Citation `detectgpt' on page 5 undefined on input line \\\\n37.\\\\n\\\\n\\\\nPackage natbib Warning: Citation `binoculars' on page 5 undefined on input line\\\\n 37.\\\\n\\\\n\\\\nLaTeX Warning: Reference `fig:logo_performance' on page 5 undefined on input li\\\\nne 39.\\\\n\\\\n\\\\nLaTeX Warning: File `figures/paper/fig2_logo_performance.pdf' not found on inpu\\\\nt line 43.\\\\n\\\\n\\\\n! Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not \\\\nfound: using draft setting.\\\\n\\\\nSee the pdftex.def package documentation for explanation.\\\\nType  H &lt;return>  for immediate help.\\\\n ...                                              \\\\n                                                  \\\\nl.43 ...]{figures/paper/fig2_logo_performance.pdf}\\\\n                                                  \\\\nTry typing  &lt;return>  to proceed.\\\\nIf that doesn't work, type  X &lt;return>  to quit.\\\\n\\\\n \\\\nHere is how much of TeX's memory you used:\\\\n 15785 strings out of 469438\\\\n 248190 string characters out of 5468411\\\\n 718985 words of memory out of 5000000\\\\n 43925 multiletter control sequences out of 15000+600000\\\\n 680903 words of font info for 285 fonts, out of 8000000 for 9000\\\\n 59 hyphenation exceptions out of 8191\\\\n 84i,10n,93p,1001b,476s stack positions out of 10000i,1000n,20000p,200000b,200000s\\\\n!  ==> Fatal error occurred, no output PDF file produced!\\\", \\\"error\\\": \\\"Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not\\\", \\\"pages\\\": null, \\\"warnings\\\": [\\\"Line number reference failed, re-run to get it right.\\\", \\\"Citation `mapping_llm_science' on page 1 undefined on i\\\", \\\"Citation `monitoring_ai_review' on page 1 undefined on\\\", \\\"Citation `fast_detectgpt' on page 1 undefined on input\\\", \\\"Citation `binoculars' on page 1 undefined on input line\\\", \\\"Citation `ld_score' on page 1 undefined on input line 8\\\", \\\"Citation `detectgpt' on page 1 undefined on input line\\\", \\\"Reference `sec:baselines' on page 1 undefined on input line 16.\\\", \\\"Citation `broken_telephone' on page 1 undefined on inpu\\\", \\\"Citation `markovian_chains' on page 1 undefined on inpu\\\", \\\"Citation `ood_baseline' on page 1 undefined on input li\\\", \\\"Reference `sec:related' on page 2 undefined on input line 39.\\\", \\\"Reference `sec:method' on page 2 undefined on input line 40.\\\", \\\"Reference `sec:results' on page 2 undefined on input line 41.\\\", \\\"Reference `sec:discussion' on page 2 undefined on input line 42.\\\", \\\"Citation `gltr' on page 2 undefined on input line 7.\\\", \\\"Citation `grover' on page 2 undefined on input line 7.\\\", \\\"Citation `release_strategies' on page 2 undefined on in\\\", \\\"Citation `detectgpt' on page 2 undefined on input line\\\", \\\"Citation `fast_detectgpt' on page 2 undefined on input\\\", \\\"Citation `binoculars' on page 2 undefined on input line\\\", \\\"Citation `dna_gpt' on page 2 undefined on input line 7.\\\", \\\"Citation `feat_aug_transformer' on page 2 undefined on\\\", \\\"Citation `reliable_detection' on page 2 undefined on in\\\", \\\"Citation `ld_score' on page 2 undefined on input line 7\\\", \\\"Citation `intrinsic_dimension' on page 2 undefined on i\\\", \\\"Citation `diveye' on page 2 undefined on input line 8.\\\", \\\"Citation `generator_barrier' on page 2 undefined on inp\\\", \\\"Citation `jawahar_survey' on page 2 undefined on input\\\", \\\"Reference `sec:baselines' on page 2 undefined on input line 11.\\\", \\\"Citation `paraphrase_evades' on page 2 undefined on inp\\\", \\\"Citation `detection_possibilities' on page 2 undefined\\\", \\\"Citation `ood_baseline' on page 2 undefined on input li\\\", \\\"Citation `self_consuming_mad' on page 2 undefined on in\\\", \\\"Citation `curse_of_recursion' on page 2 undefined on in\\\", \\\"Citation `model_collapse_avoidable' on page 2 undefined\\\", \\\"Citation `strong_model_collapse' on page 2 undefined on\\\", \\\"Citation `broken_telephone' on page 2 undefined on inpu\\\", \\\"Citation `markovian_chains' on page 2 undefined on inpu\\\", \\\"Citation `curious_decline' on page 3 undefined on input\\\", \\\"Citation `writing_diversity' on page 3 undefined on inp\\\", \\\"Citation `stamatatos_survey' on page 3 undefined on inp\\\", \\\"Citation `koppel_authorship' on page 3 undefined on inp\\\", \\\"Citation `uchendu_attribution' on page 3 undefined on i\\\", \\\"Citation `nucleus_sampling' on page 3 undefined on inpu\\\", \\\"Citation `dsir' on page 3 undefined on input line 44.\\\", \\\"Citation `qurating' on page 3 undefined on input line 4\\\", \\\"Citation `ccnet' on page 3 undefined on input line 44.\\\", \\\"Citation `watermark_llm' on page 3 undefined on input l\\\", \\\"Citation `synthid_text' on page 3 undefined on input li\\\", \\\"Citation `aaronson_watermark' on page 3 undefined on in\\\", \\\"Citation `chainwash' on page 3 undefined on input line\\\", \\\"Citation `min_k_percent' on page 3 undefined on input l\\\", \\\"Citation `detectgpt' on page 3 undefined on input line\\\", \\\"Citation `fast_detectgpt' on page 3 undefined on input\\\", \\\"Citation `binoculars' on page 3 undefined on input line\\\", \\\"Citation `uchendu_attribution' on page 3 undefined on i\\\", \\\"Citation `curse_of_recursion' on page 3 undefined on in\\\", \\\"Citation `self_consuming_mad' on page 3 undefined on in\\\", \\\"Citation `pythia' on page 3 undefined on input line 14.\\\", \\\"Citation `olmo' on page 3 undefined on input line 14.\\\", \\\"Citation `qwen3' on page 3 undefined on input line 14.\\\", \\\"Citation `nucleus_sampling' on page 3 undefined on inpu\\\", \\\"Citation `markovian_chains' on page 3 undefined on inpu\\\", \\\"Citation `detectgpt' on page 4 undefined on input line\\\", \\\"Citation `ood_baseline' on page 4 undefined on input li\\\", \\\"Citation `curious_decline' on page 4 undefined on input\\\", \\\"Citation `curious_decline' on page 4 undefined on input\\\", \\\"Citation `writing_diversity' on page 4 undefined on inp\\\", \\\"Citation `xgboost' on page 4 undefined on input line 52\\\", \\\"Citation `gltr' on page 4 undefined on input line 58.\\\", \\\"Citation `fast_detectgpt' on page 4 undefined on input\\\", \\\"Citation `ld_score' on page 4 undefined on input line 5\\\", \\\"Citation `binoculars' on page 4 undefined on input line\\\", \\\"Reference `sec:eval' on page 5 undefined on input line 7.\\\", \\\"Reference `tab:logo' on page 5 undefined on input line 7.\\\", \\\"Reference `sec:discussion' on page 5 undefined on input line 35.\\\", \\\"Citation `detectgpt' on page 5 undefined on input line\\\", \\\"Citation `binoculars' on page 5 undefined on input line\\\", \\\"Reference `fig:logo_performance' on page 5 undefined on input li\\\", \\\"File `figures/paper/fig2_logo_performance.pdf' not found on inpu\\\"]}, \\\"pages\\\": null, \\\"page_status\\\": \\\"unknown\\\", \\\"max_pages\\\": 8, \\\"min_pages\\\": 6, \\\"critical_warnings\\\": [\\\"Citation `mapping_llm_science' on page 1 undefined on i\\\", \\\"Citation `monitoring_ai_review' on page 1 undefined on\\\", \\\"Citation `fast_detectgpt' on page 1 undefined on input\\\", \\\"Citation `binoculars' on page 1 undefined on input line\\\", \\\"Citation `ld_score' on page 1 undefined on input line 8\\\", \\\"Citation `detectgpt' on page 1 undefined on input line\\\", \\\"Reference `sec:baselines' on page 1 undefined on input line 16.\\\", \\\"Citation `broken_telephone' on page 1 undefined on inpu\\\", \\\"Citation `markovian_chains' on page 1 undefined on inpu\\\", \\\"Citation `ood_baseline' on page 1 undefined on input li\\\", \\\"Reference `sec:related' on page 2 undefined on input line 39.\\\", \\\"Reference `sec:method' on page 2 undefined on input line 40.\\\", \\\"Reference `sec:results' on page 2 undefined on input line 41.\\\", \\\"Reference `sec:discussion' on page 2 undefined on input line 42.\\\", \\\"Citation `gltr' on page 2 undefined on input line 7.\\\", \\\"Citation `grover' on page 2 undefined on input line 7.\\\", \\\"Citation `release_strategies' on page 2 undefined on in\\\", \\\"Citation `detectgpt' on page 2 undefined on input line\\\", \\\"Citation `fast_detectgpt' on page 2 undefined on input\\\", \\\"Citation `binoculars' on page 2 undefined on input line\\\", \\\"Citation `dna_gpt' on page 2 undefined on input line 7.\\\", \\\"Citation `feat_aug_transformer' on page 2 undefined on\\\", \\\"Citation `reliable_detection' on page 2 undefined on in\\\", \\\"Citation `ld_score' on page 2 undefined on input line 7\\\", \\\"Citation `intrinsic_dimension' on page 2 undefined on i\\\", \\\"Citation `diveye' on page 2 undefined on input line 8.\\\", \\\"Citation `generator_barrier' on page 2 undefined on inp\\\", \\\"Citation `jawahar_survey' on page 2 undefined on input\\\", \\\"Reference `sec:baselines' on page 2 undefined on input line 11.\\\", \\\"Citation `paraphrase_evades' on page 2 undefined on inp\\\", \\\"Citation `detection_possibilities' on page 2 undefined\\\", \\\"Citation `ood_baseline' on page 2 undefined on input li\\\", \\\"Citation `self_consuming_mad' on page 2 undefined on in\\\", \\\"Citation `curse_of_recursion' on page 2 undefined on in\\\", \\\"Citation `model_collapse_avoidable' on page 2 undefined\\\", \\\"Citation `strong_model_collapse' on page 2 undefined on\\\", \\\"Citation `broken_telephone' on page 2 undefined on inpu\\\", \\\"Citation `markovian_chains' on page 2 undefined on inpu\\\", \\\"Citation `curious_decline' on page 3 undefined on input\\\", \\\"Citation `writing_diversity' on page 3 undefined on inp\\\", \\\"Citation `stamatatos_survey' on page 3 undefined on inp\\\", \\\"Citation `koppel_authorship' on page 3 undefined on inp\\\", \\\"Citation `uchendu_attribution' on page 3 undefined on i\\\", \\\"Citation `nucleus_sampling' on page 3 undefined on inpu\\\", \\\"Citation `dsir' on page 3 undefined on input line 44.\\\", \\\"Citation `qurating' on page 3 undefined on input line 4\\\", \\\"Citation `ccnet' on page 3 undefined on input line 44.\\\", \\\"Citation `watermark_llm' on page 3 undefined on input l\\\", \\\"Citation `synthid_text' on page 3 undefined on input li\\\", \\\"Citation `aaronson_watermark' on page 3 undefined on in\\\", \\\"Citation `chainwash' on page 3 undefined on input line\\\", \\\"Citation `min_k_percent' on page 3 undefined on input l\\\", \\\"Citation `detectgpt' on page 3 undefined on input line\\\", \\\"Citation `fast_detectgpt' on page 3 undefined on input\\\", \\\"Citation `binoculars' on page 3 undefined on input line\\\", \\\"Citation `uchendu_attribution' on page 3 undefined on i\\\", \\\"Citation `curse_of_recursion' on page 3 undefined on in\\\", \\\"Citation `self_consuming_mad' on page 3 undefined on in\\\", \\\"Citation `pythia' on page 3 undefined on input line 14.\\\", \\\"Citation `olmo' on page 3 undefined on input line 14.\\\", \\\"Citation `qwen3' on page 3 undefined on input line 14.\\\", \\\"Citation `nucleus_sampling' on page 3 undefined on inpu\\\", \\\"Citation `markovian_chains' on page 3 undefined on inpu\\\", \\\"Citation `detectgpt' on page 4 undefined on input line\\\", \\\"Citation `ood_baseline' on page 4 undefined on input li\\\", \\\"Citation `curious_decline' on page 4 undefined on input\\\", \\\"Citation `curious_decline' on page 4 undefined on input\\\", \\\"Citation `writing_diversity' on page 4 undefined on inp\\\", \\\"Citation `xgboost' on page 4 undefined on input line 52\\\", \\\"Citation `gltr' on page 4 undefined on input line 58.\\\", \\\"Citation `fast_detectgpt' on page 4 undefined on input\\\", \\\"Citation `ld_score' on page 4 undefined on input line 5\\\", \\\"Citation `binoculars' on page 4 undefined on input line\\\", \\\"Reference `sec:eval' on page 5 undefined on input line 7.\\\", \\\"Reference `tab:logo' on page 5 undefined on input line 7.\\\", \\\"Reference `sec:discussion' on page 5 undefined on input line 35.\\\", \\\"Citation `detectgpt' on page 5 undefined on input line\\\", \\\"Citation `binoculars' on page 5 undefined on input line\\\", \\\"Reference `fig:logo_performance' on page 5 undefined on input li\\\"], \\\"minor_warnings\\\": [\\\"Line number reference failed, re-run to get it right.\\\", \\\"File `figures/paper/fig2_logo_performance.pdf' not found on inpu\\\", \\\"Underfull \\\\\\\\hbox (badness 4391) in paragraph at lines 16--17\\\", \\\"Underfull \\\\\\\\hbox (badness 2173) in paragraph at lines 24--25\\\"], \\\"issues\\\": [\\\"compile failed: Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not\\\", \\\"79 critical warning(s): Citation `mapping_llm_science' on page 1 undefined on i; Citation `monitoring_ai_review' on page 1 undefined on; Citation `fast_detectgpt' on page 1 undefined on input; (+76 more)\\\", \\\"page count unavailable (compile likely failed)\\\"], \\\"summary\\\": \\\"FAIL: compile failed: Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not; 79 critical warning(s): Citation `mapping_llm_science' on page 1 undefined on i; Citation `monitoring_ai_review' on page 1 undefined on; Citation `fast_detectgpt' on page 1 undefined on input; (+76 more); page count unavailable (compile likely failed)\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"passed\": false, \"compiled\": {\"success\": false, \"pdf_path\": null, \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"Package natbib Warning: Citation `curious_decline' on page 4 undefined on input\\n line 37.\\n\\n\\nPackage natbib Warning: Citation `curious_decline' on page 4 undefined on input\\n line 43.\\n\\n\\nPackage natbib Warning: Citation `writing_diversity' on page 4 undefined on inp\\nut line 43.\\n\\n\\nPackage natbib Warning: Citation `xgboost' on page 4 undefined on input line 52\\n.\\n\\n\\nPackage natbib Warning: Citation `gltr' on page 4 undefined on input line 58.\\n\\n\\nPackage natbib Warning: Citation `fast_detectgpt' on page 4 undefined on input \\nline 58.\\n\\n\\nPackage natbib Warning: Citation `ld_score' on page 4 undefined on input line 5\\n8.\\n\\n\\nPackage natbib Warning: Citation `binoculars' on page 4 undefined on input line\\n 58.\\n\\n) (./results.tex [4]\\n\\nLaTeX Warning: Reference `sec:eval' on page 5 undefined on input line 7.\\n\\n\\nLaTeX Warning: Reference `tab:logo' on page 5 undefined on input line 7.\\n\\n\\nLaTeX Warning: Reference `sec:discussion' on page 5 undefined on input line 35.\\n\\n\\n\\nPackage natbib Warning: Citation `detectgpt' on page 5 undefined on input line \\n37.\\n\\n\\nPackage natbib Warning: Citation `binoculars' on page 5 undefined on input line\\n 37.\\n\\n\\nLaTeX Warning: Reference `fig:logo_performance' on page 5 undefined on input li\\nne 39.\\n\\n\\nLaTeX Warning: File `figures/paper/fig2_logo_performance.pdf' not found on inpu\\nt line 43.\\n\\n\\n! Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not \\nfound: using draft setting.\\n\\nSee the pdftex.def package documentation for explanation.\\nType  H &lt;return>  for immediate help.\\n ...                                              \\n                                                  \\nl.43 ...]{figures/paper/fig2_logo_performance.pdf}\\n                                                  \\nTry typing  &lt;return>  to proceed.\\nIf that doesn't work, type  X &lt;return>  to quit.\\n\\n \\nHere is how much of TeX's memory you used:\\n 15785 strings out of 469438\\n 248190 string characters out of 5468411\\n 718985 words of memory out of 5000000\\n 43925 multiletter control sequences out of 15000+600000\\n 680903 words of font info for 285 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,10n,93p,1001b,476s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n!  ==> Fatal error occurred, no output PDF file produced!\", \"error\": \"Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not\", \"pages\": null, \"warnings\": [\"Line number reference failed, re-run to get it right.\", \"Citation `mapping_llm_science' on page 1 undefined on i\", \"Citation `monitoring_ai_review' on page 1 undefined on\", \"Citation `fast_detectgpt' on page 1 undefined on input\", \"Citation `binoculars' on page 1 undefined on input line\", \"Citation `ld_score' on page 1 undefined on input line 8\", \"Citation `detectgpt' on page 1 undefined on input line\", \"Reference `sec:baselines' on page 1 undefined on input line 16.\", \"Citation `broken_telephone' on page 1 undefined on inpu\", \"Citation `markovian_chains' on page 1 undefined on inpu\", \"Citation `ood_baseline' on page 1 undefined on input li\", \"Reference `sec:related' on page 2 undefined on input line 39.\", \"Reference `sec:method' on page 2 undefined on input line 40.\", \"Reference `sec:results' on page 2 undefined on input line 41.\", \"Reference `sec:discussion' on page 2 undefined on input line 42.\", \"Citation `gltr' on page 2 undefined on input line 7.\", \"Citation `grover' on page 2 undefined on input line 7.\", \"Citation `release_strategies' on page 2 undefined on in\", \"Citation `detectgpt' on page 2 undefined on input line\", \"Citation `fast_detectgpt' on page 2 undefined on input\", \"Citation `binoculars' on page 2 undefined on input line\", \"Citation `dna_gpt' on page 2 undefined on input line 7.\", \"Citation `feat_aug_transformer' on page 2 undefined on\", \"Citation `reliable_detection' on page 2 undefined on in\", \"Citation `ld_score' on page 2 undefined on input line 7\", \"Citation `intrinsic_dimension' on page 2 undefined on i\", \"Citation `diveye' on page 2 undefined on input line 8.\", \"Citation `generator_barrier' on page 2 undefined on inp\", \"Citation `jawahar_survey' on page 2 undefined on input\", \"Reference `sec:baselines' on page 2 undefined on input line 11.\", \"Citation `paraphrase_evades' on page 2 undefined on inp\", \"Citation `detection_possibilities' on page 2 undefined\", \"Citation `ood_baseline' on page 2 undefined on input li\", \"Citation `self_consuming_mad' on page 2 undefined on in\", \"Citation `curse_of_recursion' on page 2 undefined on in\", \"Citation `model_collapse_avoidable' on page 2 undefined\", \"Citation `strong_model_collapse' on page 2 undefined on\", \"Citation `broken_telephone' on page 2 undefined on inpu\", \"Citation `markovian_chains' on page 2 undefined on inpu\", \"Citation `curious_decline' on page 3 undefined on input\", \"Citation `writing_diversity' on page 3 undefined on inp\", \"Citation `stamatatos_survey' on page 3 undefined on inp\", \"Citation `koppel_authorship' on page 3 undefined on inp\", \"Citation `uchendu_attribution' on page 3 undefined on i\", \"Citation `nucleus_sampling' on page 3 undefined on inpu\", \"Citation `dsir' on page 3 undefined on input line 44.\", \"Citation `qurating' on page 3 undefined on input line 4\", \"Citation `ccnet' on page 3 undefined on input line 44.\", \"Citation `watermark_llm' on page 3 undefined on input l\", \"Citation `synthid_text' on page 3 undefined on input li\", \"Citation `aaronson_watermark' on page 3 undefined on in\", \"Citation `chainwash' on page 3 undefined on input line\", \"Citation `min_k_percent' on page 3 undefined on input l\", \"Citation `detectgpt' on page 3 undefined on input line\", \"Citation `fast_detectgpt' on page 3 undefined on input\", \"Citation `binoculars' on page 3 undefined on input line\", \"Citation `uchendu_attribution' on page 3 undefined on i\", \"Citation `curse_of_recursion' on page 3 undefined on in\", \"Citation `self_consuming_mad' on page 3 undefined on in\", \"Citation `pythia' on page 3 undefined on input line 14.\", \"Citation `olmo' on page 3 undefined on input line 14.\", \"Citation `qwen3' on page 3 undefined on input line 14.\", \"Citation `nucleus_sampling' on page 3 undefined on inpu\", \"Citation `markovian_chains' on page 3 undefined on inpu\", \"Citation `detectgpt' on page 4 undefined on input line\", \"Citation `ood_baseline' on page 4 undefined on input li\", \"Citation `curious_decline' on page 4 undefined on input\", \"Citation `curious_decline' on page 4 undefined on input\", \"Citation `writing_diversity' on page 4 undefined on inp\", \"Citation `xgboost' on page 4 undefined on input line 52\", \"Citation `gltr' on page 4 undefined on input line 58.\", \"Citation `fast_detectgpt' on page 4 undefined on input\", \"Citation `ld_score' on page 4 undefined on input line 5\", \"Citation `binoculars' on page 4 undefined on input line\", \"Reference `sec:eval' on page 5 undefined on input line 7.\", \"Reference `tab:logo' on page 5 undefined on input line 7.\", \"Reference `sec:discussion' on page 5 undefined on input line 35.\", \"Citation `detectgpt' on page 5 undefined on input line\", \"Citation `binoculars' on page 5 undefined on input line\", \"Reference `fig:logo_performance' on page 5 undefined on input li\", \"File `figures/paper/fig2_logo_performance.pdf' not found on inpu\"]}, \"pages\": null, \"page_status\": \"unknown\", \"max_pages\": 8, \"min_pages\": 6, \"critical_warnings\": [\"Citation `mapping_llm_science' on page 1 undefined on i\", \"Citation `monitoring_ai_review' on page 1 undefined on\", \"Citation `fast_detectgpt' on page 1 undefined on input\", \"Citation `binoculars' on page 1 undefined on input line\", \"Citation `ld_score' on page 1 undefined on input line 8\", \"Citation `detectgpt' on page 1 undefined on input line\", \"Reference `sec:baselines' on page 1 undefined on input line 16.\", \"Citation `broken_telephone' on page 1 undefined on inpu\", \"Citation `markovian_chains' on page 1 undefined on inpu\", \"Citation `ood_baseline' on page 1 undefined on input li\", \"Reference `sec:related' on page 2 undefined on input line 39.\", \"Reference `sec:method' on page 2 undefined on input line 40.\", \"Reference `sec:results' on page 2 undefined on input line 41.\", \"Reference `sec:discussion' on page 2 undefined on input line 42.\", \"Citation `gltr' on page 2 undefined on input line 7.\", \"Citation `grover' on page 2 undefined on input line 7.\", \"Citation `release_strategies' on page 2 undefined on in\", \"Citation `detectgpt' on page 2 undefined on input line\", \"Citation `fast_detectgpt' on page 2 undefined on input\", \"Citation `binoculars' on page 2 undefined on input line\", \"Citation `dna_gpt' on page 2 undefined on input line 7.\", \"Citation `feat_aug_transformer' on page 2 undefined on\", \"Citation `reliable_detection' on page 2 undefined on in\", \"Citation `ld_score' on page 2 undefined on input line 7\", \"Citation `intrinsic_dimension' on page 2 undefined on i\", \"Citation `diveye' on page 2 undefined on input line 8.\", \"Citation `generator_barrier' on page 2 undefined on inp\", \"Citation `jawahar_survey' on page 2 undefined on input\", \"Reference `sec:baselines' on page 2 undefined on input line 11.\", \"Citation `paraphrase_evades' on page 2 undefined on inp\", \"Citation `detection_possibilities' on page 2 undefined\", \"Citation `ood_baseline' on page 2 undefined on input li\", \"Citation `self_consuming_mad' on page 2 undefined on in\", \"Citation `curse_of_recursion' on page 2 undefined on in\", \"Citation `model_collapse_avoidable' on page 2 undefined\", \"Citation `strong_model_collapse' on page 2 undefined on\", \"Citation `broken_telephone' on page 2 undefined on inpu\", \"Citation `markovian_chains' on page 2 undefined on inpu\", \"Citation `curious_decline' on page 3 undefined on input\", \"Citation `writing_diversity' on page 3 undefined on inp\", \"Citation `stamatatos_survey' on page 3 undefined on inp\", \"Citation `koppel_authorship' on page 3 undefined on inp\", \"Citation `uchendu_attribution' on page 3 undefined on i\", \"Citation `nucleus_sampling' on page 3 undefined on inpu\", \"Citation `dsir' on page 3 undefined on input line 44.\", \"Citation `qurating' on page 3 undefined on input line 4\", \"Citation `ccnet' on page 3 undefined on input line 44.\", \"Citation `watermark_llm' on page 3 undefined on input l\", \"Citation `synthid_text' on page 3 undefined on input li\", \"Citation `aaronson_watermark' on page 3 undefined on in\", \"Citation `chainwash' on page 3 undefined on input line\", \"Citation `min_k_percent' on page 3 undefined on input l\", \"Citation `detectgpt' on page 3 undefined on input line\", \"Citation `fast_detectgpt' on page 3 undefined on input\", \"Citation `binoculars' on page 3 undefined on input line\", \"Citation `uchendu_attribution' on page 3 undefined on i\", \"Citation `curse_of_recursion' on page 3 undefined on in\", \"Citation `self_consuming_mad' on page 3 undefined on in\", \"Citation `pythia' on page 3 undefined on input line 14.\", \"Citation `olmo' on page 3 undefined on input line 14.\", \"Citation `qwen3' on page 3 undefined on input line 14.\", \"Citation `nucleus_sampling' on page 3 undefined on inpu\", \"Citation `markovian_chains' on page 3 undefined on inpu\", \"Citation `detectgpt' on page 4 undefined on input line\", \"Citation `ood_baseline' on page 4 undefined on input li\", \"Citation `curious_decline' on page 4 undefined on input\", \"Citation `curious_decline' on page 4 undefined on input\", \"Citation `writing_diversity' on page 4 undefined on inp\", \"Citation `xgboost' on page 4 undefined on input line 52\", \"Citation `gltr' on page 4 undefined on input line 58.\", \"Citation `fast_detectgpt' on page 4 undefined on input\", \"Citation `ld_score' on page 4 undefined on input line 5\", \"Citation `binoculars' on page 4 undefined on input line\", \"Reference `sec:eval' on page 5 undefined on input line 7.\", \"Reference `tab:logo' on page 5 undefined on input line 7.\", \"Reference `sec:discussion' on page 5 undefined on input line 35.\", \"Citation `detectgpt' on page 5 undefined on input line\", \"Citation `binoculars' on page 5 undefined on input line\", \"Reference `fig:logo_performance' on page 5 undefined on input li\"], \"minor_warnings\": [\"Line number reference failed, re-run to get it right.\", \"File `figures/paper/fig2_logo_performance.pdf' not found on inpu\", \"Underfull \\\\hbox (badness 4391) in paragraph at lines 16--17\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 24--25\"], \"issues\": [\"compile failed: Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not\", \"79 critical warning(s): Citation `mapping_llm_science' on page 1 undefined on i; Citation `monitoring_ai_review' on page 1 undefined on; Citation `fast_detectgpt' on page 1 undefined on input; (+76 more)\", \"page count unavailable (compile likely failed)\"], \"summary\": \"FAIL: compile failed: Package pdftex.def Error: File `figures/paper/fig2_logo_performance.pdf' not; 79 critical warning(s): Citation `mapping_llm_science' on page 1 undefined on i; Citation `monitoring_ai_review' on page 1 undefined on; Citation `fast_detectgpt' on page 1 undefined on input; (+76 more); page count unavailable (compile likely failed)\"}"
    }
  },
  "sourceToolAssistantUUID": "ac053bf6-15cd-4f6c-a05b-5d9685c6f151",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

</details>

---


### Runtime record

_source line 413_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director 将结果发给 Director。",
  "leafUuid": "5efbc811-6d43-4489-9413-56556d914baa",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e"
}
```

---


### Runtime record

_source line 414_

```json
{
  "type": "ai-title",
  "aiTitle": "System message notification handling",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e"
}
```

---


### Assistant

_source line 415 · 2026-05-15T05:03:18.409Z_

<details><summary>Logged reasoning block</summary>

```text
The symlink didn't work because `paper_compile_and_check` may not follow symlinks, or it's doing something weird with the build. Let me check if the symlink was created correctly and if the file is accessible from the paper directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5efbc811-6d43-4489-9413-56556d914baa",
  "isSidechain": false,
  "requestId": "req_011Cb3mZxq54HvVnN8fyLMLM",
  "type": "assistant",
  "uuid": "037031d1-3d63-4ec2-872a-e42e4bd8c28a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119jt1gkPK6zkiAvFA4fUv6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4509,
      "cache_read_input_tokens": 61354,
      "output_tokens": 222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4509,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 222,
          "cache_read_input_tokens": 61354,
          "cache_creation_input_tokens": 4509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4509
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-15T05:03:20.952Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RNA4fB4xh9W7ZTokAAVrav`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/figures && ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/figures/paper/",
  "description": "Verify symlink and figure files are accessible"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "037031d1-3d63-4ec2-872a-e42e4bd8c28a",
  "isSidechain": false,
  "requestId": "req_011Cb3mZxq54HvVnN8fyLMLM",
  "type": "assistant",
  "uuid": "63d7937b-b5f8-4b69-a222-3c87bed12e65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119jt1gkPK6zkiAvFA4fUv6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4509,
      "cache_read_input_tokens": 61354,
      "output_tokens": 222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4509,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 222,
          "cache_read_input_tokens": 61354,
          "cache_creation_input_tokens": 4509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4509
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-15T05:03:21.012Z_

<details><summary>↩ Tool result · reported error · `toolu_01RNA4fB4xh9W7ZTokAAVrav`</summary>

```text
Exit code 2
total 12
drwxr-xr-x 2 ubuntu ubuntu 4096 May 15 05:03 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 15 05:03 ..
lrwxrwxrwx 1 ubuntu ubuntu   86 May 15 05:03 figures -> /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures
ls: cannot access '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/figures/paper/': No such file or directory
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63d7937b-b5f8-4b69-a222-3c87bed12e65",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "c390e86c-9580-4d7a-93b6-41a2f413d8bb",
  "toolUseResult": "Error: Exit code 2\ntotal 12\ndrwxr-xr-x 2 ubuntu ubuntu 4096 May 15 05:03 .\ndrwxr-xr-x 3 ubuntu ubuntu 4096 May 15 05:03 ..\nlrwxrwxrwx 1 ubuntu ubuntu   86 May 15 05:03 figures -> /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures\nls: cannot access '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/figures/paper/': No such file or directory",
  "sourceToolAssistantUUID": "63d7937b-b5f8-4b69-a222-3c87bed12e65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

</details>

---


### Assistant

_source line 418 · 2026-05-15T05:03:26.124Z_

<details><summary>Logged reasoning block</summary>

```text
I see the problem. There's a directory `docs/paper/figures/` and inside it a symlink `figures -> /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures`. So the path would be `docs/paper/figures/figures/paper/` which is wrong. Let me fix this.

Actually wait, looking at the original ln command: `ln -sf .../figures .../docs/paper/figures`. Since `docs/paper/figures` is a directory, the symlink was created INSIDE the directory at `docs/paper/figures/figures`. Let me fix this.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c390e86c-9580-4d7a-93b6-41a2f413d8bb",
  "isSidechain": false,
  "requestId": "req_011Cb3maXhkQJN2Rz48trtG5",
  "type": "assistant",
  "uuid": "5d164b68-4967-4c39-b521-32c2281cf5a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Hcf6vvESCPsRtEHyCCEic",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 413,
      "cache_read_input_tokens": 65863,
      "output_tokens": 421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 421,
          "cache_read_input_tokens": 65863,
          "cache_creation_input_tokens": 413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 413
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 419 · 2026-05-15T05:03:28.441Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WW9Z55dLR5KMeWpCshiHoa`</summary>

```json
{
  "command": "rm /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/figures/figures && rmdir /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/figures && ln -sf /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/figures && ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/figures/paper/",
  "description": "Fix symlink: remove dir and create proper symlink"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d164b68-4967-4c39-b521-32c2281cf5a3",
  "isSidechain": false,
  "requestId": "req_011Cb3maXhkQJN2Rz48trtG5",
  "type": "assistant",
  "uuid": "dc4ceaa2-6bdd-4735-8e2b-e9ae9a19944f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Hcf6vvESCPsRtEHyCCEic",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 413,
      "cache_read_input_tokens": 65863,
      "output_tokens": 421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 421,
          "cache_read_input_tokens": 65863,
          "cache_creation_input_tokens": 413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 413
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 420 · 2026-05-15T05:03:28.523Z_

<details><summary>↩ Tool result · `toolu_01WW9Z55dLR5KMeWpCshiHoa`</summary>

```text
total 768
drwxr-xr-x 2 ubuntu ubuntu   4096 May 15 04:39 .
drwxr-xr-x 3 ubuntu ubuntu   4096 May 15 03:57 ..
-rw-r--r-- 1 ubuntu ubuntu  38851 May 15 04:00 fig1_differential_response.pdf
-rw-r--r-- 1 ubuntu ubuntu 370549 May 15 04:56 fig1_differential_response.png
-rw-r--r-- 1 ubuntu ubuntu  14463 May 15 04:19 fig2_logo_performance.pdf
-rw-r--r-- 1 ubuntu ubuntu  73560 May 15 04:56 fig2_logo_performance.png
-rw-r--r-- 1 ubuntu ubuntu  22835 May 15 04:36 fig3_baseline_comparison.pdf
-rw-r--r-- 1 ubuntu ubuntu  74320 May 15 04:58 fig3_baseline_comparison.png
-rw-r--r-- 1 ubuntu ubuntu   2609 May 15 04:36 fig3_forest_plot.py
-rw-r--r-- 1 ubuntu ubuntu  26224 May 15 04:39 fig4_downstream_negative.pdf
-rw-r--r-- 1 ubuntu ubuntu 133968 May 15 04:39 fig4_downstream_negative.png
-rw-r--r-- 1 ubuntu ubuntu   3026 May 15 04:39 fig4_downstream_negative.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc4ceaa2-6bdd-4735-8e2b-e9ae9a19944f",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "17cdbd9a-d0cf-4863-b70e-fccef494d480",
  "toolUseResult": {
    "stdout": "total 768\ndrwxr-xr-x 2 ubuntu ubuntu   4096 May 15 04:39 .\ndrwxr-xr-x 3 ubuntu ubuntu   4096 May 15 03:57 ..\n-rw-r--r-- 1 ubuntu ubuntu  38851 May 15 04:00 fig1_differential_response.pdf\n-rw-r--r-- 1 ubuntu ubuntu 370549 May 15 04:56 fig1_differential_response.png\n-rw-r--r-- 1 ubuntu ubuntu  14463 May 15 04:19 fig2_logo_performance.pdf\n-rw-r--r-- 1 ubuntu ubuntu  73560 May 15 04:56 fig2_logo_performance.png\n-rw-r--r-- 1 ubuntu ubuntu  22835 May 15 04:36 fig3_baseline_comparison.pdf\n-rw-r--r-- 1 ubuntu ubuntu  74320 May 15 04:58 fig3_baseline_comparison.png\n-rw-r--r-- 1 ubuntu ubuntu   2609 May 15 04:36 fig3_forest_plot.py\n-rw-r--r-- 1 ubuntu ubuntu  26224 May 15 04:39 fig4_downstream_negative.pdf\n-rw-r--r-- 1 ubuntu ubuntu 133968 May 15 04:39 fig4_downstream_negative.png\n-rw-r--r-- 1 ubuntu ubuntu   3026 May 15 04:39 fig4_downstream_negative.py",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "dc4ceaa2-6bdd-4735-8e2b-e9ae9a19944f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

</details>

---


### Assistant

_source line 421 · 2026-05-15T05:03:32.238Z_

符号链接修复成功。重新编译。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17cdbd9a-d0cf-4863-b70e-fccef494d480",
  "isSidechain": false,
  "requestId": "req_011Cb3mb6DMGxVZYpV1LTeAS",
  "type": "assistant",
  "uuid": "424e987d-8053-400b-a17a-b9e5ed1462f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEWDw15c7Vyv5u2BHtBcZe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 832,
      "cache_read_input_tokens": 66276,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 832,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 66276,
          "cache_creation_input_tokens": 832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 832
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-15T05:03:32.867Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_compile_and_check · `toolu_01GpFGSgVUrtn8Mp33ewDTHq`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "max_pages": 8,
  "min_pages": 6,
  "clean": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "424e987d-8053-400b-a17a-b9e5ed1462f5",
  "isSidechain": false,
  "requestId": "req_011Cb3mb6DMGxVZYpV1LTeAS",
  "type": "assistant",
  "uuid": "79444cb6-a01e-4f5e-ac53-fd205256cf53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEWDw15c7Vyv5u2BHtBcZe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 832,
      "cache_read_input_tokens": 66276,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 832,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 66276,
          "cache_creation_input_tokens": 832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 832
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-15T05:03:33.932Z_

<details><summary>↩ Tool result · reported error · `toolu_01GpFGSgVUrtn8Mp33ewDTHq`</summary>

```text
Error executing tool paper_compile_and_check: 'utf-8' codec can't decode byte 0x9f in position 13336: invalid start byte
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79444cb6-a01e-4f5e-ac53-fd205256cf53",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "af2da8bb-ee28-43af-be24-a1c601435ccf",
  "toolUseResult": "Error: Error executing tool paper_compile_and_check: 'utf-8' codec can't decode byte 0x9f in position 13336: invalid start byte",
  "sourceToolAssistantUUID": "79444cb6-a01e-4f5e-ac53-fd205256cf53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-15T05:03:37.771Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MG7DZEFwVCzsF3C1QqgApV`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30",
  "description": "Compile LaTeX manually to check errors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af2da8bb-ee28-43af-be24-a1c601435ccf",
  "isSidechain": false,
  "requestId": "req_011Cb3mbUwarM5Sfm5HNpsv4",
  "type": "assistant",
  "uuid": "4ddaecff-431d-49b2-9309-e245fcfec4e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CiAi1ep1grWWesgBgLVDKZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 197,
      "cache_read_input_tokens": 67108,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 197,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 67108,
          "cache_creation_input_tokens": 197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 197
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-15T05:03:38.545Z_

<details><summary>↩ Tool result · `toolu_01MG7DZEFwVCzsF3C1QqgApV`</summary>

```text
[]\T1/ptm/m/n/10 (+20) Eduard Tulchin-skii, Kris-tian Kuznetsov, Laida

Underfull \hbox (badness 2556) in paragraph at lines 328--332
[]\T1/ptm/m/n/10 (+20) Rowan Zellers, Ari Holtz-man, Han-nah Rashkin,
)

Package natbib Warning: There were undefined citations.

[10] (./main.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/tim
es/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>

Output written on main.pdf (10 pages, 297569 bytes).
Transcript written on main.log.
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ddaecff-431d-49b2-9309-e245fcfec4e5",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "6b1f619b-dab9-46c9-a547-9386b5c09db7",
  "toolUseResult": {
    "stdout": "[]\\T1/ptm/m/n/10 (+20) Eduard Tulchin-skii, Kris-tian Kuznetsov, Laida\n\nUnderfull \\hbox (badness 2556) in paragraph at lines 328--332\n[]\\T1/ptm/m/n/10 (+20) Rowan Zellers, Ari Holtz-man, Han-nah Rashkin,\n)\n\nPackage natbib Warning: There were undefined citations.\n\n[10] (./main.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/tim\nes/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\n\nOutput written on main.pdf (10 pages, 297569 bytes).\nTranscript written on main.log.",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4ddaecff-431d-49b2-9309-e245fcfec4e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

</details>

---


### Assistant

_source line 426 · 2026-05-15T05:03:43.381Z_

<details><summary>Logged reasoning block</summary>

```text
Good! The paper compiled successfully - 10 pages. But for EMNLP the limit is 8 pages for main content (references don't count). Let me check how many pages the main content is vs references. Let me run bibtex and recompile to get citations right, then check page count.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b1f619b-dab9-46c9-a547-9386b5c09db7",
  "isSidechain": false,
  "requestId": "req_011Cb3mbpdGAr8TBPYFMHbhF",
  "type": "assistant",
  "uuid": "fef871de-61f5-43a9-a9b9-18cc9e45d1b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bec7M3D2DtKEzQXiVAASb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 67305,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 67305,
          "cache_creation_input_tokens": 895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 895
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 427 · 2026-05-15T05:03:44.466Z_

编译成功，10 页。需要运行 bibtex 解决引用，然后检查页数。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fef871de-61f5-43a9-a9b9-18cc9e45d1b1",
  "isSidechain": false,
  "requestId": "req_011Cb3mbpdGAr8TBPYFMHbhF",
  "type": "assistant",
  "uuid": "95bc974a-30a5-4aaf-b75f-cdb70a8e60b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bec7M3D2DtKEzQXiVAASb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 67305,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 67305,
          "cache_creation_input_tokens": 895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 895
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-15T05:03:45.914Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LKEJJUdxtPqHXcGLqLX3TT`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper && bibtex main 2>&1 | tail -10 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "description": "Run bibtex + two pdflatex passes to resolve citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95bc974a-30a5-4aaf-b75f-cdb70a8e60b8",
  "isSidechain": false,
  "requestId": "req_011Cb3mbpdGAr8TBPYFMHbhF",
  "type": "assistant",
  "uuid": "2a898f42-1ef4-4b4c-8ee5-ef8f8fe00066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bec7M3D2DtKEzQXiVAASb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 67305,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 67305,
          "cache_creation_input_tokens": 895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 895
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-15T05:03:47.444Z_

<details><summary>↩ Tool result · `toolu_01LKEJJUdxtPqHXcGLqLX3TT`</summary>

```text
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Illegal, another \bibstyle command---line 966 of file main.aux
 : \bibstyle
 :          {acl_natbib}
I'm skipping whatever remains of this command
Database file #1: references.bib
(There was 1 error message)
s/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/tim
es/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>

Output written on main.pdf (11 pages, 305506 bytes).
Transcript written on main.log.
s/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/tim
es/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>

Output written on main.pdf (11 pages, 305433 bytes).
Transcript written on main.log.
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a898f42-1ef4-4b4c-8ee5-ef8f8fe00066",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "e309396e-bfb1-46c1-b75d-121165c514ee",
  "toolUseResult": {
    "stdout": "This is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nThe top-level auxiliary file: main.aux\nThe style file: acl_natbib.bst\nIllegal, another \\bibstyle command---line 966 of file main.aux\n : \\bibstyle\n :          {acl_natbib}\nI'm skipping whatever remains of this command\nDatabase file #1: references.bib\n(There was 1 error message)\ns/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/tim\nes/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\n\nOutput written on main.pdf (11 pages, 305506 bytes).\nTranscript written on main.log.\ns/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/tim\nes/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\n\nOutput written on main.pdf (11 pages, 305433 bytes).\nTranscript written on main.log.",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2a898f42-1ef4-4b4c-8ee5-ef8f8fe00066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

</details>

---


### Runtime record

_source line 430 · 2026-05-15T05:03:47.446Z_

```json
{
  "parentUuid": "e309396e-bfb1-46c1-b75d-121165c514ee",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "50f45647-bdf0-4b0c-8f87-aab3f6ed90f1",
  "timestamp": "2026-05-15T05:03:47.446Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

---


### Assistant

_source line 431 · 2026-05-15T05:03:51.987Z_

<details><summary>Logged reasoning block</summary>

```text
The bibtex error about `\bibstyle` is because there are duplicate `\bibliographystyle` commands. Let me check. Also, the paper is 11 pages now with references. EMNLP allows 8 pages of main content + unlimited references. Let me check where the references start.

Actually, let me first check the duplicate bibliographystyle issue. It's likely in the acl.sty which already includes a bibliographystyle.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50f45647-bdf0-4b0c-8f87-aab3f6ed90f1",
  "isSidechain": false,
  "requestId": "req_011Cb3mcUiioduxRKbs8JSFh",
  "type": "assistant",
  "uuid": "0a10e16d-3aa2-4cd3-977b-5344b5172765",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zskDp1czP3XumRkXRzmGe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 68200,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 803,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 68200,
          "cache_creation_input_tokens": 803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 803
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 432 · 2026-05-15T05:03:52.964Z_

11 pages编译成功。bibtex 报 duplicate `\bibstyle` 错误——可能 `acl.sty` 已内置 bibliographystyle。检查并修复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a10e16d-3aa2-4cd3-977b-5344b5172765",
  "isSidechain": false,
  "requestId": "req_011Cb3mcUiioduxRKbs8JSFh",
  "type": "assistant",
  "uuid": "741f0057-2f8d-4cc5-be69-6e672a700284",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zskDp1czP3XumRkXRzmGe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 68200,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 803,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 68200,
          "cache_creation_input_tokens": 803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 803
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 433 · 2026-05-15T05:03:54.597Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Wyk7T3AToJHtL33suM5pc9`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper && grep -c \"undefined\" main.log | head -1 && grep \"Warning.*Citation.*undefined\" main.log | wc -l",
  "description": "Count remaining undefined citation warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "741f0057-2f8d-4cc5-be69-6e672a700284",
  "isSidechain": false,
  "requestId": "req_011Cb3mcUiioduxRKbs8JSFh",
  "type": "assistant",
  "uuid": "83f290eb-a7ae-41a8-9b8a-61da722eecb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zskDp1czP3XumRkXRzmGe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 68200,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 803,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 68200,
          "cache_creation_input_tokens": 803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 803
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 434 · 2026-05-15T05:03:54.664Z_

<details><summary>↩ Tool result · `toolu_01Wyk7T3AToJHtL33suM5pc9`</summary>

```text
0
0
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83f290eb-a7ae-41a8-9b8a-61da722eecb5",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "09d1216b-6cfe-4d94-8348-784d1a15f667",
  "toolUseResult": {
    "stdout": "0\n0",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "83f290eb-a7ae-41a8-9b8a-61da722eecb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

</details>

---


### Runtime record

_source line 435_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director 将结果发给 Director。",
  "leafUuid": "09d1216b-6cfe-4d94-8348-784d1a15f667",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e"
}
```

---


### Runtime record

_source line 436_

```json
{
  "type": "ai-title",
  "aiTitle": "System message notification handling",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e"
}
```

---


### Assistant

_source line 437 · 2026-05-15T05:04:00.770Z_

引用全部解决了。检查页数分布——EMNLP 限制 8 页正文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09d1216b-6cfe-4d94-8348-784d1a15f667",
  "isSidechain": false,
  "requestId": "req_011Cb3md2HGSqp9p6mWq1ufR",
  "type": "assistant",
  "uuid": "ebf44d10-f933-4b14-8655-6ee3a0383261",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LG5skYVTTP2q96YnrEzeKd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 370,
      "cache_read_input_tokens": 69003,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 370,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 69003,
          "cache_creation_input_tokens": 370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 370
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-15T05:04:06.509Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PionYPbGnzkgyReGjNvCLx`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper && grep -n \"\\\\\\\\bibliography{\" main.log 2>/dev/null; grep \"Page [0-9]\" main.log | tail -5; grep \"\\\\\\\\bibdata\" main.aux | head -3; pdftotext main.pdf - 2>/dev/null | grep -n \"References\" | head -3",
  "description": "Check which page references start on"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebf44d10-f933-4b14-8655-6ee3a0383261",
  "isSidechain": false,
  "requestId": "req_011Cb3md2HGSqp9p6mWq1ufR",
  "type": "assistant",
  "uuid": "02a215ed-5bcd-4797-8213-ef209a3199ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LG5skYVTTP2q96YnrEzeKd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 370,
      "cache_read_input_tokens": 69003,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 370,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 69003,
          "cache_creation_input_tokens": 370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 370
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-15T05:04:06.666Z_

<details><summary>↩ Tool result · `toolu_01PionYPbGnzkgyReGjNvCLx`</summary>

```text
\bibdata{references}
1688:References
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02a215ed-5bcd-4797-8213-ef209a3199ce",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "dd03dbe1-afc2-4b11-928b-f3de8d7470d7",
  "toolUseResult": {
    "stdout": "\\bibdata{references}\n1688:References",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "02a215ed-5bcd-4797-8213-ef209a3199ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-15T05:04:10.998Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NdGWkyu7wzVUsZe1mhXxYM`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper && pdftotext main.pdf - 2>/dev/null | grep -n \"^References$\" && pdftotext main.pdf - 2>/dev/null | grep -c \"^$\" | head -1; python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', 'main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\"",
  "description": "Get PDF info for page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd03dbe1-afc2-4b11-928b-f3de8d7470d7",
  "isSidechain": false,
  "requestId": "req_011Cb3mdtw2ebAoCH6cACMzK",
  "type": "assistant",
  "uuid": "fecf7b54-ffe7-4d4d-b484-7f9c616f5d5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DVE2robBoQxciifo3bBmsF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 285,
      "cache_read_input_tokens": 69373,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 69373,
          "cache_creation_input_tokens": 285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 285
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-15T05:04:11.258Z_

<details><summary>↩ Tool result · `toolu_01NdGWkyu7wzVUsZe1mhXxYM`</summary>

```text
1688:References
366
Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Fri May 15 05:03:46 2026 UTC
ModDate:         Fri May 15 05:03:46 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           11
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       305433 bytes
Optimized:       no
PDF version:     1.7
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fecf7b54-ffe7-4d4d-b484-7f9c616f5d5c",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "b20f6c8a-6c61-48dd-ad39-a1a8a2cecd7c",
  "toolUseResult": {
    "stdout": "1688:References\n366\nTitle:           \nSubject:         \nKeywords:        \nAuthor:          \nCreator:         LaTeX with hyperref\nProducer:        pdfTeX-1.40.28\nCreationDate:    Fri May 15 05:03:46 2026 UTC\nModDate:         Fri May 15 05:03:46 2026 UTC\nCustom Metadata: yes\nMetadata Stream: no\nTagged:          no\nUserProperties:  no\nSuspects:        no\nForm:            none\nJavaScript:      no\nPages:           11\nEncrypted:       no\nPage size:       595.276 x 841.89 pts (A4)\nPage rot:        0\nFile size:       305433 bytes\nOptimized:       no\nPDF version:     1.7",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fecf7b54-ffe7-4d4d-b484-7f9c616f5d5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

</details>

---


### Assistant

_source line 442 · 2026-05-15T05:04:15.467Z_

<details><summary>Logged reasoning block</summary>

```text
11 pages total. I need to figure out how many pages are main content vs references. Let me use pdf_to_images to check, or simply look at the LaTeX output to find where the bibliography starts. Let me check the log for page numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b20f6c8a-6c61-48dd-ad39-a1a8a2cecd7c",
  "isSidechain": false,
  "requestId": "req_011Cb3meEW1DrSngS4gPUzGq",
  "type": "assistant",
  "uuid": "7e299c2e-8ed3-44be-870d-086971baf5cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TytwahDDC1JfqcMQ4DvpqV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 69658,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 200,
          "cache_read_input_tokens": 69658,
          "cache_creation_input_tokens": 451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 451
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 443 · 2026-05-15T05:04:16.391Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TKLQoEHEgaTBDMrUeLwajc`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper && grep \"\\\\[.*\\\\]\" main.log | grep -E \"^\\[\" | head -20",
  "description": "Find page numbers from LaTeX log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e299c2e-8ed3-44be-870d-086971baf5cb",
  "isSidechain": false,
  "requestId": "req_011Cb3meEW1DrSngS4gPUzGq",
  "type": "assistant",
  "uuid": "d7ad1278-6287-4bd4-b71b-33545a740d9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TytwahDDC1JfqcMQ4DvpqV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 69658,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 200,
          "cache_read_input_tokens": 69658,
          "cache_creation_input_tokens": 451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 451
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 444 · 2026-05-15T05:04:16.453Z_

<details><summary>↩ Tool result · `toolu_01TKLQoEHEgaTBDMrUeLwajc`</summary>

```text
grep: main.log: binary file matches
[Loading MPS to PDF converter (version 2006.09.02).]
[2]) (./method.tex
[], [][]2023[][]) (Pythia-2.8B,
[4]) (./results.tex
[5 <./figures/paper/fig2_logo_performance.pdf>]
[6 <./figures/paper/fig1_differential_response.pdf>]
[]\T1/ptm/b/n/10.95 (+20) Depth-aware cu-ra-tion does not im-prove
[]\T1/ptm/m/n/10 (+20) Abhimanyu Hans, Avi Schwarzschild, Va-leriia
[]\T1/ptm/m/n/10 (+20) Ganesh Jawa-har, Muham-mad Abdul-Mageed, and
[]\T1/ptm/m/n/10 (+20) John Kirchen-bauer, Jonas Geip-ing, Yuxin Wen,
[9]
[]\T1/ptm/m/n/10 (+20) Eduard Tulchin-skii, Kris-tian Kuznetsov, Laida
[10]
[]\T1/ptm/m/n/10 (+20) Rowan Zellers, Ari Holtz-man, Han-nah Rashkin,
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7ad1278-6287-4bd4-b71b-33545a740d9b",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "1a9995a9-3218-400a-8b15-96d0e06d0c93",
  "toolUseResult": {
    "stdout": "grep: main.log: binary file matches\n[Loading MPS to PDF converter (version 2006.09.02).]\n[2]) (./method.tex\n[], [][]2023[][]) (Pythia-2.8B,\n[4]) (./results.tex\n[5 <./figures/paper/fig2_logo_performance.pdf>]\n[6 <./figures/paper/fig1_differential_response.pdf>]\n[]\\T1/ptm/b/n/10.95 (+20) Depth-aware cu-ra-tion does not im-prove\n[]\\T1/ptm/m/n/10 (+20) Abhimanyu Hans, Avi Schwarzschild, Va-leriia\n[]\\T1/ptm/m/n/10 (+20) Ganesh Jawa-har, Muham-mad Abdul-Mageed, and\n[]\\T1/ptm/m/n/10 (+20) John Kirchen-bauer, Jonas Geip-ing, Yuxin Wen,\n[9]\n[]\\T1/ptm/m/n/10 (+20) Eduard Tulchin-skii, Kris-tian Kuznetsov, Laida\n[10]\n[]\\T1/ptm/m/n/10 (+20) Rowan Zellers, Ari Holtz-man, Han-nah Rashkin,",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d7ad1278-6287-4bd4-b71b-33545a740d9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

</details>

---


### Tool call

_source line 445 · 2026-05-15T05:04:19.626Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019pZE4uh2bvD1LGRsBVKFNi`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper && strings main.log | grep -E \"^\\[[0-9]+\\]\" | head -20",
  "description": "Extract page markers from LaTeX log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a9995a9-3218-400a-8b15-96d0e06d0c93",
  "isSidechain": false,
  "requestId": "req_011Cb3mecijfb1tcDqPxPH1r",
  "type": "assistant",
  "uuid": "7468e14a-6b4f-4019-9d63-09e4a1330f0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRRqCRCBgSQjDYmZLrCKJw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 70109,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 610,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 70109,
          "cache_creation_input_tokens": 610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 610
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 446 · 2026-05-15T05:04:19.689Z_

<details><summary>↩ Tool result · `toolu_019pZE4uh2bvD1LGRsBVKFNi`</summary>

```text
[2]) (./method.tex
[4]) (./results.tex
[10]
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7468e14a-6b4f-4019-9d63-09e4a1330f0b",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "33752b32-c3c7-4f49-b660-c01aaa69ff82",
  "toolUseResult": {
    "stdout": "[2]) (./method.tex\n[4]) (./results.tex\n[10]",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7468e14a-6b4f-4019-9d63-09e4a1330f0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

</details>

---


### Tool call

_source line 447 · 2026-05-15T05:04:23.460Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Dr8o1DxYXr11wWo7fPGHpW`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper && pdftotext -layout main.pdf - 2>/dev/null | grep -n \"References\" | head -3",
  "description": "Find References heading position in extracted text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33752b32-c3c7-4f49-b660-c01aaa69ff82",
  "isSidechain": false,
  "requestId": "req_011Cb3merbAc2TMU642nAYXY",
  "type": "assistant",
  "uuid": "b3268e39-0387-45ce-b5ce-d79979534401",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyPwS5CfE7HMyuj5BKMcfA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 211,
      "cache_read_input_tokens": 70719,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 211,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 70719,
          "cache_creation_input_tokens": 211,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 211
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 448 · 2026-05-15T05:04:23.587Z_

<details><summary>↩ Tool result · `toolu_01Dr8o1DxYXr11wWo7fPGHpW`</summary>

```text
611:673   References                                                   Mingmeng Geng, Amr Mohamed, Guokan Shang,                728
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3268e39-0387-45ce-b5ce-d79979534401",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "f64bb8d0-04cc-4468-82c2-925c06668c06",
  "toolUseResult": {
    "stdout": "611:673   References                                                   Mingmeng Geng, Amr Mohamed, Guokan Shang,                728",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b3268e39-0387-45ce-b5ce-d79979534401",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

</details>

---


### Tool call

_source line 449 · 2026-05-15T05:04:27.391Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Bdgkf8njCm7PTUdSF36evZ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f64bb8d0-04cc-4468-82c2-925c06668c06",
  "isSidechain": false,
  "requestId": "req_011Cb3mf9Gm8tkenwWA5u5W3",
  "type": "assistant",
  "uuid": "4e414b62-32fe-432f-b839-068c2f473fe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCwjJQfoEkQdBVGPMHQ5HL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 228,
      "cache_read_input_tokens": 70930,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 228,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 70930,
          "cache_creation_input_tokens": 228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 228
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 450 · 2026-05-15T05:04:27.394Z_

<details><summary>↩ Tool result · `toolu_01Bdgkf8njCm7PTUdSF36evZ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__pdf_to_images"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e414b62-32fe-432f-b839-068c2f473fe8",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "c77f769c-04cd-499d-89eb-0ee43dec0ec4",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__pdf_to_images"
    ],
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "total_deferred_tools": 50
  },
  "sourceToolAssistantUUID": "4e414b62-32fe-432f-b839-068c2f473fe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton"
}
```

</details>

---


### Tool call

_source line 451 · 2026-05-15T05:04:30.988Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01HTXzZohXvnAopk81TCSKdU`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf",
  "pages": "8,9",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c77f769c-04cd-499d-89eb-0ee43dec0ec4",
  "isSidechain": false,
  "requestId": "req_011Cb3mfRnwGxTQPXpBgmzm4",
  "type": "assistant",
  "uuid": "f06bdae5-8a60-4d3f-891d-02c178482524",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "2ca56334-649b-49b2-953b-bf45e8a6817e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "drifting-stirring-hinton",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BqQd1zQVmNZqCGKTRCadX3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 462,
      "cache_read_input_tokens": 71158,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 462,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 139,
          "cache_read_input_tokens": 71158,
          "cache_creation_input_tokens": 462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 462
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Large event (continued)

````text
### Tool result

_source line 452 · 2026-05-15T05:04:31.963Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_01HTXzZohXvnAopk81TCSKdU`&lt;/summary>

```text
Error: result (1,483,088 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-paper-agent-f6e70382/2ca56334-649b-49b2-953b-bf45e8a6817e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821471946.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-paper-agent-f6e70382/2ca56334-649b-49b2-953b-bf45e8a6817e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821471946.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-paper-agent-f6e70382/2ca56334-649b-49b2-953b-bf45e8a6817e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821471946.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f06bdae5-8a60-4d3f-891d-02c178482524",
  "isSidechain": false,
  "promptId": "a29be202-36fd-4ca1-8b13-09d07cfde2d1",
  "type": "user",
  "uuid": "59449020-6eea-42b0-bff1-27d0b1ccf53a",
  "toolUseResult": "Error: result (1,483,088 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-paper-agent-f6e70382/2ca56334-649b-49b2-953b-bf45e8a6817e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821471946.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-paper-agent-f6e70382/2ca56334-649b-49b2-953b-bf45e8a6817e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821471946.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-paper-agent-f6e70382/2ca56334-649b-49b2-953b-bf45e8a6817e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821471946.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/_pdf_images/main_p8.png\", \"base64\": \"iVBORw0KGgoAAAANSUhEUgAABNkAAAbaCAIAAAB3QTY3AAAACXBIWXMAABcSAAAXEgFnn9JSAAgNMElEQVR4nOydd3gUVRv2FwlNilQFAQWRJl0EpIiCqFRBinRBkE4oIiVSLkRAUBGkSQ0dpCkgVYGXUAJIkNAJr0TqS5EuLSDsd3/zfJzvMLM7u0k2E8r9+yNX5szZM6fPc89pLjchhBBCCCGEEOIsrsSOACGEEEIIIYSQJw5qUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUoIYQQQgghhBCnoRYlhBBCCCGEEOI01KKEEEIIIYQQQpyGWpQQQgghhBBCiNNQixJCCCGEEEIIcRpqUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUoIYQQQgghhBCnoRYlhBBCCCGEEOI01KKEEEIIIYQQQpyGWpQQQgghhBBCiNNQixJCCCGEEEIIcRpqUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUoIYQQQgghhBCnoRYlhBBCCCGEEOI01KKEEEIIIYQQQpyGWpQQQgghhBBCiNNQixJCCCGEEEIIcRpqUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUoIYQQQgghhBCnoRYlhBBCCCGEEOI01KKEEEIIIYQQQpyGWpQQQgghhBBCiNNQixJCCCGEEEIIcRpqUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUoIYQQQgghhBCnoRYlhBBCCCGEEOI01KKEEEIIIYQQQpyGWpQQQgghhBBCiNNQixJCCCGEEEIIcRpqUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUoIYQQQgghhBCnoRYlhBBCCCGEEOI01KKEEEIIIYQQQpyGWpQQQgghhBBCiNNQixJCCCGEEEIIcRpqUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUoIYQQQgghhBCnoRYlhBBCCCGEEOI01KKEEEIIIYQQQpyGWpQQQgghhBBCiNNQixJCCCGEEEIIcRpqUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUoIYQQQgghhBCnoRYlhBBCCCGEEOI01KKEEEIIIYQQQpyGWpQQQgghhBBCiNNQixJCCCGEEEIIcRpqUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUoIYQQQgghhBCnoRYlhBBCCCGEEOI01KKEEEIIIYQQQpyGWpQQQgghhBBCiNNQixJCCCGEEEIIcRpqUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUoIYQQQgghhBCnoRYlhBBCCCGEEOI01KKEEEIIIYQQQpyGWpQQQgghhBBCiNNQixJCCCGEEEIIcRpqUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUoIYQQQgghhBCnoRYlhBBCCCGEEOI01KKEEEIIIYQQQpyGWpQQQgghhBBCiNNQixJCCCGEEEIIcRpqUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUoIYQQQgghhBCnoRYlhBBCCCGEEOI01KKEEEIIIYQQQpyGWpQQQgghhBBCiNNQixJCCCGEEEIIcRpqUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUoIYQQQgghhBCnoRYlhBBCCCGEEOI01KKEEEIIIYQQQpyGWpQQQgghhBBCiNNQixJCCCGEEEIIcRpqUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUoIYQQQgghhBCnoRYlhBBCCCGEEOI01KKEEEIIIYQQQpyGWpQQQgghhBBCiNNQixJCCCGEEEIIcRpqUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUoIYQQQgghhBCnoRYlhBBCCCGEEOI01KKEEEIIIYQQQpyGWpQQQgghhBBCiNNQixJCCCGEEEIIcRpqUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUoIYQQQgghhBCnoRYlhBBCCCGEEOI01KKEEEIIIYQQQpyGWpQQQgghhBBCiNNQixJCCCGEEEIIcRpqUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUoIYQQQgghhBCnoRYlhBBCCCGEEOI01KKEEEIIIYQQQpyGWpQQQgghhBBCiNNQixJCCCGEEEIIcRpqUUIIIYQQQgghTkMtSgghhBBCCCHEaahFCSGEEEIIIYQ4DbUo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EfO86BmOFi1aYF/aKf369aOWhg0bpkuqq27duhlTmKFDhzZo0MDfDUyIkwQxfReFOG2wc+fOAgUKxPRW8PbbbwePoxsiRIgQIUKESBZCLnpqI+SiXihsgx09fP/+/bfeeusLL7ywfv36MWPGVKtWbdu2bRlQknnz5jVp0iTcHXCqIOSipzeefvpp2tfeoC4cOHCgdevWadmMECJEiBAhQoRIHUIuemqjXbt2EY/vyhB//fXXwIEDbToK1q1bN3v27GXLlmVMkIP3339/5MiR4YroKQQFKU0YBjbEKQpaNnPmzDly5GjRosXLL788adKkF1988aGHHmrUqJHtBjlEiBAhQoQIkWEIueipil9++QUKeuGFF+bOnbto0aLdunXzxmUJESJEEGzYsKFNmzbnnXcevemGG27o169feh9cDHFCsHz58vvuu+/yyy8vUKBAxYoVIaImCk6ImDh48ODo0aO3b9+e3i/at2/fpEmT7IPiy5Ytc4WkOnDgwKxZs+J5Sk+Iv//+GwFI42TTrl27XnnlFX//XknH4cOH58+fH3N7eQa8et68ecfrBSBEiBAhgiPkoiFChAgRIkSIGHjttdcikUj9+vXT7xWLFi2qW7eu/Dzbc0CKFrt27Vr+3rZtW4sWLeSm245qGxAQql69ehUsWJDb//GPf6SltPfddx8PGTp0aFoeEhzbt29v27Zt9uzZeam/X+6k4+jRo08++aS8gvv7MA8RIkSItCDkoiFChAgRIkSI/8IOFg127NgBEVWApfQDtCdv3rwuLjpkyJBmzZrJJ7agILqp4KLCSy+9lHYuunDhwnr16m3ZsiUtDzleKAZvBnNR4Z577kk7F3UJVYgzFqEkhIiJkIuGCBEiRIgQIf6Lli1bnpD33nDDDS4u6sX//M//pIWLwqjTzkVPCB5//PETxUUfeuihNHLR4cOHr169OolFCnGKIpSEEPEQctEQIUKECBEixH9XDs8555wT8uqQi/rg1OWiK1asyJo1a+jMIkQoCRmJAwcOfPHFF6jKzz77bOPGjXY0h++//55WWLRo0dKlS9evX//bb7/Zd61bt467Fi9e/Pnnn8cMY55OCLloiBAhQoQIcTpg//792k978ODBefPmTZw4ce/eva48WBizZ88eOXLkwoULbV9B06ZNy5w5c/bs2Zc5+PXXX01+r4cnbsReGT16NCzl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OGQ6HBd1cHBwcHDIZPTo0SPqhuoEsX379nffffeMM84w3pIbN27crVu3li1b5syZ8+yzz+7evbsJ2XqCQ5GcTjocPXrURFc6Hqxfv75ChQpqRDsWt8Px4IYbbpBIc+TIUahQIf7yf/bs2fnfeLC/7LLL5s2bV61aNf6vXr16Zhc5vaCoWt99911mF8TB4f/BcVEHBwcHB4fMxIoVK0Qj08xFBUVjFgzzXLdunUJnXXzxxXPmzElGedMRCxYsyJ8/f2aXIi3o0aOHHTr7ePDmm286LppcXH311bfffruJMvjwww8j3oYNG+py586dLVq0KFGiBP8vX778FOOinhMZ3bp1u//++90xDYcTB46LOjg4ODg4ZBoOHTp04403YigfPxeVhS3Ykbrkc06hZTG1j7vI6YUdO3YUK1aMQmZ2QVKNuXPnZsuWLVlc9J133nFcNLmoUKGCHQLKw0XDkW5YtmzZcCTC2anERRctWjRo0KDMLoWDQxAcF3VwcHBwcMg0PP7445988smDDz6Yflz077//Lly4sNKrVat23EVOF+zevfvKK68UYc7ssqQOS5cuLViwICV3XPSExXPPPWdf+rko6NSpU/jU4qL0qeLFi/ft2zezC+KQodi/f/+qVau+/vrr+fPnr1u37s8//zQ//fzzz0uWLJk7d+68efP4yR/o++jRoytXrtywYUNGFthxUQcHBwcHh8zBjBkzWrduzT/pykVN/gKmhknfsmXLW2+91bhxY24YPHjw4cOHlb5t27Y3LXz88cf/+9//3jwWWC36p2vXrps3bzbp3bt3J4dZs2a1bdu2fv36/fv3/+eff8wbDxw4wD2k33///f369RswYMCCBQswms0hyezZsysfTKjp06ebbPmfSnXr1q1OnTpvvPGGyfCLL75o3759vXr1nnnmmbVr19q1plQvvPBCo0aNeOShhx6aMGGCKQlCMDkPHDgwHPE7/eijjzZr1mz48OG6bdGiRcqZCsY6bYthV6BAAZX8kksuITce10979+7t1atX8+bNb7311vvuu4/K/v777/azP/7449NPPw2Dffzxx0eMGPH888//8ccfYR8XxWS0xQ71jaUASIy3t2nThjzbtWvnkQaSf/fddxE72SLG7du3K/3vv//2tOycOXPQBHP5/fffB4gaw9d+lktkS60R+5o1a+I2hIAuffTRR488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yFo/uhGyGnHPi+YmYCbeddddaQqrfeJix44dJUqUiHs+dtasWdOmTcuUt0yYMMHeQhkhQoQIESJEiBAhQo4g4qInNnI9F01JSZG31bwAHW1dtGiRJ/3gwYMdOnQIuWQdF7/99tucOXO+/vpr6G758uU3b96csZJGiBAhQoQIESJEiJBRRFz0xIbO5sFIc7ogWQXjdDQv4IMPPsifP3/hwoXvueeel19+efz48S+88MI//vGPFi1aeLZTphXyKCP07t07swocIUKECBEiRIgQIUK6EXHRExUHDhyAgpYqVerUU08tW7Zs9+7dPYEQIpyIWLZs2V133XXhhReWKFHiiiuugIiaUBYZwTfffFO3bt3y5cv369cvOqcdIULewZEjR/7973/bfphzK5gTp02bZkfrSRNOUEFt3bo16fGN7777bsyYMXbKmjVrXn31Vb9Hj7gg2wcffMAt6S+lD0j73Xffzc7TN9Tiww8//OyzzzL3sb///vsnn3zy/PPPT506NbwTjdwEv3YFIItaIcKJjoiLRogQIUKECLkT06dPj8ViNWvWzOmCZCE+/fTT5s2by1N0us3cE05Qb7/99kUXXUSZL7300kR5Xn/99dq1a8snuZ0uF99h/OF1795dIaMg6plS7L1796akpMiruYnPnKXYsWNH586dixYtyhufeeaZTHzyTz/91KBBg4ULF44cOVJeyuU+MI8gkXbFRda1QoRcgIiLRogQIUKECLkEdnBaxw1aC08bN25cTpUnewBrKl++vJ+LeqQRgONEUOELDObPnx/MRZ3UQMEetgCxbNGiBbQwzFvatGmTiVxUqF+/frZxUaFt27aZzoJuvfVWEwR76NChrVq1ymvbjuJqVwCyohUi5AJEXDRChAgRIkTIDfjtt9/at2+f06XIGSjqrM1FT0RpdOzY8cCBAyEzf/XVV0m5KDjppJPCswU/HnrooUznovfcc082c1GFd85EFvT999/ny5cP4WTWA09QpEm7Mr0VIuQORFw0QoQIESJEyA1o27Zt9erVc7oUOQM/Fz3hpDFu3DiqYEckDkbERcMj01nQe++9xwMjLhpx0eMQBw8eXLdu3aeffrp06dKNGzfaJ8N/+OGHlStXLly4cMmSJfxk7yrnrtWrV3PXokWLVq1a9dNPP2VbgSMuGiFChAgRIpzYOHr0qIJCVaxY8TMXxsj4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GMjh1Vdf9funjGDjwIEDnngQv//++y/H4tChQ5Ejzwh5HBEXjRAhQoQIESLkIezduzclJUWBf958882k+SFdTz/9tKJt3XjjjWl6F0yjf//+bdq0Wb169ZIlS0qVKnXSSSfNmzcvvWU/LqA4xjNnzszpghyn+O9//9u7d+/TTz/95ZdfttM/+uijxx57zJzCuPDCC2vUqHGuiyuvvJLMGfEtHyHCCYqIi0aIECFChAgR8hzq168fkosK48aNSwcX7dOnT82aNY07gw0bNlSqVGnGjBlpK2sG8L///S/Tn/nvf/+7RYsWntjFEYTJkyd36dLlrLPOQls8XFR4+umnFZzcaMW3337bunVrxTnPm2ccskJLI5woiLhohAgRIkSIECHP4Z577kkTF/3000/TykUPHDhQrFixdIQIzixMmzYtWr3MEaSkpCTiomPHjuWnk046yU48evRonTp1SIeUZlcZjyN07NiRzpLTpYiQM4i4aIQIESJEiBAhzyEbuOi8efO4pX///ukqYEaxfv36okWLvv322zny9jyOhx56KBEXfe211/xcFPTt25f0888/P1sKeBxBOw6i/cmZhYMHD65bt47xaunSpRs3brTPdf/www8rV65cuHDhkiVL+Om3334zP+3fv3/16tWfuuAfLrOtwBEXjRAhQoQIEXIPli1b9sorr7zzzjvfffedSTx69Ohnqdi3b5/jLtmZlN27d9tP+PXXX2fPnj18+PCZM2d6fhL27t371ltv/fvf/+beI0eO+DP8+eefixYtGj169Jw5c9K63PHzzz/zdsfdtodVNGbMmG3btumn//u///vyyy9fffXVBQsW+G/8/fffly9fzq/Tp0/3+Iwx+P777994443XX3+desXlogElTxMXpagI51//+he3dOzY0Yj6o48+ogBTp061M2Mgzp8/33EbBZmPHz/+xx9/9D/z22+/nTZt2tixYxFC0gJ89dVX5513Hm8fNGgQ7/3666+5XWVYs2aN8mzYsEEpX3zxhX0vhqxSEBeyoq2Rref5lMHj9inMXU4C/QwPBEuxJ02ahJSoCIrtyRBSmMGvwFinkLxly5Yt6Sikky4uKm2pWrVqmOcfOnRIXxkOHz78wQcf0E2gFp48wRWho33yySf8s3btWnqNkVLSu9LXPRP1LGpxyimnKCSYZyyCnb733nujRo1avHixJ2gf/Ordd9/lH4rNM9evXx9GaHkByBY5f/zxx/oL6HHaAv3NN98ohYbz/CRlsO9CB3755ZfsKXPERSNEiBAhQoTcgP379zds2PCBBx7AqrjvvvvkHOWmm25q3Ljxrl27Vq5cWbJkSRLhQo5LOD/88MPKlSuTMnLkSPMQKMTZZ589YcIELFRI1GmnnYZdYr8FHlWlShWsfHhR6dKlixcvfuWVV/KK559/XhlWrFhx6623Pvfcc4MHD77gggt4KS8KU37MoFtuueXkk0/+61//CqupU6fO3/72t1NPPZUSYvJibnJ52WWXlSpVipSuXbva91Lliy++mDdS2r59+2Ldtm7d+qeffjIZMLkeffTRq6++esaMGRi4N998M2/xcNHgkqeJi2I6P/HEE/Xq1eMWXvqEi0ceeeSSSy4hpXbt2sr2/vvv161bN1++fNddd93cuXPPP/983ksGmsCY+Co8t6ekpIwYMaJ9+/ZkaNOmDSQkoADDhw+vXr06Of/+97/36tWLaiKNxx9/nBQqrjwwjT59+pDyl7/8xdwlsTz99NPPPPNMmTJl+EkFFhngIf3795fvon//+98h7xIC9BMCGUaqO3bsqF+/fqdOnaD0KC1ku1atWoaHhBRmMDZt2kRdEBS0CmkXKFAAZQh5r420clHIQNmyZUkfMmRI8JOXL1/esmXLwoUL0zVWrVp1zjnniMsBim288gZUhM57++23FyxYEMkzGlAS7r3zzjuD78pI90zUs2A7aKAegoajqJ9//rluef3111u0aIEAe/bsWaxYMR5O65O+evXq+++/v0SJEkWKFNmwYQP/KKh4Gtsn1wKVYAykHRk0fvvtN+g9TJ5ui2KIZ37//feO25HFOfVpktGe/2lEsv3+++8iq19//XX2lDniohEiRIgQIUJuwN133419CcnU5bXXXqsNolhvWr284447DBcVoGc2Fz148CB27RVXXKFLHoXJW61aNZMf448MTz31lC4hFdwOI+UV3377LSlYNhAM439l48aNZIDQ2rQwAHAG8hcqVKhHjx7iWnoC3KZp06ZaTiEdEoJNbHznYL9iT9uLje+88w53URGzbgaRq1SpktmTRtXkF9dw0aQlT8ceXYxvMTSTsnLlSlJg7yZl/vz5pJx55pndunXTbronn3xSq6kmT79+/R577DFzCb0kg2mFRNDCr71Hd/Pm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MpDDwoULY1nw6DxO9RH7J598grQjLkBCIo6ySkgg0gULFiTKq8+cOTN+/HiltzcaLl++jOQ3bNgQ3Wzp71iDVatWqZSEsVEGBgYGBgYGcYHhogZeGDduXLly5QKBwC233KKnFy5cmMTFixfH03v/+++//v37f/HFF7ZEnMvcuXOnS5euUqVKrVq1euSRR7JkyVKmTJlatWqVKlVK3blly5ayZcsGYlC0aNEdO3aoq3PmzOnYsSM+cdhiHDt2jMdTpUr1119/RVCLuDw+bNgwCrl+/frixYuTiW0uIAkijrJKMKDSBQsWpKgvvPBCAr/66NGjTZo0SZEiBW8/fPhwAr890XHgwIH27dvTean+p59+GsWcu3XrljVrVrJ99913VWJ82ygDAwMDAwODuMNwUYMw2LNnj5OLfv75588888yZM2f0xGgtQcA5n3/++QkTJuiJ+/fvv++++yhJ8+bNL168qNJ///33Ro0akX7HHXdICi7vvffeC+E8f/78L7/88uyzz3JVZ6pg1apVlD8sHaUkMN4333wz4opE9jjFo8w///xz0Kp4tWrVbKu+SQG25o6jrOIbemlHjBiRkFxUfzVSuu22225MLiqQ/hhdLgpeeeUVGxd1tVFJEKjHnxowaEuWLIljnvPnz+/Ro0fr1q379u2rT8NFhmnTpo2LwZYtW+KY2w2CeBLapUuXaNmmTZvGvVlji3/++efPq/GvBVsiw6565O+//9YvYf0SuMyqGIsXL7aNoTTK9OnTE6U8EQMBrl27dtGiRfH6FsS1cOHC+OjpaO/69etnzJgRq9g0D6yzEJWsDBIXhosahIeTi7qiZcuW2Jq4v65r1644rHrKb7/9VqhQIYrRpUsX10eaNWuGiy//M1QfP35cXcKw5s2bl2dx8vRH3n777bZt28a9tPGBFi1aUGBbaHFSQ7SaOwHw9ddf452rn999912CcdFdu3bBB/SUu+6660bmovS7+OCiH374oY2LXit47bXXAldjzpw5EeeGXt1zzz16bsmSJRs2bFhcSjhlypQ0adJIbm+99VZcsrpxEE9Ce//99yVPzIjtEqPegQMHovUiJ3788ce6devK21OkSEFHPnjw4LFjx3r16nXzzTdL+sMPPzx8+HD1CMRD5p7Spk2Lnid8yAwC6dChQ/r06SlD//79g5Y/gJXIkycPKY8++mgClycu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cPsHe/fuXb16NX/8+eef8+fP58HffvtNfjp//jytMHbs2G+//db9Onzi5cuXMybxul9//VWl79u3b91FrF+/XhLPnj2rEv/55x9J/OWXX+TVCocPH168eLFln6Qyd+7c+Pj4oK2Pxzxp0qQpU6Z89913iRIRQ/hHH300efLko0ePBuWiVGrBggWjR4+mYMjN8biHJNHqpUuXIgdq9/XXX2O716xZ454c8G4LHqFg586do4RLliwJW52wcvCoDn651J30lStX0sp0vUTl8Ndff6Ewlh2zpEZ6GbZt20bbIQR6ugozIRmJpufPn180QanomTNn3HvJkAOPjxs3btasWWipu2yo5TfffGPZzYrEZs+ezSNe8rIsHBp8I8pAY1EApO1dU1R0nQbad8+ePepSquaRZ1jomSMNJKmn/PHHH5bdF+Typ59+si7losht2bJlQXtoUJFadtNMtOE4tUtxUZR248aNNCg5+6xFUK2mAHpdsE7Hjh1zVM261Nfh7RSM5uZZxysctkK5+CgVFgMrFLS76U8ht8cff5yneJYCiOYIeHbChAnkg/yvmOhnCgZ9YhmaucyRTFwUS0W2VwkX7dixo+GiKYUU4aIpHrC+knDq1CncAzx5GNn27dtx2xw3MGTLZCFjtErE+cchXGMD1y6WO7SjzEVxC6CR+DS/aoDt8BO+Gj/hIsBPcObwI+XSsoUi/FM8FfkJISr2YuAGujVixIgKFSpgMt5///1XXnklYAMPlV+/+uqrmjVrkj5w4MC8efPmyJEDAikPwhZKlizJnS+99BIUtEiRIqVKlUqbNu11112H7s6ZMydfvnwPPfRQlixZSHSMBAxFxYoVmzp1Kg5ckyZNGG/69OkjviD+X61atciWp1asWCH3o9kyevE/rQnBePTRR9OkSfP888/LDVCvhx9+mBTSFy5ceNddd1Fa7s+ePbveQ0CnTp0eeeQRFGPw4MHp0qXLmTMnjzzxxBNCYkOBsjFwli9fnnoxkFevXv2ee+5xcFH4TN26dYcPH961a1dq/cADD8Cr1a+hJHno0KHWrVvL/hnc97JlywozAY899pjukIXKAYl169ZNykO9ZJsN8D7xIqwcQlVn586dzz33XMaMGXEUYFboAK9OawPh6K8IlcPmzZtffvnlbNmyoSoYLP6gtLly5bLsiAZlqFatGoSc3O644w5yEPPHnTKwIavuNrAJSOzZZ58lH8dEH5oTFxeHoKjgu+++i0gbNGigoiQjR44UcfXs2bNv3765c+cW+SM6dwRBgbK98847sgHmjTfeoAAU0rumNB/9KH369DxCz8JA7d+/n1eXLl2atsN8eeTpBwMGDJC2HjVqFFKCCKn+O3PmTKFkp0+ffv311zNnziyRJsVFP//8cxq9cOHCtD4dZ9KkSZJnKJEeOHAA9Wvfvj0a0rt3bzJp2LChEpdwUaR93333FShQ4Prrr+eyefPmYasQSqvp8osWLaJpyAczgjHHqlMwbpg+fTqVksdFJah+/fr1c9ngEtsigx8SdtsK66KLD/ultIGLwAZKICDoU/R6yilKQjNRYMtm0agrZYCZU1okhh3z33yXJxIV9Dlx4oQwJSwkQ+348eOVvUWM27ZtQ5JBoxKHDx9GRWk4ftVjB6FCM5QKxVAxCPUKzALjCIPRli1b3AO9z+ikA+gelZJSkT+VQktVUIwuzBux/O6QR9BK6YFUoOJiKixFzwpVEp9BE+8YpQ6JTGESVVTFT0zNu4IKDA2YEVqQqjnk7AgG6VwUL5ZLSi4Ono6gXNS7hDoQLLUTd6J///4OZbZCB8QFHtFSN/xENpNJXS3byIuLhbLRcdBYaIP77RI1pgBu34COLO4WwwR9Vr3X+6mw7/UTK0xsVFrBHQRMbMDaCh1dNbBsPZQJPzXtt379et3+0Ch4LPKTimjTK5E8KWgUysMfXIYN9EcLUeaicHEqENSZxnfnJ6WvVFvqrHip2paAyEQQbitjoICUGCck5I+bBalDbxilNm3adPz4cdxKfpU7sTLcc+ONNyqfHtMjLEJ9IoIRghSe6tixo5haWoqUEiVKqDcOGjSIAUZNZYN27dqJLy6XmBU5s4FRX93DwFO5cmXL1n5uYBjjBt2/xCSRcsstt7z55pvCXt566y1SWrVqpe6RAuOFy2WPHj24fOqpp2BHqlJB0aJFi4IFC+p2TbxkxUXpqxAMZS5lrMW7lUsPSVJUvJPbb7+dFDiYhE4YqO68807dm/fIgcL89NNPwqbq1KmDHzBt2rR69erRiUJVJ6wcvKuDR5ghQwZSIKUyBjAOcQmxUa/wyAEPQO5HDaDEVApuI36JDCSKD+P0c6koLtXkUg95UlrGQseiU4wjTsyMGTNUyqeffso9lEcN//Kiu+66iyHWsodDmLlQuFBCE8ghPXqMwFtW1kXGCLex7O5A+R2DsTtP/xA2RRnkEnuIKBynvNDcag5EuCj9CyYpbitGkhT0WW4IKlIGEooNh1cpRYsW5R4lZOGiyFCMNlohCok2ehQ+rIVh5KMudGpUDqFBMh3T7+LrkAnuqVQfK0GKHL8ZylaIi49RYnSgU+PTSOiqatWqHk/997//dcwm4cFA2qEucon72K1bN4/6pgr4DPqgcjVq1EifPv0999yDF16mTJkHHnhAoioIHz3nsmTJkhIdeP311/VXdOnShacwAlj1ihUrxsXFCR8LGprBR6Q8OXPmDFy6CHzfvn0827p1a+wYnY5OVKpUKeUY+I9O6sDCYOrRQO7EKceKonJi6ukvKOHTTz9dpEgRDJ0Ml7pbFqpS2BacaYl3YHbgG3I/v6JvlDksFw0VNBF4xIvdoO5IFVNPPjSQtG/YmJp3BQW9evXCi8D7YhApX768GqyDBoPESDLuM4KoejEIOiJxbi7qXUIHkAO1K168OJnzlFJmVYZQAXGPaKkbPiObyaGuAIGjpdhzeg0+G91ExbIZW9WotHPnTgpJCtRr1KhR6dKlQ1vkJ6wWWs2A/sQTT3z00UfIXEZ276d8vtc7VhhZVNoKHQRMVMDaO7pqYNmHfjFEogb0C5oMakDf111loWMMoDoXRbBcrl27lvZCnhgoLr3VOIqIMhc9cuQIpacDbNy4kXrimquAKBJhFMR/wl3AO0FMcqdl93aZTZU76Q+yUtfD1hsIhI0wNuiJjRs3htv8rQGfj9sYXeQGZMsl/Vk9cvDgQTGgej4YF4ysWHlGYoxC7dq19RvwjzNmzJg2bVoVVBODgl+i7sFF0JcqCbvQhzfcFAfpxZkgpWzZsioFc0+KImlyOkKhQoW8hYPFpPyMf3oi1k1xUTTt7rvvHjZsmBIUKid2WXzxsJKUMyro6ip/enLAnhwWtyNsDvKtDsTiXRc/cghbHYBZ13MAN910E1ISvzxsDnDCNDYcIQCGhOuvv16pAUMjj5Aol24uatnE2EGc0AHYiyOM+tBDDwUuzvYD8Q47dOigbhg6dCgpb731lrfoHLzRj6yobLly5UiZNGnS/fffry/vDJpnooCfyrP0DpXy5ptvyvCvUnB5VdBXuChDtS4fCXyoArhFinuBj6V73ozfuFYqW+GiOlFEYwPhlsaF1WrrYtSgZcuWL730EnJ25CCGQifJssJTZ4xuWyEuvpoKBrt27ZJWU33Q/ZSbi0q0SwUCkI9SsFQNn0Ef3AtSMN1vv/322bNnrYvRBLQLtiORDtJRbyir4gASNKRZ5VIGkbZt26psHd2BfHiRzLQrLorlgbrgyOqFoddDIxXZ8xOddAMLJjQA71k8B6pAHycFhVcajiNOyrx583xWSmbnHNPmmAXv75p4B00sH9GcoIDRBeyVGnqid0zNu4KiMBRPLilPlSpVrNBhHckcx2D8+PGnT5/Gi4NaiOegjykOLho26hcUTZs2Dbh203gHxD2ipUERNrKZfOqKVkBuuQ2iSHMgSazorFmzJFgs5QHIjUs1N4UDoFwLVEhivvnz5x88ePDevXuxtDK74PGUz/d6xwojjkp7BAF92q6w0VUD7J7M87nX5QpIh2HhZsvWSMVFoWBcyp4g6yI1jdk3L6LMRekPMu0L50QW8rcanOg8+j7S9evXSzCD0U5SJOiibosZI0+96NmzZ8Beo6sn4n3my5fvCReUv+Xmon/++af4Ino+EjWUVR/Tp0/n744dOzoKIJHaESNGyCVNBlFR7q+cGqKvaYGXBuWi+PoqRaxSkSJFVIq4FPp8Oy6OfkNQtGnThqcce1P1/aLikz344INuWYlrG1aSEGZygPS65SZB7rA5PProo9zsc4WntxzCVse6yEX1VVXiQYrH6ScH/AyGE3fZFOHBxj399NPkw9gsKUG5qKicGmZQs4Ad8ndkK1STDOVSuKjuXgjTcPhnbjgcZT81tWzllKn+d999N2yeiQLVz2JDzbW++OKLugSgxDhG6v6gZxfRa3Ty7BApQPe8P4TgPrtIHFCdVboRVqstmxvQ9wP2xLJ7mZZ7P5JYhgYNGjhS3FzUsQ2vUqVKJA4ZMiTUU24uumzZsoA9yYwLFbM1SDGAz6APIOWGG27QU2hQEvWlejL3pUgXf9Dx4+Pj5RIHNGDvR1D3B+0OMjGoFKxDhw5cOvY5SxRGpnQsf9HJoJBQnW6NmzVrFrg0voOKkoKL7LNSX331VcBefaAcu3379iEr79NrwwZN/ERz3HBz0bAxNe8KCqPAi1AZQhTV3+6wjtBILJVKoZtLRKxv374qUeeifqJ+QeHmon4C4qGipUERNrKZrOqKRokV0mOFffr0IRF+JZcwwEKFCqlJP9imHjvAx+aSLubI2fspP+8NGyuMLCrtEQT0abvCRlcNZEaQ5j558iQNsW3btv379+v2aufOnRA0KKuDi8oUoAqQHTt2TK1djUGxo8xF8fDwqvGV0VR6gvBsmU+AlkhVGSqwyzI7LPOi3CzLlLlh06ZNisQqgm4QCm4uKr3X2zVPFBeVGPPbb78dNNQnxloPHOL7Bi4GnsePH6+Pc1akXFS8IjneXeqYLl26li1betTRuvgpUTqenqhzURlrQ52p60eSQbmoSGDatGl+cnBz0QULFtxzKVQU31sO3tUReHNRPzmE4qKAB5s0aYLrP2HChIC2eNsPFxV6oK8WFlD3gDb3Gy0u6qemAlkFpMiwR56JhbgIcmD9oUOHqKPsbBSrSB0ZyNXNHlxUOfoOkZ46dYrLevXqeZQhFBf1OLXCj1YLMPLciavq3lEWiovqlsEnF23fvr2uEn64qGUvTRSHGEdZdj1dAfDT0QRuLiq6pLt0op/Tp09XKcoFhBXIjMdDDz2kfg3aHRwqWrBgQS4da93Fd8+aNatc+hkRgsLNRUWZdX4lzrE+dnhXyrpoohWdw2tHebxLEjZo4iea44abi/qJqXlUECIhE9dwY+WDKri7UtCzi6Qr1apVS6XoXNRn1M8NNxf1GRD3GKEcCDuaJKu64iG7u6EEC6iCin1IKJ//Fy5cKJGdRYsWyU84zFwiSXfmHk/5ea+fWGEEUWmPIKBP2xU2umog85n6dCDYsmWL/Cqn8wi3cnBRuVMd44dxkJTYrH9O3u+LCkFHKBBrWZSrqi3zyEDcFJiqrE4GaPD69ev5A/8sWYt3BcDNRX/++WdSZNdHKETARfv16xcI9rFpSdcX5cqSlWrVqlm2c+AY4SLjomSCkcJ6LlmyBFvJ4FeiRAnHeRhuyO4gx2IqnYviXgRc668U/EgyKBcVxog++8nBzUX5+6VLoZZJeMvBuzoCby7qJ4egIxBd9bHHHkO2svxGHL5EcVG6PJdZsmRx5CzpaoYwWlzUT00te9iuUKFCnjx5AsFWASWRi27atInHy5cvb9lO8+jRo3EXAvbH5f/3v//hBqm1TFZEXHT//v2BSwP2bkTARf1otcoqf/78gUtjVYIoclExQUgv1FNBuahlLx2UmVtwBewXtZKHi6ozBQSYtRYtWvTv3x/nRjiG+iksF0WfZVeb49RiCZoAWUYYAy4Kz/FZKeuiA83bZX6gWLFiBw8e9C6Jd9DEfzTHATcX9RlT86gg43XmzJnF9uJI6DNOPrno3LlzHe2lc1H/UT8H3FzUZ0A8Wlw0WuoK/3cEl2WtWVBOCGgI0tUaYJjwwIED6Yy0FI3IT9BL+cmDi3o85ee9fuxzBFFpK3QQ0I/t8hNdNWCAFia1a9cueBYNKpfHjx/Hgm3cuBGfSkIVOhflJ7lNbco4ceJEKuaisgZDTenK4lvYOTWXD7roH2mQqVGdcOKBSVRm9erV/ORnlcVVDjcXRdQMA+nSpXOHOadPny5NEwEXTUhI4O8cOXI4DgOUYUDf7sgrcKPTpEmzYMGCunXrOsoQGReV2/7zn/+8ZmPatGnuMwndqF69OvkMGjRIT9S5KGoWsHfkO07Gowq4LH4kGZSLwl54CpH6ySFRa3S95eBdHfnbm4v6ySHoCAShopqy98yKiIuePn1ahijHsYcyL6p2REeLi/qpKejatStdDNKCPmfNmtXx4ZYkclHwwAMPkANjA33t3LlzFIY8s2XLNmbMGH38tiLiotSFlqLk7pMk1XqtCLioH622bA/+scceY/yTE0Ec57JEkYvKhjG87VBPubmo2vpL9xkyZEjatGnRaooaqsqpBcnKRXHN27ZtW7x4cfGkZSIlUVwUzZEV7+psCIUMGTKkT59enJ5YctGwlRKUKlVKFI/M1Z5PD3gHTfxHcxxwc9GwMTU/Fdy3b5+MlQF7+a4KgfnkohIurF+/vkrRuajPqJ8bbi7qMyAeLS4aLXWdOnWqI7gsfSQUJ8yVKxflF0O6du3afPnyqUCbdMmwXNT7KT/vjZiLekelBUGDgH5sl5/oqoHMiwI1ta5OIRJGhhHbY0NIGf1XDhIT2qWOYpabV65cGZtiR5mLyipctbOcgY1L8RK2bt3K3/jcouu4noqsnzx5Euls2bJF+rZMDZtvuvhB0P2issu8dOnS+jHoc+fOVXveIuCiOMoyxSF72RUgIYULF3Zskh4xYkTAPonB/VWAyLgovahatWqJDc/IOagYZX1+iSEzcHGOi1rffPPNAXsmSn+wU6dOclZtWEm6ueiJEycYwJTjGzaHRHFRbzmErY4Vjov6ycE9AtFheYThWWUrm7LUYirGp4B9EIKjtA4XuUGDBgHXEizYIDmrnUURc1HRXhVs9lNTCBtqKdLGnwu4Vuo68rRs+rdu3To9xRvjxo0jh5w5c6p113hU4ig4dstHwEWBLJFCS/XjeUeNGqW85Ai4qOVDq1EJrIcsBJLzJxwrdaPIReHzujfmfgpfMHDpMVGvv/66PrWFjnFDzAbd5EOyclGRkjLpEXBR6yKpU8spBTLdoba9xZKLhq2UYM6cOaSXK1cOzfEzxecdNPEZzXHDzUXDxtS8K4iRUe21ZMkSCRupyLJPLiozn++9955K0bmoz6ifG24u6jMgHsU1usmqrkE5IYmUH9Nq2WSAQQqtU7/64aJhnwr7XisJXNQ7Ku0RBPRju/xEVw1knyf9TlkSmf+ULzZ9EQxyqIpQU3VkrEyorl27NjbFjjIXlYW4K1asgFiidlJP4dkiIKGjaJJ890Y+egOTUZfqJ+997QYCObVMnZIn2Lhxo6wtwRq+9dZbEAMsSMWKFZWBELMiH6sQyMkxGTNm1K28nIkvu9cAPjoDDCZYnZjHCIdpwCA6SoUFuf766/HU3cOq7IDXQ5uyUhHPVS9/wF7CoVKqV6+O6WzdujWse/To0VOmTMGwhv2EF47yXXfdRVaPP/44PhZqNnv27KxZswbs8wzFNA8ePFjic0gDPjBs2DCMqaJDYSUpXFTfPvTyyy9TcjWlHzYHOfLO+yup/uXgXR2aQ767oHwg/APZL6Q+w+Odw7lz5/iJwUAnISTKufBvvvnm7t27J0yY8Nhjj3FZqVIlHC+cfsY5+a7p9u3bsXSQFuviIcC8XSkJJoJRhxIqlYPE4h6p8+gt+xzFgP1pXJUiEQf9OI2gkM1aY8aMOXPmDA5H2JoyQObNm1eNnTwlR3ToG7rceXbr1i1gr3bbtWuXd3lUtkgA10HxNOSDoNBYx50yl5I5c2bdpZMi0YPk0i1SfE0J7efJkwf3gmrWqFFDl5V0EDWpaF08R9exmsABb62mhDVr1kS86v66des6/JgmTZo4/FexDBTPkaLbColW6Oe7xMfHY6b070O4nxJvuECBAhguOT8Q71OPQUDOUTP17dPUC59BHysiLirnVSpWQ08PXHrYmDs0Y7m4qARfHEeULV++nESsmVzGkouGrZSADiVRG3qcHtkMhbBBk7DRnKCYNGlS4NJFqmFjat4VpITq6FTrYkOoCUafXBSbmStXLv37qDoX9RP1Cwo5y03/WJfPgHgUuWiyqmtQTijbNOQYc9yVgB0BUb/K9h9V/aBcNOxTYd9rRcpFw0alPYKAPm1X2OiqAR1Bdoqq6XeZ8MTrkyW7CsLRYGTiQ+K0yKyp+A8yfej4GFvyIcpcFCaDH6nYNkqmf2oSN0t9evUL+yMuavhHiUVeAnzW2JzdlHqBX9WjR49bbrmFnnnTTTf17NlTP6QHXRQvM2Cfu92uXTtFIKdPn16yZMmAfah3//79UVCaSXb/g0aNGm3YsAEXVoK4AXvRjhrJaFyGz7i4OHzutm3b4jE7TgZSaNOmzdChQ/UU2poUGUsoEjns3bt3zZo1MjEYsINn+JSoQYUKFSQFEyZbNRiQhETp0L+aFQqyYkTuxylHSlQQycDeFeEZMWKE8LGAfTa9IwjqIUnrIhfFsYaiQxFxx2vXrq1bSY8c6PmMefC6gH1mD8IJuwPWjxxCVQfZinMJKOTatWtJkfE+YE+SKx8uVA5Lly6tVq2apDP+qcM8wPDhw9OmTUt6tmzZ4KIMIfKtP26TPt6lS5eATWJr1aqFSzFt2jTxxgL2sRkqnIEdYOCEXaBdPIJu6G4HfqRIEueGKuMU4khJxITXedMn8kFQ4iIo6hKqpig8DQqlVBtaEJecY8EAzIAqHqQ7T0oludGzvJtSgVHf4YDCo9RpVYJ169Ypyb/wwgsMEjhAuKSSggu+fv36UCL97rvv5Et9gYuHRshML9ZYHA5QpkwZakpL9erVSzaP3XHHHd6zFqG0moKJMVEeLUOAWgFYp04dLEbfvn1FjXEy5JNLEEixDPgxPEhWblth2V0G4cAbqWmHDh2guA0bNlQTO0EtjGUTCfk2D9WXUtGCefPmbdas2ccff9y9e3d6MQL02V6XM3wGfcTD4059PYuotz69gKaRor6JJUwPc0oroPkSTciaNSvaKNEQd2jGuhgu0T/YJt/EVhSXMmA29UU6fqKTQSG8V4+NtmzZMqAd42ld/EQzeuizUgqyK9Lx+bRQCBs0CRujDAoxL479ct4xNe8K4sHjDKgANGqDiVbHE7jDOsLN9ANsGEbpj/rGP9ltQT5q/Y53CUNBjIZ+BrLlIyAeNFoaCmEjm8mqrsIJdY2lY8J71SlQsn4NzJo1C0qAGktkAQonkXQ5m0NNZvp8Kux7LR+xwsii0h5BQJ+2K2x01cCyO7KsLWX0x3WR6U33vjbH2UUnT54UEvuNDeFiYZ3SaCFZzi5iKIJC4JG7v2+DwuE68Cva72Cb/MQj/OQn7mjgB4cPH2aoiPpHC7AdjGTeo+bx48ej+F5cc0wqniW9iwEVSoaZe/vtt2E+fnbr0cfob6JXQWdTUUWG6j179oRaFh5KkmqNLq9AJh5Vjkpb+JRD2OqERQQ50HP1EBJGQF/5adksxXEIRChgCrChUd+/d/ToUfdqiyTKyp0ndBqHFWboMwcazuE2oSpRj8T9+uuvqF+oD45FjGSyMGEBv0XZ/DcZGkU5lcmSPyj2jh07aP0raTNI2KAPkG8sixeOJ40Cd+rUSUUl5syZg3xUvKBAgQLCqaCpEvrEZezQoQOZSxgxX7588pUpR2hm1apVL7/8smQL91ChDVyid999Fx8U9tWrVy+oDu9STeAzOukAHqosSQjYXxOVwAp+qszIScgD5YdRyIF2WbJk4aV01bCVUqDY6dOnVxFMb3gHTQTeUU4HDh06BDGQHRYZMmSgldWxqJZnONW7gnDR22+/vUqVKpMmTeIpmokBxQod1sFtQ2d45MEHH2zTpg2Vqlatmv4dICiECjw999xzS5YsCVtCN+BykBmkLZSDiutfVfEIiHtES93wGdlMDnUVCCeESCNGHmndujWEkJbVzZHqqtR33bp16IyEMLp37z527Fg6mvyKHPRJZo+nwr6XX8PGCuHAkUWlvYOAPgPWoaKrBgo0JVJSc3sIOahtcXBRy/YTVq5cKU+hNu5NBMmH5D1H18Ag6YCAMfgFNTevvfaa4ziZGCPo2UXJhMtZDgYKOLhVq1Y1ATWDlIL/oE9iIVFIFXrA44GH6BYpaLgnFKA3l8Nn28JWSoCRd+8jDYuwQZNoRXM8YmoeFZTz0gAkyjuW6sCJEye438/co58SRgA/AfHoIurqqq+VRQ0gBkElw3vVCSyWveM37O4k76d8vjdieESlwwYB/duuZIquXknACUFKJ0+eTFT7cvPvv/+OGxNjhm+4qMHljtKlS2fNmtWx8NWyY89t27ZNkSIpxJKLXs5yMBDgi9erV0/fvmhgYHAF4MUXX/RetW5gkCiEOs/2Sn2vgYEHDBc1uNwhn+fOlStXhw4dRo8e/d///rdfv3516tR55ZVXHB+hjj1kxdfSpUtj8K7LWQ4GgvPnz5v1QgYGVwaOHDmSkJBw9OjRRYsWFSxY0HRtgyjCcFEDAwXDRQ1SAaZPn16lSpU77rjjtttuq1SpUrt27XyeU5p8+P7771u0aHHjjTdi0++///7evXvHYG39ZSgHAwMDgysSNWrUkG1padKk8T701cAgsTh27FjAPgwvUUudU+97DQw8YLiogYGBgYGBgcElSEhIiIuLu/fee+VUTwODaAHVqlq16g02atSo4X0I/BXwXgMDbxguamBgYGBgYGBgYGBgYBBrGC5qYGBgYGBgYGBgYGBgEGsYLmpgYGBgYGBgYGBgYGAQaxguamBgYGBgYGBgYGBgYBBrGC5qYGBgYGBgYGBgYGBgEGsYLmpgYGBgYGBgYGBgYGAQaxguapDK8O+//27YsGHZsmUqZcuWLePGjfvrr7+i/q65c+cmJCToKXv27Jk5c2bUX3TkyJGRI0ceO3Ys6jmHBdL79NNPk5LD+fPn58+fv2PHjrC3ffjhh9u2bXP/dO7cuRUrVgwYMGDGjBkpIoSo4+TJk+jJwYMHPe45ceJEfHz82bNno/jeCPpCchSVAixdupTCRLeo4MCBA5MnT07UIwYGBgYGBgaXLQwXNUhN6NWrV86cOQOBwCuvvKIS4+LiSIn6J+DUJ6FxxLn85JNPihQpQsr9998f3ReB1q1bk3P79u2jnnMowAF69uyZO3du3vv4449Hlsmvv/7aokWL6667jkw+/vhj75tnzZrFbcWLF3ek//bbb5UrV165cuUHH3zADdmyZUvV3+D+8ssv69SpkzZtWuqybt26oPds3ry5WrVqqBb3IMMovj1RfSE5ivrvv/926dLlhhtu4P4PP/wwWkUFlPA///kPj9x2220+HzFw4KeffkpKKO3s2bOjR4/+4Ycfolik6AL1+/rrr7/44ouULoiBQfRx4MCBUaNG/fHHH5E9fv78+YULF3777bfRLZWBQdJhuKhBhLhw4UKKvPfdd991cFFc3rp16ybKp/dZeN6i88PFixdHi4s6CrB69eoaNWps2LAh6TknChMnTkwKFxVUrFjRDxc9cuQIzIc3OtJr1qz55JNPyt/Dhg2rX78+DqWVcgqWdFD+u+++24PgWbZbkDFjxqhz0cT2hWQqasOGDcNy0Qi67d69ew0XjQy0b4UKFZDevffeG3Em//3vf8mhSpUqUSxYFDF58mRR5ldffTWly2JgEH00atQI9e7Xr19iH9y3b1/r1q0zZcrE4/TiZCiagUGSYLioQYRo1arVyZMnY/9e8Yd0LppYzJw5M7JJ1B07dkSFi/7www89evRIYiZRwZdffpl0LioDZFguGhQHDx5MkyaN23e8fEQUGR599FFvggfuuOOOqHPRCJAcRaVBw3LRCPD7778bLhoxtm/fnkQu+vPPPz/11FNz5syJYqmii1GjRqUWLuqOtcUm+pZ6Y3wGy5Ytq1mz5vfffx/Z408//bThogaXJ6LPRXEiv7kUDGDy019//YU3v2bNGjzgbdu2/fnnn/qDv/zyy8aNG1euXMn/3puXDFIcMp+Gaxj7VyeRi3733XeZM2f+5JNPIng2Klz09OnTcXFxl4m3lOJcdMGCBW7f8bISUWQwXNRw0csNjLBJ5KKXPz766KNUwUXHjh2LI6SnfPvttwMHDkzu98bmLQaXJ9544w3DRQ0uT0Sfi65du/aLSyGHmly4cAF3h8sVK1asWrWKP1avXo3TKU9BPuVm+Qns27cv6mW7UoGPOHv2bDw/JHz+/HnHr3/99df8+fMte5HkmDFjIGPqJ3w7yMDo0aNpi7///tvx4OHDh2fOnDlq1Khly5adOXNGpUPkrr32Woza0qVLeePRo0f9ZOhRjLA4efJkQkICFdy+fXtQLrpt2zbH2TnHjh2DHU2dOnXLli0qtME94lX379+fkquNT6HK9s8//yxfvlxtz9C56P79+8ePHz99+nSkpOq+7iLkRJYDBw6oFNkDyT0QPzJ55plnSPzmm29UgfEUEZqj4ufOnduwYcO4ceNmzZq1d+9ex6/0KZrm0KFDIgHk8/nnn7ulF6odrSRwUUSK2zd58mRa381FQ8mTt6uzoGhTJCArrkUaokseIkoUJH+BZLJ79+51GmQlsGqj3377TT1LGWj3Dz74YNGiRToB+/nnn+VmdSrP999/r79CISjB442IgtakB9Gy/gne2bNn9ZIrTdizZ4+kUAt1s7svSMnRgQkTJrjPjopuUQU6F6WXTZw4EQV26F6oonpYM52Lkhv6jE8fdPuTR32TYohSNQwXvUyArciQIQO2V6UwxOTLl69nz57J+t7YvMXgsoXholcPTp06xciIkYGR4Ta7zwjEQZLJwh9//NHxE6P/1q1bd+3aFavC/n9EmYviHEMjN27c+KsGmf/EOeAn5IJ7QVXx4bikwpbt8eOFc4l/b9lDJn+vXLnSzY4M3JgxY0bhwoXnzp2L73X77bdff/31ZcuWfeKJJwYMGLB58+aXX345W7Zs1113HQLnDyxRrly55EGIRN26dYcPH961a9csWbI88MADOv/v0qXLPffcA9ukaSpWrBgXFyf+Lq35zjvvyNkkmLbu3bt//fXX3hl6FyMspk2blj9/ftxKtOKll14qWbKk4qLwh969e8shKPokzOLFi4sWLYrHiR/cqlWr9OnTS/rIkSNxxYTnUHLoU6iy4SLj0Mg5SYqyKi46dOhQOfEF4FXIHkjYphzPA9Bhy3Z2aRTZayc+N0S9Zs2aXD744IMU4P3336cv4PHDB9KkSfP888/rFV+xYgVVGzhwIBWHs8H/GzRoIJSJVnjttdeyZ89OVvAlqpM3b97MmTNzSbqeSah2FETARenjvKJ8+fJz5syhOtWrVyd/xUVDyRPa8Oyzz5KoJrWwgEjgqaee4gZUpbsNdMktIv9l04GI6tevTz68VEg+5ZHDb3Lnzk2KcFFI9WOPPVa8ePHjx4/Lg1DQYsWKTZ06FS1q0qQJYu/Tp48sbEP4nTp1IgeqLDfDb+kOpNx66636290Ej/xJfPHFF2mLSZMm8VLpRH4IHgMJ6i2q1blzZxX+oCmrVq1aqlQp/gjVFyg5/bRFixajRo1q1qwZvzZs2FA/ETe6RRUIF+WNNEEuG1wiVYnIhCqq5WnNLI2Lfv755/RN7kyXLh0dh0L6qW8SDVEqAh4Ggp0yZYre2XUuiiPy2WefYVTdMV+JcNEL6NH64wIeXLJkiZ7CqC1nBaEe022oELOAjoYp4120mgSb/FSBp/T4C6WiqHoKboOlhYfwvaxLuShdm15Medx7Sc6dO7d8+fLRo0fzv+OkNH7Colq2gRo7dqz4JII9e/aQIcOc23tzg5d++umnjDgLFy7UD5tB8VBsCjlmzBiKTf4IRLbcM7qRooIjoUri3UCWPRLRIug/JlqtPgv1Fst2wPDEGMWQXlAHlNwQLzViqFLDfVBgOubNmydxT2kgHXTDNWvWUHGGZgZHt8RkvRK3UXEURtUOr1q1O60giXv37pUUXYc92minDUrFME3TiP237GU4lAdlWLVqVdCjwj20xaPM/sWSKL1CDRznSjAcoORYTiiHOB6hEIqL0qa0LDJxW3iPzFEhdAYzQkdzt6YDQXVSwVsxIAIJCQknTpygydavX09fwJJ7v+4qB2ops3pqbg+56Yvz1RlvwBHM5Ta6CekRTwNEhihzUQwWdcA/c/+0bds2flKWDsUSQeBm4ZrIfKn0UsSEi0yKPuFmEBQMbPjK3bp1k0tkiK1hqKOvMkgz/OBNksI9+NCYElxA4SroaOnSpZU5liNMK1SoIJdySA9er1zSFly2bdtWvVfmSXSvwiNDj2KEBUQUd1M/ubF27dqKi2LgsFzlypVzOLV33nknr5C/KRLsURVMJvHUGt1QZaMzMzDgCru56I033tihQweUk1e/9dZbwhDo6nKP0FfdavN2xUWti2uMVeSegh07dow3kqhzUSzFNddcwxigUhgquAchSzfhf6n4Qw89JFaD8tx88808pbhK2HaMgIvi5RcsWFANyWfOnJHDeIWLhpInfRyZuxdYMgC7Z7kdIooYtBHFyJQpkyot/SXgOsv3hRdeUPowaNAgHlHbCkC7du0k7CKXWDCdi1o26Q3LRbFyRYoUQffUDQwAojn+CV6tWrW4H2KsJ6IDwgRC9YVevXp17NhRXT7zzDPcoCxGMhVVuGiBAgUWLFhg2c5E5cqVSRk/frxHUb2tmXWRi9Kg0EshGCtXrpTggp/6JsUQpRbg1yLqrl274vW2bt06bdq0CER+Ulx09uzZWbNmLVSoEDQ+c+bMumsLJ7nrrrt4hPEaoWXMmFF1DYxJ3bp1M2TIoGZWcb7Lli0roT14L60gLIsbcN/lnvPnz0OBKA9ewcyZM7NkyeJzuymGEVUXxcMbxtzBPSRKlT17doYbMekoRpkyZR5++GEhwIqLvvnmm9SRgYDL/Pnz63QUo/fUU0/R0/v27UtWhQsXxvey7FAFPA0TyuiGZyzHgz/22GNSC+xAmzZtcKbr1KmD3Lx3s0MtcuTIAefZuHEjAxbFkFdYdjxUzmNv0qRJ9+7dUUj6yBNPPEHKI488Qgo9wqMkHg0kIEMEQjn5gwxvuukmIbTut8j9tAv3Iy7MyMCBA2+44QYKLB/WQmHefvvtfPny8dRXX30lMUcUxr32SjB06NBKlSoxZMNPcuXKhYLpLJFiIGocAxhd+/btGdbRCpmugefUq1cP1cKKbtq0iQdpMt5F4flJ1ZqU8uXLK+PMH9SlRIkSwk5DtRGvGDZsGHUU+8NPolSyRpp68br4+HjKHBcXh6gZYRFU//79vbUlbJn9iMW/XqH/UDU5fkwfGefOnfvAAw/Q1jgYNFyxYsU81NLNRWHOdN533nkHESFJfBv9KA2PzPF8SEFRESMy0Z0KN0LppMBDMSAUVPaWW26h2KtXr6YLIGSsN4Kii3m88SoHCkl3RlEhloy2DO5IT1/5dejQIW6g7XQuyvhIgyr6mrq5KB4GdcBKYoKp55YtW1REkL/5ScW0cOCkwvxBf+APPTCPgSDlp59+im7xrjwwqNBL582bp1LEZCsajwlLY0NXRDk8E+vz90XQBGKgpYEQPkYZAy33ixMjY6HAwUXDZhi0GGEBz8G5wUbriVhkB3sRtqAGV6yY8Cs1rz5hwgTlGzm4qHfZ7rvvPjcXpab6Pc8995xO5/Lmzevgog8++KAHFxUIz9S5KAMDJlhRaAG0k9vGjh0rl9zvaH2ZZsTiy2XYdkwsF8VUIajhw4fric8++2xAW6MbSp6YghhzUVU2/ACVIjJU7sLZs2eLFi0qIUM4POJiiNVzQMlx+PDp5RFRbJ2LYuvDclHcES4d60UlbOGf4GEVhXep9Tb4NHiKupI4+gKqy9COJ6c6JpxBCF6yFlW4KG63SpEd5nqbOopq+bBmwkURtV5l4Rtii8LWNzJDlFqAwYT/w8fkEqOHc6ksmHR/Ulq1aiXRmdGjR5NSq1YtlUPx4sXpAvI3QsZ1Vh32+PHj+H+BS1f5QiylRfr164dseUTOR1HHZfMKvb0GDBigd0Zv8BTV0XsrPZSeSKJ+GwRVfcRFuChlZpj414ZYgCFDhsgNuCh0XjVyzZ8/X4JT3EkibIFLDC/e8MGDB1977TWxdXje+tJWHHTHIKID1aKQ8Bm5xCN02HaJj+hrdCV0q17hURKPBrLsiD/tq9bwb9iwQVd+x1sse0ogW7ZsKlhp2TFlegejDyYRdfrxxx9FhRo3bozpowzNmjULWmtGJRRDRf3gcjzVoEEDlS2XixcvVvf37t1bNwjYFt4LtXvxxRdliht3Qt4rNzC+cAml0V+KsqnBLlQbURHU5uGHHw7YwXFkkpCQULduXboDzmeePHmU/kPLuefmm2/GlRe66KEtfsocViz+9Upi1i+//LLDimKZ4Xjy9+nTp9V0QlA4uCgdFm6v9JD8M9lQe5pCZS4qrXol3v5LL70U6qXeOhlWMWg+tJGUihUryiwXVAKxY/Y9ano1A5dG5vZCfbubdBqdUVJWpyouyji7xobQ0dTNRVE4YZgrV65EFvK39GTUiL9RRJnVgaLIrxhuOCd/4GmpfFBuUi7n75hdJsAI6uQE1KhRw+E1XnPNNWr0EjDABOw1kE+4oFxSNaGPHRcfESde5eDgon4ydBcjLGbPnk22Kq4vcO8XlUlF3amVKZeyZcsyqDjydHNRj7LJlKZ7ja5+z+rVq8XDk8vIuKh4HspfYQgM2CtXHeURnsAALJfCRXnWUTt966Z3OyaWi7Zp00YilHqi+6VB5SnzhzHmojK3Bt2SS4yPRK/V1NmECRMQi/w9ffp0/ScFYfgjRoywIuWi0N306dM7IgsRnF0k2argQp8+fRy9w9EXxo8fz2W1atUcvfLJJ59UC6WSo6jus4tEw5UT5i6q5cOaBT27SDqpxLz81DcCQ5Ra0LZtWzRTb7tx48YhDam7cNHChQurX/EvScFkqRR8U+yVuhQPXj/WwcFFN2/eTErlypVVClQzoO0U4A8cR9mMY9n+Llbdf43ef/99cnv77bdVStWqVUlRhv3kyZO4qupX4aK47CpF+EPTpk3lEmqKvVKhCvw2uITKUASSOXNmFbu07Ol6dIYxTj0ly/JRzqBlpo5wyE6dOqkUbi5ZsqS6DMtFQ5XECtdANE2LFi30+1u2bKk+S+Z+C4aXFEfQXyQs5g7Iphj3WQY69u/fT5/Sowyy7R/zLpdxcXHYEP0RzCasT9eNG2644dprr1U3MGDpoy2mWwITatkdr7jvvvvk77Bt9Prrr7t9CTk5TxeIDNZqysRbW8KW2VssidUrIJE1NTLKkAqvVl1+9OjRoZ61XFx0zJgxMLq/Ncgq7kGDBnlnLsZcaYj3e7110o9iyGqItWvXqntEE4T/GzggM4JQSmzj9u3bt23bhh7qg8LOnTshaCizg4sq4PGmei5Kv/r6668xFhgONFsopVTpzJkzwk5xeiRdMVU3F+URw0X9AL+NPqk+z2jZobWCBQvq97h9L5mFC3vwKS2CEenfv/+WLVuEaqqfHFzUT4YRuIBysI3DzPnhomiUWCssWrNmzfS1xFHnonT4gA1x+KLCRZctW+bwGgXz5s0jvVChQnLph4tanu2YWC4qY5VabxbqpZcPFwV0B3KTuCyFfO6553LkyAF1lGlzpKHCwLi83NmqVStHDh06dFAObgRc9MKFC7A7XurINgIuKopRpEgRGVqKFSvmOHLc0Rdk7tH7FclR1FBcVJ8dcnfbsNbMg4tKJ/VTX7dydu/e/Z5LEXb70+WJPHny1K9fP9SvQc8uwpNWcTTLnn4R1frrr79kyy6PKGm4cxAuqhsQaWjF/cRk4bLjuUbwNRF4HQpJvdQuO6FGak3gyJEjZS+xwH12EYod0OZ+6adolDtmKqe+SV92OMdQOMYR9yOhZggtLQJ44sQJmSvT1dgPFw1aEsuzgeTrux6swP2Wu+++O23atI4djGJ+IQByKeOX9yK1CRMmuMcFBVzhgD2v5UiXgWPw4MFy6eB1Ml7ogRIJxapYod70Ydso6FZJMTj66IPe6pX11pawZfYWSwR65VZvmTOsXLly0J1xDjiEgB5my5bNXQDk7J05diBTpkwUnm6o74V2w1snfSqGcFF94aTY/KBbcw1knak+HQjUaYv4q2rN6ZXMRR0Qgo5QxHoyrshGUFJ27dolMoKjyiG67jW6+q4tg6DAn27QoIH0W9kdnj17docOuX2v+Pj4gGvjmY7z589jZYoXLy6DnLggHlw0bIZBixEWsAKyVdNWAj9c1LJjH6+//nq6dOn4CVdGjS5R56IgQ4YMyn2PChddv349l1myZHG8SNIfeeQRuQzLRcO2Y2K5KPSY+9WKuKAvtS4zLjpo0CBy69q1K3+XKlVq+/btb775Jilz587dsGGDcrlAv379HFxIT3/nnXesiLgodo+/kYnDF4/smy5UQRodGlC1alXHr46+0KRJk8ClEWU3kqOokXHRsNYsLBf1U1+3ck6dOvWlS5EiX6tKIqA91P3FF18MdUMoLoo/rafgrPTq1atNmzaohEy7KWsWARcF0t3kQbWv3j/q1q0buLjvAJWge2Jjs2bNKivQoKa6WobiotLNuZO/KU+odwVlgDJ56Di0Jix+/PFHbG+3bt0YehwWIylc1ArdQLJeWj/HywHHW86ePQudIMVxYI8cK5A/f3659MNFqSn36Oc86Vi0aBG/Yrgc6bJOp3nz5nIZlotCe+i50Cdp+jJlyqimD9tGQbmoBGfvuusuNWtUrVo16L1aguutLWHL7C2WCPTKrd440mKc06dP37lzZ8csugMOIRQpUkRfJOWGR+Z4UDJFjIlW63Tc8NZJn4rhzUXnzZvniCQq3nV1Qo6JldN56NqHDx+Wy+PHj6PYGzduxAhL+OlK5qIy0a86Np1ZP5TIsqN6kAQuT58+LT/h9Bw9elROfFL5yJ5a7zPBDATYsipVqsC7MHzDhg1ze1Fu30uWlRYrVswREKV1ZK8Rjjs3LFu2TNLDctGwGQYtRlgMHDgw4FqyEpaLMlCp3kWnEt+9Xbt2kpJM86KMYXIZFS4qC7SA44MTMsmg6hKWi4Ztx8Ry0erVqwcuruEJ9VLrMuOiv/32G6MmHsbixYtlL+iePXsC9lRJw4YNFy5cqO5MSEggPUeOHA4mJvOin376qRXpGl05BMuxYjwyLiqje7ly5ejy7pUIjr6Az8pl69atHbcxLKnTUJOjqJFxUSucNQvLRf3U90pdoytTEJCTUDf44aIrV6688847Z86cKZdR4aKW7XTefffdEubwIEtBQcMpzcHM4htIK9MRGHeeffZZ/WZvLip7SRwHEOgIygBfeOGFgGsHtTdGjhyJGNWGuihyUY8Gklk4R+hWh+MtWDn5Nptj1otBJ2CfEiSXfrgohjTgilEqyCjjPrB6xIgRgYtRQssHF7Xsk/NIpPoM8foSgLBtFOoI2b59+0LIUZhTp06hzDlz5lTtElZbwpbZWywR6FXQTxZB0Vu2bClhhZIlS3qsXHUIIXfu3BB7x3YMBzwyh+o88sgj4qg4VuEqeOukT8Xw5qIbNmxwRBLdX7+7qiDzonIurKTI3B76LIwMPd9jA9F9YR+x6zhN/UrgojLtqeYz8b/V4lvYOSJQyxWQyxcXv+ly/vx5fWepHMYrU6bRLd6Vh7NnzzI8e08gu30vLObNN99MZ1ar9gWdOnWSxSdFixbVOYzs6de3L8qmO3Vea9gMgxYjLDZu3Cjuiz5Yynkb+o4gh1NLYVRETS4zZcqk5hL5KXDpYTYeZfPDRRcsWIClVvF+CHlAm5mBnOfJkyegbfSX8z8cttvtqcsEkWPvItYZWqV2s4TlomHbMbFcdMCAAdyfL18+/ShF+XSKfuSvfy6KYxpwLYsNKqKjR4+qD7EkFiJM/Aw0SlLQh3Tp0hUqVEjP8Ny5c6LYcvqrAm5Z4cKFxbLL7BMuiIpnC7PNnj27/oiD4D355JMB++Mi+j1yIFBiTwunwPJdIlxS94GWjr6AHgbslep68IWGgJOrw3uSo6iRcdGw1iwsF/VT3yuVi2JqcIvTp0/voA1///23nJQbloseOXLk+uuvr169uvo16VxUOTR0Ljl1XD83yw9Q+Lvuuitjxow0rpyecvDgQRqxRo0a9GuHo+/NRRFF2rRpaX33wkIxX0EZoMzS6HtWBZs2bQq6MHLhwoXcP3DgQJUSLS7q3UASEcamOUJpiEv6lPstcjjflClT9PsZsgNafNAPF5XogJuQyAyMnFoXcC2q7Natmz5a+eGieIwkVqpUiSZevny5Sg/bRh6f1nzxxRfbtm3bpk0bmkw3cWG1JWyZvcWSWL2yXOqNwVR+BT1RBi9HdE+HQwiiPMo9UJg1axYq5JE5LFRtv0cU8jG5oFvqvHXSp2KYNbqJwrFjx7CKurMk8584KrJS1Q3HbvArgYvKd2lWrFixZcsW2fMJZH2g+ogL6RgU+VsF2r/99lsusc7btm0TQnuVz7P7hMwcMiT37t175MiR8fHxn376qW7I8ADEOXMsBRk8eLBYATxRCMawYcNwuBXzESP12GOPYXTwy2XlW9asWWk4mTBhMAjYX0g7c+aMmDbvDEMVIyzkFETc7lWrVkEGUB4ZPrGMjKASrWjcuDEpausIVjJLlizKTmH08aTVZypleEBi5DZ58uTTp097lE2O6FQERlgHjpE6oRetLlGihArgWRe5LvLBjq9cuZKySYHfffdd3WMoUKDAqVOn5DQz6+Ipo/rqUAwKPjdDnYqbHjp06NZbb9VdHDnZRc08WxeJhJp5CNuOcrCHCoGHBSKSo03xPmHmyFC+D0FK1apVZY4xlDz37dtHOr6UTv9EgevVq6ff6RYRf8iA53FenweEcusHCMsJK3379nXciR+Gb0GTqQAwQzXuiO44qtOPMNkM20gVfaO+CFM9JbvalLf03XffyXJxvAHUAK175513ZFKiffv2if1a2ty5cwPa9LgOR1+wLg7kGTJkQMg4oxgK3GKZ402+ooqmvffeeypFNFxf4+AualhrhvsSsA900ddfSCdVE7ne9Y3YEKUKiEGgb6rDbOhrtJp8tzAsF5Wzu3SqIz4flkcuI+CiePn6dLqcOq7iAhg3P6dCiNHOkSMHXUxSsDbwBPcXLLy5KJAvDFepUkV3jvv06SOnNwdlgHL+GZ2CP1Ti/v37oZRBS9uyZUudiwo/UUterYsTYvpnWuXMrS5duqiUoCXxbiBGQ0TkoDe4+3RGGbDcb5EJKKShv4VuS2UVD/HDRRmXuYcW0b/VgSVRC1zldOV+/frpT1WrVg3aplZ++uGi1sWDCbFa+jgSto1CcVEoqJuMKXhrS9gye4slsXpludSbnqV/TEVizdQo1OMOIfTo0SNgH8yub49nBHzrrbe8M4cl6l9mkm23Qc8kC6uTfhTDcNFEAa9MdorK3B5yxqGSdaayZFdBONrXX3/tOB/hSuCi9Fj5jqgAX1xfK48noe+mVSOcPCgffVF8NdR5xAY6kLYc0uNA3bp1cdeWLl1Kr5aUJ554wrGsn3FI1uMF7Fkd/VS0NWvWyDedMmbM2KFDB4yCTJ7ky5dPXEOIjTisRYoUUfP7oTL0LoY3eDXmL3369GLTa9euPWrUqBtvvBFfhyGEwsDxYAIBe1PokCFD6GwySQtFpADwVfwzclDOKwopxhEGBXcKVTaor5yfLlRN8T1cZ1xbZI4xxeeAc+rf47Ls+f/ixYvLg6VLl6aEderUQW6dOnX6/vvvLds7lNE0U6ZMePl4jUOHDhV6Ix9XVCtM8Nhw3RgqGBJwIGgCNV+HWBgRaR1xDWfMmEEKohDOEBcXJ4OlRzvCTpEPdwbsmWeGH8d64FCg20LqpIJUoWfPno0aNYKgdu7cGW0MJU+4n3xhMmAfeQ+1Ix+cHvi2MAcqqAZsh4gse9Gy3EmKf+XRgZT0XQCIAsHKZ/QcoBY0HJKhLZA8frbj8AnyQb2lLtQd/pktW7aHHnqI6pAhtktO0AnYy6Hli5qWPWWnuir3o3uQqFKlSg0ePDixmxHkhCHH4q49e/a4+4Jlx86bN28uPQgULVpUfQUhOYrKyAfDx0UL2BOY8iEKiKhoOA1NgwbttlY4a4YvolQLb37r1q0MmbKlPGCvTZW1CR71TYohShWAP4gFQIwdO3bs379/mTJl1BEg8mlcBK7ul70AyEpcbVkNSw70RIZjuqQEnqBAsrxFPs9LospBPslQtmxZlSJBBwyXXL7yyiv6x2xfe+01tT1MTjHFqutfdAgKbAU2iqZUKbNmzQpcGsgQyBe/9Fl9Cbep81EkzhWwyQwUl9EEpqFmrjC5AftQdMdmE7FdaCw543kjGSQcymDya8CeCEVFcXgYJq677joMFyKVsKbMD9P1sEIQA8ydfPYWyUBBMd0MIkFLEraBZElkwP54CZYZyRcqVEg58e63yFc90qRJk5CQoCRAZ6d7qpfK4pqwjqmsR6WZoFLvv/8+Yy7j4PHjx+XXgwcPYjMZedWqBzxgZKL6ptg0lEEFiSR26V7AKXxMff/TZxvJCfB6JNe6qAxVq1aFlTEaorpQLBmm9RtCaYufMnuLJVF6ZdlrvwP2l2nlErqIq6NiPSdPnqQpHYt6dEiURH2mhfsx72IT0MYPP/ywWbNmjH0SUfXIHC6q7wX47LPPqEKo8968dTKsYlgXT0zUUyT+6Oe4pqsTDAQyt4cuMZrzN/+7j467kveLCs6cOYNPduLECTefxPii3Ni7oEfq0aX5lQEyspV4VyHwkrGMBw4c2LBhA+MTIzQOFmYaT9rBkYICOeOg4MU6hl7LdlMYSlVoihvQbzUfaNlrJtViUT8ZJgXnz5+nw8j3ytGrUN/aVmWQsYESbtq0yb3ABrJKF01KCfF3EU6oA07IGSEo2+reZYcYcbsdJ0aEAjdTWjV6JRZh2zEy0Ba0iDREchw66hYRFgMTWaRIkcgydJMoxwm0DojcQrUR8uRXNb3jfyMl/h99VuxbxPvhN2/erG/69QNaigIn6o1RKWqikERrpiOC+l4ZgO3g6onzlzVrVhxBScf5e/zxxyUdfrh37158vtq1a0sKrrCc+69ScElpjnHjxkkEgbaYMmWKTBMF7GNsES++Dv5lwJ5nhr3QC/BK4WABe/mDLEVp3bp1vnz5+B//tVOnTo888ohM0lr2GTnCnJVv7QEKpn/dHtcCf9RhFWfMmCGxjMyZM/fu3ZtRAGohC9rhDDjBYvdQLQlsSTn79OkjYwHOroqXwRwcy7wbNGgA61CBD7cDpyAfpRSazVMMQLJH4I477pDJRsZHCRHefvvt4vBh3GSqB58eShCqJN4NJPdMnjxZMpdAzJo1a1TBHG+RRHpKx44dc+bMCQ/p3r17pUqV1AJU8hf2ErB3dsBhPAYOfurQoYOcZxOwJ6Id01aIhcS8efO+8cYb3MmL1No3tFG+5ySqiGzRLhU2at++vT7E0PRwJ7fJDdVGMCuaXr6SCufBnijLjy8hS4ccqFGjhqppKG3xWWZvsfjXK+4cMmSIcDApBj42QqCtGQvGjBlDT0ekav2XA4cOHYIHylRB/vz5hw8fLmM3qigf3A7YhLlp06aqT3lkTl/OnTs3dZk2bRqJZcuW9Q4neeikt2LQhSm2BBbLlCmTkJBAqWQDSMCOJ8aYL6UWoKI4jWpub/369UF3EV/5XNQgNti3b1+2bNn0MJ7CvHnz1PEGBgZXBgYPHjxx4sSULkXKAx9IX5h9ZcBYsyji8OHDO3bsiCzctnv3bp3D//TTTxIEjAxqch7fyL3OEw/7gw8+cG+Zc+Po0aOOCLW+rioC/Pzzz4mNyuEZ4yX7CTzBl7Zt26b21Fn2WQN6aF4+/afXSB7xDrMKwjaQRISDrmAM9RYegXmqAyAihhwcCMcLdYOElZP4ZUiPpvffRpbNRWHgyHPjxo2wqTlz5kyaNGnAgAH33XefY8VpBNqiw1ssiSqzDlpNosxyGkvEB6z89ttvFMDxuEfmpPPrhQsXfvzxR/q1H7F46KQgKophoAORolQYh+jODCUTDBdNxejcuXMgENBXHgroz82bN/f+7pOBQerCyJEjQwV9rwYcOXIkISEBj3zRokUFCxZM+sz25QZjza5C4KPXrl07iazSwCACoHslS5acPHmy+6clS5Y4Tjc0MDBIVhgumoqxdOnStGnTZsqUqVGjRsOHD4+Pjx80aFDTpk3r1q3r50AIA4NUhKv8VG05lkbWQ6qzqa8kGGt2teGff/5p3LixY8GegUFsINuV1W5qBQaal19+We2/MDAwiAEMF03dWL9+/fPPP1+gQIFs2bKVLl1aTvRJ6UIZGBhEGQkJCXFxcffee29id06mIhhrdrXhKg8wGaQgfvnlF9nE+NRTT8FI4+PjhwwZAgutXbt20J0CBgYGyQfDRQ0MDAwMDAwMDK4i7Nu3r02bNkWKFMmaNWvJkiUbNmx4BUf6DAwuZxguamBgYGBgYGBgYGBgYBBrGC5qYGBgYGBgYGBgYGBgEGsYLmpgYGBgYGBgYGBgYGAQaxguamBgYGBgYGBgYGBgYBBrGC5qYGBgYGBgYGBgYGBgEGsYLmpgYGBgYGBgYGBgYGAQaxguahAe+/btmzRpkp4ya9asy/zTf5GVMKXq9c8//6xYsWLDhg2xf3WM8fvvv3/00UfHjx9P6YIYRA3/+9//xowZs3PnzpQuSCQwCmlgYGBgYJCCMFzUwAuTJ08uWbJkIBC49dZbVeKBAwdIufbaa8+ePZuCZfNAZCVMkXrBQt944w356Pb7778fs/fGHl9++eVTTz11zTXXUNMdO3akdHEMogasBG1avnz5lC5I4mAU0sDAwMDAIMVhuKhBGOzcudPBRf/9999mzZp16dLFceeFCxei8sak5xOqhMnxVFTQqlWrxHLRaEk7uvAuFcQ7V65csXT9ky6ly1POlxUOHDgAqZs+fXpKF+T/I1HtFXuFvAIwa9aszz//PFGPyMz5rl27kqlI3ti4cePy5ctj+caDBw+OGjXq999/j3rO+/btu0w6WnIj9q3mRgSqHkukSLfipYcPH3an//nn+VWr9n388feffbZr27ajeFMk/vrrmd27zZITg/AwXNQgDP7++28HFw2FF198MemO+/bt2/v165fETFId+vbtm1guGhVpRxd+2q5s2bIxc/3j4+OT6M1cndqYqpHYfhFLhbwCIItHMmXK9Ndff/l/SmbOK1WqlHwFC/XevHnz8upXXnkllu9t2rQpL+3Vq1cU81y3bl2FChXItkiRIlHM9jJESrWaA5GpeiwR+2717bffNm/e3LGj4dix0889Nyt9+ndvv31grVofNW36aalSY7Nnf6969akFCgwbPHhdzIpnkHoRfS76ww8/fHMpfv75Z/mJLs2Qv2bNmi+//HLbtm1//vmn+/GjR4/yyKlTp6JeMIPI4JOLjhkzhtu4OSnvOnny5D333PPWW28lJZPUiMRy0ahIO7rw2XYxc/03b96cMWPGpUuXRpzDVauNqRcR9IuriotGa8lJ165dE/WUzJx//PHHSXy7Hzjq+MEHH8Se1XzxxRc1a9bEyUl6Vnp10NKrgYtaKdRq1qXSjkzVk6kwQVNi2a3A+vXrq1at6tjBNHv29mzZ+l9/fZ9p077V0zdsOBgXNzIQ+L/evVfFpngGqRrR56Jr16794lLIME8vWrduHZcrVqxYtWoVf6xevfr06dP6s3/88QeJ/HTixImoF+wKBnJbtGjRsGHDEhISkDNMfvv27aQzFq6zIeEAXLR1F7F//349hz///HPu3LkjR46cP3++Q/hBuShv4Y3KKs2aNSt9+vTcRvOR+W+//bZx40b1ru+++05uO3TokKT8+OOP7lr8/vvvjz76KJk0btyYe7Zu3Srp58+fX7hwIX9QZnzNPXv2qEe2bNkyceLECRMmbNq0yZGbo4SSsnjx4l9//ZW/v/nmm7Fjx7rPCnI/hTDnzJnDH+fOnVu2bNm4ceP27t3rLvyRI0dmzpxJSai4T4cPOSPz8ePHI42gXJSRZvr06YzKdBmEoNLd0pb0f/755/PPPx89ejRP/fTTT37KkFiEekWotnMjlOtPiyCK2bNnI0nHTx7KadmSnzFjxkcffYS2q7VD6H/u3Ll5EZ2C8nhII+k1suxlS9g9NIpyHjx4UM9E9QJeRAqvUCmyiklw/PjxL7/8kj+++uortMhjdR+aIAVesmSJsp9UfJ0GDMLOnTvlbwSrnkUz6Ur8Kqbgww8//Prrr92vQKM+++wz+hrOhxQ7bDnpJnQcx52YI8sOQVJg+indX37i7XQ9xKWXzc/b6RFytBhqgAc2depU6qJ+jaxfXD1cFDt8Ze9IFzRq1Ei/xDKk+AxbxKCLrVy5Ul3+8ssvVwkXTZFWc0g7ZYFtd1ffoduxBF5Kzpw5HZ7b2rX706TpkSVL7127gizEPXr09O23D3zrrcv6kEuDywRR5qL4OjBJ3PFfNcj8J3SIn/DY8KVwwr7//nsulYeHK4B3ouir4aL+MWnSpHvuuQdXD7GPGDGiYMGCOXLkgNtYtuP78MMPY9Nfe+01y24d5F+xYkVS3njjDZUDLhpUk/9hdA0aNMDiwPHUrw4uSsO1bt06e/bsJDI0WjZVeOedd6677jpSunbt2r17d+6BPsl5PE899dTu3bvlWdzT5s2b33333UF3OCxYsOCJJ56QQ1DIBO6xefPmli1bkg9vp3Y33HADvz7wwAOWPWdVuXJlMqfMlDxr1qytWrUKVUIc5fbt22fLlo0UCvbkk0/my5cvY8aMXA4dOjTUU/CZ+vXrcxvvxY0rWrRogQIF0qRJQ00Ro6MJ+BXPe/LkyTfbQOzUBV85VKvRXoULF+b+5cuXI/P77rvPwUVff/31uLg46Q5UuUyZMtIpgkrbsh3NvHnzduvWDUrWv39/nHIy96VAvuHxCnfbhcrE7fpDUZAz2Q4fPrx06dJUbcqUKepXb+WEnd5///2LFy9Go/g1T548kk4B8Nh40QsvvEB5KF7y1Wjp0qU0JYWH8Lz55pvp0qVr166dhDPgqJQ8YEPMIEwVjwctIoVfSYG+1q5d+9prr33mmWegZ3Jzx44dg74LxatVq9bAgQPfe++92267ja4kdA5O+MEHH/BqnqUMZ86cwWlAmakCjE6EjGcj6g2ZLFGiBG+Udz333HPnzp1Trxg/fjzNgSXBRGTIkKFSpUoSvglVToRfr149uglWSHJYtWoVXYzC0DQUGO0tVaoUzXrNNdfAn+mAiOvBBx+86aabyEFva4+3Q3RpCO6vWbMmLJSGvuOOO7ik+YQPR9wvrhIuisHEfCGWlC5I8kLm0/SU1MtFZWUH9l+lGC6afHBLO2WBGcSL0FPcuh0z/PPPP9hJRhY98fz5C0WKjAgE/u+991aHenD8+E3t2y9M/gIaOIHT++233zLWMwTjyrrXmTMiyMJVPb7AU3QEnmIQx+NS8dwYIMqaTU3ozIp76MAV4CdFQnCsxc8WGSGRNTYMF00UxowZkylTJrUKGjRp0gSDJVzUsp1yxUUFH374oc5F//jjD7zGRx99VC4PHz7Mr9WqVVP3O7goGrxnzx7cRMXZBNzgWB0HsyIF/1UvMMXDFw9VHbG2alUkXiaUgJTrr7++S5culI3/pWo4weJVy51QVi6/+uqrUCWEh+MQk1KhQgVxUrkHxxqeKRoY9Cm6Ytq0aZFPw4YNxeXFdeaGqlWrqjJv3bqVG5TAcZSFMNOldfnoiI+PZ9g7cOCAXP7777/lypXTuajUumfPnnIpfAb64SFt3kgx1FRbwYIFb7zxRn02NenwfoWj7ULB4fqT2yOPPKLOh8CAwOSRudwQVjlvv/12FU2gJA899JD6CcrEzd5rdJNeIww998ybN0+ljBo1ipRnn31WpUgQRN+SAI1UXPT48eOdO3fmkrePHj16586djRs3lhlFB44dOwbfU3t1Vq9ezVN33XWXKnCvXr1IqVOnjvwKeVNT9Cj53r175ZweuuSGDRtwL+g+WbNmJaV3795y2/Lly2kO9UbJ8Pnnn/coJ+min4qLWnYchxSYITlI8bDqpNx5551NmzaVHof+I3wIknrK4+0AIXOJMOGcUq/mzZuTAsNUj0TQL64wLkpNV65ciY1FmEePHpWRVE3yI/x169bho6j7V6xYQS9DOXlEwhYCzNd/beihHwHiXbhwoWivnoK15O1ff/312LFjN27c6HiKrr148WJHilpysmTJkvHjx+/bt89dI3SJss2YMSPoahodamJcVgRI3XVWc+jQoWk23OsO9u/fz50oNk6Yw2/zUzs3yFCXJ8C3E8lTEWpE39FXRrhrLSs7GMGpi0hG56JIj2FCltW4H6ec48aN++STTzAa3uUkn88++0xlOGnSJHcr0N1QJ4Qzc+ZM3dkQ4NTRfagLr6NB1VoGMvz0008pPzV1CFxEyg2IGq8Pn8SxsslPq6E2smCKAuMIqSUP3qU9e/Ys9Z04cSI2kJzFVgSVthVM1QW8ixJS7KArO3QE7Y8KGE/MGhqF66KUAQF26tSJwhQvXlw0mRoF1W0rJt3KuujVONR+6ND1EFH+HT9+JtSDf/114YsvfnIk/vjjiWnTvp00acsPPzipzqZNh7/99ojcM2HCpoSE3e4+QsqXX/48evTXCxbsPnbstGXgAt6sLD6V/wG2yLH+HBMhP6nh4MyZMwwHpKCx6sGYfe0sylz0yJEjlB7aidZiYhjG1Boq/uYntcCSwU+qqrtoMq1quKhPIKVbbrnlpZde0hP79eunc1GcCQcXlRTFRVE1/NFXX31V3QA9w8FVl0HX6OLSheWitOxNN90Er1DjATYdL9yxMFuH2/vHnpICRXQ81aNHD3xKNfwMHjyY2+B4HiXERydFPxavdOnSpPzwww8eT8nsrjKIeLFcUgt1A/RY5zwMrgiQAoeqIx0eSoAfryfiXutclNzw4xlK5RK/kF+h8ep+t7Rx4hm6VDlr1qzJDe6ROCnwfkVkXJSREj75twaYEjfIacbeyok6ycS78n4og7rTDxdNeo2KFi2qK4NlexJ58uThQXVskszg6YZOUpSLs2jRIi7LlSvn8SLwwgsvNGjQQJeVKCcOh9yA/bz//vtJQXMomNvJkHCMvo1NnAz4P0Kg5HBFHCyVP0abX+nCMs0bqpyYfQcXlaZxSEZWIuiOPoVUkgn7dootsST1OE6YTlatiPrFlcRFsU4VK1ak7+zevRt/FAuJB29pk/wPP/xw9+7dUWxMXNeuXfPnz08iboosIsBqYZ3wYypVqoS1xOxMnToVG96+fXvJX188IvPVOL7t2rWTiAbuS9WqVclTInp42PIUzVS3bl1aX03o4QfTPbkNBd66dWtcXFyBAgUk5qhzElqN11WvXh0PiWJLLOPxxx+nLrrRFugT491tSJsqVkN9KSfWQyI4KuTPWxgfixUrxlvos2gLUkIIPmvnAGoML5LlSGpab9iwYSLqoUOHMvJiH2RRAN05VFOqlR2NGjWiLkK6FBedO3dutmzZChUqlCZNmkyZMqmYrGWHeJAtjwwfPpz+niVLFmhM0FfQ7k8//TTVwRxRO4okayXSpUtHFdRt9Lu7774b2fJHz549uUcGJjoyr5DugzSeffbZgA0ZYRE7nRHzAlujPDA92aojCzQkPLd69WrErhZoqChV2FZDM3F7UB4sDJQStVGWIVRpBZhENG3KlCn80b9/f56SbR1uabtVXSBLZ6ksHFJWuKAV9JqgEg7VHwUitBEjRnTs2JFyotVCtnk1r+C9tItoMgVw63ZsupUAm48oHLTwkUfwJP8vd+6BQR8JIZAL7dotfOWV+aNGfVW/PkPP/3XpskyyHTZsff78Q0mB4r7xxpI8eQbddFNfLhs0mK3nAO/9z3/+27nz0s8/31u37oxrrukRFzfyiSemPP30DP/FuOJBc0Ojdu7ciUvAWLxu3Tr6mj7JSTfkBpn8U1wUpeKSDsUAih2jl3EZdBdPciDKXHTv3r1CJiHWwrCBdDB6o9RTHEdIqfyqC8hw0URBZjjHjRunJ8pspH8uamkb4hmAR40ahVnE+qtfg3JRMdzeXBTgx5OoXBlGJp1QueH2/j1OTlLFRqkqV67MbZh1jxIKF9UX4WB/SdE7m/spcff19yIfRgV12bBhQ27QF/7hAWTOnDlUzHv27P/H3pnA2Vj9f/zaQmSLEH727GUN0T9LlkSl8pMQoiTZEiUqZJClEDKYspZlbBn7kiX7EpGtGfuSJfu+3f/b/eb8jue597l3Zu6MpfN5zWte9znPec6+fD/nfM/3THFpusEC+3lRlTvkZsgYb5Eb1Ft7aQuXkA+nTZuWO3duPKiTukGBcxQx46IQCRpbDRvUnrBz43z66acJDb4he906AuGiscyRGFq036vZrl07l0dXVh79clESySMJdkiq27ObCt+zl9X06dOVH+YVWT7XabmCFJcucNCEkJCEnuHOj7Jly9qjEFrrK52ISoFwUXujlcYgC5R+YxcuquutMcXiggeHKPz2iweJiw4bNozeoZZmGA+VEoo0ZqWjK1rcadOmxZERbP/+/XiQBbL27du7PNsv4hNHtX5BH2QelwamBHQKtmTJkrg899xzSD9uj150okSJ4BsyBp44cQJO67pTuVRUTujOhC/Ej8RbRjlR6kEkkscmTZpIf8TF1xXQ0gB0F2E1mTNnJjRJD3wDF2UfOyIiQp8xR40axSMsK8DcWYDjsWPH3nvvPdedKqZMgrjADWQTktFA2KnDEC0jmF1HN1WqVM2bN5fRg/rFpVq1aip2KBnEUh6Ro+CiFLLXA/OEIKtL8BnkAfxcvnyZNiPMUO2HlyhRQl9ahRCSd9oYJQORkyM/jIE0GGFHjIqIfBQR06t8snfvXtdtfQ3YJg1PqgnPTL4ERR6FnKtp0bnWlMIUX9EeEKw7dOjw9ddfO6RWHuvWrasratHYlPUHS2l7bepuz4Ig7VA9ytrWgAEDvNagQ39kLNXt38qKttpXECNVFh1dS9uOt25FOAkTJqSiLe6PPgqZ/6JSpVH2T65evX7u3BX9D3bjviUQLuzefYny9swzIwnhp5/+WRtt23YOj3nzDpo585b6JF8JO9269aj6BP6ZNm3vGzduNYnr12/gGQ/Tpm2X3VQDt2fnX+zy+LL/jPvy5cs3b94sJyUVF12/fj2Pagmb3i3hOKhvBBFB5qJkg8GFPkz3QyCQvIkag9r/ZcwSd52pCgwXjRaEosjcphADLur2zBZMloxH1B1THQRMvYoNF2VWZp6DmEktv/LKK2qa9IpocVF6yI8//shIyrzVp08fXYDwmsI44qKik1mnTh3lki1bNjUN29G9e3eX7ZicV9tFK1eubNas2TfffLNo0SI1lwu8ljbyDVN1ixYtli5dKnOkSJAvxRokwzkKd0y56JNPPlm8eHHnTxwaJzQmZ86cLs/uGd1B3zwPhIvGMkciyRUrVsziTjvEvWbNmvIYFC5KD7J0ZF8Q/S6kYfsrOxcFclZ57dq1UDX7eKIjjrioNAa/sceMi7odq9j9YHFRmgd5UXsgtBl1F6WFiwpKly7t8hyh1x27du2KiK+M28nQpO+tCZ/XBXQZWvWxXXa81UB68OBBl+2gIx0ZGVcJOojRllZUpkwZ+rXyIGreb7/9tkMJ+OKiagQDCxcudGnb6fPnz2c8F7VG9+1G1bJly8BzZ4cc5dC5qIwJDP7K5YMPPsCF5PkKxBcX1dXaESsTJEigOtqIESOyZ8+uq07IKm3Pnj29RnH27Fn79CqrD2rPFhIOwVNvZdJUmnsff/wxj7QZPQTeUrn6YMWkWahQIfXImGnpdLIEkCVLFnn0W2uiMJU8eXILfXJOLXMN7FSJl1S9krztpe22NXUaCY+63UeE2woVKliUsRV89UcEXYQEeKmqJjlwQXZk7TUQLuqOr24l4sfrr79ucU+YsCs8sEmT6fZPtm07BueUjU3+3ntv5o4dx7dvP54oUbeoqJPwUvkLCVnG2ypVxshX3367hkedrH7wwSydrF68eJVIK1b8H/v9/PPFeBg71smy4L8Nop26YsWKM2fObNu2jcmOFqvzyR07djAV0nEsXJSmgsSuxBLZO3WW2IOIuD0JLYVCtqUgyCd0XFx27twptFNXbzBcNFpgdHB5TjjojjHgoqGhoYyMyo5UELkoQASU9DAQ67ORVwTORQ8cOMAc0Lx5c4lRdHTvChdFGoCIIhAMHz6cCXLSpEkwDa8nNPQCsdBOCxclHLwhKcokKjq6zlyUngUrGzPmn2Fdl7m/iTXCwsKco3DHlIsiGSD4Olgedm6cbo84hVTH7EuwBQoUUGJHIFw0ljkSASJ9+vQWdzk/qQSpoHDRffv24adWrVoOftyeloOokSlTJjvHcPvgonJpIUPu6NGj+SHbC14Rp1zUb+wx46LOVex+sLgoTN7lUckbOHCg16tNLFxU8m5XzFPfKlt3UAX1lor2ykV1TVFLqXo1uiNCs3q0D/Wi665OPEoz04dBO3xxUZ0WynCq9hL1/O7evVvGZ/0Mhd/c2WGPVLioUvdw31Ya8qq/IPDFRS3FqB8JqVu3LsORXbPAl/1kBiWXRxdUdxRyAt+Wx5seuD0VFB4eDtflrZrgJBdwYEvIqkhPnz6NiEJF86F6K0cJ9N1aRgxRfhZFOb+1Jq3FMsL4Ta2QQxim6Dzr8MpFLU29YcOGulaOX/jqj5AB3GlF9poSY+MBctH46VY//vijS9uz1cL5Gh5Yo8Y4r1+Bzp0hsV/kyvXPpvGwYesSJOiKf8tfw4b/LAMJF/3yy/+ZMv7004W4fPfdPxLa7t0neSxQ4H/qb5Mn/4ELH/pKw78QyMYW1VSg1BwgqDxK17NwUR0IEnLviVc7o3GBIHNRWeNRFJxWLpu8SkuBV5BPHs+fPy+v9C5quGi0IAOrZQMkulxUzlzpt3IHl4tGRUUxMiIcMyEpEym+EDgXReDWL6G+i1zU7TlD8vzzz7dv375169ZwJ1+nRwT9+vVz3XnIzW3jomIkBqojj3656NGjR1OnTq3r/Nhl7ljCbxQx46JiUiUiIsLi7eeff0ZOcm6cDJdKw40fhQoV0svQLxeNfY4Y1l0eWE5mDho0yKVpjAeFizJm0vAQ1+y2BPQzSPR0YhczP7ly5bI0Ra9cFKqWNWtWt4e2uTxmtyw6OZSz7BrFKRf1G3sMuGgg/eJB4qLu28p+gO6gBhB3NLkojW3s2LFNmjSZNGkS9Ak/zBrqbbxx0ddeew0XWQhze/TPeWSod8h+4FzUorpC4ps2bQpngKW4POcGA8+dHfHMRRkZ5Dev6OO+ArTDKxeV3bYMGTIol7Nnz/bs2ZPs0KJk0lQ00hcXdXuIfZs2bTp37szwSAr1WOxc1H17E1Kuo/Nba764qHNqmallo9jl0VvRdzgD4aJFihRRptoDhNf+KKf07XxYIU65aHS7FT7x0KpVK4t7lSpjRKXW14dDh67FQ/Hiw+Tx/fcjeLx0yeflz3656LVrNzJlQr79IjLyn5N9gwbdsp+0YcNhX2H+CyFXlgiNvHjxoqjaihUi5t
```

---
