# Research conversation: <project_context> # 项目: recovery_aware_struct_prune ## 运行环境 - 服务器名: westb-23072 - SSH 账户: root（调用 ssh_execute / submit_t — Part 2 of 2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-project-context-recovery-aware-struct-prune-westb-23072-ssh-root-ssh-execute-s-copy-516.md) · [Structured JSON](../../../sessions/bd/bd284532baf56f89213a.json)

## Round 1

### Tool result

_source line 85 · 2026-05-23T11:02:52.692Z_

<details><summary>↩ Tool result · `toolu_01SW8KXJo9vfu8VurdvkLYqQ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/data_provenance_audit.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6515c16e-71ed-4b43-b0fa-66232255205f",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "6c7f0f52-b672-4321-8d39-7f226aea7dbb",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/data_provenance_audit.md",
    "content": "# Data Provenance Audit — recovery_aware_struct_prune\n\nGenerated: 2026-05-23\n\n**Convention:**\n- **Script**: NEW = created ≥ 2026-05-23 (pred_answer/gold_answer format); OLD = before that date\n- **Seed**: single seed (42) unless noted; multi-seed results show individual seeds and mean\n- ⚠️ = discrepancy or missing registry record\n\n---\n\n## Table 1: Recovery Capacity Spectrum (`tab1_recovery_gradient.tex`)\n\nGRPO dynamics at 20% sparsity, 100 steps. Reward metrics from GRPO training runs.\n\n| Row | Column | Paper Value | Registry exp_id | Server | Script | Seed |\n|-----|--------|-------------|-----------------|--------|--------|------|\n| CKA-only | Peak Rew. | 0.354 | `grpo_cka_only_20` (peak_reward=0.3544) | westb-23072 | OLD (2026-05-17) | 42 |\n| CKA-only | Mean Rew. | 0.285 | `grpo_cka_only_20` (computed from reward curve) | westb-23072 | OLD | 42 |\n| CKA-only | Min f₀ | 0.125 | `grpo_cka_only_20` (from training logs) | westb-23072 | OLD | 42 |\n| Random | Peak Rew. | 0.190 | `grpo_random_20` (reward_peak=0.19) | westb-23072 | OLD (2026-05-17) | 42 |\n| Random | Mean Rew. | 0.164 | `grpo_random_20` (reward_final=0.164) | westb-23072 | OLD | 42 |\n| Random | Min f₀ | 0.300 | `grpo_random_20` (from training logs) | westb-23072 | OLD | 42 |\n| Standard | Peak Rew. | 0.081 | `grpo_standard_20_fair` (peak_reward=0.081) | westb-23072 | OLD (2026-05-18) | 42 |\n| Standard | Mean Rew. | 0.050 | `grpo_standard_20_fair` (final_reward=0.054) | westb-23072 | OLD | 42 |\n| Standard | Min f₀ | 0.500 | `grpo_standard_20_fair` (from training logs) | westb-23072 | OLD | 42 |\n| RASP (α=1.0) | Peak Rew. | 0.061 | `grpo_rasp_20_fair` (peak_reward=0.061) | westb-23072 | OLD (2026-05-17) | 42 |\n| RASP (α=1.0) | Mean Rew. | 0.031 | `grpo_rasp_20_fair` (final_reward=0.01) | westb-23072 | OLD | 42 |\n| RASP (α=1.0) | Min f₀ | 0.675 | `grpo_rasp_20_fair` (from training logs) | westb-23072 | OLD | 42 |\n\n**Result file paths** (GRPO training outputs):\n- CKA-only: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/`\n- Random: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/`\n- Standard: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_fair/`\n- RASP: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_fair/`\n\n---\n\n## Table 2: Reward-Accuracy Decoupling (`tab2_decoupling.tex`)\n\nGSM8K (N=1,319) accuracy. Multi-seed mean ± std for CKA-only, Standard, Random.\n\n| Row | SFT Acc.(%) | GRPO Acc.(%) | Δ(pp) | Peak Rew. | Registry exp_id (SFT) | Registry exp_id (GRPO) | Seed |\n|-----|-------------|--------------|-------|-----------|----------------------|----------------------|------|\n| Unpruned | 81.27 | 81.27 | 0.00 | 0.669 | `eval_sft_unpruned_full` (westd-11672, 2026-05-16) | `eval_grpo_unpruned_v2_step100` (westd-11672, 2026-05-16) | 42 |\n| CKA-only 20% | 63.91 | 64.39±0.19 | +0.48 | 0.354 | `eval_gsm8k_sft_cka_only_20` (westd-29022, 2026-05-20) | 3-seed mean: see Table below | 3 seeds |\n| Standard 20% | 59.29 | 59.84±0.38 | +0.55 | 0.081 | `eval_sft_standard_full_westd` (westd-11672, 2026-05-15) | 3-seed mean: see Table below | 3 seeds |\n| RASP (α=1.0) 20% | 61.49 | 60.88 | −0.61 | 0.061 | `eval_gsm8k_sft_rasp_20` (westd-29022, 2026-05-20) | `eval_gsm8k_grpo_rasp_20_fair` (westd-29022, 2026-05-19) | 42 |\n| Random 20% | 51.25 | 50.72±0.15 | −0.53 | 0.190 | `eval_gsm8k_sft_random_20` (westd-29022, 2026-05-21) | 3-seed mean: see Table below | 3 seeds |\n| ShortGPT 20% | 44.73 | 43.37 | −1.36 | -- | `eval_gsm8k_sft_shortgpt_20` (westd-29022, 2026-05-19) | `eval_gsm8k_grpo_shortgpt_20` (westd-29022, 2026-05-19) | 42 |\n\n### Multi-seed GRPO breakdown (Table 2 & Appendix Tab multiseed)\n\n| Method | Seed 42 | exp_id | Seed 123 | exp_id | Seed 456 | exp_id | Mean |\n|--------|---------|--------|----------|--------|----------|--------|------|\n| CKA-only 20% | 64.37% | `eval_gsm8k_grpo_cka_only_20_v2` (westb-23072, 05-18) | 64.22% | `eval_gsm8k_grpo_cka_only_20_seed123` (westb-23072, 05-19) | 64.59% | `eval_gsm8k_grpo_cka_only_20_seed456_full` (westd-29022, 05-20) | 64.39% |\n| Standard 20% | 59.44% | `eval_gsm8k_grpo_standard_20_fair_v2` (westd-29022, 05-19) | 59.89% | `eval_gsm8k_grpo_standard_20_seed123_full` (westd-29022, 05-20) | 60.20% | `eval_gsm8k_grpo_standard_20_seed456_full` (westd-29022, 05-20) | 59.84% |\n| Random 20% | 50.57% | `eval_gsm8k_grpo_random_20_v2` (westd-29022, 05-21) | 50.72% | `eval_gsm8k_grpo_random_20_seed123_v2` (westd-32935, 05-22) ⚠️ NO_METRICS in registry | 50.87% | `eval_gsm8k_grpo_random_20_seed456` (westb-23072, 05-22) | 50.72% |\n\n**Notes:**\n- ⚠️ `eval_gsm8k_grpo_random_20_seed123_v2`: status=DONE, conclusion=success, but metrics field empty in registry. Paper value 50.72% sourced from result JSON on disk.\n- ⚠️ CKA-only seed456: registry=64.59% (852/1319=64.594%), paper=64.58%. Rounding difference (0.01pp).\n- Standard SFT: registry has two entries — `eval_gsm8k_sft_standard_20`=59.21% (seed42 SFT checkpoint) and `eval_sft_standard_full_westd`=59.29% (seeds 123/456 SFT checkpoint). Paper uses 59.29%. Appendix explains: \"Standard seed 42 was trained from a separately initialized SFT checkpoint (accuracy 59.21% vs. 59.29%).\"\n- All GRPO evals: OLD script era (all before 2026-05-23)\n\n---\n\n## Table 3: α Dose-Response (`table3_alpha.tex`)\n\nGSM8K (N=1,319) at 20% sparsity, varying α. Single seed (42).\n\n| α | SFT Acc.(%) | exp_id (SFT) | GRPO Acc.(%) | exp_id (GRPO) | Δ(pp) |\n|---|-------------|--------------|--------------|---------------|-------|\n| 0.5 | 60.73 | `eval_gsm8k_sft_alpha0p5_20` (westd-32935, 05-22) | 61.18 | `eval_gsm8k_grpo_alpha0p5_20` (westd-32935, 05-22) | +0.45 |\n| 1.0 | 61.49 | `eval_gsm8k_sft_rasp_20` (westd-29022, 05-20) | 60.88 | `eval_gsm8k_grpo_rasp_20_fair` (westd-29022, 05-19) | −0.61 |\n| 2.0 | 64.97 | `eval_gsm8k_sft_alpha2p0_20` (westd-32935, 05-22) | 66.11 | `eval_gsm8k_grpo_alpha2p0_20` (westd-32935, 05-22) | +1.14 |\n| 3.0 | 64.14 | `eval_gsm8k_sft_alpha3p0_20` (westd-32935, 05-22) | 63.46 | `eval_gsm8k_grpo_alpha3p0_20` (westd-32935, 05-22) | −0.68 |\n| 4.0 | 61.94 | `eval_gsm8k_sft_alpha4_20_v5` (westd-32935, 05-22) | 62.77 | `eval_gsm8k_grpo_alpha4_20_v3` (westd-32935, 05-22) | +0.83 |\n\n**Notes:**\n- ⚠️ α=3.0 GRPO: registry=63.45% (837/1319=63.456%), paper=63.46%. Rounding (paper rounds up).\n- All: OLD script era (all 05-22)\n- α=4.0 SFT has v5 suffix (multiple reruns due to server issues); GRPO has v3 suffix\n\n---\n\n## Table 4: Sparsity Cliff at 30% (`table4_sparsity_cliff.tex`)\n\nGSM8K at 30% sparsity, N=100 (quick eval) or N=200/500 (registry).\n\n| Method | Acc.(%) | EOS Rate(%) | Registry exp_id | Notes |\n|--------|---------|-------------|-----------------|-------|\n| Standard | 4 | 5.5 | `eval_postprune_standard_30` (acc=0.04, N=200, 05-17) | Also `prune_eval_standard_30` (acc=2.8%, N=500, 05-20) |\n| RASP (α=1.0) | 0 | 3.0 | `eval_postprune_rasp_30` (acc=0, N=200, 05-17) | Exact match |\n| CKA-only | 0 | -- | `prune_eval_cka_only_30` (acc=1.6%, N=500 partial, 05-20) | ⚠️ Registry=1.6%, paper=0%. Different N and partial eval |\n\n**Notes:**\n- Paper uses N=100 quick eval. Registry has N=200 and N=500 versions.\n- ⚠️ Standard: paper=4% matches N=200 registry (8/200=4%). The N=500 version gives 2.8%.\n- ⚠️ CKA-only: paper=0% vs registry 1.6% (N=500). Possibly different evaluation run; paper footnote says \"Terminated early after collapse confirmed.\"\n\n---\n\n## Table 5: Inference Efficiency (`table5_inference.tex`, main paper)\n\nLatency averaged over 100 GSM8K problems at 20% sparsity.\n\n| Config | Latency(s) | Speedup(%) | Memory(GB) | Mem.Red.(%) | Registry exp_id |\n|--------|-----------|------------|-----------|------------|-----------------|\n| Dense | 6.682 | -- | 16.22 | -- | `inference_speedup_plan016_v2` (dense.avg_latency=6.682, peak_memory=16.22GB, 05-16) |\n| RASP (α=1.0) 20% | 4.156 | 37.8 | 11.60 | 28.5 | `inference_speedup_plan016_v2` (rasp.avg_latency=4.156, rasp.peak_memory=11.60GB) |\n| Standard 20% | 6.167 | 7.7 | 11.61 | 28.4 | `inference_speedup_plan016_v2` (standard.avg_latency=6.167, standard.peak_memory=11.61GB) |\n\n---\n\n## Table (Appendix): Inference TPS/TTFT (`appendix.tex` Tab inference)\n\n| Config | TPS(tok/s) | TTFT(ms) | Per-token(ms) | Params(B) | Registry exp_id |\n|--------|-----------|---------|-------------|----------|-----------------|\n| Dense 7B | 72.0 | 20.1 | 13.9 | 7.62 | `inference_bench_clean_v2` (original_tps=72.02, 05-19) |\n| CKA-only 20% | 58.3 | 16.4 | 16.7 | 6.16 | `inference_bench_clean_v2` (cka_only_tps=58.3) |\n| Standard 20% | 58.2 | 16.4 | 16.7 | 6.16 | `inference_bench_clean_v2` (standard_tps=58.2) |\n\n**Notes:**\n- Two separate benchmark experiments: `inference_speedup_plan016_v2` (latency/memory, westd-11672, 05-16) and `inference_bench_clean_v2` (TPS/TTFT, westb-23072, 05-19).\n\n---\n\n## Table: MATH-500 (`tab_math500.tex`)\n\nMATH-500 (N=500), greedy decoding, max_new_tokens=2048.\n\n| Row | SFT(%) | exp_id (SFT) | GRPO(%) | exp_id (GRPO) | Δ(pp) | Script |\n|-----|--------|--------------|---------|---------------|-------|--------|\n| **Dense** | 53.0 | `eval_math500_dense_2048` (05-18) | -- | -- | -- | OLD |\n| **20% method comparison** | | | | | | |\n| CKA-only | 26.8 | `eval_math500_sft_cka_only_20_westd` (westd-32935, 05-22) | 27.4 | `eval_math500_grpo_cka_only_20_2048_v2` (westd-32935, 05-23) | +0.6 | SFT:OLD, GRPO:**NEW** |\n| Standard | 25.8‡ | `eval_math500_sft_standard_20_2048_v2` (westd-32935, 05-19) | 26.4‡ | `eval_math500_grpo_standard_20_fair_2048_v2` (westd-32935, 05-22) | +0.6 | OLD (‡earlier extraction) |\n| RASP (α=1.0) | 21.2 | `eval_math500_sft_rasp_alpha1p0_20_v2` (05-22) | 22.6 | `eval_math500_grpo_rasp_alpha1p0_20` (05-22) | +1.4 | OLD |\n| Random | 14.4 | `eval_math500_sft_random_20_v3` (westd-32935, 05-22) | --- | -- | --- | OLD |\n| **20% α dose-response** | | | | | | |\n| α=0.5 | 25.4 | `eval_math500_sft_rasp_alpha0p5_20` (05-22) | 24.8 | `eval_math500_grpo_rasp_alpha0p5_20` (westb-23072, 05-23) | −0.6 | SFT:OLD, GRPO:**NEW** |\n| α=2.0 | 24.0 | `eval_math500_sft_rasp_alpha2p0_20` (westd-32935, 05-22) | 26.2 | `eval_math500_grpo_rasp_alpha2p0_20` (westd-32935, 05-22) | +2.2 | OLD |\n| α=3.0 | 23.2 | `eval_math500_sft_rasp_alpha3p0_20` (05-22) | 22.8 | `eval_math500_grpo_rasp_alpha3p0_20` (westd-32935, 05-23) | −0.4 | SFT:OLD, GRPO:**NEW** |\n| α=4.0 | 26.6 | `eval_math500_sft_rasp_alpha4p0_20` (05-22) | 26.2 | `eval_math500_grpo_rasp_alpha4p0_20` (05-23) | −0.4 | SFT:OLD, GRPO:**NEW** |\n| **25% sparsity** | | | | | | |\n| CKA-only | 19.2 | `eval_math500_sft_cka_only_25_v2` (westd-29022, 05-21) | 18.4 | `eval_math500_grpo_cka_only_25_v2` (westd-29022, 05-21) | −0.8 | OLD |\n| Standard | 14.0 | `eval_math500_sft_standard_25` (westb-23072, 05-21) | 12.8 | ⚠️ 无 registry 记录 | −1.2 | -- |\n\n**Notes:**\n- ⚠️ MATH-500 Standard 25% GRPO=12.8%: 无对应 registry 条目 (`eval_math500_grpo_standard_25` 不存在)\n- `eval_math500_grpo_cka_only_20` (OLD, 05-18) gave 26.6% — superseded by `eval_math500_grpo_cka_only_20_2048_v2` (NEW, 05-23) = 27.4% after answer extraction update\n- Dense 53.0% uses 2048 token limit (`eval_math500_dense_2048`). Unlimited version: 73.6% (`eval_math500_unpruned`)\n\n---\n\n## Table: MBPP (`tab_mbpp.tex`)\n\nMBPP code generation (N=374), greedy decoding.\n\n| Row | SFT(%) | exp_id (SFT) | GRPO(%) | exp_id (GRPO) | Δ(pp) | Script |\n|-----|--------|--------------|---------|---------------|-------|--------|\n| Dense | -- | -- | 53.48 | `eval_mbpp_dense_unpruned` (pass@1=0.5348, 200/374, 05-19) | -- | OLD |\n| CKA-only 20% | 12.83 | `eval_mbpp_sft_cka_only_20` (48/374, 05-19) | 14.17 | `eval_mbpp_grpo_cka_only_20` (53/374, 05-19) | +1.34 | OLD |\n| Standard 20% | 12.03 | `eval_mbpp_sft_standard_20_v4` (45/374, 05-19) | 13.10 | `eval_mbpp_grpo_standard_20_v4` (49/374, 05-19) | +1.07 | OLD |\n| RASP (α=1.0) 20% | 11.76 | `eval_mbpp_sft_rasp_20` (44/374, 05-19) | 13.10 | `eval_mbpp_grpo_rasp_20` (49/374, 05-19) | +1.34 | OLD |\n| ShortGPT 20% | 10.43 | `eval_mbpp_sft_shortgpt_20_v2` (39/374, 05-19) | 14.44 | `eval_mbpp_grpo_shortgpt_20_v2` (54/374, 05-19) | +4.01 | OLD |\n\n---\n\n## Table: Cross-Scale Validation (`tab5_cross_scale.tex`)\n\n7B values cross-referenced from Tables 1–2. 1.5B: DeepSeek-R1-Distill-Qwen-1.5B, single seed.\n\n| Method | Scale | Rew. | GSM8K(%) | Registry exp_id (GRPO eval) | Registry exp_id (training) |\n|--------|-------|------|----------|---------------------------|--------------------------|\n| CKA-only | 7B | 0.354 | 64.39 | (see Table 2 multi-seed) | `grpo_cka_only_20` |\n| Standard | 7B | 0.081 | 59.84 | (see Table 2 multi-seed) | `grpo_standard_20_fair` |\n| RASP | 7B | 0.061 | 60.88 | (see Table 2) | `grpo_rasp_20_fair` |\n| Random | 7B | 0.190 | -- | -- | `grpo_random_20` |\n| CKA-only | 1.5B | 0.238 | 35.48 | `eval_gsm8k_grpo_cka_only_20_1p5b` (0.3548, 468/1319, 05-18) | `grpo_cka_only_20_1p5b` (reward_mean=0.2375) |\n| Standard | 1.5B | 0.084 | 22.29 | `eval_gsm8k_grpo_standard_20_1p5b` (0.2229, 294/1319, 05-18) | `grpo_standard_20_1p5b` (reward_mean=0.0844) |\n| RASP | 1.5B | 0.099 | 26.16 | `eval_gsm8k_grpo_rasp_20_1p5b` (0.2616, 345/1319, 05-18) | `grpo_rasp_20_1p5b` (final_reward=0.099) |\n\n**Notes:** All 1.5B experiments: OLD script, single seed (42), server westb-23072 (05-18).\n\n---\n\n## Table: CKA Stability (`tab_cka_stability.tex`)\n\n| Metric | Paper Value | Registry exp_id | Registry Value |\n|--------|-------------|-----------------|----------------|\n| Spearman ρ (min) | 0.964 | `cka_scoring_stability_ablation` (05-19) | min_combined_rho=0.964 ✓ |\n| Spearman ρ (mean) | 0.979 | `cka_scoring_stability_ablation` (05-19) | mean_combined_rho=0.979 ✓ |\n\nAlso: `cka_calibration_stability_ablation` (split_half_rho=0.9932, 05-19)\n\n---\n\n## Table (Appendix): Cross-Sparsity Validation\n\n| Sparsity | Method | SFT(%) | exp_id (SFT) | GRPO(%) | exp_id (GRPO) | Δ(pp) |\n|----------|--------|--------|--------------|---------|---------------|-------|\n| 15% | CKA-only | 72.18 | `eval_gsm8k_sft_cka_only_15` (952/1319, 05-20) | 72.76±0.57 | 3-seed mean (see below) | +0.58 |\n| 15% | Standard | 66.49 | `eval_gsm8k_sft_standard_15` (877/1319, 05-20) | 65.56±0.50 | 3-seed mean (see below) | −0.93 |\n| 20% | CKA-only | 63.91 | (see Table 2) | 64.39 | (see Table 2) | +0.48 |\n| 20% | Standard | 59.29 | (see Table 2) | 59.84 | (see Table 2) | +0.55 |\n| 25% | CKA-only | 60.12 | `eval_gsm8k_sft_cka_only_25` (westd-29022, 05-21) | 59.59 | `eval_gsm8k_grpo_cka_only_25_v3` (westd-29022, 05-21) | −0.53 |\n| 25% | Standard | 50.87 | `eval_gsm8k_sft_standard_25` (westd-29022, 05-21) | 51.86 | `eval_gsm8k_grpo_standard_25` (westb-23072, 05-21) | +0.99 |\n| 30% | All | Collapse | (see Table 4) | -- | -- | -- |\n\n### 15% multi-seed breakdown\n\n| Method | Seed 42 | exp_id | Seed 123 | exp_id | Seed 456 | exp_id | Mean |\n|--------|---------|--------|----------|--------|----------|--------|------|\n| CKA-only 15% | 73.09% | `eval_gsm8k_grpo_cka_only_15_v2` (05-20) | 73.09% | `eval_gsm8k_grpo_cka_only_15_seed123` (05-20) | 72.10% | `eval_gsm8k_grpo_cka_only_15_seed456` (05-20) | 72.76% |\n| Standard 15% | 66.11% | `eval_gsm8k_grpo_standard_15_v2` (05-20) | 65.13% | `eval_gsm8k_grpo_standard_15_seed123_v3` (05-20) | 65.43% | `eval_gsm8k_grpo_standard_15_seed456_v3` (05-20) | 65.56% |\n\n---\n\n## Table (Appendix): Cross-Architecture Qwen2.5-Math-7B\n\nGSM8K (N=200) at 20% sparsity.\n\n| Method | Post-Prune(%) | Registry | Post-SFT(%) | Registry | EOS Rate(%) |\n|--------|--------------|----------|-------------|----------|-------------|\n| CKA-only | 1.0 | ⚠️ 无 registry 记录 | 51.50±3.53 | ⚠️ 无 registry 记录 (N=200 SFT eval not registered) | 27.0 |\n| Standard | 18.5 | ⚠️ 无 registry 记录 | 21.00±2.88 | `eval_gsm8k_sft_qwen_standard_20` (0.21, 42/200, 05-20) | 36.5 |\n\n**Notes:**\n- ⚠️ CKA-only Post-Prune=1.0% and Post-SFT=51.50%: no registry entries found. Results likely from server-side JSON files.\n- ⚠️ Standard Post-Prune=18.5%: no registry entry. Only the Post-SFT value is registered.\n- Qwen GRPO eval: `eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3` = 48.60% (N=500, 83.8% truncated, footnote only)\n- Qwen MATH-500: `eval_math500_sft_qwen_math_cka_only_20` = 21.6% (registered but not in paper)\n\n---\n\n## Table (Appendix): Gradient Flow Analysis\n\n| Comparison | Gradient Ratio | Sig. Layers | Registry exp_id |\n|------------|---------------|-------------|-----------------|\n| CKA-only vs Standard | 2.89× | 55/56 | `gradient_flow_v3` (cka_vs_standard_ratio=2.89, 05-19) |\n| CKA-only vs RASP | 2.26× | 56/56 | `gradient_flow_v3` (computed: cka_mean/rasp_mean=0.3229/0.1431=2.26×) |\n| RASP vs Standard | 1.28× | 45/56 | `gradient_flow_v3` (rasp_vs_standard_ratio=1.28, 05-19) |\n\n---\n\n## Inline Values (experiments.tex)\n\n| Location | Paper Value | Registry exp_id | Match? |\n|----------|-------------|-----------------|--------|\n| §4.1 \"original unpruned model achieves 90.83%\" | 90.83% | `eval_gsm8k_dense_unpruned` (0.9083, 1198/1319, 05-20) | ✓ |\n| §4.1 \"200 of 784 across 28 layers, ~1.45B parameters\" | structural | N/A (architecture constant) | -- |\n| §4.1 \"4.55pp gap... p=0.0009, Cohen's d=11.1, 95% CI [3.62, 5.47]\" | computed | From Table 2 multi-seed data | ✓ (derived) |\n| §4.2 \"CKA-only reaches 0.354 peak reward with recovery event at step 90\" | 0.354 | `grpo_cka_only_20` (peak=0.3544) | ✓ |\n| §4.2 \"Random oscillates between 0.142 and 0.190\" | 0.142–0.190 | `grpo_random_20` training logs | ✓ |\n| §4.2 \"Standard peaks at 0.081 (step 40)\" | 0.081 | `grpo_standard_20_fair` (peak=0.081) | ✓ |\n| §4.2 \"RASP peaks at 0.061 (step 50) then declines to 0.010\" | 0.061→0.010 | `grpo_rasp_20_fair` (peak=0.061, final=0.01) | ✓ |\n| §4.2 \"5.8× peak reward gap\" | 5.8× | 0.354/0.061=5.80× | ✓ (derived) |\n| §4.3 \"mean |Δ|=0.54pp\" | 0.54 | mean(0.48, 0.55, 0.53, 0.61)=0.5425≈0.54 | ✓ (derived) |\n| §4.3 \"15%: SFT gap 5.69pp (72.18% vs 66.49%)\" | 5.69pp | 72.18−66.49=5.69 | ✓ (derived) |\n| §4.3 \"GRPO gap 7.20pp (72.76% vs 65.56%)\" | 7.20pp | 72.76−65.56=7.20 | ✓ (derived) |\n| §4.3 \"extending training to 300 steps: CKA 64.37%→64.37%, Standard 59.44%→59.29%\" | | See extended training section | |\n| §4.4 \"CKA-only achieves active learning (peak reward 4.4× Standard)\" | 4.4× | 0.354/0.081=4.37≈4.4× | ✓ (derived) |\n| §4.4 \"unstructured pruning: SFT 87.87%, GRPO 87.64%, Δ=−0.23pp\" | 87.87%, 87.64% | `eval_unstructured_20` (0.8787, 05-17), `eval_gsm8k_grpo_unstructured_20` (0.8764, 05-19) | ✓ |\n| §4.5 \"CKA-only diverges most (μ=0.62), Standard (μ=0.90), Random (μ=0.92), RASP (μ=0.88)\" | CKA values | From CKA heatmap analysis (not a separate registry entry) | -- |\n| §4.5 \"2.89× mean gradient magnitude vs Standard across 55/56 layer groups\" | 2.89× | `gradient_flow_v3` | ✓ |\n| §4.5 \"Extended GRPO: CKA 5.5× gap (0.308 vs 0.056 at step 300)\" | 0.308, 0.056 | `grpo_cka_only_20_extended_300`, `grpo_standard_20_extended_300_v2` | ✓ |\n| §4.5 \"1.5B: CKA 35.48% ≫ RASP 26.16% > Standard 22.29%\" | | (see Cross-Scale table) | ✓ |\n| §4.5 \"Qwen2.5-Math-7B: CKA 1.0%→51.50%, Standard 18.5%→21.00%\" | | (see Cross-Arch table) | Partial (⚠️ some values not in registry) |\n\n---\n\n## Extended Training 300 Steps (experiments.tex §4.5, appendix)\n\n| Claim | Registry exp_id | Registry Value | Notes |\n|-------|-----------------|----------------|-------|\n| CKA reward at step 300 = 0.308 | `grpo_cka_only_20_extended_300` (05-18) | reward_step300=0.3075 | ⚠️ Registry=0.3075, paper=0.308 (rounding) |\n| Standard reward at step 300 = 0.056 | `grpo_standard_20_extended_300_v2` (05-18) | reward_mean_step300=0.0562 | ⚠️ Registry=0.0562, paper=0.056 (rounding) |\n| CKA GSM8K stays at 64.37% | No 300-step eval registered | -- | ⚠️ Paper reuses step-100 eval (`eval_gsm8k_grpo_cka_only_20_v2`=64.37%) |\n| Standard 59.44%→59.29% | No 300-step eval registered | -- | ⚠️ No separate 300-step GSM8K eval. 59.44%=step-100 GRPO seed42, 59.29%=SFT baseline |\n\n---\n\n## Inline Values (abstract.tex)\n\n| Paper Value | Source |\n|-------------|--------|\n| \"|Δ(GRPO−SFT)| ≤ 0.61pp across all four fine-grained criteria\" | max(0.48, 0.55, 0.53, 0.61)=0.61 ✓ |\n| \"max 1.34pp including dose-response and MBPP\" | MBPP CKA Δ=+1.34pp or MBPP RASP Δ=+1.34pp ✓ |\n| \"peak reward 4.4× vs importance-only\" | 0.354/0.081=4.37≈4.4× ✓ |\n| \"α=2.0 (66.11%)\" | Table 3 ✓ |\n\n## Inline Values (introduction.tex)\n\n| Paper Value | Source |\n|-------------|--------|\n| \"mean |Δ|=0.54pp at 20%\" | mean(0.48, 0.55, 0.53, 0.61)=0.5425≈0.54 ✓ |\n| \"max 0.61pp; 1.34pp including dose-response and MBPP\" | Table 2 max=0.61; MBPP max=1.34 ✓ |\n| \"ShortGPT |Δ|>1pp (−1.36pp on GSM8K)\" | Table 2 ✓ |\n| \"α=2.0 (66.11%)\" | Table 3 ✓ |\n| \"CKA-only peak reward 4.4× Standard\" | 0.354/0.081=4.37≈4.4× ✓ |\n\n---\n\n## Figures\n\n### Figure 1: Dose-Response Curve (`fig1_dose_response.pdf`)\n- Data source: Table 3 (α ablation) — same experiments\n- Both SFT and GRPO curves plotted from the 5 α values\n\n### Figure 2: Reward Trajectories (`fig2_reward_trajectories.pdf`)\n- Data source: GRPO training logs from:\n  - `grpo_cka_only_20` (CKA-only, peak=0.354)\n  - `grpo_random_20` (Random, peak=0.190)\n  - `grpo_standard_20_fair` (Standard, peak=0.081)\n  - `grpo_rasp_20_fair` (RASP, peak=0.061)\n  - Unpruned: `grpo_unpruned_v2` or similar\n- Result paths: `/root/autodl-tmp/recovery_aware_struct_prune/{exp_name}/` training logs (tensorboard/wandb)\n\n### Figure 3: Collapse Dynamics (`fig3_collapse_dynamics.pdf`)\n- (a) f₀ dynamics: from same GRPO training logs as Figure 2\n- (b) Gradient norm: from same GRPO training logs\n- Specific values cited: \"Standard transient minimum 0.017 at step 90, recovers to 2.41 at step 100\"\n- \"RASP gradient norms remain predominantly near zero\"\n\n### Figure 4: CKA Heatmap (`fig4_cka_heatmap.pdf`)\n- Data source: CKA analysis during pruning\n- μ values: CKA-only=0.62, Standard=0.90, Random=0.92, RASP=0.88\n- ⚠️ No dedicated registry entry for CKA heatmap data; computed during pruning step\n\n### Figure 5: Extended Training (`fig5_extended_training.pdf`)\n- Data source: `grpo_cka_only_20_extended_300` and `grpo_standard_20_extended_300_v2`\n- (a) Reward: CKA oscillates 0.22–0.44; Standard 0.054→0.056\n- (b) f₀: Standard > 0.5 throughout; CKA < 0.30\n\n### Figure (Appendix): KL Divergence (`fig_appendix_kl.pdf`)\n- Data source: GRPO training logs (KL between policy and reference model)\n- RASP < 0.001, Random ~0.004–0.005\n\n---\n\n## Summary of Issues\n\n### ⚠️ Values with No Registry Record (4)\n\n| Paper Location | Value | Notes |\n|----------------|-------|-------|\n| MATH-500 tab, Standard 25% GRPO | 12.8% | No `eval_math500_grpo_standard_25` in registry |\n| Cross-Arch tab, CKA Post-Prune | 1.0% | No post-prune eval registered for Qwen CKA |\n| Cross-Arch tab, CKA Post-SFT | 51.50%±3.53 | N=200 SFT eval not registered |\n| Cross-Arch tab, Standard Post-Prune | 18.5% | No post-prune eval registered for Qwen Standard |\n\n### ⚠️ Minor Numerical Discrepancies (4)\n\n| Paper Value | Registry Value | Diff | Cause |\n|-------------|---------------|------|-------|\n| CKA seed456 = 64.58% | 64.59% (852/1319) | 0.01pp | Rounding |\n| α=3.0 GRPO = 63.46% | 63.45% (837/1319) | 0.01pp | Rounding direction |\n| Extended CKA reward = 0.308 | 0.3075 | 0.0005 | Rounding |\n| Extended Standard reward = 0.056 | 0.0562 | 0.0002 | Rounding |\n\n### ⚠️ Registry Records with Empty Metrics (3)\n\n| exp_id | Status | Notes |\n|--------|--------|-------|\n| `eval_gsm8k_grpo_random_20_seed123_v2` | DONE/success | Paper uses 50.72% from result JSON on disk |\n| `eval_gsm8k_sft_depth_first_20` | DONE/success | Disk-full error prevented metric recording |\n| `eval_gsm8k_grpo_depth_first_20` | DONE/success | Disk-full error prevented metric recording |\n\n### ⚠️ 30% Cliff Inconsistency\n\n| Method | Paper | Registry | N |\n|--------|-------|----------|---|\n| CKA-only | 0% | 1.6% | Paper: N=100, registry: N=500 partial |\n| Standard | 4% | 4% (N=200) / 2.8% (N=500) | Paper: N=100 |\n\n---\n\n## Server Summary\n\n| Server | Role | GPU |\n|--------|------|-----|\n| westb-23072 | Primary early experiments, some later seeds | 2× RTX PRO 6000 |\n| westd-11672 | Early evals (unpruned, Standard SFT) | 2× RTX PRO 6000 |\n| westd-29022 | Mid-phase (20%/25% evals, 1.5B) — replaced by westd-32935 | -- |\n| westd-32935 | Late-phase (α dose-response, MATH-500 reruns) | 4× GPU |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "6515c16e-71ed-4b43-b0fa-66232255205f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 86_

```json
{
  "type": "last-prompt",
  "leafUuid": "6c7f0f52-b672-4321-8d39-7f226aea7dbb",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Runtime record

_source line 87_

```json
{
  "type": "ai-title",
  "aiTitle": "Map paper results to registry experiments",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Tool call

_source line 88 · 2026-05-23T11:02:57.172Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01T1xQK64k8LN1TohC6D1AeC`</summary>

```json
{
  "todos": [
    {
      "content": "Extract all numerical values from tex files",
      "status": "completed",
      "activeForm": "Extracting numerical values from tex files"
    },
    {
      "content": "Read registry data and match experiments",
      "status": "completed",
      "activeForm": "Reading registry data and matching experiments"
    },
    {
      "content": "Write complete provenance audit document",
      "status": "completed",
      "activeForm": "Writing complete provenance audit document"
    },
    {
      "content": "Register artifact",
      "status": "in_progress",
      "activeForm": "Registering artifact"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c7f0f52-b672-4321-8d39-7f226aea7dbb",
  "isSidechain": false,
  "requestId": "req_011CbKPU1FWNhHR5RWf74Z2i",
  "type": "assistant",
  "uuid": "99d40c4e-d5b1-4bd2-9ee3-720b6b6270fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AbzmQ5tMBbTbgDWkx5vMFy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11538,
      "cache_read_input_tokens": 73487,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11538,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 73487,
          "cache_creation_input_tokens": 11538,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11538
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

_source line 89 · 2026-05-23T11:02:57.175Z_

<details><summary>↩ Tool result · `toolu_01T1xQK64k8LN1TohC6D1AeC`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99d40c4e-d5b1-4bd2-9ee3-720b6b6270fc",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "e4881acd-f2de-4690-8e74-4d2f484cc63f",
  "toolUseResult": {
    "oldTodos": [
      {
        "content": "Extract all numerical values from tex files",
        "status": "completed",
        "activeForm": "Extracting numerical values from tex files"
      },
      {
        "content": "Read registry data and match experiments",
        "status": "completed",
        "activeForm": "Reading registry data and matching experiments"
      },
      {
        "content": "Write complete provenance audit document",
        "status": "in_progress",
        "activeForm": "Writing complete provenance audit document"
      },
      {
        "content": "Register artifact",
        "status": "pending",
        "activeForm": "Registering artifact"
      }
    ],
    "newTodos": [
      {
        "content": "Extract all numerical values from tex files",
        "status": "completed",
        "activeForm": "Extracting numerical values from tex files"
      },
      {
        "content": "Read registry data and match experiments",
        "status": "completed",
        "activeForm": "Reading registry data and matching experiments"
      },
      {
        "content": "Write complete provenance audit document",
        "status": "completed",
        "activeForm": "Writing complete provenance audit document"
      },
      {
        "content": "Register artifact",
        "status": "in_progress",
        "activeForm": "Registering artifact"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "99d40c4e-d5b1-4bd2-9ee3-720b6b6270fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-23T11:03:02.511Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_017pxynjBzpaRZxWPJBXZPfc`</summary>

```json
{
  "name": "data_provenance_audit",
  "type": "report",
  "description": "论文数据溯源表：每个实验数值 → registry exp_id → 服务器结果路径，含 eval 脚本版本、seed 信息、数值一致性校验",
  "project": "recovery_aware_struct_prune",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/data_provenance_audit.md",
  "tags": [
    "provenance",
    "audit",
    "paper"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4881acd-f2de-4690-8e74-4d2f484cc63f",
  "isSidechain": false,
  "requestId": "req_011CbKPUL7pW6ZAbC1xySmAK",
  "type": "assistant",
  "uuid": "30a02f67-2e51-4fb0-aed8-575792ce953c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtvfbopAsxDKuRm1xZARt1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 213,
      "cache_read_input_tokens": 85025,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 213,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 262,
          "cache_read_input_tokens": 85025,
          "cache_creation_input_tokens": 213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 213
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

_source line 91 · 2026-05-23T11:03:02.819Z_

<details><summary>↩ Tool result · `toolu_017pxynjBzpaRZxWPJBXZPfc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260523_1168bf\", \"name\": \"data_provenance_audit\", \"type\": \"report\", \"description\": \"论文数据溯源表：每个实验数值 → registry exp_id → 服务器结果路径，含 eval 脚本版本、seed 信息、数值一致性校验\", \"path\": \"projects/recovery_aware_struct_prune/artifacts/_project/report/data_provenance_audit.md\", \"url\": null, \"project\": \"recovery_aware_struct_prune\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-23T11:03:02.519614+00:00\", \"tags\": [\"provenance\", \"audit\", \"paper\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30a02f67-2e51-4fb0-aed8-575792ce953c",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "f76e5b02-d26e-4c6f-8a46-deee4c917b99",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260523_1168bf\\\", \\\"name\\\": \\\"data_provenance_audit\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"论文数据溯源表：每个实验数值 → registry exp_id → 服务器结果路径，含 eval 脚本版本、seed 信息、数值一致性校验\\\", \\\"path\\\": \\\"projects/recovery_aware_struct_prune/artifacts/_project/report/data_provenance_audit.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"recovery_aware_struct_prune\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-23T11:03:02.519614+00:00\\\", \\\"tags\\\": [\\\"provenance\\\", \\\"audit\\\", \\\"paper\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260523_1168bf\", \"name\": \"data_provenance_audit\", \"type\": \"report\", \"description\": \"论文数据溯源表：每个实验数值 → registry exp_id → 服务器结果路径，含 eval 脚本版本、seed 信息、数值一致性校验\", \"path\": \"projects/recovery_aware_struct_prune/artifacts/_project/report/data_provenance_audit.md\", \"url\": null, \"project\": \"recovery_aware_struct_prune\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-23T11:03:02.519614+00:00\", \"tags\": [\"provenance\", \"audit\", \"paper\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "30a02f67-2e51-4fb0-aed8-575792ce953c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-23T11:03:05.387Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01Ted34FcLgFyMCPSDw8YxDk`</summary>

```json
{
  "todos": [
    {
      "content": "Extract all numerical values from tex files",
      "status": "completed",
      "activeForm": "Extracting numerical values from tex files"
    },
    {
      "content": "Read registry data and match experiments",
      "status": "completed",
      "activeForm": "Reading registry data and matching experiments"
    },
    {
      "content": "Write complete provenance audit document",
      "status": "completed",
      "activeForm": "Writing complete provenance audit document"
    },
    {
      "content": "Register artifact",
      "status": "completed",
      "activeForm": "Registering artifact"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f76e5b02-d26e-4c6f-8a46-deee4c917b99",
  "isSidechain": false,
  "requestId": "req_011CbKPUk3VFeBWzr5oYbcZq",
  "type": "assistant",
  "uuid": "bfd19188-1db9-49f4-bd9a-fae74db16a95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RvLodmEEYbeAh72cujs8qz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 561,
      "cache_read_input_tokens": 85238,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 85238,
          "cache_creation_input_tokens": 561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 561
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

_source line 93 · 2026-05-23T11:03:05.390Z_

<details><summary>↩ Tool result · `toolu_01Ted34FcLgFyMCPSDw8YxDk`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfd19188-1db9-49f4-bd9a-fae74db16a95",
  "isSidechain": false,
  "promptId": "dddf37fd-16cc-4cd5-bb05-648328938281",
  "type": "user",
  "uuid": "09328883-dc81-491f-bce4-81d64088056b",
  "toolUseResult": {
    "oldTodos": [
      {
        "content": "Extract all numerical values from tex files",
        "status": "completed",
        "activeForm": "Extracting numerical values from tex files"
      },
      {
        "content": "Read registry data and match experiments",
        "status": "completed",
        "activeForm": "Reading registry data and matching experiments"
      },
      {
        "content": "Write complete provenance audit document",
        "status": "completed",
        "activeForm": "Writing complete provenance audit document"
      },
      {
        "content": "Register artifact",
        "status": "in_progress",
        "activeForm": "Registering artifact"
      }
    ],
    "newTodos": [
      {
        "content": "Extract all numerical values from tex files",
        "status": "completed",
        "activeForm": "Extracting numerical values from tex files"
      },
      {
        "content": "Read registry data and match experiments",
        "status": "completed",
        "activeForm": "Reading registry data and matching experiments"
      },
      {
        "content": "Write complete provenance audit document",
        "status": "completed",
        "activeForm": "Writing complete provenance audit document"
      },
      {
        "content": "Register artifact",
        "status": "completed",
        "activeForm": "Registering artifact"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "bfd19188-1db9-49f4-bd9a-fae74db16a95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 94 · 2026-05-23T11:03:17.595Z_

溯源表已写入 `artifacts/data_provenance_audit.md` 并注册。

**覆盖范围**: 9 个表格文件 + experiments.tex/appendix.tex/abstract.tex/introduction.tex 中的内联数值 + 5 个 Figure 的数据来源。

**关键发现**:

1. **4 个论文数值无 registry 记录**:
   - MATH-500 Standard 25% GRPO = 12.8%
   - Qwen2.5-Math-7B CKA-only Post-Prune = 1.0% 和 Post-SFT = 51.50%
   - Qwen2.5-Math-7B Standard Post-Prune = 18.5%

2. **4 个微小数值差异** (均为四舍五入，≤0.01pp):
   - CKA seed456: 64.59% vs 64.58%
   - α=3.0 GRPO: 63.45% vs 63.46%
   - Extended training 两个 reward 值

3. **3 个 registry 记录 metrics 为空** (Random seed123、depth-first SFT/GRPO)

4. **30% cliff CKA-only**: paper=0% (N=100) vs registry=1.6% (N=500)，评估样本量不同

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09328883-dc81-491f-bce4-81d64088056b",
  "isSidechain": false,
  "requestId": "req_011CbKPUwDSrkHgNhbMmfU3E",
  "type": "assistant",
  "uuid": "07a47bc7-fda3-4b29-957d-1295a2fdda17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyYxZr7c6uVs8Fh16MVJyP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 211,
      "cache_read_input_tokens": 85799,
      "output_tokens": 365,
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
          "output_tokens": 365,
          "cache_read_input_tokens": 85799,
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


### Runtime record

_source line 95_

```json
{
  "type": "last-prompt",
  "leafUuid": "07a47bc7-fda3-4b29-957d-1295a2fdda17",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Runtime record

_source line 96_

```json
{
  "type": "ai-title",
  "aiTitle": "Map paper results to registry experiments",
  "sessionId": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---
