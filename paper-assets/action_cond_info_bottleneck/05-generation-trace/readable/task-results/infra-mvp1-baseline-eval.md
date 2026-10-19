# infra mvp1 baseline eval

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_mvp1-baseline-eval_20260515T170211_result.json`
- **Structured JSON:** [`8b3ce23a17d6e252694a.json`](../../sessions/8b/8b3ce23a17d6e252694a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both processes running. Here's the full status:

---

**汇报:**

### Eval 启动状态
- **运行中** — PID 41715, GPU 1 (5.4 GB VRAM), 130% CPU
- 当前 suite: `libero_spatial` (50 episodes × 10 tasks)
- 4 suites 顺序执行: spatial → object → goal → 10
- 输出缓冲中（episodes 完成后才打印），预计每 task ~12-15 min
- 需要修复的依赖问题: robosuite 缺失 → 1.4.0, libero assets 缺失 → sparse git checkout + symlink, 缺少 easydict/hf-egl-probe/thop

### 模型下载
- **完成** — `lerobot/smolvla_libero` (906 MB) via aria2c 16 connections, HF cache 完整

### 数据集下载
- **进行中** — PID 44581, 457 files via `snapshot_download`
- 已有: 34 parquet + meta (2.3 GB), 总计 ~36 GB
- 当前速度 ~1.5 files/s（小文件阶段）

### EGL
- 已解决 — `MUJOCO_GL=egl PYOPENGL_PLATFORM=egl` 在 `run_eval_std.sh` 中设置

### GPU 0 ACIB 训练
- **已完成** — 5000 步, checkpoint-2500 和 checkpoint-5000 已保存
- 配置: β=0.1 (无 warmup), batch_size=8, hidden_dim=64
- 已知问题: scorer collapsed (scorer_mean≈0.8, sparsity=0) — 验证了 β warmup fix 的必要性

### 代码部署
- ✅ `train_acib.py` (β warmup fix)
- ✅ `config_h64.yaml`, `config_h128.yaml` (β=0.01, beta_warmup_steps=1000, batch_size=64)

### 待关注
- numpy 被降级到 1.26.4 (lerobot 要求 >=2.0.0) — 目前 eval 正常运行
- 等 eval 首个 suite 结果出来确认数值合理性

---
