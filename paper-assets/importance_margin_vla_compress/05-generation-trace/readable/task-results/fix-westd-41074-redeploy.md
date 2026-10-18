# fix westd 41074 redeploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd-41074-redeploy_20260523T145924_result.json`
- **Structured JSON:** [`a03d52ac97926f29cd14.json`](../../sessions/a0/a03d52ac97926f29cd14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**任务实际无需执行——4 个实验已在 westd-41074 正常运行**

### 现状
| GPU | 实验 | PID | 进度 | 运行时长 |
|-----|------|-----|------|----------|
| 0 | k=0.95 | 124997 | T0 30 ep / 83% | 6:07 |
| 1 | k=0.7 | 125142 | T0 30 ep / 87% | 6:03 |
| 2 | k=0.3 | 125328 | T0 40 ep / 88% | 5:59 |
| 3 | k=0.9 | 125577 | T0 30 ep / 67% | 5:55 |

### 关键发现
- **PID 120874 是 defunct `cat` 进程**（非训练进程），无需 kill
- **PI05 模型从本地路径加载** (`/root/autodl-tmp/pi05_libero_finetuned`)，不依赖在线 paligemma tokenizer 下载，网络问题对实验无影响
- **Registry 4 个 exp 已是 RUNNING 状态**，hypothesis 已正确设置
- 日志位置：`/root/runs/importance_margin_vla_compress/eval_pi05_random_k0{X}_goal_seed42_v2.log`

GPU 利用率 18-52%，正常推理中。预计每个 suite 50 ep × 10 task ≈ 60-90 分钟完成。

---
