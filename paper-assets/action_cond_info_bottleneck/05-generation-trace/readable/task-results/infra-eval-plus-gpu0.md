# infra eval plus gpu0

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_eval-plus-gpu0_20260515T174849_result.json`
- **Structured JSON:** [`1e844531fa430ea1d1c5.json`](../../sessions/1e/1e844531fa430ea1d1c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Log last modified at 01:56 but process still running at 78% CPU with 5443 MiB GPU. Output is likely buffered (Python block-buffers through pipes). The eval is running.

---

## 汇报

### 1. n_episodes 语义：**per task**
`eval_policy_all` 遍历 `{suite: {task_id: vec_env}}`，对每个 task 调用 `eval_one(n_episodes=50)`。所以 `--eval.n_episodes=50` = 50 episodes/task = 500 episodes/suite（10 tasks）。当前设置正确。

### 2. GPU 0 eval (baseline_plus)：已启动
- PID 73475, `libero_spatial` suite 运行中
- GPU 0: 5443 MiB, 78% CPU — 在跑 episodes
- 模型已缓存（411 files 瞬间完成）
- 脚本：`/root/acib/scripts/run_eval_plus_gpu0.sh`
- 输出：`/root/acib/outputs/baseline_plus/`
- 4 个 suite 按顺序跑：spatial → object → goal → libero_10
- 预计每 suite 数小时（500 episodes），总共 ~8-16 小时

### 3. 数据集下载
- `lerobot/libero` dataset: PID 44582 运行中，340MB 已下载（457 files 中约 84%）
- 下载目标：`/root/autodl-tmp/libero_dataset`

### 4. GPU 1 eval (baseline_std)
- **第一次运行（01:27-01:29）失败**：全部 4 suite 报 `ModuleNotFoundError: robosuite`
- **第二次运行（01:41 起）**：robosuite 已装好，当前在跑 `libero_10`（PID 76957）
- 但无 `eval_info.json` 产出——前面 3 个 suite (spatial/object/goal) 似乎跑完了但没生成结果文件
- GPU 1 当前 3 MiB（模型在 suite 间卸载/重载中）
- **注意**：EGL cleanup errors 频繁出现（`EGLGLContext.__del__`），虽然是 "Exception ignored"，可能影响结果写入

### 5. Registry
- `mvp1_baseline_plus` 已更新为 RUNNING，gpu=cuda:0

---
