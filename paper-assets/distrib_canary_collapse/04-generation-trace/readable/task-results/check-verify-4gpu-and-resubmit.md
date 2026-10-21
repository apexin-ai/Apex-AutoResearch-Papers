# check verify 4gpu and resubmit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_verify_4gpu_and_resubmit_20260519T184652_result.json`
- **Structured JSON:** [`54ad1dd3a8eb99a38051.json`](../../sessions/54/54ad1dd3a8eb99a38051.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部正在运行，不需要重提交。

| 实验 | GPU | PID | 运行时间 | GPU 显存 | GPU 利用率 |
|------|-----|-----|---------|---------|-----------|
| qwen35_08b_wiki_a100_s43_fp32 | cuda:1 | 174453→174458 | 40:12 | 22864 MiB | 62% |
| scale_69b_a100_s43 | cuda:2 | 177510→177515 | 19:33 | 41204 MiB | 92% |
| alpha_sweep_a045_s42_fp32 | cuda:4 | 178540→178545 | 15:19 | 12706 MiB | 68% |
| c4_a025_s42_fp32 | cuda:5 | 178620→178625 | 15:17 | 12908 MiB | 72% |

4 个 PID 全部存活，GPU 均有显存占用且利用率正常。Pythia-6.9B 占用最大（41GB，92% 利用率），符合 bf16 大模型预期。

---
