# eval seed300 step5 ood bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_seed300_step5_ood_bjb1_20260522T175535_result.json`
- **Structured JSON:** [`20a67ed14a37742663dc.json`](../../sessions/20/20a67ed14a37742663dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval is running — model loaded on cuda:0 (8133 MiB), cuda:1 untouched. Environment loading in progress.

## 结果汇总

### 1. FSDP → HF 转换
- 完成，311 parameters，2.03B params (4.06 GB bf16)
- 输出: `/root/autodl-tmp/checkpoints/exp029_seed300_step5_hf/`
- Symlink: `qwen_exp029_seed300_step5_hf` → `exp029_seed300_step5_hf`

### 2. OOD Eval 启动
- **PID**: 439148 (TaskRunner: 441087)
- **GPU**: cuda:0, 8133 MiB used
- **Config**: `_alfworld_seed300_step5_ood_eval.yaml`
- **Log**: `/root/autodl-tmp/logs/seed300_step5_ood_eval.log`
- 134 AlfworldSG_OOD tasks, temp=0.4, val_only=True

### 3. Seed300 训练 Metrics

| Metric | Step 0 | Step 5 | Delta |
|--------|--------|--------|-------|
| pass@1 | 12.5% | **25.0%** | +12.5pp |
| action_is_valid | 78.3% | 66.3% | -12.0pp |
| response_length (val) | 7088 | 6203 | -885 |
| reward/mean@32 | 1.25 | 2.50 | +1.25 |

### 4. 判断: **Healthy**
- pass@1 从 12.5% 翻倍到 25.0%（+12.5pp），明确提升
- action_is_valid 下降 12pp 值得关注，但 pass@1 提升说明模型学到了更有效的策略（虽然 validity 下降，但成功率提升）
- response_length 缩短说明模型行为更紧凑

---
