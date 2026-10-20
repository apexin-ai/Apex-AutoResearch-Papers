# code exp wiki pair submit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_wiki_pair_submit_20260517T112140_result.json`
- **Structured JSON:** [`b555733014437aad141e.json`](../../sessions/b5/b555733014437aad141e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已成功提交并注册为 RUNNING：

| 实验 | GPU | PID | 日志 |
|------|-----|-----|------|
| `exp_wiki_pythia` | cuda:2 | 26873 | `~/runs/gen-depth-contamination/exp_wiki_pythia.log` |
| `exp_wiki_olmo` | cuda:3 | 27620 | `~/runs/gen-depth-contamination/exp_wiki_olmo.log` |

两者共享 Wikipedia 5K seed data，使用 Qwen2.5-1.5B 作为 scorer，continuation mode，depth 0-5，nucleus p=0.95, T=1.0，bootstrap 10000 resamples（pipeline 默认）。

---
