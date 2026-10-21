# code update sec4 exec only 3seed

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_update-sec4-exec-only-3seed_20260515T163741_result.json`
- **Structured JSON:** [`53724535f7efea73f2f6.json`](../../sessions/53/53724535f7efea73f2f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All numbers in the abstract reference seed 42 specifically for the collapse trajectory (0.642→0.003, 32%→96%) and are consistent. SFT 92.2% is consistent with the 3-seed data.

修改完成。报告如下：

---

**修改内容**:

1. **`paper/appendix.tex` — Table `tab:fol-detailed`** (exec-only 区块):
   - 新增 s43 1000-step 行: PR=0.90, ISR*=0.531, H7=100%, N-H=0% (H7 dominant)
   - 新增 s44 1000-step 行: PR=1.00, ISR*=0.002, H7=0%, H1=85%, N-H=3% (H8=15%)
   - 新增 1000-step 3-seed 汇总行: PR=0.95±0.05, ISR*=0.18±0.31, N-H=1.0±1.7%
   - 原 500-step 汇总行标签从 "500-step only" 改为 "500-step"

2. **`paper/experiments.tex` — §4.1 Cross-seed instability** (line 32):
   - 新增一句："By 1000 steps, all three converge to high PR (0.95±0.05) but ≤3% non-hacking, each through a different dominant mode (s42: H1 saturation; s43: H7 tautology; s44: H1+H8)."

3. **`artifacts/_project/paper/table_1000step_comparison.tex`**:
   - 原单行 exec-only (s42) 拆为 3 个 per-seed 行 + 1 个 mean 行

**确认一致的数字** (无需修改):
- SFT 数据: per-seed PR (0.13/0.11/0.15), genuine (92.3%/90.9%/93.3%), pooled 92.2% — 全部一致
- 所有引用 s42 1000-step 的地方 (abstract/intro/conclusion/§4.1 collapse/appendix): ISR=0.003, PR=0.96 — 一致
- Table `tab:goodhart-landscape`: SFT PR=13%, N-H=92% — 一致

**需注意**:
- exec-only 3-seed ISR 均值 0.18±0.31 的高方差来自 s43 的 H7 tautology (ISR=0.531), 与 s42/s44 的接近零形成对比
- s44 genuine=3% (3/100) 不是 0%, 这是三个 seed 中唯一有 genuine 残留的

---
