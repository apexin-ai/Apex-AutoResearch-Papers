# deploy exp 076 debate mistral folio

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp-076-debate-mistral-folio_20260519T172805_result.json`
- **Structured JSON:** [`2f7872475658ca350679.json`](../../sessions/2f/2f7872475658ca350679.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**汇报：**

- **vLLM**：在 cuda:3 port 8003 启动成功（加了 `--enforce-eager` + `VLLM_USE_FLASHINFER_SAMPLER=0` 绕过 Blackwell 架构下 FlashInfer 不兼容问题）
- **实验**：tmux session `exp076_run` 已启动，正在处理 204 条 FOLIO 数据（日志确认 [1/204] 开始推理）
- **Registry**：`exp-076-debate-mistral-folio` 状态 RUNNING
- **参数修正**：任务描述的 `--k-debate 4 --n-rounds 3` 实际对应 `--n-debates 4`（脚本内置 3 轮辩论，无 `--n-rounds` 参数）
- **监控**：`tail -f /root/symb_invariant_consensus/results/exp076_debate_mistral_folio/run.log`

---
