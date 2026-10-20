# Dose-Response Map fp32 缺口分析报告

> 生成时间: 2026-05-19 ~06:00 UTC

## 1. Dose-Response Map 逐 α Provenance 状态

| α | Provenance | Seeds (registry) | PermG | d1 drift | Regime | 关键实验 ID |
|---|-----------|-------------------|-------|----------|--------|-------------|
| 0.00 | **fp16** (pre-D080) | s43, s44 (registry); s42 (pre-registry) | 0/24 (0%) | -13.8% | Null | alpha_sweep_a000_s43, alpha_sweep_a000_s44 |
| 0.05 | ✅ fp32 | s42 | 0/8 (0%) | -24.9% | 盲区 | alpha_sweep_a005_s42_v3 |
| 0.10 | ✅ fp32 (部分) | s43 fp32 done; s42 fp32 RUNNING | 0/8 | -22.1% | Canary 盲区 | alpha_sweep_a010_s43_fp32; alpha_sweep_a010_s42_fp32 (RUNNING) |
| 0.25 | **fp16** (pre-D080) | s43, s44 (registry); s42 (pre-registry) | ~0/24 | -40.3% | Sub-threshold | alpha_sweep_a025_s43, alpha_sweep_a025_s44 |
| 0.50 | **fp32 × 3 RUNNING** | s42/s43/s44 全部 RUNNING | TBD | TBD | Boundary | alpha_sweep_a050_s42/s43/s44_fp32 (05:31 提交, ~5h) |
| 0.60 | ✅ fp32 | s42 | 3/8 (38%) | -28.2% | Transitional | alpha_sweep_a060_s42_fp32_v3 |
| 0.75 | **fp16** (信号强, 低优先) | s43, s44 (registry); s42 (pre-registry) | ~20/24 (83%) | -32.7% | Transitional | alpha_sweep_a075_s43, alpha_sweep_a075_s44 |
| 1.00 | ✅ fp32 (多 seed) | multi-seed | ~24/32 (75%) | -28.3% | Confirmatory | mvp_v4_rep42, mvp_v4_rep43, mvp_v4_rep45 等 |

**fp32 覆盖率**: 8 点中 3 点 ✅ fp32 (0.05, 0.60, 1.00)，1 点部分 fp32 (0.10)，1 点 RUNNING (0.50)，3 点 fp16 (0.00, 0.25, 0.75)。

## 2. fp16 缺口详情

### α=0.25 (P0 — dose-response 主轴 gap)
- **现有 fp16 数据**: alpha_sweep_a025_s43 (d1=-40.5%, PermG=0/8), alpha_sweep_a025_s44 (metrics incomplete)
- **缺口**: 3 seeds 均为 fp16。D091+D092 要求主轴表纯 fp32。
- **影响**: sub-threshold regime 的 PermG 零检出是 step function 叙事关键锚点。

### α=0.00 (P0 — FPR ground truth)
- **现有 fp16 数据**: alpha_sweep_a000_s43 (PermG=0/8, d1=-13.9%), alpha_sweep_a000_s44 (PermG=0/8, d1=-14.6%)
- **缺口**: 3 seeds 均为 fp16。null control 是 FPR=0 的 ground truth。
- **影响**: Claim 3 (FPR control) 的基础数据。

### α=0.75 (P2 — 低优先)
- **现有 fp16 数据**: alpha_sweep_a075_s43 (d1=-32.3%), alpha_sweep_a075_s44 (d1=-31.8%)
- **信号强度**: PermG ~83%，drift ~32%，fp16→fp32 不太可能翻转结论。低优先。

## 3. α=0.25 fp32 重跑建议

3 seeds × ~4-5h = ~12-15 GPU-hours

```bash
# seed=42
python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 \
  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \
  --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s42_fp32

# seed=43
python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 43 \
  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \
  --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43_fp32

# seed=44
python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 44 \
  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \
  --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44_fp32
```

Registry ID: alpha_sweep_a025_s42_fp32, alpha_sweep_a025_s43_fp32, alpha_sweep_a025_s44_fp32

## 4. α=0.00 fp32 重跑建议

3 seeds × ~4-5h = ~12-15 GPU-hours

```bash
# seed=42
python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 \
  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \
  --synthetic_ratio 0.00 --output_dir results/alpha_sweep/a000_s42_fp32

# seed=43
python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 43 \
  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \
  --synthetic_ratio 0.00 --output_dir results/alpha_sweep/a000_s43_fp32

# seed=44
python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 44 \
  --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 \
  --synthetic_ratio 0.00 --output_dir results/alpha_sweep/a000_s44_fp32
```

Registry ID: alpha_sweep_a000_s42_fp32, alpha_sweep_a000_s43_fp32, alpha_sweep_a000_s44_fp32

最早启动时间: ~10:30 UTC（a050 fp32 × 3 完成释放 cuda:2/3/4 后），6 seeds 并行 ~5h 完成。

## 5. experiment_plan.yaml 过期 registry_id（6 条）

| # | Plan ID | 当前 registry_id | 状态 | 修复动作 |
|---|---------|-----------------|------|----------|
| 1 | plan_001 | alpha_sweep_a025_s42_v3 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 待 fp32 重跑后填入 alpha_sweep_a025_s42_fp32 |
| 2 | plan_001b | alpha_sweep_a000_s42 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 待 fp32 重跑后填入 alpha_sweep_a000_s42_fp32 |
| 3 | plan_001c | alpha_sweep_a050_s42 | NOT IN REGISTRY (pre-registry fp16) | → alpha_sweep_a050_s42_fp32 (RUNNING) |
| 4 | plan_001d | alpha_sweep_a075_s42 | NOT IN REGISTRY (pre-registry fp16) | 移除 → 低优先 fp32 重跑 |
| 5 | plan_010 | gen_wiki_gpt2m_a100_s42_v3 | NOT IN REGISTRY (superseded by v4) | ✅ → gen_wiki_gpt2m_a100_s42_v4 (DONE/success) |
| 6 | plan_030 | gen_opt13b_a100_s43_bf16 | DONE/killed | 移除 → 需重新安排 OPT-1.3B s43 |

## 6. GPU 调度建议

当前 8/8 满载。释放顺序预估：
1. **~07:00 UTC**: scale_69b (cuda:0) 完成 → 1 GPU 释放
2. **~10:30 UTC**: a050 fp32 × 3 (cuda:2/3/4) + a010_s42 (cuda:5) 完成 → 4 GPU 释放
3. **qwen35/gpt2m_s43/smollm3**: 时间不确定，预计 05-19 内完成

α=0.25 + α=0.00 共 6 seeds → 需 6 GPU 并行。最早 ~10:30 UTC 启动全部。~15:30 UTC 全部完成后 dose-response map 达到 7/8 fp32 覆盖（仅 α=0.75 仍 fp16）。