# fix eval and training check

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval_and_training_check_20260516T031649_result.json`
- **Structured JSON:** [`8adaa7724d8579b37204.json`](../../sessions/8a/8adaa7724d8579b37204.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Part A: 训练状态

| 训练 | PID | GPU | 当前 step | 总 steps | 进度 | final/ checkpoint | 状态 |
|------|-----|-----|-----------|----------|------|-------------------|------|
| visual | 370295 | cuda:0 | 8,400 | 30,000 | 28% | 无 | **running** |
| physical | 370372 | cuda:1 | 8,150 | 30,000 | 27% | 有（旧 run，10:02） | **running** |
| universal_r16 | 370451 | cuda:2 | 8,250 | 30,000 | 28% | 有（旧 run，10:03） | **running** |
| universal_r48 | 370656 | cuda:3 | 8,200 | 30,000 | 27% | 无 | **running** |
| spatial | — | — | — | — | — | 有（旧 run，09:54） | 未在训练 |

- 4 个 tmux session 都活着，进程运行 ~52 分钟
- GPU 利用率 0-2%（step 间歇），VRAM ~8.2GB/卡
- physical/universal_r16/spatial 的 `final/` 是上一轮 run 的产物（创建时间早于当前 tmux session 10:26），当前 run 还在跑
- 预计完成：~18s/step × 21,800 remaining steps ≈ 109 小时（~4.5 天）

---

## Part B: eval 扰动筛选

`get_tasks_by_perturbation` **已在当前代码中正确实现**，不需要额外修复。

验证结果（`libero_object` suite）：

| 扰动类型 | 筛选任务数 | 与 JSON 一致 |
|----------|-----------|-------------|
| camera_viewpoints | 396 | ✓ |
| light_conditions | 297 | ✓ |
| background_changes | 248 | ✓（alias → Background Textures） |
| background_textures | 248 | ✓ |
| sensor_noise | 422 | ✓ |
| objects_layout | 403 | ✓ |
| robot_initial_states | 398 | ✓ |
| nominal | 10 | ✓（base BDDL 文件） |

函数通过 `PERTURBATION_TO_JSON_CATEGORY` 映射 → 从 `task_classification.json` 按 category 过滤 → 在标准 benchmark 中定位索引。原描述的 `f"{task_suite}_{perturbation_type}"` 拼接 bug 已被此实现替代。

---
