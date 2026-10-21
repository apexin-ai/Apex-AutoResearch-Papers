# code script fixes d019 d038

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_script-fixes-d019-d038_20260515T145232_result.json`
- **Structured JSON:** [`e85792d74102f2d5c558.json`](../../sessions/e8/e85792d74102f2d5c558.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

### Task 1: `plot_regime_map.py` 改为程序化读取 JSON — 完成

- 添加 `json`/`os`/`warnings` 导入
- 新增 `load_pfdr_from_json()` 函数，从 `cross_alpha_v6.json` 的 `granger_causality` 列表按 `direction` + `alpha` 提取 `p_fdr`
- JSON 路径搜索：远程路径 → 本地相对路径，均不可用时 fallback 到 `HARDCODED_DATA` 并打印 WARNING
- 服务器验证：JSON 加载的值与原硬编码值完全一致
- 本地语法检查通过；本地无 matplotlib 故不生成 PDF（符合要求）

### Task 2: `analyze_extended.py` 的 `cohen_f2_label` — D019 违规已修复

- **发现违规**：`analyze_extended.py:56` 的 `cohen_f2_label(f2)` 无 `df_resid` 参数，不检查 `df_resid < 20`，直接返回 Cohen 分类
- **调用路径**：line 218 的 TY Granger 结果（plan_006 T=18 分析调用）会触发此函数，而 T=18 时 `df_resid` 极低
- **已修复**：
  - 函数签名改为 `cohen_f2_label(f2, df_resid=None)`
  - 添加 guard：`df_resid is not None and df_resid < 20` → 返回 `"df_too_low"`
  - 调用处改为 `cohen_f2_label(f2, df_resid=df_resid)`
- 与 `analyze_alpha_sweep.py` 的 `_f2_label` 和 `permutation_granger.py` 的 guard 逻辑一致

---
