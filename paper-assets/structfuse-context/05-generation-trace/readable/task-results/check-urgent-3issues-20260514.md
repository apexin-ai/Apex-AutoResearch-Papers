# check urgent 3issues 20260514

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_urgent_3issues_20260514_20260514T190956_result.json`
- **Structured JSON:** [`28a9b8e5777ef15a4c4c.json`](../../sessions/28/28a9b8e5777ef15a4c4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 问题 1：Qwen chain 状态

### 1a. 进程

`ps aux` 中相关进程：
- **PID 73543** — 原始 tmux session `m2_full_qwen`（May 13 启动）
- **PID 966920** — `bash /root/structfuse/watch_and_chain_qwen_s42.sh`（May 14 启动，pts/0）
- **PID 504138** — GPU 0 上的 python 训练进程，占用 **50632 MiB** VRAM

`pstree` 被 read-only 白名单拦截。

### 1b. output 目录

```
/root/autodl-tmp/structfuse/full_m2_outputs/
total 0
drwxr-xr-x 2 root root 31 May 14 00:59 random_s42
```

仅一个子目录，来自初始被 kill 的那次运行。

### 1c. 产出文件

```
/root/autodl-tmp/structfuse/full_m2_outputs/random_s42/train.log
```

仅一个 log，无 .pt / .json / .safetensors。

### 1d. chain 脚本 (`run_m2_full_qwen.sh`)

- `OUT_BASE="/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen"` ← **主输出路径**（不在 `full_m2_outputs`）
- `TRAIN_SCRIPT="/root/structfuse-context/training/train.py"`
- STRATEGIES: random / embedding_distance / dataflow_aware, SEEDS: 43 44 = 6 runs
- 追加 bm25_s42 = **共 7 runs**（TOTAL_RUNS 变量写的 9，实际 7）
- LOG_DIR: `/root/runs/m2_full_qwen/`

### 1e. `/root/runs/structfuse-context/m2_full_qwen.log`

```
==========================================
[1/9] Starting: random_s42 at Thu May 14 01:39:30 CST 2026
==========================================
EXIT_CODE=0
```

这是原始 tmux wrapper 的 log，session 已退出（exit code 0）。

### 1f. 其他 log

- `/root/runs/structfuse/ ` 下无 `run_m2_full_qwen*.log`
- `/tmp/` 下找到：`/tmp/model_download_qwen.log`、`/tmp/agent-ml-exit/m2_full_qwen.exit`、`/tmp/edit_qwen.py`

**exit 文件内容**：`0|2026-05-14T11:17:27Z`（原始 tmux session 在 5/14 19:17 CST 退出，code 0）

### 1g. GPU 0 进程

```
504138, python, 50632 MiB
```

**PID 504138 的 cmdline**：
```
python /root/structfuse-context/training/train.py
  --train-file .../train_random_s44.jsonl
  --val-file .../val_random_s44.jsonl
  --output-dir /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44
  --hard-negative-strategy random --seed 44
  --batch-size 8 --num-epochs 2 --eval-steps 500
```

### 1h. wandb

`full_m2_outputs/` 下无 wandb runs（因为实际输出在 `checkpoints/m2_full_qwen/`）。

### 实际 chain 进度（`/root/runs/m2_full_qwen/s43plus_all.log`）

| Run | Status | 关键指标 |
|-----|--------|---------|
| **1/9 random_s43** | ✅ DONE (May 14 19:24 → May 15 01:58) | Early stopped @step 1500, best val_loss=0.4476 @500, best R@1=0.5554 |
| **2/9 random_s44** | 🔄 IN PROGRESS | Step 350, loss=0.2364, lr=2e-5（健康下降中） |
| 3-7 | ⏳ pending | embedding_distance_s43/s44, dataflow_aware_s43/s44, bm25_s42 |

### Checkpoint 目录

```
/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/
  random_s42/  → best_by_val_loss/ best_by_recall_at_1/ final/  ✅
  random_s43/  → best_by_val_loss/ best_by_recall_at_1/ final/  ✅
  random_s44/  → (empty, training in progress)
```

### Watcher (`watch_and_chain_qwen_s42.sh`, PID 966920)

监视 PID 337267（已不存在）。`kill -0 337267` 应该立即 fail，所以 while 循环已退出。Watcher 应该已经开始执行 `run_m2_s42_supplement.sh`，但 `/root/runs/m2_full_qwen/` 下无 `s42_supplement.log`，且 GPU 0 被 random_s44 占用。Watcher 可能正在等待 conda activate 或已静默失败。

### 结论

**Qwen chain 未卡住。** GPU 0 上 random_s44 正在训练（step 350/~2816），loss 健康下降。2/7 runs 已完成，5 runs 待完成。

---

## 问题 2：m1_reextract_v2 输出路径

### 2a. 完整命令行

```
python extraction/batch_extract.py
  --metadata /tmp/m1_failed_metadata.jsonl
  --output-dir /root/autodl-tmp/structfuse/full_m1_data
  --repos-dir /root/autodl-tmp/structfuse/full_m1_data/repos
  --workers 4 --timeout 300 --python-only
  --skip-log /root/autodl-tmp/structfuse/full_m1_data/skip_log_rerun.jsonl
```

多个子进程活跃（PID 209821/209824/209825），多个 CodeQL java 进程正在跑。

### 2b. 输出文件

```
/root/autodl-tmp/structfuse/full_m1_data/all.jsonl  (6.56 GB, modified May 13 18:46)
```

`/root/structfuse/` 下无 all.jsonl / recovered.jsonl。

### 2c. m1_reextract_v2.log 最后 10 行

```
2026-05-15 03:09:33 [INFO] [Project-MONAI__MONAI...] CodeQL call_graph: 2331 entries, 283 reachable files
2026-05-15 03:09:45 [INFO] [facebookresearch__hydra...] CodeQL call_graph: 22 entries, 10 reachable files
2026-05-15 03:09:47 [INFO] [dask__dask...] CodeQL call_graph: 342 entries, 82 reachable files
2026-05-15 03:09:57 [INFO] [facebookresearch__hydra...] CodeQL call_graph: 132 entries, 26 reachable files
2026-05-15 03:10:08 [INFO] [facebookresearch__hydra...] CodeQL call_graph: 76 entries, 28 reachable files
2026-05-15 03:10:11 [INFO] [conan-io__conan...] CodeQL call_graph: 147 entries, 66 reachable files
2026-05-15 03:10:19 [INFO] [facebookresearch__hydra...] CodeQL call_graph: 285 entries, 44 reachable files
2026-05-15 03:10:30 [INFO] [facebookresearch__hydra...] CodeQL call_graph: 43 entries, 21 reachable files
2026-05-15 03:10:41 [INFO] [facebookresearch__hydra...] CodeQL call_graph: 200 entries, 40 reachable files
2026-05-15 03:10:46 [INFO] [dask__dask...] CodeQL call_graph: 796 entries, 172 reachable files
```

**活跃运行中**，最新日志时间 03:10（几分钟前）。

---

## 问题 3：tmux watcher 状态

### 3a. tmux ls

```
TMUX_BLOCKED — 'tmux' is not allowed in read-only mode
```

### 3b. tmux capture-pane

同样被拦截，无法执行。

**结论**：`tmux ls` 和 `tmux capture-pane` 均被 `ssh_read_only` 白名单阻止，需要 `ssh_execute` 才能查看 tmux sessions。

---
