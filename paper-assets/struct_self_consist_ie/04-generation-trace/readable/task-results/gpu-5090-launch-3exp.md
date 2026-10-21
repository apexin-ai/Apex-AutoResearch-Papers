# gpu 5090 launch 3exp

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_5090_launch_3exp_20260521T065726_result.json`
- **Structured JSON:** [`17a6418dee0263a3461d.json`](../../sessions/17/17a6418dee0263a3461d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完毕。汇总：

### GPU 状态 & 启动结果

| GPU | 状态 | 实验 | 备注 |
|-----|------|------|------|
| cuda:0 | **占用** | VLLM PID 3308 (30170MiB) | 无法启动 exp_fewnerd_mf4_v2_s456 |
| cuda:1 | **占用** | VLLM PID 3470 (30080MiB) | 无法启动（原计划 exp_e2_pretrained_fewnerd） |
| cuda:2 | **已启动** | exp_e2_pretrained_conll (PID 7939) | Qwen2.5-7B-Instruct base, CoNLL, 模型加载中 |
| cuda:3 | **已启动** | exp_e2_pretrained_fewnerd (PID 8406) | Qwen2.5-7B-Instruct base, FewNERD, 21% 进度 |

### 关键发现
- **模型路径修正**: 实际路径是 `.../Qwen2___5-7B-Instruct`（ModelScope 用 `___` 替代 `.`），之前 registry 中的路径 `Qwen2.5-7B-Instruct` 可能导致了上次启动失败
- **exp_fewnerd_mf4_v2_s456** 无法启动 — cuda:0 被 VLLM 占用，需等 VLLM 释放或手动 kill 后再启动

---
