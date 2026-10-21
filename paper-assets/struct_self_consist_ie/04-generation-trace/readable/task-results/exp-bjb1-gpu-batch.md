# exp bjb1 gpu batch

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_bjb1_gpu_batch_20260514T150709_result.json`
- **Structured JSON:** [`b10715d6abddb96468ba.json`](../../sessions/b1/b10715d6abddb96468ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张 GPU 全部满载运行：

| GPU | 显存占用 | 实验 | 状态 |
|-----|---------|------|------|
| 0 | 24728/32607 MiB | exp_017_llama_conll (已有训练) | 运行中 |
| 1 | 30084/32607 MiB | exp_007_llama_seed123 | ✅ 已启动，正在推理 |
| 2 | 29968/32607 MiB | exp_007_llama_seed456 | ✅ 已启动，正在推理 |
| 3 | 30134/32607 MiB | exp_008_re_seed123 | ✅ 已启动，正在推理 |

**跳过的实验：** exp_001_seed456_v2 (NER N=16 seed=456) — GPU 0 被 `llamafactory-cli train train_config_llama_conll2003.yaml` (exp_017_llama_conll) 占用。等该训练完成后可补跑。

3 个新实验均已注册到 registry（RUNNING），tmux 会话：`exp007_s123`, `exp007_s456`, `exp008_rs123`。日志显示 vLLM 已加载模型并开始生成。

---
