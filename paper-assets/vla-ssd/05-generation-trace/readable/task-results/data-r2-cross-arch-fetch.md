# data r2 cross arch fetch

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_r2_cross_arch_fetch_20260520T033224_result.json`
- **Structured JSON:** [`5fedb25a357c3915a0ae.json`](../../sessions/5f/5fedb25a357c3915a0ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 报告

| 模型 | 层数 | Seeds | R² Peak 层 | Peak 值 |
|------|------|-------|-----------|---------|
| **OpenVLA** | 33 (L0-L32) | 15 | **L9** | 0.637 ± 0.008 |
| **TracVLA-Phi3V** | 33 (L0-L32) | 5 | **L11** | 0.634 ± 0.007 |

关键差异：
- OpenVLA 的 R² 在浅层（L0-L9）就达到 peak 后逐层下降，深层（L25+）跌至 ~0.53
- Phi3V 从 L0 的负值（-0.329）起步，逐层上升至 L11 达到 peak，之后保持高位平台（L11-L21 约 0.62-0.63），深层衰减更温和（L32 仍有 0.554）

### 文件路径
- Phi3V JSON: `artifacts/phi3v_r2_action_probe/phi3v_r2_per_layer.json`
- OpenVLA JSON: `artifacts/phi3v_r2_action_probe/openvla_r2_per_layer.json`
- LaTeX 表格: `artifacts/phi3v_r2_action_probe/cross_arch_r2_table.tex`

---
