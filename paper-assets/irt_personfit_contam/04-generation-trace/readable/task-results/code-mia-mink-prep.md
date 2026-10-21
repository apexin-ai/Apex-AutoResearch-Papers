# code mia mink prep

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mia-mink-prep_20260521T080628_result.json`
- **Structured JSON:** [`d522af0dea980a14566b.json`](../../sessions/d5/d522af0dea980a14566b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出总结：

1. **`/root/autodl-tmp/post_rl_contam/eval_mia.py`** — MIA 评估脚本
   - 支持 `--stage base|sft|grpo --gpu N`
   - 计算 Loss / Min-K% / Min-K%++ 三类方法，K=10/20/30/40/50
   - Min-K%++ 使用 vocab-level μ/σ 标准化（与 Zhang et al. 2024 一致）
   - 输出 per-item scores + AUC-ROC 到 `results/mia_{stage}_results.json`

2. **`/root/autodl-tmp/post_rl_contam/compare_mia_lz.py`** — 对比脚本
   - 自动加载 MIA 和 lz* 结果，生成跨 stage 对比表
   - 已验证可运行（当前输出 base/sft 的 lz* 结果，MIA 数据待 eval_mia.py 运行后填入）

3. **scikit-learn** 已安装，所有 import 验证通过

4. **memory.md** 已更新 "MIA 对比准备" 段

运行命令：`python eval_mia.py --stage base --gpu 0`（需 GPU，约 1-2h/stage）。

---
