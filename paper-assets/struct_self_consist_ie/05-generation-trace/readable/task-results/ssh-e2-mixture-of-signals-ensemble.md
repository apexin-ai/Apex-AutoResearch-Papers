# ssh e2 mixture of signals ensemble

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_e2-mixture-of-signals-ensemble_20260520T101418_result.json`
- **Structured JSON:** [`c4286818327939fbd970.json`](../../sessions/c4/c4286818327939fbd970.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

E2 实验完成。结果汇总：

**Selection F1 (best-of-N sample selection)**
- 5-signal 加权 ensemble 跨 7 configs 平均比 best single signal **+0.72pp** (paired bootstrap p=0.000, **显著**)
- 最优权重中 LP 始终占主导 (0.8)，VC 作为次要信号贡献增益
- LR ensemble 在 fewnerd 上接近 grid search 效果，但在 conll/scierc 上表现差

**Entity Construction (weighted majority voting)**
- Ensemble 加权构建 vs uniform 构建：**-0.11pp** (p=1.0, **不显著**)
- 加权构建在这个 task 上没有带来提升

**Per-config 细节**

| Config | BestSig | Ens CV | Δpp | Optimal weights |
|--------|---------|--------|-----|-----------------|
| conll_s123 | FK=.9045 | .9090 | +0.68 | VC=0.6, EM=0.2, LP=0.2 |
| conll_s456 | FK=.9030 | .9063 | +0.33 | VC=0.8, EM=0.2 |
| fewnerd_s123 | LP=.7619 | .7731 | +1.12 | VC=0.2, LP=0.8 |
| fewnerd_s456 | LP=.7620 | .7679 | +0.59 | VC=0.2, LP=0.8 |
| fewnerd_s789 | LP=.7617 | .7666 | +0.49 | VC=0.2, LP=0.8 |
| scierc_s456 | SJ=.6442 | .6471 | +0.29 | SJ=0.2, LP=0.8 |
| scierc_s789 | LP=.6514 | .6436 | +0.03 | FK=0.2, LP=0.8 |

结论：Ensemble 对 selection 有显著但适度的提升；对 entity construction 无提升。LP 是核心信号，VC 是最有效的互补信号。

---
