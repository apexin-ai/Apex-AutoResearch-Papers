# ssh 14b inference pids

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_14b-inference-pids_20260520T143003_result.json`
- **Structured JSON:** [`e02af34c8d71c045755c.json`](../../sessions/e0/e02af34c8d71c045755c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个推理进程的 PID 和对应关系：

| PID | 数据集 | GPU | 显存占用 |
|-----|--------|-----|----------|
| **201291** (parent: 201001) | FewNERD (`fewnerd_n1`) | cuda:0 | 31092 MiB |
| **201978** (parent: 201712) | CoNLL2003 (`conll2003_n1`) | cuda:1 | 31112 MiB |
| **203428** (parent: 203156) | SciERC (`scierc_n2`) | cuda:3 | 31032 MiB |

上面是 VLLM EngineCore 的 PID（实际占 GPU 的进程）。对应的 `run_mvp_pilot.py` 父进程 PID 分别是 201001、201712、203156。cuda:2 空闲。

---
