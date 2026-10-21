# ssh 5090c fill and check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090c_fill_and_check_20260521T145124_result.json`
- **Structured JSON:** [`ec1e1c040e084b791fa5.json`](../../sessions/ec/ec1e1c040e084b791fa5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。

---

### cuda:1: CoNLL MF4v2 s42 rerun
- **状态**: 已启动
- **PID**: 329610 (VLLM EngineCore: 329884)
- **GPU 1**: 91%, 30235 MiB
- **进度**: 模型已加载，正在推理 256/27624 (1%)，渲染完成
- **参数**: `qwen3-8b-conll2003-merged`, n_samples=8, T=1.0, seed=42, collect_logprobs
- **预计时间**: ~15-20 min

### cuda:0: FewNERD N=16 s123
- **进程**: 存活 (PID 311985 + VLLM 312685)，运行 3h28m
- **进度**: 2798/37648 (7%)，~33 it/s，剩余 ~17 min
- **模型**: qwen3-8b-fewnerd-exp021-merged, n_samples=16
- **建议**: 继续等待，即将完成

### cuda:2: 候选实验
GPU 2 空闲 (0%, 0 MiB)。缺失实验：

| 优先级 | 实验 | 模型 | 说明 |
|--------|------|------|------|
| 1 | **scierc_n16_s123** | qwen3-8b-scierc-merged-v2 | 目录存在但为空，需重跑 |
| 2 | **scierc_n16_s456** | qwen3-8b-scierc-merged-v2 | 目录不存在，N16 第三个 seed |
| 3 | **e2_pretrained_fewnerd_s456** | Qwen2.5-7B-Instruct | pretrained baseline，s123 在 GPU3 跑，s456 未做 |

### cuda:3（附带信息）
- e2_pretrained_fewnerd_s123 运行中 (PID 306365)，Qwen2.5-7B-Instruct，n=8, seed=123

---
