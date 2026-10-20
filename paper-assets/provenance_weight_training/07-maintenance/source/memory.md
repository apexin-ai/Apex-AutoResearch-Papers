# Memory

## N=5 B=4 统计显著性确认 (2026-05-24)

N=3→N=5 扩展解决了 Round 13 核心瓶颈（BH 校正后不显著）。

| Seed | Adaptive PPL | Uniform PPL | Δ |
|------|-------------|------------|-------|
| 42 | 17.680 (tau07_seed42) | 17.694 | -0.014 |
| 123 | 17.666 (tau07_seed123) | 17.686 | -0.020 |
| 456 | 17.677 (tau07_seed456) | 17.702 | -0.025 |
| 789 | 17.668 (adaptive_seed789) | 17.695 | -0.027 |
| 234 | 17.678 (adaptive_seed234) | 17.708 | -0.030 |

**Mean Δ = -0.023 ± 0.006, t(4) = -8.21, p = 0.0012, p_BH(k=9) = 0.011**

新 seed 的 Δ(-0.027, -0.030) 比原 3-seed 均值(-0.020) 更大——效应随 seed 增加未衰减。

⚠️ **配置一致性决策**：论文的 3-seed baseline 用 tau07_seed（τ=0.7，默认 n_min），新 seed 用 adaptive_seed（τ=0.7, n_min=2）。两者 τ 一致但 n_min 可能不同（取决于 tau07 训练时的默认值）。若需严格一致，可改用 adaptive_fix_seed（τ=0.7, n_min=2），此时 Δ 更大（-0.037±0.008, p_BH=0.005）。

## Permuted Score Control 确认 detector 信号 load-bearing (2026-05-24)

permuted_score_control_seed42: 将真实 q-score 随机打乱（保持 score 分布不变，但 score-sample 对应关系随机化）。
- holdout_ppl=17.919 vs uniform=17.694 → **Δ=+0.225（比 uniform 更差）**
- vs random_reweight (17.951): permuted 略好，因为仍保留了真实 score 分布的 shape
- **解读**：adaptive weighting 的效果来自 score 的排序正确性（正确识别哪些样本是 contaminated），而非权重的非均匀性。与 random_reweight 共同构成 Claim 2 的双重 ablation evidence。

## D062 coupling rule 已验证 (2026-05-17)

bs8_auto_nmin_r5 (PPL 17.66) 确认 n_min=⌊B/2⌋ coupling rule 在 bs=8 下有效（n_min=4）。
- bs=4, n_min=2: adaptive_fix PPL=17.653 (success)
- bs=8, n_min=4: bs8_auto_nmin_r5 PPL=17.66 (success)
- bs=8, n_min=2: bs8_nmin2_seed42_r2 PPL=17.73 (negative — n_min 过小导致 over-downweight)

结论：n_min=⌊B/2⌋ 是 Method section 的正式设计原则。n_min 过小 (< B/2) 导致 ESS 约束松弛，b* 过大。

## Batch-adaptive τ 方向关闭 (2026-05-17)

两轮实验均 negative。固定 τ=0.8 + dual constraint 已足够。不再投入资源。

## Claim 2 跨 seed 已由 D074 定稿 (2026-05-18)

grid b=0.3 三 seed (17.620±0.033) vs adaptive (17.651±0.007)，gap 0.031 在方差内。

## Claim 3 ρ=0.6 三 seed 完整 (2026-05-18)

Adaptive: mean 17.736±0.004 vs Uniform: mean 17.763±0.008, Δ=0.028。
adaptive 方差仅为 uniform 的一半。

## ρ=0.2 adaptive 无效 (2026-05-17)

D068 决定 Claim 3 scope 限制为 ρ≥0.4, τ∈[0.7,0.8]。ρ=0.2 在 Discussion 报告为 limitation。

## ρ=0.3 boundary check 结果 (2026-05-23, 3-seed 定稿)

| | Adaptive holdout | Uniform holdout | Δ holdout | Δ OWT | Δ Wiki |
|------|-----------------|----------------|-----------|-------|--------|
| seed42 | 17.422 | 17.422 | 0.000 | +0.010 | −0.032 |
| seed123 | 17.435 | 17.433 | +0.002 | +0.022 | −0.039 |
| seed456 | 17.424 | 17.419 | +0.005 | +0.006 | −0.007 |
| **mean** | **17.427** | **17.425** | **+0.002** | **+0.013** | **−0.026** |

**结论：ρ=0.3 是 transition zone（3-seed 确认）。** Adaptive 在 holdout/OWT 上无效（mean Δ = +0.002/+0.013），仅 wiki 上有微弱优势（−0.026）。
- vs ρ=0.2: adaptive 有害 → ρ=0.3: 中性 → ρ=0.4: 有效 (Δ=−0.020)
- 3-seed 内 Δ holdout 范围 [0.000, +0.005]，非常稳定
- 论文可报告为："method becomes effective at ρ ≥ 0.4; at ρ=0.3 the signal is too weak for reliable reweighting"

## Grid-b 曲线平坦性 (2026-05-17)

[0.2, 0.5] 区间 PPL 极平坦（b=0.2: 17.643, b=0.3: 17.640, b=0.5: 17.651）。adaptive b* 落在平坦区间内。

## 30476 SIGKILL 事件 (2026-05-17)

4 实验同时被 SIGKILL，oom_kill=0，根因不明。教训：查 cgroup 计数器。

## Llama-3.2-3B 跨模型泛化 (2026-05-17) — neutral-to-positive

PPL: adaptive 10.58 vs uniform 10.53 (Δ=+0.05); MMLU: adaptive 53.42% vs uniform 51.85% (Δ=+1.57pp, 3.9σ)

## 1.7B 规模验证 — positive (2026-05-18) — Line B

Qwen3-1.7B: adaptive PPL=13.27 vs uniform (Plan B) PPL=13.50, Δ=-0.23。
Plan B 公平性限制：uniform fresh optimizer。1.7B seed123 from scratch 在跑消除 confound。

## Multi-Detector 结论 (2026-05-18, 更新)

| Detector | AUC | Adaptive PPL | Uniform PPL | Δ | 结论 |
|----------|-----|-------------|-------------|---|------|
| TF-IDF+LR | 0.94 | 17.65 | 17.69 | -0.04 | ✅ positive |
| GPT-2 PPL | 0.913 | **17.79** | 17.69 | **+0.10** | ❌ negative |
| N-gram PPL | 0.73 | 17.82 | 17.69 | +0.13 | ❌ negative |

**关键洞察：AUC 不是充分条件。**

## 30476 路径注意 (2026-05-18)

- eval 数据：`data/human/eval_holdout.jsonl`（NOT `data/eval_holdout.jsonl`）
- output_dir：`/root/autodl-tmp/output/models/`（NOT `/root/autodl-tmp/provenance_weight_training/output/models/`）

## Batch-size Amplification 完整趋势 (2026-05-23, 定稿)

| Batch Size | n_min | Seeds | Adaptive holdout | Uniform holdout | Δ(A−U) holdout |
|-----------|-------|-------|-----------------|----------------|----------------|
| B=4 | 2 | 3 | 17.674±0.007 | 17.694±0.008 | −0.020±0.008 |
| B=8 | 4 | 2 | 17.641 | 17.691 | −0.050 (−0.044, −0.056) |
| B=16 | 8 | 3 | 17.631±0.008 | 17.694±0.015 | −0.068±0.005 |

**单调递增趋势确认（3 数据点）：B=4 → B=8 → B=16，Δ 从 −0.020 → −0.050 → −0.068**
B=8 2-seed 精确数据：
- seed42: adaptive=17.650, uniform=17.694, Δ=−0.044
- seed123: adaptive=17.631, uniform=17.687, Δ=−0.056

机制：更大 batch → n_min 绝对值更大 → weight distribution 有更多自由度做细粒度调节

## Epoch Confound 量化证据 (2026-05-22, 3-seed 完整定稿)

### D&R full 3-seed
| seed | holdout | owt | wiki |
|------|---------|-----|------|
| 42 | 17.285 | 18.014 | 15.05 |
| 123 | 17.272 | 18.008 | 15.05 |
| 456 | 17.277 | 18.017 | 15.04 |
| **mean** | **17.278±0.007** | **18.013±0.005** | **15.047±0.006** |

### dr_epoch_matched 3-seed
| seed | holdout |
|------|---------|
| 42 | 17.651 |
| 123 | 17.659 |
| 456 | 17.660 |
| **mean** | **17.657±0.005** |

### Epoch confound per seed
| seed | D&R full | epoch-matched | adaptive baseline | confound % |
|------|---------|---------------|-------------------|------------|
| 42 | 17.285 | 17.651 | 17.653 | 99.5% |
| 123 | 17.272 | 17.659 | 17.643 | >100% |
| 456 | 17.277 | 17.660 | ~17.651 | >100% |

**全部 3 seed 确认：D&R 表观优势 100% 来自 epoch confound。**

⚠️ 旧版 dr_epoch_matched_seed123 (holdout=18.332) 因 grad_accum 配置错误（effective batch=4）已作废。

## Random Reweight 3-seed 定稿 (2026-05-22)

| seed | holdout | owt | wiki |
|------|---------|-----|------|
| 42 | 17.958 | 18.606 | 15.519 |
| 123 | 17.945 | 18.622 | 15.562 |
| 456 | 17.951 | 18.602 | 15.503 |
| **mean** | **17.951±0.007** | **18.610±0.011** | **15.528±0.031** |

vs adaptive mean holdout=17.651 → **Δ=+0.300**, vs uniform=17.694 → **random 差于 uniform by 0.257**
**3-seed 稳健确认：detector signal 是 load-bearing 的。**

## [失败模式] eval fp16 vs bfloat16 dtype 不匹配 (2026-05-22)

eval_perplexity.py 用 `torch.float16` 加载 bfloat16 训练的模型。wiki 大数据量触发溢出 → NaN。**已修复：改为 bfloat16。**

## [失败模式] grad_accum 配置遗漏 (2026-05-21)

提交前必须逐项验证 effective batch = batch_size × grad_accum = 16。

## [失败模式] 磁盘空间 — westd-41312 checkpoint 保存 (2026-05-23)

/root/autodl-tmp 250GB 被 checkpoint 占满，4 实验同时崩溃。修复：清理 97GB 旧 checkpoint + 所有后续实验加 --save_total_limit 2。提交新实验前必须 df -h 预检。

## [失败模式] Cron 误判完成的实验为 failed (2026-05-24)

permuted_score_control_seed42 和 contamination_20_tau07_seed42 训练正常完成（6103/6103 steps, "Training complete"），但因无 W&B sentinel 被 cron 5× miss auto-resolve 为 failed。**根因**：submit_training_job 的 cron 依赖 W&B metrics 或 sentinel 文件判断完成，但这些实验没有配置 W&B。**修复**：收到 cron failed 回调时，必须先 tail_training_logs 验证日志最后是否有 "Training complete" 再判断真实结论。
