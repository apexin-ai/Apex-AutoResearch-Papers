# Backbone Scaling 70B 实验状态报告

**检查时间**: 2026-05-17 17:39 CST

## 运行状态：模型下载中（未开始实验）

实验脚本在 tmux session `backbone-scaling-70b` 中运行，但尚未进入 episode collection 阶段。

### 当前进度

- **模型下载**: Qwen2.5-72B-Instruct-AWQ，11 个 safetensors shards
- **已完成**: 8/11 shards（已落盘到最终目录）
- **进行中**: 3/11 shards（在 `._____temp` 临时目录中）
- **下载开始**: 16:49:13 CST
- **预计完成**: ~17:40-17:45 CST（剩余 3 shards，按当前速率约 1-2 分钟/shard）

### 下载时间线

| 时间 | 进度 |
|------|------|
| 16:49 - 17:34 | 0/11（大文件写入缓冲，未出现在最终目录） |
| 17:34:44 | 1/11 |
| 17:36:14 | 4/11 |
| 17:37:44 | 8/11 |
| 17:38:44 | 8/11（等待剩余 3 shards） |

### 实验配置

```bash
python src/episode_level_collection.py \
    --model_path /root/autodl-tmp/models/Qwen/Qwen2.5-72B-Instruct-AWQ \
    --task_types "chemistry-mix,find-animal,..." (11 types) \
    --episodes 20 \
    --max_steps 30 \
    --gpu_id 0 \
    --tp 2 \
    --output_dir results/backbone_72b/ \
    --seed 42
```

- 11 task types x 20 episodes = 220 episodes
- Tensor parallelism = 2 (dual GPU)
- Max steps per episode = 30

### 预计实验总时长

模型下载完成后，episode collection 预计需要 4-8 小时（72B AWQ 双 GPU 推理比 7B 慢约 3-5x）。

### 结果目录

`/root/autodl-tmp/simgate-modular-routing/results/backbone_72b/` 尚未创建。

## 待提取 Metrics（实验完成后）

- death_rate_overall
- death_rate_per_task (11 task types)
- score_distribution
- completion_status
- 对比基准：7B death rate = 42.9%, 0.5B death rate = 13.3%

## 下次检查建议

模型下载预计数分钟内完成，episode collection 预计 4-8 小时后完成。建议 5-6 小时后再次检查。
