# ssh 14b merge inference

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_14b-merge-inference_20260520T141932_result.json`
- **Structured JSON:** [`e4e7a0680d113fb6b647.json`](../../sessions/e4/e4e7a0680d113fb6b647.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个推理进程全部正常运行：

| GPU | 数据集 | 显存占用 | 进度 | 速度 |
|-----|--------|---------|------|------|
| cuda:0 | FewNERD (37648 inst) | 31101 MiB | 519/37648 (~1.4%) N=1 | ~9 it/s |
| cuda:1 | CoNLL (3453 inst) | 31121 MiB | 714/3453 (~21%) N=1 | ~8 it/s |
| cuda:3 | SciERC (551 inst) | 30839 MiB | rendering prompts | starting |

预计时间：
- SciERC: 最快完成（551 inst × 5 N），约 30-60 min
- CoNLL: 3453 inst × 5 N，约 2-4h  
- FewNERD: 37648 inst × 5 N，约 20-30h（N=16 最重）

所有进程都用 nohup 后台运行，可以安全断开。需要我定期检查进度吗？

---
