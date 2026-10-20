# ssh audit remaining checkpoints

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_audit_remaining_checkpoints_20260524T011651_result.json`
- **Structured JSON:** [`4e1f3c44a51d5fffcfae.json`](../../sessions/4e/4e1f3c44a51d5fffcfae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。汇总如下：

## Checkpoint 审计结果

| # | Checkpoint | 服务器 | 实际路径 | model.safetensors | 大小 | 可用 |
|---|-----------|--------|---------|-------------------|------|------|
| 1 | `sft_standard_20` | westd-32935 | `.../sft_standard_20/` | ✓ | 12G | ✓ |
| 2 | `sft_rasp_alpha0p5_20` | westd-32935 | `.../sft_rasp_alpha0p5_20/` | ✓ | 12G | ✓ |
| 3 | `sft_rasp_alpha3p0_20` | **westb-23072** | `.../sft_rasp_alpha3p0_20/checkpoint-935/` | ✓ | 12G | ✓ (注意子目录) |
| 4 | `sft_rasp_alpha4p0_20` | westd-32935 | `.../sft_alpha4_20/` | ✓ | 12G | ✓ (目录名无 rasp_ 前缀) |
| 5 | `grpo_rasp_alpha0p5_20` | **westb-23072** | `.../grpo_rasp_alpha0p5_20/` | ✓ | 12G | ✓ |
| 6 | `grpo_rasp_alpha3p0_20` | — | **不存在** | ✗ | — | **✗ 缺失** |
| 7 | `grpo_rasp_alpha4p0_20` | westd-32935 | `.../grpo_alpha4_20/` | ✓ | 12G | ✓ (目录名无 rasp_ 前缀) |
| 8 | `sft_cka_only_25` | westd-32935 | `.../sft_cka_only_25/` | ✓ | 11G | ✓ |

## 结论

**7/8 可直接提交 eval**，需要注意：
- `sft_rasp_alpha3p0_20` 和 `grpo_rasp_alpha0p5_20` 在 westb-23072 上，eval 脚本需指向该服务器或先 SCP 到 westd-32935
- `sft_rasp_alpha3p0_20` 的模型在 `checkpoint-935/` 子目录下，路径需包含该子目录
- `sft_alpha4_20` 和 `grpo_alpha4_20` 目录名无 `rasp_` 前缀，eval 配置需对应调整

**1 个缺失：`grpo_rasp_alpha3p0_20`** — westd-32935 上的 `grpo_rasp_alpha3p0_20_v2` 只有 README.md 和 completions/，无模型权重；westb-23072 上完全没有该目录。需要重新训练或确认该 checkpoint 是否在其他位置。

---
