# code e1c resume sft pipeline

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e1c_resume_sft_pipeline_20260518T123442_result.json`
- **Structured JSON:** [`5cd18cae460746c85e67.json`](../../sessions/5c/5cd18cae460746c85e67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终状态汇报

**SFT pipeline 无需恢复 — 三个 1.5B SFT 全部完成。**

| 模型 | 状态 | 权重验证 | Registry |
|------|------|----------|----------|
| sft_cka_only_20_1p5b | 完成 (12:09) | shapes match per_layer_intermediate_size | DONE/success |
| sft_standard_20_1p5b | 完成 (12:17) | OK | DONE/success |
| sft_rasp_20_1p5b | 完成 (12:29) | OK | DONE/success |

**GPU 占用：**
- **cuda:0**: PID 803652 — `eval_gsm8k.py` on pruned_standard_20_1p5b (quick, max_samples=100), 3.6GB, ~4min
- **cuda:1**: PID 765350 — `eval_math500.py` on grpo_cka_only_20, 30.6GB, 435/500 (87%), 预计 1-2h 完成

**磁盘**: 98% (5.8G free)

前一个 worker 的 SFT 训练和 registry 更新已全部完成，失败点应在后续步骤。

---
