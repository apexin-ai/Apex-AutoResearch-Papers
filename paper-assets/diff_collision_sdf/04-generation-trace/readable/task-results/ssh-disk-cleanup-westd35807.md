# ssh disk cleanup westd35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_disk_cleanup_westd35807_20260520T065434_result.json`
- **Structured JSON:** [`762815596179aab0478f.json`](../../sessions/76/762815596179aab0478f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

## 清理结果

| | 清理前 | 清理后 |
|---|---|---|
| 已用 | 350GB (100%) | 254GB (73%) |
| 可用 | 1.3MB | **97GB** |

**已删除 (~96GB):**
- A1 旧 checkpoint: steps 1, 2, 500–4500, 5500 (~78GB)
- A1 不完整 checkpoint: tmp_6500 (4.6GB)
- A1 诊断文件: diag_dryrun2 (14GB)
- 空目录: diag_dryrun, test_dry, a3_grad_refine_spatial_bowl

**保留的 A1 checkpoint:** step 5000, 6000

---

## Baseline 空间评估 — **严重不足**

每个 baseline checkpoint = **19GB**，3 个 baseline 同时存档。

当前状态：
- 3 个 baseline 均在 step 8000，各存了 4 个 checkpoint（2000/4000/6000/8000）
- 已占用: 3 × 4 × 19GB = **228GB**

剩余需求（目标 30000 步，每 2000 步一存）：
- 还需保存 11 轮（step 10000–30000）
- 新增空间: 3 × 11 × 19GB = **627GB** — 远超可用 97GB

**现有 97GB 只够再存 ~5 个 checkpoint（约 1.7 轮），大约到 step 10000–12000 就会再次满盘。**

### 建议（需要你决策）

1. **清理 baseline 旧 checkpoint**：每个 baseline 只保留最新的 8000，删除 2000/4000/6000。释放 3×3×19 = **171GB**，加上已有 97GB = 268GB 可用。但仍只够 ~14 轮（到 step ~36000，刚好覆盖）。
2. **调大 save_interval**：从 2000 改为 5000 或 10000，大幅减少 checkpoint 数量。
3. **两者结合**（最稳妥）：清理旧 checkpoint + 加大 save_interval。

---
