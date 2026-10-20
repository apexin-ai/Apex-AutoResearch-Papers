# figure fig2 legend fix v3

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig2-legend-fix-v3_20260524T141250_result.json`
- **Structured JSON:** [`f7dfa6d7505e65e964d1.json`](../../sessions/f7/f7dfa6d7505e65e964d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**方案**：选择了 `upper center` + `ncol=2`，图例横排居中在标题下方。

**具体参数**：
```python
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=2, frameon=False)
```

**判断依据**：位置 1 (No Trace) 和 2 (Full Trace) 的柱子仅到 ~82，上方到标题之间有大片空白。两端高柱 (Exception-Only ~99, VOTA ~84-99) 的 gap 标注不会与居中图例重叠。

已上传 `fig3_cross_model_gap_legend_v3.png` 到飞书。

---
