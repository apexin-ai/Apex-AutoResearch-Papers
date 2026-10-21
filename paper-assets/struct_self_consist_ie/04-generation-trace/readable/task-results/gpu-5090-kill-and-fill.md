# gpu 5090 kill and fill

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_5090_kill_and_fill_20260521T075158_result.json`
- **Structured JSON:** [`92d8081ac059deb7c32b.json`](../../sessions/92/92d8081ac059deb7c32b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张卡全部在跑。最终状态：

| GPU | 状态 | 实验 | PID | 备注 |
|-----|------|------|-----|------|
| cuda:0 | 运行中 | FewNERD MF4v2 seed456 | 3308 | fine-tuned 模型，13:53 开始 |
| cuda:1 | **新启动** | FewNERD MF4v2 seed123 | 13611 | fine-tuned 模型，刚启动 |
| cuda:2 | **新启动** | FewNERD MF4v2 seed42 | 13761 | fine-tuned 模型，刚启动 |
| cuda:3 | 运行中 | E2 pretrained FewNERD seed42 | 8696 | base Qwen2.5-7B，14:59 开始 |

操作总结：
- 已 kill cuda:1 重复的 E2 pretrained FewNERD 进程（PID 3470）
- cuda:2 的 E2 pretrained CoNLL 已完成（report.json 已生成）
- 在 cuda:1/cuda:2 启动了 FewNERD MF4v2 的 seed123 和 seed42 实验（37648 instances，预计 3-4h）
- 注意：模型路径需要用嵌套路径 `checkpoints/qwen3-8b-fewnerd-exp021-merged/qwen3-8b-fewnerd-exp021-merged`，任务模板里的路径缺少 vocab 文件

---
