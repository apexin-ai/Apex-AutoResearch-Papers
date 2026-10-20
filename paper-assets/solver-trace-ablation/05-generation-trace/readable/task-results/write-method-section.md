# write method section

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_method-section_20260515T004322_result.json`
- **Structured JSON:** [`bffbaf0b8bca4a877ebc.json`](../../sessions/bf/bffbaf0b8bca4a877ebc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method 章节草稿已完成，两个版本均已注册为 artifact：

- **LaTeX**: `artifacts/_project/paper/method_76d073.tex` (`art_20260515_76d073`)
- **Markdown**: `artifacts/_project/paper/method_draft.md` (`art_20260515_3bf026`)

**结构覆盖**（6 个子节，~1200 words）：

| 子节 | 内容 |
|------|------|
| §3.1 Task | NL→FOL/Prolog formalization，Prover9/SWI-Prolog 验证，r_exec 的结构盲区 |
| §3.2 GRPO | 标准 GRPO 公式（advantage + policy gradient），baseline PR 轨迹 12%→32%→93%（引用 `sta-phase0-baseline`, `plan003-eval-exec-only-r5`） |
| §3.3 STA | LOO 消融 4 步协议，solver-agnostic 设计，proved-only ISR* 定义 |
| §3.4 ISR | 形式化定义 ISR(f) = (1/n)Σ𝟙[fail]，[0,1] 边界语义，syntactic necessity ≠ semantic faithfulness，premise count bias 预告 |
| §3.5 Reward | 4 种配方（exec-only / additive ISR / additive random control / SFT），convex combination 失败简述 |
| §3.6 Taxonomy | 7 种 hacking 模式（H1-H7），标注 ISR-specific（H6）和 Prolog-specific（H7），meta-Goodhart 归因 |

**关键写作决策**：
- ISR 定义处即标注"syntactic necessity ≠ semantic faithfulness"，为 Discussion 中 ρ=-0.049 铺垫
- Premise count bias 在 §3.4 预告，§4 中用 premise-count-matched 1.06x 分析兑现
- H6/H7 独立编号（非连续 H5→H6→H7），H6 明确标注 64.5% vs 0% 的 ISR-specificity
- Convex combination 仅一句带过（penalty effect），避免占用 word budget

---
