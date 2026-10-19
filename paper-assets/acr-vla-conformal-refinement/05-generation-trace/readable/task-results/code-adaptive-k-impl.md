# code adaptive k impl

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_adaptive-k-impl_20260519T224032_result.json`
- **Structured JSON:** [`52684ee5b45dc2082e81.json`](../../sessions/52/52684ee5b45dc2082e81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

511 → 593 行，净增 82 行，符合预期（新函数 ~48 行 + docstring ~8 行 + 各处逻辑增加 ~26 行）。

实现完成。总结所有修改：

**`--mode adaptive_k` 已添加到 evaluate.py，包含以下修改：**

1. **Docstring** (L20-27): 添加 adaptive_k 模式描述和使用说明
2. **argparse choices** (L74): 添加 `"adaptive_k"` 选项
3. **`select_action_adaptive_k()`** (L302-349): 新函数，核心逻辑：
   - K=2 采样 → L2 距离判断
   - L2 ≤ τ: 取 K=2 均值，**不过 CRM**（fast path）
   - L2 > τ: 扩展到 K=10（复用 K=2 + 追加 8），argmin 选择 + CRM obs_only 校正
4. **CRM 加载** (L406, L410): `adaptive_k` 加入 CRM 加载条件，unc_dim=0（obs_only）
5. **默认 checkpoint** (L379-382): 自动使用 `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`
6. **默认 ε=0.2** (L429-430): `max_correction_norm` 默认 0.2
7. **Rollout dispatch** (L465-470): `adaptive_k` 模式走新函数
8. **输出 JSON** (L537-541): 添加 `per_step_K`, `avg_K`, `adaptive_trigger_rate`, `threshold` 字段
9. **输出文件命名** (L580-582): `adaptive_k` 模式使用 `_t{threshold}` 后缀

---
