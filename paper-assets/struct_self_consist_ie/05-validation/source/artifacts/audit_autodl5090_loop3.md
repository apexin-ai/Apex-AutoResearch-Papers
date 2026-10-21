# autodl-5090 实验状态审计 (2026-05-14)

## GPU 状态

| GPU | 利用率 | 显存占用 | 总显存 |
|-----|--------|----------|--------|
| cuda:0 | 0% | 2 MiB | 32607 MiB |
| cuda:1 | 0% | 2 MiB | 32607 MiB |
| cuda:2 | 0% | 2 MiB | 32607 MiB |
| cuda:3 | 0% | 2 MiB | 32607 MiB |

**4 GPU 全部空闲。** 无训练/推理进程，无 tmux session。

---

## 实验状态详情

### 1. exp_017_llama_conll_infer — Registry: RUNNING → 实际: DONE

- **完成时间**: 2026-05-15 01:41
- **输出文件**: samples.jsonl (9.5MB, 3453 行), report.json
- **配置**: conll2003/NER, n_samples=8, T=1.0, vLLM (llama3.1-8b-conll2003-merged)
- **推理速度**: ~53.96 it/s, ~9197 input toks/s, ~3017 output toks/s
- **关键指标**:
  - Greedy F1: **0.9266**, Oracle F1: 0.9443, headroom: +0.0177
  - Fleiss' kappa: 0.9278, Soft Jaccard: 0.9726
  - Full rho(SJ,F1): **+0.4314** (p~0), Cond rho(SJ,F1): **+0.4356**
  - Structural > Surface: **YES** (delta=+0.0037)
  - Logprob baseline AUROC: 0.7610 (full), 0.8102 (cond)
  - Sample F1=0: 4.3%
- **Verdict**: **MARGINAL**
- **操作**: → 标记 DONE

### 2. exp_001_seed456_v2_ner — Registry: RUNNING → 实际: DONE

- **完成时间**: 2026-05-15 01:21
- **输出文件**: samples.jsonl (6.8MB, 551 行), report.json
- **配置**: scierc/NER, n_samples=16, T=1.0
- **关键指标**:
  - Greedy F1: **0.6639**, Oracle F1: 0.8112, headroom: +0.1473
  - Fleiss' kappa: 0.4512, Soft Jaccard: 0.7025
  - Full rho(SJ,F1): **+0.3838** (p~5e-20), Cond rho(SJ,F1): **+0.3494**
  - Structural > Surface: **YES** (delta=+0.1604) — 最大优势
  - Logprob baseline AUROC: 0.6233 (full), 0.6014 (cond)
  - Sample F1=0: 12.3%
- **Verdict**: **MARGINAL**
- **操作**: → 标记 DONE

### 3. exp_003_wnut17_v2_infer — Registry: ANALYZING → 实际: DONE

- **完成时间**: 2026-05-15 01:16
- **输出文件**: samples.jsonl (4.8MB, 1287 行), report.json, run.log (115KB)
- **配置**: wnut17/NER, n_samples=16, T=1.0
- **关键指标**:
  - Greedy F1: **0.5246**, Oracle F1: 0.6597, headroom: +0.1350
  - Fleiss' kappa: 0.6818, Soft Jaccard: 0.8798
  - Full rho(SJ,F1): **+0.0616** (p=0.106, 不显著), Cond rho(SJ,F1): **+0.2953**
  - Structural > Surface: **NO** (delta=-0.0499)
  - Logprob baseline AUROC: 0.2181 (full, 反转), 0.7175 (cond)
  - **54% samples F1=0** — 建议 T=0.7 重跑
- **Verdict**: **FAIL**
- **操作**: → 标记 DONE (结果 FAIL)

### 4. exp_002_merge_conll2003 — Registry: PREPARING (PID 57524) → 实际: DONE

- **PID 57524**: 已退出
- **日志**: EXIT_CODE=0 (成功完成)
- **操作**: → 标记 DONE

---

## 训练日志 (/root/runs/struct_self_consist_ie/)

| 文件 | 时间 | 大小 |
|------|------|------|
| exp_007_llama_inference.log | May 14 21:58 | 98KB |
| exp_007_ner_multi_model.log | May 14 21:08 | 115KB |
| exp_001_ner_n16_seed123.log | May 14 20:54 | 109KB |
| exp_008_re_n16_full.log | May 14 20:53 | 104KB |
| exp_003_ner_wnut17.log | May 14 20:52 | 175KB |
| exp_001_n16_seed456_full.log | May 14 20:44 | 14KB |
| exp_001_n16_seed123_full.log | May 14 20:44 | 14KB |
| exp_002_ner_conll2003.log | May 14 20:36 | 317KB |
| exp_002_merge_conll2003.log | May 14 20:26 | 12B |
| exp_001_ner_n16_scierc.log | May 14 20:24 | 108KB |

---

## 结论

| 实验 | Registry 状态 | 实际状态 | 需要操作 |
|------|---------------|----------|----------|
| exp_017_llama_conll_infer | RUNNING | DONE (MARGINAL) | 标记 DONE |
| exp_001_seed456_v2_ner | RUNNING | DONE (MARGINAL) | 标记 DONE |
| exp_003_wnut17_v2_infer | ANALYZING | DONE (FAIL) | 标记 DONE |
| exp_002_merge_conll2003 | PREPARING | DONE (exit 0) | 标记 DONE |

**所有 4 个实验均已完成，无一在运行。4 GPU 完全空闲，可分配新任务。**

### 关键发现

1. **conll2003 (Llama FT)**: structural > surface 但优势极小 (delta=+0.004)，verdict MARGINAL
2. **scierc**: structural 优势最大 (delta=+0.16)，但 greedy F1 本身较低 (0.66)，verdict MARGINAL
3. **wnut17**: FAIL — 54% F1=0、surface 反超 structural、logprob full AUROC 反转 (0.218)。需降温度 T=0.7 重跑
4. **merge_conll2003**: 静默完成，无后续动作
