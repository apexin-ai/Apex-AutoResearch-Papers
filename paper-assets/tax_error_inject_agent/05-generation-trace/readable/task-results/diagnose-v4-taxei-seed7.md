# diagnose v4 taxei seed7

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_v4-taxei-seed7_20260515T153530_result.json`
- **Structured JSON:** [`597cf5a7e01dbc7c968e.json`](../../sessions/59/597cf5a7e01dbc7c968e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：v4-taxei-seed7 训练成功完成，无需重跑。**

误报原因：cron 采集 metrics 时训练刚启动（step 180/3387, 5%），之后训练正常跑完全部 3387 steps。

关键指标：
- train_loss: 0.3568, final step loss: 0.1753
- token_acc: 0.9009 (avg), 0.9328 (final)
- 训练时长: 1h 49m 52s, 无 OOM/error
- checkpoint: `/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4_seed7/v0-20260515-214039/checkpoint-3387`
- 未使用 wandb
- cuda:3 当前空闲

Registry 已更新为 DONE/success，诊断报告已写入 artifacts。

---
