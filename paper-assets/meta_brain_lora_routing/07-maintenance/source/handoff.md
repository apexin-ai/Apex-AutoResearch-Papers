# Director Handoff — 2026-05-17 03:40 UTC

## 🎉 重大进展：Eval 通了 + Nominal Baseline 已建立

### Nominal Baseline: 66% (50 episodes, libero_spatial)
- 使用 `eval_base_no_lora.py`（OpenPIMetaBrainPolicy, routing=none）
- 9 个 tasks，成功率 20%-100% 不等（平均 66%）
- 所有失败均为 timeout，无崩溃
- 低于 openpi 官方 ~80%，但作为项目内 relative comparison 完全有效
- 明显弱项："on ramekin" 仅 20%（如果 LoRA routing 能改善 hard cases 是很好的 evidence）

### Eval 根因修复
最终根因：`jaxtyping 0.2.36 + beartype 0.22.9` 严格检查拒绝 `np.True_` 作为 image_mask。修复：入口加 `jaxtyping_disable = True`。
LIBERO-Plus 包含所有原版 tasks，无需单独安装原版 LIBERO。

## 当前运行中

| GPU | 任务 | 状态 |
|-----|------|------|
| 0 | visual v3 LoRA training (final) | 接近完成 |
| 1 | rank-48 universal training (plan_013) | step 250/10K, ~3.5h |
| 2 | perturbation degradation eval | Worker 在跑 |
| 3 | v3 LoRA routing eval | Worker 在跑 |

## 等待中的关键结果（最重要！）

1. **Perturbation degradation 数据**：frozen model 在 _table/_tb/_add/_language 各 20 ep 的成功率。期望显著低于 66% baseline → 证明扰动确实 hurt performance。

2. **v3 LoRA routing eval**：
   - routing=universal（通用 adapter 对照）
   - routing=par（PAR 自动路由到对应 expert）
   - 期望 PAR > universal > frozen，核心 Claim 2

3. **rank-48 universal 完成后**：与 4×r16 PAR routing 做参数量对比（Claim 3）

## 下一步决策

收到上述结果后：
- 如果 PAR > universal 且差异显著 → 核心假设成立，进入论文写作
- 如果 PAR ≈ universal → 需要分析 routing 是否实际生效，可能 router 需重训（基于新 checkpoint activations）
- 如果 perturbation 没有 degradation → 研究假设不成立，需 pivot

## 关键注意事项

- **PAR Router 可能需要重训**：当前 router 基于 pi0_base（旧 checkpoint）的 activations 训练。换了 fine-tuned checkpoint 后 activation 分布可能不同。如果 PAR routing 表现不如预期，第一个检查点是 router 兼容性。
- **正确 eval 脚本**：`eval_base_no_lora.py`（使用 OpenPIMetaBrainPolicy）
- **正确 checkpoint**：`/root/autodl-tmp/checkpoints/pi0_libero_openpi/`
- **废弃路径**：`/root/autodl-tmp/checkpoints/pi0_libero/`（lerobot base model）
- **Reviewer 注意**：rank-48 参数量对比不完全精确（r48=11.1M vs 4×r16=14.7M total stored, 但 inference 时 r48=11.1M active vs PAR routing=3.7M active）。论文需精确说明对比维度。

## CoRL DDL: 2026-05-29（12 天）

时间充裕。当前 eval 结果 40-60 min 内返回。之后进入论文写作阶段。
