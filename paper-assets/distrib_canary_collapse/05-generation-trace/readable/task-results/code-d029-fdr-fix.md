# code d029 fdr fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d029_fdr_fix_20260515T091148_result.json`
- **Structured JSON:** [`764062baaac849aab249.json`](../../sessions/76/764062baaac849aab249.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。总结：

### 修改内容

**consensus_framework.py** (`load_sig_matrix()`):
- 新增 `apply_fdr=True` 参数
- `apply_fdr=True` 时读 `significant_fdr`（FDR-corrected），无该字段时 fallback 到 `significant`（覆盖 threshold_onset 无 p_raw 的情况）

**cross_alpha_analysis_v4.py** (`run_consensus_per_alpha()`):
- α=1.0 路径：显式传 `apply_fdr=True` 给 `load_sig_matrix()`
- 单 seed α 路径：收集各 method 的 `p_value`，per-method per-seed 对 16 pairs 做 BH FDR 校正（`multipletests(method="fdr_bh")`），threshold_onset 无 p-value 保留原始 `significant` flag

### 验证结果
- α=1.0 (4 seeds): 6 robust 不变（FDR 收紧 method-level 计数但不翻转 consensus）
- α=0.00: 0→0 robust
- α=0.25: 1→1 robust
- α=0.50: 3→0 robust（`perm_granger` 7→0 sig 导致 3 个边缘 ece 对跌破 4/5 method 门槛）

### 文件位置
- 服务器：`/root/autodl-tmp/distrib_canary_collapse/consensus_framework.py` + `cross_alpha_analysis_v4.py`
- 本地：`artifacts/analysis/consensus_framework/consensus_framework.py` + `artifacts/analysis/cross_alpha/cross_alpha_analysis_v4.py`

---
