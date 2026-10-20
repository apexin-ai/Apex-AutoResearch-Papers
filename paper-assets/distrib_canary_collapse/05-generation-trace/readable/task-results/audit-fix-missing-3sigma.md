# audit fix missing 3sigma

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_fix_missing_3sigma_20260520T020753_result.json`
- **Structured JSON:** [`386a377a0140cc7e10fa.json`](../../sessions/38/386a377a0140cc7e10fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已存在且内容正确。我独立验证了所有数据：

**验证结果：**
1. `3sigma_recompute_d105_17855.json` 仅包含 3 个实验（scale_69b、qwen35_08b、padding），不含 Pythia-410M s43
2. 使用 `recompute_3sigma_d105.py` 中的 `onset_gen_3sigma` 算法对 Pythia-410M s43 重算：threshold_3σ = **0/8**（所有 downstream 均未突破 3σ，canary onset: te=gen2, ece=gen4）
3. 任务描述中 Pythia-410M s43 的 "threshold=2/8" 实际是 s42 的数据，s43 确认为 0/8

**修正后 K 值汇总：**

| 实验 | thresh_3σ | K≥3 (2σ→3σ) | K≥4 (2σ→3σ) |
|------|-----------|-------------|-------------|
| Pythia-6.9B s42 | 2/8 | 5/8 → **3/8** | 1/8 → **0/8** |
| Qwen3.5-0.8B s42 | 0/8 | 8/8 → **3/8** | 3/8 → **0/8** |
| Padding-410M s42 | 0/8 | 6/8 → **0/8** | 0/8 → **0/8** |
| Pythia-410M s43 | 0/8 | 6/8 → **0/8** | 0/8 → **0/8** |

`artifacts/table7_missing_3sigma_fix.md` 已包含完整的 per-pair 原始数据、修正后 K 值表格和汇总，无需更新。

---
