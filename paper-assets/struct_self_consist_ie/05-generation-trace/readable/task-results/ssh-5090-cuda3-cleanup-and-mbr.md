# ssh 5090 cuda3 cleanup and mbr

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090_cuda3_cleanup_and_mbr_20260521T122136_result.json`
- **Structured JSON:** [`71f17b34af9bd122b484.json`](../../sessions/71/71f17b34af9bd122b484.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part A: cuda:3 — e2_pretrained_fewnerd

**不能 kill。** 实验仍在活跃运行：

- 进度：**75% (28249/37648 prompts)**，不是 301184/301184
- 速度：~16 it/s，剩余 ~9400 prompts
- 预计完成：**~10 分钟后**（从现在算起）
- PID 8411 → vLLM::EngineCore PID 8696 占 cuda:3 (30628MiB)

其余 3 个 GPU 也都被活跃实验占用：
| GPU | 实验 | 模型 |
|-----|------|------|
| 0 | fewnerd_n16_s42 | qwen3-8b-fewnerd-exp021-merged |
| 1 | fewnerd_mf4v2_seed42 | qwen3-8b-fewnerd-exp021-merged |
| 2 | fewnerd_mf4v2_seed123 | qwen3-8b-fewnerd-exp021-merged |
| 3 | e2_pretrained_fewnerd | Qwen2.5-7B-Instruct (pretrained) |

### Part B: CoNLL MBR — 无法执行

CoNLL MF4v2 的推理数据**不存在**：

- `conll_mf4v2_seed123/` 和 `conll_mf4v2_seed456/` 目录不存在
- `conll_mf4_seed123/` 和 `conll_mf4_seed456/` 目录存在但**完全为空**（无 samples.jsonl）
- `find` 搜索确认没有任何 `*conll*mf4*` 路径下有 samples.jsonl

**CoNLL MF4v2 推理还没跑过。** 需要先用 fine-tuned 模型对 CoNLL 数据集跑推理生成 samples.jsonl，之后才能做 MBR 计算。MBR 脚本 `e3_mbr_multiseed.py` 已部署，但缺输入数据。

---
