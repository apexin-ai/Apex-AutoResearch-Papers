# audit figures and repo

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_figures_and_repo_20260524T042900_result.json`
- **Structured JSON:** [`94d29fa441b25ee15953.json`](../../sessions/94/94d29fa441b25ee15953.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/audit_figures_repo.md` 并注册为 artifact。

## 审计结果

### 2 个 CRITICAL 问题（必须在提交前修复）

**1. Fig 2 constraint_regime_decomposition — 数据源错误**
- 图脚本硬编码的是 **tau=0.8** 实验的 regime 数据：α_eff=38.2%, ESS=59.8%, clean=2.0%
- 但 caption 和正文描述的是 **tau=0.7** 的数据：~50% α_eff, ~44% ESS, ~6% clean
- 服务器上 `binding_stats_seed42.json` 确认了 38.3/59.8/1.9（tau=0.8），与图脚本一致但与文字不一致
- **图的柱状图会显示 38/60/2，caption 却说 50/44/6，reviewer 会立刻发现**

**2. Fig 4 dr_dual_curve — adaptive 参考线标错**
- 图中 "Adaptive b*" 参考线 = 17.651（实际是 grid b=0.5 seed 42 的值）
- 论文正文报告的 adaptive 结果 = 17.674（tau=0.7 三种子均值）
- 把 grid-search 结果错标为 "Adaptive b*"

### 1 个 MODERATE 问题

**3. Fig 3 tau=0.8 PPL 值**：脚本 17.6527 vs registry 17.644，差 0.009

### 匿名仓库：状态正常
- Public 可访问，2026-05-23 push，2 commits，README 标题匹配论文
- 无法从 web 确认精确 144 文件数（需 clone 验证）

---
