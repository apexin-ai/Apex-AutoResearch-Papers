# analysis ty seed audit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ty_seed_audit_20260515T235823_result.json`
- **Structured JSON:** [`46c9e4062d30087fc472.json`](../../sessions/46/46c9e4062d30087fc472.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心发现：

**两个 bug 导致三份报告互相矛盾：**

1. **Off-by-one**（`window_sensitivity.py:193`）：`[:T]` 在 T=10 时只取 10 个点，少了 gen_10。ECE→d1 因此从 3/4 sig 掉到 2/4 sig（seed 45 从 p=0.028 变为 p=0.069）。

2. **两套不兼容的 TY 实现**：
   - `method_ablation.py`（论文用的）：ADF 测 d_max、固定 p=1、F-test → TE 系列被正确判为 I(0)，d_max=0，df_resid=7，F 值 100–500，全部显著
   - `window_sensitivity.py`：硬编码 d=1、AIC 选 p=2、chi² → VAR(3) 吃光自由度，TE 全部 p>0.3

**关键结论：**
- **Paper FNR=33.3% (2/6) 正确** — ECE→d2 和 ECE→d3 各 2/4 sig，被 TY miss
- **Paper ECE→d1 sig_seeds=3/4 正确** — s42✓ s43✓ s44✗ s45✓
- **Window sensitivity 报告的 TE p>0.3 是错的** — 用了错误的 TY 实现（Bug #2），不是 off-by-one 导致的
- ECE pairs 中 s44/s45 不显著的根因：ADF 将这两个 seed 的 ECE 判为 I(1)，d_max=1 导致 df_resid 只有 4，power 不足

报告已写入 `artifacts/ty_seed_audit/ty_audit_report.md` 并注册。

---
