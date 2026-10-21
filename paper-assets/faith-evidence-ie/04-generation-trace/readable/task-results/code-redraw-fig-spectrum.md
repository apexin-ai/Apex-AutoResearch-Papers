# code redraw fig spectrum

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_redraw-fig-spectrum_20260523T140419_result.json`
- **Structured JSON:** [`c79db9f0d42614dc885b.json`](../../sessions/c7/c79db9f0d42614dc885b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

fig_spectrum 重绘完成。所有标签清晰无重叠，数据点正确。

输出文件已保存到：
- `artifacts/fig_spectrum.pdf` / `.png`
- `figures/paper/fig_spectrum.pdf` / `.png`
- 服务器 `/root/autodl-tmp/freige/artifacts/fig_spectrum.pdf` / `.png`

变更要点：
- 坐标轴交换：x=Rel-F1, y=Evi-F1 (TP)
- DPO 1ep (33.38, 80.90) 和 DPO 3ep (31.45, 84.84) 均为实心标记，无 "†"
- "gradual decay" 箭头从 DPO 1ep 指向 DPO 3ep（Rel-F1 单调下降）
- RSFT CED 改为 3-seed mean 单点
- GRPO bf16 改为 step 100 单点（移除 trajectory）

---
