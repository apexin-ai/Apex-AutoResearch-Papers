# analysis eval math500 grpo rasp alpha2p0 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_math500_grpo_rasp_alpha2p0_20_20260523T031600_result.json`
- **Structured JSON:** [`f64abd7b03c218ac82fe.json`](../../sessions/f6/f64abd7b03c218ac82fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**GRPO RASP α=2.0 MATH-500 结果：26.2% (131/500)**

| 配置 | MATH-500 |
|------|----------|
| SFT α=2.0 | 24.0% |
| **GRPO RASP α=2.0** | **26.2%** |
| GRPO Standard 20% | 26.4% |
| GRPO CKA-only 20% | 26.6% |

**Δ(GRPO RASP − SFT) = +2.2pp**，超过 1pp 阈值。

**C1 decoupling 判定**：在 MATH-500 上，GRPO RASP (26.2%) 与 SFT (24.0%) 差距 2.2pp，不满足 |Δ| < 1pp 的严格标准。不过 GRPO 三种剪枝方式（Standard 26.4%、CKA-only 26.6%、RASP 26.2%）之间差异极小（<0.4pp），说明 GRPO 恢复训练本身在 MATH-500 上一致性地比 SFT 高约 2pp——这更可能反映 GRPO 训练目标对数学推理的微弱增益，而非结构差异效应。C1 decoupling 在**剪枝方法间**依然成立（三种方法互差 <0.5pp），但 GRPO vs SFT 的 training-objective gap 需要在论文中区分讨论。

---
