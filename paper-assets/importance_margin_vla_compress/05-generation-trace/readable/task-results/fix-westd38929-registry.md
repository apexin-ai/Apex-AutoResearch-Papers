# fix westd38929 registry

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd38929_registry_20260525T072734_result.json`
- **Structured JSON:** [`548922274f695d12092b.json`](../../sessions/54/548922274f695d12092b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

There's no `register_cron` MCP tool available — the experiment monitoring cron registration isn't possible through the current toolset. The registry has been fixed with all provenance metadata. Here's the summary:

## Report

| Experiment | GPU | PID | Progress | Last Task SR | Registry |
|---|---|---|---|---|---|
| `eval_openvla_attn_k09_long_seed42_v3` | 0 | 2508 | Task 4/10 (starting) | Task 3: 34.0% | RUNNING ✓ |
| `eval_openvla_attn_k085_long_seed42_v3` | 1 | 2583 | Task 4/10 (Ep 10/50) | Task 3: 56.0% | RUNNING ✓ |
| `eval_openvla_random_k09_long_seed42_v3` | 2 | 2763 | Task 4/10 (Ep 10/50) | Task 3: 62.0% | RUNNING ✓ |
| `eval_openvla_l2norm_k09_long_seed42_v3` | 3 | 2944 | Task 4/10 (starting) | Task 3: 52.0% | RUNNING ✓ |

**Registry fixes applied:**
- All 4 entries previously had `failure_reason: "startup recovery: RUNNING with no cron and no server/pid info"` — they were auto-failed by the system due to missing provenance
- Updated hypotheses for all 4
- Updated specs with correct `pid`, `gpu`, `log_path`, `server` for each
- Status confirmed RUNNING for all 4

**Not done:** `register_cron` monitoring — no such MCP tool exists. If you want session-based polling via CronCreate, let me know.

---
