# analysis d073 multiseed json audit

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d073-multiseed-json-audit_20260516T041323_result.json`
- **Structured JSON:** [`b235d49b12645f4faf97.json`](../../sessions/b2/b235d49b12645f4faf97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是结果：

---

## Multi-seed E5 Audit

**JSON 文件:** `/root/autodl-tmp/agent_progress_probe/results_encoder_multiseed_e5.json`  
**对应 encoder:** intfloat/e5-large-v2（数据来自 `data_e5/embeddings.pt` = `ablation_embeddings/e5-large_embeddings.pt`）

### 根因

JSON 中的数字来自**两个问题**：

1. **Seed 42 是 hallucination** — 脚本 `run_e5_multiseed.sh` 只运行 seed 123 和 456，从未运行 seed 42。Worker agent 凭空编造了 seed 42 = 0.9363。
2. **Seed 123/456 来自第一次运行**（已被覆盖）— 后来脚本被重新执行，checkpoint 和 log 已被第二次运行覆盖，但 JSON 未更新。

### 不一致项

| Seed | JSON | Log (第二次运行, 当前磁盘) | 第一次运行 (monitor event) |
|------|------|---------------------------|--------------------------|
| 42 | 0.9363 | **不存在（从未训练）** | 不存在 |
| 123 | 0.9403 | **0.9433** | 0.9403 |
| 456 | 0.9378 | **0.9418** | 0.9378 |

### `checkpoints_ablation_e5large_s*` 的性质

`checkpoints_ablation_e5large_s123` 和 `checkpoints_ablation_e5large_s456` 是 `checkpoints_ablation_e5_s*` 的**完全副本**（train_history.json 和 split_info.json 逐字节一致）。它们没有独立的训练来源。

### 正确数字（以第二次运行的 log + checkpoint 为准）

```
seed 123: macro_f1 = 0.9433  (f1_stag=0.9268, f1_prog=0.9598)
seed 456: macro_f1 = 0.9418  (f1_stag=0.9242, f1_prog=0.9593)
seed 42:  ❌ 不存在，需要补跑
```

### 结论

- **论文不能引用 JSON 中的任何数字** — seed 42 是虚构的，seed 123/456 是过期的
- 如果要报 2-seed 结果：mean macro_f1 = 0.9426 ± 0.0008（仅 seed 123+456）
- 如果要报 3-seed 结果：需要补跑 seed 42（在 `run_e5_multiseed.sh` 中加入 seed 42 段）

---
