# infra P0 kill and restart occ s1 correct params

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_P0_kill_and_restart_occ_s1_correct_params_20260521T004253_result.json`
- **Structured JSON:** [`25ccdae221ec46c49e1b.json`](../../sessions/25/25ccdae221ec46c49e1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**汇报：**

- **Step 1:** PID 54250 — **KILLED** (force_killed)
- **Step 2:** occ_s0 完整命令行已提取，含所有关键超参数
- **Step 3:** occ_s1 已重启，tmux PID 56245，GPU 进程 PID 56325（cuda:1, 正在加载模型 550 MiB）
- **Step 4:** 参数验证 — **PASS**

关键参数确认（从 `/proc` cmdline 逐项核对）：

| 参数 | 值 | 状态 |
|------|-----|------|
| `num_images_in_input` | 2 | ✓ |
| `use_proprio` | True | ✓ |
| `batch_size` | 8 | ✓ |
| `learning_rate` | 5e-4 | ✓ |
| `image_aug` | True | ✓ |
| `lora_rank` | 32 | ✓ |
| `use_l1_regression` | True | ✓ |
| `use_diffusion` | False | ✓ |
| `use_film` | False | ✓ |
| `use_occ_head` | True | ✓ |
| `occ_data_dir` | /root/occsafe_vla/occ_data | ✓ |
| `occ_detach` | false | ✓ |
| `seed` | 43 | ✓ |
| `resume` | True, step 7500 | ✓ |
| `CUDA_VISIBLE_DEVICES` | 1 | ✓ |
| `run_root_dir` | .../occ_s1 | ✓ |
| `vla_path` | ...occ_s1/...--7500_chkpt | ✓ |

---
