# review appendix xref audit

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_appendix-xref-audit_20260518T052112_result.json`
- **Structured JSON:** [`066386d71ca9b992786c.json`](../../sessions/06/066386d71ca9b992786c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Appendix references `sec:diagnostics` (L195) and `tab:main_results` (L225) — both exist in experiments.tex. Reverse check clean.

## 附录交叉引用审计

### 未被正文引用的附录 labels:

| Label | 位置 | 类型 | 状态 |
|---|---|---|---|
| `\label{app:diagnostics}` | appendix.tex:L193 | section | 未被任何文件引用（正文用 `\ref{tab:capability_trap}` 直接引表，跳过了 section label） |
| `\label{app:power}` | appendix.tex:L223 | section | 未被任何文件引用（正文 limitations_content.tex 用 `\ref{tab:power}` 直接引表，跳过了 section label） |
| `\label{app:bootstrap}` | appendix.tex:L247 | section | 未被任何文件引用（正文 discussion.tex 用 `\ref{tab:bootstrap}` 直接引表，跳过了 section label） |
| `\label{alg:maxsat}` | appendix.tex:L157 | algorithm | 仅附录内部自引用（appendix.tex:L151） |
| `\label{alg:scorer}` | appendix.tex:L177 | algorithm | 仅附录内部自引用（appendix.tex:L151）；正文 method.tex:L73 用文字 "Algorithm~2" + `\ref{app:z3-pseudocode}` 间接引用，未用 `\ref{alg:scorer}` |

### 已被正文引用的附录 labels:

| Label | 位置 | 类型 | 引用位置 |
|---|---|---|---|
| `\label{app:prompts}` | appendix.tex:L3 | section | method.tex:L52, experiments.tex:L13, limitations_content.tex:L1 |
| `\label{app:z3-pseudocode}` | appendix.tex:L149 | section | method.tex:L73 |
| `\label{tab:capability_trap}` | appendix.tex:L218 | table | experiments.tex:L67, appendix.tex:L195（自引） |
| `\label{tab:power}` | appendix.tex:L240 | table | limitations_content.tex:L1, appendix.tex:L225（自引） |
| `\label{tab:bootstrap}` | appendix.tex:L264 | table | discussion.tex:L8, appendix.tex:L249（自引） |

### 反向检查（附录引用正文 label）:

| 附录引用 | 目标 | 正文中是否存在 |
|---|---|---|
| `\ref{sec:diagnostics}` (L195) | experiments.tex:L65 | 存在 |
| `\ref{tab:main_results}` (L225) | experiments.tex:L27 | 存在 |
| `\ref{alg:maxsat}` (L151) | appendix.tex:L157 | 存在（自引） |
| `\ref{alg:scorer}` (L151) | appendix.tex:L177 | 存在（自引） |
| `\ref{tab:capability_trap}` (L195) | appendix.tex:L218 | 存在（自引） |
| `\ref{tab:power}` (L225) | appendix.tex:L240 | 存在（自引） |
| `\ref{tab:bootstrap}` (L249) | appendix.tex:L264 | 存在（自引） |

反向检查全部通过，无悬空引用。

### 总结

**10 个附录 labels 中，5 个被正文引用，5 个未被正文引用。**

- 3 个 section labels（`app:diagnostics`、`app:power`、`app:bootstrap`）完全无人引用——正文绕过 section label 直接引用了其中的 table label，导致这些 section label 成为孤儿。虽然不影响编译，但如果审稿人想跳转到附录对应 section，正文缺少 section 级引导。
- 2 个 algorithm labels（`alg:maxsat`、`alg:scorer`）仅在附录内部互引，正文未直接使用 `\ref{alg:...}`。`alg:scorer` 的情况尤其值得注意：method.tex 用硬编码 "Algorithm~2" 而非 `\ref{alg:scorer}`，如果 algorithm 编号变化会导致不一致。

---
