# pipeline seed5 fsdp hf and ood eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_pipeline_seed5_fsdp_hf_and_ood_eval_20260521T140048_result.json`
- **Structured JSON:** [`67ce5a2b3ee9e95ae45c.json`](../../sessions/67/67ce5a2b3ee9e95ae45c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 3 已加载 8.8GB，模型正在加载中（vLLM 还会继续分配）。

### 产出汇总

| 项目 | 结果 |
|------|------|
| FSDP→HF 转换 | 成功，311 params, 2.03B, bf16, `/root/autodl-tmp/checkpoints/exp029-seed5/global_step_10_hf/` |
| 符号链接 | `qwen_exp029_seed5_step10_hf` → `global_step_10_hf` |
| Eval 配置 | `_alfworld_exp029_seed5_ood_eval.yaml`，YAML 验证通过 |
| Eval PID | 375913（子进程 TaskRunner=382535, WorkerDict=383150） |
| GPU 使用 | 0,1: Seed 7 训练 (97GB) / 2: Seed 6 eval 已完成或空闲 / 3: Seed 5 eval 加载中 (8.8GB↑) |
| 日志 | `/tmp/exp029_seed5_ood_eval.log` |

GPU 2 (Seed 6 eval) 显示 0 MiB——可能已经跑完了，建议确认一下 PID 342378 状态。

---
