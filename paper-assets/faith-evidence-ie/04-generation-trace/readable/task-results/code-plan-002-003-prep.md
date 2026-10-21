# code plan 002 003 prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_002_003_prep_20260515T180127_result.json`
- **Structured JSON:** [`ac9c2e039cb825835467.json`](../../sessions/ac/ac9c2e039cb825835467.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇总

### Plan_002: Test Set Evaluation — 可行性报告

**结论：test set 无 gold labels，必须提交 CodaLab 评测。**

- `test.json`: 1000 docs, keys=`[sents, title, vertexSet]`, **无 labels 字段**
- 原 `inference.py --split test` 不可用（`prepare_eval_data` 依赖 labels 构造 prompt，test split 返回 0 docs）。已有失败记录：`test_rsft_s44/` 产出 0 条预测
- 已部署 `test_inference.py`，从 vertexSet 直接构造 prompt，绕过 labels 依赖，附带 CodaLab 格式转换（relation name → Pxxx code, entity name → vertexSet index）

**推荐方案：用 RSFT best seed (s43, rel_f1=0.4683) 跑 test**

Dry-run 命令：
```bash
cd /root/autodl-tmp && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
CUDA_VISIBLE_DEVICES=0 python -m freige.eval.test_inference \
  --model_path /root/autodl-tmp/rsft_output_s43 \
  --base_model /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_path /root/autodl-tmp/data/docred \
  --output_dir /root/autodl-tmp/eval_results/test_rsft_s43 \
  --no-quantize --batch_size 16 --max_new_tokens 1024
```
预计时长：~1h（1000 docs, 参照 dev 985 docs ~3600s）。产出 `codalab_submission.json` 可直接提交。

---

### Plan_003: EDCR Cross-Method Table — 已完成

脚本和数据均已就绪。完整表格：

```
Method                       rel_f1   delta  evi_f1    EDCR   delta  preds  trunc
──────────────────────────────────────────────────────────────────────────────────
SFT baseline                 0.4057   +0.0p  0.7979  0.7118   +0.0p  18815    367
RSFT-CED (s42, 3ep)          0.4449   +3.9p  0.8187  0.6565   -5.5p  15307    213
RSFT-CED (s43, 3ep)          0.4683   +6.3p  0.8156  0.6388   -7.3p  14970    171
RSFT-CED (s44, 3ep)          0.4655   +6.0p  0.8087  0.6350   -7.7p  15202    189
RSFT-CED (r2a, 1ep)          0.4494   +4.4p  0.8108  0.6641   -4.8p  15482    208
RSFT-CED (r2b, α=32)         0.4493   +4.4p  0.8128  0.6609   -5.1p  14829    179
RSFT-flatNLI (3ep)           0.4539   +4.8p  0.8043  0.6431   -6.9p  15294    199
CED-reranker (N=8)           0.4864   +8.1p  0.8188  0.6156   -9.6p  14782      -
bf16 GRPO (G=8)              0.4549   +4.9p  0.8086  0.6318   -8.0p  10701     61

RSFT-CED 3-seed: 0.4596±0.0128 | 0.8144±0.0051 | 0.6434±0.0114
```

**关键观察**：所有改进方法 EDCR 均低于 SFT（0.71→0.61-0.66），rel_f1 提升越大 EDCR 下降越多。这是 recall-oriented training 的固有 trade-off：更多预测 → 更多 distractor citations。EDCR 数据跨方法一致，均由同一 evaluator.py 计算，无需重跑。

重新生成表格：`cd /root/autodl-tmp && python -m freige.eval.cross_method_table`

---
