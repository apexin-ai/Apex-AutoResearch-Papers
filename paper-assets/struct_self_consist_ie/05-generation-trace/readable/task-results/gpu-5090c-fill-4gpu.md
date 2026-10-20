# gpu 5090c fill 4gpu

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_5090c_fill_4gpu_20260521T071406_result.json`
- **Structured JSON:** [`9efa3265be8e99c4a2a2.json`](../../sessions/9e/9efa3265be8e99c4a2a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张 GPU 全部满载运行：

| GPU | 实验 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| cuda:0 | exp_fewnerd_n16_s456_v2 (FewNERD N=16 s456) | 30117 MiB | 27% |
| cuda:1 | exp_conll_n16_s123_v2 (CoNLL N=16 s123) | 30149 MiB | 84% |
| cuda:2 | exp_conll_n16_s456_v2 (CoNLL N=16 s456) | 30147 MiB | 91% |
| cuda:3 | exp_e2_pretrained_scierc (SciERC E2 baseline) | 30349 MiB | 85% |

过程中处理了：5090-c 没有 tmux（conda 安装 + symlink 到 /usr/local/bin）、两个僵尸 registry 记录（exp_14b_inference_fewnerd、exp_fewnerd_7b_n16_s42 标记 DONE）。

---
