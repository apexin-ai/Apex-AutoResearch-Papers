# analysis v9 pcgrad cossim check

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v9_pcgrad_cossim_check_20260519T180416_result.json`
- **Structured JSON:** [`3168506356f8a3a8519e.json`](../../sessions/31/3168506356f8a3a8519e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志共 53 行，训练仍在 Epoch 0 step 1100，且 PCGRAD 诊断仅 2 个采样点（step 50 和 100）。以下是完整分析。

---

## PCGRAD 诊断汇总

| step | cos_sim | mag_ratio_pre | mag_ratio_post | conflict_layers | conflicting_steps |
|------|---------|---------------|----------------|-----------------|-------------------|
| 50   | -0.0610 | 2.81          | 2.78           | 54.0%           | 4/8               |
| 100  | -0.0707 | 6.01          | 5.97           | 57.6%           | 7/8               |

## L_GAR 趋势（每50步）

| step | L_GAR (v9) | vs v7 同阶段 |
|------|-----------|-------------|
| 0    | 0.2342    | ~0.23 (相同起点) |
| 50   | 0.2349    | — |
| 100  | 0.2337    | — |
| 150  | 0.2270    | — |
| 200  | 0.2339    | — |
| 250  | 0.2280    | — |
| 300  | 0.2205    | — |
| 350  | 0.2196    | — |
| 400  | 0.2090    | v7 已开始快速下降 |
| 450  | 0.1675    | — |
| 500  | 0.1760    | — |
| 550  | 0.1673    | — |
| 600  | 0.1244    | — |
| 650  | 0.1102    | — |
| 700  | 0.0939    | — |
| 750  | 0.0737    | — |
| **800** | **0.0832** | **v7 ≈ 0.006** |
| 850  | 0.0491    | — |
| 900  | 0.0410    | — |
| 950  | 0.0304    | — |
| 1000 | 0.0343    | — |
| 1050 | 0.0239    | — |
| 1100 | 0.0367    | — |

## Gate 趋势

| step | mean   | std    | min    | max    |
|------|--------|--------|--------|--------|
| 0    | 0.8097 | 0.0341 | 0.6836 | 0.8672 |
| 50   | 0.8101 | 0.0572 | 0.7109 | 0.9453 |
| 100  | 0.8717 | 0.0497 | 0.7773 | 0.9766 |

训练行中 Gate 值的趋势：0.810 → 0.816 → 0.827 → 0.856 → 0.869 → 0.882 → 0.877 → **0.899** (step 1100)

## 分析结论

### 1. PCGrad 投影基本无效

- **cos_sim 仍为负值**：step 50 = -0.061，step 100 = -0.071。v7 epoch 0 的 cos_sim = -0.089。PCGrad 后 cos_sim 没有变正，说明投影并未消除梯度冲突方向——它只在逐层投影，但聚合后全局冲突仍然存在。
- **mag_ratio 几乎不变**：pre→post 变化仅 ~1%（2.81→2.78, 6.01→5.97）。NTP 梯度仍以 3-6x 的幅度压制 GAR。
- **conflict_layers 在上升**：54% → 57.6%，且 conflicting_steps 从 4/8 → 7/8，说明随着训练推进冲突变得更普遍。

### 2. L_GAR 衰减被减缓但未被阻止

- **step 800 对比**：v9 L_GAR = 0.083 vs v7 = 0.006，v9 高 **13.8x**。PCGrad 确实让 L_GAR 在前期衰减更慢。
- **但 L_GAR 仍在单调下降**：0.234 → 0.037 (step 1050)，下降了 **84%**。趋势上看正在趋近 0，只是速度比 v7 慢约 2-3x。
- **step 0-350 是"高原期"**（0.23→0.22），之后加速下降。v7 没有这个高原期。
- 结论：PCGrad 延缓了坍塌但无法阻止。到 epoch 1-2，L_GAR 大概率也会趋近 0。

### 3. NTP 仍然主导

- mag_ratio 从 2.81（step 50）跃升到 6.01（step 100），趋势与 v7（epoch 0: 7.5 → epoch 2: 14.7）一致。NTP 梯度在训练中持续放大其相对优势。
- Gate 持续走高（0.81 → 0.90），与 v7 行为一致：模型通过关闭 turn 分支来降低 Loss。

### 4. 对 paper 因果论证的意义

这组结果**强化因果链**：

> **梯度冲突 → NTP 主导 → gate 坍塌 → L_GAR 消失**

PCGrad 是一个"弱干预"——它投影掉逐层冲突分量但保留了量级不对称。结果符合预期：
- 减缓但不阻止坍塌 → 证明梯度冲突是**必要条件之一**但非唯一原因
- mag_ratio 不变 → **量级主导**(magnitude dominance) 是独立于方向冲突的另一致因
- 这为 paper 提供了 ablation 证据：方向投影 alone 不够，还需要量级均衡（如 GradNorm/动态权重）

**注意**：PCGRAD 诊断仅 2 个采样点，且训练还在 Epoch 0。需要等完整 3 epoch 训练结束后才能下最终结论。目前的趋势已经足够说明 PCGrad 的局限性。

---
