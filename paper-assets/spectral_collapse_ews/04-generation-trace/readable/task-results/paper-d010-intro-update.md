# paper d010 intro update

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d010_intro_update_20260517T072931_result.json`
- **Structured JSON:** [`370581d9a71e7020db79.json`](../../sessions/37/370581d9a71e7020db79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成，`\label{sec:controller}` 已正确添加到 method.tex line 27。

## 修改汇总

### introduction.tex 修改

| 行 | 修改内容 |
|---|---|
| 3 | `---` → `,`（去 em-dash） |
| 8 | `---` → `,`（去 em-dash） |
| 15 | `---concentrating...rather than spreading it uniformly` → `, with real data concentrated...rather than spread uniformly`（去 em-dash + -ing 结尾） |
| 16 | controller 信号从 `effective rank` 改为 `effective rank + spectral log-volume`，明确 controller 使用 spectral log-volume |
| 21 | Contribution 1 重写：三阶段特征化 + 四指标（eff_rank, spectral log-volume, ppl, HellaSwag）+ 引用 `sec:spectral_trajectory`, `tab:phase0_metrics` |
| 22 | Contribution 2 重写：spectral log-volume 作为 EWS，比 eff_rank 更早下降，larger models temporal lead + 引用 `sec:cross_validation` |
| 23 | Contribution 3 重写：controller 基于 spectral log-volume decline rate；删除 "calibration error"；引用 `sec:controller`, `tab:phase0_metrics` |
| 21 | 去掉重复的 "to our knowledge"（line 14 已有） |
| 28 | `opening a new paradigm` → 拆为新句 `This finding supports the case for closed-loop intervention`（去 -ing 结尾 + "paradigm" 黑名单词） |

### method.tex 修改
- Line 27: 添加 `\label{sec:controller}`

### 验证通过
- 0 个 em-dash/en-dash
- 0 个 "calibration error" / "ECE"
- 0 个 "log-determinant" 残留
- 3 条 contribution 均有 section/table 引用

---
