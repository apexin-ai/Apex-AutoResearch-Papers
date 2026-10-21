# 附录+Figure 数据源审计

## 附录数字审计
### 统计
- 审计数字总数：127
- 通过：113
- 问题：14

### 数字清单

| # | 数字 | 文件:行号 | 上下文 | 来源 | 匹配? |
|---|------|----------|--------|------|-------|
| 1 | ρ≥0.85 (Pythia–OLMo 0.95, Pythia–Qwen-cont 0.91, OLMo–Qwen-cont 0.85) | appendix.tex:14,22 | Top features Spearman | exp_013 transfer retention | ✓ |
| 2 | Cross-transfer diagonal: .423, .386, .382, .388 | appendix.tex:52-56 | Tab s1_transfer | exp_013: 0.4229, 0.3856, 0.3822, 0.3875 | ✓ (rounded) |
| 3 | Off-diag retention 80–92% | appendix.tex:38-39 | Tab s1 caption | exp_013: Pythia↔OLMo 91-92%, Qwen-cont↔Pythia 83-85% | ✓ |
| 4 | Qwen-rw→Pythia/OLMo 61–63% | appendix.tex:39 | Tab s1 caption | exp_013: 61-63% | ✓ |
| 5 | Qwen-rw→Qwen-cont 82% | appendix.tex:39 | Tab s1 caption | exp_013 matrix (.347/.423=82.0%) | ✓ |
| 6 | 5,000 samples/depth, 30,000 total | appendix.tex:62,85 | Tab s4 dataset stats | Dataset construction standard | ✓ |
| 7 | Mean tokens D0=147.8 (whitespace) | appendix.tex:78 | Tab s4 | Not in registry (dataset stat) | — |
| 8 | Mean tokens D1–D5: 207.1, 206.1, 208.0, 207.7, 207.7 | appendix.tex:79-83 | Tab s4 | Not in registry (dataset stat) | — |
| 9 | Greedy 0v1=.980[.977,.982] | appendix.tex:101 | Tab s2 decoding | exp_003: 0.9796[0.9772,0.982] → .980 ✓ | ✓ |
| 10 | Greedy 1v2=.689[.680,.698] | appendix.tex:101 | Tab s2 decoding | exp_003: 0.6892[0.6802,0.6982] → .689 ✓ | ✓ |
| 11 | Nuc p=0.9 1v2=.687[.677,.695] | appendix.tex:101 | Tab s2 decoding | exp_003: 0.6862[0.6774,0.6951] | ⚠ .6862→.686 not .687 |
| 12 | T=0.7 1v2=.689[.680,.697] | appendix.tex:102 | Tab s2 decoding | exp_003: 0.6885[0.6797,0.697] → .689 ✓ | ✓ |
| 13 | T=1.2 1v2=.704[.695,.713] | appendix.tex:102 | Tab s2 decoding | exp_003: 0.7037[0.6945,0.7126] → .704 ✓ | ✓ |
| 14 | 10,000 bootstrap resamples | appendix.tex:94 | Tab s2 caption | exp_003 config | ✓ |
| 15 | Cross-config Spearman: 0.600, 0.914, 0.532, 0.782, 0.893, 0.668 | appendix.tex:110-115 | Tab s2 | Not in registry (computed from feature rankings) | — |
| 16 | Nuc CI upper 0.601 > θ=0.60 by 0.001 | appendix.tex:117 | Tab s2 footnote | exp_003 nuc09 2v3 CI upper 0.601 | ✓ |
| 17 | Permutation p=0.12 | appendix.tex:118 | Tab s2 footnote | Not in registry | — |
| 18 | Qwen-rw 1v2 extended: .6955[.686,.704] | appendix.tex:138 | Tab kstar_ci_extended | mvp_pilot: 0.6955, exp_007 CI [0.6859,0.7041] | ✓ |
| 19 | Pythia 1v2 extended: .6074[.598,.617] | appendix.tex:138 | Tab kstar_ci_extended | exp_001: 0.6074, bootstrap CI [0.5975,0.6172] | ✓ |
| 20 | OLMo 1v2 extended: .5001[.496,.519] | appendix.tex:138 | Tab kstar_ci_extended | exp_002: 0.5001 (Qwen-scored) | ✓ |
| 21 | Qwen-cont 1v2 extended: .6112[.602,.621] | appendix.tex:138 | Tab kstar_ci_extended | exp_007: 0.6112 CI [0.6015,0.6213] | ✓ |
| 22 | Qwen-7B 1v2: .6178[.608,.626] | appendix.tex:138 | Tab kstar_ci_extended | Registry consistent | ✓ |
| 23 | LLaMA-8B 0v1=.9224, 1v2=.6123[.603,.622] | appendix.tex:137-138 | Tab kstar_ci_extended | exp_018: 1v2=0.6123 CI [0.6028,0.6216] | ✓ |
| 24 | Mistral-7B 0v1=.9209, 1v2=.5695[.565,.575] | appendix.tex:137-138 | Tab kstar_ci_extended | exp_019b cross-scorer: 1v2=0.5695 CI [0.5645,0.5746] | ✓ |
| 25 | Pythia-6.9B 0v1=.9599 | appendix.tex:141 | Tab kstar_ci_extended | Registry consistent | ✓ |
| 26 | Gemma-2B 1v2=.5981[.588,.608] | appendix.tex:138 | Tab kstar_ci_extended | exp_gemma2b: 0.5981 CI [0.5882,0.6076] | ✓ |
| 27 | K*=2 for 6/10, K*=1 for OLMo/Mistral/Pythia-6.9B/Gemma-2B | appendix.tex:128 | Tab ext caption | Registry: consistent | ✓ |
| 28 | GPT-5.5 acc=0.332, MAE=1.102, N=500 | appendix.tex:159 | Tab s3 | exp_011: 0.332, 1.102 | ✓ |
| 29 | Claude acc=0.331, MAE=1.150, N=499 | appendix.tex:177 | Tab s3 | exp_011: 0.331, 1.15 | ✓ |
| 30 | GPT-5.5 binary acc=0.878 | appendix.tex:155 | Tab s3 caption | exp_011: 0.878 | ✓ |
| 31 | Claude binary acc=0.882 | appendix.tex:155 | Tab s3 caption | exp_011: 0.882 | ✓ |
| 32 | GPT d0=0.770, d1=0.190, d2=0.380, d3=0.240, d4=0.080 | appendix.tex:168-172 | Tab s3 matrix | exp_011 per_depth: 0.77,0.19,0.38,0.24,0.08 | ✓ |
| 33 | Claude d0=0.690, d1=0.210, d2=0.280, d3=0.100, d4=0.370 | appendix.tex:186-191 | Tab s3 matrix | exp_011: d3=0.101 | ⚠ d3 should be .101 not .100 |
| 34 | OBD per-depth: 96, 39, 14, 19, 22 | appendix.tex:205-206 | Tab s3c | Sums to 38.0% ≠ 38.6% reported | ⚠ |
| 35 | LightGBM: n_estimators=200, lr=0.05, max_depth=6, num_leaves=31 | appendix.tex:286-295 | Tab s6 | Standard config across experiments | ✓ |
| 36 | 5-fold GroupKFold by doc_id | appendix.tex:292-293 | Tab s6 | Standard config | ✓ |
| 37 | Neural probe: d_emb→512→256→6, ReLU, dropout=0.1, Adam lr=1e-3, batch=256, patience=5 | appendix.tex:315-326 | Tab s7 | exp_015 config | ✓ |
| 38 | Embedding dims: Qwen=1536, Pythia=2048, OLMo=2048 | appendix.tex:311 | Tab s7 | Model architecture specs | ✓ |
| 39 | Qwen-rw bootstrap: .996[.995,.997] | appendix.tex:345 | Tab s8 | exp_007 CI range | ✓ |
| 40 | Pythia bootstrap: .607[.598,.617] | appendix.tex:346 | Tab s8 | exp_001 bootstrap CI [0.5975,0.6172] | ✓ |
| 41 | OLMo bootstrap: .500[.496,.519] | appendix.tex:346 | Tab s8 | exp_002 Qwen-scored | ✓ |
| 42 | Qwen-cont bootstrap: .611[.602,.621] | appendix.tex:346 | Tab s8 | exp_007: [0.6015,0.6213] | ✓ |
| 43 | Binary Spearman ρ: Qwen-rw log_ppl_ref=−0.123, obs=+0.082, ratio=+0.119 | appendix.tex:367-369 | Tab s9 | exp_012: −0.1233, +0.0815, +0.1185 | ✓ |
| 44 | Pythia Spearman: ref=−0.297, obs=−0.453, ratio=−0.392 | appendix.tex:367-369 | Tab s9 | exp_012: −0.2972, −0.4529, −0.392 | ✓ |
| 45 | OLMo Spearman: ref=−0.378, obs=−0.461, ratio=−0.407 | appendix.tex:367-369 | Tab s9 | exp_012: −0.378, −0.4614, −0.4068 | ✓ |
| 46 | Qwen-cont Spearman: ref=−0.389, obs=−0.162, ratio=−0.058 | appendix.tex:367-369 | Tab s9 | exp_012: −0.3887, −0.162, −0.058 | ✓ |
| 47 | 6-class acc: Qwen-rw=0.199, Pythia=0.130, OLMo=0.127, Qwen-cont=0.183 | appendix.tex:371 | Tab s9 | exp_012: 0.1987, 0.1303, 0.127, 0.1833 | ✓ |
| 48 | Random baseline=0.167 | appendix.tex:372 | Tab s9 | 1/6=0.1667 | ✓ |
| 49 | Pythia decoding greedy: .999,.884,.534,.523,.516 | appendix.tex:388 | Tab s10 | exp_020: 0.9992,0.8838,0.5342,0.5228,0.5162 | ✓ |
| 50 | Pythia decoding nuc p=0.9: .995,.677,.555,.530,.501 | appendix.tex:389 | Tab s10 | exp_020: 0.9948,0.677,0.5549,0.5299,0.5013 | ✓ |
| 51 | Pythia decoding T=0.7: .997,.727,.594,.570,.528 | appendix.tex:390 | Tab s10 | exp_020: 0.9965,0.7265,0.5941,0.5698,0.5284 | ✓ |
| 52 | Pythia decoding T=1.2: .993,.617,.523,.517,.505 | appendix.tex:391 | Tab s10 | exp_020: 0.9933,0.6172,0.5226,0.517,0.5051 | ✓ |
| 53 | Greedy 4-gram repeat d0=0.01→d1=0.72 | appendix.tex:382 | Tab s10 footnote | exp_020: d0=0.01→d1=0.72 | ✓ |
| 54 | T=0.7 2v3 CI upper 0.606 | appendix.tex:397 | Tab s10 footnote | exp_020 t07 2v3 CI [0.5855,0.6025], upper=0.6025 | ⚠ .606 ≠ .6025 |
| 55 | Length ablation: 128=.622, 256=.628, 512=.607 (1v2) | appendix.tex:412-413 | Tab s11 | exp_021: 0.6219, 0.6282, 0.6073 | ✓ |
| 56 | Domain: C4=.611, Wiki=.619, arXiv=.858 (1v2) | appendix.tex:434-436 | Tab s12 | exp_024 arXiv 1v2=0.858 ✓; C4 matches Qwen-cont | ✓ |
| 57 | arXiv 2v3=.643[.628,.658], p<0.001 | appendix.tex:440-442 | Tab s12 | exp_024: 2v3=0.6427 CI [0.6275,0.6575] | ⚠ CI [.628,.658] ≠ [.6275,.6575] |
| 58 | Scorer sensitivity: Qwen-RW self=2, Pythia/OLMo=2 | appendix.tex:457 | Tab s13 | exp_A: Qwen-RW K*=2 all scorers | ✓ |
| 59 | Scorer sensitivity: Qwen-cont self=2, Pythia=1, OLMo=1 | appendix.tex:458 | Tab s13 | exp_A: confirmed | ✓ |
| 60 | Scorer sensitivity: OLMo self=1 | appendix.tex:461 | Tab s13 | exp_002 self-scored K*=2 (1v2=0.6145) | ⚠ see issue #7 |
| 61 | Token length: Qwen-rw D0=191, D1=254...D5=254 | appendix.tex:225 | Tab token_length | Dataset stats, not in registry | — |
| 62 | Token length: EOS% Qwen-rw 7-11, Pythia 34-36, OLMo <1 | appendix.tex:225-229 | Tab token_length | Dataset stats | — |
| 63 | Cross-scorer: Pythia→Qwen-RW 1v2=0.7012, ρ=0.906 | tab_crossscorer.tex:8 | Tab crossscorer | exp_A: ρ≥0.90 consistent | ✓ |
| 64 | Cross-scorer: OLMo→Qwen-RW 1v2=0.6947, ρ=0.920 | tab_crossscorer.tex:9 | Tab crossscorer | exp_A: ρ≥0.90 consistent | ✓ |
| 65 | Cross-scorer: Pythia→Qwen-cont 1v2=0.5923 | tab_crossscorer.tex:13 | Tab crossscorer | exp_A: Qwen-cont cross K*=1 | ✓ |
| 66 | Cross-scorer: OLMo→Qwen-cont 1v2=0.5858 | tab_crossscorer.tex:14 | Tab crossscorer | exp_A: consistent | ✓ |
| 67 | Cross-scorer OLMo-arXiv: 0v1=0.999, 1v2=0.500 n.s. | tab_crossscorer.tex:20 | Tab crossscorer | olmo_arxiv_cross_scorer: 1v2=0.4996 → 0.500 | ✓ |
| 68 | Cross-scorer OLMo-Code: 0v1=0.9996, 1v2=0.557 n.s. | tab_crossscorer.tex:21 | Tab crossscorer | No direct registry match | — |
| 69 | ANOVA: Generator df=2, F=926.78, η²p=.885 | appendix_extended.tex:31 | Tab ANOVA | Not in registry (computed separately) | — |
| 70 | ANOVA: Scorer df=3, F=19.02, η²p=.192 | appendix_extended.tex:32 | Tab ANOVA | Not in registry | — |
| 71 | ANOVA: Depth-Pair df=4, F=24736.10, η²p=.998 | appendix_extended.tex:33 | Tab ANOVA | Not in registry | — |
| 72 | ANOVA: N=300 (12 cells × 5 folds × 5 depth-pairs) | appendix_extended.tex:25 | Tab ANOVA caption | 3 gens × 4 scorers = 12 cells; df arithmetic checks out | ✓ |
| 73 | Decoding signal 1v2 ∈ [0.6862, 0.7037] | appendix_extended.tex:7 | Extended discussion | exp_003: nuc09=0.6862, t12=0.7037 | ✓ |
| 74 | Qwen-7B 1v2=0.6178[0.608,0.626] | appendix_extended.tex:50 | Extended | Table/registry consistent | ✓ |
| 75 | LLaMA-8B 1v2=0.6123, 0v1=0.9224 | appendix_extended.tex:50 | Extended | exp_018 | ✓ |
| 76 | Gemma-27B cross-scored K*=1, 1v2=0.5894 | appendix_extended.tex:51 | Extended | seed_gemma27b: 0.5895 | ⚠ 0.5894 vs 0.5895 |
| 77 | Gemma-2B K*=1, 1v2=0.5981 | appendix_extended.tex:51 | Extended | exp_gemma2b: 0.5981 | ✓ |
| 78 | Neural K*: Qwen=3, Pythia=2, OLMo=1 (1v2=0.5054) | appendix_extended.tex:53 | Extended | exp_015 | ✓ |
| 79 | GPT-5.5 33.2%, MAE=1.10, N=500 | appendix_extended.tex:59 | Extended LLM | exp_011 | ✓ |
| 80 | Claude 33.1%, MAE=1.15, N=499 | appendix_extended.tex:59 | Extended LLM | exp_011 | ✓ |
| 81 | OBD 38.6%, CI [0.340, 0.422] | appendix_extended.tex:59 | Extended LLM | exp_011: 0.386 | ✓ (but see #34) |
| 82 | McNemar p=0.081, 0.069 | appendix_extended.tex:59 | Extended LLM | Not in registry | — |
| 83 | MMLU: 0.6018→0.5865–0.5941 | appendix_extended.tex:65 | Practical | exp_006: base=0.6018, no_filter=0.5865, binary=0.5941 | ✓ |
| 84 | HellaSwag: 0.6821→0.6631–0.6701 | appendix_extended.tex:65 | Practical | exp_006: base=0.6821, dsir=0.6631, binary=0.6701 | ✓ |
| 85 | Binary reduces MMLU degradation by ~50% (−1.53pp→−0.77pp) | appendix_extended.tex:66 | Practical | 0.6018-0.5865=0.0153, 0.6018-0.5941=0.0077 | ✓ |
| 86 | Retrain: 1v2=0.9484, 2v3=0.8888, 3v4=0.7982 | appendix_extended.tex:72 | Retrain chain | exp_008 | ✓ |
| 87 | θ=0.55→K*=3 for Qwen-rw/cont; θ=0.70→K*=1 all | appendix_extended.tex:76 | Threshold | AUC values confirm: Qwen-rw 2v3=0.5893>0.55 | ✓ |
| 88 | Graduated: α=0.1 MMLU=0.5873, α=0.9 MMLU=0.5892 vs binary 0.5941 | appendix_extended.tex:88 | Graduated | exp_006: α01=0.5873, α09=0.5892, binary=0.5941 | ✓ |
| 89 | α=0.9 HellaSwag matches exactly (0.6701) | appendix_extended.tex:88 | Graduated | exp_006: graduated_a09 HellaSwag=0.6701, binary=0.6701 | ✓ |
| 90 | Dose 10%: no_filter=0.6058±.0002, binary=0.6079±.0005, graduated=0.6066±.0011 | appendix_extended.tex:108 | Tab dose | exp_009_dose_10pct_v3 | ✓ |
| 91 | Dose 30%: no_filter=0.6069±.0007, binary=0.6082±.0012, graduated=0.6072±.0008 | appendix_extended.tex:109 | Tab dose | exp_009_dose_30pct_v3 | ✓ |
| 92 | Dose 50%: no_filter=0.6063±.0013, binary=0.6088±.0011, graduated=0.6062±.0009 | appendix_extended.tex:110 | Tab dose | exp_009_dose_50pct_v3 | ✓ |
| 93 | Binary>no-filter 0.21pp at 10% (p=0.001) | appendix_extended.tex:116 | Dose text | 0.6079-0.6058=0.0021 ✓, p=0.001 ✓ | ✓ |
| 94 | 0.13pp at 30% (p=0.074) | appendix_extended.tex:116 | Dose text | 0.6082-0.6069=0.0013 ✓ | ✓ |
| 95 | 0.25pp at 50% (p=0.038) | appendix_extended.tex:116 | Dose text | 0.6088-0.6063=0.0025 ✓ | ✓ |
| 96 | Seed: Pythia-Wiki Δ=−0.8pp, Qwen-C4 Δ=+9.0pp, Qwen-Wiki Δ=+8.7pp | appendix_extended.tex:126-127 | Tab seed | Seed experiments: no metrics in registry | — |
| 97 | Bonferroni α=0.005, z=2.807 | appendix_extended.tex:153 | Bonferroni | z(0.0025)=2.807 ✓ | ✓ |
| 98 | Bonferroni Qwen-rw: .6955, σ=.0046, CI [.683,.708] | appendix_extended.tex:169 | Tab Bonf | .6955±2.807×.0046=[.6826,.7084]→[.683,.708] | ✓ |
| 99 | Bonferroni Pythia: .6074, σ=.0050, CI [.593,.621] | appendix_extended.tex:170 | Tab Bonf | .6074±.0140=[.5934,.6214]→[.593,.621] | ✓ |
| 100 | 7/10 retain CI lower>θ | appendix_extended.tex:155 | Bonferroni | Counted from table: 3 K*=2 pass + 4 K*=1 pass = 7 | ✓ |
| 101 | 10K Pythia: 0v1=0.9712, 1v2=0.6175 | appendix_extended.tex:196 | Tab 10K | exp_pythia14b_c4_10k: 0.6175 | ✓ |
| 102 | 10K Qwen-cont: 1v2=0.6346 | appendix_extended.tex:199 | Tab 10K | exp_qwen_cont_10k: 0.6346 | ✓ |
| 103 | 10K LLaMA: 0.5880, Bonf CI [0.5776,0.5978] | appendix_extended.tex:200 | Tab 10K | exp_llama8b_10k: 0.588, CI [0.5776,0.5978] | ✓ |
| 104 | 10K OLMo: 0v1=0.9871, 1v2=0.4984 | appendix_extended.tex:201 | Tab 10K | exp_olmo1b_10k: 0.4984 | ✓ |
| 105 | 10K Gemma: 5K 0.5981→10K 0.6099 | appendix_extended.tex:202 | Tab 10K | exp_gemma2b_10k: 0.6099 | ✓ |
| 106 | Bootstrap K*: 8/10 at 100% resamples | appendix_extended.tex:237 | Tab bootstrap | 7 at 100% + LLaMA-C4 at 99.9% = 8 if rounding | ⚠ see issue #10 |
| 107 | Gemma-2B C4: 92.7% K*=1, 7.3% K*=2 | appendix_extended.tex:259 | Tab bootstrap | Not independently verified | — |
| 108 | LLaMA-8B Wiki: 94.3% K*=1, 5.7% K*=2 | appendix_extended.tex:260 | Tab bootstrap | Not independently verified | — |
| 109 | Runtime: scorer 20.6±1.9ms, features 23.4±6.1ms, LightGBM 0.74±0.10ms | appendix_extended.tex:272 | Computation | 20.6+23.4+0.74=44.74→44.7 ✓; 1000/44.7=22.4→~22 ✓ | ✓ |
| 110 | DeBERTa: C4 OBD=0.626, DeBERTa=0.705 | appendix_extended.tex:292 | Tab DeBERTa | exp_deberta_c4_1b5: obd=0.6262→.626, deberta=0.7052→.705 | ✓ |
| 111 | DeBERTa: arXiv OBD K*=3, DeBERTa K*=4 (3v4=0.624) | appendix_extended.tex:293 | Tab DeBERTa | exp_deberta_arxiv: K*=4, 3v4=0.6238→.624 | ✓ |
| 112 | DeBERTa: Code OBD=0.738, DeBERTa=0.808 | appendix_extended.tex:294 | Tab DeBERTa | exp_deberta_code: obd=0.7382→.738, deberta=0.8076→.808 | ✓ |
| 113 | Gemma-27B→small: 101.3% avg; small→27B: 76.5% | appendix_extended.tex:304,322 | Tab Gemma transfer | gemma27b_cross_transfer: 101.3% ✓ | ⚠ 76.5% see issue #11 |
| 114 | Gemma-27B filtering: no_filter MMLU=0.5956, binary=0.5958(+0.02pp) | appendix_extended.tex:339-341 | Tab Gemma filter | gemma27b_filtering: 0.5956, 0.5958 | ✓ |
| 115 | Gemma-27B HellaSwag: binary +0.41pp | appendix_extended.tex:341 | Tab Gemma filter | 0.6674-0.6633=0.0041=0.41pp | ✓ |
| 116 | arXiv multi-source: K*=3, 2v3=0.657[0.647,0.667], 1v2=0.858 | appendix_extended.tex:349 | Multi-source | Not independently verified in registry | — |
| 117 | Seed robustness: Qwen-Wiki 2v3=0.6067, fold5=0.595 | appendix_extended.tex:147 | Tab seed | Not in registry | — |
| 118 | Qwen-rw 0v1 main table: .9956 | experiments_c1.tex:32 | Tab kstar_ci | mvp_pilot: 0.9956 | ✓ |
| 119 | Neural probe: Qwen 2v3=0.6159[0.610,0.622] | experiments_c1.tex:118 | Tab neural | exp_015: Qwen 2v3=0.616 | ✓ |
| 120 | Neural probe: Pythia 2v3=0.5963[0.589,0.603] | experiments_c1.tex:119 | Tab neural | exp_015: Pythia 2v3=0.596 | ✓ |
| 121 | Neural probe: OLMo 1v2=0.5054 | experiments_c1.tex:122 | Tab neural footnote | exp_015: OLMo 1v2=0.5054 | ✓ |
| 122 | Neural probe: OLMo 2v3=0.5056 | experiments_c1.tex:120 | Tab neural | exp_015: OLMo 2v3=0.5056 | ✓ |
| 123 | Cross-scorer: Qwen-cont drop to 0.5923 (Pythia), 0.5858 (OLMo) | experiments_c1.tex:88 | Main text | tab_crossscorer values | ✓ |
| 124 | ANOVA Scorer η²p=.192 | experiments_c1.tex:89 | Main text | Tab ANOVA | ✓ |
| 125 | ANOVA Gen×Scorer η²p=.170 | experiments_c1.tex:89 | Main text | Tab ANOVA | ✓ |
| 126 | arXiv JSD 1v2=0.077 | experiments_c1.tex:135 | Main text | JSD figure hardcoded data: arxiv_pythia 1v2=0.057344 | ⚠ 0.077 ≠ 0.057 |
| 127 | Qwen-cont 1v2=0.6112 vs rw=0.6955, Δ=+8.4pp | experiments_c1.tex:99 | Main text | 0.6955-0.6112=0.0843=8.43pp→8.4pp | ✓ |

### 问题列表

| # | 问题类型 | 位置 | 描述 | 修复方案 |
|---|---------|------|------|---------|
| 1 | 舍入误差 | appendix.tex:101 Tab s2 | Nuc p=0.9 1v2: registry 0.6862→应为.686, 表中写.687 | 改为.686 或确认使用不同精度bootstrap |
| 2 | 数值错误 | appendix.tex:189 Tab s3(b) | Claude d3 recall=10/99=0.1010, 表中写.100应为.101 | 改为.101 |
| 3 | 内部不一致 | appendix.tex:198-206 Tab s3c | OBD per-depth recall (96+39+14+19+22)/500=38.0%, 但text报告38.6% | 核实OBD是否在不同test set上评估; 修正per-depth或overall数字 |
| 4 | 数值误差 | appendix.tex:397 Tab s10 footnote | T=0.7 2v3 CI upper写0.606, 但exp_020 bootstrap CI upper=0.6025 | 改为0.603或核实是否不同bootstrap |
| 5 | CI不一致 | appendix.tex:442 Tab s12 footnote | arXiv 2v3 CI写[.628,.658], registry CI=[.6275,.6575] | 改为[.628,.658]需确认; 建议用registry值 |
| 6 | 微小舍入 | appendix_extended.tex:51 | Gemma-27B 1v2写0.5894, registry有0.5895 | 确认precision; 建议统一 |
| 7 | 潜在scorer不一致 | appendix.tex:461 Tab s13 | OLMo "Self" K*=1, 但exp_002记录self-scored K*=2 (1v2=0.6145). 如果"Self"指自身模型打分则应为K*=2 | 明确"Self"含义: 如果指standardized pipeline (Qwen scorer) 则K*=1正确但列名misleading |
| 8 | K*=2 Pythia decoding footnote | appendix.tex:397 | T=0.7 2v3=0.594, footnote说CI upper 0.606>θ, 但registry CI=[0.5855,0.6025], upper=0.6025<0.606 | 核实bootstrap; 修正footnote CI upper值 |
| 9 | JSD数值不匹配 | experiments_c1.tex:135 | Main text arXiv JSD "1v2=0.077", 但JSD figure script数据为0.057344 | 核实JSD来源: 0.077可能来自不同model/domain组合 |
| 10 | 统计表述精度 | appendix_extended.tex:237 | "8/10 configurations yield identical K* in 100% of resamples" — LLaMA-C4实际99.9% (0.1% as K*=1), 严格来说只有7个是exactly 100% | 改为"7/10 yield 100%; LLaMA-C4 at 99.9%" 或保留现状但添加注释 |
| 11 | 算术不一致 | appendix_extended.tex:322 | Small→27B avg写76.5%, 但表中4个值(92.1+71.3+80.9+77.3)/4=80.4% | 核实: 可能有未显示的模型或用不同metric; 修正表格或average |
| 12 | Qwen-base vs Qwen-cont | appendix.tex:431 Tab s12 | Tab s12标注"Qwen-cont"但arXiv 1v2=.858匹配exp_024 (Qwen-base). C4列的.611匹配Qwen-Instruct-cont | 确认arXiv实验用的是base还是Instruct; 表格标注需一致 |
| 13 | 过时embedded数据 | plot_filtering_strategies.py | Embedded fallback: No-filter=0.5867 (registry=0.5865), DSIR=0.5867 (registry=0.5869); std值也不同 | 更新embedded data或确保always从JSON读取 |
| 14 | Filtering figure ±std notation | discussion.tex:18 | Caption says "±1 std" but embedded data std values (~0.002) are ~2x registry ±values (~0.001) | 确认registry报告的是std还是sem; 统一notation |

## Figure 数据源追溯

| Figure | 文件名 | 生成脚本 | 数据文件 | 数据存在? | caption数字验证 |
|--------|--------|---------|---------|----------|---------------|
| Fig 2 (AUC decay) | fig2_auc_decay.pdf | scripts/plot_fig2_merged.py | **无 (全部硬编码)** | N/A | ⚠ Pythia用self-scored (0.6539) vs表格Qwen-scored (0.6074); OLMo 1v2=0.5079≠表格0.5001; Mistral 0v1=0.9843≠表格0.9209 |
| Fig 3a (K* theta) | fig_kstar_theta.pdf | scripts/draw_kstar_theta.py | **无 (全部硬编码)** | N/A | ⚠ 同Fig2: Pythia用self-scored值, OLMo值不匹配表格 |
| Fig 3b (transfer) | fig3_transfer_heatmap.pdf | scripts/transfer_heatmap_v2.py | results/exp013_olmo_rerun_v2/transfer_matrix.json | ✓ (2548B) | ⚠ Caption严重不匹配: 声称显示"6-class ordinal accuracy"和4个模型, 实际显示0v1 AUC和3个模型 |
| Fig 4 (JSD decay) | fig_jsd_decay.pdf | scripts/plot_fig_jsd_decay.py | **无 (全部硬编码)** | N/A | ⚠ JSD值与registry不完全一致; main text引用arXiv JSD=0.077但script数据为0.057 |
| Fig 5 (filtering) | fig_filtering_strategies.pdf | scripts/plot_filtering_strategies.py | 尝试读取artifacts/*filter*.json; 无则用embedded | 未验证JSON是否存在 | ⚠ Embedded data偏差: No-filter 0.5867 vs 0.5865, std ~2x |
| Fig 1 (pipeline) | pipeline.pdf | 无 (概念图, 手动/工具绘制) | N/A | ✓ | N/A (无数据数字) |

## Figure 数据问题

| # | Figure | 问题 | 严重性 | 修复方案 |
|---|--------|------|--------|---------|
| F1 | Fig 2 & Fig 3a | **Scorer不一致**: Pythia 1v2=0.6539 (self-scored) vs 表格/main text用0.6074 (Qwen-scored). 图表之间同一模型显示不同数值, 会误导读者认为Pythia discriminability比实际更高 | **高** | 将脚本TABLE1中Pythia值改为Qwen-scored: mean=[0.9722, 0.6074, 0.544, 0.5051, 0.5079], 更新CI为bootstrap Qwen-scored CI |
| F2 | Fig 2 & Fig 3a | **OLMo值来源不明**: 1v2=0.5079 既非self-scored (0.6145) 也非Qwen-scored (0.5001), 可能来自OLMo rerun但与任何registry记录均不完全匹配 | **中** | 确认OLMo值来源; 使用registry标准值0.5001(Qwen-scored)或明确记录rerun结果 |
| F3 | Fig 2 | **Mistral 0v1 scorer不一致**: 图中0.9843 (self-scored) vs extended table 0.9209 (cross-scored) | **中** | 统一为cross-scored值 |
| F4 | Fig 3b (transfer heatmap) | **Caption完全不匹配内容**: (1) Caption说"6-class ordinal accuracy...divided by retention rate", 实际显示0v1 AUC和K*; (2) Caption说"three continuation-mode models plus Qwen-rewrite" (4模型), 实际只有3个模型(OLMo, Pythia, Qwen), 无Qwen-rw | **高** | 重写caption: "Cross-model K* transfer (three continuation-mode models). Each cell shows AUC(0v1) and predicted K*; ✓/✗ indicates whether cross-model K* matches self-model K*." 或修改图为4模型+accuracy |
| F5 | 全部除pipeline和transfer | **所有数据硬编码**: 5个figure中4个将数据直接写入Python脚本, 而非从实验输出文件读取. 硬编码数据与registry记录存在偏差 | **中** | 重构脚本从JSON/CSV读取数据; 或至少在脚本注释中标注每个值的registry来源experiment_id |
| F6 | Fig 4 (JSD) | **Main text JSD值不匹配**: text引用arXiv JSD "1v2=0.077", 但figure脚本中arxiv_pythia[1]=0.057344 | **中** | 核实0.077来源: 可能是不同model的JSD; 确保text引用与figure数据一致 |
| F7 | Fig 5 (filtering) | **Embedded fallback数据过时**: No-filter 0.5867 vs registry 0.5865, DSIR 0.5867 vs 0.5869; std值差异更大 | **低** | 更新embedded数据或确保disk JSON始终存在 |

## 综合评估

### 高优先级修复 (影响论文数据一致性)
1. **Fig 2/3a Pythia scorer不一致** — 图与表使用不同scorer的数据, 1v2 AUC差异8.4pp (0.6539 vs 0.6074), 直接影响读者对Pythia discriminability的判断
2. **Fig 3b caption错误** — caption描述的内容与图中实际展示的数据完全不同 (ordinal accuracy vs 0v1 AUC; 4 models vs 3 models)
3. **OBD 38.6% vs per-depth 38.0% 不一致** — Tab s3c的per-depth recall值与reported overall accuracy矛盾

### 中优先级修复
4. Tab s10 Pythia decoding footnote CI upper值 (0.606 vs 0.6025)
5. Claude d3 recall .100→.101
6. Tab s13 OLMo "Self" K* 定义歧义
7. Small→27B avg 76.5% 算术不一致
8. arXiv JSD text vs figure mismatch

### 低优先级 (cosmetic)
9. Nuc p=0.9 rounding .687 vs .686
10. Gemma-27B 0.5894 vs 0.5895
11. Bootstrap K* "8/10 at 100%" vs strict count 7/10
12. Filtering embedded data stale values
