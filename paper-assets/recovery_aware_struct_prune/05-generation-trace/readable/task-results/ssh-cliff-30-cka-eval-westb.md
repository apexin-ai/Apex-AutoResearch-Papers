# ssh cliff 30 cka eval westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cliff_30_cka_eval_westb_20260523T113710_result.json`
- **Structured JSON:** [`a4371bef5ea35722ef1d.json`](../../sessions/a4/a4371bef5ea35722ef1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job 正常运行。

**汇报**：

| 项目 | 详情 |
|------|------|
| **服务器** | **westd-32935**（非 westb-23072，因 westb 上 7B 源模型不存在且数据盘仅剩 9.2GB） |
| **Pruned model** | **已有** — `/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_30/`（mode=cka_only, sparsity_actual=28.9%, 7.6B→5.4B params） |
| **GPU** | cuda:1（11066 MiB 占用） |
| **Eval PID** | 130690（tmux session: `eval_gsm8k_postprune_cka_only_30_n1319`） |
| **配置** | N=1319, greedy (temperature=0), bf16, max_new_tokens=2048, seed=42 |
| **Registry** | `eval_gsm8k_postprune_cka_only_30_n1319` → RUNNING |
| **预计完成** | ~1.5-2 小时（约 21:00-21:30 UTC+8），参考同服务器同规模 eval 的 ~3-5s/sample |

**westb-23072 无法执行的原因**：DeepSeek-R1-Distill-Qwen-7B 模型文件不存在（HF cache 仅有 refs，无 snapshots/blobs），数据盘 250G 已用 241G，无法下载模型（~14GB）也无法存放 pruned output（~10GB）。

---
