# research novelty drayson check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_novelty-drayson-check_20260514T233111_result.json`
- **Structured JSON:** [`89f10a10365f1beb1289.json`](../../sessions/89/89f10a10365f1beb1289.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已保存并注册。

**核心结论**:

1. **Drayson et al. 确认使用完全相同公式** w=(1-q)^b，但 b 通过验证集 empirical 选取（GPT-2/SmolLM≤360M 用 b=10，SmolLM-1.7B 用 b=1），无理论推导，无 ablation。

2. **我们的 adaptive b* 是明确的新贡献** — 在 2024-2026 文献中无人做过 contamination score 权重指数的 principled 自适应推导。

3. **关键差异化维度**:
   - b 选择: empirical validation vs principled derivation
   - 问题设置: 已知比例 vs 未知比例
   - 规模: 36K docs vs 132M+ tokens
   - 检测器: 强(AUC=0.986) vs 轻量即可(AUC=0.939)

4. **建议 framing**: 主打 "unknown proportion + principled b*"，明确 credit Drayson 的公式贡献，将我们定位为同一框架内的 principled extension for realistic settings。

Sources:
- [Drayson et al. (arXiv:2502.15654)](https://arxiv.org/abs/2502.15654)
- [Golden Ratio Weighting (arXiv:2502.18049)](https://arxiv.org/abs/2502.18049)
- [Dynamic Loss Reweighting (ICLR 2025)](https://arxiv.org/abs/2502.06733)
- [DoReMi (NeurIPS 2023)](https://arxiv.org/abs/2305.10429)
- [Escaping Collapse (NeurIPS 2025)](https://neurips.cc/virtual/2025/loc/san-diego/poster/115205)

---
