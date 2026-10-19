# Cell B 1-GPU 多种子训练配置 — 就绪报告

## 1. Model Path（已确认 1.7B）

- **路径**: `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4`
- **架构**: Qwen3ForCausalLM, hidden_size=2048, num_hidden_layers=28, num_attention_heads=16
- **确认**: Qwen3-1.7B（非 4B）

## 2. 创建的文件

### Config: `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_factorial_h2_episode_adv_1gpu.yaml`

基于原始 Cell B config（`_alfworld_factorial_h2_episode_adv.yaml`）适配 1-GPU：
- `system.CUDA_VISIBLE_DEVICES: "0"`（原 "0,1"）
- `trainer.n_gpus_per_node: 1`（原 2）
- 其他参数完全一致：h=2, episode_level advantage, 15 training steps, 134 OOD val episodes
- YAML 语法验证通过

### 启动脚本: `/root/cost-verify-agent-rl/scripts/run_cell_b_1gpu.sh`

```bash
bash scripts/run_cell_b_1gpu.sh 100   # seed=100
bash scripts/run_cell_b_1gpu.sh 200   # seed=200
bash scripts/run_cell_b_1gpu.sh 300   # seed=300
```

脚本通过 Hydra CLI override 设置 seed 和对应的 experiment_name / checkpoint 路径，无需为每个 seed 创建单独 config。

## 3. Seed 字段

- **字段名**: `seed.train`（定义在 base.yaml，默认 10000）
- **覆盖方式**: Hydra CLI `seed.train=${SEED}`
- **参考**: exp029_seed2 config 使用 `seed.train: 43`，验证字段名正确

## 4. 启动方式

- `python train.py --config-name <name>`（非 torchrun）
- 与 exp029 系列启动脚本一致

## 5. ScienceWorld SFT 进度

- **PID**: 171362，已运行 ~1h07m
- **进度**: 192/450 steps（43%）
- **预计剩余**: ~1h20m（~18.5s/step）
- **GPU 0**: 100% utilization, 49541/97887 MiB

## 6. 磁盘状态

- `/root/autodl-tmp`: 80GB 可用（250G 总量，69% 已用）
- 足够存放多个 Cell B checkpoint

## 7. 阻塞问题

**无阻塞**。SFT 完成后即可用 GPU 0 启动 Cell B seed 实验。需串行跑（1 GPU），每个 seed 约需数小时。
