# code d014 eval prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d014-eval-prep_20260515T200102_result.json`
- **Structured JSON:** [`474d8fe22162ffde4df2.json`](../../sessions/47/474d8fe22162ffde4df2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本部署完成，语法验证通过。汇总如下：

---

### 1. Baseline checkpoint 存在性

| Checkpoint | 状态 | 大小 |
|---|---|---|
| `baseline/step_005000/checkpoint.pt` | ✅ 存在 | 1.16 GB |
| `baseline/step_010000/checkpoint.pt` | ✅ 存在 | 1.16 GB |
| `baseline/step_015000/checkpoint.pt` | ✅ 存在 | — |
| `baseline/step_020000/checkpoint.pt` | ✅ 存在 | — |
| `baseline/step_025000/checkpoint.pt` | ✅ 存在 | — |
| `baseline/step_029999/checkpoint.pt` | ✅ 存在 | 1.16 GB |
| `baseline/latest/` | ✅ 存在 | 同 step_029999 |

所有 baseline checkpoint 齐全，无缺失。

### 2. v7 checkpoint 列表

**`checkpoints/imm_anchor/`** (v7, lambda=0.5, config: `imm_anchor.yaml`)：
- step_002000 ~ step_026000（每 2000 步，共 13 个） + latest
- latest 写入时间 03:54，仍在训练中，预期最终到 step_029999 或 step_030000

**`checkpoints/imm_anchor_v7_1/`** (v7.1, lambda=0.2, config: `imm_anchor_v7_1.yaml`)：
- step_002000, step_004000, step_006000 + latest
- 也在并行训练

### 3. evaluate.py CLI 参数

| 参数 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `--checkpoint` | str | **必填** | checkpoint 文件或目录路径 |
| `--config` | str | **必填** | YAML 配置文件路径 |
| `--gpu` | int | 0 | GPU 编号 |
| `--output` | str | None | 结果 JSON 输出路径 |
| `--max_batches` | int | 100 | 评估最大 batch 数 |
| `--lipschitz_samples` | int | 100 | Lipschitz 估计采样数 |
| `--seed` | int | 42 | 随机种子 |

注意：参数名是 `--max_batches`（不是 `--max_eval_batches`）。

### 4. eval 脚本

已部署到 `/root/autodl-tmp/importance_margin_vla_compress/run_d014_eval.sh`，`chmod +x` 已执行，`bash -n` 语法检查通过。

用法：`bash run_d014_eval.sh [GPU_ID]`，默认 GPU 0。

脚本自动检测 v7 最终 checkpoint（优先 `latest/`），依次执行 4 个 eval phase。

### 5. evaluate.py 修复确认

- **D011 hash 修复** ✅ — line 260: `hashlib.md5(condition.encode()).hexdigest()`
- **Pruning hook 范围修复** ✅ — line 164: `n_visual = 64`，line 180: `torch.randperm(n_visual, ...)`

---
