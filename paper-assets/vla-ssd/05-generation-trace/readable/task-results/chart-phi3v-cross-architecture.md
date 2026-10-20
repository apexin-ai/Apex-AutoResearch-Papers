# chart phi3v cross architecture

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_chart_phi3v_cross_architecture_20260519T184441_result.json`
- **Structured JSON:** [`5c7cbe6bb7bfdd9a2513.json`](../../sessions/5c/5c7cbe6bb7bfdd9a2513.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成并注册（`art_20260519_7fe815`）。

**数据概要：**
- **OpenVLA**: untrained 全部为 0 → trained 在 L0=20, L1=22 处出现强 entry spike，之后迅速衰减至 0
- **Phi3V**: untrained 已经在大部分层保持 28-32 的高水平（继承自 instruction tuning）→ trained 在 L1-L2 饱和到 32，但中间层大幅下降（dip 到 0-7），尾部逐步回升至 17-18

**输出文件：**
- 服务器: `/root/autodl-tmp/vla-ssd/results/figures/fig_cross_architecture_attention.{pdf,png}`
- 本地 artifacts: `fig_cross_architecture_attention.{pdf,png}`

---
