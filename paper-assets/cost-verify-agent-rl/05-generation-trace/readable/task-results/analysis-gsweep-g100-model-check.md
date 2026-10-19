# analysis gsweep g100 model check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gsweep_g100_model_check_20260523T183630_result.json`
- **Structured JSON:** [`e6e90cfd36dcccdd86b0.json`](../../sessions/e6/e6e90cfd36dcccdd86b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：Registry 记录错误。**

所有 4 个 gamma sweep 配置（g050/g080/g095/g100）使用的模型路径完全一致：

```
model_path: /root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4
```

这是 Qwen3-1.7B SFT 模型。g100 实验实际用的也是 Qwen3-1.7B，不是 Qwen2.5-3B。Registry 中 `gsweep_g100_h5_seed1` 标记为 Qwen2.5-3B 是记录错误，需要修正。

---
