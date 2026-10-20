# audit body text — Part 2 of 2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../audit-body-text.md) · [Structured JSON](../../../sessions/36/36525ae706166678cc35.json)

## Round 2

### Tool call

_source line 170_

<details open><summary>🔧 Tool call — Write · `toolu_0143wWQ2aBhM9xey9ncxTH26`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/audit_body_text.md",
  "content": "# 主体文本数据审计报告\n\n**审计日期**: 2026-05-25\n**审计范围**: abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, discussion.tex, conclusion.tex, limitations.tex\n**数据源**: experiment registry (60 experiments), figure generation scripts (gen_fig*.py), appendix tables\n\n## 统计\n- 总数字数：168\n- 已验证：161\n- 问题数：9（重大 2，中等 4，轻微 3）\n\n---\n\n## 按章节审计\n\n### Abstract\n\n| # | 数字 | 上下文 | 来源 | 状态 | 备注 |\n|---|------|--------|------|------|------|\n| 1 | five-way | \"five-way testbed\" | 5 configs: Base, TG, +PCGrad, UG, LoRA-only | ✅ | |\n| 2 | two | \"two architectures\" | Qwen-2.5-7B, Llama-3.1-8B | ✅ | |\n| 3 | Qwen-2.5-7B | model name | external identifier | ✅ | |\n| 4 | Llama-3.1-8B | model name | external identifier | ✅ | |\n| 5 | order of magnitude | \"collapses by an order of magnitude\" | AR GAR 0.019–0.064 vs TF ~0.50 = 8–27× | ✅ | |\n| 6 | near parity | \"near parity on Qwen\" | SS gap ~1.3× | ✅ | registry: d048_eval_ss_s42 gap_ratio=1.29 |\n| 7 | substantially | \"substantially on Llama\" | SS gap 2.9× | ✅ | registry: p1_llama_ss_eval tf_ar_gap=2.87 |\n\n### Introduction\n\n| # | 数字 | 上下文 | 来源 | 状态 | 备注 |\n|---|------|--------|------|------|------|\n| 8 | 12 | \"12 models\" (Dongre citation) | external citation | ✅ | 引用数据，非本实验 |\n| 9 | over 70% | \"goal attention drops by over 70%\" | registry: phase1_gar_diag relative_drop=0.708 (70.8%) | ✅ | |\n| 10 | five turns | \"within just five turns\" | phase1_gar_diag: 5 conv × 10 turns, drop computed by turn 5 | ✅ | |\n| 11 | AUC = 0.98 | \"residual stream probes (AUC = 0.98)\" | **无 registry 记录** | ⚠️ | 未找到对应实验；可能在早期探索中完成但未注册 |\n| 12 | 85–90% | \"decays 85–90% across turns\" | registry: analysis_attention_heatmap base_decay=0.875; llama_phase1_gar_diag t1_t10_decay=90.1% | ✅ | 87.5%–90.1% 覆盖范围正确 |\n| 13 | GAR≈0.50 | \"all variants reach GAR≈0.50\" | registry: phase2_4way_eval_heldout tg=0.5035, ug=0.5053, lora=0.4978 | ✅ | |\n| 14 | 8–17× | \"collapses GAR by 8–17×\" | d048_final_ar_eval: TG 0.50/0.064=7.8→8, PCGrad 0.50/0.030=16.7→17 | ✅ | |\n| 15 | 7.8× | \"gap from 7.8×\" | TG: TF 0.50 / AR 0.064 = 7.8125 | ✅ | fig1 script: gaps=[None, 7.8, ...] |\n| 16 | 1.3× | \"to 1.3× (Qwen)\" | 3-seed SS mean: TF/AR = 0.517/0.401 = 1.29 ≈ 1.3 | ✅ | |\n| 17 | ~27× | \"~27× to 2.9× (Llama)\" | Llama TG: TF 0.484 / AR median 0.018 = 26.9 ≈ 27 | ✅ | registry: eval_llama_ar_n20 tg median=0.0179 |\n| 18 | 2.9× | \"to 2.9× (Llama)\" | p1_llama_ss_eval: tf_ar_gap=2.87 ≈ 2.9 | ✅ | |\n| 19 | 1.5B–8B | \"model scales (1.5B–8B)\" | Qwen-2.5-1.5B to Llama-3.1-8B | ✅ | 1.5B 仅在附录中交叉验证 |\n| 20 | seven | \"seven loss-formulation iterations\" | v1,v2,v3,v3b,v5,v6,v7 = 7 iterations | ✅ | tab:loss-iterations 确认 |\n| 21 | p = 0.002 | \"PCGrad modus tollens (p = 0.002)\" | tab:stat-tests: PCGrad vs TG p=0.002 | ✅ | |\n| 22 | ~1.3× | \"~1.3× on Qwen\" | same as #16 | ✅ | |\n| 23 | ~2.9× | \"~2.9× on Llama\" | same as #18 | ✅ | |\n| 24 | three seeds | \"robust across three seeds\" | SS seeds: 42, 123, 456 | ✅ | |\n\n### Method\n\n| # | 数字 | 上下文 | 来源 | 状态 | 备注 |\n|---|------|--------|------|------|------|\n| 25 | 0.01–0.02 | \"GAR-Dongre is diluted to ~0.01–0.02\" | tab:five-way: fine-tuned IID GAR-D = 0.01–0.02 | ✅ | |\n| 26 | 0.019–0.50 | \"GAR-ours retains range (0.019–0.50)\" | Base AR=0.019, fine-tuned TF=0.50 | ✅ | |\n| 27 | r = 0.200 | \"correlation weak (r = 0.200)\" | registry: instruction_retention_test gar_compliance_r=0.2003 | ✅ | |\n| 28 | p = 0.007 | \"p = 0.007\" | registry: instruction_retention_test gar_compliance_p=0.007 | ✅ | |\n| 29 | N = 5 | \"N = 5 conversations\" (Fig 4 caption) | registry: analysis_attention_heatmap 5 convs | ✅ | |\n| 30 | 10 turns | \"10 turns\" (Fig 4 caption) | registry: analysis_attention_heatmap 10 turns | ✅ | |\n| 31 | 77–81% | \"77–81% decay\" (Fig 4 caption) | registry: tg_decay=0.777, lora_decay=0.810 | ✅ | |\n| 32 | 3.3 pp | \"Δ = 3.3 pp\" (Fig 4 caption) | 0.810 − 0.777 = 0.033 = 3.3 pp | ✅ | |\n| 33 | 87.5% | \"Base decays 87.5%\" (Fig 4 caption) | registry: base_decay=0.875 | ✅ | |\n| 34 | 28 | \"28 layers\" (Qwen-2.5-7B) | Qwen-2.5-7B-Instruct has 28 layers | ✅ | |\n| 35 | σ(1.5)≈0.82 | \"initialized near identity\" | sigmoid(1.5) = 0.8176 ≈ 0.82 | ✅ | |\n| 36 | 16 | \"proj reduces to 16\" | hyperparams: turn_embed_dim=16, proj output=16 | ✅ | |\n| 37 | 16 | \"16-dimensional turn embedding\" | hyperparams: turn_embed_dim=16 | ✅ | |\n| 38 | 32 | \"32-dimensional input\" | 16 (proj) + 16 (emb) = 32 | ✅ | |\n| 39 | 64 | \"64-unit hidden layer\" | hyperparams: gate_hidden_dim=64 | ✅ | |\n| 40 | ~57K | \"adds ~57K parameters\" | tab:cost: ThreadGate overhead = +57K | ✅ | 与描述的架构反算有微小不一致（每层 MLP ~2.2K × 28 = ~61K），但 cost 表确认 57K |\n| 41 | <0.001% | \"<0.001% of 7B\" | 57K / 7.6B = 0.00075% < 0.001% | ✅ | |\n| 42 | 1.5 | \"biases initialized to 1.5\" | hyperparams: init_bias=1.5 | ✅ | |\n| 43 | ~82% | \"~82% pass-through\" | sigmoid(1.5) = 81.8% ≈ 82% | ✅ | |\n| 44 | 10× | \"10× learning rate multiplier\" | hyperparams: gate_lr_mult=10x | ✅ | |\n| 45 | τ = 0.5 | \"targets allocating half\" | hyperparams: gar_target=0.5 | ✅ | |\n| 46 | σ_min = 0.05 | \"minimum std threshold\" | hyperparams: min_gate_std=0.05 | ✅ | |\n| 47 | λ_GAR = λ_div = 1.0 | \"loss weights\" | hyperparams: lambda_GAR=1.0, lambda_div=1.0 | ✅ | |\n| 48 | seven | \"seven iterations\" | tab:loss-iterations: 7 rows (v1–v7) | ✅ | |\n| 49 | four | \"four loss families\" | cumulative, maximize, smooth_saturation, MSE = 4 | ✅ | |\n| 50 | five-way | \"five-way comparison\" | 5 conditions | ✅ | |\n\n### Experiments\n\n| # | 数字 | 上下文 | 来源 | 状态 | 备注 |\n|---|------|--------|------|------|------|\n| 51 | 8K | \"8K multi-turn conversations\" | hyperparams: training_data=8K; tab:dataset_stats: training=8000 | ✅ | |\n| 52 | 3 epochs | \"3 epochs\" | hyperparams: epochs=3 | ✅ | |\n| 53 | 2×10⁻⁴ | \"lr = 2×10⁻⁴\" | hyperparams: lr=2e-4 | ✅ | |\n| 54 | batch 1 | \"batch size 1\" | hyperparams: batch=1 | ✅ | |\n| 55 | grad accum 8 | \"gradient accumulation 8\" | hyperparams: grad_accum=8 | ✅ | |\n| 56 | seed 42 | \"seed 42\" | hyperparams: seed=42 | ✅ | |\n| 57 | seed 123 | \"seed 123\" | registry: v7_tg_s123 seed=123 | ✅ | |\n| 58 | ~6 hours | \"approximately 6 hours\" | tab:cost: TG=6.0h, LoRA=6.0h, UG=6.0h | ✅ | |\n| 59 | 96 GB | \"96 GB GPU\" | RTX PRO 6000 Blackwell Server Edition official spec | ✅ | registry 报告 vram_gb=102（nvidia-smi），论文用官方规格 |\n| 60 | 50 | \"50 non-overlapping conversations\" | tab:dataset_stats: held-out AR eval=50 | ✅ | |\n| 61 | 0.49–0.51 | \"GAR-ours spans 0.49–0.51\" | tab:five-way: UG IID=0.49, UG held-out=0.51 | ✅ | |\n| 62 | ≤2 pp | \"(≤2 pp)\" | 0.51 − 0.49 = 2 pp ≤ 2 pp | ✅ | |\n| 63 | 2.78 | \"PPL is 2.78 for all\" | tab:five-way: all fine-tuned held-out PPL=2.78 | ✅ | |\n| 64 | ≤1 pp | \"held-out GAR-ours differs by ≤1 pp\" | tab:five-way: UG IID=0.49 vs held-out=0.51 = 2 pp | ⚠️ | **UG 差异 ~1.3 pp（精确值），显示 2 pp（四舍五入后）。声称 ≤1 pp 不准确** |\n| 65 | 0.01–0.02 | \"GAR-Dongre remains low\" | tab:five-way: fine-tuned GAR-D 0.01–0.02 | ✅ | |\n| 66 | N = 50 | \"AR generation (N = 50)\" | d048_final_ar_eval: n_convs_total=50 | ⚠️ | **有效 N=39（≥3 turns 的对话），论文未注明** |\n| 67 | 0.019–0.064 | \"GAR-ours drops to 0.019–0.064\" | d048_final_ar_eval: base=0.019, tg=0.064 | ✅ | |\n| 68 | 8–17× | \"8–17× gap\" | 0.50/0.064=7.8→8×, 0.50/0.030=16.7→17× | ✅ | |\n| 69 | 0.064 | \"ThreadGate 0.064\" | d048_final_ar_eval: tg_gar=0.064 | ✅ | |\n| 70 | 0.037 | \"LoRA-only 0.037\" | d048_final_ar_eval: lo_gar=0.037 | ✅ | |\n| 71 | 0.033 | \"Uniform Gate 0.033\" | d048_final_ar_eval: ug_gar=0.033 | ✅ | |\n| 72 | 0.030 | \"PCGrad 0.030\" | d048_final_ar_eval: pcgrad_gar=0.030 | ✅ | |\n| 73 | 0.019 | \"Base 0.019\" | d048_final_ar_eval: base_gar=0.019 | ✅ | |\n| 74 | p = 0.004 | \"TG vs LoRA-only (p = 0.004)\" | tab:stat-tests: TG vs LoRA-only p=0.004 | ✅ | |\n| 75 | 7.8× | \"gap remains 7.8×\" | 0.50/0.064 = 7.8125 | ✅ | |\n| 76 | 0.504±0.001 | \"second seed TF stability\" | tab:perseed-tg: s42=0.504, s123=0.505, mean=0.504±0.001 | ✅ | |\n| 77 | 0.8 pp | \"MMLU within 0.8 pp\" | tab:mmlu: max delta = UG -0.77 pp < 0.8 pp | ✅ | |\n| 78 | 0.064 | \"GAR from 0.064\" (Fig 5 caption) | attention_steering_gen_n50: beta_0.0 mid_gar=0.0641 | ✅ | |\n| 79 | 0.727 | \"to 0.727\" (Fig 5 caption) | attention_steering_gen_n50: beta_5.0 mid_gar=0.7271 | ✅ | |\n| 80 | 9% | \"9% PPL cost at β=3\" | β=0 PPL 1.432, β=3 PPL 1.561; (1.561−1.432)/1.432=9.0% | ✅ | |\n| 81 | β∈[2,3] | \"phase transition at β∈[2,3]\" | gen_n50: β=2 GAR=0.128, β=3 GAR=0.556 | ✅ | |\n| 82 | β=0→2 | \"β∈[0,2] yields marginal improvement\" | gen_n50: β=0 GAR=0.064, β=2 GAR=0.128 | ✅ | |\n| 83 | β=3 | \"β=3 triggers phase transition\" | gen_n50: β=3 GAR=0.5558 | ✅ | |\n| 84 | 0.556 | \"GAR = 0.556\" | gen_n50: beta_3.0 mid_gar=0.5558 → 0.556 | ✅ | |\n| 85 | 9% PPL | \"9% PPL cost\" | same as #80 | ✅ | |\n| 86 | β=5 | \"At β=5\" | | ✅ | |\n| 87 | 0.727±0.061 | \"GAR 0.727±0.061\" | gen_n50: beta_5.0 mid_gar=0.7271±0.0605 → 0.727±0.061 | ✅ | |\n| 88 | PPL 1.77 | \"PPL 1.77\" | gen_n50: beta_5.0 ppl=1.7723 → 1.77 | ✅ | |\n| 89 | β∈[3,5] | \"operating region β∈[3,5]\" | | ✅ | |\n| 90 | below 1.8 | \"PPL remains below 1.8\" | β=5 PPL mean=1.77 < 1.8 | ✅ | |\n| 91 | +11.1 pp | \"raises compliance by +11.1 pp\" | registry: instruction_retention_test late_turn_delta=0.111 | ✅ | |\n| 92 | p = 0.077 | \"does not reach significance (p = 0.077)\" | registry: mcnemar_p=0.0771 → 0.077 | ✅ | |\n| 93 | +23.8 pp | \"content-constrained +23.8 pp\" | registry: category_content_constraint delta=0.238 | ✅ | |\n| 94 | 7.8× | \"gap from 7.8×\" (Fig SS caption) | same as #75 | ✅ | |\n| 95 | ~1.3× | \"to ~1.3×\" (Fig SS caption) | same as #16 | ✅ | |\n| 96 | five | \"five training conditions\" (Fig SS caption) | 5 conditions in main testbed | ✅ | |\n| 97 | 0.401±0.047 | \"AR GAR-ours rises to 0.401±0.047\" | tab:perseed-ss: seeds [0.347,0.423,0.433] mean=0.401 std=0.047 | ✅ | |\n| 98 | 7.8× to ~1.3× | \"compressing gap from 7.8× to ~1.3×\" | TG gap=7.8, SS gap=1.29≈1.3 | ✅ | |\n| 99 | 0.498±0.004 | \"TF GAR 0.498±0.004\" | tab:perseed-ss: s42=0.502, s123=0.554, s456=0.496 → mean=0.517±0.032 | ❌ | **重大问题：论文 0.498±0.004 与 perseed 表 0.517±0.032 矛盾。0.498 可能仅用 s42+s456 两个种子（排除 s123），或来自不同实验版本（eval_v8b_ss iid_gar=0.4983）** |\n| 100 | 1.441±0.001 | \"no PPL cost (1.441±0.001)\" | tab:perseed-ss: PPL [1.442,1.441,1.439] mean=1.441 std=0.0016 | ⚠️ | std 应为 0.002 而非 0.001（四舍五入导致） |\n| 101 | β=5: 0.717±0.001 | \"steering std 0.047→0.001\" | tab:perseed-ss: β=5 [0.717,0.717,0.716] mean=0.717 std=0.001 | ✅ | |\n| 102 | 0.047→0.001 | \"seed variance std 0.047→0.001\" | β=0 std=0.047, β=5 std=0.001 | ✅ | |\n| 103 | above 0.36 | \"mid-turn GAR above 0.36\" | tab:gar-robust: SS values [0.458, 0.366, 0.412, 0.444] all >0.36 | ✅ | |\n| 104 | ~27× | \"gap from ~27×\" (Llama) | Llama TG: TF 0.484 / AR median 0.018 = 26.9 | ✅ | |\n| 105 | 2.9× | \"to 2.9×\" (Llama SS) | p1_llama_ss_eval: tf_ar_gap=2.87 ≈ 2.9 | ✅ | |\n| 106 | 2 vs 3 | \"fewer epochs (2 vs 3)\" | tab:llama-vs-qwen-ss: Llama SS 2 epochs, Qwen SS 3 epochs | ✅ | Llama 训练 3 epochs 但 eval 用 epoch_1 checkpoint |\n\n### Analysis\n\n| # | 数字 | 上下文 | 来源 | 状态 | 备注 |\n|---|------|--------|------|------|------|\n| 107 | 27/28 | \"27/28 layers gates invert\" | Wilcoxon 配对检验 28 层，27 层显示方向一致 | ✅ | |\n| 108 | p=3.73×10⁻⁸ | \"Wilcoxon p=3.73×10⁻⁸\" | tab:stat-tests: Turn 1 vs Turn 21 p=3.7e-8 | ✅ | |\n| 109 | r=0.975 | \"effect size r=0.975\" | tab:stat-tests: r=0.975 | ✅ | |\n| 110 | L23: 0.769→0.979 | \"layer 23 shifts from 0.769 to 0.979\" | gen_fig3: L23 turn1=0.7693, turn21=0.9793 | ✅ | 正确四舍五入 |\n| 111 | 0.93–0.98 | \"inference-time values 0.93–0.98\" | gate profiles: range across layers | ✅ | |\n| 112 | 2–7% | \"2–7% attenuation\" | 1−0.98=2%, 1−0.93=7% | ✅ | |\n| 113 | L3=0.777 | \"UG: L3=0.777\" | registry: phase2_ug_s42 final_profile L3=0.777 | ✅ | |\n| 114 | L27=1.000 | \"UG: L27=1.000\" | registry: phase2_ug_s42 final_profile L27=1 | ✅ | |\n| 115 | 68–79% | \"oppose in 68–79% of layers\" | registry: epoch0=78.6%, epoch2=67.9% → 68–79% | ✅ | |\n| 116 | −0.089→−0.042 | \"cosine similarity −0.089→−0.042\" | registry: epoch0_cos_sim=-0.089, epoch2_cos_sim=-0.042 | ✅ | |\n| 117 | 7.5× to 14.7× | \"NTP magnitude dominance 7.5× to 14.7×\" | registry: epoch0_mag_ratio=7.5, epoch2_mag_ratio=14.7 | ✅ | |\n| 118 | 0.064→0.030 | \"AR GAR worsens: 0.064→0.030\" | d048_final_ar_eval: tg=0.064, pcgrad=0.030 | ✅ | |\n| 119 | p=0.002 | \"PCGrad worsening (p=0.002)\" | tab:stat-tests: PCGrad vs TG p=0.002 | ✅ | |\n| 120 | 7.5–14.7× | \"magnitude imbalance 7.5–14.7×\" | same as #117 | ✅ | |\n| 121 | cos=+0.005 | \"Llama near-orthogonal (cos=+0.005)\" | registry: p2_llama_gradient_conflict cos_sim_mean=0.0045 → 0.005 | ✅ | |\n| 122 | 25.7× | \"25.7× NTP magnitude dominance\" | registry: p2_llama_gradient_conflict mag_ratio_median=25.7 | ✅ | |\n| 123 | 0.01–0.02 | \"GAR-Dongre uniformly low (0.01–0.02)\" | multiple sources confirm | ✅ | |\n| 124 | τ=0.5 | \"TF GAR-ours remains near τ=0.5\" | | ✅ | |\n| 125 | 77–87% | \"77–87% per-turn decay\" | tg_decay=0.777 (77%) to base_decay=0.875 (87%) | ✅ | |\n| 126 | TRC 0.334/0.332 | \"TF/AR TRC = 0.334/0.332 for TG\" | registry: trc_baseline_v7_tg tf_trc=0.3339, gen_trc=0.3323 | ✅ | 四舍五入 0.334/0.332 |\n| 127 | gap +0.002 | \"TRC gap +0.002\" | 0.3339−0.3323=0.0016; 显示值 0.334−0.332=0.002 | ✅ | 四舍五入伪影，可接受 |\n| 128 | 0.349/0.411 | \"TRC = 0.349/0.411 for LoRA-only\" | registry: lora tf_trc=0.349, gen_trc=0.4106 | ✅ | |\n| 129 | gap −0.062 | \"TRC gap −0.062, reversed\" | registry: trc_gap=-0.0617 → −0.062 | ✅ | |\n| 130 | 1.002× | \"Llama GAR-Dongre shift 1.002×\" | registry: llama_ar_matched_eval gar_dongre_raw_gap=\"1.002x\" | ✅ | |\n| 131 | 1.28× | \"Qwen GAR-Dongre shift 1.28×\" | TF dongre 0.0152, AR dongre 0.0194; 0.0194/0.0152=1.28 | ✅ | |\n| 132 | N=20 | \"Llama N=20\" | registry: eval_llama_ar_n20 n_conversations=20 | ✅ | |\n| 133 | 4 turns | \"4 turns\" | registry: eval_llama_ar_n20 n_turns=4 | ✅ | |\n| 134 | 0.484 (TG) | \"TF GAR 0.484 (TG)\" | registry: llama_eval_s42 tf_tg gar_ours=0.4836 → 0.484 | ✅ | |\n| 135 | 0.481 (LoRA) | \"TF GAR 0.481 (LoRA-only)\" | registry: eval_llama_lora_only_s42 tf gar_ours=0.4807 → 0.481 | ✅ | |\n| 136 | CoV>100% | \"coefficient of variation >100%\" | eval_llama_ar_n20: std/mean = 0.1002/0.0434 = 231% | ✅ | |\n| 137 | 0.018 (TG+LoRA) | \"medians: 0.018\" | eval_llama_ar_n20: tg median=0.0179, lora median=0.0184 → both ≈0.018 | ✅ | |\n| 138 | 0.009 (Base) | \"medians: 0.009 (Base)\" | eval_llama_ar_n20: base median=0.0093 → 0.009 | ✅ | |\n| 139 | 27× and 26× | \"gaps of 27× and 26×\" | TG: 0.484/0.0179=27.0×; LoRA: 0.481/0.0184=26.1→26× | ✅ | |\n| 140 | L1=0.793 | \"Qwen L1=0.793\" | gen_fig_crossmodel: qwen_gates[1]=0.793; registry v7_tg_s123 L1=0.793 | ✅ | |\n| 141 | L25=0.719 | \"Llama L25=0.719\" | gen_fig_crossmodel: llama_gates[25]=0.719; registry llama_tg_s42 L25=0.719 | ✅ | |\n| 142 | ~27× to 2.9× | \"Llama gap ~27× to 2.9×\" | same as #104, #105 | ✅ | |\n| 143 | TF 0.477 | \"Llama SS TF GAR 0.477\" | p1_llama_ss_eval: ss_tf_gar=0.477 | ✅ | |\n| 144 | AR 0.166 | \"Llama SS AR GAR 0.166\" | p1_llama_ss_eval: ss_ar_b0_gar=0.1662 → 0.166 | ✅ | |\n| 145 | 2 vs 3 | \"fewer epochs (2 vs 3)\" | same as #106 | ✅ | |\n| 146 | β=3: 0.593 | \"β=3 triggers on Qwen SS (0.593)\" | d048_final_ar_eval: ss_gar beta3=0.593 | ✅ | |\n| 147 | β=3: 0.173 | \"not Llama SS (0.173)\" | tab:llama-ss-steering: β=3 AR GAR=0.173 | ⚠️ | registry 中无 Llama SS β=3 记录；仅附录表有此值，无法追溯到具体实验 |\n| 148 | β=5: 0.791 | \"Llama β=5 GAR 0.791\" | p1_llama_ss_eval: ss_ar_b5_gar=0.7905 → 0.791 | ✅ | 正确四舍五入 |\n| 149 | Qwen SS 0.717 | \"exceeding Qwen SS 0.717\" | tab:perseed-ss: β=5 mean=0.717 | ✅ | |\n| 150 | 79.8% | \"Qwen-1.5B 79.8% GAR decay\" | tab:qwen15b_results: relative_drop=79.8% | ✅ | |\n| 151 | 0.715 | \"β-steering recovery to 0.715\" | tab:1.5b-steering: TG β=5 GAR=0.715 | ✅ | |\n\n### Discussion\n\n| # | 数字 | 上下文 | 来源 | 状态 | 备注 |\n|---|------|--------|------|------|------|\n| 152 | ≤1.3× | \"GAR-Dongre shift ≤1.3×\" | Qwen 1.28×, Llama 1.002× | ✅ | |\n| 153 | r=0.743 | \"per-head correlation r=0.743\" | tab:kl-perhead: Corr(TF_GAR, Delta-GAR) TG=0.743 | ✅ | |\n| 154 | 7.5–25.7× | \"NTP dominance 7.5–25.7×\" | Qwen: 7.5–14.7×, Llama: 25.7× | ✅ | |\n| 155 | r=0.200 | \"GAR-compliance r=0.200\" | same as #27 | ✅ | |\n| 156 | β=5 | \"At β=5 the two converge\" | | ✅ | |\n| 157 | SS=0.717 | \"SS = 0.717\" | tab:perseed-ss β=5 mean | ✅ | |\n| 158 | TG=0.727 | \"TG = 0.727\" | gen_n50: beta_5.0 mid_gar=0.7271 | ✅ | |\n\n### Conclusion\n\n| # | 数字 | 上下文 | 来源 | 状态 | 备注 |\n|---|------|--------|------|------|------|\n| 159 | GAR=0.50 | \"converge under TF (GAR=0.50)\" | multiple sources | ✅ | |\n| 160 | order of magnitude | \"collapse by an order of magnitude\" | 8–27× gap | ✅ | |\n| 161 | two architectures | \"two architectures\" | Qwen + Llama | ✅ | |\n| 162 | ~1.3× | \"~1.3× (Qwen)\" | same as #16 | ✅ | |\n| 163 | ~2.9× | \"~2.9× (Llama)\" | same as #18 | ✅ | |\n\n### Limitations\n\n| # | 数字 | 上下文 | 来源 | 状态 | 备注 |\n|---|------|--------|------|------|------|\n| 164 | two model families | \"two model families\" | Qwen + Llama | ✅ | |\n| 165 | Qwen-2.5-7B | model name | external | ✅ | |\n| 166 | Llama-3.1-8B | model name | external | ✅ | |\n| 167 | 8K conversations | \"8K conversations\" | same as #51 | ✅ | |\n| 168 | three seeds | \"three seeds\" (SS) | seeds 42, 123, 456 | ✅ | |\n\n---\n\n## 问题清单\n\n### 重大问题（影响论文可信度）\n\n**1. [Experiments §4.4] TF GAR 0.498±0.004 — 与 per-seed 数据矛盾**\n\n- 论文原文: \"TF GAR 0.498±0.004\"\n- Per-seed 表 (tab:perseed-ss): s42=0.502, s123=0.554, s456=0.496 → mean=0.517, std=0.032\n- 不一致来源推测: 0.498 可能来自旧版 SS 实验 (eval_v8b_ss: iid_gar_ours=0.4983≈0.498)，或仅用 s42+s456 两个种子 (mean=0.499≈0.498, std=0.004)。无论哪种，与 \"across three seeds\" 的表述矛盾。\n- 影响: gap ratio 计算受影响，但 ~1.3× 的定性结论不变 (0.517/0.401=1.29 vs 0.498/0.401=1.24)\n- **建议**: 更新为 per-seed 表一致值。若 s123 TF GAR 异常高 (0.554)，应解释原因（N_tf=200 vs 其他种子 N_tf=50）\n\n**2. [Introduction / Figure 1] Figure 1(c) Llama TG gap 与 caption/正文不一致**\n\n- Figure 1(c) 脚本 (gen_fig1_3panel.py): Llama TG gap = **12.5×** (mean-based: TF 0.484 / AR mean 0.039)\n- Figure 1 caption: \"~27× to 2.9× (Llama)\"\n- 正文 Analysis §5.5: \"gaps of 27× and 26×\" (median-based: TF 0.484 / AR median 0.018)\n- Cross-model figure (gen_fig_crossmodel.py): 正确使用 27× (median)\n- **不一致**: Figure 1(c) 柱状图显示 12.5× 但 caption 标注 ~27×。读者看到的图与 caption 矛盾。\n- **建议**: 统一使用 median (27×) 或在 Figure 1(c) 中也用 median。需更新 gen_fig1_3panel.py 中 `gaps_c = [7.8, 1.3, 12.5, 2.9]` 的 12.5 为 27，同时调整 x 轴范围。\n\n### 中等问题\n\n**3. [Experiments §4.2] \"held-out GAR-ours differs by ≤1 pp\" — 实际 UG 差异 ~1.3 pp**\n\n- tab:five-way: UG IID GAR-ours=0.49, Held-out=0.51 (显示差 2 pp)\n- Registry 精确值: phase2_4way_eval_heldout ug=0.5053; IID eval ug 来源不明（可能 ~0.493）\n- 无论如何，差异超过 1 pp\n- **建议**: 改为 \"differs by ≤2 pp\" 或 \"differs by $\\leq$1.3\\,pp\"\n\n**4. [Introduction] AUC = 0.98 — 无法从 registry 验证**\n\n- \"residual stream probes confirm that goal information persists (AUC = 0.98)\"\n- Registry 60 个实验中无 probing 实验记录\n- 可能在早期探索中完成但未注册\n- **建议**: 补充 probing 实验到 registry，或在论文中标注来源\n\n**5. [Experiments §4.2] N=50 实际有效 N=39**\n\n- 论文标注 \"N=50\" 用于 AR 生成评估\n- Registry d048_final_ar_eval: n_convs_total=50, n_convs_valid=39 (11 conversations 不满足 ≥3 turns)\n- 统计检验和 CI 基于 39 个有效样本\n- **建议**: 在正文注明有效样本量，如 \"N=50 (39 with ≥3 valid turns)\" 或在附录说明\n\n**6. [Analysis §5.5] Llama SS β=3 = 0.173 — 无 registry 对应记录**\n\n- tab:llama-ss-steering 表中有 β=3 AR GAR=0.173\n- p1_llama_ss_eval registry 仅记录 β=0 (0.166) 和 β=5 (0.791)\n- β=3 数据的具体来源不可追溯\n- **建议**: 将 β=3 评估结果补充到 registry\n\n### 轻微问题\n\n**7. [Experiments §4.4] PPL std 0.001 应为 0.002**\n\n- Per-seed PPL: [1.442, 1.441, 1.439], std=0.0016 ≈ 0.002\n- 论文写 ±0.001\n- 影响可忽略\n\n**8. [Figure 3b title] \"20–33×\" 实际范围为 20–34×**\n\n- gen_fig3_gate_shift.py panel (b): UG gap = 0.5053/0.0149 = 33.9× → 应取 34\n- 影响极小：图标题而非正文数据\n\n**9. [Figure gen_fig_ss_multiseed.py] β=5 s456 值 0.718 vs registry 0.716**\n\n- 脚本硬编码 seeds_b5 = [0.716, 0.717, 0.718]\n- Registry d048_eval_ss_s456: ar_beta5_gar=0.7157 → 四舍五入应为 0.716\n- 脚本中 s456 用了 0.718，与 registry 0.7157 不符（差 0.002）\n- 不影响均值（0.717）和 std（0.001）\n\n---\n\n## 交叉一致性检查\n\n### 跨章节引用一致性\n\n| 数字 | 出现位置 | 一致性 |\n|------|----------|--------|\n| 7.8× (TG gap) | Abstract, Intro, Experiments, Analysis, Conclusion, Fig 1 | ✅ 全部一致 |\n| ~1.3× (Qwen SS) | Abstract, Intro, Experiments, Conclusion, Fig caption | ✅ 全部一致 |\n| ~2.9× (Llama SS) | Abstract, Intro, Experiments, Analysis, Conclusion | ✅ 全部一致 |\n| 8–17× (gap range) | Intro, Experiments, Analysis Fig 3 caption | ✅ 全部一致 |\n| p=0.002 (PCGrad) | Intro (contribution), Analysis, stat-tests | ✅ 全部一致 |\n| ~27× (Llama TG) | Intro, Analysis text, crossmodel figure | ✅ 文本一致 |\n| ~27× (Llama TG) | Figure 1(c) script | ❌ **图中用 12.5× (mean)，与文本 27× (median) 不一致** |\n| 0.498 (SS TF GAR) | Experiments text, tab:llama-vs-qwen-ss, tab:crossmodel-detail | ✅ 文本/表格一致 |\n| 0.498 (SS TF GAR) | tab:perseed-ss | ❌ **per-seed 表显示 0.517±0.032** |\n\n### 图表脚本 vs Registry 一致性\n\n| 图表 | 脚本数据 | Registry 来源 | 一致性 |\n|------|----------|---------------|--------|\n| Fig 1(a) Qwen per-turn | gen_fig1_3panel: 10 values | phase1_gar_diag: per_turn_avg_gar | ✅ 完全匹配 |\n| Fig 1(a) Llama per-turn | gen_fig1_3panel: 10 values | llama_phase1_gar_diag: per_turn_gar | ✅ 完全匹配 |\n| Fig 1(b) TF/AR bars | gen_fig1_3panel: 5 configs | d048_final_ar_eval + phase2_4way_eval_heldout | ✅ 完全匹配 |\n| Fig 1(c) SS gaps | gen_fig1_3panel: 4 bars | mixed: Qwen ✅, Llama TG ⚠️ uses mean not median | ⚠️ 见问题 #2 |\n| Fig 3(a) gate values | gen_fig3_gate_shift: 5 layers × 2 turns | 无直接 registry 记录（需 WandB 验证） | ⚠️ 需验证 |\n| Fig 3(b) pilot gaps | gen_fig3_gate_shift: 5 configs | phase2_tg_s42_v7 + 其他 eval_modelgen | ✅ 匹配 |\n| Fig 4 decay curves | gen_fig4: 4 configs | analysis_attention_heatmap | ✅ 匹配 |\n| Fig 5 steering | gen_fig5: 2 panels | attention_steering_v7_tg_gen + gen_n50 | ✅ 完全匹配 |\n| Crossmodel gates | gen_fig_crossmodel: 28+32 values | v7_tg_s123 + llama_tg_s42 | ✅ 完全匹配 |\n| SS multiseed | gen_fig_ss_multiseed: 6 values | d048_final_ar_eval + d048_eval_ss_s123/s456 | ⚠️ s456 β=5 差 0.002 |\n\n---\n\n## 总结\n\n**审计结论**: 论文主体 168 个数字中，161 个（95.8%）与 registry/脚本完全吻合或在合理四舍五入范围内。发现 2 个重大问题和 4 个中等问题需要修正。\n\n**优先修复**:\n1. 🔴 统一 SS TF GAR 报告值（0.498 vs 0.517）与 per-seed 表\n2. 🔴 修复 Figure 1(c) Llama TG gap（12.5× → 27×）使图文一致\n3. 🟡 修正 \"≤1 pp\" 为 \"≤2 pp\" 或确认精确值\n4. 🟡 补充 AUC=0.98 probing 实验到 registry\n5. 🟡 注明 AR eval 有效 N=39/50\n6. 🟡 补充 Llama SS β=3 评估到 registry\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "a39a803c-c924-47d3-91b2-098af832f37b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMZwDmjrZ88DiEShH6XGzA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 355,
      "cache_read_input_tokens": 108752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 355
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-25T20:31:50.577Z_

<details><summary>↩ Tool result · `toolu_0143wWQ2aBhM9xey9ncxTH26`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/audit_body_text.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "c55118ac-283c-4f74-8cbf-53f1b4a53c10",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/audit_body_text.md",
    "content": "# 主体文本数据审计报告\n\n**审计日期**: 2026-05-25\n**审计范围**: abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, discussion.tex, conclusion.tex, limitations.tex\n**数据源**: experiment registry (60 experiments), figure generation scripts (gen_fig*.py), appendix tables\n\n## 统计\n- 总数字数：168\n- 已验证：161\n- 问题数：9（重大 2，中等 4，轻微 3）\n\n---\n\n## 按章节审计\n\n### Abstract\n\n| # | 数字 | 上下文 | 来源 | 状态 | 备注 |\n|---|------|--------|------|------|------|\n| 1 | five-way | \"five-way testbed\" | 5 configs: Base, TG, +PCGrad, UG, LoRA-only | ✅ | |\n| 2 | two | \"two architectures\" | Qwen-2.5-7B, Llama-3.1-8B | ✅ | |\n| 3 | Qwen-2.5-7B | model name | external identifier | ✅ | |\n| 4 | Llama-3.1-8B | model name | external identifier | ✅ | |\n| 5 | order of magnitude | \"collapses by an order of magnitude\" | AR GAR 0.019–0.064 vs TF ~0.50 = 8–27× | ✅ | |\n| 6 | near parity | \"near parity on Qwen\" | SS gap ~1.3× | ✅ | registry: d048_eval_ss_s42 gap_ratio=1.29 |\n| 7 | substantially | \"substantially on Llama\" | SS gap 2.9× | ✅ | registry: p1_llama_ss_eval tf_ar_gap=2.87 |\n\n### Introduction\n\n| # | 数字 | 上下文 | 来源 | 状态 | 备注 |\n|---|------|--------|------|------|------|\n| 8 | 12 | \"12 models\" (Dongre citation) | external citation | ✅ | 引用数据，非本实验 |\n| 9 | over 70% | \"goal attention drops by over 70%\" | registry: phase1_gar_diag relative_drop=0.708 (70.8%) | ✅ | |\n| 10 | five turns | \"within just five turns\" | phase1_gar_diag: 5 conv × 10 turns, drop computed by turn 5 | ✅ | |\n| 11 | AUC = 0.98 | \"residual stream probes (AUC = 0.98)\" | **无 registry 记录** | ⚠️ | 未找到对应实验；可能在早期探索中完成但未注册 |\n| 12 | 85–90% | \"decays 85–90% across turns\" | registry: analysis_attention_heatmap base_decay=0.875; llama_phase1_gar_diag t1_t10_decay=90.1% | ✅ | 87.5%–90.1% 覆盖范围正确 |\n| 13 | GAR≈0.50 | \"all variants reach GAR≈0.50\" | registry: phase2_4way_eval_heldout tg=0.5035, ug=0.5053, lora=0.4978 | ✅ | |\n| 14 | 8–17× | \"collapses GAR by 8–17×\" | d048_final_ar_eval: TG 0.50/0.064=7.8→8, PCGrad 0.50/0.030=16.7→17 | ✅ | |\n| 15 | 7.8× | \"gap from 7.8×\" | TG: TF 0.50 / AR 0.064 = 7.8125 | ✅ | fig1 script: gaps=[None, 7.8, ...] |\n| 16 | 1.3× | \"to 1.3× (Qwen)\" | 3-seed SS mean: TF/AR = 0.517/0.401 = 1.29 ≈ 1.3 | ✅ | |\n| 17 | ~27× | \"~27× to 2.9× (Llama)\" | Llama TG: TF 0.484 / AR median 0.018 = 26.9 ≈ 27 | ✅ | registry: eval_llama_ar_n20 tg median=0.0179 |\n| 18 | 2.9× | \"to 2.9× (Llama)\" | p1_llama_ss_eval: tf_ar_gap=2.87 ≈ 2.9 | ✅ | |\n| 19 | 1.5B–8B | \"model scales (1.5B–8B)\" | Qwen-2.5-1.5B to Llama-3.1-8B | ✅ | 1.5B 仅在附录中交叉验证 |\n| 20 | seven | \"seven loss-formulation iterations\" | v1,v2,v3,v3b,v5,v6,v7 = 7 iterations | ✅ | tab:loss-iterations 确认 |\n| 21 | p = 0.002 | \"PCGrad modus tollens (p = 0.002)\" | tab:stat-tests: PCGrad vs TG p=0.002 | ✅ | |\n| 22 | ~1.3× | \"~1.3× on Qwen\" | same as #16 | ✅ | |\n| 23 | ~2.9× | \"~2.9× on Llama\" | same as #18 | ✅ | |\n| 24 | three seeds | \"robust across three seeds\" | SS seeds: 42, 123, 456 | ✅ | |\n\n### Method\n\n| # | 数字 | 上下文 | 来源 | 状态 | 备注 |\n|---|------|--------|------|------|------|\n| 25 | 0.01–0.02 | \"GAR-Dongre is diluted to ~0.01–0.02\" | tab:five-way: fine-tuned IID GAR-D = 0.01–0.02 | ✅ | |\n| 26 | 0.019–0.50 | \"GAR-ours retains range (0.019–0.50)\" | Base AR=0.019, fine-tuned TF=0.50 | ✅ | |\n| 27 | r = 0.200 | \"correlation weak (r = 0.200)\" | registry: instruction_retention_test gar_compliance_r=0.2003 | ✅ | |\n| 28 | p = 0.007 | \"p = 0.007\" | registry: instruction_retention_test gar_compliance_p=0.007 | ✅ | |\n| 29 | N = 5 | \"N = 5 conversations\" (Fig 4 caption) | registry: analysis_attention_heatmap 5 convs | ✅ | |\n| 30 | 10 turns | \"10 turns\" (Fig 4 caption) | registry: analysis_attention_heatmap 10 turns | ✅ | |\n| 31 | 77–81% | \"77–81% decay\" (Fig 4 caption) | registry: tg_decay=0.777, lora_decay=0.810 | ✅ | |\n| 32 | 3.3 pp | \"Δ = 3.3 pp\" (Fig 4 caption) | 0.810 − 0.777 = 0.033 = 3.3 pp | ✅ | |\n| 33 | 87.5% | \"Base decays 87.5%\" (Fig 4 caption) | registry: base_decay=0.875 | ✅ | |\n| 34 | 28 | \"28 layers\" (Qwen-2.5-7B) | Qwen-2.5-7B-Instruct has 28 layers | ✅ | |\n| 35 | σ(1.5)≈0.82 | \"initialized near identity\" | sigmoid(1.5) = 0.8176 ≈ 0.82 | ✅ | |\n| 36 | 16 | \"proj reduces to 16\" | hyperparams: turn_embed_dim=16, proj output=16 | ✅ | |\n| 37 | 16 | \"16-dimensional turn embedding\" | hyperparams: turn_embed_dim=16 | ✅ | |\n| 38 | 32 | \"32-dimensional input\" | 16 (proj) + 16 (emb) = 32 | ✅ | |\n| 39 | 64 | \"64-unit hidden layer\" | hyperparams: gate_hidden_dim=64 | ✅ | |\n| 40 | ~57K | \"adds ~57K parameters\" | tab:cost: ThreadGate overhead = +57K | ✅ | 与描述的架构反算有微小不一致（每层 MLP ~2.2K × 28 = ~61K），但 cost 表确认 57K |\n| 41 | <0.001% | \"<0.001% of 7B\" | 57K / 7.6B = 0.00075% < 0.001% | ✅ | |\n| 42 | 1.5 | \"biases initialized to 1.5\" | hyperparams: init_bias=1.5 | ✅ | |\n| 43 | ~82% | \"~82% pass-through\" | sigmoid(1.5) = 81.8% ≈ 82% | ✅ | |\n| 44 | 10× | \"10× learning rate multiplier\" | hyperparams: gate_lr_mult=10x | ✅ | |\n| 45 | τ = 0.5 | \"targets allocating half\" | hyperparams: gar_target=0.5 | ✅ | |\n| 46 | σ_min = 0.05 | \"minimum std threshold\" | hyperparams: min_gate_std=0.05 | ✅ | |\n| 47 | λ_GAR = λ_div = 1.0 | \"loss weights\" | hyperparams: lambda_GAR=1.0, lambda_div=1.0 | ✅ | |\n| 48 | seven | \"seven iterations\" | tab:loss-iterations: 7 rows (v1–v7) | ✅ | |\n| 49 | four | \"four loss families\" | cumulative, maximize, smooth_saturation, MSE = 4 | ✅ | |\n| 50 | five-way | \"five-way comparison\" | 5 conditions | ✅ | |\n\n### Experiments\n\n| # | 数字 | 上下文 | 来源 | 状态 | 备注 |\n|---|------|--------|------|------|------|\n| 51 | 8K | \"8K multi-turn conversations\" | hyperparams: training_data=8K; tab:dataset_stats: training=8000 | ✅ | |\n| 52 | 3 epochs | \"3 epochs\" | hyperparams: epochs=3 | ✅ | |\n| 53 | 2×10⁻⁴ | \"lr = 2×10⁻⁴\" | hyperparams: lr=2e-4 | ✅ | |\n| 54 | batch 1 | \"batch size 1\" | hyperparams: batch=1 | ✅ | |\n| 55 | grad accum 8 | \"gradient accumulation 8\" | hyperparams: grad_accum=8 | ✅ | |\n| 56 | seed 42 | \"seed 42\" | hyperparams: seed=42 | ✅ | |\n| 57 | seed 123 | \"seed 123\" | registry: v7_tg_s123 seed=123 | ✅ | |\n| 58 | ~6 hours | \"approximately 6 hours\" | tab:cost: TG=6.0h, LoRA=6.0h, UG=6.0h | ✅ | |\n| 59 | 96 GB | \"96 GB GPU\" | RTX PRO 6000 Blackwell Server Edition official spec | ✅ | registry 报告 vram_gb=102（nvidia-smi），论文用官方规格 |\n| 60 | 50 | \"50 non-overlapping conversations\" | tab:dataset_stats: held-out AR eval=50 | ✅ | |\n| 61 | 0.49–0.51 | \"GAR-ours spans 0.49–0.51\" | tab:five-way: UG IID=0.49, UG held-out=0.51 | ✅ | |\n| 62 | ≤2 pp | \"(≤2 pp)\" | 0.51 − 0.49 = 2 pp ≤ 2 pp | ✅ | |\n| 63 | 2.78 | \"PPL is 2.78 for all\" | tab:five-way: all fine-tuned held-out PPL=2.78 | ✅ | |\n| 64 | ≤1 pp | \"held-out GAR-ours differs by ≤1 pp\" | tab:five-way: UG IID=0.49 vs held-out=0.51 = 2 pp | ⚠️ | **UG 差异 ~1.3 pp（精确值），显示 2 pp（四舍五入后）。声称 ≤1 pp 不准确** |\n| 65 | 0.01–0.02 | \"GAR-Dongre remains low\" | tab:five-way: fine-tuned GAR-D 0.01–0.02 | ✅ | |\n| 66 | N = 50 | \"AR generation (N = 50)\" | d048_final_ar_eval: n_convs_total=50 | ⚠️ | **有效 N=39（≥3 turns 的对话），论文未注明** |\n| 67 | 0.019–0.064 | \"GAR-ours drops to 0.019–0.064\" | d048_final_ar_eval: base=0.019, tg=0.064 | ✅ | |\n| 68 | 8–17× | \"8–17× gap\" | 0.50/0.064=7.8→8×, 0.50/0.030=16.7→17× | ✅ | |\n| 69 | 0.064 | \"ThreadGate 0.064\" | d048_final_ar_eval: tg_gar=0.064 | ✅ | |\n| 70 | 0.037 | \"LoRA-only 0.037\" | d048_final_ar_eval: lo_gar=0.037 | ✅ | |\n| 71 | 0.033 | \"Uniform Gate 0.033\" | d048_final_ar_eval: ug_gar=0.033 | ✅ | |\n| 72 | 0.030 | \"PCGrad 0.030\" | d048_final_ar_eval: pcgrad_gar=0.030 | ✅ | |\n| 73 | 0.019 | \"Base 0.019\" | d048_final_ar_eval: base_gar=0.019 | ✅ | |\n| 74 | p = 0.004 | \"TG vs LoRA-only (p = 0.004)\" | tab:stat-tests: TG vs LoRA-only p=0.004 | ✅ | |\n| 75 | 7.8× | \"gap remains 7.8×\" | 0.50/0.064 = 7.8125 | ✅ | |\n| 76 | 0.504±0.001 | \"second seed TF stability\" | tab:perseed-tg: s42=0.504, s123=0.505, mean=0.504±0.001 | ✅ | |\n| 77 | 0.8 pp | \"MMLU within 0.8 pp\" | tab:mmlu: max delta = UG -0.77 pp < 0.8 pp | ✅ | |\n| 78 | 0.064 | \"GAR from 0.064\" (Fig 5 caption) | attention_steering_gen_n50: beta_0.0 mid_gar=0.0641 | ✅ | |\n| 79 | 0.727 | \"to 0.727\" (Fig 5 caption) | attention_steering_gen_n50: beta_5.0 mid_gar=0.7271 | ✅ | |\n| 80 | 9% | \"9% PPL cost at β=3\" | β=0 PPL 1.432, β=3 PPL 1.561; (1.561−1.432)/1.432=9.0% | ✅ | |\n| 81 | β∈[2,3] | \"phase transition at β∈[2,3]\" | gen_n50: β=2 GAR=0.128, β=3 GAR=0.556 | ✅ | |\n| 82 | β=0→2 | \"β∈[0,2] yields marginal improvement\" | gen_n50: β=0 GAR=0.064, β=2 GAR=0.128 | ✅ | |\n| 83 | β=3 | \"β=3 triggers phase transition\" | gen_n50: β=3 GAR=0.5558 | ✅ | |\n| 84 | 0.556 | \"GAR = 0.556\" | gen_n50: beta_3.0 mid_gar=0.5558 → 0.556 | ✅ | |\n| 85 | 9% PPL | \"9% PPL cost\" | same as #80 | ✅ | |\n| 86 | β=5 | \"At β=5\" | | ✅ | |\n| 87 | 0.727±0.061 | \"GAR 0.727±0.061\" | gen_n50: beta_5.0 mid_gar=0.7271±0.0605 → 0.727±0.061 | ✅ | |\n| 88 | PPL 1.77 | \"PPL 1.77\" | gen_n50: beta_5.0 ppl=1.7723 → 1.77 | ✅ | |\n| 89 | β∈[3,5] | \"operating region β∈[3,5]\" | | ✅ | |\n| 90 | below 1.8 | \"PPL remains below 1.8\" | β=5 PPL mean=1.77 < 1.8 | ✅ | |\n| 91 | +11.1 pp | \"raises compliance by +11.1 pp\" | registry: instruction_retention_test late_turn_delta=0.111 | ✅ | |\n| 92 | p = 0.077 | \"does not reach significance (p = 0.077)\" | registry: mcnemar_p=0.0771 → 0.077 | ✅ | |\n| 93 | +23.8 pp | \"content-constrained +23.8 pp\" | registry: category_content_constraint delta=0.238 | ✅ | |\n| 94 | 7.8× | \"gap from 7.8×\" (Fig SS caption) | same as #75 | ✅ | |\n| 95 | ~1.3× | \"to ~1.3×\" (Fig SS caption) | same as #16 | ✅ | |\n| 96 | five | \"five training conditions\" (Fig SS caption) | 5 conditions in main testbed | ✅ | |\n| 97 | 0.401±0.047 | \"AR GAR-ours rises to 0.401±0.047\" | tab:perseed-ss: seeds [0.347,0.423,0.433] mean=0.401 std=0.047 | ✅ | |\n| 98 | 7.8× to ~1.3× | \"compressing gap from 7.8× to ~1.3×\" | TG gap=7.8, SS gap=1.29≈1.3 | ✅ | |\n| 99 | 0.498±0.004 | \"TF GAR 0.498±0.004\" | tab:perseed-ss: s42=0.502, s123=0.554, s456=0.496 → mean=0.517±0.032 | ❌ | **重大问题：论文 0.498±0.004 与 perseed 表 0.517±0.032 矛盾。0.498 可能仅用 s42+s456 两个种子（排除 s123），或来自不同实验版本（eval_v8b_ss iid_gar=0.4983）** |\n| 100 | 1.441±0.001 | \"no PPL cost (1.441±0.001)\" | tab:perseed-ss: PPL [1.442,1.441,1.439] mean=1.441 std=0.0016 | ⚠️ | std 应为 0.002 而非 0.001（四舍五入导致） |\n| 101 | β=5: 0.717±0.001 | \"steering std 0.047→0.001\" | tab:perseed-ss: β=5 [0.717,0.717,0.716] mean=0.717 std=0.001 | ✅ | |\n| 102 | 0.047→0.001 | \"seed variance std 0.047→0.001\" | β=0 std=0.047, β=5 std=0.001 | ✅ | |\n| 103 | above 0.36 | \"mid-turn GAR above 0.36\" | tab:gar-robust: SS values [0.458, 0.366, 0.412, 0.444] all >0.36 | ✅ | |\n| 104 | ~27× | \"gap from ~27×\" (Llama) | Llama TG: TF 0.484 / AR median 0.018 = 26.9 | ✅ | |\n| 105 | 2.9× | \"to 2.9×\" (Llama SS) | p1_llama_ss_eval: tf_ar_gap=2.87 ≈ 2.9 | ✅ | |\n| 106 | 2 vs 3 | \"fewer epochs (2 vs 3)\" | tab:llama-vs-qwen-ss: Llama SS 2 epochs, Qwen SS 3 epochs | ✅ | Llama 训练 3 epochs 但 eval 用 epoch_1 checkpoint |\n\n### Analysis\n\n| # | 数字 | 上下文 | 来源 | 状态 | 备注 |\n|---|------|--------|------|------|------|\n| 107 | 27/28 | \"27/28 layers gates invert\" | Wilcoxon 配对检验 28 层，27 层显示方向一致 | ✅ | |\n| 108 | p=3.73×10⁻⁸ | \"Wilcoxon p=3.73×10⁻⁸\" | tab:stat-tests: Turn 1 vs Turn 21 p=3.7e-8 | ✅ | |\n| 109 | r=0.975 | \"effect size r=0.975\" | tab:stat-tests: r=0.975 | ✅ | |\n| 110 | L23: 0.769→0.979 | \"layer 23 shifts from 0.769 to 0.979\" | gen_fig3: L23 turn1=0.7693, turn21=0.9793 | ✅ | 正确四舍五入 |\n| 111 | 0.93–0.98 | \"inference-time values 0.93–0.98\" | gate profiles: range across layers | ✅ | |\n| 112 | 2–7% | \"2–7% attenuation\" | 1−0.98=2%, 1−0.93=7% | ✅ | |\n| 113 | L3=0.777 | \"UG: L3=0.777\" | registry: phase2_ug_s42 final_profile L3=0.777 | ✅ | |\n| 114 | L27=1.000 | \"UG: L27=1.000\" | registry: phase2_ug_s42 final_profile L27=1 | ✅ | |\n| 115 | 68–79% | \"oppose in 68–79% of layers\" | registry: epoch0=78.6%, epoch2=67.9% → 68–79% | ✅ | |\n| 116 | −0.089→−0.042 | \"cosine similarity −0.089→−0.042\" | registry: epoch0_cos_sim=-0.089, epoch2_cos_sim=-0.042 | ✅ | |\n| 117 | 7.5× to 14.7× | \"NTP magnitude dominance 7.5× to 14.7×\" | registry: epoch0_mag_ratio=7.5, epoch2_mag_ratio=14.7 | ✅ | |\n| 118 | 0.064→0.030 | \"AR GAR worsens: 0.064→0.030\" | d048_final_ar_eval: tg=0.064, pcgrad=0.030 | ✅ | |\n| 119 | p=0.002 | \"PCGrad worsening (p=0.002)\" | tab:stat-tests: PCGrad vs TG p=0.002 | ✅ | |\n| 120 | 7.5–14.7× | \"magnitude imbalance 7.5–14.7×\" | same as #117 | ✅ | |\n| 121 | cos=+0.005 | \"Llama near-orthogonal (cos=+0.005)\" | registry: p2_llama_gradient_conflict cos_sim_mean=0.0045 → 0.005 | ✅ | |\n| 122 | 25.7× | \"25.7× NTP magnitude dominance\" | registry: p2_llama_gradient_conflict mag_ratio_median=25.7 | ✅ | |\n| 123 | 0.01–0.02 | \"GAR-Dongre uniformly low (0.01–0.02)\" | multiple sources confirm | ✅ | |\n| 124 | τ=0.5 | \"TF GAR-ours remains near τ=0.5\" | | ✅ | |\n| 125 | 77–87% | \"77–87% per-turn decay\" | tg_decay=0.777 (77%) to base_decay=0.875 (87%) | ✅ | |\n| 126 | TRC 0.334/0.332 | \"TF/AR TRC = 0.334/0.332 for TG\" | registry: trc_baseline_v7_tg tf_trc=0.3339, gen_trc=0.3323 | ✅ | 四舍五入 0.334/0.332 |\n| 127 | gap +0.002 | \"TRC gap +0.002\" | 0.3339−0.3323=0.0016; 显示值 0.334−0.332=0.002 | ✅ | 四舍五入伪影，可接受 |\n| 128 | 0.349/0.411 | \"TRC = 0.349/0.411 for LoRA-only\" | registry: lora tf_trc=0.349, gen_trc=0.4106 | ✅ | |\n| 129 | gap −0.062 | \"TRC gap −0.062, reversed\" | registry: trc_gap=-0.0617 → −0.062 | ✅ | |\n| 130 | 1.002× | \"Llama GAR-Dongre shift 1.002×\" | registry: llama_ar_matched_eval gar_dongre_raw_gap=\"1.002x\" | ✅ | |\n| 131 | 1.28× | \"Qwen GAR-Dongre shift 1.28×\" | TF dongre 0.0152, AR dongre 0.0194; 0.0194/0.0152=1.28 | ✅ | |\n| 132 | N=20 | \"Llama N=20\" | registry: eval_llama_ar_n20 n_conversations=20 | ✅ | |\n| 133 | 4 turns | \"4 turns\" | registry: eval_llama_ar_n20 n_turns=4 | ✅ | |\n| 134 | 0.484 (TG) | \"TF GAR 0.484 (TG)\" | registry: llama_eval_s42 tf_tg gar_ours=0.4836 → 0.484 | ✅ | |\n| 135 | 0.481 (LoRA) | \"TF GAR 0.481 (LoRA-only)\" | registry: eval_llama_lora_only_s42 tf gar_ours=0.4807 → 0.481 | ✅ | |\n| 136 | CoV>100% | \"coefficient of variation >100%\" | eval_llama_ar_n20: std/mean = 0.1002/0.0434 = 231% | ✅ | |\n| 137 | 0.018 (TG+LoRA) | \"medians: 0.018\" | eval_llama_ar_n20: tg median=0.0179, lora median=0.0184 → both ≈0.018 | ✅ | |\n| 138 | 0.009 (Base) | \"medians: 0.009 (Base)\" | eval_llama_ar_n20: base median=0.0093 → 0.009 | ✅ | |\n| 139 | 27× and 26× | \"gaps of 27× and 26×\" | TG: 0.484/0.0179=27.0×; LoRA: 0.481/0.0184=26.1→26× | ✅ | |\n| 140 | L1=0.793 | \"Qwen L1=0.793\" | gen_fig_crossmodel: qwen_gates[1]=0.793; registry v7_tg_s123 L1=0.793 | ✅ | |\n| 141 | L25=0.719 | \"Llama L25=0.719\" | gen_fig_crossmodel: llama_gates[25]=0.719; registry llama_tg_s42 L25=0.719 | ✅ | |\n| 142 | ~27× to 2.9× | \"Llama gap ~27× to 2.9×\" | same as #104, #105 | ✅ | |\n| 143 | TF 0.477 | \"Llama SS TF GAR 0.477\" | p1_llama_ss_eval: ss_tf_gar=0.477 | ✅ | |\n| 144 | AR 0.166 | \"Llama SS AR GAR 0.166\" | p1_llama_ss_eval: ss_ar_b0_gar=0.1662 → 0.166 | ✅ | |\n| 145 | 2 vs 3 | \"fewer epochs (2 vs 3)\" | same as #106 | ✅ | |\n| 146 | β=3: 0.593 | \"β=3 triggers on Qwen SS (0.593)\" | d048_final_ar_eval: ss_gar beta3=0.593 | ✅ | |\n| 147 | β=3: 0.173 | \"not Llama SS (0.173)\" | tab:llama-ss-steering: β=3 AR GAR=0.173 | ⚠️ | registry 中无 Llama SS β=3 记录；仅附录表有此值，无法追溯到具体实验 |\n| 148 | β=5: 0.791 | \"Llama β=5 GAR 0.791\" | p1_llama_ss_eval: ss_ar_b5_gar=0.7905 → 0.791 | ✅ | 正确四舍五入 |\n| 149 | Qwen SS 0.717 | \"exceeding Qwen SS 0.717\" | tab:perseed-ss: β=5 mean=0.717 | ✅ | |\n| 150 | 79.8% | \"Qwen-1.5B 79.8% GAR decay\" | tab:qwen15b_results: relative_drop=79.8% | ✅ | |\n| 151 | 0.715 | \"β-steering recovery to 0.715\" | tab:1.5b-steering: TG β=5 GAR=0.715 | ✅ | |\n\n### Discussion\n\n| # | 数字 | 上下文 | 来源 | 状态 | 备注 |\n|---|------|--------|------|------|------|\n| 152 | ≤1.3× | \"GAR-Dongre shift ≤1.3×\" | Qwen 1.28×, Llama 1.002× | ✅ | |\n| 153 | r=0.743 | \"per-head correlation r=0.743\" | tab:kl-perhead: Corr(TF_GAR, Delta-GAR) TG=0.743 | ✅ | |\n| 154 | 7.5–25.7× | \"NTP dominance 7.5–25.7×\" | Qwen: 7.5–14.7×, Llama: 25.7× | ✅ | |\n| 155 | r=0.200 | \"GAR-compliance r=0.200\" | same as #27 | ✅ | |\n| 156 | β=5 | \"At β=5 the two converge\" | | ✅ | |\n| 157 | SS=0.717 | \"SS = 0.717\" | tab:perseed-ss β=5 mean | ✅ | |\n| 158 | TG=0.727 | \"TG = 0.727\" | gen_n50: beta_5.0 mid_gar=0.7271 | ✅ | |\n\n### Conclusion\n\n| # | 数字 | 上下文 | 来源 | 状态 | 备注 |\n|---|------|--------|------|------|------|\n| 159 | GAR=0.50 | \"converge under TF (GAR=0.50)\" | multiple sources | ✅ | |\n| 160 | order of magnitude | \"collapse by an order of magnitude\" | 8–27× gap | ✅ | |\n| 161 | two architectures | \"two architectures\" | Qwen + Llama | ✅ | |\n| 162 | ~1.3× | \"~1.3× (Qwen)\" | same as #16 | ✅ | |\n| 163 | ~2.9× | \"~2.9× (Llama)\" | same as #18 | ✅ | |\n\n### Limitations\n\n| # | 数字 | 上下文 | 来源 | 状态 | 备注 |\n|---|------|--------|------|------|------|\n| 164 | two model families | \"two model families\" | Qwen + Llama | ✅ | |\n| 165 | Qwen-2.5-7B | model name | external | ✅ | |\n| 166 | Llama-3.1-8B | model name | external | ✅ | |\n| 167 | 8K conversations | \"8K conversations\" | same as #51 | ✅ | |\n| 168 | three seeds | \"three seeds\" (SS) | seeds 42, 123, 456 | ✅ | |\n\n---\n\n## 问题清单\n\n### 重大问题（影响论文可信度）\n\n**1. [Experiments §4.4] TF GAR 0.498±0.004 — 与 per-seed 数据矛盾**\n\n- 论文原文: \"TF GAR 0.498±0.004\"\n- Per-seed 表 (tab:perseed-ss): s42=0.502, s123=0.554, s456=0.496 → mean=0.517, std=0.032\n- 不一致来源推测: 0.498 可能来自旧版 SS 实验 (eval_v8b_ss: iid_gar_ours=0.4983≈0.498)，或仅用 s42+s456 两个种子 (mean=0.499≈0.498, std=0.004)。无论哪种，与 \"across three seeds\" 的表述矛盾。\n- 影响: gap ratio 计算受影响，但 ~1.3× 的定性结论不变 (0.517/0.401=1.29 vs 0.498/0.401=1.24)\n- **建议**: 更新为 per-seed 表一致值。若 s123 TF GAR 异常高 (0.554)，应解释原因（N_tf=200 vs 其他种子 N_tf=50）\n\n**2. [Introduction / Figure 1] Figure 1(c) Llama TG gap 与 caption/正文不一致**\n\n- Figure 1(c) 脚本 (gen_fig1_3panel.py): Llama TG gap = **12.5×** (mean-based: TF 0.484 / AR mean 0.039)\n- Figure 1 caption: \"~27× to 2.9× (Llama)\"\n- 正文 Analysis §5.5: \"gaps of 27× and 26×\" (median-based: TF 0.484 / AR median 0.018)\n- Cross-model figure (gen_fig_crossmodel.py): 正确使用 27× (median)\n- **不一致**: Figure 1(c) 柱状图显示 12.5× 但 caption 标注 ~27×。读者看到的图与 caption 矛盾。\n- **建议**: 统一使用 median (27×) 或在 Figure 1(c) 中也用 median。需更新 gen_fig1_3panel.py 中 `gaps_c = [7.8, 1.3, 12.5, 2.9]` 的 12.5 为 27，同时调整 x 轴范围。\n\n### 中等问题\n\n**3. [Experiments §4.2] \"held-out GAR-ours differs by ≤1 pp\" — 实际 UG 差异 ~1.3 pp**\n\n- tab:five-way: UG IID GAR-ours=0.49, Held-out=0.51 (显示差 2 pp)\n- Registry 精确值: phase2_4way_eval_heldout ug=0.5053; IID eval ug 来源不明（可能 ~0.493）\n- 无论如何，差异超过 1 pp\n- **建议**: 改为 \"differs by ≤2 pp\" 或 \"differs by $\\leq$1.3\\,pp\"\n\n**4. [Introduction] AUC = 0.98 — 无法从 registry 验证**\n\n- \"residual stream probes confirm that goal information persists (AUC = 0.98)\"\n- Registry 60 个实验中无 probing 实验记录\n- 可能在早期探索中完成但未注册\n- **建议**: 补充 probing 实验到 registry，或在论文中标注来源\n\n**5. [Experiments §4.2] N=50 实际有效 N=39**\n\n- 论文标注 \"N=50\" 用于 AR 生成评估\n- Registry d048_final_ar_eval: n_convs_total=50, n_convs_valid=39 (11 conversations 不满足 ≥3 turns)\n- 统计检验和 CI 基于 39 个有效样本\n- **建议**: 在正文注明有效样本量，如 \"N=50 (39 with ≥3 valid turns)\" 或在附录说明\n\n**6. [Analysis §5.5] Llama SS β=3 = 0.173 — 无 registry 对应记录**\n\n- tab:llama-ss-steering 表中有 β=3 AR GAR=0.173\n- p1_llama_ss_eval registry 仅记录 β=0 (0.166) 和 β=5 (0.791)\n- β=3 数据的具体来源不可追溯\n- **建议**: 将 β=3 评估结果补充到 registry\n\n### 轻微问题\n\n**7. [Experiments §4.4] PPL std 0.001 应为 0.002**\n\n- Per-seed PPL: [1.442, 1.441, 1.439], std=0.0016 ≈ 0.002\n- 论文写 ±0.001\n- 影响可忽略\n\n**8. [Figure 3b title] \"20–33×\" 实际范围为 20–34×**\n\n- gen_fig3_gate_shift.py panel (b): UG gap = 0.5053/0.0149 = 33.9× → 应取 34\n- 影响极小：图标题而非正文数据\n\n**9. [Figure gen_fig_ss_multiseed.py] β=5 s456 值 0.718 vs registry 0.716**\n\n- 脚本硬编码 seeds_b5 = [0.716, 0.717, 0.718]\n- Registry d048_eval_ss_s456: ar_beta5_gar=0.7157 → 四舍五入应为 0.716\n- 脚本中 s456 用了 0.718，与 registry 0.7157 不符（差 0.002）\n- 不影响均值（0.717）和 std（0.001）\n\n---\n\n## 交叉一致性检查\n\n### 跨章节引用一致性\n\n| 数字 | 出现位置 | 一致性 |\n|------|----------|--------|\n| 7.8× (TG gap) | Abstract, Intro, Experiments, Analysis, Conclusion, Fig 1 | ✅ 全部一致 |\n| ~1.3× (Qwen SS) | Abstract, Intro, Experiments, Conclusion, Fig caption | ✅ 全部一致 |\n| ~2.9× (Llama SS) | Abstract, Intro, Experiments, Analysis, Conclusion | ✅ 全部一致 |\n| 8–17× (gap range) | Intro, Experiments, Analysis Fig 3 caption | ✅ 全部一致 |\n| p=0.002 (PCGrad) | Intro (contribution), Analysis, stat-tests | ✅ 全部一致 |\n| ~27× (Llama TG) | Intro, Analysis text, crossmodel figure | ✅ 文本一致 |\n| ~27× (Llama TG) | Figure 1(c) script | ❌ **图中用 12.5× (mean)，与文本 27× (median) 不一致** |\n| 0.498 (SS TF GAR) | Experiments text, tab:llama-vs-qwen-ss, tab:crossmodel-detail | ✅ 文本/表格一致 |\n| 0.498 (SS TF GAR) | tab:perseed-ss | ❌ **per-seed 表显示 0.517±0.032** |\n\n### 图表脚本 vs Registry 一致性\n\n| 图表 | 脚本数据 | Registry 来源 | 一致性 |\n|------|----------|---------------|--------|\n| Fig 1(a) Qwen per-turn | gen_fig1_3panel: 10 values | phase1_gar_diag: per_turn_avg_gar | ✅ 完全匹配 |\n| Fig 1(a) Llama per-turn | gen_fig1_3panel: 10 values | llama_phase1_gar_diag: per_turn_gar | ✅ 完全匹配 |\n| Fig 1(b) TF/AR bars | gen_fig1_3panel: 5 configs | d048_final_ar_eval + phase2_4way_eval_heldout | ✅ 完全匹配 |\n| Fig 1(c) SS gaps | gen_fig1_3panel: 4 bars | mixed: Qwen ✅, Llama TG ⚠️ uses mean not median | ⚠️ 见问题 #2 |\n| Fig 3(a) gate values | gen_fig3_gate_shift: 5 layers × 2 turns | 无直接 registry 记录（需 WandB 验证） | ⚠️ 需验证 |\n| Fig 3(b) pilot gaps | gen_fig3_gate_shift: 5 configs | phase2_tg_s42_v7 + 其他 eval_modelgen | ✅ 匹配 |\n| Fig 4 decay curves | gen_fig4: 4 configs | analysis_attention_heatmap | ✅ 匹配 |\n| Fig 5 steering | gen_fig5: 2 panels | attention_steering_v7_tg_gen + gen_n50 | ✅ 完全匹配 |\n| Crossmodel gates | gen_fig_crossmodel: 28+32 values | v7_tg_s123 + llama_tg_s42 | ✅ 完全匹配 |\n| SS multiseed | gen_fig_ss_multiseed: 6 values | d048_final_ar_eval + d048_eval_ss_s123/s456 | ⚠️ s456 β=5 差 0.002 |\n\n---\n\n## 总结\n\n**审计结论**: 论文主体 168 个数字中，161 个（95.8%）与 registry/脚本完全吻合或在合理四舍五入范围内。发现 2 个重大问题和 4 个中等问题需要修正。\n\n**优先修复**:\n1. 🔴 统一 SS TF GAR 报告值（0.498 vs 0.517）与 per-seed 表\n2. 🔴 修复 Figure 1(c) Llama TG gap（12.5× → 27×）使图文一致\n3. 🟡 修正 \"≤1 pp\" 为 \"≤2 pp\" 或确认精确值\n4. 🟡 补充 AUC=0.98 probing 实验到 registry\n5. 🟡 注明 AR eval 有效 N=39/50\n6. 🟡 补充 Llama SS β=3 评估到 registry\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 172_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01BvaPioceS5ndvNhGChhsL3`</summary>

```json
{
  "todos": [
    {
      "content": "Audit Abstract numbers",
      "status": "completed",
      "activeForm": "Auditing Abstract numbers"
    },
    {
      "content": "Audit Introduction numbers",
      "status": "completed",
      "activeForm": "Auditing Introduction numbers"
    },
    {
      "content": "Audit Method numbers",
      "status": "completed",
      "activeForm": "Auditing Method numbers"
    },
    {
      "content": "Audit Experiments numbers",
      "status": "completed",
      "activeForm": "Auditing Experiments numbers"
    },
    {
      "content": "Audit Analysis numbers",
      "status": "completed",
      "activeForm": "Auditing Analysis numbers"
    },
    {
      "content": "Audit Discussion numbers",
      "status": "completed",
      "activeForm": "Auditing Discussion numbers"
    },
    {
      "content": "Audit Conclusion numbers",
      "status": "completed",
      "activeForm": "Auditing Conclusion numbers"
    },
    {
      "content": "Audit Limitations numbers",
      "status": "completed",
      "activeForm": "Auditing Limitations numbers"
    },
    {
      "content": "Write audit report to artifacts/audit_body_text.md",
      "status": "completed",
      "activeForm": "Writing audit report"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "de65498d-b381-47d3-aa4b-883d8ffa3c85",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jg8nJuEJHTEjP18Natd3Mu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13399,
      "cache_read_input_tokens": 109107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13399
      },
      "output_tokens": 32,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-25T20:32:02.065Z_

<details><summary>↩ Tool result · `toolu_01BvaPioceS5ndvNhGChhsL3`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "fe3f70f7-2c94-4c4e-9075-9994b556d891",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Audit Abstract numbers",
        "status": "completed",
        "activeForm": "Auditing Abstract numbers"
      },
      {
        "content": "Audit Introduction numbers",
        "status": "completed",
        "activeForm": "Auditing Introduction numbers"
      },
      {
        "content": "Audit Method numbers",
        "status": "completed",
        "activeForm": "Auditing Method numbers"
      },
      {
        "content": "Audit Experiments numbers",
        "status": "completed",
        "activeForm": "Auditing Experiments numbers"
      },
      {
        "content": "Audit Analysis numbers",
        "status": "completed",
        "activeForm": "Auditing Analysis numbers"
      },
      {
        "content": "Audit Discussion numbers",
        "status": "completed",
        "activeForm": "Auditing Discussion numbers"
      },
      {
        "content": "Audit Conclusion numbers",
        "status": "completed",
        "activeForm": "Auditing Conclusion numbers"
      },
      {
        "content": "Audit Limitations numbers",
        "status": "completed",
        "activeForm": "Auditing Limitations numbers"
      },
      {
        "content": "Write audit report to artifacts/audit_body_text.md",
        "status": "in_progress",
        "activeForm": "Writing audit report"
      }
    ],
    "newTodos": [
      {
        "content": "Audit Abstract numbers",
        "status": "completed",
        "activeForm": "Auditing Abstract numbers"
      },
      {
        "content": "Audit Introduction numbers",
        "status": "completed",
        "activeForm": "Auditing Introduction numbers"
      },
      {
        "content": "Audit Method numbers",
        "status": "completed",
        "activeForm": "Auditing Method numbers"
      },
      {
        "content": "Audit Experiments numbers",
        "status": "completed",
        "activeForm": "Auditing Experiments numbers"
      },
      {
        "content": "Audit Analysis numbers",
        "status": "completed",
        "activeForm": "Auditing Analysis numbers"
      },
      {
        "content": "Audit Discussion numbers",
        "status": "completed",
        "activeForm": "Auditing Discussion numbers"
      },
      {
        "content": "Audit Conclusion numbers",
        "status": "completed",
        "activeForm": "Auditing Conclusion numbers"
      },
      {
        "content": "Audit Limitations numbers",
        "status": "completed",
        "activeForm": "Auditing Limitations numbers"
      },
      {
        "content": "Write audit report to artifacts/audit_body_text.md",
        "status": "completed",
        "activeForm": "Writing audit report"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 174_

审计完成。报告已写入 `artifacts/audit_body_text.md`。

**168 个数字中 161 个验证通过（95.8%），发现 9 个问题：**

**2 个重大问题：**
1. **SS TF GAR 0.498±0.004** — per-seed 表显示 0.517±0.032，值和标准差都不匹配。疑似仅用 2 个种子或来自旧版实验（eval_v8b_ss）
2. **Figure 1(c) Llama TG gap** — 图中柱状图显示 12.5×（mean-based），但 caption 和正文均写 ~27×（median-based），图文矛盾

**4 个中等问题：**
3. "held-out GAR differs by ≤1 pp" — UG 实际差 ~1.3 pp
4. AUC=0.98（residual stream probes）— registry 无对应实验记录
5. AR eval 标注 N=50 但有效 N=39
6. Llama SS β=3=0.173 无 registry 可追溯记录

**3 个轻微问题：** PPL std 四舍五入、图标题范围、multiseed 脚本末位数字偏差。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "f3033577-28db-4bef-afbb-c3060efd87ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjvNHWEcf6AGXKfYU8cmoK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 350,
      "cache_read_input_tokens": 122506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 350
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 175_

审计完成。报告已写入 `artifacts/audit_body_text.md`。

**168 个数字中 161 个验证通过（95.8%），发现 9 个问题：**

**2 个重大问题：**
1. **SS TF GAR 0.498±0.004** — per-seed 表显示 0.517±0.032，值和标准差都不匹配。疑似仅用 2 个种子或来自旧版实验（eval_v8b_ss）
2. **Figure 1(c) Llama TG gap** — 图中柱状图显示 12.5×（mean-based），但 caption 和正文均写 ~27×（median-based），图文矛盾

**4 个中等问题：**
3. "held-out GAR differs by ≤1 pp" — UG 实际差 ~1.3 pp
4. AUC=0.98（residual stream probes）— registry 无对应实验记录
5. AR eval 标注 N=50 但有效 N=39
6. Llama SS β=3=0.173 无 registry 可追溯记录

**3 个轻微问题：** PPL std 四舍五入、图标题范围、multiseed 脚本末位数字偏差。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1209503,
  "duration_api_ms": 1404260,
  "num_turns": 26,
  "stop_reason": "end_turn",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "total_cost_usd": 4.10678125,
  "usage": {
    "input_tokens": 8833,
    "cache_creation_input_tokens": 124855,
    "cache_read_input_tokens": 524960,
    "output_tokens": 45120,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 124855,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 363,
        "cache_read_input_tokens": 122506,
        "cache_creation_input_tokens": 350,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 350
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1515,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00159,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8860,
      "outputTokens": 72726,
      "cacheReadInputTokens": 1272095,
      "cacheCreationInputTokens": 257071,
      "webSearchRequests": 0,
      "costUSD": 4.105191250000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "82453589-a6df-4a2e-aadd-8fc2e20a785a"
}
```

</details>

---
