# diagnose and submit d112 step3 to step4

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_and_submit_d112_step3_to_step4_20260519T073210_result.json`
- **Structured JSON:** [`968400766221f11ed64b.json`](../../sessions/96/968400766221f11ed64b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**Step 3 训练完成 (d112_rsft_s44_train → DONE/success)**
- 567/567 steps 完成，final train_loss = 0.6488
- 最后 5 步 loss 稳定：0.6359 → 0.6684 → 0.6495 → 0.6461 → 0.6488
- Checkpoint: `/root/autodl-tmp/rsft_output_4b_sft_s44/checkpoint-567/`（adapter_model.safetensors 252MB）

**Step 4 eval 已提交 (d112_rsft_s44_eval)**
- GPU: cuda:0（提交前 0 MiB，符合 C001）
- PID: 627505，tmux session: d112_rsft_s44_eval
- Cron 已注册，120s 轮询
- 预期目标: ign_f1 > 0.4734 (SFT s44 baseline)

---
