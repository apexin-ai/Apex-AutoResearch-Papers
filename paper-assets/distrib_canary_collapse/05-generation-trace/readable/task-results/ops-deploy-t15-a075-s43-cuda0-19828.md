# ops deploy t15 a075 s43 cuda0 19828

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-t15-a075-s43-cuda0-19828_20260523T063939_result.json`
- **Structured JSON:** [`3d1c1c2192a51b9f0012.json`](../../sessions/3d/3d1c1c2192a51b9f0012.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

参数与 parent 完全一致，仅 seed=43 和 output_dir 不同。

**部署完成：**

| 项目 | 值 |
|------|-----|
| exp_id | scale_14b_t15_a075_s43_fp32 |
| PID | 857058 |
| GPU | cuda:0 (10,284 MiB / 97,887 MiB) |
| tmux session | `t15_a075_s43` |
| output_dir | `results/phase_diagram/t15_a075_s43_fp32_14b/` |
| seed | 43 |
| 其他参数 | T=15, α=0.75, fp32, steps=5000, gen_batch=8 |

注意：`tee` 日志写入失败（输出目录创建晚于 tee 启动），但训练进程正常运行。可通过 `tmux attach -t t15_a075_s43` 查看实时输出。预计运行约 17-18h（参考 parent s42 从 20:37 到 14:15）。

---
