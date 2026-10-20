# analysis c4 a025 s42 fp32 mmct detail

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c4_a025_s42_fp32_mmct_detail_20260519T222129_result.json`
- **Structured JSON:** [`ae50556afe6b0c4cd398.json`](../../sessions/ae/ae50556afe6b0c4cd398.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册。核心发现：

1. **canary→mauve 是唯一接近显著的通道**：ece→mauve PermG raw p=0.031（F=17.9），entropy→mauve p=0.041（F=15.0），两者 raw-significant 但 BH FDR 8-pair 校正后统一拉到 0.094，刚好未过 0.05

2. **FDR 是瓶颈而非效应量**：如果做单 pair 检验，ece→mauve 直接通过。8-pair 校正吞掉了所有信号

3. **ece→mauve 存在双向性红旗**：rev p=0.028 也 raw-significant，两个方向都非随机，更像共因驱动而非因果

4. **K≥3=8/8 全部来自 naive+diff+threshold**：这三个方法检测的是 co-movement 而非 Granger 因果性，K=3 共识在此场景下无区分力。K=4 的 3 个 pair 额外票来自 TY

5. **C4 vs WikiText 呈对称反转的 collapse 模式**：
   - C4：entropy -53%、ppl +3617%，但 d1 仅 -4.1%（"calibration collapse without diversity collapse"）
   - WikiText：entropy -4.8%、ppl -18%，但 d1 -39%（"diversity collapse without calibration collapse"）
   - mauve 是唯一在两种模式下都大幅下降的指标（C4 -52%，Wiki -42%），因此 canary→mauve 是最有希望的跨数据集通道

---
