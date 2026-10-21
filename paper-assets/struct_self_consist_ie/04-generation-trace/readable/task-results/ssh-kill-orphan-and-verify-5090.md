# ssh kill orphan and verify 5090

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_orphan_and_verify_5090_20260522T110552_result.json`
- **Structured JSON:** [`185cb8e7b8481f7ac0a5.json`](../../sessions/18/185cb8e7b8481f7ac0a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU 释放: 4/4 卡空闲 (均 0% util, 2 MiB used)
SciERC model: OK (checkpoints/qwen3-8b-scierc-merged-v2/)
SciERC data: OK (data/scierc/processed_data/test.json)
FewNERD model: OK (checkpoints/qwen3-8b-fewnerd-exp021-merged/)
FewNERD data: OK (data/fewnerd/test.json)
可提交: SciERC 推理, FewNERD MF4 s123 推理
```

注：原始 4 个 PID 已 kill，但各自有 VLLM::EngineCore 子进程残留，用 SIGKILL 清理后 4 张 5090 全部释放。

---
