# submit gated isr dual pilot

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_gated-isr-dual-pilot_20260516T141922_result.json`
- **Structured JSON:** [`455975abdaa97c3833a4.json`](../../sessions/45/455975abdaa97c3833a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行，汇报如下：

**GPU 状态**
| GPU | Memory | Util | PID |
|-----|--------|------|-----|
| 0 (s42) | 81,638 / 97,887 MiB (83%) | 97% | 860451 |
| 1 (s43) | 82,250 / 97,887 MiB (84%) | 97% | 860525 |

**训练进度**（启动 ~45s 后）
- **s42**: step 8/500, ~5.25s/step
- **s43**: step 12/500, ~3.73s/step

**Step metrics（早期）**
- reward: 0.0（正常，模型尚未学会生成可证明的 FOL）
- prove_rate: 0.0–0.125
- gate_pass: 0.000（ISR gate 尚未通过，符合预期——需要先学会证明才能触发 gate）
- parse_rate: 0.0–1.0

**修复记录**：原 config `per_device_batch_size=2` 改为 1 后触发 TRL 验证错误（`generation_batch_size=4` 不能被 `num_generations=8` 整除）。修复：在 GRPOConfig 中显式设置 `generation_batch_size=num_generations`（=8），保持 effective batch = 1×8×4 = 32 不变。

无 OOM，训练正常推进。预估 500 步约 30–45 分钟完成。

---
