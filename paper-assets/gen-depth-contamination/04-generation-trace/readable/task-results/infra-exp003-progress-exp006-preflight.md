# infra exp003 progress exp006 preflight

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp003_progress_exp006_preflight_20260513T103619_result.json`
- **Structured JSON:** [`309aae15939bbb2b7684.json`](../../sessions/30/309aae15939bbb2b7684.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-003 进度

- **当前 config: 2/4 (nucleus p=0.9, T=1.0)**
- 已完成: greedy（14:44→18:03，含生成+特征提取+分析，共 ~3h20m）
- nuc09 进行中：depth_0 已完成，**depth_1 生成 311/313 batches (99%)**，~6.3s/batch
- greedy 各 depth 耗时参考：~32min/depth + 39min 特征分析

**预估剩余时间：**
| Config | 剩余 |
|--------|------|
| nuc09 (当前) | depth 2-5 + 分析 ≈ 2h50m |
| nuc095_T07 | ~3h20m |
| nuc095_T12 | ~3h20m |
| **总计** | **~9h30m** |

日志最新关键输出：
- greedy 分析结果：K* (max depth with AUC > 0.60) = 2，top feature = freq_entropy
- nuc09 于 18:04 启动，当前正在生成 depth 1

## GPU 利用率

- GPU: NVIDIA RTX 4090 D
- **GPU utilization: 47%**
- **Memory: 3.9 / 24.0 GB (16%)**
- PID 34916 (python) 占用 3912 MiB
- 评估：显存大量空闲（~20GB），GPU 计算利用率中等——瓶颈在 autoregressive decoding，单 batch 无法充分利用，属正常水平

## exp-006 前置检查

| 检查项 | 状态 | 备注 |
|--------|------|------|
| run_exp006.sh | ✅ | 4.1KB, 可执行 |
| exp006_filtering_strategies.py | ✅ | 10.9KB |
| exp006_continued_pretraining.py | ✅ | 7.2KB |
| exp006_evaluate.py | ✅ | 2.5KB |
| exp006_analyze.py | ✅ | 9.7KB |
| Qwen depth chain 数据 | ✅ | depth_0~5.jsonl, 每个 5000 条, 共 30000 条 |
| Qwen 模型权重 | ✅ | config.json + model.safetensors 存在 |
| lm-eval-harness | ✅ | 0.4.11 |
| peft | ✅ | 0.19.0 |
| lightgbm | ✅ | 4.6.0 |
| 缺失依赖 | 无 | 全部就绪 |

**run_exp006.sh 配置**: 6 strategies (no-filter, binary-ours, binary-drayson, graduated, surprisal, dsir) × 5 seeds (42/123/456/789/1024), alpha 扫 0.1~0.9。

**结论：exp-006 全部前置条件满足，exp-003 完成后可直接启动。**

---
