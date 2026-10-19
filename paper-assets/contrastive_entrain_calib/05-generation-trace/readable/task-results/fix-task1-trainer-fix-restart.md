# fix task1 trainer fix restart

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_task1-trainer-fix-restart_20260518T163237_result.json`
- **Structured JSON:** [`fda7b3ca022c08c957d7.json`](../../sessions/fd/fda7b3ca022c08c957d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常训练。

---

## 产出总结

### 1. Trainer 文件路径 + 修改概要

**文件**: `/root/mvp_v2_1_expanded/training/dcgrpo_trainer.py`（原文件已损坏，从 .pyc 字节码反向工程重建 + 修复）

**关键 diff**:

| 修复项 | 原代码 | 修复后 |
|--------|--------|--------|
| **Fix A: R3 反转** | 两个 hypothesis（"revised" vs "maintained"），无反转 | 统一 hypothesis + `_extract_last_response()` + invalid_pressure 时 `R3 = 1 - P(entail)` |
| **Fix B: R2 权重** | DCGRPOConfig: r1=0.5, r2=0.3 | r1=0.25, r2=0.0, r3=0.75; compute_rewards 中 r2_weight==0 时跳过 R2 计算 |
| **Fix C: NLI 模型** | 默认 `microsoft/deberta-v3-base`; DebertaV2Tokenizer 无 fallback | 默认 `cross-encoder/nli-deberta-v3-base`; DebertaV2Tokenizer → AutoTokenizer fallback; 动态检测 entailment index |

### 2. R3 反转 Sanity Test

```
Case 1: valid_correction, raw_nli=0.8 → R3=0.80 [PASS]
Case 2: invalid_pressure, raw_nli=0.8 → R3=0.20 [PASS - correctly penalized]
Case 3: valid_correction, raw_nli=0.2 → R3=0.20 [PASS - correctly low]
Case 4: invalid_pressure, raw_nli=0.2 → R3=0.80 [PASS - correctly rewarded]
Config defaults PASS, _extract_last_response PASS
```

### 3. 训练脚本修改确认

- **exp-002**: R1=0.25, R2=0.0, R3=0.75, num_generations=2, max_completion_length=256
- **exp-003**: R1=0.0, R2=0.0, R3=1.0, num_generations=2, max_completion_length=256

### 4. 旧进程 Kill 确认

PID 63704 和 63563 已终止。

### 5. 新 tmux session + PID

| 实验 | tmux session | PID | GPU |
|------|-------------|-----|-----|
| exp-002 | `exp002` | 69020 | cuda:0 |
| exp-003 | `exp003` | 69094 | cuda:1 |

### 6. 前 3 步 R1/R2/R3 日志值 (exp-002)

| Step | R1 mean | R2 mean | R3 mean | Combined |
|------|---------|---------|---------|----------|
| 0 | -0.2051 | 0.0000 | 0.2775 | 0.1569 |
| 1 | -0.3367 | 0.0000 | 0.5686 | 0.3423 |
| 2 | -0.6237 | 0.0000 | **0.8354** | 0.4706 |

R3 从 0.28 → 0.57 → 0.84 快速上升，反转逻辑生效。R2 = 0 符合预期。exp-003 正常运行（R3-only 模式，无详细 reward 日志但步进正常）。

---
