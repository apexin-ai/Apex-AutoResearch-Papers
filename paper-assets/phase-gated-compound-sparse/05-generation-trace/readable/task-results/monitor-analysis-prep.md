# monitor analysis prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_analysis_prep_20260515T050120_result.json`
- **Structured JSON:** [`4aebc5e9b00870fef6cf.json`](../../sessions/4a/4aebc5e9b00870fef6cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 脚本审查报告：`analyze_n500_unified.py`（740行）

### D064 合规性（median_diff 为主，d_z 为辅）：✅ 符合

- `analyze_condition()` 主输出为 `median_ii_diff` + bootstrap 95% CI + `wilcoxon_p`，无 mean（D054 合规）
- `within_dz_importance` 中 d_z 带 `dz_reliable` 标记，CI 过宽(>0.5)或高稀疏度不对称时标记为不可靠
- LaTeX 输出中不可靠 d_z 带 `$\dagger$` 符号
- rank-biserial r 已添加（D064 补充要求）
- 文件头 docstring 明确标注 "D064: d_z auxiliary with reliability flag"

### D059 合规性（random 对比不报 d_z）：✅ 符合

- **Step 2**（~L305-340）：`within_dz_importance` 仅遍历 `imp_` 前缀的 key，random 不参与 d_z 计算
- **Step 3**（~L343-370）：`rand_comparisons` 只报 `median_diff` + `wilcoxon_p`，无 d_z
- **Step 4**（~L373-400）：`imp_vs_rand` 只报 `median_diff` + `rank_biserial_r` + `wilcoxon_p`，无 d_z
- 注释显式标注 `"D059: no d_z"`
- LaTeX Table 4 标题为 "Random within-sparsity (Wilcoxon + median_diff, no d_z)"

### 排列检验：⚠️ 部分不符

- `permutation_monotonicity_test()`（L193-232）使用 `N_PERM=5000` 次 Monte Carlo 随机排列
- **问题**：4 个稀疏度水平只有 4!=24 种排列，应用穷举排列得到精确 p 值，而非 5000 次随机抽样近似
- 当前实现不算错误（Monte Carlo 收敛到近似值），但精度不如穷举，且计算量反而更大

### 其他检查项：✅ 均符合

| 检查项 | 状态 |
|--------|------|
| `--csv` 输出 | ✅ L604 |
| `--latex` 输出 | ✅ L605 |
| Qwen + DeepSeek 双模型 | ✅ `MODEL_MAP = {"deepseek": "ds", "qwen": "qw"}`，default="all" |
| Bonferroni 校正 | ✅ L410-448，跨所有 p 值统一校正 |
| D063（random 不报 FAIL/PASS） | ✅ random 条件只报数值+显著性 |

### 需修改项

**唯一修改建议**：`permutation_monotonicity_test()`（L193-232）应改为 4!=24 穷举排列：

```python
# L215-220 当前代码（Monte Carlo）:
for _ in range(n_perm):
    perm_vals = rng.permutation(vals)
    perm_stat = float(np.sum(np.diff(perm_vals)))
    if perm_stat >= observed_stat:
        count += 1
p = (count + 1) / (n_perm + 1)

# 应改为穷举:
from itertools import permutations
all_perms = list(permutations(vals))  # 24 种
count = sum(1 for pv in all_perms if np.sum(np.diff(pv)) >= observed_stat)
p = count / len(all_perms)
```

同时 `N_PERM = 5000` 常量和函数签名中的 `n_perm` 参数可以移除（穷举不需要）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "deepseek": "ds",
    "qwen": "qw"
  }
}
```

</details>

---
