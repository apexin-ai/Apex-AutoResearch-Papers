# ssh d027 perlayer rsa noinst

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d027-perlayer-rsa-noinst_20260515T222833_result.json`
- **Structured JSON:** [`4117f34e19efc8bf14ff.json`](../../sessions/41/4117f34e19efc8bf14ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出已保存到 `westd-19183:/root/autodl-tmp/vla-ssd/results/perlayer_rsa/`。

## 结果

### Peak RSA（验证通过）
| 条件 | Peak Layer | RSA |
|------|-----------|-----|
| Trained + Instruction | 9 | 0.4876 |
| Untrained + Instruction | 12 | 0.4846 |
| Trained, No Instruction | 30 | 0.4890 |
| Untrained, No Instruction | 6 | 0.4802 |

### 关键发现：Instruction 效果的层级分布

**Trained model** — instruction 效果高度层依赖：
- **Early layers (1-10)**：instruction 大幅提升 RSA，Δ 均值 +0.082，peak 在 layer 7（Δ=+0.138）
- **Mid layers (11-21)**：效果趋零，Δ 均值 +0.013
- **Deep layers (22-32)**：instruction 反而降低 RSA，Δ 均值 −0.034（no-inst 的 RSA 在深层单调递增至 0.489）

**Untrained model** — instruction 效果几乎为零：
- 所有层 Δ 在 [−0.014, +0.014] 内，均值仅 +0.005
- 曲线极其平坦（layer 1 后 RSA 稳定在 0.47-0.48）

**核心 pattern**：Training 使 LLM 学会在 early layers 利用 instruction 信息提升 action alignment，但代价是 deep layers 的 RSA 降低。Untrained（random）LLM 对 instruction 无差异响应——instruction tokens 穿过 random weights 后不产生有意义的 representation 变化。

### 产出文件
- `perlayer_rsa_all_conditions.json` — 全部数据
- `perlayer_rsa_comparison.pdf` / `.png` — 对比图（上：4 条件 RSA 曲线 + 2 条 reference 虚线；下：instruction effect Δ 柱状图）

---
