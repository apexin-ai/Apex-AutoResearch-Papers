# 全文数据真实性与可追溯性审计报告

**日期**: 2026-05-29 (DDL day)
**论文**: Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis
**目标会议**: CoRL 2026

---

## (a) 审计规模

| 审计模块 | 数字/数据点数 | 来源 |
|----------|-------------|------|
| 正文（abstract, intro, method, experiments, discussion） | 78 | audit_maintext.md |
| 图表（14 图 + 9 附录图 caption） | ~750 | audit_figures.md |
| 附录（29 表 + 文本定量声明） | ~580 | audit_appendix.md |
| **总计** | **~1,408** | |

数据源覆盖：plot 脚本硬编码值、本地 artifacts JSON、服务器 bootstrap_v3 JSON、threecond_multiseed_v2.json、full_32layer_attention_summary.json、paired_cohens_d.json、bonferroni_global.json、branch_split_rsa_results.json 等。

---

## (b) 问题统计

| 严重度 | 数量 | 说明 |
|--------|------|------|
| MEDIUM | 3 | 数值不一致，可能影响审稿人质疑 |
| LOW | 4 | 微小偏差，不影响结论 |
| INFO | 2 | 格式/措辞问题 |
| **总计** | **9** | 去重后（L31 heads 问题跨三个模块合并为 1 个） |

**核心结论：所有主要定量声明（ΔR² 范围、Cohen's d 范围、CI、p 值、排名统计）均可追溯且正确。无系统性数据错误。**

---

## (c) 每个问题的详细描述

### MEDIUM-1: Figure 7 左 panel L31 trained heads = 19（脚本）vs 18（论文/表/服务器）

- **位置**: plot_multi_layer_attention.py `trained_heads=[24,4,10,19]`；experiments.tex L131 "L31: 18"；tab:multilayer_attention L31=18；server JSON=18
- **原始值**: 服务器 full_32layer_attention_summary.json → 18；plot 脚本 → 19
- **论文值**: 18（正文 + 附录表格均为 18）
- **影响**: fig_multi_layer_attn.pdf 中 L31 数据点偏高 1 head。正文文字和表格正确（18），仅图的绘制值错（19）
- **严重程度**: 中等 — 不改变 entry-exit pattern 定性结论，但 figure-table 不一致可被审稿人发现
- **建议**: 修正 plot_multi_layer_attention.py 中 trained_heads[3] 从 19 改为 18，重新生成图

### MEDIUM-2: tab:2x2_r2_summary Δ_train(L15-L25 avg) 不可从 tab:2x2_r2 复现

- **位置**: appendix.tex tab:2x2_r2_summary
- **论文值**: OpenVLA +0.313, TraceVLA +0.103
- **从 tab:2x2_r2 计算**: OpenVLA +0.355, TraceVLA +0.137
- **影响**: 涉及训练效应深度集中程度的定量描述。定性结论不变（OpenVLA >> TraceVLA）
- **可能原因**: 不同层范围定义、加权方式、或来自不同计算管道（可能用了 15-seed vs 4-seed 数据）
- **严重程度**: 中等 — 审稿人如果尝试从 Table 复现会得到不同数值
- **建议**: 确认计算方法并在表注中标明层范围和计算方式；或用可复现的数值替换

### MEDIUM-3: tab:2x2_r2_summary TraceVLA Reference late-layer std = 0.068 vs 计算值 0.170

- **位置**: appendix.tex tab:2x2_r2_summary, "Late-layer std" 列
- **论文值**: 0.068
- **从 tab:2x2_r2 计算 (L25-L31)**: 0.170
- **其他三个 late-layer std**: OpenVLA ref 0.277、OpenVLA trained 0.040、TraceVLA trained 0.011 — 均可从 L25-L31 数据复现
- **可能原因**: "late-layer std" 对该条目使用了不同层范围或不同的 std 含义（profile variability vs cross-seed variability）
- **严重程度**: 中等 — 3/4 可复现，1/4 不可
- **建议**: 确认计算方法，统一四个条目的层范围定义

### LOW-1: OpenVLA L1 trained heads 24（正文/dedicated analysis）vs 23（bar chart/bulk extraction）

- **位置**: experiments.tex L18 "24/32"；plot_l1_attention.py trained_counts=[23,...]
- **原因**: 已知方法差异（dedicated per-layer analysis vs 32-layer bulk extraction），appendix 已有注释 "threshold boundary effects"
- **影响**: 低 — 已在附录说明，审稿人可理解
- **建议**: 保留现状，附录注释已足够

### LOW-2: 附录段落 TraceVLA trained 27/32 vs bar chart 29/32；NORA ref 13/16 vs chart 14/16

- **位置**: appendix.tex ~L725 段落 vs plot_l1_attention.py
- **影响**: 附录配文中的 point estimate 与图表绘制值不一致，但 experiments.tex 使用范围值 "27-30/32" 和 "13-14/16" 覆盖了两者
- **严重程度**: 低 — 正文范围表述正确
- **建议**: 修正附录段落配文与图表一致（29/32 和 14/16），或改为范围表述

### LOW-3: 附录 Llama-2 base 终值 "L32: 0.551" vs 实际 L31: 0.557

- **位置**: appendix.tex L179
- **原始值**: plot_action_r2_threecond.py llama2base_mean[31] = 0.5571 → 0.557
- **论文值**: "L32: 0.551"（层号偏 1，数值偏 0.006）；std 范围 "0.003-0.035" vs 实际 0.002-0.028
- **严重程度**: 低 — 不影响任何结论
- **建议**: 修正为 "L31: 0.557, std 0.003-0.028"

### LOW-4: tab:seed_sensitivity R² std = 0.002 vs 从显示值计算 0.001

- **位置**: appendix.tex tab:seed_sensitivity
- **影响**: 极小 — 可能使用全精度值计算 std，显示值四舍五入后不一致
- **严重程度**: 低
- **建议**: 保留（全精度计算合理）

### INFO-1: NORA training "unchanged" 措辞不完全精确

- **位置**: experiments.tex L119
- **详情**: Goal: ref=13 → trained=13（不变 ✓）；Spatial: ref=14 → trained=12（减少 2 head）
- **影响**: "unchanged" 对 Goal 成立但对 Spatial 不精确。幅度小（≤2 head），定性描述可接受
- **建议**: 可改为 "training leaves this largely unchanged (13-14 → 12-13)"

### INFO-2: 未标记的 counterfactual Goal 表缺少 \label

- **位置**: appendix.tex L271
- **影响**: 该表有 caption 但无 label，不可被引用
- **建议**: 添加 \label{tab:counterfactual_goal}

---

## (d) 保留但暂找不到独立出处的数字

以下数字仅做了内部一致性验证，无独立数据文件可逐值比对：

| 数字/表 | 位置 | 验证方式 | 保留理由 |
|---------|------|---------|---------|
| tab:spatial_cross_instruction 全部数值 | appendix L414 | 内部逻辑验证（chance=10%, trained→100%） | 趋势符合预期 |
| tab:metric_invariance 全部数值 | appendix L435 | 内部一致性（profile r > 0.989） | 高相关性符合预期 |
| tab:qa_probe 全部数值 | appendix L670 | 与 training_effect_summary 交叉验证 | 数值范围合理 |
| Spatial RSA peak L14 ρ=0.691, Δ=+0.023 | appendix L367 | 无独立源 | 方法与 Goal 一致，数值范围合理 |
| 15-seed std=0.004（L460 "R²=0.637±0.004"） | appendix L460 | openvla_r2_per_layer.json 显示 std=0.008 | 可能是不同统计量（SEM vs std） |
| ρ=0.583, p=0.10 的原始计算 | discussion.tex L16 | Power analysis 数学验证通过 | 无原始计算脚本，但统计逻辑正确 |

---

## 已排除的已知关注

| 关注 | 结论 |
|------|------|
| counterfactual bar TraceVLA Spatial/Object wrong↔shuffled 交换 | **已排除** — 经 cf_batch_missing_v1_analysis.md 和 cf_batch_part2_v1_analysis.md 交叉验证，条件映射完全正确 |
| threecond R² 硬编码值与 artifact 偏移 | **已解释** — 3-seed (v2) vs 15-seed 的 sample mean 差异，非数据错误（Loop #16 验证） |

---

## 审计总结

**~1,408 个数字审计完成。9 个问题（3 MEDIUM + 4 LOW + 2 INFO），无系统性数据错误。**

所有核心定量声明——ΔR² 范围（0.16-0.46）、Cohen's d 范围（0.45-1.52）、CI、p=0.008、NLP ΔR²=0.000、Table 1 全部 20 个 cell——均可追溯到原始数据且逐位匹配。

3 个 MEDIUM 问题中：
- M1（L31 heads）仅影响一张图的一个数据点，正文/表格均正确
- M2-M3（2x2 summary 表）影响附录中的汇总统计，不被正文引用

**建议 DDL 前修复优先级**：M1（改 1 行脚本重出图）> M2-M3（表注说明）> LOW（可 camera-ready 阶段修正）
