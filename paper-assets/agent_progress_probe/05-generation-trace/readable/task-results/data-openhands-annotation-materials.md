# data openhands annotation materials

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_openhands-annotation-materials_20260514T124009_result.json`
- **Structured JSON:** [`8d1289954ab4c248989a.json`](../../sessions/8d/8d1289954ab4c248989a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

**数据分布**
| 类别 | 数量 | 占比 |
|------|------|------|
| progress (label=1) | 119,212 | 77.0% |
| stagnation (label=0) | 31,440 | 20.3% |
| tie (label=-1) | 4,091 | 2.6% |

**Confidence 交叉分布** — stagnation 在 conf≥2 有 8,626 条，conf=3 有 900 条；progress 在 conf=3 仅 102 条。

**抽样结果** — 50 条全部来自 confidence=3（最高质量），25 stagnation + 25 progress 完全均衡。

**输出文件**
- 标注材料: `annotation_materials/openhands_samples.jsonl` — 每条含 window_id, source="openhands", instance_id, actions(原始对话文本), 空白标注字段
- 抽样统计: `annotation_materials/openhands_sampling_stats.json`
- 抽样脚本: `prepare_openhands_annotation.py`

---
