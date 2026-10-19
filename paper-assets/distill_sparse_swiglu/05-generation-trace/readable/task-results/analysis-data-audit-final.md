# analysis data audit final

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_data_audit_final_20260523T191559_result.json`
- **Structured JSON:** [`1f1827bf4ba018ac93e4.json`](../../sessions/1f/1f1827bf4ba018ac93e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

K=8 is only mentioned in the K-curve figure caption context ("~250 at K=8"), not with a specific PPL value in the main text. Appendix fix is sufficient.

## 数据自查报告

### ✅ 已核对一致

**Abstract & Introduction:**
- "14.5% PPL reduction" ← (10.30−8.81)/10.30=14.47% ✓ (teal_28.5pct_sanity PPL=10.30)
- "<1% of base" ← 75.9M/8.03B=0.95% ✓
- "MMLU −5.2pp on 8B" ← 40.7−45.86=−5.16pp ✓
- "GSM8K −20.1pp on 14B" ← 32.0−52.1=−20.1pp ✓
- "+67.2M params compensation" ✓
- "46–68% Jaccard divergence" ✓ (30%=46.26%, 50%=68.24%)
- "PPL gap ≤0.65pp" (C1 ablation) ✓
- "28.13±0.20" (BCE 50% 3-seed) ✓
- "8.81 vs 10.30, both at 28.5%" ✓
- "7.3× variance amplification" ← 9.5/1.3=7.31 ✓
- "−17.3% on Mistral" ← (8.38−6.93)/8.38=17.3% ✓
- "6.4% latency overhead" ← (126.78−119.11)/119.11=6.44% ✓

**Table 3 (Main Results):** 所有行全部核对通过
- Dense, TEAL 30%/50% uniform (含GSM8K), BCE global/uniform, MSE, KL global/uniform — 每个数字均与 registry 一致

**Table 4 (C1 Ablation):** 所有 12 行 × 5 列核对通过
- 30% s42/s123/s456 C1 vs KL ✓
- 50% s42 C1 (c1_ablation_eval_uniform) ✓
- 50% s42 KL (kl50_s42_uniform_eval: ARC 32.59, WG 62.35, MMLU 27.92, GSM8K 1.97) ✓

**Table 5 (Ablation):** 所有 PPL 值核对通过
- Forward KL, JSD, Reverse KL, STE, MSE, Per-layer KL (K=1, K=4), BCE variants ✓

**§4.5 Derived Claims:**
- "within 2.7%" ← (9.05−8.81)/8.81=2.72% ✓
- "2.05× worse" ← 18.52/9.05=2.05 ✓
- "PPL 67% closure" ← (9.05−8.89)/(9.05−8.81)=66.7% ✓
- "coupling range 2.08 PPL" ← 10.75−8.67=2.08 ✓
- "signal type gap 9.47 PPL" ← 18.52−9.05=9.47 ✓
- K=16 PPL 8.67±0.02 ✓

**Appendix Tables:**
- Latency: 全部 5 行 ✓
- OOD (C4): 全部 ✓
- OOD Downstream: 全部 12 个数字 ✓
- Constraint: 全部 ✓
- Cross-architecture (Mistral): PPL/Adv 全部 ✓
- Mistral downstream: TEAL 全部 ✓, KL PPL ✓
- Qwen-14B: KL global/uniform, TEAL global/uniform (PPL, ARC-c, WG, MMLU, GSM8K) ✓
- Allocation summary: 全部 ✓
- K-curve table (Appendix W): K=1,2,4,16,32 ✓
- db sensitivity, tau schedule, training convergence ✓

**Figure source data:**
- gen_k_curve_ppl.py: K=1,2,4,16,32 数据点 ✓

### ⚠️ 已修复

1. **K=8 PPL (K-curve table + figure)**: 8.99 → **9.00**
   - Registry 3-seed: s42=8.9704, s123=9.0648, s456=8.9515, mean=8.9956, 标准四舍五入为 9.00
   - 修复: `appendix.tex:639`, `gen_k_curve_ppl.py:28`

### ❌ 待人工确认

1. **Qwen-14B TEAL uniform HS/PIQA**: 两次独立 eval 结果不一致
   - v1 (`qwen14b_teal30_uniform_hspiqa`, updated 5/20): HS=67.72, PIQA=74.70 ← 论文使用此值
   - v2 (`qwen14b_teal30_uniform_hspiqa_v2`, completed 5/19): HS=67.56, PIQA=74.27
   - 影响: appendix.tex Table 6 TEAL uniform 行的 HS/PIQA 两个值
   - 建议: 确认哪次 eval 是权威版本

2. **Figure 2 (sparsity sweep) KL 50% PPL = 12.00**: 来源不明确
   - bench_kl50_global (s42) = 11.79
   - 3-seed mean KL50 global = 11.84
   - bench_kl50_uniform (s42) = 11.96 ← 最接近 12.00 但标注为 "global allocation"
   - 影响: Figure 2 的 50% 数据点位置和 "48% better" 标注
   - 建议: 确认数据来源，如为 uniform 值则改为 11.96 或改用 global 值 11.79/11.84

3. **Figure 2 caption vs annotation 不一致**: caption 引用 "14.5%, 50%, 82%" (uniform 比较), 但 figure 标注显示 "18%, 48%, 82%" (global 比较)。两套数字各自正确但来自不同 allocation baseline，可能引起审稿人困惑。

---
