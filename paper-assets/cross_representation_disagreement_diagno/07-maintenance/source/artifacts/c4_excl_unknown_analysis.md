# C4 Excl. Unknown FAIL 根因分析

## 数据概览

| 模式 | N | Targeted | Blind | Delta | 判定 |
|------|---|----------|-------|-------|------|
| All | 47 | 30 (63.8%) | 24 (51.1%) | +12.8pp | PASS |
| Excl. Unknown | 29 | 18 (62.1%) | 16 (55.2%) | +6.9pp | 边缘 |
| GT=Unknown only | 18 | 12 (66.7%) | 8 (44.4%) | +22.2pp | — |

排除 GT=Unknown 后 delta 从 12.8pp 降至 6.9pp，因为 GT=Unknown 是 targeted 优势最大的子集。

## 根因：FOL targeted repair 反效果

### 按 repair_type 分解（Excl. Unknown）

| repair_type | N | Targeted | Blind | Delta |
|-------------|---|----------|-------|-------|
| code | 22 | 17 (77.3%) | 13 (59.1%) | **+18.2pp** |
| fol | 7 | 1 (14.3%) | 3 (42.9%) | **-28.6pp** |

**Code targeted repair 表现优秀（+18.2pp）**，但 **FOL targeted repair 严重拖后腿（-28.6pp）**。

### 4-way 交叉表（Excl. Unknown）

| | code (N=22) | fol (N=7) |
|--|-------------|-----------|
| Both correct | 13 | 0 |
| Only targeted correct | 4 | 1 |
| Only blind correct | **0** | **3** |
| Both wrong | 5 | 3 |

Code 修复中 blind 从未独立胜出（0 cases）。FOL 修复中 blind 在 3/7 cases 独立胜出，targeted 几乎完全失败。

### 核心缺陷：FOL targeted repair 锚定原始答案

| 指标 | FOL repair | Code repair |
|------|-----------|-------------|
| Stuck on original verdict | **60%** (6/10) | 11% (4/37) |
| Changed verdict | 40% | 89% |

当 FOL_orig=Unknown 且 GT≠Unknown（5 cases），targeted 有 **80% 保持 Unknown 不变**。诊断信息反而锚定模型，使其仅做最小修改而非结构性重写。

### 按 error_side 分解（Excl. Unknown）

| error_side | N | Targeted | Blind | Delta |
|------------|---|----------|-------|-------|
| code | 19 | 17 (89.5%) | 13 (68.4%) | +21.1pp |
| fol | 4 | 1 (25.0%) | 3 (75.0%) | -50.0pp |
| both | 6 | 0 (0%) | 0 (0%) | 0.0pp |

error_side=both 完全无法修复（0/6），两种表征都错时缺乏可靠参照。

## 为什么 GT=Unknown 有利于 targeted？

Blind repair 在 GT=Unknown 上仅 44.4% 正确（8/18），因为 blind 倾向于给出确定性答案（True/False），而非 Unknown：
- Blind 在 GT=Unknown 上的输出分布：Unknown=8, False=6, True=4

Targeted repair 在 GT=Unknown 上 66.7% 正确（12/18），诊断上下文使模型更保守，巧合地有利于 Unknown 判断。

## 按 GT label 分解

| GT | N | Targeted | Blind | Delta |
|----|---|----------|-------|-------|
| True | 11 | 5 (45.5%) | 5 (45.5%) | **0.0pp** |
| False | 18 | 13 (72.2%) | 11 (61.1%) | +11.1pp |
| Unknown | 18 | 12 (66.7%) | 8 (44.4%) | +22.2pp |

GT=True delta=0 的原因：code 修复在 GT=True 上 targeted 仍优于 blind，但 FOL 修复在 GT=True 上 targeted 0/3、blind 2/3，完全抵消。

## 诊断结论

### 这是 pipeline 问题还是方法论限制？

**两者兼有：**

1. **Pipeline 问题（可修复）— FOL targeted prompt 设计缺陷**
   - FOL targeted repair prompt 导致模型锚定原始 formalization，仅做 patch 而非 rewrite
   - 修复方向：prompt 应明确指示"以诊断为线索从头重写 formalization，不要在原始代码上做最小修改"
   - 预期效果：若 FOL targeted 从 14.3% 提升到 ≥42.9%（blind 水平），整体 delta 可恢复到 >10pp

2. **方法论限制（需讨论）— error_side=both 不可修复**
   - 两种表征都错时，cross-representation disagreement 本身缺乏可靠参照
   - Excl. Unknown 中有 6/29 = 20.7% 的 repair units 属于此类
   - 论文中应承认：方法前提是至少一种表征正确

## 改进建议

### 高优先级
1. **重写 FOL targeted repair prompt**：
   - 当前问题：诊断信息包含原始 FOL 代码 → 模型倾向于最小 patch
   - 改进：只提供诊断结论（"FOL 输出 Unknown 但 GT 可能是 True/False"），不附带原始代码，或明确指示 rewrite-from-scratch
   - 可额外提示："Unknown 通常意味着约束不够强，考虑是否遗漏了关键前提的形式化"

2. **分离 C4 报告**：
   - 主报告按 repair_type 分别报告 C4：code repair（核心贡献）和 FOL repair（已知局限）
   - 总体 C4 作为补充指标

### 中优先级
3. **error_side=both 的处理策略**：
   - 当诊断为 both-error 时，考虑多轮迭代修复（先修一侧，再用修复结果做参照修另一侧）
   - 或在 C4 计算中排除 both-error 样本，因为它们不满足方法的基本假设

4. **GT=True 样本的 code 修复**：
   - Code_orig 多为 Unknown/False，repair 需要将其改为 True
   - 当前 targeted 在 GT=True 上仅 5/8（code only），有提升空间
   - 检查 targeted prompt 是否在 code 侧有类似的保守偏见
