# paper r26 fig5 hatch

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r26_fig5_hatch_20260522T084215_result.json`
- **Structured JSON:** [`c802a7814ad800742c59.json`](../../sessions/c8/c802a7814ad800742c59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### Hatch pattern 分配

| Category | Hatch | 示例 bar |
|----------|-------|---------|
| baseline | 无 (实色) | No filter, DSIR |
| alternative | `//` (斜线) | Surprisal selection, Graduated weighting |
| ours | `xx` (交叉) | Binary K* filtering |

### 脚本修改 diff

3 处改动：

1. **新增 `category_hatches` 字典** — 在 `colors` 列表后，定义每个 category 对应的 hatch pattern
2. **bar 创建后应用 hatch** — `edgecolor` 从 `"white"` 改为 `"#555555"`（使 hatch 线条可见），并逐 bar 设置 `set_hatch()`
3. **图例同步更新** — legend Patch 加上对应 hatch 和新 edgecolor

新图已覆盖 `artifacts/figures/` 和 `docs/paper/figures/` 中的 PDF/PNG。

---
