# code vtc m96 eval prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_vtc_m96_eval_prep_20260522T063803_result.json`
- **Structured JSON:** [`d92cc542b88ae884d6b1.json`](../../sessions/d9/d92cc542b88ae884d6b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是完整的 eval 方案：

---

## VTC M96 Eval 方案

### 训练当前进度
- **Step**: 89800 / 100000（89.8%）
- **速度**: ~0.5 sps（50 steps / ~100s）
- **剩余**: ~10200 steps → ~5.7h → 预计 **~20:20** 完成
- **Loss**: ~2.5（稳定）

### Checkpoint 保存机制
训练代码 `train_openvla_smart_compress.py:408-415`：
- 周期性保存（save_every=50000）→ `checkpoint_step{N}.pt`，仅含 **compressor_state_dict**
- **训练结束**（final=True）→ `checkpoint_step100000.pt` + `checkpoint.pt`，含 **完整 model_state_dict**

当前已有：`checkpoint.pt`（19.9GB, May 21 15:59）— 这是之前的 final checkpoint，**训练完成后会被覆盖为 step 100000 的版本**。

### Eval 命令

```bash
cd /root/autodl-tmp/importance_margin_vla_compress

CUDA_VISIBLE_DEVICES=0 python eval_openvla_smart_compress.py \
    --n_queries 96 \
    --checkpoint_path checkpoints/openvla_sc_m96_seed42/checkpoint.pt \
    --suite libero_object \
    --num_episodes 50 \
    --gpu 0 \
    --seed 42 \
    --model_path /root/autodl-tmp/openvla-libero-object \
    --output eval_results/eval_openvla_sc_m96_seed42.json
```

### 关键信息

| 项目 | 值 |
|------|-----|
| **Eval 脚本** | `eval_openvla_smart_compress.py` |
| **Checkpoint 路径** | `checkpoints/openvla_sc_m96_seed42/checkpoint.pt` |
| **预期输出路径** | `eval_results/eval_openvla_sc_m96_seed42.json` |
| **环境变量** | `MUJOCO_GL=egl`（脚本内已自动设置），`CUDA_VISIBLE_DEVICES=0` |
| **可用 GPU** | GPU 0、GPU 1 空闲；GPU 2-3 被训练占用 |
| **预计 eval 时间** | ~2-3h（参考 SmolVLA M96 eval 耗时 57min，OpenVLA 7B 约 3-5x 更慢） |

### 注意事项

1. **必须等训练完成后再 eval** — 训练结束会保存 final `checkpoint.pt`（含完整 model_state_dict）。如果用当前的 step 50k checkpoint，结果不代表最终模型。
2. **LIBERO 资源已就绪** — `libero_floor_base_style.xml` 存在，之前的 FileNotFoundError 已修复。
3. **之前 OpenVLA eval 的失败原因**：m64 是 checkpoint 损坏（zip archive），m128 是 LIBERO 资源缺失。当前环境这两个问题都不存在。
4. **用 nohup 运行**（eval 耗时长，防 SSH 超时）：
```bash
nohup bash -c 'cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 python eval_openvla_smart_compress.py --n_queries 96 --checkpoint_path checkpoints/openvla_sc_m96_seed42/checkpoint.pt --suite libero_object --num_episodes 50 --gpu 0 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --output eval_results/eval_openvla_sc_m96_seed42.json' > logs/eval_openvla_sc_m96_seed42.log 2>&1 &
```

---
