# code ifr perhead diagnostic

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ifr-perhead-diagnostic_20260513T073307_result.json`
- **Structured JSON:** [`437313eaefe0d9d68f8a.json`](../../sessions/43/437313eaefe0d9d68f8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**Per-head IFR 分解已经在运行，无法修复零重叠。** 根因不在 head 粒度。

### 核心发现

| 维度 | IFR | EAP-IG / EP |
|------|-----|-------------|
| Source 节点偏好 | MLP 输出 (`m2, m20, m22`) | 特定注意力头 (`a20.h9`) |
| 度量本质 | activation 幅度（"残差流中存在多少"） | 梯度因果性（"对 metric 影响多大"） |

**关键数据：**

1. **Destination-side 退化是 100%** — IFR 和 EAP-IG 都有同样问题（3281/3281 和 4164/4164 组全退化），这是架构性的（同层头共享 residual stream）

2. **即使 collapse 到 (src, dst_layer) 粒度，Jaccard 仍为 0.0000** — IFR 选的 source 节点和梯度方法完全不同

3. **Jaccard sweep**: 首次非零出现在 N=500（IFR-EAP=0.045），说明需要扩到前 500 条边才开始有微弱交集

4. **`unique_score_rank` 策略**: 把 100 unique scores 展开后 |IFR|=2191 条边，Jaccard 也仅 0.065

**结论**: IFR proximity 本质上度量的是 activation magnitude，天然偏向高幅度 MLP 输出；梯度方法度量的是 causal influence，找到任务相关的特定注意力头。这两者在 Qwen-0.5B IOI 上对信息流的理解根本不同。Per-head 分解不是修复方向。

---
