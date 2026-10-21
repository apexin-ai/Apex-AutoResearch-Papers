# fix latex encoding and gpu check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_latex_encoding_and_gpu_check_20260520T110215_result.json`
- **Structured JSON:** [`984060dc644f62713e64.json`](../../sessions/98/984060dc644f62713e64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，不再报 UTF-8 错误。

---

## 汇报

### 1. LaTeX 编码问题

**根因**：不在 .tex/.bib 文件（都是合法 UTF-8 + 正确 LaTeX 编码 `{\'c}`）。问题在 `/home/ubuntu/agent-ml-research/core/writing/latex_compiler.py:139` 的 `_run()` 函数——`subprocess.run(text=True)` 在 pdflatex 的 stdout 包含 T1 编码字符（作者名 "Ana Marasović" 的 ć 被 T1 字体编码为 0xa2）时 UTF-8 strict 解码失败。

**修复**：去掉 `text=True`，改为 `proc.stdout.decode("utf-8", errors="replace")`。验证通过：编译成功，16 页，9 个 warnings。

### 2. 训练状态

| GPU | 显存占用 | GPU Util |
|-----|---------|----------|
| 0 | 61.7/97.9 GB | 100% |
| 1 | 61.7/97.9 GB | 100% |
| 2 | 45.6/97.9 GB | 97% |
| 3 | 45.6/97.9 GB | 76% |

| 实验 | 当前 step / total | 进度 |
|------|-------------------|------|
| uniform_1_7b_seed42_v5 | 2691/6103 | 44% |
| adaptive_1_7b_seed42_v5 | 2555/6103 | 42% |
| contamination_60_adaptive_seed42_tau08 | 2211/6103 | 36% |
| contamination_60_adaptive_seed123_tau08 | 2210/6103 | 36% |

4 个进程全部在跑，GPU 利用率正常，训练稳定。

---
