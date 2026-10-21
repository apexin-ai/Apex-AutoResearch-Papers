# check eval ss s123 results

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_ss_s123_results_20260523T173042_result.json`
- **Structured JSON:** [`ccc57546604376e04e90.json`](../../sessions/cc/ccc57546604376e04e90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the report:

---

## TF Eval 结果 (SS s123, epoch 2)

- 状态: **TF 完成, AR 进行中**

| Config | Turn 1 GAR | PPL |
|--------|-----------|-----|
| Base + GAR-ours | 0.1008 | 3.96 |
| Base + GAR-dongre | 0.0075 | 3.96 |
| **SS s123 + GAR-ours** | **0.5536** | **2.61** |
| **SS s123 + GAR-dongre** | **0.4106** | **2.61** |

Mid-turns avg GAR: 全部 NaN（num_turns=2，无 mid-turns 可测）

## Gate Dynamic Range (TF, SS s123)

门控 turn1→turn15 偏移最大的层：
- L19: 0.175 → 0.973 (diff **-0.798**)
- L24: 0.400 → 0.978 (diff -0.578)
- L6: 0.421 → 0.947 (diff -0.526)
- L9: 0.502 → 0.935 (diff -0.433)

## s42 AR 参考（用于后续 s123 AR 对比）

| Beta | Base | SS s42 | SS s42 CI |
|------|------|--------|-----------|
| 0.0 | 0.019 | **0.347** | [0.327, 0.366] |
| 3.0 | 0.531 | **0.593** | [0.574, 0.613] |
| 5.0 | 0.704 | **0.717** | [0.696, 0.738] |

## AR Eval 状态

- AR 1/2 (SS s123 beta=0,3,5): **正在运行** (PID 110052, 29.5GB VRAM, 58% GPU util)
- AR 2/2: 未开始
- 无 AR 结果文件产出（仍在生成中）

## GPU 链状态

- **Step 1/7** (SS s123 eval): TF ✓, AR 进行中
- Step 2/7 (SS s456 resume training): 未开始
- Steps 3-7: SS s456 eval → Qwen-1.5B phase1 → Qwen-1.5B TG → Qwen-1.5B eval → MMLU eval

链脚本 `scripts/gpu_chain_next.sh` 使用 `set -e`，各步骤串行执行，AR eval 完成后会自动推进到 Step 2。

---
