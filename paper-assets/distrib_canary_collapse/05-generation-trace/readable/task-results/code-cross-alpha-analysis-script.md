# code cross alpha analysis script

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross_alpha_analysis_script_20260515T063902_result.json`
- **Structured JSON:** [`42fcb7aeab1ea60e1f47.json`](../../sessions/42/42fcb7aeab1ea60e1f47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`cross_alpha_analysis.py` 已部署到 `/root/autodl-tmp/distrib_canary_collapse/`，验证通过：

**验证结果对比 v3：**
- dose-response drift%：完全一致（a025 d1=-40.3%, a050 d1=-37.3%）
- entropy→d1 at α=0.25：p_raw=0.0152（v3: 0.0152）✓
- ECE→d1 at α=0.50：p_raw=0.0208（v3: 0.0211，permutation 随机性内）✓
- cross-correlation：entropy_vs_d1 peak lag=1 一致，r 值匹配
- 0/24 FDR-sig，符合预期

**用法：**
```bash
# 自动扫描所有 α 目录
python cross_alpha_analysis.py

# 指定目录 + 自定义参数
python cross_alpha_analysis.py --alpha-dirs a000_s42 a025_s42 a050_s42 a075_s42 --n-perms 5000

# a075 完成后直接跑
python cross_alpha_analysis.py
```

---
