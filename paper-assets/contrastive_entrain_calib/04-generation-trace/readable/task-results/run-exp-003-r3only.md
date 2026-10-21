# run exp 003 r3only

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp-003_r3only_20260518T144402_result.json`
- **Structured JSON:** [`447104a0ca028a604a6c.json`](../../sessions/44/447104a0ca028a604a6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练任务已提交并在运行。

**总结：**

| 项目 | 状态 |
|------|------|
| 脚本 | `/root/contrastive_entrain_calib/training/run_exp003_r3only.py` 已部署 |
| 配置 | `r1=0.0, r2=0.0, r3=1.0`，`direction_path=""`（R3-only fallback） |
| 训练参数 | batch=1, grad_accum=16, lr=5e-5, max_steps=6000, LoRA r=64, num_gen=4 |
| 数据 | 362 条 calibration_v2_1_expanded.jsonl |
| 进程 | screen session `exp003`（PID 54216），cuda:1 |
| 输出 | `/root/autodl-tmp/checkpoints/exp003_r3only_seed1/` |
| 日志 | `/root/autodl-tmp/checkpoints/exp003_r3only_seed1.log` |
| Registry | exp-003 → RUNNING |
| 当前状态 | Qwen3-8B 模型下载中（~4MB/s，预计 ~1小时），之后自动开始训练 |

注意事项：
- 使用 `HF_ENDPOINT=https://hf-mirror.com` 绕过 huggingface.co 网络不可达
- HF cache 放在 `/root/autodl-tmp/.cache/huggingface`（数据盘 218GB 可用）
- DeBERTa-v3-base（R3 NLI 模型）会在训练首次计算 reward 时自动下载

---
