# code exp 002 k ablation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-002-k-ablation_20260516T184917_result.json`
- **Structured JSON:** [`851771b9ed3b82419368.json`](../../sessions/85/851771b9ed3b82419368.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已更新并验证通过。

**完成的修改**（`/root/symb_invariant_consensus/scripts/run_k_ablation.py`）：

1. **默认 K 值**：`6,8,12,16,20` → `6,8,11,12,16,20`（增加 K=11 odd-K 对照组）
2. **Tiebreak 检测**：新增 `detect_sc_tie()` 函数，检测 SC 投票中前两名票数相同的情况
3. **每题记录** `sc_is_tie` 字段
4. **Summary 新增指标**：`tie_count`、`tie_sica_wins`、`tie_sc_wins`、`tie_sica_rate`
5. **输出表格**：增加 `Ties` 和 `TieWin` 列
6. **Odd-K 自动验证**：末尾自动检查 K=11 是否 Δ=0（确认 SICA 优势是否完全来自 tiebreak）

**启动命令**（exp-001 完成后执行）：
```bash
cd /root/symb_invariant_consensus && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
nohup python scripts/run_k_ablation.py \
  --k-values 6,8,11,12,16,20 \
  --output-dir results/k_ablation \
  --traces-cache results/k_ablation/traces_20.json \
  > results/k_ablation/run.log 2>&1 &
```

预计运行时间：60 题 × 6 个 K 值 × ~3 min/题 ≈ 5-6h（trace 只生成一次 K_max=20 条，后续 K 复用子集）。

---
