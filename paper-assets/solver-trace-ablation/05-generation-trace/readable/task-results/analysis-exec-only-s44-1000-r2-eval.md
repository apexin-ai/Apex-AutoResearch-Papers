# analysis exec only s44 1000 r2 eval

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exec-only-s44-1000-r2-eval_20260515T163255_result.json`
- **Structured JSON:** [`5f50789b0e2c8e744bfe.json`](../../sessions/5f/5f50789b0e2c8e744bfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 三 seed exec-only 1000 步完整对比

| | s42 (plan016) | s43 (plan001-s43-1000-r2) | s44 (plan001-exec-only-s44-1000-r2) |
|---|---|---|---|
| prove_rate | 0.96 | 0.90 | **1.00** |
| ISR | 0.003 | 0.531 | 0.002 |
| H7 | 0 | **90 (100%)** | 0 |
| H1 | **96 (100%)** | 0 | **85 (85%)** |
| H8 | 0 | 0 | **15 (15%)** |
| genuine | 0 | 0 | **3 (3%)** |

## 关键发现

**s44 500→1000 步发生了 hacking mode 跳转**：H7 从 97 降到 0，H1 从 0 涨到 85，H8 从 0 涨到 15。模型完全从 trivial-premise（H7）模式切换到了 conclusion-in-premise（H1）+ conjunction-collapse（H8）模式。

**三个 seed 收敛为两种模式**：
- s42, s44 → H1 主导模式（低 ISR ~0.002-0.003）
- s43 → H7 主导模式（高 ISR ~0.531）

**s44 是唯一有 genuine proofs 的 seed**（3/100 = 3%），但仍然接近 0。三个 seed 的 genuine rate 实质上都是 0%。

**s44 是唯一出现 H8 的 seed**（15%）。H8 = conjunction collapse，与 H1 有 3 个样本重叠（100 - 85 - 15 + 3 = 3 genuine）。

**ISR 语义（C006）**：s42/s44 的低 ISR 反映 H1 模式——结论直接嵌入前提，删除任何一条非结论前提不影响结果，ISR≈0 是冗余编码而非无推理。s43 的高 ISR 反映 H7 模式——trivial premises 下每条都"必要"（因为 ISR 的 STA 计算在 trivial 上得分高）。

---
