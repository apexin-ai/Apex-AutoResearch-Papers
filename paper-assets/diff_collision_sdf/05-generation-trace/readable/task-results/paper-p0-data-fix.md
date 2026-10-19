# paper p0 data fix

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_p0-data-fix_20260528T040250_result.json`
- **Structured JSON:** [`20c098d80b47f401fa10.json`](../../sessions/20/20c098d80b47f401fa10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 最终报告

**修改文件：**
1. `docs/paper/appendix.tex` L271 — SDF λ=0.1 s0 seed=7 行：`48 & 74 & 72 & 34 & 57.0` → `60 & 74 & 68 & 30 & 58.0`
2. `docs/paper/appendix.tex` L275 — mean±std 行重算（见下）
3. `artifacts/fig_pertask_car_fingerprint.py` L27 — LoRA s0 数据：`{'CP': 74, 'Milk': 66, 'OJ': 68, 'BBQ': 20}` → `{'CP': 74, 'Milk': 70, 'OJ': 56, 'BBQ': 26}`

**重算的 mean±std（4 seeds: 7/42/123/256）：**

| | OJ | CP | Milk | BBQ | Agg |
|---|---|---|---|---|---|
| 旧值 | 58.5±7.2 | 74.0±1.6 | 71.5±3.8 | 27.5±5.4 | 57.9±1.0 |
| 新值 | 61.5±1.9 | 74.0±1.6 | 70.5±4.1 | 26.5±4.1 | 58.1±0.9 |

**PDF 编译：** 成功，17 页，579,350 bytes
**paper_switch.py --verify：** Scenario B (10/10 OK)，Scenario C (11/11 OK)，全部通过

---
