# code verify gpu chain

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_gpu_chain_20260523T080029_result.json`
- **Structured JSON:** [`25eb43dd862e93bded21.json`](../../sessions/25/25eb43dd862e93bded21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`gpu_chain_next.sh` 已更新，`chmod +x` 已设置。

## 完整链条状态

| Step | 任务 | 脚本路径 | 状态 |
|------|------|----------|------|
| 1 (跳过) | SS s123 训练 | `scripts/d048_ss_s123.sh` | 运行中 (PID 84793) |
| 2 → Chain 1/7 | SS s123 eval (TF+AR N=50) | `scripts/d048_eval_ss_s123.sh` | ✅ 已存在 |
| 3 → Chain 2/7 | SS s456 resume (epoch_0→2) | `scripts/d048_ss_s456_resume.sh` | ✅ 已存在 |
| 4 → Chain 3/7 | SS s456 eval (TF+AR N=50) | `scripts/d048_eval_ss_s456.sh` | ✅ 已存在 |
| 5 → Chain 4/7 | Qwen-1.5B Phase 1 diag | `scripts/qwen15b_phase1_diag.sh` | ✅ 已存在 |
| 6 → Chain 5/7 | Qwen-1.5B TG training | `scripts/qwen15b_tg_train.sh` | ✅ 已存在 |
| 7 → Chain 6/7 | Qwen-1.5B eval | `scripts/qwen15b_eval.sh` | ✅ 已存在 |
| 8 → Chain 7/7 | MMLU eval 6 checkpoints | `scripts/mmlu_eval_all.sh` | ✅ 已存在 |

**改动**：原 `gpu_chain_next.sh` 包含了 SS s123 训练步（已在运行，不应重复），且顺序错误（s456 在 s123 eval 之前）。已重写为正确顺序，每步前有 `check_gpu_free` 检查 GPU 显存 ≤1000MiB。所有子脚本均已存在且可执行，无需新建。

---
