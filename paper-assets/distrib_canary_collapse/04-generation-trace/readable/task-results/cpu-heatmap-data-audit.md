# cpu heatmap data audit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_heatmap-data-audit_20260521T184750_result.json`
- **Structured JSON:** [`14d9ebdc72cbc7202004.json`](../../sessions/14/14d9ebdc72cbc7202004.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。结果摘要：

**实际完成 15/20 格（非 13/20）**，5 格 RUNNING。所有 PermG 值已通过 5method_leadlag.json 文件交叉验证，与 registry 一致。

### Heatmap Grid (PermG fwd /8)

| T\α | 0.45 | 0.50 | 0.60 | 0.75 |
|-----|------|------|------|------|
| T=5 | 0 | 0 | 0 | 0 |
| T=10 | 0 | 6 | 0 | 6 |
| T=15 | 6 | 6 | 0 | **RUNNING** |
| T=20 | 5 | 6 | 0 | 6 |
| T=25 | **RUNNING** | **RUNNING** | **RUNNING** | **RUNNING** |

### 关键发现

1. **数据分布在 3 个不同路径**：T=5/T=15/T=25 在 `phase_diagram/`，T=10 在 `alpha_sweep/`，T=20 在 `t20/`
2. **跨 2 台服务器**：T=15 α=0.45 和 T=25 α=0.75 在 westd-19828，其余在 westd-17855
3. **α=0.60 列全零**：所有已完成的 T 值均 PermG=0/8（sync-dip structural）
4. **现有 heatmap 脚本** `phase_diagram_draft.py` 缺少 T=15 α=0.60 数据点，需更新
5. **T=25 进度**：4 个格子均在 14-15/26 gens 左右

Manifest 已写入 `artifacts/heatmap_data_manifest.json` 并注册，包含 `heatmap_grid.matrix` 可直接用于绘图。

---
