# collect v5 results all

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_v5-results-all_20260514T014417_result.json`
- **Structured JSON:** [`f08a9eed4a54f2d076fb.json`](../../sessions/f0/f08a9eed4a54f2d076fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验完成状态

四个 v5 实验**全部仍在运行**，尚无 `profiling_results.json` 输出：

| 实验 | GPU | 进度 | 启动时间 |
|------|-----|------|----------|
| mvp_v5_fixed_s020 | cuda:0 (nohup) | 27/50 (54%) | 09:26 |
| mvp_v5_fixed_s030 | cuda:1 (nohup) | 28/50 (56%) | 09:26 |
| mvp_v5_fixed_s015 | cuda:2 (tmux) | 22/50 (44%) | 09:32 |
| mvp_v5_fixed_s025 | cuda:3 (tmux) | 22/50 (44%) | 09:32 |

NaN skip 在 s015/s025 的日志中有体现（`Skipped 1 NaN attention layers: [27]`），修复生效。

预计还需 **~15-20 分钟**完成。

## 关键指标汇总 / Registry 更新

无法执行——所有实验未完成，无结果文件。需等实验跑完后再收集。

## Qwen 下载状态

**已完成。** 4 个 safetensor shard 全部到位，总计 15.2GB：

```
model-00001-of-00004.safetensors: 3.9G
model-00002-of-00004.safetensors: 3.9G
model-00003-of-00004.safetensors: 3.9G
model-00004-of-00004.safetensors: 3.6G
```

路径：`/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B/Qwen/Qwen2___5-7B/`（有 symlink `Qwen2.5-7B -> Qwen2___5-7B`）。

注意：服务器上仍有 3 个冗余 ModelScope 下载进程和 1 个 HF 下载进程在跑（文件已完整），可以 kill 掉释放资源，要清理吗？

---
