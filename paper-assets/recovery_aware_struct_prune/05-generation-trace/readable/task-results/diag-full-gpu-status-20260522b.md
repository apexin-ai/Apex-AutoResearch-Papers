# diag full gpu status 20260522b

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_full_gpu_status_20260522b_20260522T052149_result.json`
- **Structured JSON:** [`29345431bb50e23cfff1.json`](../../sessions/29/29345431bb50e23cfff1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westb-23072 (2× RTX PRO 6000, 96GB each)

| GPU | 显存占用 | GPU-Util | PID | 任务 | 进度 |
|-----|---------|----------|-----|------|------|
| cuda:0 | 4,239 / 97,887 MiB | 95% | 147029 | eval_math500_sft_standard_20_1p5b | **130/500** (26%), ~49min elapsed, ETA ~2.5h |
| cuda:1 | 4,281 / 97,887 MiB | 96% | 147313 | eval_math500_sft_rasp_20_1p5b | **145/500** (29%), ~49min elapsed, ETA ~2.3h |

---

## westd-32935 (4× RTX PRO 6000, 96GB each)

| GPU | 显存占用 | GPU-Util | PID | 任务 | 进度 |
|-----|---------|----------|-----|------|------|
| cuda:0 | 17,541 / 97,887 MiB | 93% | 2234 | eval_math500_grpo_standard_20_fair_2048_v2 | **114/500** (23%), Acc@100=0.34, ~1h32m elapsed, ETA ~5h |
| cuda:1 | 15,329 / 97,887 MiB | 96% | 5241 | eval_math500_sft_random_20_v3 | **61/500** (12%), ~1h09m elapsed, ETA ~8h+ |
| cuda:2 | 16,507 / 97,887 MiB | 97% | 3586 | eval_gsm8k_sft_alpha4_20_v5 | **1176/1319** (89%), Acc@1150=0.6261, ~1h26m elapsed, ETA ~7min |
| cuda:3 | 16,507 / 97,887 MiB | 91% | 2737 | eval_gsm8k_grpo_alpha4_20_v3 | **1303/1319** (99%), Acc@1300=0.6292, ~1h30m elapsed, ETA <1min |

**要点**：
- westd-32935 cuda:3 (gsm8k_grpo_alpha4_20_v3) 即将完成
- westd-32935 cuda:2 (gsm8k_sft_alpha4_20_v5) ~7min 内完成
- westb-23072 两张卡显存占用很低 (4GB)，是 1.5B 模型评测
- westd-32935 cuda:0/1 的 MATH-500 评测还需较长时间（生成长度大，每题 ~60-100s）

---
