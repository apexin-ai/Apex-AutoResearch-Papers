# code scaling curve precheck

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scaling-curve-precheck_20260519T192719_result.json`
- **Structured JSON:** [`790ac4d538336ca622c6.json`](../../sessions/79/790ac4d538336ca622c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**预检结果：PASS**

| 检查项 | 结果 |
|--------|------|
| 正常生成 PDF/PNG（4 组图） | PASS — 无报错，4 组 ×2 格式全部生成 |
| X 轴对数刻度 | PASS — log scale，刻度标注 4B/7B/8B/14B/32B/72B |
| 8B FT + 72B ZS 数据点正确 | PASS — 实线 vs 虚线区分 regime，三色区分 dataset |
| 多数据集分色分标记 | PASS — SciERC(蓝圆)/FewNERD(橙三角)/CoNLL(绿菱) |
| None placeholder 跳过 | PASS — `_extract` 过滤 None，7B/14B/32B 全 None 不报错不渲染 |
| 填入新数据点后兼容 | PASS — 添加 fake 7B FT 后 3 点正常连线渲染 |

预览图已存至 `artifacts/scaling_curve_draft_preview.png`（2点）和 `artifacts/scaling_curve_draft_3pt_preview.png`（3点）。脚本无需修复。

---
