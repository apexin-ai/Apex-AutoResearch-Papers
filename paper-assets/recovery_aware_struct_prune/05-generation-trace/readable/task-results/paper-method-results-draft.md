# paper method results draft

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_method-results-draft_20260517T174402_result.json`
- **Structured JSON:** [`90d4413e36e0adac8387.json`](../../sessions/90/90d4413e36e0adac8387.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个文件已写入：

- `paper/method.md` — 包含 RASP scoring formula ($S(h) = I(h) \times (1-F(h))^\alpha$)、Taylor importance + intra-layer CKA 计算、pruning procedure、两阶段 recovery pipeline (SFT + GRPO 超参)、collapse diagnostic framework (frac\_zero\_std / grad\_norm / mean\_terminated\_length)、实验设计 (DeepSeek-R1-Distill-Qwen-7B, 20% sparsity, N=1319 GSM8K)。

- `paper/results.md` — 按 claim-evidence 结构组织：
  - 4.1 C1: 三模型 reward-accuracy decoupling (Unpruned Δ=0.00pp, Standard -0.38pp, RASP -0.84pp) + Qwen Math 跨模型验证
  - 4.2 C2: collapse severity gradient (RASP step 10 permanent, Standard step 60 transient, Unpruned never) + mechanism 解释 + 25% sparsity 确认
  - 4.3 C3: SFT recovery 对比 (RASP +2.2pp, p=0.25) + Redundancy-Stability Tradeoff 总结
  - 4.4: Alpha ablation (U-shape post-prune, SFT equalizing effect)

所有数字均标注了 registry 来源实验 ID。

---
