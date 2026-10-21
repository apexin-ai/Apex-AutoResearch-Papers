# audit nmin eval consistency

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_nmin_eval_consistency_20260515T155958_result.json`
- **Structured JSON:** [`05860fcc82347514139a.json`](../../sessions/05/05860fcc82347514139a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Phase 1: 差异根因报告

### PPL=17.644 来源
- **文件**: `/root/provenance_weight_training/output/eval_perplexity_results.json`
- **eval 方法**: `eval_perplexity.py`（sliding window, stride=1024, fp16 autocast）
- **eval 数据**: 5000 docs, 4,077,068 tokens
- **生成环境**: **旧 AutoDL 服务器**（checkpoint 路径含 `/root/autodl-tmp/`）
- **nmin_ablation_analysis.py 路径**: 前 3 个 lookup 位置都不存在，fallback 到 Location 4（aggregated file）

### PPL=17.690 来源
- **文件**: Registry `adaptive_seed42.metrics.eval_ppl_holdout`
- **eval 方法**: **HuggingFace Trainer inline eval**（训练时自动触发，`--eval_steps 500`）
- **eval 数据**: 4,080,000 tokens（不同 token 计数方式）

### 具体原因
**两个不同 eval pipeline 产生了不同结果**：
1. Trainer inline eval 用 HuggingFace 的 loss 聚合（计算方式不同于 sliding window），token 计数 4,080,000
2. `eval_perplexity.py` 用 sliding window (stride=1024)，token 计数 4,077,068
3. Token 数差 2,932（0.07%），PPL 差 0.046

**为什么只有 adaptive_seed42 (n_min=3) 有此问题**：它是最早的实验，registry 只记录了 inline eval 值。后续的 adaptive_fix_seed42 和 nmin1_seed42 都做了 post-hoc eval 并更新了 registry。

### 额外发现
- `nmin_ablation_analysis.py` 中 n_min=2 的值是 **hardcoded** (`17.650, "hardcoded (D018 confirmed)"`)，非从 eval 文件读取
- n_min=3 的值来自旧 AutoDL 服务器迁移过来的 eval 文件

---

## Phase 2: 统一 Eval 结果

**Pipeline**: `eval_perplexity.py --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048` (fp16, sliding window stride=1024, GPU 0 on westd-47453)

| n_min | Experiment | PPL | Loss | Tokens | 耗时 |
|-------|-----------|-----|------|--------|------|
| 1 | nmin1_seed42 | **17.789** | 2.8786 | 4,077,068 | 172s |
| 2 | adaptive_fix_seed42 | **17.653** | 2.8709 | 4,077,068 | 157s |
| 3 | adaptive_seed42 | **17.644** | 2.8704 | 4,077,068 | 153s |

**结论**：n_min=2 和 n_min=3 性能接近（Δ=0.009），均优于 n_min=1（+0.135/+0.145）。

---

## Phase 3: 已完成操作

1. **Registry 已更新**: `adaptive_seed42.metrics.eval_ppl_holdout` 从 17.69 → 17.644，`eval_holdout_tokens` 从 4,080,000 → 4,077,068，添加了 eval_method 和 eval_note 审计记录
2. **统一 eval 文件**: 已保存至服务器 `output/eval_results/unified_nmin_ablation_eval.json`
3. **Artifact 已注册**: `art_20260515_293dac`
4. **未修改** `nmin_ablation_analysis.py` 和图表 — 等 Director 决定

---
