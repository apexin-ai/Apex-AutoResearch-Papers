# prepare remaining math500 fixed evals

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prepare_remaining_math500_fixed_evals_20260524T042704_result.json`
- **Structured JSON:** [`046ca91d7b6eaae58f5d.json`](../../sessions/04/046ca91d7b6eaae58f5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-29022 不可连接。汇总结果：

| 实验 | 预期路径 | 实际位置 | 状态 |
|------|---------|---------|------|
| `sft_cka_only_25` | westd-32935: `.../sft_cka_only_25` | **westd-32935** (root level, 有 config.json) | ✅ 可用 |
| `grpo_rasp_alpha0p5_20` | westd-32935: `.../grpo_rasp_alpha0p5_20` | **westb-23072** (root level, 有 config.json) | ⚠️ 需迁移 |
| `sft_rasp_alpha3p0_20` | westd-32935: `.../sft_rasp_alpha3p0_20/checkpoint-935` | **westb-23072** (checkpoint-935/config.json 存在) | ⚠️ 需迁移 |
| `grpo_rasp_alpha3p0_20_v2` | westd-32935: `.../grpo_rasp_alpha3p0_20_v2/checkpoint-100` | westd-32935 仅有 README.md + completions/（旧 eval 输出）；westb-23072 不存在；westd-29022 不可连接 | ❌ 缺失 |
| `grpo_alpha4_20` | westd-32935: `.../grpo_alpha4_20/checkpoint-100` | **westd-32935** root level 有完整模型文件（config.json, model.safetensors），但无 checkpoint-100 子目录 | ⚠️ 路径修正 |

### 结论

**可直接提交（1个）：**
- `sft_cka_only_25` — westd-32935 上就绪

**需路径修正（1个）：**
- `grpo_alpha4_20` — 模型在 `.../grpo_alpha4_20/`（非 checkpoint-100 子目录），eval 脚本路径改为根目录即可

**需 SCP 迁移到 westd-32935（2个）：**
- `grpo_rasp_alpha0p5_20` — 从 westb-23072 迁移
- `sft_rasp_alpha3p0_20/checkpoint-935` — 从 westb-23072 迁移

（或者这两个直接在 westb-23072 上跑 eval）

**checkpoint 缺失（1个）：**
- `grpo_rasp_alpha3p0_20_v2/checkpoint-100` — 三台服务器均无完整模型。westd-29022 已关机无法连接。需要重新训练，或确认该 checkpoint 是否曾存储在其他路径。

---
