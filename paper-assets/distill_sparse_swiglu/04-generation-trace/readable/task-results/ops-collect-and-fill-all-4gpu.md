# ops collect and fill all 4gpu

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-and-fill-all-4gpu_20260518T095855_result.json`
- **Structured JSON:** [`208c173dce9ba68f6247.json`](../../sessions/20/208c173dce9ba68f6247.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 卡确认运行正常。

## 汇总

### P0: 结果收集完成

| 实验 | wikitext2_ppl | arc_norm | wino | mmlu | gsm8k | 状态 |
|---|---|---|---|---|---|---|
| kl_comp_30pct_s42_eval | 8.98 | 0.3993 | 0.6898 | 0.2531 | 0.0842 | DONE ✓ |
| kl50_s42_uniform_eval | 11.96 | 0.3259 | 0.6235 | 0.2792 | 0.0197 | DONE ✓ |
| kl_comp_30pct_s123 (41718) | — | — | — | — | — | 已验证 checkpoint 存在 ✓ |

### P1: 4 卡全部填满

| GPU | 实验 | 类型 | 状态 |
|---|---|---|---|
| 34887:0 | kl_comp_30pct_s123_eval | downstream benchmark | 正在跑 arc_challenge ✓ |
| 34887:1 | kl50_s456_uniform_eval | downstream benchmark | 模型加载中 ✓ |
| 41718:0 | kl_comp_30pct_s456 | compensation 训练 | step 100/1000 ✓ |
| 41718:1 | kl_comp_50pct_s42 | compensation 训练 (50% sparsity) | 刚启动 ✓ |

34887 首次提交因 httpx 客户端 bug 崩溃，加 `HF_HUB_OFFLINE=1` 后修复。41718 cuda:1 无现成 eval 可跑，提交了 50% sparsity compensation 训练（探索 compensation 在高 sparsity 下是否也有效）。

---
