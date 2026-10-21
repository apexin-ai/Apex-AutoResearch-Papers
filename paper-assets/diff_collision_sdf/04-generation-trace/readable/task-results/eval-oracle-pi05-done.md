# eval oracle pi05 done

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_oracle-pi05-done_20260529T013126_result.json`
- **Structured JSON:** [`abe67761a9ec8338fa24.json`](../../sessions/ab/abe67761a9ec8338fa24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

### Oracle Pi0.5 Eval 结果 (eval_oracle_pi05_lora_s0)

| Task | TSR | CAR | LoRA s0 CAR | Δ CAR |
|------|-----|-----|-------------|-------|
| 0 OJ | 25.0% | 50.0% | 68% | **-18%** |
| 1 CP | 90.0% | 75.0% | 74% | +1% |
| 2 Milk | 27.5% | 70.0% | 66% | +4% |
| 3 BBQ | 60.0% | 12.5% | 20% | **-7.5%** |
| **Overall** | **50.6%** | **51.9%** | **57.0%** | **-5.1%** |

假设验证通过：Oracle SDF refinement 确实降低了 Pi0.5 LoRA 的 overall CAR（57.0% → 51.9%），支持 Claim 2。BBQ 和 OJ 是主要受损任务（CAR 分别下降 7.5% 和 18%），CP 和 Milk 基本持平或微升。

---
