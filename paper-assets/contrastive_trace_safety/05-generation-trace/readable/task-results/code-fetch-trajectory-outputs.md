# code fetch trajectory outputs

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fetch_trajectory_outputs_20260519T071847_result.json`
- **Structured JSON:** [`eed9743e4df9780bec1e.json`](../../sessions/ee/eed9743e4df9780bec1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### 1. Caption 内容

> Aggregate probe score trajectories aligned to the commitment point (CP, vertical dashed line at $t - t_{\mathrm{CP}} = 0$). Each panel shows mean scores across test traces, with shaded bands indicating $\pm 1$ standard deviation. The HS probe (blue, solid) exhibits a sharper transition at CP than the text probe (orange, dashed) and crosses the 0.5 threshold (dotted horizontal line) at or before CP in three of four models.

### 2. Data JSON 格式确认

结构为 `{ model_name: { probe_type: { "steps": [...], ... } } }`，示例：

```json
{
  "R1-8B": {
    "hs": {
      "steps": [-73, -72, -71, -70, -69, -68, -67, -66, -65, ...],
      ...
    }
  }
}
```

格式正常，按模型 → 探针类型 → 步骤数组组织。

### 3. 文件存在性与大小

| 文件 | 大小 | 时间 |
|------|------|------|
| `fig_trajectory.pdf` | 24 KB | May 19 15:17 |
| `fig_trajectory.png` | 414 KB | May 19 15:17 |

两个文件大小合理，时间戳一致。

---
