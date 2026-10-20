# writing neural probe polish

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_neural-probe-polish_20260514T175344_result.json`
- **Structured JSON:** [`04bbd0f1a66efff782e3.json`](../../sessions/04/04bbd0f1a66efff782e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项检查结果：

**(a) K\* hierarchy 论证** — 达标。
- 三层级定义清晰：K\*\_theory（理论上界，最优表示+分类器）、K\*\_neural（表示依赖上界，模型探针）、K\*\_15D（可部署边界，模型无关特征）— lines 386-392
- 数值明确标注：K\*\_15D=2, K\*\_neural=3, K\*\_theory≥3 — lines 390, 392
- 信息丢失机制：line 391 明确说"at least one additional discriminable generation boundary exists in the frozen representations but is lost during projection into the hand-crafted feature space"，结合 lines 380-381 具体指出 2v3 边界（neural AUC=0.6195 > θ vs 15D AUC=0.5609 < θ）

**(b) Interpretability–discriminability tradeoff** — 达标。
- 两端对比清晰：15D = model-free, interpretable, lightweight, trains in seconds (line 396-397) vs Neural = model-specific, opaque, 100×+ overhead (line 398)
- Neural probe 明确定位为"theoretical exploration tool" (line 399)
- Headline result 结论明确："K\*=2 remains the relevant boundary for deployable depth estimation" (line 400)

**(c) Pending replication caveat** — 达标。
- Single dataset caveat 清晰：仅 Qwen-continuation，Pythia/OLMo pending (line 408)
- 2v3 边缘性量化：+1.95pp over θ, std=0.0094, ~2 std deviations (line 403)
- 双重声明 preliminary：line 404 "preliminary evidence...not as a firm revision" + line 409 "single-dataset preliminary finding rather than a general result"
- 5 个 TODO(exp-015-rerun) 占位符完整保留 (lines 361, 364, 405-407)

**质量达标，无需修改。**

---
