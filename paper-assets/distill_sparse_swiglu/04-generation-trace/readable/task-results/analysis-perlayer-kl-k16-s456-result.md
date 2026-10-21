# analysis perlayer kl k16 s456 result

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perlayer_kl_k16_s456_result_20260523T092413_result.json`
- **Structured JSON:** [`8967c47a426ebc6bd0d7.json`](../../sessions/89/8967c47a426ebc6bd0d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### K=16 s456 — FAILED
- **崩溃点**: Step 500/1000，`torch.save` 写 checkpoint 时磁盘满
- **错误**: `RuntimeError: PytorchStreamWriter failed writing file` (EXIT_CODE=1)
- **最后指标**: avg_kl=0.1746, avg_sp=0.296, kl=0.1289
- **Checkpoint**: `predictor_perlayer_kl_k4_step_500.pt` (386MB) 存在但**大概率损坏**（写入中途失败）
- Registry 已更新为 DONE/failed

### K=16 s123 — STILL RUNNING (PID 128425)
- **当前进度**: Step 500/1000，已成功保存 step_500 checkpoint (435MB)
- **最后指标**: avg_kl=0.1790, avg_sp=0.298, kl=0.1338
- **风险**: 磁盘已 100% 满（30G / 188K free），下次 step 1000 保存 checkpoint 时极大概率同样崩溃

### GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 100% | 42.3G / 95.6G (s123 运行中) |
| cuda:1 | 0% | 0 / 95.6G (空闲) |

### 紧急问题：根分区 100% 满
`overlay 30G 30G 188K 100% /`

需要立即清理磁盘空间，否则 s123 也会在 step 1000 崩溃。建议清理方向：
1. 删除旧/无用 checkpoint（其他实验的）
2. 清理 pip cache (`pip cache purge`)
3. 清理 HF cache 中不再需要的模型
4. 将大文件移到数据盘 `/root/autodl-tmp/`（如果有）

是否需要我排查可清理空间？

---
