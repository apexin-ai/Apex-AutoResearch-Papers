# ops pre check next experiments

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pre-check-next-experiments_20260516T032517_result.json`
- **Structured JSON:** [`c43c7f844cae255e8119.json`](../../sessions/c4/c43c7f844cae255e8119.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### 1. smolvla_libero_plus 缓存
**已缓存。** 完整 snapshot 存在（model.safetensors + configs + preprocessors），blobs 目录齐全。后续实验可直接离线加载。

### 2. ACIB-H dry-run
**成功。** `--mode hard` 全流程跑通：
- 参数解析 → 模型加载 → 数据集加载 → 1 步训练 → checkpoint 保存
- 输出确认：`Starting ACIB-HARD training`，所有超参数正确传递
- 450M 参数，22.2% trainable，bfloat16

### 3. eval_acib.py 参数
| 参数 | 类型 | 说明 |
|------|------|------|
| `--checkpoint_dir` | **必须** | 训练输出目录 |
| `--checkpoint_step` | 可选 | 指定 step，默认最新 |
| `--base_model` | 可选 | base SmolVLA model id |
| `--suites` | 可选，多值 | 评测 suite |
| `--gpu` | 可选 | GPU 编号 |
| `--n_episodes` | 可选 | 评测 episode 数 |
| `--out_dir` | **必须** | 结果输出目录 |
| `--seed` | 可选 | 随机种子 |

### 4. 阻塞问题
**无阻塞。** 所有后续实验依赖就绪。

当前服务器状态：
- GPU 0：v5_div_reg 训练中（22GB/98GB）
- GPU 1：baseline_std libero_10 eval 中（6.6GB/98GB）+ baseline_plus_v2 eval

---
