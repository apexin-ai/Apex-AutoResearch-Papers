# 诊断报告：llama-cross-model-full 实验状态

**诊断时间**: 2026-05-19 12:30 UTC  
**结论**: **Cron 误报，实验正常运行中**

## 实验状态：运行中

- 两个 tmux session (`llama-full-gpu0`, `llama-full-gpu1`) 均存在且活跃
- 两块 RTX 5090 均加载了 vLLM (各占 28008 MiB)，GPU 0 满载 (100%)，GPU 1 当前 0% util（episode 间切换）
- ScienceWorld Java 进程正常运行（3 个 GatewayServer 实例）
- 脚本进程 PID 276421 (gpu0) 和 276639 (gpu1) 均存活

**误报原因**: 脚本在每个 task 间重启 vLLM，导致 cron 监控的原始 PID (277224) 失效，触发 "process dead 5x" 逻辑。

## 已完成 Tasks (2/11)

| Task | GPU | Episodes | 状态 |
|------|-----|----------|------|
| chemistry-mix | GPU 0 | 20/20 | DONE (有 collection_meta.json) |
| identify-life-stages-2 | GPU 1 | 20/20 | DONE (有 collection_meta.json) |

## 进行中 Tasks (2/11)

| Task | GPU | Episodes | 状态 |
|------|-----|----------|------|
| find-animal | GPU 0 | 11/20 | 进行中 (episode 11) |
| inclined-plane-determine-angle | GPU 1 | 10/20 | 进行中 (episode 10) |

## 未开始 Tasks (7/11)

**GPU 0 队列** (find-animal 之后):
- find-non-living-thing
- freeze
- grow-fruit
- identify-life-stages-1

**GPU 1 队列** (inclined-plane-determine-angle 之后):
- lifespan-longest-lived
- lifespan-longest-lived-then-shortest-lived
- measure-melting-point-unknown-substance

## 数据量统计

| Task | episode_summary | episodes.jsonl | labeled_steps.jsonl |
|------|----------------|----------------|---------------------|
| chemistry-mix | 20 episodes | 318 KB | 129 KB |
| identify-life-stages-2 | 20 episodes | 329 KB | 211 KB |
| find-animal | 11 episodes (进行中) | 169 KB | 101 KB |
| inclined-plane-determine-angle | 10 episodes (进行中) | 153 KB | 21 KB |

## ETA 估算

根据已完成 task 耗时推算（约 4 min/episode，加 vLLM 重启开销约 5 min/task）：

- **GPU 0**: 剩余 9 + 20x4 = 89 episodes, 约 6 小时, 完成时间 ~18:30 UTC
- **GPU 1**: 剩余 10 + 20x3 = 70 episodes, 约 5 小时, 完成时间 ~17:30 UTC
- **整体 ETA**: ~18:30 UTC（GPU 0 是瓶颈）

## 建议

无需干预。实验正常运行，继续等待即可。Cron 监控逻辑需要适配"脚本内循环重启 vLLM"的模式，避免后续误报。
