# check gpu status all

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_status_all_20260516T205928_result.json`
- **Structured JSON:** [`750a6009f34bb34ce270.json`](../../sessions/75/750a6009f34bb34ce270.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇报

| GPU | 状态 | 详情 |
|-----|------|------|
| **cuda:0** | 占用 | `scripts/serve_policy.py` (7790 MiB, 0% util, 闲置serving) |
| **cuda:1** | 满载训练 | v3_lora_universal_r48 (12842 MiB, 99% util, 532W) |
| **cuda:2** | 空闲 | 无进程, 3 MiB, P8 节能状态 |
| **cuda:3** | eval 运行中 | `eval_lora_openpi.py` baseline eval (8276 MiB, 36% util) |

### v3_lora_universal_r48 训练进度
- **当前 step: 1600 / 10000** (16% 完成)
- loss 稳步下降: 0.8479 → 0.8235
- 每 50 step 约 51.3s，预估剩余时间: ~2.4 小时
- lr=1.89e-04, grad_norm 有波动但可控

### eval 进程
- cuda:3 上正在跑 baseline eval (`--routing none`)
- 任务: libero_spatial, 扰动类型: background_textures, objects_layout, robot_initial_states, nominal
- 20 episodes, 日志在 `/tmp/eval_baseline_v3.log`
- tmux session: `v3_lora_universal_r48`

### evaluate_libero_plus.py
- 存在且可用 (23934 bytes, 最后修改 04:48 today)

### 可用资源
- **cuda:2 完全空闲**，可立即用于新任务
- cuda:0 虽有 serve_policy 占用但 GPU util 为 0%，如不需要 serving 可释放

---
