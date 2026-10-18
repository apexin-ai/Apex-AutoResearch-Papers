# exp taxonomy broad spectrum

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_taxonomy-broad-spectrum_20260522T033416_result.json`
- **Structured JSON:** [`a8f75476216c90ca884c.json`](../../sessions/a8/a8f75476216c90ca884c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动，qwen2.5-72b 模型正在加载中。

**已完成：**
1. **attacks.py** — 添加了 3 个 broad-spectrum 攻击类（`VerbosityBias`, `PositionBias`, `AuthorityBias`）+ `apply_position_attack` 和 `measure_position_asr` 辅助函数
2. **run_taxonomy_broadspectrum.py** — 完整脚本，包含：
   - Phase 1: 6 模型 serial load/unload，score clean + 3 attacks × 2 datasets（带 checkpoint）
   - Phase 2: Individual ASR (6×3×2)，position bias 使用专用 ASR 计算
   - Phase 3: 20-panel OLS 回归 + η_max cross-panel variance
   - Diagnostic: 检查 K_eff 一致性 + η_max CV < 0.3 artifact 警告
3. **Registry** — `taxonomy-broad-spectrum` 状态已更新为 RUNNING

tmux session `taxonomy` 运行中，第一个模型 qwen2.5-72b 正在加载。预计 6 模型 × 8 轮 scoring ≈ 2-3 小时完成。

---
