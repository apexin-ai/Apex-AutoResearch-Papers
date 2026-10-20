# OLMo-2-7B s42 Rerun Eval Analysis

**Date**: 2026-05-21
**Server**: westd-29999
**evaluate.py md5**: `17673bf373f00f83ccc41fc1d355a4cd` (37775 bytes)
**Note**: evaluate.py 大小与 C009 reference (37591 bytes) 不同，差 184 bytes。但本次 rerun 内部 10 个 eval 使用同一脚本，结果互相一致。

## Rerun vs Paper 对比表

### MMLU (5-shot)

| Dosage | Paper (%) | Rerun (%) | Correct/Total | Δ (pp) | Status |
|--------|-----------|-----------|---------------|--------|--------|
| d000   | 53.79     | 53.79     | 7553/14042    | 0.00   | ✅ 精确匹配 |
| d005   | 55.89     | 56.14     | 7883/14042    | +0.25  | ✅ <0.5pp |
| d025   | 57.73     | 56.17     | 7888/14042    | **-1.56** | ⚠️ 显著偏低 |
| d050   | 57.44     | 57.25     | 8039/14042    | -0.19  | ✅ <0.5pp |
| d100   | 58.60     | 57.00     | 8004/14042    | **-1.60** | ⚠️ 显著偏低 |

### ARC-Challenge (25-shot)

| Dosage | Paper (%) | Rerun (%) | Correct/Total | Δ (pp) | Status |
|--------|-----------|-----------|---------------|--------|--------|
| d000   | 76.11     | 76.11     | 892/1172      | 0.00   | ✅ 精确匹配 |
| d005   | 76.62     | 76.62     | 898/1172      | 0.00   | ✅ 精确匹配 |
| d025   | 78.16     | 78.16     | 916/1172      | 0.00   | ✅ 精确匹配 |
| d050   | 79.61     | 79.61     | 933/1172      | 0.00   | ✅ 精确匹配 |
| d100   | 80.03     | 80.03     | 938/1172      | 0.00   | ✅ 精确匹配 |

## 关键发现

### 1. d000 MMLU 基线验证通过
d000 MMLU = **53.79%**，与论文值精确匹配。之前 53.79% vs 58.60% 的 discrepancy 中，53.79% 是正确的 d000 值。58.60% 是 d100 的值，不是 d000。

### 2. ARC 全量精确匹配
5 个 dosage 的 ARC 结果与论文值完全一致（0.00pp 偏差），确认 checkpoint 和 evaluate.py 对 ARC 评测无版本差异影响。

### 3. MMLU d025/d100 存在显著偏差
- d025: rerun 56.17% vs paper 57.73%，低 1.56pp
- d100: rerun 57.00% vs paper 58.60%，低 1.60pp

可能原因：
- evaluate.py 版本差异（37775 vs 37591 bytes）可能影响 MMLU 的 mc_suffix 处理（参考 C009/C010 的 mc_suffix 位置差异），但不影响 ARC（不同 prompt format）
- d000/d005/d050 匹配良好而 d025/d100 偏低，说明不是全局系统性偏移，可能与特定 dosage 的 adapter 在不同 mc_suffix 位置下的敏感度有关

### 4. Rerun MMLU 剂量-响应曲线
```
Paper:  d000(53.79) → d005(55.89) → d025(57.73) → d050(57.44) → d100(58.60)
Rerun:  d000(53.79) → d005(56.14) → d025(56.17) → d050(57.25) → d100(57.00)
```
- Paper 曲线：持续上升（d050 有小 dip），d000→d100 增幅 4.81pp
- Rerun 曲线：d005 后 plateau，d050 后轻微回落，d000→d100 增幅 3.21pp
- 两个曲线都显示 contamination 带来明确增益

## 结论

### d000 基线
**验证通过**。d000 MMLU = 53.79% 是正确值，确认原始数据无误。

### MMLU d025/d100 偏差
需要进一步排查 evaluate.py 版本差异的具体影响。建议：用论文原始 evaluate.py（37591 bytes 版本）对 d025 和 d100 重新 eval，确认偏差是否来自脚本版本。当前 rerun 使用的 evaluate.py 为 37775 bytes，比 reference 版本多 184 bytes。

### Pattern 分类
OLMo-2-7B 在 MMLU 和 ARC 上均为 **Benefit** pattern：
- MMLU: d000→d100 增幅 3.21pp (rerun) / 4.81pp (paper)，两者都远超 Immune 阈值
- ARC: d000→d100 增幅 3.92pp，精确匹配
- **无需修改 pattern 分类**