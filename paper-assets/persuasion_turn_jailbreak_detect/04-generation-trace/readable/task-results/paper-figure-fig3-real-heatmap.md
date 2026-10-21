# paper figure fig3 real heatmap

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig3_real_heatmap_20260518T040215_result.json`
- **Structured JSON:** [`49a631fa03cba76c3e9e.json`](../../sessions/49/49a631fa03cba76c3e9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报如下：

---

## 执行结果

### 1. 真实数据的稀疏模式

三种攻击类型的转移矩阵稀疏程度差异极大：

| 攻击类型 | 非零 cell | 稀疏率 | 总转移次数 | 最大值 | 使用策略数 |
|----------|----------|--------|-----------|--------|-----------|
| **Crescendo** | 29/81 | 35.8% | 1818 | 545 | 8/9 |
| **FITD** | 6/81 | 7.4% | 541 | 161 | 4/9 |
| **Deceptive Delight** | 8/81 | 9.9% | 565 | 129 | 6/9 |

**Crescendo** 策略多样性最高，使用了 8 种策略，转移路径分散。主导模式是 `role_assignment→role_assignment`（545 次，占 30%），`obfuscation→obfuscation`（173 次）也很突出，表现为后期策略锁定。

**FITD** 极度稀疏，仅使用 4 种策略（none/rapport/emotion/role），形成一条近乎线性的路径：`none→role_assignment→rapport_building→emotional_manipulation→role_assignment`（循环），`role_assignment` 自环 161 次。

**Deceptive Delight** 使用 6 种策略但转移集中在少数路径：`emotional_manipulation→role_assignment`（129）是最强跨策略转移，`none→gradual_escalation→emotional_manipulation` 形成固定开局序列。

### 2. 图的视觉效果

- 300 DPI，4026x1330px，适合双栏论文格式
- 使用 `SymLogNorm` 处理极端值（role→role=545 vs 大量 20-80 的值），保持视觉可辨识性
- YlOrRd colormap，0 值显示为白色/极浅色，稀疏性一目了然
- 每个 cell 标注实际数值，审稿人可直接验证
- 每个子图标注总转移次数

### 3. 与伪造数据的主要差异

真实数据的核心特征是**高度稀疏**和**策略锁定**：
- FITD 和 DD 仅激活 4-6 种策略（而非 9 种全覆盖），大量 cell 为零
- 自环（同策略持续）在所有攻击中占主导地位，尤其是 `role_assignment` 自环
- Crescendo 相对丰富，但仍然有明显的稀疏区域（`direct_request` 完全未使用）
- 这种模式反映了真实攻击的结构性特征：每种攻击有固定的策略序列模板，而非随机组合

### 产出文件

- 远程：`src/plot_strategy_heatmap.py`（脚本）、`results/fig3_strategy_heatmap.pdf`、`results/fig3_strategy_heatmap.png`
- Artifact 已注册：`fig3_strategy_heatmap_pdf`、`fig3_strategy_heatmap_png`、`plot_strategy_heatmap_script`

---
