# paper writing

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_20260516T025433_result.json`
- **Structured JSON:** [`fe443cd95c0cf19932e9.json`](../../sessions/fe/fe443cd95c0cf19932e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Introduction 已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex`。

**结构**：5 段，按 writing_plan.yaml 的 para_1–para_5 组织：
1. **Problem** — VLA 的隐含假设：LLM fine-tuning 注入 action knowledge
2. **Gap** — 现有工作停留在 behavioral 层面，无 representational decomposition（引用 grant2026, haon2025）
3. **Approach** — 2×2 factorial design + RSA + probes，分解 OpenVLA 各组件
4. **Findings** — 三个核心发现，所有数字均来自同一 probe set（50ep），RSA 数字全部安全
5. **Contributions** — 3-item itemize + 一句 implications 指向 Discussion

**合规检查**：
- R² 数字仅引用 Proj/LLM 系列（0.706, 0.731, 0.686），未混入 CLIP/DINO 100ep 数字
- 未使用 "consistently"（单 benchmark）
- "significantly" 未出现（统计检验用 p 值直接报告）
- 所有引用均限于允许的 bibtex keys
- 术语与 experiments.tex / method.tex / discussion.tex 一致

---
