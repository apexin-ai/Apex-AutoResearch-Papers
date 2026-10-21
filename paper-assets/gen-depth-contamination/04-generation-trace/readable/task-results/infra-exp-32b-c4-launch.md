# infra exp 32b c4 launch

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp_32b_c4_launch_20260517T193636_result.json`
- **Structured JSON:** [`dfcc2a5905dc19b2ca35.json`](../../sessions/df/dfcc2a5905dc19b2ca35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**exp_32b_c4 已经在运行中**，无需重复启动。

| 项目 | 状态 |
|------|------|
| 模型 Qwen2.5-32B | 完整下载（17 shards, ~65GB），已加载到 cuda:1（64.7GB VRAM） |
| 磁盘空间 | 158GB 可用，充足 |
| 数据 | `data/exp_32b_c4/` 就绪（seed_docs.jsonl 539MB, depth_0.jsonl 5MB） |
| 实验进度 | PID 14642，depth 1 生成中（4/2500 batches, ~12s/batch, 预计 depth 1 需 ~8h） |
| Scorer Qwen2.5-1.5B (base) | **正在下载**（PID 14794, .incomplete 4.1GB），预计几分钟内完成 |
| Registry | 已更新 spec（补充 data_path, data_count, model_name, seed） |

**注意事项**：Scorer 模型在生成全部完成后才会加载（pipeline line 702），当前下载应能在 depth 1 结束前完成，不影响实验。exp_14b_c4 也依赖同一 scorer 路径，下载完成后两个实验都能正常进入 scoring 阶段。

---
