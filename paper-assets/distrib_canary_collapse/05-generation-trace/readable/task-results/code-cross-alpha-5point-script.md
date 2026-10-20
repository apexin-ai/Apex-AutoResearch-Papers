# code cross alpha 5point script

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross_alpha_5point_script_20260515T085132_result.json`
- **Structured JSON:** [`7bcf6b39cf80e3a8f618.json`](../../sessions/7b/7bcf6b39cf80e3a8f618.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**产出：**
- 服务器脚本：`/root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py` — 已部署、语法验证通过
- 本地执行文档：`artifacts/cross_alpha_v4_ready.md`

**v4 相比 v3 的新增：**
- α=1.0 自动从 `results/mvp/rep_{42..45}` 加载（4 seeds，full consensus via method_ablation.json）
- 对每个 α 点运行 5 方法×16 对的 consensus classification；单 seed 点标注 "method agreement only"（seed_threshold=1）
- 跨 α regime comparison 矩阵，直接显示哪些 pair 在不同 α 下分类变化
- 同时输出 JSON + Markdown 报告

a075_s42 完成后执行：
```bash
python3 cross_alpha_analysis_v4.py --n-perms 5000 --consensus-n-perms 1000 --update-registry
```

---
