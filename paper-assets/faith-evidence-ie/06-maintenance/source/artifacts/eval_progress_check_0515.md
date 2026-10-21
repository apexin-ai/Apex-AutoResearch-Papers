# Eval Progress Check — 2026-05-15 19:31 UTC

## 实验进度

| 实验 | PID | GPU | 进度 | ETA | 状态 |
|------|-----|-----|------|-----|------|
| rsft_r1 (seed=42) | 186329 | cuda:2 | **100%** (124/124) | — | ✅ 已完成 |
| rsft_r2a | 189488 | cuda:1 | **88%** (109/124) | ~12 min | 🔄 运行中 |
| rsft_r2b | 189855 | cuda:3 | **89%** (110/124) | ~11 min | 🔄 运行中 |
| ced_reranker_poc | 178050 | cuda:0 | **60%** (591/985 docs) | ~2.5h | 🔄 运行中 |

## rsft_r1 结果（已完成）

| 指标 | 值 |
|------|-----|
| F1 | **0.4449** |
| Precision | 0.4607 |
| Recall | 0.4302 |
| Evi-F1 | 0.8187 |
| EDCR | 0.6565 |
| Format OK | 985/985 (100%) |
| Truncated | 213/985 |
| Inference time | 6033s (~100 min) |

对比 s44: F1=0.4655, r1 比 s44 低 2.06 pp。

## GPU 状态

| GPU | 利用率 | 显存 | 占用者 |
|-----|--------|------|--------|
| 0 | 59% | 17.0/31.8 GB | ced_reranker_poc |
| 1 | 60% | 13.8/31.8 GB | rsft_r2a |
| 2 | 76% | 11.9/31.8 GB | rsft_r1（已完成，显存未释放） |
| 3 | 62% | 13.8/31.8 GB | rsft_r2b |

## s43 Eval 命令

rsft_r1 已完成，GPU 2 可用（可能需要先 kill 残留进程释放显存）。r2a/r2b 约 12 分钟后完成，届时 GPU 1/3 也可用。

**完整命令（在 tmux 中执行）：**

```bash
# 先检查 GPU 2 是否有残留进程
nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader

# 在 tmux session 中运行
tmux new-session -d -s mvp2_eval_rsft_s43

tmux send-keys -t mvp2_eval_rsft_s43 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && mkdir -p eval_results/rsft_s43 && CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s43 --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/rsft_s43 --no-quantize' Enter
```

**或 nohup 方式（通过 ssh_execute 提交）：**

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && mkdir -p eval_results/rsft_s43 && nohup bash -c 'CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s43 --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/rsft_s43 --no-quantize' > eval_results/rsft_s43/eval.log 2>&1 & echo "PID=$!"
```

参数来源：基于 s44 eval 的成功 config（已确认 `--model_path` / `--data_path` / `--sft_adapter` / `--no-quantize` 为正确参数名）。预计运行时间 ~100 分钟。

## 异常发现

1. **rsft_r1 PID 已死但 GPU 2 显存未释放**（11.9GB）—— 可能有子进程残留，提交 s43 前需检查并 kill
2. **所有 tmux session 均不存在**（pane not found）—— 进程是通过 nohup 在后台运行，tmux session 可能已自动退出，进程仍存活
3. **r1 vs s44 差距**：r1 F1=0.4449 vs s44 F1=0.4655，差 2pp，可能因 seed 不同或 rsft_output vs rsft_output_s44 是不同 checkpoint
