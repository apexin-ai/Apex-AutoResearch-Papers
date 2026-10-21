# ops ty registry sync batch

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_ty_registry_sync_batch_20260520T202351_result.json`
- **Structured JSON:** [`c39e1e54c30c0ee26778.json`](../../sessions/c3/c39e1e54c30c0ee26778.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成汇总

**62/62 个 registry metrics 更新全部成功。**

### 关键发现

| 类别 | 数量 |
|------|------|
| 更新成功 | 62 |
| 无需更新（已一致） | 3 (`t20_a045/a050/a100_s42_fp32`) |
| 跳过（无 registry 条目） | 6 |

### 唯一实质值变化
- **`generalize_pythia1b_c4_a100_s42`**: K3 8→7, K4 8→0, TY 4→1（TY 方向修复后 forward 显著数下降）

### 其余 61 个均为 None→新值
此前 metrics 中没有 5method 字段，现已全部补齐：`ty_forward_sig`, `perm_granger_fdr_forward/reverse_sig`, `diff_xcorr_fdr_forward/reverse_sig`, `threshold_onset_forward_sig`, `robust_pairs_K3`, `robust_pairs_K4`

### 跳过的 6 个实验（无 registry 条目）
`ablation_accumulate_a050_s43`, `alpha_sweep_a000_s42_fp32`, `gen_wiki_gpt2m_a100_s43`, `scale_check_pythia14b_a050_s42`, `scale_check_pythia69b_wiki_a100_s42`, `scale_check_pythia69b_wiki_a100_s43`

---
