# Figure Plan — Recovery-Aware Structured Pruning (RASP)

---

## Fig 1: RASP Pipeline Overview

**类型**: 流程/架构图（method figure）

**内容**:
```
Pre-trained Reasoning LLM (DeepSeek-R1-Distill-Qwen-7B)
        │
        ├──────────────────────────┐
        ▼                          ▼
  Importance I(h)           CKA Overlap F(h)
  (Taylor gradient)        (intra-layer pairwise)
        │                          │
        └──────────┬───────────────┘
                   ▼
        RASP Score: S(h) = I(h) × (1 - F(h))^α
                   │
                   ▼
        Structured Pruning (remove lowest S(h))
                   │
                   ▼
        ┌──────────┴──────────┐
        ▼                     ▼
  SFT Warmup              [对比: Standard Pruning]
  (fix generation)         只用 I(h), 无 F(h) 修正
        │
        ▼
  GRPO RLVR Recovery
  (restore reasoning)
        │
        ▼
  Recovered Compact Model
```

**关键设计要素**:
- 左侧主 pipeline 用蓝色系，右侧 Standard 对比用灰色/红色
- I(h) 和 F(h) 分支用不同颜色区分（如蓝 vs 橙），在合并处突出 RASP scoring 公式
- Standard pruning 旁路用虚线表示，标注 "importance-only"
- Recovery 阶段标注 "SFT Warmup → GRPO" 两步
- 在 CKA Overlap 框旁加小示意：同层 head 间 pairwise CKA matrix

**数据可用性**: 无需实验数据，纯方法示意图

**建议工具**: TikZ（最佳）或 matplotlib + patches + FancyArrowPatch

**论文位置**: Section 3 (Method) 开头，首次引用

**尺寸**: 双栏宽度（full width），高度约 6-8cm

---

## Fig 2: CKA Overlap vs Recoverability Scatter Plot

**类型**: 散点图

**内容**:
- **X 轴**: F(g) — per-structure CKA functional overlap（pruned structure 与其最相似 retained structure 的 CKA）
- **Y 轴**: Recoverability — retained structure 在 pruned model vs GRPO-recovered model 之间的 activation shift（1 - cosine similarity）
- 每个点 = 一个被剪掉的 structure（attention GQA group 或 MLP channel group）
- 按 structure type 着色：蓝色 = attention，橙色 = MLP
- 或按 layer index 着色（viridis colormap）+ colorbar
- 回归线 + Spearman ρ 及 95% CI 标注在图上
- 标注 2-3 个典型点（如 "Layer 2 attn: low F(h), low recovery" vs "Layer 25 attn: high F(h), high recovery"）

**数据来源**:
- `correlation_analysis.py` 输出 `correlation_results.json`
- 需要：base model, pruned model (RASP 20%), GRPO-recovered model, `cka_scores.pt`, `pruning_metadata.pt`
- 服务器路径: `/root/autodl-tmp/recovery_aware_struct_prune/` 下的对应 checkpoint

**数据可用性**: **待 correlation_analysis.py 执行**。代码已写好（`artifacts/correlation_analysis.py`），需 GRPO stage 2 checkpoint 完成后运行。GRPO v2 状态: DONE（`grpo_stage2_rasp_20_DONE_20260515`）

**关键设计要素**:
- 颜色方案：attention (#1f77b4) vs MLP (#ff7f0e)，与 `correlation_analysis.py` 一致
- 点大小 30，alpha 0.7，黑色细边框
- 右下角文本框：ρ = X.XX, 95% CI [X.XX, X.XX], p < 0.001
- 如果 attention 和 MLP 趋势不同，可考虑分面（两个子图）
- 灰色虚线标注 "Recoverable zone" 阈值

**建议工具**: matplotlib（已有 `make_scatter_plot` 函数，需微调为论文质量）

**论文位置**: Section 5.3 (Claim 2: F(h) predicts recoverability)

**尺寸**: 单栏宽度，约 8cm × 6cm

---

## Fig 3: RLVR vs SFT Recovery Trajectory

**类型**: 折线图

**内容**:
- **X 轴**: Training steps
- **Y 轴**: GSM8K accuracy (%) 或 reward mean
- **4 条线**:
  1. RASP + SFT → GRPO（蓝色实线，主角）
  2. Standard + SFT → GRPO（红色实线）
  3. RASP + SFT only（蓝色虚线）
  4. Standard + SFT only（红色虚线）
- 分两阶段：SFT warmup（左半）→ GRPO recovery（右半），用竖线分隔
- **关键标注**:
  - "Reward Desert" 区域：Standard + GRPO 在某步数后 reward 停滞的区间（灰色阴影）
  - RASP + GRPO 的持续上升趋势
  - 水平虚线标注 baseline accuracy (82.6%)
  - 各条线终点标注最终准确率

**数据来源**:
- wandb runs: SFT training logs (train loss / eval accuracy per step)
- wandb runs: GRPO v2 training logs (reward_mean, gsm8k_accuracy per step)
- 4 个 run：`sft_rasp_20`, `sft_standard_20`, `grpo_stage2_rasp_20`, `grpo_stage2_standard_20`

**数据可用性**: **部分已有**。SFT runs 已完成。GRPO stage 2 runs 已完成（DONE status）。需从 wandb 提取 step-level metrics。

**关键设计要素**:
- 颜色方案：RASP = 蓝色系 (#1f77b4)，Standard = 红色系 (#d62728)；实线 = +GRPO，虚线 = SFT only
- X 轴两段拼接：SFT steps (0 → SFT_end) | GRPO steps (0 → 2000)，中间竖虚线分隔标注 "SFT → GRPO"
- 水平灰色虚线标 baseline 82.6%
- "Reward Desert" 灰色阴影区（Standard GRPO 停滞区间）
- 图例放右下角，避免遮挡曲线

**建议工具**: matplotlib

**论文位置**: Section 5.4 (Claim 3: Recovery method conditions optimal pruning)

**尺寸**: 双栏宽度或 1.5 栏宽度，高度约 5-6cm

---

## Fig 4: α Ablation 曲线（可选）

**类型**: 折线图 + 误差棒

**内容**:
- **X 轴**: α 值 {0, 0.5, 1.0, 2.0, 4.0}
- **Y 轴**: Post-prune GSM8K accuracy (%)
- 单条线 + 95% CI 误差棒
- α=0 等价于 Standard pruning（标注）
- α=1.0 为当前默认值（用星号或不同 marker 高亮）
- 可选第二条线：post-recovery accuracy（如果有对应 GRPO 数据）

**数据来源**:
- `src/run_alpha_ablation.sh` 输出
- α=1.0 已有结果（24.3% post-prune on full eval）
- 其他 α 值待运行

**数据可用性**: **待 α ablation 实验执行**。代码和脚本已准备好（`src/run_alpha_ablation.sh`）。α=1.0 可复用。磁盘空间约束需顺序执行（每个 α prune → eval → 删除 → 下一个）。

**关键设计要素**:
- X 轴用 log scale 或等距排列（0 作为特殊点）
- α=0 标注 "= Standard"
- α=1.0 用 ★ marker
- 如果存在最优点，用箭头标注
- 灰色水平虚线标 baseline

**建议工具**: matplotlib

**论文位置**: Section 5.5 (Ablation Studies)

**尺寸**: 单栏宽度，约 7cm × 5cm

---

## Fig 5: Per-layer Pruning Distribution（可选）

**类型**: 分组柱状图（grouped bar chart）

**内容**:
- **X 轴**: Layer index (0-27)
- **Y 轴**: 该层被剪掉的 structure 数量（或剪枝比例 %）
- **两组柱**: Standard (红) vs RASP (蓝)
- 可分为上下两个子图：attention heads (上) + MLP groups (下)
- 突出关键差异：RASP 在哪些层保留更多、在哪些层剪掉更多

**数据来源**:
- `pruning_metadata.pt` 中的 `attn_keep_masks` 和 `mlp_keep_masks`
- 需要 Standard 和 RASP 两个版本的 pruning metadata
- 服务器路径: `/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20/` 和 `pruned_standard_20/`

**数据可用性**: **已有**。两个 pruned model 目录中各有 `pruning_metadata.pt`。

**关键设计要素**:
- 柱宽窄（28 层 × 2 组），用颜色区分 Standard vs RASP
- 标注差异最大的层（如 "Layer 5: RASP 保留全部 4 GQA groups，Standard 只保留 2"）
- 上方标注总剪枝预算相同（matched parameter count）
- 考虑用热力图替代（层 × method，颜色深浅 = 剪枝比例），更紧凑

**建议工具**: matplotlib

**论文位置**: Section 5.2 (Analysis) 或 Appendix

**尺寸**: 双栏宽度（如果柱状图）或单栏（如果热力图）

---

## Fig 6: CKA Overlap Heatmap（可选）

**类型**: 热力图

**内容**:
- 展示某代表层（如 Layer 12）的 attention head/GQA group 间 pairwise CKA overlap matrix
- 或展示所有 28 层的 per-head mean overlap 作为 1D heatmap
- 对角线为 1.0，颜色从浅（低 overlap）到深（高 overlap）
- 标注高 overlap 区域 = "redundant but recoverable" 和低 overlap 区域 = "unique, must preserve"

**数据来源**:
- `results/cka_scores.pt`
- 包含 `attn_cka_matrix` (per-layer pairwise CKA) 和 `attn_overlap` (per-head mean overlap)

**数据可用性**: **已有**。`cka_scores.pt` (122KB) 已缓存在服务器。

**关键设计要素**:
- 颜色方案：`coolwarm` 或 `YlOrRd`（学术标准）
- 如果展示单层 pairwise matrix：4×4 (GQA groups) 或更大
- 如果展示全层 summary：28 行 × N 列热力图
- 对角线标为灰色（self-overlap = 1.0，不 informative）
- 叠加 RASP 剪枝决策标记（✓ 保留 / ✗ 移除）

**建议工具**: matplotlib + seaborn.heatmap

**论文位置**: Section 4 (CKA-based Functional Overlap) 或 Appendix

**尺寸**: 单栏宽度

---

## 汇总

| 图号 | 标题 | 类型 | 数据状态 | 位置 | 宽度 |
|------|------|------|----------|------|------|
| Fig 1 | RASP Pipeline Overview | 流程图 | 无需数据 | §3 Method | 双栏 |
| Fig 2 | CKA Overlap vs Recoverability | 散点图 | 待 correlation_analysis 运行 | §5.3 Claim 2 | 单栏 |
| Fig 3 | Recovery Trajectory | 折线图 | 待 wandb 数据提取 | §5.4 Claim 3 | 双栏 |
| Fig 4 | α Ablation | 折线图 | 待 ablation 实验 | §5.5 Ablation | 单栏 |
| Fig 5 | Per-layer Pruning Distribution | 柱状图/热力图 | ✅ 已有 | §5.2 / Appendix | 双栏 |
| Fig 6 | CKA Overlap Heatmap | 热力图 | ✅ 已有 | §4 / Appendix | 单栏 |

**优先级**: Fig 1 > Fig 3 > Fig 2 > Fig 5 > Fig 4 > Fig 6

**全局风格约束**:
- 字体: 与 LaTeX 正文一致（serif / Computer Modern），matplotlib 中用 `plt.rcParams['font.family'] = 'serif'`
- 字号: 轴标签 ≥ 9pt，刻度标签 ≥ 8pt（单栏图缩放后仍可读）
- 颜色一致性: 全文 RASP = 蓝色 (#1f77b4)，Standard = 红色 (#d62728)，GRASPrune = 绿色 (#2ca02c)，Baseline = 灰色
- 输出格式: PDF（矢量图，用于 LaTeX）+ PNG 300dpi（备用）
- 无网格或仅用浅灰网格
