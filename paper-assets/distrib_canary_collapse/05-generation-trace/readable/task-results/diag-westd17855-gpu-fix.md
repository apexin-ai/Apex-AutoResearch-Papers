# diag westd17855 gpu fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd17855_gpu_fix_20260518T220434_result.json`
- **Structured JSON:** [`def4b1d304ccaed076fa.json`](../../sessions/de/def4b1d304ccaed076fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个实验 registry 状态已更新为 RUNNING。最终状态汇总：

## westd-17855 GPU 状态

| GPU | 实验 | PID | tmux session | 状态 |
|-----|------|-----|-------------|------|
| cuda:0 | scale_69b_a100_s42 | 29033 | scale_69b_a100_s42 | RUNNING (已有) |
| cuda:1 | qwen35_08b_wiki_a100_s42 (fp32) | 55423 | qwen35_08b_fp32 | RUNNING ✓ |
| cuda:2 | alpha_sweep_a060_s42_fp32 | 55503 | a060_s42_fp32 | RUNNING ✓ |
| cuda:3 | alpha_sweep_a005_s42 (fp32) | 55751 | a005_s42_fp32 | RUNNING ✓ |
| cuda:4 | interv_pred_a075_s42_fp32 | 56026 | interv_pred_fp32 | RUNNING ✓ |
| cuda:5 | alpha_sweep_a010_s43 | 45289 | alpha_sweep_a010_s43 | RUNNING (已有) |

**注意事项：**
- cuda:4 dry-run 进程 (PID 52764) 已 kill
- submit_on_allocated 在 westd-17855 上因 conda 环境未激活导致 `python: command not found`，改用手动 tmux + conda activate 提交
- cuda:5 上 OPT-1.3B (PID 44889) 无 CUDA_VISIBLE_DEVICES，与 alpha_sweep_a010_s43 共享 GPU（上次 session 遗留，未动）
- 所有新实验均 fp32（无 --bf16 参数）

---
