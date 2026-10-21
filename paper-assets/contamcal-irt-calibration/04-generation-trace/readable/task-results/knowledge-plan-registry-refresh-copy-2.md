# knowledge plan registry refresh

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_plan-registry-refresh_20260515T200819_result.json`
- **Structured JSON:** [`e46eb6786870b4316a3b.json`](../../sessions/e4/e46eb6786870b4316a3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。

**汇总：**

| 指标 | 更新前 | 更新后 |
|------|--------|--------|
| **Claim 1** | 14.3% (1/7) | **28.6% (2/7)** |
| **Claim 2** | 0% (0/5) | **60.0% (3/5)** |
| **Claim 3** | 0% (0/1) | 0% (0/1) |
| **Overall** | 7.7% (1/13) | **38.5% (5/13)** |
| Orphaned | 1 | **0** |

**更新了 6 个 plan entry 的 registry_id：**
- exp-001: `exp_001_sft_d100_15B_v2` → `exp_001_sft_injection`（更准确的 umbrella 实验）
- exp-002: 空 → `exp_002_signals_05B` ✓ (Claim 2 +1)
- exp-003: 空 → `exp_003_rrf_05B` ✓ (Claim 2 +1)
- exp-006: 空 → `exp_006_irt_05B_gsm8k` ✓ (Claim 1 +1)
- exp-008: 空 → `exp_008_signal_survival_v4` ✓ (Claim 2 +1)
- exp-015: `exp_001_sft_d100_qc_only`(orphaned) → `null`

**未能提升的：**
- exp-004 (sim sweep): 全 6 版均 failed，保留原 ID
- exp-005 (noise prop): 全版本 failed/negative，保留原 ID
- Claim 3 仍 0%——唯一实验 exp-005 无成功版本

---
