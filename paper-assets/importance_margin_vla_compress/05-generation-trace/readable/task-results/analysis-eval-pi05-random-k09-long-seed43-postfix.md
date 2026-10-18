# analysis eval pi05 random k09 long seed43 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_random_k09_long_seed43_postfix_20260524T203734_result.json`
- **Structured JSON:** [`80ddc57b0d35e43e4fd3.json`](../../sessions/80/80ddc57b0d35e43e4fd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部正常完成。结果汇总：

---

## 实验 1: Random k=0.9 Long seed43

**总 SR = 35.6%** (178/500) | EXIT_CODE=0 ✓

| Task | SR |
|------|-----|
| T0: put both the alphabet soup and the tomat… | 22% |
| T1: put both the cream cheese box and the bu… | 46% |
| T2: turn on the stove and put the moka pot o… | 44% |
| T3: put the black bowl in the bottom drawer | 50% |
| T4: put the white mug on the left plate and… | 18% |
| T5: pick up the book and place it in the bac… | 32% |
| T6: put the white mug on the plate and put t… | 10% |
| T7: put both the alphabet soup and the cream… | 50% |
| T8: put both moka pots on the stove | 4% |
| T9: put the yellow and white mug in the micr… | 80% |

**对比**: seed42 Random k=0.9 Long = 32.0% → seed43 = 35.6%，差异 3.6pp，seed 间基本稳定。  
**Importance margin**: L2norm k=0.9 Long = 80.0% vs Random k=0.9 Long avg ≈ 33.8% → margin = **46.2pp**  
**Conclusion**: SUCCESS — Random baseline 正常完成，确认 Long suite 下 k=0.9 的 importance margin 巨大。

---

## 实验 2: L2norm k=0.925 Goal seed42

**总 SR = 89.8%** (449/500) | EXIT_CODE=0 ✓

| Task | SR |
|------|-----|
| T0: open the middle drawer of the cabinet | 86% |
| T1: put the bowl on the stove | 96% |
| T2: put the wine bottle on top of the cabinet | 100% |
| T3: open the top drawer and put the bowl ins… | 92% |
| T4: put the bowl on top of the cabinet | 98% |
| T5: push the plate to the front of the stove | 98% |
| T6: put the cream cheese in the bowl | 88% |
| T7: turn on the stove | 100% |
| T8: put the bowl on the plate | 96% |
| T9: put the wine bottle on the rack | 44% |

**对比**: L2norm k=0.85 Goal = 87.4% → L2norm k=0.925 Goal = 89.8%（+2.4pp）  
**Cliff zone 判断**: Random k=0.925 Goal = 70.0%, L2norm k=0.925 Goal = 89.8% → importance margin = **19.8pp**。L2norm 在 92.5% retention 下仍远高于 random，无 cliff。  
**Conclusion**: SUCCESS — L2norm 在 Goal suite 的 cliff zone 不在 k=0.925 附近，性能仍接近 full retention（87.4%→89.8%），importance-aware pruning 稳定。

---

## 实验 3: L2norm k=0.3 Goal seed42

**总 SR = 51.8%** (259/500) | EXIT_CODE=0 ✓

| Task | SR |
|------|-----|
| T0: open the middle drawer of the cabinet | 70% |
| T1: put the bowl on the stove | 18% |
| T2: put the wine bottle on top of the cabinet | 76% |
| T3: open the top drawer and put the bowl ins… | 26% |
| T4: put the bowl on top of the cabinet | 68% |
| T5: push the plate to the front of the stove | 44% |
| T6: put the cream cheese in the bowl | 20% |
| T7: turn on the stove | 98% |
| T8: put the bowl on the plate | 76% |
| T9: put the wine bottle on the rack | 22% |

**对比**: Object L2norm k=0.3 Goal = 30.4%, Random k=0.3 Goal = 32.2% → **L2norm k=0.3 Goal = 51.8%**  
**Importance margin at extreme pruning**: L2norm 51.8% vs Random 32.2% = **+19.6pp**  
**Conclusion**: SUCCESS — 即使在极端裁剪（仅保留 30% tokens = 76/256）下，L2norm 仍比 random 高出近 20pp。之前 Object L2norm k=0.3=30.4% 的低值可能是 Object suite 本身更难（不同 suite）。Goal suite 上 L2norm importance-aware pruning 在极端压缩下仍有显著优势。

---
