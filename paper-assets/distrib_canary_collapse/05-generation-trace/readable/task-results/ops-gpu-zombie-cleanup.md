# ops gpu zombie cleanup

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_zombie_cleanup_20260521T021054_result.json`
- **Structured JSON:** [`88ce310e11b28beb494a.json`](../../sessions/88/88ce310e11b28beb494a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 zombie 全部清理完毕，GPU 显存已释放。

```
westd-17855 (6x H800 97GB):
- cuda:0: 27214 MiB, 92%  — alpha_sweep_a048_s42_fp32 + alpha_sweep_a070_s42_fp32
- cuda:1: 14503 MiB, 75%  — (活跃实验)
- cuda:2: 14535 MiB, 85%  — (活跃实验)
- cuda:3: 70763 MiB, 99%  — scale_69b_a100_s43_bf16
- cuda:4: 0 MiB, 0%       — FREED (was zombie gen_gpt2m_a100_s43)
- cuda:5: 0 MiB, 0%       — FREED (was zombie alpha_sweep_a010_s42_bf16)

westd-19828 (2x H800 97GB):
- cuda:0: 0 MiB, 0%       — FREED (was zombie scale_14b_a050_s42_bf16)
- cuda:1: 24347 MiB, 97%  — generalize_pythia1b_c4_a100_s43_v2
```

释放了 3 块 GPU：17855 的 cuda:4/5 和 19828 的 cuda:0。

---
