# train imm fullft 100k cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_imm_fullft_100k_cqa1_20260516T215247_result.json`
- **Structured JSON:** [`154549ac522360e8f611.json`](../../sessions/15/154549ac522360e8f611.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练确认正常运行：

**产出总结：**

1. **代码/config 同步**：通过 SSH key 从 westd 到 cqa1 成功同步 `train_twostage.py` + `libero_imm_twostage_fullft.yaml`（MD5 验证通过）

2. **100K checkpoint 路径**：`/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_full_ft/step_099999/checkpoint.pt`（1.3GB）

3. **修复**：`imm/acis.py` 添加 dtype 自动转换（BFloat16→Float32）解决了 mat1/mat2 dtype mismatch

4. **启动命令**：
   ```
   CUDA_VISIBLE_DEVICES=1, WANDB_MODE=offline
   python train_twostage.py --config configs/libero_imm_twostage_fullft.yaml --gpu 0 --wandb_run libero_imm_fullft_100k
   ```

5. **训练状态**：
   - GPU 1：2881 MiB 已使用
   - Stage 1 运行中：step=50/10000, margin_loss=0.2964, sps=3.6
   - Expert 155 params 冻结，ACIS 10 params 训练中（3.46M 参数，0.76%）
   - tmux session: `libero_imm_fullft_100k`
   - Log: `~/runs/importance_margin_vla_compress/libero_imm_fullft_100k.log`

---
