# paper conclusion update check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_conclusion_update_check_20260517T200404_result.json`
- **Structured JSON:** [`3b9e3311d0c3972b3f58.json`](../../sessions/3b/3b9e3311d0c3972b3f58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

写入成功。总结：

## conclusion.tex 更新内容

**旧版问题：** 只提 "GPT-2-medium replication"，缺 OPT-1.3B、C4 域转移、ECE vs token_entropy 信号质量差异；末段将跨架构泛化仅作为"conjecture"。

**具体修改：**

| 段落 | 旧 | 新 |
|------|----|----|
| Para 2 | "scaling from exploratory screening..." (-ing 分词) | "provides four tiers ... from exploratory screening to publication-grade claims" |
| Para 3 (新增) | 仅提 GPT-2 medium replication | 三架构泛化 (Pythia-410M, GPT-2 Medium, OPT-1.3B) + C4 域转移 (Pythia-1B 8/8 consensus) + ECE vs token_entropy 信号质量差异 |
| Para 4 | dose-response 内容散落在旧 Para 3 | 独立段落，完整 5-regime dose-response + detectability boundary |
| Para 5 | "we **conjecture** the consensus framework transfers" | "the consensus framework's successful **generalization** across architectures and data domains **supports** its transfer" |

## experiments.tex 中剩余 `[TBD]` 标记

| 文件:行号 | 内容 |
|-----------|------|
| `experiments.tex:342` | Table caption: `\textbf{[TBD]}: Scale experiment (Pythia-1.4B) in progress.` |
| `experiments.tex:351` | Table row: `Scale ($3.4\times$) & Pythia-1.4B / Wiki & \multicolumn{7}{c}{\textbf{[TBD]}}` |

两处均为 Pythia-1.4B scale 实验，待该实验完成后填入数据。无其他 CONDITIONAL/TODO 标记。

---
