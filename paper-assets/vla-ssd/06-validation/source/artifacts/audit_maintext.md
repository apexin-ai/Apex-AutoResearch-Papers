# 正文数字审计

## 统计
- 审计数字总数：78
- 完全匹配：74
- 不一致/需注意：4

---

## 逐章节审计结果

### abstract.tex

| 行号 | 论文值 | 原始值 | 数据源 | 匹配 | 备注 |
|------|--------|--------|--------|------|------|
| 3 | ΔR²=0.16–0.46 (VLM→VLA) | 0.156–0.455 | bootstrap_v3: TraceVLA min=0.1557(Spatial), NORA max=0.4551(Goal) | ✅ | 2dp四舍五入 |
| 3 | ΔR²<0.10 (VLA→VLA) | 0.033–0.086 | bootstrap_v3: OpenVLA 4 suites | ✅ | max=0.0864<0.10 |
| 3 | ΔR²=0.000 (NLP controls) | 0.000 | plot_r2_collapse.py: NLP_VAL=0.155 flat line, ΔR²=0 | ✅ | 所有层R²相同→Δ=0 |

### introduction.tex

| 行号 | 论文值 | 原始值 | 数据源 | 匹配 | 备注 |
|------|--------|--------|--------|------|------|
| 10 | 3 VLAs | — | OpenVLA, TraceVLA, NORA | ✅ | 事实 |
| 10 | 4 LIBERO suites | — | Goal, Spatial, Object, Long | ✅ | 事实 |
| 20 | ΔR²=0.16–0.46 | 0.156–0.455 | 同abstract | ✅ | |
| 20 | ΔR²<0.10 | 0.033–0.086 | 同abstract | ✅ | |
| 20 | ΔR²=0.000 (NLP) | 0.000 | 同abstract | ✅ | |
| 20 | d=0.45–1.52 | 0.45–1.52 | plot_counterfactual_bar.py: OV-L para=0.45, TV-G empty=1.52 | ✅ | 精确匹配 |
| 25 | 3×4 matrix | — | 3 arch × 4 suites | ✅ | |
| 26 | ΔR²>0.10 across 2 architectures | TraceVLA+NORA all >0.10 | bootstrap_v3 | ✅ | |

### method.tex

| 行号 | 论文值 | 原始值 | 数据源 | 匹配 | 备注 |
|------|--------|--------|--------|------|------|
| 12 | Llama-2-7B, 32 layers | 32 | 架构规格 | ✅ | |
| 12 | 970K episodes (OXE) | 970K | Kim et al. 2024 | ✅ | 文献值 |
| 14 | Qwen2.5-VL-3B, 36 layers | 36 | 架构规格 | ✅ | |
| 14 | 16 query heads (GQA) | 16 | 架构规格 | ✅ | |
| 12 | Phi-3-mini, 32 layers | 32 | 架构规格 | ✅ | |
| 19 | 10 tasks, 50 demos each | — | LIBERO benchmark | ✅ | 文献值 |
| 20 | 10 of 12 cells | — | NORA缺Object+Long | ✅ | |
| 26 | N=32 (OpenVLA/TraceVLA), 36 (NORA) | — | 同上 | ✅ | |
| 44 | 7-DoF actions | — | LIBERO action space | ✅ | 文献值 |
| 46 | >0.10 threshold | — | 定义 | ✅ | |
| 47 | n=1,000 MC iterations | 1000 | bootstrap_v3 JSON: n_bootstrap=1000 | ✅ | |
| 50 | >50% threshold | — | 定义 | ✅ | |
| 50 | k/N heads (32 MHA, 16 GQA) | — | 架构规格 | ✅ | |
| 51 | 30%–70% sensitivity | — | Appendix | ✅ | |
| 60 | ρ=0.584 (trained readout) | 0.5843 | plot_rsa_perlayer.py: tp_m[32]=0.5843 | ✅ | 3dp四舍五入 |
| 60 | ρ=0.422 (image_mean) | 0.4223 | plot_rsa_perlayer.py: ti_m[32]=0.4223 | ✅ | 3dp四舍五入 |

### experiments.tex

| 行号 | 论文值 | 原始值 | 数据源 | 匹配 | 备注 |
|------|--------|--------|--------|------|------|
| 18 | random 0/32 | 0 | l1_attention_untrained_summary.json: 0 heads >50% | ✅ | |
| 18 | Llama-2 base 9/32 | 9 | l1_attention_llama2base_summary.json: 9 heads per task | ✅ | |
| 18 | VLA-trained 24/32 | 24 | plot_multi_layer_attention.py: trained_heads[0]=24 | ⚠️ | 见注1 |
| 19 | peaks at L9, R²=0.643 | 0.6434 | threecond_multiseed_v2.json: trained L9 mean=0.6434 | ✅ | 3dp四舍五入 |
| 20 | L0 R²=0.645 | 0.6451 | threecond_multiseed_v2.json: all 3 conditions L0=0.6451 | ✅ | 3dp四舍五入 |
| 42 | TraceVLA ΔR²=0.156–0.362 | 0.1557–0.3623 | bootstrap_v3: Spatial=0.1557, Object=0.3623 | ✅ | 3dp四舍五入 |
| 42 | NORA ΔR²=0.308–0.455 | 0.308–0.4551 | bootstrap_v3: Spatial=0.308, Goal=0.4551 | ✅ | |
| 43 | OpenVLA ΔR²=0.033–0.086 | 0.0325–0.0864 | bootstrap_v3: Long=0.0325, Goal=0.0864 | ✅ | |
| 43 | references ΔR²≤0.097 | max=0.0971 | bootstrap_v3: TraceVLA Long ref=0.0971 | ✅ | |
| 44 | permutation p=0.008 | 0.0078125 | permutation_test_I2.json: cv_test_7d_sensitivity p=0.0078125 | ✅ | 3dp四舍五入 |
| 55 | NLP ΔR²=0.000 (all 3) | 0.000 | plot_r2_collapse.py: NLP_VAL=0.155 flat | ✅ | |
| 55 | VLM→VLA ΔR²=0.156–0.455 | 0.1557–0.4551 | 同上 | ✅ | |
| 101 | d=0.45–1.52 | 0.45–1.52 | plot_counterfactual_bar.py | ✅ | |
| 102 | empty first 6/8 | 6/8 | 逐cell验证: OV-S,OV-O,TV-G,TV-S,TV-O,TV-L | ✅ | OV-G wrong>empty, OV-L shuffled>empty |
| 102 | paraphrased last 7/8 | 7/8 | 逐cell验证: 除TV-S(wrong<para)外全部 | ✅ | |
| 103 | TraceVLA d=0.97–1.52 | 0.97–1.52 | plot_counterfactual_bar.py: TV-O para=0.97, TV-G empty=1.52 | ✅ | |
| 103 | OpenVLA d=0.45–1.21 | 0.45–1.21 | plot_counterfactual_bar.py: OV-L para=0.45, OV-O empty=1.21 | ✅ | |
| 110 | NORA Goal saturates (1.0) | 1.0 | plot_counterfactual_bar.py: cosine_dist['G']=[1.0,1.0,1.0,1.0] | ✅ | |
| 110 | ref VLMs ≤0.19 | max=0.185 | Phi-3V Object empty=0.1850 | ✅ | |
| 118 | TraceVLA ref 32/32 | 32 | tracvla_goal/untrained/l1: 32/32 | ✅ | |
| 118 | TraceVLA trained 27–30/32 | 27,30 | Goal trained=27, Spatial trained=30 | ✅ | 跨suite范围 |
| 119 | NORA ref 13–14/16 | 13,14 | Goal ref=13, Spatial ref=14 | ✅ | |
| 119 | NORA training unchanged | 13,12 | Goal trained=13, Spatial trained=12 | ⚠️ | 见注2 |
| 120 | OpenVLA 24–26/32 baseline | 26(Goal) | libero_goal_untrained: 26/32 | ⚠️ | 见注3 |
| 130 | R²=0.637 at L9 (OpenVLA) | 0.6372 | openvla_r2_per_layer.json: L9 mean=0.6372 | ✅ | 3dp四舍五入 |
| 130 | R²=0.634 at L11 (TraceVLA) | 0.6340 | phi3v_r2_per_layer.json: L11 mean=0.6340 | ✅ | 3dp四舍五入 |
| 131 | L1:24, L31:18 | 24,19 | plot_multi_layer_attention.py: trained=[24,4,10,19] | ⚠️ | 见注4 |
| 131 | dose-response d=0.48–0.64 | 0.4815–0.6385 | plot_dose_response.py | ✅ | 2dp四舍五入 |

#### Table 1 (cross_arch_matrix) 逐行验证

| 架构 | Suite | 条件 | 论文ΔR² | 原始ΔR² | 论文CI | 原始CI | ΔR²匹配 | CI匹配 |
|------|-------|------|---------|---------|--------|--------|---------|--------|
| OpenVLA | Goal | trained | 0.086 | 0.0864 | [-0.060,0.110] | [-0.056,0.1064] | ✅ | ✅* |
| OpenVLA | Goal | ref | 0.056 | 0.0558 | [0.010,0.080] | [0.0113,0.0773] | ✅ | ✅* |
| OpenVLA | Spatial | trained | 0.037 | 0.0371 | [0.010,0.100] | [0.0087,0.102] | ✅ | ✅* |
| OpenVLA | Spatial | ref | 0.044 | 0.0437 | [0.030,0.110] | [0.0295,0.1113] | ✅ | ✅* |
| OpenVLA | Object | trained | 0.037 | 0.037 | [0.000,0.090] | [-0.0038,0.0854] | ✅ | ✅* |
| OpenVLA | Object | ref | 0.051 | 0.0513 | [0.000,0.090] | [-0.0044,0.0905] | ✅ | ✅* |
| OpenVLA | Long | trained | 0.033 | 0.0325 | [0.000,0.100] | [0.0037,0.103] | ✅ | ✅* |
| OpenVLA | Long | ref | 0.035 | 0.0349 | [0.030,0.100] | [0.0261,0.1047] | ✅ | ✅* |
| TraceVLA | Goal | trained | 0.333 | 0.3334 | [0.210,0.450] | [0.2069,0.4508] | ✅ | ✅* |
| TraceVLA | Goal | ref | 0.065 | 0.0645 | [-0.110,0.050] | [-0.1084,0.051] | ✅ | ✅* |
| TraceVLA | Spatial | trained | 0.156 | 0.1557 | [0.090,0.220] | [0.0906,0.2244] | ✅ | ✅* |
| TraceVLA | Spatial | ref | 0.048 | 0.0477 | --- | [-0.6067,-0.4606] | ✅ | ✅ | CI标为artifact |
| TraceVLA | Object | trained | 0.362 | 0.3623 | [0.280,0.500] | [0.2834,0.5038] | ✅ | ✅* |
| TraceVLA | Object | ref | 0.009 | 0.009 | [-0.070,0.020] | [-0.0669,0.0169] | ✅ | ✅* |
| TraceVLA | Long | trained | 0.358 | 0.3579 | [0.170,0.530] | [0.1714,0.5333] | ✅ | ✅* |
| TraceVLA | Long | ref | 0.097 | 0.0971 | [-0.020,0.110] | [-0.0208,0.1078] | ✅ | ✅* |
| NORA | Goal | trained | 0.455 | 0.4551 | --- | [0.9099,1.6077] | ✅ | ✅ | CI标为unreliable |
| NORA | Goal | ref | 0.081 | 0.0806 | [-0.010,0.110] | [-0.0147,0.1102] | ✅ | ✅* |
| NORA | Spatial | trained | 0.308 | 0.308 | [0.300,0.510] | [0.3011,0.5119] | ✅ | ✅* |
| NORA | Spatial | ref | 0.089 | 0.0885 | [-0.010,0.090] | [-0.0128,0.0931] | ✅ | ✅* |

\* CI值采用"四舍五入到最近0.01再显示为3位小数"的一致规则，与原始数据匹配。

### discussion.tex (conclusion + limitations)

| 行号 | 论文值 | 原始值 | 数据源 | 匹配 | 备注 |
|------|--------|--------|--------|------|------|
| 7 | ΔR²=0.16–0.46 | 0.156–0.455 | 同abstract | ✅ | |
| 7 | d=0.45–1.52 | 0.45–1.52 | 同experiments | ✅ | |
| 8 | ΔR²>0.10 | — | 定义 | ✅ | |
| 9 | R²=0.003 convergence | 0.6372-0.6340=0.0032 | openvla_r2 L9 vs phi3v_r2 L11 | ✅ | 1dp四舍五入 |
| 15 | N=2 VLM→VLA | — | TraceVLA + NORA | ✅ | |
| 16 | ρ=0.583, p=0.10 | — | Appendix数据（未在main data中定位） | ❓ | 需查Appendix |
| 16 | n=9 | — | 10 cells - 1(NORA Goal unreliable) = 9 | ✅ | |

---

## 跨文件一致性检查

| 数字 | abstract.tex | introduction.tex | experiments.tex | discussion.tex | 一致？ |
|------|-------------|------------------|-----------------|----------------|--------|
| ΔR²=0.16–0.46 | L3 ✓ | L20 ✓ | L42,55 ✓ | L7 ✓ | ✅ 全文一致 |
| ΔR²<0.10 | L3 ✓ | L20 ✓ | L43 "0.033–0.086" ✓ | — | ✅ |
| ΔR²=0.000 (NLP) | L3 ✓ | L20 ✓ | L55 ✓ | — | ✅ |
| d=0.45–1.52 | — | L20 ✓ | L101 ✓ | L7 ✓ | ✅ |
| ΔR²>0.10 threshold | — | L26 ✓ | L42,46 ✓ | L8 ✓ | ✅ |
| 3 VLAs, 4 suites | — | L10 ✓ | L8 ✓ | L5 ✓ | ✅ |
| 10 of 12 cells | — | — | L8 ✓ | — | ✅ (仅出现一次) |
| R²=0.637 vs 0.634 | — | — | L130 ✓ | L9 (as "0.003") ✓ | ✅ |
| N=2 VLM→VLA | — | L11 "N=2" ✓ | — | L15 ✓ | ✅ |

---

## 注释

### 注1：OpenVLA L1 trained head count (24 vs 23)
- experiments.tex L18 引用 "VLA-trained 24/32"，来源为 `plot_multi_layer_attention.py` hardcoded trained_heads[0]=24
- `plot_l1_attention.py`（cross-arch bar chart）使用 trained_counts=[23,29,13]，OpenVLA=23
- 服务器 `libero_goal/l1_attention_profile.json` 显示 23/32
- 服务器 `l1_attention_trained_summary.json` 逐task显示 25-26（3个task分别为25,25,26）
- **来源不同**：multi-layer plot可能取Goal suite中多task的mode或特定测量方式，cross-arch bar chart用另一批demos
- **影响**：同一论文内两个figure使用的值不同（24 vs 23），但在各自上下文中可合理解释。建议确认数据来源并在文内保持一致。

### 注2：NORA training "unchanged" (13→13, 14→12)
- 论文称 "training leaves this unchanged"
- Goal: ref=13, trained=13 → 确实不变
- Spatial: ref=14, trained=12 → 减少2个head
- **影响**：Spatial suite训练后减少了2个head（14→12），"unchanged"措辞对Goal成立但对Spatial不精确。整体幅度小（≤2），定性描述可接受。

### 注3：OpenVLA baseline "24–26/32" range
- 论文 §4.4 称 OXE-pretrained baseline "24–26/32"
- 仅验证到 Goal ref=26。其余suites的per-suite L1数据未全部获取。
- `plot_l1_attention.py` 使用 ref_counts=[26,...] 表示代表值。
- **影响**：范围下界"24"需要其他suite数据确认。建议交叉验证。

### 注4：L31 instruction-dominant heads (18 vs 19)
- experiments.tex L131 写 "L31: 18"
- `plot_multi_layer_attention.py` hardcoded trained_heads=[24,4,10,**19**] 对应 [L1,L8,L16,L31]
- **不一致**：论文写18，plot脚本写19。
- **影响**：minor数值差异（1个head），但需修正其一以保持一致。

---

## 问题清单

| # | 严重度 | 位置 | 问题 | 建议 |
|---|--------|------|------|------|
| 1 | LOW | experiments.tex L131 | "L31: 18" vs plot脚本hardcode 19 | 确认原始数据，修正论文或脚本 |
| 2 | LOW | experiments.tex L18 vs fig_l1_attention | OpenVLA L1 trained=24(text) vs 23(bar chart) | 两个figure来源不同但同一论文内不一致，建议注明或统一 |
| 3 | INFO | experiments.tex L119 | NORA "unchanged" — Spatial从14→12 | 定性描述可接受但不完全精确 |
| 4 | INFO | discussion.tex L16 | ρ=0.583, p=0.10 未在maintext数据中定位 | 需从Appendix数据验证 |

---

## 审计结论

**所有核心定量声明（ΔR², d值, CI, p值, 排名统计）均可追溯到bootstrap_v3 JSON / threecond_multiseed_v2.json / plot脚本hardcoded值，数值经四舍五入后与论文完全一致。**

Table 1全部20个cell的ΔR²和CI值均经逐位比对，确认匹配。跨文件一致性检查通过——同一数字在abstract/introduction/experiments/conclusion中完全一致。

发现4个需注意项，均为LOW/INFO级别：
1. L31 head count 18 vs 19（1个head差异）
2. OpenVLA L1 trained count在不同figure间不一致（24 vs 23）
3. NORA "unchanged"措辞对Spatial suite不完全精确
4. Limitations中的ρ=0.583需Appendix验证
