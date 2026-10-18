# train fullft seed1 cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_fullft_seed1_cqa1_20260516T213227_result.json`
- **Structured JSON:** [`e8e9aaa226bffa65bd67.json`](../../sessions/e8/e8e9aaa226bffa65bd67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功运行。

## 总结

**启动命令：**
```bash
CUDA_VISIBLE_DEVICES=0 python train.py --config configs/libero_full_ft_seed1.yaml --gpu 0 --seed 1 --wandb_run libero_fullft_seed1
```

**tmux session:** `libero_fullft_seed1`

**nvidia-smi 确认：** GPU 0 显存 5813 MiB，利用率 24%

**训练输出（前几步）：**
```
step=0/100000    loss=1.7711  lr=1.00e-07  grad=20.27  sps=0.8
step=50/100000   loss=1.9781  lr=5.10e-06  grad=17.56  sps=3.5
step=100/100000  loss=0.6096  lr=1.01e-05  grad=3.17   sps=3.6
step=150/100000  loss=0.6683  lr=1.51e-05  grad=6.14   sps=3.7
```

Loss 正在下降，速度 ~3.7 sps，训练正常。创建了 `configs/libero_full_ft_seed1.yaml`（output_dir 指向 `checkpoints/libero_full_ft_seed1`）。

---
