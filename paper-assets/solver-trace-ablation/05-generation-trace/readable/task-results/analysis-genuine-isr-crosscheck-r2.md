# analysis genuine isr crosscheck r2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_genuine-isr-crosscheck-r2_20260514T152653_result.json`
- **Structured JSON:** [`b36ad2a841b9622c16f3.json`](../../sessions/b3/b36ad2a841b9622c16f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**比较表**:
| Condition | Seed | PR | Genuine ISR | H7% | Hacking |
|-----------|------|------|-------------|-----|---------|
| ISR β=0.1 | s42 | 0.81 | **0.601** | 16% | partial |
| ISR β=0.1 | s43 | 0.61 | N/A (n≈2) | 97% | severe |
| ISR β=0.1 | s44 | 0.89 | Unknown (n≈12) | 87% | severe |
| Random β=0.1 | s42 | 0.79 | 0.104 | 0% | none |
| Random β=0.1 | s44 | 0.89 | 0.062 | 0% | none |

**关键发现**:
1. **Genuine ISR 信号存在但不 robust** — s42 genuine ISR (0.601) vs random (0.104) = 5.8×，差异大且可解释
2. **3-seed mean±std 无法计算** — s43 仅 ~2 genuine samples，s44 的 12 genuine samples 缺 per-sample ISR 分解
3. **Random 完全无 hacking** — 两个 seed 均无 conclusion duplication，ISR 全部 genuine
4. **2/3 seed collapse** — ISR reward 本身诱导 hacking，方法不稳定

**建议**: 论文用 s42 做 within-seed case study（genuine 0.601 vs random 0.104），不报 3-seed 均值。若需 s44 genuine ISR，需对 eval outputs 跑 per-sample H7 分类。

---
