# audit ref verify C

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ref-verify-C_20260526T103536_result.json`
- **Structured JSON:** [`fe7e1873d9730418eb77.json`](../../sessions/fe/fe7e1873d9730418eb77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Auditor C — 全部 52 条引用验证报告

---

### 逐条验证结果

```
[1]  zhang2026latentgrpo       | ✓   |
[2]  zou2023repe              | ⚠️  | cite key 年份 "2023"，但实际发表于 ICLR 2025
[3]  rimsky2024caa            | ✓   |
[4]  shao2024grpo             | ✓   |
[5]  li2023iti                | ✓   |
[6]  turner2023actadd         | ✓   |
[7]  gao2023scaling           | ✓   |
[8]  skalse2022hacking        | ✓   |
[9]  casper2023openproblems   | ✓   | TMLR 2023.12.30 发表，年份 2023 可接受
[10] denison2024subterfuge    | ✓   |
[11] sharma2023sycophancy     | ⚠️  | cite key 年份 "2023"，但实际发表于 ICLR 2024
[12] shapira2026amplifies     | ✗   | 第一作者应为 Itai Shapira，非 Ori Shapira
[13] wang2025internal         | ✓   |
[14] wei2024synthetic         | ✓   |
[15] ackermann2026gradreg     | ⚠️  | 标题略有缩写，原文更长（含 "Reinforcement Learning from Human Feedback"）
[16] obrien2025fewbadneurons  | ✓   |
[17] mckinney2023fragility    | ✗   | 年份错误：NeurIPS 2022 Deep RL Workshop，应为 2022
[18] papadatos2024probepenalties | ✗ | 作者名字错误："Harris" → Henry，"Richard" → Rachel
[19] burns2023ccs             | ✓   |
[20] sinii2025smallvectors    | ✓   |
[21] consistency2025bctact    | ⚠️  | cite key 不规范（未用第一作者姓氏 irpan）
[22] beigi2025smart           | ✓   |
[23] rafailov2023dpo          | ✓   |
[24] ethayarajh2024kto        | ✓   |
[25] luo2026craft             | ⚠️  | 已被 ICML 2026 接收，venue 应更新
[26] manheim2019goodhart      | ⚠️  | arXiv 首次提交 2018.03，cite key 用 2019（末次修改），可接受但不常见
[27] wu2026rewardhacking      | ✓   |
[28] he2023debertav3          | ✓   |
[29] yang2025qwen3            | ✓   |
[30] grattafiori2024llama3    | ✓   |
[31] openai2025gpt41          | ✓   |
[32] kelkar2026persona        | ✗   | 第一作者应为 Ishaan Kelkar，非 Ameya Kelkar
[33] vennemeyer2025sycophancy | ✓   |
[34] hu2022lora               | ✓   |
[35] schulman2017ppo          | ✓   |
[36] rajbhandari2020zero      | ✓   |
[37] christiano2017rlhf       | ✓   |
[38] pan2022effects           | ✓   |
[39] marks2024geometry        | ✗   | venue 错误：实际发表于 COLM 2024，非 ICLR 2024
[40] kadavath2022language      | ✓   |
[41] lin2022truthfulqa        | ✓   |
[42] lightman2024verify       | ✓   |
[43] touvron2023llama         | ✓   |
[44] ouyang2022instructgpt    | ✓   |
[45] bai2022training          | ✓   |
[46] stiennon2020summarize    | ⚠️  | 标题介词错误："with" → "from"（应为 "Learning to Summarize from Human Feedback"）
[47] ziegler2019finetuning    | ✓   |
[48] hubinger2024sleeper      | ✓   |
[49] perez2023discovering     | ✓   |
[50] uesato2022solving        | ✓   |
[51] hewitt2019designing      | ✓   |
[52] belinkov2022probing      | ✓   |
```

---

### 汇总统计

| 状态 | 数量 | 占比 |
|------|------|------|
| ✓ 正确 | 40 | 76.9% |
| ⚠️ 需注意 | 7 | 13.5% |
| ✗ 必须修正 | 5 | 9.6% |

---

### 必须修正的错误（✗）

| # | cite_key | 问题 | 修正方案 |
|---|----------|------|----------|
| 12 | `shapira2026amplifies` | 第一作者名错误 | Ori Shapira → **Itai Shapira** |
| 17 | `mckinney2023fragility` | 年份错误 | 2023 → **2022**（NeurIPS 2022 Workshop） |
| 18 | `papadatos2024probepenalties` | 两位作者名字均错 | Harris → **Henry**, Richard → **Rachel** |
| 32 | `kelkar2026persona` | 第一作者名错误 | Ameya Kelkar → **Ishaan Kelkar** |
| 39 | `marks2024geometry` | venue 错误 | ICLR 2024 → **COLM 2024** |

### 建议修正的问题（⚠️）

| # | cite_key | 问题 |
|---|----------|------|
| 2 | `zou2023repe` | cite key 年份 2023 vs 实际 ICLR 2025 |
| 11 | `sharma2023sycophancy` | cite key 年份 2023 vs 实际 ICLR 2024 |
| 15 | `ackermann2026gradreg` | 标题缩写，缺少 "from Human Feedback" |
| 21 | `consistency2025bctact` | cite key 不规范，应为 irpan2025consistency |
| 25 | `luo2026craft` | 已被 ICML 2026 接收，venue 应更新 |
| 26 | `manheim2019goodhart` | arXiv 首次提交 2018，cite key 用 2019 |
| 46 | `stiennon2020summarize` | 标题 "with" 应为 "from" |

---

### Citation 语义正确性验证

| 引用 | 正文声称内容 | 判定 | 说明 |
|------|------------|------|------|
| `wu2026rewardhacking` | "representation-level directions can succeed as reward signals" | ✓ | 论文提出 Advantage Modification，用对比学习提取概念方向并整合进 GRPO，确实将表征方向用作奖励信号 |
| `manheim2019goodhart` | "taxonomize four Goodhart variants" | ✓ | 确实分类了四种变体：Regressional, Extremal, Causal, Adversarial |
| `vennemeyer2025sycophancy` | "sycophancy decomposes into independently steerable sub-behaviors" | ✓ | 论文识别出三种不同的谄媚行为，各自有独立的线性方向，可独立调控 |
| `papadatos2024probepenalties` | "Best-of-N reranking with linear probe penalties" | ✓ | 论文确实用线性探针得分修改代理奖励，在 Best-of-N 采样中重排候选 |
| `denison2024subterfuge` | "evidential warrant" | ⚠️ | **"evidential warrant" 一词未出现在该论文中。** 论文讨论从谄媚到奖励篡改的泛化，与 "evidential warrant" 仅有间接关联。引用松散 |
| `wang2025internal` | "late-layer preference shifts" + "social pressure overrides internal knowledge" | ✓ | 论文 abstract 明确提到 "late-layer output preference shift"，且研究了用户意见如何覆盖模型内部事实知识 |

---

### Orphan 条目

7 条 bib 条目未在正文中引用：`rafailov2023dpo`, `ethayarajh2024kto`, `mckinney2023fragility`, `schulman2017ppo`, `stiennon2020summarize`, `ziegler2019finetuning`, `hubinger2024sleeper`。其中 `stiennon2020summarize` 标题本身也有错，建议一并清理或在正文中引用。

---

**总结：5 条必须修正（作者名错误×2、年份错误×1、venue 错误×1、作者名错误×1），7 条建议修正，1 条语义引用松散（denison2024subterfuge 与 "evidential warrant"）。**

---
