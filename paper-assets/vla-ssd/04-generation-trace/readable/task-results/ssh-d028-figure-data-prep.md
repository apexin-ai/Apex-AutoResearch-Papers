# ssh d028 figure data prep

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d028-figure-data-prep_20260515T223154_result.json`
- **Structured JSON:** [`16bc6ab760f963859107.json`](../../sessions/16/16bc6ab760f963859107.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个文件全部生成完毕，保存在 `/root/autodl-tmp/vla-ssd/results/figure_data/`。

**产出汇总：**

| 文件 | 内容 |
|------|------|
| `fig_2x2_matrix.csv` | 5 行：4 个 VLA 条件 + DINO。trained_with_inst peak=0.4876@L9, trained_no_inst=0.489@L30, untrained_with_inst=0.4846@L12, untrained_no_inst=0.4802@L6, DINO=0.388 |
| `fig_siglip_vs_vla_vs_dino.csv` | 拆分为 global peak RSA 和 bootstrap task-mean + CI 两组列，因为两者度量不同。SigLIP=0.6153 [0.5257, 0.6954]（有CI），VLA 4 条件 peak 均在 0.48-0.49，DINO global=0.388 |
| `fig_perlayer_rsa.csv` | 33 层 × 4 条件 + DINO/SigLIP 参照线，完整数值 |
| `fig_probing_summary.csv` | 6 种方法的 trained/untrained/DINO 最佳结果 + delta |
| `fig_output_head.json` | 37 个组件（vision, projector, embedding, llm_L0-L31, llm_final_norm, lm_head）的 rel_change 和 cos_sim |

**注意事项：**
- `fig_siglip_vs_vla_vs_dino.csv` 做了修正：DINO 的 global peak RSA (0.388) 与 bootstrap CI (基于 per-task mean=0.6122) 来自不同聚合方式，不能混用。已分列存储，画图时注意选择一致的度量。SigLIP 的 CI 是 per-task bootstrap，与其 peak RSA (0.6153) 一致，因为 SigLIP 本身就是 per-task 计算的。
- with_inst 条件（rsa_results.json）没有 bootstrap CI 数据，only no_inst 条件有。

---
