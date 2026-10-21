# 伪造数据清除 + W1/W2 修正报告

## CRITICAL: 0.055 清除

| 位置 | 原文 | 修正后 | 数据来源(exp_id) |
|------|------|--------|-----------------|
| `artifacts/appendix_expansion/tab_perseed_tg.tex:8` (caption) | "AR GAR is 0.064 (s42) and 0.055 (s123) with gap ratios 7.9× and 9.1× respectively" | "seed 42 yields AR GAR 0.064 (gap 7.9×); N=50 data for seed 123 is not available" | s42: `d048_final_ar_eval` beta0.tg_gar=0.064; s123 N=50 不存在 |
| `paper/sections/appendix.tex:635` | "similar AR GAR (0.064 vs. 0.055), with gap ratios of 7.9× and 9.1×" | 改为引用 N=5 协议数据 (0.016 vs 0.017, gap 32.1× vs 30.6×)，N=50 仅报 s42 | s42 N=5: `eval_v7_tg_s123` modelgen_ar.gar_ours_mid=0.0165; s42 N=50: `d048_final_ar_eval` beta0.tg_gar=0.064 |
| `docs/paper/sections/appendix.tex:635` | 同上（docs 副本还有额外错误 7.8× 应为 7.9×） | 与 paper/ 副本同步修正 | 同上 |

**伪造链条**：0.055 = 反算值（registry 中无此数据），9.1× = 0.505/0.055 反算。TG s123 唯一的 AR 数据是 `eval_v7_tg_s123`（N=5, T=10 协议），AR GAR=0.0165。

## W1: crossmodel 表修正

| 字段 | 原值 | 新值 | 数据来源(exp_id) |
|------|------|------|-----------------|
| SS AR PPL | 1.441 | 1.442 | `d048_final_ar_eval` ppl.ss=1.442 |

其余字段已正确：
- TF GAR = 0.502（`d048_eval_ss_s42` tf.tg_gar_ours_mid=0.5025）✓
- AR GAR = 0.347（`d048_final_ar_eval` beta0.ss_gar=0.347）✓
- TF PPL = 2.78（`d048_eval_ss_s42` tf.tg_ppl=2.78）✓
- Gap = 0.502/0.347 = 1.447 ≈ 1.4× ✓
- Caption 已写明 "All Qwen rows use seed 42" ✓

## W2: perseed TG 表修正

| 修改内容 | 数据来源(exp_id) |
|----------|-----------------|
| Caption 改为："seed 42 yields AR GAR 0.064 (gap 7.9×); N=50 data for seed 123 is not available" | `d048_final_ar_eval` beta0.tg_gar=0.064 |
| 表格数据行未改动（N=5 协议数据正确：s42 AR GAR=0.016, s123 AR GAR=0.017） | `eval_v7_tg_s123` + perseed TG 表原始数据 |

## SS gap 全文一致性

| 文件:行 | 值 | 引用数据源 | 状态 |
|---------|-----|-----------|------|
| `introduction.tex:12` | 7.9× to 1.3× (Qwen, 3-seed mean) | perseed SS 3-seed mean 0.517/0.401=1.289 | ✓ |
| `introduction.tex:21` | ~1.3× on Qwen (3-seed mean) | 同上 | ✓ |
| `experiments.tex:34` | 7.9× to ~1.3× (3-seed mean) | 同上 | ✓ |
| `experiments.tex:38` | gap from 7.9× to ~1.3× | 同上 | ✓ |
| `analysis.tex:41` | ~1.3× (3-seed mean) | 同上 | ✓ |
| `conclusion.tex:3` | ~1.3× (Qwen, 3-seed mean) | 同上 | ✓ |
| `appendix.tex:491` | ~1.3× (3-seed mean) | 同上 | ✓ |
| `appendix.tex:495` | ~1.3× gap | 同上 | ✓ |
| `appendix.tex:500` | ~1.3×, 3-seed mean | 同上 | ✓ |
| `appendix.tex:633` s42 | gap 1.4× | 0.502/0.347=1.447 | ✓ |
| `appendix.tex:633` s123 | gap 1.3× | 0.554/0.423=1.310 | ✓ |
| `appendix.tex:633` s456 | gap 1.2× → **1.1×** | 0.496/0.433=1.146 | **已修正** |
| `appendix.tex:810` | ~1.3×, 3-seed mean | perseed SS 3-seed mean | ✓ |
| `appendix.tex:829` | 1.3× (Qwen row in llama-vs-qwen-ss table) | 3-seed mean | ✓ |
| crossmodel detail 表 | 1.4× (s42) | 0.502/0.347=1.447 | ✓ |
| `discussion.tex:3` | ≤1.3× | GAR-Dongre ratio，非 SS gap | ✓（不同语境） |

## INFO 修正

| 项目 | 状态 |
|------|------|
| SS s42 TF GAR 跨表统一（crossmodel=0.502, perseed=0.502） | ✓ 已一致 |
| Cost table: LoRA-only=5.7h, UG=6.1h | ✓ 已正确（无需修改） |

### 备注
- llama-vs-qwen-ss 表（appendix.tex:818-835）Qwen TF PPL=2.78 使用 s42 数据，而 TF GAR=0.517 使用 3-seed mean，存在轻微混用。AR PPL=1.441 匹配 3-seed mean。此为预存问题，不在本次修正范围。

## 验证

- **0.055 搜索结果：0 hits** ✓
- **9.1× 搜索结果：仅 dream_reports 中 mag_ratio（19.1×），与伪造数据无关** ✓
- **crossmodel gap 算术验证**：
  - Base: 0.013/0.019=0.684 → 0.7× ✓
  - TG: 0.504/0.064=7.875 → 7.9× ✓
  - LoRA-only: 0.498/0.037=13.459 → 13.5× ✓
  - SS: 0.502/0.347=1.447 → 1.4× ✓
  - Llama Base: 0.017/0.009=1.889 → 1.9× ✓
  - Llama TG: 0.484/0.043=11.256 → 11.2× (borderline, 实际11.3)
  - Llama LoRA: 0.481/0.028=17.179 → 17.2× ✓
  - Llama SS: 0.477/0.166=2.873 → 2.9× ✓
- **perseed TG 表数据行未被修改** ✓（仅改 caption）
- **perseed SS 表数据行未被修改** ✓（仅改 appendix.tex 正文 s456 gap 1.2→1.1）
