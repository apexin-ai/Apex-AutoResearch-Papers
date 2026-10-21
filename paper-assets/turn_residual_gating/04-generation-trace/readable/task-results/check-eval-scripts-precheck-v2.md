# check eval scripts precheck v2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_scripts_precheck_v2_20260523T150253_result.json`
- **Structured JSON:** [`0edd8d85f4d4ecf79f7b.json`](../../sessions/0e/0edd8d85f4d4ecf79f7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据足够了，汇总结果。

---

## GPU Chain 脚本状态

### `gpu_chain_next.sh` 7步流水线

| 步骤 | 脚本 | 存在 | 关键参数/依赖 |
|------|------|------|-------------|
| 1/7 | `d048_eval_ss_s123.sh` | ✅ | 取 `runs/d048_ss_s123/epoch_{2,1,0}` 最高可用 epoch |
| 2/7 | `d048_ss_s456_resume.sh` | ✅ | `--resume runs/d048_ss_s456/epoch_0`（已存在 ✅） |
| 3/7 | `d048_eval_ss_s456.sh` | ✅ | 依赖 step 2 产出 |
| 4/7 | `qwen15b_phase1_diag.sh` | ✅ | 模型 `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B-Instruct` |
| 5/7 | `qwen15b_tg_train.sh` | ✅ | 同上，batch_size=4，输出 `runs/qwen15b_tg_v7_s42` |
| 6/7 | `qwen15b_eval.sh` | ✅ | Base + LoRA-only + TG 三组对比 |
| 7/7 | `mmlu_eval_all.sh` | ✅ | 6 个 checkpoint 串行评估 |

所有脚本均已到位，每步前有 `check_gpu_free()`（>1000MiB 则 abort），链式 `set -e` 任一失败即停。

### 等待脚本 PID 94251

**存活** — 运行 3h16m，正在 30s 间隔轮询 PID 84793 退出。超时 6h（剩余约 2h44m 余量）。退出后会检查 GPU 显存 <1000MiB 再启动 chain。

---

## SS s123 训练进度

| 指标 | 值 |
|------|-----|
| PID 84793 | **运行中**，已运行 7h10m，CPU 100% |
| 当前位置 | **Epoch 2 / Step 2800**（共 3 epochs） |
| 每 epoch 步数 | ~8000 steps（batch=1, 8k 数据） |
| Epoch 2 进度 | **35%**（2800/8000） |
| 最新 Loss | L_NTP=1.065, L_GAR≈0, Total≈1.065 |
| Gate 均值 | 0.948~0.953, std=0.05 |
| SS ratio | 0.300（已达上限） |
| GPU 显存 | 33387 / 97887 MiB（34%），利用率 99% |

### Checkpoint 状态

| Checkpoint | 保存时间 | 状态 |
|-----------|---------|------|
| epoch_0 | 18:33:24 | ✅ 完整（lora + gate_params.pt） |
| epoch_1 | 21:55:20 | ✅ 完整（lora + gate_params.pt） |
| epoch_2 | — | ⏳ 训练中 |

### 时间估算

- epoch 0 → epoch 1：~3h22m
- epoch 1 → 当前（epoch 2 step 2800）：已 ~1h10m
- 剩余 epoch 2：约 65% × 3h20m ≈ **2h10m**
- **预计完成时间：~01:10 CST (May 24)**

完成后 wait 脚本自动触发 gpu_chain_next.sh，无需人工干预。一切正常运行。

---
