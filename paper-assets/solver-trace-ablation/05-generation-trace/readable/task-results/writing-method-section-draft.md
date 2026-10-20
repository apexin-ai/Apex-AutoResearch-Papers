# writing method section draft

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_method-section-draft_20260515T023348_result.json`
- **Structured JSON:** [`75519c7e1334fb4e1e37.json`](../../sessions/75/75519c7e1334fb4e1e37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method 章节已写入 `docs/paper/method.tex`（version 11，coverage 29/29）。

**结构**（约 1100 字，含 LaTeX 环境）：
- 3.1 Task — 形式化定义 $\pi_\theta: x \to y$，FOL/Prolog 双 solver
- 3.2 GRPO with Execution-Only Reward — 含 group normalization 公式 + $r_{\text{exec}} = \mathcal{S}(y)$
- 3.3 STA Protocol — 三步 LOO 算法，proved-only footnote 强调 C004
- 3.4 ISR Definition — $\mathrm{ISR}(x,y) = \frac{1}{n}\sum_i \mathbf{1}[\mathcal{S}(y_{\setminus i})=0]$，明确两个 scope limits（syntactic ≠ semantic; count bias）
- 3.5 Reward Formulations — 5 个公式（exec / additive ISR / additive random / convex / SFT），明示 random 是 matched control（D033/D057）
- 3.6 Hacking Taxonomy — 7 modes，含 query-as-fact gaming（Prolog s44 classifier blind spot, C006）

**符号一致性**：$r_{\text{exec}}$, $\mathrm{ISR}$, $\beta$, $n$, $c_i$, $\mathcal{S}$ 全程统一。所有引用用 `\citep{placeholder}` 占位（GRPO/Prover9/SWI-Prolog/ProofWriter/PPO/neurosymbolic GRPO 共 6 处）。

注意：tool 报警说有 2 个数字未挂 claims（`\{0, 1\}` 等公式中的常量），无需 provenance 追溯，可忽略。

---
