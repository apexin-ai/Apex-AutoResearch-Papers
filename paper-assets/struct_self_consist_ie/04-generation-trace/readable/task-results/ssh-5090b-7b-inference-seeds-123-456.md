# ssh 5090b 7b inference seeds 123 456

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090b-7b-inference-seeds-123-456_20260520T024108_result.json`
- **Structured JSON:** [`279303881d8e9daae471.json`](../../sessions/27/279303881d8e9daae471.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 seed 都已成功启动并进入 prompt rendering 阶段。

## 启动状态总结

| 项目 | 详情 |
|------|------|
| **服务器** | autodl-5090-b, 4× RTX 5090 (32GB) |
| **模型** | 本地 merge 完成: base (Qwen2.5-7B-Instruct) + QLoRA adapter → `checkpoints/qwen25-7b-fewnerd-merged/` (15GB) |
| **Seed 123** | GPU 0, PID 164573, 30054 MiB, rendering prompts ~69% (25928/37648) |
| **Seed 456** | GPU 1, PID 165181, 30262 MiB, rendering prompts ~17% (6424/37648) |
| **GPU 2-3** | 空闲 |
| **输出目录** | `output/fewnerd_7b/qwen25_7b_n8_seed123` / `output/fewnerd_7b/qwen25_7b_n8_seed456` |
| **日志** | `logs/7b_inference_seed123.log` / `logs/7b_inference_seed456.log` |

**执行过程**：5090-b 和 5090-c 不在同一 AutoDL 区域，无法直接 rsync 15GB merged model。改为传输 309MB LoRA adapter + 本地用 peft merge（5090-b 已有基座模型）。SSH 密钥对临时建立实现跨区域传输。

**命令与 5090-c seed 42 一致**：`--dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --collect_logprobs`，tensor_parallel 默认 1（单 GPU 足够放 7B）。

每个 seed 处理 37648 prompts（4706 test instances × 8 samples），预计运行 ~85 min。

---
