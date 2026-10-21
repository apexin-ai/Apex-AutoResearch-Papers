# 019a/019b ManiSkill3 Dry-Run 验证报告

**日期**: 2026-05-16  
**服务器**: bjb1-45299 (2×RTX PRO 6000, 98GB each)

## 验证结果：PASS

### 1. ManiSkill3 安装状态
- **版本**: 3.0.1 ✓
- **PickCube-v1 环境**: 可用，obs shape = (1, 42) ✓

### 2. DreamerV3 集成
- `dreamer.py` L198-205: `maniskill` suite 已集成，调用 `envs/maniskill.py` wrapper
- `configs.yaml` L206-215: `maniskill_state` 配置块已就绪
- `envs/maniskill.py`: 完整的 DreamerV3-compatible wrapper（state obs、action normalization、GPU resolve）

### 3. Dry-Run 结果 (cuda:0, --compile False)
```
[2500] eval_return 1.0 / eval_length 200.0 / eval_episodes 10.0
[2500] model_loss 6.9 / actor_loss -0.1 / value_loss 9.3 / kl 1.6
```
- Prefill (2500 steps) ✓
- Evaluation (10 episodes) ✓  
- Training step (model/actor/value 更新) ✓

### 4. 注意事项
- **必须加 `--compile False`**: 当前 PyTorch 版本的 torch.compile 有 Triton "duplicate template name" bug
- **必须设 `LD_PRELOAD` 和 `MUJOCO_GL=egl`**: SAPIEN 渲染依赖

---

## 019a Baseline 提交命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/autodl-tmp/event-gated-adaptive-horizon && \
nohup bash -c 'LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl \
python dreamer.py \
  --configs maniskill_state \
  --steps 256000 \
  --seed 0 \
  --device cuda:1 \
  --logdir /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019a_pickcube_baseline \
  --compile False' > /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019a_pickcube_baseline.log 2>&1 &
```

**配置说明** (继承自 `maniskill_state`):
- task: maniskill_PickCube-v1
- action_repeat: 1
- envs: 1
- train_ratio: 512
- time_limit: 200
- gate_enabled: false (pure baseline)
- imag_horizon: 15
- steps: 256000 (约 5h on RTX PRO 6000)

---

## 019b CIVO Trigger 提交命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/autodl-tmp/event-gated-adaptive-horizon && \
nohup bash -c 'LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl \
python dreamer.py \
  --configs maniskill_state \
  --steps 256000 \
  --seed 0 \
  --device cuda:0 \
  --logdir /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019b_pickcube_civo \
  --compile False \
  --gate_enabled true \
  --gate_fixed_dt 2 \
  --gate_subsample_min_dt 1 \
  --gate_subsample_max_dt 2 \
  --imag_horizon 8 \
  --dt_emb_freeze false' > /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019b_pickcube_civo.log 2>&1 &
```

**019b vs 019a 差异**:
| 参数 | 019a (baseline) | 019b (CIVO) |
|------|----------------|-------------|
| gate_enabled | false | true |
| gate_fixed_dt | 0 | 2 |
| gate_subsample_max_dt | 0 | 2 |
| imag_horizon | 15 | 8 |
| dt_emb_freeze | false | false |
| device | cuda:1 | cuda:0 |

**说明**: 019b 使用 fixed dt=2 + subsample ON + H=8 imagination。dt_emb 不 freeze（从随机初始化开始学习）。如果需要 pretrained dt_emb，需要从之前的 Walker 实验 checkpoint 加载——但 PickCube 是新 domain，建议从头训。

---

## GPU 状态 (验证时)
- cuda:0: 4165 MiB / 97887 MiB (009d Walker baseline)
- cuda:1: 4690 MiB / 97887 MiB (010a Cheetah baseline)
- 010a 完成后 cuda:1 释放，立即提交 019a
