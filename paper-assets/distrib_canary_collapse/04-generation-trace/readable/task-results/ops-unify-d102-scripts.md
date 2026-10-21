# ops unify d102 scripts

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_unify-d102-scripts_20260522T174341_result.json`
- **Structured JSON:** [`eb0e1a6068bc0d02d7f8.json`](../../sessions/eb/eb0e1a6068bc0d02d7f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器 MD5 完全一致：

| 文件 | MD5 |
|------|-----|
| `permutation_granger.py` | `236811e1b16495247fd6b02a3c922eee` |
| `run_5method_analysis_d102.py` | `318853fa69384ada42458177fdb80940` |

---

**汇报：**

1. **run_5method_analysis_d102.py 差异**：仅第 223 行一个注释 `# col0=canary causes col1=downstream`（17855 有，19828 无），**无功能差异**。已删除 17855 的注释使两版一致。

2. **permutation_granger.py 差异**：
   - 17855 旧版（116行/3633B）：仅核心 `permutation_granger_test` 函数
   - 19828 版（355行/12627B）：核心函数 + 扩展 docstring + 额外返回字段 (`f2_size`, `df_resid`, `f2_note`) + 独立 `__main__` 多 seed FDR 分析脚本
   - 核心计算逻辑一致，`f_stat`/`p_value`/`significant` 数值完全相同

3. **选择 19828 为准**：D102 Worker 已在 19828 运行；19828 是功能超集。已用 gzip+base64 传输覆盖 17855。

4. **MD5 验证通过**：两台服务器两个文件 checksum 完全一致。

5. **D102 import 确认**：`run_5method_analysis_d102.py` 第 17 行 `from permutation_granger import permutation_granger_test`，只使用返回 dict 的 `f_stat`、`p_value`、`significant` 字段——两版本在这些字段上行为一致，**D102 分析结果不受影响**。

---
