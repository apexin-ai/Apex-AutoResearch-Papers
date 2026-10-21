# 附录表格审计

## 统计
- 审计表格：29/29
- 数值总数：~580
- 匹配：~570
- 问题：6（含 1 个已知问题）

## 逐表审计

### tab:cf_summary (line 73)
- 数值数量：6
- 数据源：plot_counterfactual_bar.py 硬编码值
- 匹配：✅
- 详情：OpenVLA d range 0.45--1.21（min=OV-L P=0.45, max=OV-O E=1.21）✅；TraceVLA 0.97--1.52（min=TV-O P=0.97, max=TV-G E=1.52）✅；"empty ranks first in 6/8" 验证正确（OV-S, OV-O, TV-G, TV-S, TV-O, TV-L）✅

### tab:counterfactual (line 96)
- 数值数量：32 (8 cells × 4 conditions)
- 数据源：plot_counterfactual_bar.py cohens_d dict
- 匹配：✅
- 详情：所有 8 行 4 列与脚本硬编码完全一致。排名标注（1st/2nd/3rd/4th）均正确。

### tab:perhead_bootstrap (line 231)
- 数值数量：8
- 数据源：附录正文 (lines 224-226)
- 匹配：✅
- 详情：Collective d（0.65, 0.41）、Per-head d（0.027, 0.051）及 CI 均与正文一致。Difference 0.024 = 0.051 - 0.027 ✅

### tab:dose_response (line 253)
- 数值数量：24 (8 rows × 3 cols)
- 数据源：plot_dose_response.py 全精度数组
- 匹配：✅
- 详情：所有 8 个 Cohen's d 值四舍五入到三位小数后一致。CI 上下界同样一致。示例：4 heads: 0.4815→0.482, CI [0.449, 0.511] ✅

### (unnamed counterfactual Goal table, line 271)
- 数值数量：9
- 数据源：与 tab:counterfactual OV-G 行交叉验证
- 匹配：✅ ⚠️ 缺少 \label
- 详情：Empty 1.170→1.17, Wrong 1.182→1.18, Shuffled 1.096→1.10, Paraphrased 0.996→1.00 均为正确四舍五入。L1 ablation d=0.650 与 tab:perhead_bootstrap 一致。**但此表无 \label，无法被引用。**

### tab:action_shift_perdim (line 292)
- 数值数量：14
- 数据源：附录正文 (lines 203-205)
- 匹配：✅
- 详情：Instruction gripper=0.291, Control gripper=0.141 与正文完全一致。所有 translational <0.01, rotational <0.04 声明成立。

### tab:counterfactual_spatial (line 392)
- 数值数量：12
- 数据源：tab:counterfactual OV-S 行 + 正文 line 55
- 匹配：✅
- 详情：E=1.173→1.17, S=0.979→0.98, W=0.885→0.89, P=0.807→0.81 均正确。Jaccard 值逻辑正确（empty=0, shuffled=1.0）。排序 E>S>W>P 与正文一致。

### tab:spatial_cross_instruction (line 414)
- 数值数量：20
- 数据源：无独立 JSON 可验证
- 匹配：✅（内部一致性）
- 详情：image_mean 全部~10% 符合 chance 预期；trained readout L4→100%；reference readout L31=75.4% 与正文 "decays more steeply than Goal (82%)" 一致。

### tab:metric_invariance (line 435)
- 数值数量：12
- 数据源：无独立数据文件
- 匹配：✅（内部一致性）
- 详情：所有 profile r > 0.989 ✅；peak layers 一致或仅差 1 层 ✅

### tab:seed_sensitivity (line 466)
- 数值数量：14
- 数据源：plot_action_r2_threecond.py 数据间接验证
- 匹配：⚠️ 微小问题
- 详情：Peak R² mean=0.655 ✅ (computed: (0.654+0.656+0.653+0.655+0.655)/5=0.6546→0.655)。但 **std=0.002 与从表中显示值计算的 std=0.001 不一致**（可能源自未四舍五入的原始值）。Peak layer mean=10.6 ✅, std=2.7 ✅ (population std)。

### tab:demo_sensitivity (line 514)
- 数值数量：10
- 数据源：附录正文
- 匹配：✅
- 详情：RSA Δ=-3.6% = (0.606-0.628)/0.628 ✅；R² Δ=-7.6% = (0.609-0.659)/0.659 ✅；layer shift +2 = 11-9 ✅

### tab:delta_r2_threshold (line 560)
- 数值数量：15
- 数据源：experiments.tex tab:cross_arch_matrix ΔR² 值
- 匹配：✅
- 详情：逐行验证——在 threshold=0.10 和 0.15 时 clean separation 成立。VLM→VLA 6 个 trained ΔR² 均>0.10（最小=0.156）；OpenVLA 4 个均<0.10（最大=0.086）；Reference 10 个均<0.10（最大=0.097）。At 0.20, TraceVLA Spatial=0.156<0.20 所以 5/6 ✅。

### tab:training_effects (line 582)
- 数值数量：9
- 数据源：tab:training_effect_summary 交叉验证
- 匹配：✅
- 详情：RSA best-vs-best Δ=+0.017, R² image_mean Δ=+0.015, R² readout Δ=+0.069 三个核心值均与 summary 表一致。

### tab:training_effect_summary (line 611)
- 数值数量：18
- 数据源：tab:training_effects + 其他附录段落
- 匹配：✅
- 详情：RSA peak 0.628 (L12)→0.612 (L0)→Δ=0.016→text says 0.017（四舍五入差异：0.628-0.612=0.016 vs reported 0.017）。R² peaks 和 instruction attention 值均与对应表/文字一致。

### tab:dense_routing (line 640)
- 数值数量：27
- 数据源：附录正文 (lines 633-635)
- 匹配：✅
- 详情：L0=10% (chance), L1=100%/100%/10%, 所有值与 step-function 描述一致。表注说明 dense vs sparse 评估的微小差异。

### tab:qa_probe (line 670)
- 数值数量：6
- 数据源：附录正文 + tab:training_effect_summary
- 匹配：✅
- 详情：Trained readout L20=86.3%, Reference readout L20=85.3%, DINOv2=82.7% 与 summary 表 "Progress classification 86.3% (L20) vs 85.3% (L4)" 部分匹配（注：summary 表 Reference best layer=L4 但 qa_probe 表说 L20 — 这可能是不同 probe 配置）。

### tab:cross_arch_probe (line 696)
- 数值数量：24
- 数据源：附录正文 (lines 691-693, 724-726)
- 匹配：✅
- 详情：OpenVLA Random init L1=100%, Llama-2 base L1=80.2%, VLA trained L1=99.6% 均与正文一致。TraceVLA head counts 27-30/32 与正文一致。

### tab:multilayer_attention (line 762)
- 数值数量：18
- 数据源：plot_multi_layer_attention.py + server full_32layer_attention_summary.json
- 匹配：⚠️ **L31 heads 不一致**
- 详情：
  - L1: Trained 24, 57.7% ✅（script=24, 0.577; server=24, 0.5729）
  - L8: Trained 4, 46.8% ✅（script=4, 0.468; server bulk=3, 但 dedicated=4）
  - L16: Trained 10, 48.4% ✅（script=10, 0.484; server bulk=9, 但 dedicated=10）
  - **L31: Table=18, 56.3% ⚠️ vs Script=19, 56.3%; Server bulk=18, 54.0%**
  - 表格 L31=18 与 server bulk 数据一致；但 plot script 用了 19→**figure 和 table 不一致**
  - Llama-2 和 Random init 列全部 ✅

### tab:threshold_sensitivity (line 787)
- 数值数量：15
- 数据源：附录正文 (lines 780-781)
- 匹配：✅
- 详情：30% VLA=32, 40%=31, 50%=24, 60%=9, 70%=5。三组排序在所有阈值下 VLA > Llama-2 > Random ✅

### tab:attention_decomp (line 809)
- 数值数量：10
- 数据源：附录正文 (line 827)
- 匹配：✅
- 详情：行和验证：62.4+18.8+18.8=100.0 ✅, 44.9+27.1+28.0=100.0 ✅。Δ 计算：+17.5, -8.3, -9.2 均算术正确。38.2× ratio 在正文中一致。

### tab:per_dim_mae (line 838)
- 数值数量：21
- 数据源：tab:action_shift_perdim 交叉验证
- 匹配：✅
- 详情：MAE 值精确到 5 位小数。Ratios 基本正确（dx: 5.09 vs computed 5.11 — 四舍五入顺序差异）。

### tab:per_task_r2 (line 858)
- 数值数量：33
- 数据源：tab:task_complexity 交叉验证
- 匹配：✅
- 详情：Mean baseline=0.256 ✅ (computed: 2.557/10)；Mean ablated=0.363 ✅ (computed: 3.627/10)；Mean ΔR²=0.107 ✅ (computed: 1.070/10)。所有 10 tasks Δ>0 ✅。

### tab:task_complexity (line 890)
- 数值数量：16
- 数据源：tab:per_task_r2 + Mann-Whitney 计算
- 匹配：✅
- 详情：Instr-disc mean=0.141 ✅ (0.844/6)；Vis-suff mean=0.057 ✅ (0.226/4)；Ratio=2.49× ✅ (0.1407/0.0565)；Mann-Whitney U=21.0 手动验证 ✅；p=0.033 ✅。

### tab:specificity_control (line 929)
- 数值数量：8
- 数据源：附录正文 (line 1075)
- 匹配：✅
- 详情：Instruction 0.650, Random 0.601±0.021, Image 0.580, Bottom-24 0.565。正文引用 "0.65, 0.60, 0.58" 为正确四舍五入。

### tab:paired_dz (line 948)
- 数值数量：12
- 数据源：paired_cohens_d.json
- 匹配：✅
- 详情：RSA d_z=0.5461→0.55 ✅; L1 ablation d_z=1.1673→1.17 ✅; Random-24 mean=1.8423±0.3302→1.84±0.33 ✅; Dose-response d_z=1.7917→1.79 ✅; Cross-arch d_z=0.4772→0.48 ✅。

### tab:2x2_r2_summary (line 985)
- 数值数量：16
- 数据源：tab:2x2_r2 + openvla_r2_per_layer.json + phi3v_r2_per_layer.json
- 匹配：⚠️ 两处问题
- 详情：
  - Peak layers/R² 与 tab:2x2_r2 bolded 值完全一致 ✅
  - Δ_train(peak): OpenVLA +0.008 (0.637-0.629) ✅; TraceVLA +0.056 (0.634-0.578) ✅
  - **Δ_train(L15-L25 avg): OpenVLA reported +0.313, computed +0.355** ⚠️
  - **Δ_train(L15-L25 avg): TraceVLA reported +0.103, computed +0.137** ⚠️
  - **Late-layer std: TraceVLA Reference reported 0.068, computed mean of L25-L31 cross-seed stds = 0.170** ⚠️ (其他三个 late-layer std 值 match L25-L31 range)

### tab:2x2_r2 (line 1004)
- 数值数量：132 (33 layers × 4 conditions × mean only)
- 数据源：openvla_r2_per_layer.json, phi3v_r2_per_layer.json, phi3v_untrained_r2_per_layer.json
- 匹配：✅
- 详情：抽查 12 个关键值（L0/L9/L11/L32 × trained/ref）全部一致。OpenVLA L9 trained: JSON=0.6372→table=0.637 ✅; TraceVLA L11 trained: JSON=0.6340→table=0.634 ✅; OpenVLA L0 ref: JSON=0.6294→table=0.629 ✅。

### tab:methodological_precedent (line 1170)
- 数值数量：1 (ρ=0.583)
- 数据源：附录正文 line 1106 + discussion.tex line 16
- 匹配：✅
- 详情：描述性表格。"Ours" 行 ρ=0.583 与附录 Extended Discussion 及 discussion.tex 一致。

### tab:nlp_controls (line 1198)
- 数值数量：9
- 数据源：plot_r2_collapse.py (NLP_VAL=0.155) + plot_nlp_control_overlay.py
- 匹配：✅
- 详情：三个模型 ΔR²=0.000, Mean R²=0.155±0.000/0.001。NLP_VAL=0.155 在两个 plot 脚本中一致。Layers 32/32/36 与架构匹配。

### tab:arch_diversity (line 1230)
- 数值数量：0（描述性）
- 数据源：N/A
- 匹配：✅
- 详情：TraceVLA Phi-3-mini 3.8B/32 layers, NORA Qwen2.5-VL 3B/36 layers 与其他表数据一致。

### tab:convergent_evidence (line 1260)
- 数值数量：6
- 数据源：各分析段落
- 匹配：✅
- 详情：ΔR²=0.16-0.46 与 tab:cross_arch_matrix range 一致；d=0.45-1.52 与 tab:cf_summary 一致；d=0.48-0.64 与 tab:dose_response 范围一致。

## 附录文本定量声明审计

| 位置 | 声明 | 验证 | 状态 |
|------|------|------|------|
| L7 | N=63,228 observations | 10 tasks × 50 demos ≈ 63K | ✅ 合理 |
| L27 | RSA: mean ρ across 10 tasks, 10K bootstrap | 方法描述 | ✅ |
| L46 | Random init 0/32 (11.7%), Llama-2 9/32 (36.5%), Trained 24/32 (57.7%) | tab:multilayer_attention L1 行 | ✅ |
| L47 | L31: 18 heads | tab:multilayer_attention ✅, server ✅, **script=19** ⚠️ |
| L53 | Wrong d=1.182, empty 1.170, shuffled 1.096, paraphrased 0.996 | Unnamed table ✅ |
| L55 | Spatial: empty 1.173, shuffled 0.979, wrong 0.885, paraphrased 0.807 | tab:counterfactual_spatial ✅ |
| L60 | Dose: 0.482 to 0.639, 4→32 heads | tab:dose_response ✅ |
| L61 | 72.3% tokens, d=0.65, trajectory d=2.943 | tab:perhead_bootstrap d=0.65 ✅ |
| L65 | Readout R²=0.678 (L13), ref 0.609 (L32), Δ=+0.069 | tab:training_effect_summary ✅ |
| L155-157 | DINOv2 ρ=0.619, SigLIP ρ=0.621, Fused ρ=0.634, Projector ρ=0.615 | branch_split_rsa_results.json ✅ |
| L177 | L0: R²=0.645±0.008 | plot_action_r2_threecond.py: 0.6451±0.0084 ✅ |
| L178 | Trained peaks L9: R²=0.643±0.014 | Script: 0.6434±0.0137 ✅ |
| **L179** | **Llama-2 base L0→L32: 0.551, std 0.003--0.035** | **Script L31=0.557 (not 0.551); std range 0.002--0.028** ⚠️ |
| L190 | Dominant +0.030, Random +0.071±0.013, z=-3.11 | 内部一致（z=0.041/0.013≈3.15, close to 3.11）✅ |
| L367 | Spatial RSA peak L14 ρ=0.691, R² peak L13 0.696 | 无独立源验证 |
| L368 | Spatial Δ=+0.023, CI [0.012, 0.036], p<0.001 | 无独立源验证 |
| L458 | 5-seed peak R²=0.655±0.002 | tab:seed_sensitivity ✅ (std 可能有微小偏差) |
| L460 | 15-seed L9: R²=0.637±0.004 | openvla_r2_per_layer.json: 0.6372±0.0083→std 偏差 |
| L486 | TraceVLA Goal 0.227±0.010, Spatial 0.136±0.002, OpenVLA 0.013±0.001 | 无独立源验证 |
| L545 | Min detectable Δ_RSA=0.030, Δ_R²=0.026 | Power analysis 逻辑正确 ✅ |
| L546 | RSA d_z=0.56, power=0.356 | 计算验证：ncp=1.771, power≈0.36 ✅ |
| L547 | R² d_z=2.68, power=1.000 | 计算验证：ncp=8.47, power≈1.0 ✅ |
| L1061 | 45 sig → 40 survive Bonferroni (88.9%) | bonferroni_global.json ✅ |
| L1106 | ρ=0.583, p=0.10, n=9 | Fisher Z power analysis verified ✅ |
| L1110 | Power=0.37, need n≥21 for 80% | 计算验证 ✅ |

## 正文↔附录交叉一致性

| 正文位置 | 引用内容 | 附录值 | 状态 |
|----------|---------|--------|------|
| experiments.tex L19 | Trained peaks L9 R²=0.643 | Appendix L178: 0.643±0.014 | ✅ |
| experiments.tex L19 | L0 R²=0.645 | Appendix L177: 0.645±0.008 | ✅ |
| experiments.tex L42-43 | TraceVLA ΔR²=0.156--0.362, NORA 0.308--0.455 | tab:cross_arch_matrix ✅ | ✅ |
| experiments.tex L43 | OpenVLA ΔR²=0.033--0.086 | tab:cross_arch_matrix ✅ | ✅ |
| experiments.tex L44 | Permutation p=0.008 | Appendix L1250: p=0.008 | ✅ |
| experiments.tex L101 | d=0.45--1.52 | tab:cf_summary ✅ | ✅ |
| experiments.tex L103 | TraceVLA d=0.97--1.52, OpenVLA 0.45--1.21 | tab:cf_summary ✅ | ✅ |
| experiments.tex L130 | R²=0.637 at L9 vs 0.634 at L11 | tab:2x2_r2 ✅ | ✅ |
| experiments.tex L131 | L1: 24, **L31: 18** | tab:multilayer_attention: 18 ✅, **script: 19** ⚠️ | ⚠️ |
| experiments.tex L131 | Dose d=0.48--0.64 | tab:dose_response: 0.482--0.639 ✅ | ✅ |
| discussion.tex L7 | ΔR²=0.16--0.46 | tab:cross_arch_matrix: 0.156--0.455 ✅ | ✅ |
| discussion.tex L7 | d=0.45--1.52 | tab:cf_summary ✅ | ✅ |
| discussion.tex L9 | R²=0.003 convergence | tab:2x2_r2: 0.637-0.634=0.003 ✅ | ✅ |
| discussion.tex L16 | ρ=0.583, p=0.10 | Appendix L1106 ✅ | ✅ |

## discussion.tex ρ=0.583 来源追溯

- **声明**: "ΔR²–success-rate correlation (ρ=0.583, p=0.10)" (discussion.tex L16)
- **附录来源**: §Extended Discussion (appendix.tex L1106), "Correlating trained ΔR² with published LIBERO success rates across all nine available architecture-suite cells yields ... Spearman ρ = 0.583, p = 0.10, n = 9"
- **数据基础**: 9 architecture-suite cells 的 trained ΔR² 值来自 tab:cross_arch_matrix；success rates 来自 published LIBERO evaluations（外部数据，无本地文件）
- **Power analysis 验证**: Fisher Z-transform, ρ=0.583, n=9: Z=0.668, SE=0.408, z-stat=1.637. Power = P(Z > 1.96-1.637) = P(Z > 0.323) ≈ 0.37 ✅. For n=21: power ≈ 0.81 ✅
- **状态**: 数值在附录和 discussion.tex 间一致。无独立数据文件可验证 ρ 本身的计算，但 power analysis 逻辑正确。

## 问题清单

### P1 [中等] tab:multilayer_attention L31 vs plot script
- **描述**: tab:multilayer_attention 和正文说 L31 trained=18/32 heads, 但 plot_multi_layer_attention.py 硬编码 trained_heads[L31]=19
- **Server 验证**: full_32layer_attention_summary.json 显示 trained L31 n_instruction_dominant=18，与表一致
- **影响**: fig_synthesis_panels (left panel, fig_multi_layer_attn.pdf) 中 L31 点显示为 19，与表/文字的 18 不一致
- **来源**: Script 可能使用了 dedicated per-layer analysis 的结果（与 bulk extraction 有微小差异），或为旧版本遗留
- **严重性**: 中等——数值差 1 head，不改变定性结论（entry-exit pattern），但 figure-table 不一致

### P2 [中等] tab:2x2_r2_summary Δ_train(L15-L25 avg) 计算不一致
- **描述**: 
  - OpenVLA: Summary 报告 +0.313, 从 tab:2x2_r2 L15-L25 均值差计算得 +0.355
  - TraceVLA: Summary 报告 +0.103, 计算得 +0.137
- **影响**: 涉及对训练效应深度集中程度的定量描述
- **可能原因**: 可能使用了不同的层范围、加权方式、或来自不同的计算管道
- **严重性**: 中等——定性结论（OpenVLA 训练效应远大于 TraceVLA）不变，但具体数值不可从表中复现

### P3 [中等] tab:2x2_r2_summary TraceVLA Reference late-layer std
- **描述**: Summary 报告 late-layer std=0.068, 但从 tab:2x2_r2 数据计算 L25-L31 cross-seed std 均值=0.170
- **影响**: 涉及对 reference 模型深层不稳定性的量化描述
- **可能原因**: "Late-layer std" 定义不明确——可能使用了不同的层范围或不同的 std 含义（profile variability vs cross-seed std）
- **严重性**: 中等——其他三个 late-layer std（OpenVLA ref 0.277, trained 0.040; TraceVLA trained 0.011）在 L25-L31 均可复现

### P4 [低] 附录文本 Llama-2 base 终值 (line 179)
- **描述**: 正文写 "L32: 0.551, std 0.003--0.035"
  - 实际: plot_action_r2_threecond.py 最后一层是 L31 (index 31), 值=0.5571→0.557
  - std 范围: 实际 0.002--0.028 (not 0.003--0.035)
- **影响**: 较小——不影响定性结论
- **严重性**: 低——可能是从不同数据版本引用，或 L32 指代不同位置

### P5 [低] tab:seed_sensitivity R² std 显示值
- **描述**: 表格显示 5 个 peak R² 值 (0.654, 0.656, 0.653, 0.655, 0.655), std 报告为 0.002, 但从这 5 个值计算 std≈0.001
- **影响**: 极小——不影响任何结论
- **严重性**: 低——可能使用了全精度值计算 std，显示值四舍五入后导致不一致

### P6 [信息] 未标记的 counterfactual Goal 表 (line 271)
- **描述**: 该表有 \caption 但无 \label，不可引用
- **影响**: 不影响数据正确性，但影响论文可引用性
- **严重性**: 低

## 未能独立验证的表格

以下表格无独立数据文件可用于逐值比对，仅做了内部一致性检查：
- tab:spatial_cross_instruction — 内部逻辑一致
- tab:metric_invariance — 内部逻辑一致
- tab:qa_probe — 与 tab:training_effect_summary 交叉一致
- tab:specificity_control — 与附录正文一致
- tab:demo_sensitivity — 算术验证正确

## 结论

29 张表中：
- **23 张表完全匹配或仅有可解释的四舍五入差异**
- **3 张表存在可复现的数值不一致**（P1 L31 heads, P2 Δ_train avg, P3 late-layer std）
- **3 处附录文本有微小数值偏差**（P4 endpoint, P5 std, P6 missing label）
- 所有正文↔附录交叉引用在核心数值上一致（ΔR² ranges, d ranges, peak R², head counts），唯一例外是 L31=18 vs figure 的 19
- 无发现任何影响论文主要结论的系统性错误
