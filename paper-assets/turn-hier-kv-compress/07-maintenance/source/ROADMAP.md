# turn-hier-kv-compress — Research Dashboard

> 最后更新: 2026-05-13 17:23 UTC | 更新原因: DEFINITIVE KILL — MVP 证伪核心假设

## 核心方向
TurnKV: 利用 agent 协议的 turn boundary markers 做零成本语义角色分割，结合 ExpectedAttention 做 per-segment 预算分配的 KV cache 压缩策略。

## 最终结论：DEFINITIVE KILL (D008)

**核心假设被证伪**：role labels（SYSTEM/USER/TOOL_RESULT/THINKING）无法预测 token-level 信息重要性。

| 轮次 | 方案 | KIRR diff | 根因 |
|------|------|-----------|------|
| v1 | 乘法调制 | -4.5pp | 实现 bug（recency 双重计算） |
| v2 | 归一化乘法 | +1.7pp | PPL 爆炸 1.74×, full KIRR 14.4%（评估无效） |
| v3b | **加法偏置 α=0.1** | **-4.5pp** | **Pure Structural 0% KIRR = role labels 零预测力** |

**决定性证据**：v3b Pure Structural（仅用角色标签排序）KIRR=0%，说明 role 是 coarse 标签（5 种），token importance 是 fine-grained 的，role-level 先验无法捕捉 within-segment 的信息分布。

## 资源使用
- GPU: 2×RTX PRO 6000 96GB, ~8 GPU·h consumed
- 实验: 8 个（0 positive, 6 negative, 2 killed）
- 决策: D001-D008

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D008 | 2026-05-13 | DEFINITIVE KILL：4 轮实验一致 negative，Pure Structural 0 | mvp_v3b_cr85, mvp_v3b_cr70 |
| D007 | 2026-05-13 | Pivot to additive offset: final_score = ea_score + | mvp_eval_02_cr70, mvp_eval_02_cr85 |
| D006 | 2026-05-13 | 条件性继续：给 24h 做最终 MVP 验证（修复评估 + 温和调制），仍负向则 KILL。放弃 E | mvp_eval_02_cr70, mvp_eval_02_cr85 |
| D005 | 2026-05-13 | EASS budget 归一化：B_final 除以 token-weighted 均值，从绝对压制 | mvp_eval_01_cr70, mvp_eval_01_cr85 |
| D004 | 2026-05-13 | 暂缓 KILL 决定：MVP 实验数据不可信（PPL 评估失效 + 10/80 traces + 可 | mvp_eval_01_cr70, mvp_eval_01_cr85 |
| D003 | 2026-05-13 | 修复 EASS recency 双重计算: 去掉连续衰减因子，仅用 B_prior 桶编码 rece | — |
| D002 | 2026-05-13 | 采纳 Reviewer 5 条 warning，修正 MVP gate: 差值驱动 pass(≥10 | — |
| D001 | 2026-05-13 | MVP 方案: Llama-3.1-8B + 合成 agent traces + TurnKV vs | — |


