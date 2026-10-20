# code exp changepoint kstar

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_changepoint_kstar_20260520T071251_result.json`
- **Structured JSON:** [`6611bcfc008f82631edf.json`](../../sessions/66/6611bcfc008f82631edf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果总结：

## exp_changepoint_kstar 结果

**37 个实验的 PELT changepoint K* vs θ=0.60 K* 对比：**

| 指标 | 值 |
|------|-----|
| Exact agreement | 17/37 (45.9%) |
| **Within ±1 agreement** | **35/37 (94.6%)** |
| CP 方向 | 始终 ≤ θ（保守，从不高估） |

**Disagreement 模式非常规律：**
- 18 个 off-by-1 案例：disputed pair 的 AUC 在 [0.607, 0.654]，均值 0.636。PELT 把这些 borderline pair 归入 near-chance cluster，θ=0.60 判为 detectable
- 2 个 outlier：7-point retrain chain（所有 AUC > 0.60，无 chance-level 平台），CP 找到内部拐点

**Paper 叙事：** 非参数变点检测验证了 θ=0.60 的合理性。K\*\_cp 与 K\*\_θ 在 94.6% 实验中一致（±1），且 CP 系统性偏保守，说明 θ=0.60 是合理但略 liberal 的 cutoff，不引入虚假检测。

**其他发现：**
- Bootstrap (2000 samples) 与 direct PELT 结果完全一致
- PELT / BinSeg / BottomUp 三种方法在 primary penalty 下结果相同
- Best PELT penalty = 0.1（agreement 48.6%），但 penalty sensitivity 有限（5-point 序列的固有局限）

---
