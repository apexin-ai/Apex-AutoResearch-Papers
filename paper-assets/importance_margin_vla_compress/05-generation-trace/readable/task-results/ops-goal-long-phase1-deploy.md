# ops goal long phase1 deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_goal_long_phase1_deploy_20260522T093045_result.json`
- **Structured JSON:** [`064ff28c5ef4e857c60e.json`](../../sessions/06/064ff28c5ef4e857c60e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个进程都在 GPU 上正常运行。两个 baseline 已成功部署，正在初始化 LIBERO 环境。

## 脚本检查
- `--suite` 支持: `libero_object`, `libero_spatial`, `libero_goal`, `libero_10`
- `libero_goal` 支持: **是**，SUITE_CONFIG 已有，max_steps=400
- `libero_long` 支持: **否** — LIBERO 库中无此 suite。**`libero_10` 即 LIBERO-Long**（10 个长视野复合任务，max_steps=520）
- `--prune_mode none`: baseline 模式（不 patch embed_prefix，完整推理）

## 数据集检查

| 服务器 | bddl_files | init_files | datasets 目录 |
|--------|-----------|-----------|--------------|
| cqa1-33015 | libero_goal ✓ / libero_10 ✓ | libero_goal ✓ / libero_10 ✓ | 不存在（eval 不需要） |
| westd-27271 | ✓（同包） | ✓（同包） | `/root/autodl-tmp/libero_data/datasets/`（空） |
| westd-41074 | ✓（同包） | ✓（同包） | 仅 `libero_object` |

bddl_files 和 init_files 随 LIBERO 包安装，所有 suite 均可用于 eval（仿真环境，不需要 demo 数据）。

## Baseline 部署（cqa1-33015）

| GPU | 实验 | PID | 验证 |
|-----|------|-----|------|
| 0 | π0.5 baseline `libero_goal` seed42, 50eps/task | 329795 | ✅ GPU 9498MiB, 进程存活, 模型已加载 |
| 2 | π0.5 baseline `libero_10`(Long) seed42, 50eps/task | 330299 | ✅ GPU 9498MiB, 进程存活, 模型已加载 |
| 1 | （已有实验）l2norm k=0.9 object seed43 | 249668 | 运行中 |

命令：
- Goal: `--prune_mode none --suite libero_goal --n_episodes 50 --seed 42`
- Long: `--prune_mode none --suite libero_10 --n_episodes 50 --seed 42`

n_episodes=50 per task × 10 tasks = **500 total episodes**（与任务要求一致）。

## 后续 Phase 2 可行性
**能直接跑。** 脚本已支持 `libero_goal` 和 `libero_10`（Long），只需改 `--suite` 和 `--prune_mode`/`--keep_ratio` 参数即可跑 pruning 实验。无需修改脚本或下载数据。

---
