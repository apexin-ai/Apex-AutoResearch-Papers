# westb-14838 诊断报告 (2026-05-18 05:53 UTC)

## GPU 进程状态

| GPU | PID | 状态 | 退出原因 |
|-----|-----|------|---------|
| cuda:0 | 321045 | DEAD | vLLM EngineDeadError |
| cuda:1 | 69734 | ALIVE | 正常运行，处理最后一个 task |
| cuda:2 | 321159/540229 | DEAD | 进程不存在 |

## cuda:0 崩溃详情

崩溃栈：
```
episode_level_collection.py:main() → run_task_collection() → run_episode_deterministic()
→ agent.generate_candidate_actions() → _generate_vllm() → llm.generate()
→ vllm EngineCore ensure_alive() → EngineDeadError
```
根因：vLLM v1 engine core 内部异常导致进程不可恢复退出。dmesg 不可读（容器无权限），无法确认是否 OOM。

## cuda:1 进度

运行命令：7 个 task，每个 20 episodes
```
grow-fruit, identify-life-stages-1, identify-life-stages-2,
inclined-plane-determine-angle, lifespan-longest-lived,
lifespan-longest-lived-then-shortest-lived, measure-melting-point-unknown-substance
```

当前数据量（episode_summary.jsonl 行数）：
- grow-fruit: 20
- identify-life-stages-1: 20
- identify-life-stages-2: 40
- inclined-plane-determine-angle: 40
- lifespan-longest-lived: 21
- lifespan-longest-lived-then-shortest-lived: 20
- measure-melting-point-unknown-substance: 21 (最后更新 05:52，活跃中)

## nvidia-smi 摘要

| GPU | 显存 | 温度 | 状态 |
|-----|------|------|------|
| 0 | 0 / 97887 MiB | 30°C P8 | 空闲 |
| 1 | 87255 / 97887 MiB | 41°C P0 | cuda:1 运行中 |
| 2 | 0 / 97887 MiB | 31°C P8 | 空闲 |
| 3 | 0 / 97887 MiB | 30°C P8 | 空闲 |

## 空闲可用 GPU

**GPU 0, 2, 3 均空闲可用。**

## 建议

1. cuda:1 正常工作中，预计即将完成，不要中断
2. GPU 0/2/3 三卡空闲，可立即启动新任务
3. cuda:0 的 EngineDeadError 重启即可，需确认其原任务列表并补跑未完成部分
