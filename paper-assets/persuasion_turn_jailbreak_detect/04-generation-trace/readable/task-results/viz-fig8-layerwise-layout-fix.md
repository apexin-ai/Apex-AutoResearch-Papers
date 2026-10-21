# viz fig8 layerwise layout fix

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fig8_layerwise_layout_fix_20260524T092324_result.json`
- **Structured JSON:** [`05ebc5d73664b2f9f99f.json`](../../sessions/05/05ebc5d73664b2f9f99f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个布局问题已修复：

1. **(a) "Late layers" 文字**：ylim 从 11.5 扩到 13.0，文字现在在数据线上方空白区域，不再被 vanilla 在 layer 10 的峰值（9.70）遮挡
2. **(b) "15× vanilla" 注释**：从右上角 (7.5, 12.5) 移到左侧空白区域 (3.0, 11.5)，箭头指向 layer 10 的数据点
3. **图例**：从两个 panel 各自的内置图例改为顶部统一图例，4 个 variant 横排显示，不与任何元素重叠

PDF 和 PNG 已复制到本地 `docs/paper/figures/paper/`。

---
