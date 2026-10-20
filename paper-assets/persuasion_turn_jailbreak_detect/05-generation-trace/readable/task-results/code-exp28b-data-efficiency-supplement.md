# code exp28b data efficiency supplement

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp28b-data-efficiency-supplement_20260520T155601_result.json`
- **Structured JSON:** [`823151b868f9c4013ad7.json`](../../sessions/82/823151b868f9c4013ad7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已提交，状态：

- **PID**: 73186
- **日志**: `/tmp/exp28b.log`
- **Registry**: `exp28b_data_efficiency_supplement` → RUNNING
- **预计时间**: ~3h（10 个 run 串行）

**训练矩阵**：
| 条件 | N=50 | N=125 | N=250 | N=350 |
|------|------|-------|-------|-------|
| 9-class s123 | 运行中 | pending | pending | pending |
| 9-class s456 | pending | pending | pending | pending |
| vanilla s42 | pending | — | pending | — |

脚本设计：
- 9-class: `data_seed=42`（相同数据子集），`model_seed=123/456`（不同模型初始化）
- Vanilla: `data_seed=42, model_seed=42`，补 N=50 和 N=250
- 每个 run 完成后保存中间结果到 `results/exp28b_intermediate.json`
- 全部完成后自动合并 exp28+exp28b 到 `results/exp28_combined_data_efficiency.json`，含 mean±std 汇总

可以用 `tail /tmp/exp28b.log` 随时查看进度。

---
