# audit encoder multiseed

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_encoder-multiseed_20260516T042326_result.json`
- **Structured JSON:** [`e30832a3544c88403143.json`](../../sessions/e3/e30832a3544c88403143.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。汇总报告如下：

---

## Multiseed JSON 审计报告

### 审计范围
服务器 `bjb2-23165` 上所有 multiseed JSON 文件，共发现 4 个：

| # | 文件 | 创建时间 |
|---|------|---------|
| 1 | `artifacts/bgem3_multiseed_test_results.json` | 2026-05-15 06:15 |
| 2 | `artifacts/multiseed_structural_results.json` | 2026-05-15 02:54 |
| 3 | `artifacts/multiseed_gb_crossagent_fixed_results.json` | 2026-05-15 08:15 |
| 4 | `results_encoder_multiseed_e5.json` | (已知有问题，已重新生成) |

GTE-large 只有预计算 embeddings (`ablation_embeddings/gte-large_embeddings.pt`)，**无 multiseed 文件**。

---

### 1. `bgem3_multiseed_test_results.json` — **SUSPECT**

**问题与 E5 相同模式：无生成脚本、缺少 results.json 出处文件。**

逐 seed 对比：

| Seed | JSON test_macro_f1 | 最佳 val_macro_f1 (train_history) | results.json 存在? | 验证状态 |
|------|-------------------|----------------------------------|-------------------|---------|
| 42 | 0.9413 | 0.9579 (epoch 5) | 无（但 d073 重跑确认） | **已验证** |
| 123 | 0.8474 | 0.9179 (epoch 2) | **无** | **不可验证** |
| 456 | 0.9364 | 0.9480 (epoch 5) | **无** | **不可验证** |

红旗：
- `grep -r "bgem3_multiseed" *.py *.sh` — 无结果，没有任何脚本生成此文件
- 3 个 checkpoint 目录 (`checkpoints_ablation_bgem3{,_s123,_s456}`) 都只有 `split_info.json`、`best_model.pt`、`train_history.json`，**全部缺少 `results.json`**（而 `encoder_ablation_train.py` 正常应输出此文件）
- 无 BGE-M3 评估日志（E5 有 `multiseed_e5.log`，BGE-M3 无对应文件）
- Seed 42 靠 `artifacts/d073/probe_bge_m3/results.json`（今天 11:45 重跑）追溯验证，值精确匹配到小数点后 16 位
- Seed 123 的 val→test 落差 7.0pp（seed 42 仅 1.7pp，seed 456 仅 1.2pp），虽有注释声称是不同 split 所致，但无法核实

### 2. `multiseed_structural_results.json` — **CLEAN**

- 由 `multiseed_structural.py` 生成（脚本存在，sklearn RF/GB 确定性计算）
- non_nlp_baseline 三 seed 值完全相同（std=0.0）— 相同数据 split + 树模型，符合预期
- **cross_agent GB seeds 42/123/456 的值与第 3 个文件精确匹配** — 交叉验证通过

### 3. `multiseed_gb_crossagent_fixed_results.json` — **CLEAN**

- 由 `multiseed_gb_crossagent_fixed.py` 生成（脚本存在，含标签验证断言 `stag_pct > 15%`）
- 5 seeds (42, 123, 456, 789, 1024)，前 3 个与文件 2 精确一致
- 包含 `oh_label_verification` 元数据

### 4. `results_encoder_multiseed_e5.json` — **CLEAN (重新生成版)**

- 由 `run_e5_multiseed.sh` 生成，`multiseed_e5.log` 包含完整训练+评估输出
- 日志值 vs JSON 值：seed 123 macro_f1=0.9433 ✓，seed 456 macro_f1=0.9418 ✓
- 注释标注 "All 3 seeds from real training runs"

---

### 汇总

| 文件 | 状态 | 问题 |
|------|------|------|
| bgem3_multiseed_test_results.json | **SUSPECT** | seed 123/456 无出处，无生成脚本，无评估日志 |
| multiseed_structural_results.json | CLEAN | 脚本生成，交叉验证通过 |
| multiseed_gb_crossagent_fixed_results.json | CLEAN | 脚本生成，交叉验证通过 |
| results_encoder_multiseed_e5.json | CLEAN | 已重新生成，日志完整 |

### 修复建议

对 BGE-M3 seeds 123/456，用已保存的 checkpoint 重跑 test 评估：

```bash
python3 eval_probe_only.py \
  --checkpoint checkpoints_ablation_bgem3_s123/best_model.pt \
  --data_dir ablation_data_bgem3 \
  --split_info checkpoints_ablation_bgem3_s123/split_info.json

python3 eval_probe_only.py \
  --checkpoint checkpoints_ablation_bgem3_s456/best_model.pt \
  --data_dir ablation_data_bgem3 \
  --split_info checkpoints_ablation_bgem3_s456/split_info.json
```

需要确认 `eval_probe_only.py` 是否兼容 BGE-M3 embeddings 格式（embed_dim=1024 vs E5 的 1024），以及 `ablation_data_bgem3` 目录结构是否匹配。

---
