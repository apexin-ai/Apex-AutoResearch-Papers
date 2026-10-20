# check d048 eval dryrun

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d048_eval_dryrun_20260522T133136_result.json`
- **Structured JSON:** [`5d36bfe198935d3574bd.json`](../../sessions/5d/5d36bfe198935d3574bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。以下是报告：

---

## Eval 脚本 Dry-Run 验证报告

### 1. 参数正确性

| 脚本 | 使用的参数 | --help 匹配 | 状态 |
|------|-----------|-------------|------|
| `eval_phase2_gar.py` | `--gate-type`, `--checkpoint-dir`, `--conversations-path`, `--output-dir`, `--gar-variant`, `--gate-profile` | 全部匹配 | ✅ |
| `eval_attention_steering.py` | `--checkpoint`, `--gate-type`, `--mode`, `--max-convs`, `--beta`, `--gar-variant`, `--output-dir`, `--output-name` | 全部匹配 | ✅ |

### 2. Checkpoint 路径

| Checkpoint | 路径 | lora/ | gate_params.pt | 状态 |
|-----------|------|-------|----------------|------|
| TG s42 | `runs/phase2_tg_s42_v7/epoch_2` | ✅ | ✅ | ✅ |
| UG s42 | `runs/phase2_ug_s42/epoch_2` | ✅ | ✅ | ✅ |
| LO s42 | `runs/phase2_lora_only_s42/epoch_2` | ✅ | 无（正常） | ✅ |
| PCGrad s42 | `checkpoints/tg_v9_pcgrad_s42/epoch_2` | ✅ | ✅ | ✅ |
| SS s42 | `runs/d048_ss_s42/epoch_0` | ✅ | ✅ | ⚠️ 见下 |
| Base model | `/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct/` | — | — | ✅ |

### 3. 数据文件
- `data/ultrachat_eval_heldout.json` — ✅ 存在 (453KB)

### 4. 磁盘空间
- 根分区：30G 总量，14G 可用 (46% 空闲)
- 单个 checkpoint ≈ 91MB（3 epochs），全部 runs/ = 613MB
- 14 个新 checkpoint × ~30MB/epoch ≈ 1.3GB 新增（远小于可用空间）
- **磁盘充足** ✅

### 5. CPU Dry-Run
`eval_attention_steering.py` 在 `CUDA_VISIBLE_DEVICES=""` 下成功加载模型权重到 CPU（无报错），参数解析和模型加载均通过。被 timeout 15s 截断，说明进入了推理阶段。 ✅

### 6. 需要修复的问题

**⚠️ `d048_eval_ss_s42.sh` 的 epoch 查找逻辑有 bug：**

```bash
for ep in 2 1; do   # 只查 epoch_2 和 epoch_1
```

SS s42 目前仍在训练，当前只有 `epoch_0`。如果训练未完成到 epoch_1，此脚本会报错退出（"No complete checkpoint found"）。

对比 `d048_queue_runner.sh` 的 `run_and_eval()` 函数查找 `2 1 0`，包含了 epoch_0 fallback。

**建议**：将 `d048_eval_ss_s42.sh` 的循环改为 `for ep in 2 1 0; do`，与 queue_runner 保持一致。或者等 SS 训练跑完 epoch_2 后再执行。

---
