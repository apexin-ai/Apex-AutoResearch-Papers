# SSH 恢复后执行清单

> 前置条件：westd-35807 和 westd-45947 SSH 恢复，端口确认

---

## Phase 0: 验证 + Registry 修正（5 min）

```bash
# westd-35807 — 确认 4 个实验 checkpoint 完整
ls /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l005/30000/
ls /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l01/30000/
ls /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l005/30000/
ls /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l01/30000/

# 读日志确认完成
tail -5 /tmp/train_pi05_a1_obj_s1_l005.log
tail -5 /tmp/train_pi05_a1_obj_s1_l01.log
tail -5 /tmp/train_pi05_a1_obj_s2_l005.log
tail -5 /tmp/train_pi05_a1_obj_s2_l01.log

# 磁盘检查
df -h /root/autodl-tmp/

# GPU 状态
nvidia-smi
```

**如果 checkpoint 存在** → `update_registry` 改 conclusion=success，记录 metrics  
**如果某个不存在** → 读 log 确认中断原因 → 从最近 checkpoint 恢复训练

---

## Phase 1: Batch 1 Eval（~30 min）— westd-35807 4 GPU

4 模型并行：s0_l005 + s0_l01 + s1_l005 + s1_l01

### 公共环境（每个 tmux window 开头）
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export JAX_PLATFORMS=cpu
export MUJOCO_GL=osmesa
export PYTHONPATH=/root/colliforce-vla/openpi/src:$PYTHONPATH
cd /root/colliforce-vla
```

### 命令模板（serve + eval 双进程）
```bash
CUDA_VISIBLE_DEVICES={GPU} python openpi/scripts/serve_policy.py \
    --env libero --policy:checkpoint --policy.config pi05_libero \
    --policy.dir {CKPT_PATH} \
    --port {PORT} &
SERVE_PID=$!; sleep 60

python scripts/eval_pi05_safelibero.py \
    --port {PORT} --suite safelibero_object --safety_level II --n_episodes 50 \
    --seed 7 --output_path {OUTPUT_PATH}

kill $SERVE_PID
```

### Batch 1 参数表

| Window | GPU | Port | Checkpoint | Output |
|--------|-----|------|-----------|--------|
| s0_l005 | 0 | 8000 | `.../seed0_l005/30000` | `eval_30k_s0_l005.json` |
| s0_l01 | 1 | 8001 | `.../seed0_l01/30000` | `eval_30k_s0_l01.json` |
| s1_l005 | 2 | 8002 | `.../seed1_l005/30000` | `eval_30k_s1_l005.json` |
| s1_l01 | 3 | 8003 | `.../seed1_l01/30000` | `eval_30k_s1_l01.json` |

Checkpoint 全路径前缀：`/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_`  
Output 全路径前缀：`/root/autodl-tmp/eval_results/d012_final/`

---

## Phase 2: Batch 2 Eval + λ_sdf=0 Dry-Run（~30 min）— westd-35807

Batch 1 完成后：

### 2A: s2 Eval（2 GPU）

| Window | GPU | Port | Checkpoint | Output |
|--------|-----|------|-----------|--------|
| s2_l005 | 0 | 8000 | `.../seed2_l005/30000` | `eval_30k_s2_l005.json` |
| s2_l01 | 1 | 8001 | `.../seed2_l01/30000` | `eval_30k_s2_l01.json` |

### 2B: λ_sdf=0 Ablation Dry-Run（2 GPU，验证能启动）

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/colliforce-vla
WANDB_MODE=offline PYTHONUNBUFFERED=1 \
python scripts/train_a1_sdf_aux_pi05.py \
  --scene object_pudding \
  --seed 0 \
  --gpu 2 \
  --batch_size 32 \
  --num_train_steps 30000 \
  --lambda_sdf 0 \
  --lambda_ee 0.01 \
  --lr 2.5e-5 \
  --save_interval 2000 \
  --exp_name a1_sdf_pi05_object_pudding_seed0_l000 \
  2>&1 | tee /tmp/train_pi05_a1_obj_s0_l000.log
```

**Dry-run 验证**：启动后观察前 10 步 loss 正常（action_loss ~0.1-0.3, sdf_loss 项应为 0 或不出现），确认 Phase 1 能正常跑。

---

## Phase 3: 汇总 + 正式 Ablation

### 3A: 汇总 3-seed × 2-lambda 30K Eval 结果

| | λ=0.005 | λ=0.01 |
|---|---------|--------|
| seed 0 | TSR/CAR/SSR/frozen | TSR/CAR/SSR/frozen |
| seed 1 | TSR/CAR/SSR/frozen | TSR/CAR/SSR/frozen |
| seed 2 | TSR/CAR/SSR/frozen | TSR/CAR/SSR/frozen |
| **mean±std** | | |

对比 baseline（Pi0.5 3-seed: TSR=74.7±1.5%, CAR=26.8±1.6%）和 LoRA baseline（待完成）。

### 3B: λ_sdf=0 正式训练（dry-run 通过后）

```bash
# 正式提交（通过 submit_training_job）
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/colliforce-vla && \
WANDB_MODE=offline PYTHONUNBUFFERED=1 \
python scripts/train_a1_sdf_aux_pi05.py \
  --scene object_pudding --seed 0 --gpu 2 \
  --batch_size 32 --num_train_steps 30000 \
  --lambda_sdf 0 --lambda_ee 0.01 --lr 2.5e-5 \
  --save_interval 2000 \
  --exp_name a1_sdf_pi05_object_pudding_seed0_l000 \
  2>&1 | tee /tmp/train_pi05_a1_obj_s0_l000.log
```

---

## 注意事项

1. **s2_l01 特殊关注**：SDF loss 异常偏高 (~0.067 vs ~0.033)，eval 后需检查是否为 outlier
2. **λ_sdf=0 语义澄清**：当前命令 λ_sdf=0 意味着 Phase 1 和 Phase 2 均无 SDF loss（SDF decoder 存在但不获得梯度）。如果 Director 意图是 "Phase 1 正常预热（λ>0），Phase 2 关闭（λ=0）"，需要修改训练脚本支持 phase-dependent lambda。
3. **磁盘风险**：之前 baseline_spatial_bowl_s1_v2 因磁盘满崩溃，eval 前必须检查 autodl-tmp 剩余空间
4. **s0 eval 服务器选择**：如果 westd-45947 的 LoRA baseline 仍在跑，s0 eval 放 westd-35807
