# analysis ssr computation

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ssr_computation_20260527T113223_result.json`
- **Structured JSON:** [`4e8fd64b7da5fa74635f.json`](../../sessions/4e/4e8fd64b7da5fa74635f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here are the results:

| Condition | Seeds | TSR | CAR | SSR |
|-----------|-------|-----|-----|-----|
| Pi0.5 baseline | 1 | 71.5% | 71.5% | 28.0% |
| LoRA s0 30K | 1 | 51.5% | 43.5% | 29.5% |
| LoRA s1 30K | 1 | 51.5% | 47.5% | 27.0% |
| SDF λ=0.005 s0 30K | 1 | 55.5% | 43.0% | 30.0% |
| SDF λ=0.005 s1 30K | 1 | 50.5% | 46.0% | 24.0% |
| SDF λ=0.005 s2 30K | 1 | 56.0% | 47.5% | 29.5% |
| SDF λ=0.01 s0 30K | 1 | 52.5% | 43.0% | 32.5% |
| SDF λ=0.01 s1 30K | 1 | 55.5% | 42.5% | 30.0% |
| SDF λ=0.01 s2 30K | 1 | 53.5% | 45.5% | 28.0% |
| SDF λ=0.1 s0 30K | — | — | — | **JSON 被覆盖，无法计算** |
| SDF λ=0.1 s1 30K | 1 | 49.0% | 41.5% | 26.5% |

**说明：**
- SDF λ=0.1 s0 30K 的 JSON 被三次写入同一文件 `eval_safelibero_object_all_levelII_30000_lora_baseline_seed7.json` 覆盖（s0→reeval_lora→s1），当前文件内容为 s1 数据。日志仅记录了 TSR=47%/CAR=58%，无 per-episode 数据，无法算 SSR。
- 所有 `reeval_*` 文件来自 westd-45947（May 26 reeval 批次），SDF λ=0.1 s1 来自 westd-35807。

**按条件平均：**

| Condition | Avg TSR | Avg CAR | Avg SSR |
|-----------|---------|---------|---------|
| Pi0.5 baseline | 71.5% | 71.5% | 28.0% |
| LoRA (2 seeds) | 51.5% | 45.5% | 28.3% |
| SDF λ=0.005 (3 seeds) | 54.0% | 45.5% | 27.8% |
| SDF λ=0.01 (3 seeds) | 53.8% | 43.7% | **30.2%** |
| SDF λ=0.1 (1 seed) | 49.0% | 41.5% | 26.5% |

**关键发现：** Baseline 虽然 TSR=71.5%，但 CAR 也高达 71.5%，导致 SSR 仅 28.0%。SDF λ=0.01 的 SSR=30.2% 是所有条件中最高的——尽管 TSR 下降到 53.8%，但 CAR 大幅降低到 43.7%，使得"安全完成任务"的比例反而更高。这直接回应了 reviewer 的 "reduced exposure" 质疑：模型不是因为"做得少"而碰撞少，而是在维持甚至提高安全完成率的同时减少了碰撞。

---
