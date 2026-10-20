# plan-006-deep-internal 失败诊断

## 失败原因

**GPU 资源冲突 + 重复启动。**

两个进程均使用 `CUDA_VISIBLE_DEVICES=0`，在同一块 RTX 5090 (32GB) 上竞争内存：

| 进程 | 日志 | 启动时间 | 任务 |
|------|------|----------|------|
| Process 1 | `plan006_deep_internal.log` | 22:41 | **全部 6 个任务**（含不属于 GPU0 的 identify-life-stages-1, lifespan-longest-lived, find-non-living-thing, lifespan-longest-lived-then-shortest-lived） |
| Process 2 | `plan006_gpu0.log` | 23:37 | inclined-plane-determine-angle, chemistry-mix |

两个 vLLM 实例各请求 85% GPU 显存 (27.7GB x 2 = 55.4GB)，远超 32GB。GPU 1 全程空闲。

## 关键错误

```
# gpu0.log 最后一行
ERROR 05-16 00:10:48 [core_client.py:704] Engine core proc EngineCore died unexpectedly, shutting down client.

# deep_internal.log 最后两行
(EngineCore pid=486404) INFO 05-16 00:10:38 [core.py:1201] Shutdown initiated (timeout=0)
(EngineCore pid=486404) INFO 05-16 00:10:38 [core.py:1224] Shutdown complete
```

Process 1 的 vLLM 在 00:10:38 被 kill (clean shutdown)，Process 2 在 00:10:48 引擎崩溃。

## 已完成 Episode 统计

| 任务 | episodes.jsonl 行数 | collection_meta | 状态 |
|------|---------------------|-----------------|------|
| identify-life-stages-1 | 20 | 20/20 | 完成 |
| lifespan-longest-lived | 20 | 20/20 | 完成 |
| find-non-living-thing | 20 | 20/20 | 完成 |
| lifespan-longest-lived-then-shortest-lived | 20 | 2/20 (元数据不准) | 需验证 |
| inclined-plane-determine-angle | 20 | 20/20 | 完成 |
| chemistry-mix | 17 | 无 meta | 缺 3 集，补充进程在跑 |

**总计**: 117/120 episodes (97.5%)，chemistry-mix 补充进程正在运行中。

## 数据完整性风险

两个进程同时写入同一输出目录，episodes.jsonl 可能有重复条目。`lifespan-longest-lived-then-shortest-lived` 的 meta 声称只收集了 2 集，但 JSONL 有 20 行，需要去重检查。

## 当前服务器状态 (00:18 UTC+8)

- GPU 0: 100% 利用率，28GB 占用 (两个 chemistry-mix 补充进程 + vLLM)
- GPU 1: 空闲
- 两个 chemistry-mix 补充进程正在运行 (PIDs 508260, 509607)
- 无 tmux session

## 可否重试 + 修复建议

**不需要完全重试。** 5/6 任务已完成，chemistry-mix 补充进程正在收集剩余 3 集。

重试前需修复：
1. **CUDA_VISIBLE_DEVICES 分配错误**：并行进程必须分配到不同 GPU (GPU0/GPU1)，不能都用 GPU 0
2. **Process 1 任务范围错误**：启动了全部 6 个任务而非计划的 2 个，导致与 Process 2 重复执行
3. **去重检查**：合并结果前需检查 episodes.jsonl 是否有重复条目 (两个进程同时写入同一目录)
4. **当前补充进程冲突**：目前两个补充进程又在 GPU 0 上竞争，可能重演相同问题，建议 kill 一个

## Cron 判定失败原因

进程未完成全部任务 -> 未写入 sentinel 文件 -> 未注册 W&B run -> cron 连续 5 次检测到 "process dead with no sentinel/W&B" -> 自动标记为 failed。
