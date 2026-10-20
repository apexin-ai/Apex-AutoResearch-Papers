# analysis prepare gpt2m a025 pipeline

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prepare_gpt2m_a025_pipeline_20260516T012138_result.json`
- **Structured JSON:** [`53a4dc4ba588255a9afe.json`](../../sessions/53/53a4dc4ba588255a9afe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析 pipeline 已准备好，保存在 `artifacts/gpt2m_a025_analysis_plan.md`。

内容包含：
- **Pre-check**: 验证 11 代完成 + all_metrics.json 存在，附带手动汇聚脚本作为 fallback
- **Step 1**: Drift 提取（gen0 vs gen10，9 个指标）
- **Step 2**: Lead-lag 分析（完整的 Python 脚本，从 leadlag_gpt2m_s42.py 适配，输出到 `results/gen_wiki_gpt2m_a025_s42/analysis/`）
- **Step 3**: 三方对比表（GPT-2m α=0.25 vs Pythia α=0.25 vs GPT-2m α=1.0）+ 自动 regime 分类
- **判断标准**:
  - Success: drift 在 mild range（entropy <20%, ECE <200%, PPL <50%），方向与 Pythia α=0.25 一致，regime = MILD
  - Negative: drift 进入 moderate/severe 区间，或方向相反，或 diversity 无 collapse
  - Inconclusive: 方向对但幅度差异 >3x，或 lead-lag 信号太弱（T=11 下可预期）

所有命令可直接复制执行，按顺序 0→1→3→2→5 跑即可。

---
