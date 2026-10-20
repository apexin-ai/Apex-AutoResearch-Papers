# code sync paper remote

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sync-paper-remote_20260519T170406_result.json`
- **Structured JSON:** [`7fcfd3998a0281d2781c.json`](../../sessions/7f/7fcfd3998a0281d2781c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. 同步结果
- **远程没有 git 仓库**，改用 rsync 同步 .tex/.bib 文件
- rsync 显示 tex/bib 文件已是最新（无差异传输）
- **注意**：远程磁盘 30G/30G 已满（100%），PDF/图片等大文件未同步（空间不足）

### 2. K / num_generations 所有提及

| 文件 | 行号 | 内容 |
|------|------|------|
| `experiments.tex` | 10 | `$K{=}4$, lr $10^{-6}$, 500 steps default` |
| `method.tex` | 8 | `GRPO~\citep{deepseekmath} ($K{=}4$)` |
| `checklist.tex` | 41 | `GRPO $K{=}4$, 500/1000 steps` |
| `appendix.tex` | 846 | `$K{=}4$ rollouts, FOLIO training set` (LLaMA 实验) |

另外 `experiments.tex:63` 和 `appendix.tex:185` 提到 "GRPO rollouts" 但未指定 K 值（上下文已由前文定义）。

### 3. K=8 错误声明检查
**未发现任何 K=8 的声明。** 所有 4 处 K 值声明均为 `K=4`，与实际配置一致。

---
