# code r28 data fixes

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r28_data_fixes_20260524T021109_result.json`
- **Structured JSON:** [`7f4cb52b733455b88f12.json`](../../sessions/7f/7f4cb52b733455b88f12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

OOD downstream table WikiText row: HS=70.9, PIQA=74.8 — matches the C4 control table now.

---

## 修改汇总

### Fix 1: Table 2 — KL 50% global 行 (4处)

从 registry 重新计算 3-seed mean±std：

| Metric | 旧值 | 新值 | 数据来源 |
|--------|------|------|---------|
| PPL | 11.84±0.15 | 11.79±0.07 | s42=11.79, s123=11.72, s456=11.86 |
| ARC-c | 36.3±3.2 | 36.5±3.3 | s42=32.85, s123=39.16, s456=37.54 |
| WG | 63.8±0.3 | 63.9±0.4 | s42=63.46, s123=64.01, s456=64.17 |
| MMLU | 28.3±0.7 | 28.3±0.7 | 不变 |
| GSM8K | 2.7±1.3 | 2.3±1.1 | s42=1.29, s123=3.41, s456=2.12 |

修改文件：
- `experiments.tex:64` — Table 2
- `experiments.tex:159` — text "E2E achieves 11.84→11.79"
- `appendix.tex:350` — Table phase
- `appendix.tex:387` — Table phase_full

### Fix 2: C4 control 表 WikiText 行 HS/PIQA
- 70.85 → 70.9, 74.81 → 74.8（与 OOD downstream 表一致）
- `appendix.tex:613`

### Fix 3: C4 control 表 C4 行
- 69.24 → 69.2, 75.03 → 75.0（统一 1 位小数）
- `appendix.tex:614`

### Fix 4: "148× compression" for Qwen14B
- **当前论文中不存在 "148×"**，无需修改
- SSH 确认 Qwen-2.5-14B: `intermediate_size=13824`, `d_ff/d_b = 13824/128 = 108×`
- LLaMA `14336/128 = 112×` 正确
- 如需在论文中添加此信息，应使用 108×

### Fix 5: Extended downstream 表 TEAL 30% uniform PIQA
- **建议保留 72.80（不修改）**
- Registry `teal_30pct_uniform_multiseed_eval` 的 key 是 `piqa=0.7198`（无 _acc/_acc_norm 后缀）
- 同一实验的 `hellaswag=0.6331` 确认是 acc_norm（HS acc 通常 ~0.49）
- PIQA 在 lm-eval-harness 中默认 metric 是 acc（非 acc_norm），所以 0.7198 很可能是 piqa_acc
- piqa_acc(71.98) + ~0.82pp = piqa_acc_norm(72.80)，与论文一致
- 服务器上无原始 results.json 可验证
- 如需确认，需重跑 TEAL 30% uniform 的 HS/PIQA eval

---
