# code n32 analysis prep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_n32_analysis_prep_20260523T080941_result.json`
- **Structured JSON:** [`1735b09cecebc63f878b.json`](../../sessions/17/1735b09cecebc63f878b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**Step 1 — 数据格式确认**
- N=32 输出目录 `fewnerd_pretrained_n32_seed42/` 存在但为空（正在跑）
- N=8 pretrained 数据在 `e2_pretrained_fewnerd/samples.jsonl`（2GB, 37648 instances, 32565 gold-nonempty）
- 每个 instance 有 `{id, text, gold, greedy, samples[N], logprobs}`，每个 sample 有 `entities, relations, cumulative_logprob, mean_logprob` 等字段

**Step 2 — 分析脚本已部署**
- 路径: `/root/autodl-tmp/struct_self_consist_ie/code/analyze_n32.py`
- 使用 `unified_metrics.py` 作为核心依赖
- Entity voting: `(text, type)` 计数，> N/2 阈值，pick best span
- 退化率: keyset_surface 定义（与参考值一致）
- 同时输出 micro-averaged 和 instance-averaged 指标

**Step 3 — N=8 验证通过**
- Greedy=0.539, MV Δ=+3.2pp, Degen=12.6%, Oracle Δ=+11.3pp — 与参考值基本吻合

**Step 4 — 模板已准备**
- `artifacts/n32_table_row.md` 已写入，含 LaTeX 行模板和 scenario 判定标准

**N=32 完成后运行命令**:
```bash
cd /root/autodl-tmp/struct_self_consist_ie/code
python analyze_n32.py --input /root/autodl-tmp/struct_self_consist_ie/output/fewnerd_pretrained_n32_seed42/samples.jsonl
```

---
