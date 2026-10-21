# ops verify checkpoint path 30k eval

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_checkpoint_path_30k_eval_20260525T094127_result.json`
- **Structured JSON:** [`9c6c5e2b7aefe9262643.json`](../../sessions/9c/9c6c5e2b7aefe9262643.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Checkpoint 核实结果

### Eval 进程命令行

**全部 4 个 eval 使用的是 `/best/` checkpoint，而非 `/30000/`：**

| Session | `--policy.dir` 实际值 | GPU | Port |
|---------|----------------------|-----|------|
| eval_s1_l005 | `.../seed1_l005/best` | cuda:0 | 8000 |
| eval_s1_l01 | `.../seed1_l01/best` | cuda:1 | 8001 |
| eval_s2_l005 | `.../seed2_l005/best` | cuda:2 | 8002 |
| eval_s2_l01 | `.../seed2_l01/best` | cuda:3 | 8003 |

注意：tmux session 名和日志文件名都带 `30k`（如 `/tmp/eval_30k_s1_l005.log`、输出路径 `30k_evals/`），但实际加载的模型路径是 `/best`。**命名具有误导性。**

### 目录内容

| Checkpoint 目录 | 子目录 |
|----------------|--------|
| seed0_l005 | `30000/` only |
| seed0_l01 | `30000/` only |
| seed1_l005 | `29999/`, `30000/`, `best/` |
| seed1_l01 | `29999/`, `30000/`, `best/` |
| seed2_l005 | `29999/`, `30000/`, `best/` |
| seed2_l01 | `29999/`, `30000/`, `best/` |

### Best checkpoint 对应的实际步数

从 `best_loss.txt` 读取（格式: loss step）：

| 模型 | best step | best loss |
|------|-----------|-----------|
| seed1_l005 | **16000** | 0.01143 |
| seed1_l01 | **16000** | 0.01168 |
| seed2_l005 | **10000** | 0.00874 |
| seed2_l01 | **10000** | 0.00911 |

### 模型文件差异

best/ 目录的 `model.safetensors` 与 30000/ 的大小不同，确认不是同一个文件：
- `best/model.safetensors`: 7,473,091,320 bytes（May 25 13:06 创建，是合并后的模型）
- `best/model_lora.safetensors`: 7,540,115,784 bytes
- `30000/model.safetensors`: 7,540,115,784 bytes

### 结论

**Reviewer 怀疑成立。当前 4 个 "30K eval" 实际加载的是 `/best/` checkpoint：**
- seed1 的 best = step **16000**
- seed2 的 best = step **10000**
- **没有一个在用 step 30000 的模型**

eval 目前正在运行中（s1_l005 跑到 ep 111/200，s2_l01 跑到 ep 97/200），结果将写入 `30k_evals/` 目录但实际评估的不是 30K checkpoint。这些结果作废，需要杀掉进程并用 `/30000` 路径重新启动。

---
