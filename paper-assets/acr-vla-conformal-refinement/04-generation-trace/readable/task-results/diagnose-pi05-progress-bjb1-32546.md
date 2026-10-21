# diagnose pi05 progress bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-progress-bjb1-32546_20260521T110131_result.json`
- **Structured JSON:** [`281a006c86d332bc29aa.json`](../../sessions/28/281a006c86d332bc29aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

**6 个进程全部已死，所有 GPU 空闲。**

### 进程/GPU 状态
- `ps -p 982849,983128,983472,983816,984171,984515` 返回 exit 1（无匹配）
- 所有 6 张 GPU 利用率 0%，显存 1 MiB / 24564 MiB

### 实验结果
| 实验 | 进度 | SR |
|---|---|---|
| object-seed{42,43,44} | 10/10 tasks 完成 (EXIT_CODE=0) | **0.0% (0/200)** ×3 |
| spatial-seed{42,43,44} | 8 task 完成 + 第 9 task 10/20 处崩溃 | 0.0% (无 EXIT_CODE) ×3 |

### Fix 状态：**部分生效，但仍然失败**
- ✅ `[pi05] Fixed 437 vision tower keys` — vision_tower remap 已部署生效
- ❌ `[pi05] Vision tower missing_keys (376)` — **multi_modal_projector + 整个 language_model 仍 missing**
- 结果：vision tower 加载真实权重，但 **language_model 在随机权重下运行** → 0% SR

### 关键发现
- 故障模式不是预想的"vision tower 随机"，而是 **language_model 命名不匹配 checkpoint**，376 key 仍 missing
- spatial 三个实验都在完全相同位置死亡（task 9 rollout 10/20），且 `/root/miniconda3/lib/python3.12/site-packages/lerobot/policies/pi05/modeling_pi05.py` 文件 mtime 是 18:59（spatial 死后 ~4 分钟）→ 高度怀疑 lerobot pip 重装导致进程崩溃
- 路径修正：模型在 python3.12 下（不是 3.11），路径为 `lerobot/policies/pi05/`（不是 `lerobot/common/policies/pi0/`）

详细 summary 已写入 `artifacts/pi05_vla_only_eval_progress_20260521.md`。需修复 376-key remap（追加 `language_model.*` 和 `multi_modal_projector.*` 的 remap 逻辑）后重启全部 6 个实验。

---
