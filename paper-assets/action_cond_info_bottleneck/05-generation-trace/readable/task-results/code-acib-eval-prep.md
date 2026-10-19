# code acib eval prep

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_acib-eval-prep_20260516T044111_result.json`
- **Structured JSON:** [`8ae24be4e29d335b4733.json`](../../sessions/8a/8ae24be4e29d335b4733.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出汇总

### 1. eval_acib.py 可用性: **Y**

脚本完整可用，支持所有需要的参数：`--checkpoint_dir`, `--base_model`, `--suites`(支持多 suite 一次跑), `--n_episodes`, `--gpu`, `--out_dir`, `--seed`。跨 suite 复用 policy 缓存，无需重复加载。

### 2. 无需修改

### 3. 命令模板已写入
`artifacts/eval_seed1_commands.sh`，含 3 种方式：
- **Option A**: 一条命令跑全部 4 suites（推荐）
- **Option B**: 单独 suite 命令
- **Option C**: nohup 后台运行

### 4. 时间预估

每 suite 50 episodes（10 tasks × 5 episodes）。参考当前 baseline eval（libero_10 已跑 3.3h+ 仍未完成），ACIB eval 有额外 bottleneck forward 但模型规模相同。保守估计：
- 每 suite: **1.5–3 小时**
- 4 suites 串行: **6–12 小时**

### 5. Checkpoint 状态

| 路径 | 状态 |
|------|------|
| `checkpoint-5000` | ✓ 已存在 |
| `checkpoint-10000` | ⏳ 即将生成（当前 step 9900） |
| `checkpoint-15000` | 未到 |
| `checkpoint-20000` (final) | 未到 |

### ⚠️ 时间修正

seed1 训练**并非** ~07:45 UTC 完成。当前状态：
- **Step 9900/20000**，速度 0.9 steps/s
- 剩余 ~10,100 steps ÷ 0.9 ≈ 11,222 秒 ≈ **3.1 小时**
- **预计完成时间: ~15:50 UTC（今天）**

### GPU 状态

| GPU | 占用 | 进程 |
|-----|------|------|
| 0 | 21.5GB/97.9GB | seed1 训练 (16GB) + baseline_plus eval (5.3GB) |
| 1 | 22.8GB/97.9GB | seed2 训练 (16GB) + 另一个 eval (6.6GB) |

训练完成后 GPU 0 释放 ~16GB，剩余 baseline eval 可能仍在跑。97GB 显存足够同时运行 eval。启动前需按 C001 检查并 kill seed1 训练残留进程。

---
