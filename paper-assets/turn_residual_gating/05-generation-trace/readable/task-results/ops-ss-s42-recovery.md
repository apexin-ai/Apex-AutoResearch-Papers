# ops ss s42 recovery

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_ss_s42_recovery_20260522T155403_result.json`
- **Structured JSON:** [`78de3c97e9bcc800db17.json`](../../sessions/78/78de3c97e9bcc800db17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。汇报如下：

---

## SS s42 OOM 诊断结果

### 1. Checkpoint 状态
- **仅有 `epoch_0` checkpoint**：`runs/d048_ss_s42/epoch_0/`
  - `lora/adapter_model.safetensors` (20MB)
  - `gate_params.pt` (3.3MB)
- 无 `epoch_1` checkpoint

### 2. 崩溃点
- **最后日志**: Epoch 1 Step 7800 (OOM 在随后某步)
- **OOM 原因**: 另一个进程 PID 30899 占了 68.62 GiB，训练进程只剩 ~26 GiB，softmax 分配 424MiB 时失败
- **每 epoch ~8000 steps** (dataset=8000, batch=1, grad_accum=8 → 1000 optimizer steps/epoch)
- Epoch 1 几乎跑完，**损失 ~1 整个 epoch 的训练进度**

### 3. Resume 支持
- **支持 `--resume` 参数**，指向 epoch checkpoint 目录
- 恢复内容：LoRA weights + gate params + turn_embedding
- **不保存 optimizer/scheduler 状态** — resume 后 optimizer 从零开始，scheduler 会 fast-forward 到正确 step
- 从 `epoch_0` 恢复将从 epoch 1 重新开始

### 4. 推荐恢复命令

```bash
cd /root/turn_residual_gating && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
PYTHONUNBUFFERED=1 python src/train_phase2_v8b.py \
  --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct \
  --gate-type threadgate \
  --gar-loss-mode mse_target --gar-target 0.5 \
  --lambda-gar 1.0 --lambda-gate-div 1.0 \
  --min-gate-std 0.05 --init-bias 1.5 \
  --gate-lr-multiplier 10 \
  --lr 2e-4 --batch-size 1 --grad-accum 8 \
  --max-seq-len 2048 \
  --scheduled-sampling --ss-max-ratio 0.3 \
  --seed 42 --epochs 3 \
  --output-dir runs/d048_ss_s42 \
  --data-dir data/ultrachat_8k \
  --resume runs/d048_ss_s42/epoch_0
```

### 5. 预估剩余时间
- Total 3 epochs, epoch 0 完成，需重跑 epoch 1 + epoch 2
- 每 epoch ~8000 steps ≈ 若 Epoch 0 耗时约 X 小时，还需 ~2X 小时
- （从 log 时间戳来看，Epoch 0 Step 0 到 Epoch 1 Step 0 的间隔可估算单 epoch 时长，但 log 无时间戳，需看文件时间）

**注意**: 启动前务必确认 PID 30899（占 68GB 的进程）已不存在，否则会再次 OOM。当前 `nvidia-smi` 显示 GPU 已清空，可以安全启动。

---
