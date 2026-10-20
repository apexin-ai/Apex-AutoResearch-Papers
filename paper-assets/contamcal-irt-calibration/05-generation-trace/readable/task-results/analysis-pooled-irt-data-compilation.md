# analysis pooled irt data compilation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pooled-irt-data-compilation_20260515T194224_result.json`
- **Structured JSON:** [`50e15ac69a88d8902aeb.json`](../../sessions/50/50e15ac69a88d8902aeb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**不能直接启动 IRT fitting。** 主要阻塞项：

**当前状态**: alpha=32 一致的 IRT 候选模型 20 个，但 3B 只有 4 个（缺 4 个），导致主 benchmark 全部不达标：
- MMLU: N=12 (需16)
- GSM8K: N=15 (需16)
- ARC-C: N=12 (需16)
- HumanEval: N=20 ✓ (但已降级为 appendix)

**4 个阻塞项**:

| 阻塞项 | 状态 | 预计解决 |
|--------|------|---------|
| 3B d025_a32_s42 SFT 重训 | 训练中 ~2% (68/3384步) | ~4h |
| 3B d100_a32_s42 SFT 重训 | lora_adapter 空，未开始/失败 | 需排查 |
| 3B d100_a32_s123 SFT 重训 | lora_adapter 空，未开始/失败 | 需排查 |
| 3B d000_s42 aligned eval | checkpoint 就绪 (alpha=32)，eval 未跑 | 可立即启动 |

**可立即执行**: 3B d000_s42 的 aligned eval（checkpoint 存在且 alpha=32 确认）。

**额外风险**: 现有 IRT 脚本 (`run_irt_calibration.py`) **没有 alpha 过滤**，直接运行会混入 alpha=16 的 3B v2 eval（违反 D055）。跑 IRT 前需要加 exclusion 或归档 alpha=16 eval 目录。

详细清单已注册: `artifacts/_project/report/irt_data_readiness.md`

---
