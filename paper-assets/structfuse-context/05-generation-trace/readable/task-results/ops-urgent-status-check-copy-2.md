# ops urgent status check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_status_check_20260514T161829_result.json`
- **Structured JSON:** [`77c9ebe64441b68c0561.json`](../../sessions/77/77c9ebe64441b68c0561.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。以下是报告。

---

## 检查 1: GPU 使用状态

```
GPU 0 (GPU-41b1...d04): utilization=100%, memory=50481/97887 MiB (51.6%)
  └─ PID 337271 占用 50472 MiB — m2_full_qwen (random_s43) 训练进程

GPU 1 (GPU-d831...181): utilization=100%, memory=55407/97887 MiB (56.6%)
  └─ PID 76627 占用 55398 MiB — m2_full_starcoder (random_s42) 训练进程
```

两块 GPU 均 100% 利用率，各被一个训练进程独占。

---

## 检查 2: m2_full_qwen (random_s43)

**tmux session**: `m2_qwen_s43` — 存在  
**进程状态**: PID 337271 存活，CPU 96%，wandb PID 338192 也在  
**父进程**: PID 337267 (`bash run_m2_full_qwen.sh`) 存活

**训练进度** (tmux 输出):
```
  New best R@1=0.5357, saved to .../m2_full_qwen/random_s43/best_by_recall_at_1
  step 550  loss=0.2363  lr=1.95e-05
  step 600  loss=0.2311  lr=1.92e-05
  ...
  step 1000  loss=0.2950  lr=1.63e-05
  [eval@1000] val_loss=0.4638, R@1=0.5285, R@5=0.9672, R@10=1.0
  val_loss not improved (1/2)
  step 1050  loss=0.3190
  ...
  step 1200  loss=0.0518  lr=1.42e-05
```

- 当前约 step 1200，lr 在衰减中
- 最佳 R@1=0.5357（step 500 eval），step 1000 eval 降到 0.5285，early stopping 计数 1/2
- 状态：**正常运行中**

---

## 检查 3: m2_full_starcoder

**tmux sessions**: `m2_full_starcoder` 和 `m2_starcoder_s43` 均存在但 pane 为空（输出重定向到日志）  
**进程状态**: PID 76627 存活，CPU 87.6%，已运行 1146 分钟（~19 小时）  
**watcher**: PID 309679 正在等 76627 结束后自动启动 s43+

**训练进度** (从 `/root/runs/structfuse-context/m2_full_starcoder.log`):
```
  step 3500  [eval] val_loss=0.6588, R@1=0.4534, R@5=0.9057, R@10=1.0
  val_loss not improved (5/0)
  ...
  step 4000  loss=0.0636  lr=2.07e-07
```

- 当前 step 4000，lr 已接近 0（2.07e-07），处于训练末期
- R@1=0.4534（明显低于 Qwen 的 0.5357）
- early stopping 计数显示 5/0 — **patience 已用完但训练仍在继续**（可能 patience 设置不同或按 epoch 结束）
- 状态：**正常运行中，接近训练结束**

---

## 检查 4: m1_reextract_v2

**tmux session**: `m1_reextract_v2` — 存在  

**输出** (最后几行):
```
2026-05-15 00:18:35 [INFO] batch_extract: [facebookresearch__fvcore.a491d5b9.combine_module__97dqxr34] CodeQL call_graph: 63 entries, 12 reachable files
2026-05-15 00:18:44 [INFO] batch_extract: [...combine_module__9k8jf7ll] CodeQL call_graph: 63 entries, 12 reachable files
2026-05-15 00:18:53 [INFO] batch_extract: [dask__dask.5f61e423.func_pm_ctrl_shuffle__7zq2s7en] CodeQL call_graph: 196 entries, 70 reachable files
2026-05-15 00:18:54 [INFO] [...combine_module__a7pzqf5f] 63 entries, 12 reachable files
2026-05-15 00:19:05 [INFO] [...combine_module__bf810te8] 87 entries, 12 reachable files
2026-05-15 00:19:15 [INFO] [...combine_module__bkx3meqi] 63 entries, 12 reachable files
```

- 正在处理 `facebookresearch__fvcore` 和 `dask__dask` 仓库的 CodeQL call_graph 提取
- 最后一条日志时间 00:19:15（约 5 分钟前），间隔 ~10 秒/样本
- 状态：**正常运行中**

---

## 异常/注意事项

1. **m2_full_starcoder (s42)** 的 `val_loss not improved (5/0)` 看起来 patience 已耗尽，但进程仍在跑到 step 4000 且 lr 接近 0，可能即将自然结束。watcher 进程已就绪，会在 s42 结束后自动启动 s43。
2. **m2_starcoder_s43** 的 tmux session 已创建但还是空的——符合预期，等 s42 跑完才会开始。
3. 无异常崩溃或错误信息。

---
