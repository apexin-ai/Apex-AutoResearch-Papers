# code lf oracle baseline

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lf_oracle_baseline_20260514T081838_result.json`
- **Structured JSON:** [`9a2a2fb1a40721f2132a.json`](../../sessions/9a/9a2a2fb1a40721f2132a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**产出**: `artifacts/lf_oracle_baseline.py`

**运行方式** (在服务器上):
```bash
python lf_oracle_baseline.py --data_dir /root/autodl-tmp/agent_progress_probe --split_info /root/autodl-tmp/agent_progress_probe/checkpoints/split_info.json
```

**实现的 6 个 baseline 变体**:
1. **LF Majority Vote** — 直接用 `majority_label`（abstain 时 fallback 到 prior）
2. **LF Any-Stagnation** — 任一 LF 投 0 即判 stagnation
3. **LF All-Agreement** — 所有非 abstain LF 一致才预测，否则用 prior
4. **Single LF: file_diff_delta** / **command_repetition** / **outcome_backpropagation** — 各 LF 独立作为分类器

**索引对齐逻辑**: 先过滤 `majority_label != -1`（与 `generate_embeddings.py` 一致），再应用 `keep_indices` 置信度过滤，最后用 `split_info` 的 train/val/test indices 取子集。

**预期输出格式**:
```
=== LF Coverage on Test Set ===
  file_diff_delta: X/N (xx.x%)
  command_repetition: X/N (xx.x%)
  ...

=== Results ===
| Method                      | Macro-F1 | Accuracy | Prec(M) | Rec(M) | F1(stag) | F1(prog) |
|------------------------------|----------|----------|---------|--------|----------|----------|
| GRU Probe (probe_001 ref)   | 0.9055   |    —     |    —    |    —   |    —     |    —     |
| LF Majority Vote             | x.xxxx  | x.xxxx   | ...
| ...
```

**注意**: LF Majority Vote 预期会接近 1.0（因为 ground truth 就是 majority_label），这是 ceiling baseline。更有意义的对比是 Any-Stagnation、All-Agreement 和 Single LF 变体——它们会低于 probe，支撑 Claim 1。

---
