# research read inst cond results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_read_inst_cond_results_20260516T231543_result.json`
- **Structured JSON:** [`311486a152c0e975a391.json`](../../sessions/31/311486a152c0e975a391.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在情况清楚了。脚本仍在运行中，输出被 pipe buffer 缓冲（stdout 未 flush 到 tee）。

总结：

**进程状态**: 仍在运行（PID 749462，已运行约74分钟，占用5.5GB RAM，纯 CPU sklearn 计算）

**结果文件**: `/root/autodl-tmp/vla-ssd/results/qa_probe/instruction_conditional_results.json` **尚未生成**（脚本在最后才写 JSON）

**工作量分析**: 
- 4 个条件组合: trained_image_mean, trained_last_preaction, untrained_image_mean, untrained_last_preaction
- 每个条件: 9 层 × 10 tasks（每个 h5 文件 1.8-4GB）
- 外加 1 个 DINOv2 baseline
- 总计: 4×9 = 36 组 PCA-256 + LogisticRegression + 1 组 DINO

**为什么慢**: 每次迭代要从 ~25GB 的 h5 文件加载特征到内存做 PCA 降维+逻辑回归，且全在 CPU 上跑。

**日志为空的原因**: Python stdout 通过 pipe 到 tee，默认 block-buffered，print 输出全在缓冲区里。

脚本结构是最后才一次性写 JSON，所以只能等它跑完。按当前速度（74分钟消耗中），预计还需要一段时间才能完成全部 36+1 组分类。需要等待，或者你想我 kill 掉重新跑一个带 `flush=True` 或 `python -u` 的版本来看中间进度？

---
