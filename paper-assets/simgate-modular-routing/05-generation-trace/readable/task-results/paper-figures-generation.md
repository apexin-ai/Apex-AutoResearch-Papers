# paper figures generation

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figures-generation_20260515T101501_result.json`
- **Structured JSON:** [`f8cb78d374ac1925b165.json`](../../sessions/f8/f8cb78d374ac1925b165.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部产出完成。总结：

**已生成并注册的 artifacts：**

1. **signal_reversal.pdf + .png** — 服务器路径 `/root/autodl-tmp/simgate-modular-routing/docs/paper/figures/`
   - Grouped bar chart，红色(det-preferred)、绿色(int-preferred)、灰色(no-preference)
   - 带 "Signal Reversal" 箭头标注，突出 ScienceWorld 与 MATH 间的 label 分布反转
   - Artifact ID: `art_20260515_0113e0`

2. **cross_env_summary_table.tex** — 已注册到 artifacts
   - 三行对比表：ScienceWorld / MATH / ALFWorld
   - 含脚注说明 ALFWorld capability gap 机制差异
   - Artifact ID: `art_20260515_bf2e29`

PNG 无法通过 SCP 拉回本地（SSH 密钥不兼容本地 scp 调用），图表文件留存服务器上，可通过 SSH 访问验证。

---
