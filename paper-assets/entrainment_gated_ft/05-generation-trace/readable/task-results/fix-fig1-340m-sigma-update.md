# fix fig1 340m sigma update

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_fig1-340m-sigma-update_20260519T191646_result.json`
- **Structured JSON:** [`894efa66bdd3fdd6cce8.json`](../../sessions/89/894efa66bdd3fdd6cce8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已更新。340M 线 endpoint 在 attn_ratio=25% 处为 0.0160（旧值 0.0151），略高于之前，符合预期。"rebound" 标注仍正确指向 7.7% 处的 bump，1.3B 的 "-79%" 标注由代码动态计算，未受影响。

产出：
- `figures/paper/gen_fig1.py` — sigma_340M 已更新为 exp-007 权威值
- `figures/paper/fig1_decoupling_hero.pdf` + `.png` — 重新生成
- `artifacts/_project/chart/fig1_decoupling_hero.pdf` — 已复制

---
