# eval mistral contam5 fixed theta

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mistral-contam5-fixed-theta_20260524T060459_result.json`
- **Structured JSON:** [`876535355f8de0a90da3.json`](../../sessions/87/876535355f8de0a90da3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算完成。Contam_5 fixed-θ 结果：

| 指标 | 值 |
|------|-----|
| θ_fixed | -1.0876 |
| lz\*_free | -5.729 |
| **lz\*_fixed** | **-6.643** |
| Cohen's d (point) | **3.94** |
| Cohen's d (bootstrap median) | 3.98 |
| 95% CI | [2.47, 12.93] |

对比三个 contam 水平：

| 条件 | lz\*_fixed | Cohen's d | 95% CI |
|------|-----------|-----------|--------|
| contam_5 | -6.64 | 3.94 | [2.47, 12.93] |
| contam_15 | -3.48 | 2.69 | [1.53, 9.06] |
| contam_50 | -11.33 | 5.80 | [3.87, 18.45] |

注意：contam_5 的 fixed-θ lz\*（-6.64）比 free-θ（-5.73）更极端，符合预期——固定 θ 消除了被污染项目对能力估计的膨胀效应，使 misfit 信号更强。contam_5 的 Cohen's d = 3.94 远超大效应阈值（0.8），说明即使仅 5% 污染也能被 person-fit 可靠检测。

结果已保存到 `/root/autodl-tmp/ctrl_contam_mistral/results/theta_fixed_n10_recompute.json`。seen/unseen 的 fixed-θ 分拆无法计算（结果文件中没有 `seen_indices`）。

---
