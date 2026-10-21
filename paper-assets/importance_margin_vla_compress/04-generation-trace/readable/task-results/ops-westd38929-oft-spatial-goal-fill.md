# ops westd38929 oft spatial goal fill

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-oft-spatial-goal-fill_20260521T022803_result.json`
- **Structured JSON:** [`919facda26f2fb5c3ea6.json`](../../sessions/91/919facda26f2fb5c3ea6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### Checkpoints — 已完成
- Spatial: 20G, 无 .aria2, unnorm_key = `libero_spatial_no_noops`
- Goal: 10G, 无 .aria2, unnorm_key = `libero_goal_no_noops`

### 脚本 — 无需修改
`eval_oft_libero.py` 已支持多 suite：`--checkpoint` 参数化，`--suite` 选择，unnorm_key 自动解析 (`{suite}` → `{suite}_no_noops`)

### 当前 GPU 状态

| GPU | Job | 进度 | 预估剩余 |
|-----|-----|------|----------|
| cuda:0 | random k=0.95 object | **Task 10/10** | ~20 min |
| cuda:1 | random k=0.7 object | Task 9/10 Ep10/50 | ~50 min |
| cuda:2 | OFT Object baseline | 刚启动 | 数小时 |
| cuda:3 | **OFT Goal baseline** | 刚启动 | 数小时 |

### 结论
- **OFT Goal baseline** — 已经在 cuda:3 上运行，无需操作
- **OFT Spatial baseline** — 所有 GPU 被占。cuda:0 (random k=0.95) 约 20 分钟后完成，到时可在 cuda:0 上提交 Spatial

需要我等 cuda:0 空出后自动提交 OFT Spatial baseline 吗？

---
