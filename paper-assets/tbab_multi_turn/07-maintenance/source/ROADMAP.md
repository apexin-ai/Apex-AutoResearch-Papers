# tbab_multi_turn — Research Dashboard

> 最后更新: 2026-05-18 23:59 UTC | 更新原因: MVP KILL 确认，项目等待用户确认终止

## 核心方向
TBAB: turn 边界 bridge tokens + position reset，利用 RoPE 频段恢复理论改善多轮对话性能。

## 当前阶段：MVP KILL — 等待用户确认终止

### 模型（D002）
Mistral-7B-Instruct-v0.1（rope_theta=10K, d_head=128）

### MVP 结果

| 条件 | P̄ (2-seed 均值) | 结论 |
|------|-----------------|------|
| C1 LoRA-only | 6.59% | baseline |
| C2 Position reset only | 5.49% | ❌ 无效 |
| C4 Full TBAB | 5.49% | ❌ 无效 |

**Gate: C4 - C1 = -1.10%, 阈值 ≥3% → KILL (D003/D004)**

### 失败诊断
1. 代码无 bug（merge_and_unload / position_ids / train-inference 一致性全部排除）
2. Bridge tokens = "dead memory"（浅层 engage 4.65x，深层 L2-L30 抑制 0.06-0.34x）
3. Input-level token injection 深层失效是已知结构性限制（P-Tuning v2 文献）
4. Position reset 独立无效（C2 = C1_s137）
5. 根因：模型 turns≥6 全部崩溃（0%），无干预空间

### GPU 资源
| 服务器 | GPU | 状态 |
|--------|-----|------|
| westb-25721 | 1×RTX PRO 6000 94GB | 空闲，等待释放 |

## 已完成实验
- [x] mvp_c1_s42: DONE, P̄=7.69%
- [x] mvp_c1_s137: DONE, P̄=5.49%
- [x] mvp_c4_s42: DONE, P̄=5.49%
- [x] mvp_c4_s137: DONE, P̄=5.49%
- [x] mvp_c2_s42: DONE, P̄=5.49%
- [x] Attention weight 分析: bridge tokens dead memory 确认
- [ ] ~~mvp_c2_s137~~: 跳过（C2_s42 已确认无效）
- [ ] ~~mvp_c3_s42/s137~~: 跳过（bridge tokens 已确认 dead memory, D003）

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D004 | 2026-05-18 | MVP KILL 确认，项目终止。Position reset 和 bridge tokens 均无 | mvp_c2_s42, mvp_c4_s42, mvp_c4_s137, mvp_c1_s42, mvp_c1_s137 |
| D003 | 2026-05-18 | Phase 1 gate KILL 确认，等 C2 结果做最终项目去留判定；跳过 C3 实验 | mvp_c4_s42, mvp_c1_s42, mvp_c1_s137 |
| D002 | 2026-05-18 | MVP 主模型确定为 Mistral-7B-Instruct-v0.1（rope_theta=10K | — |
| D001 | 2026-05-18 | MVP 主模型从 Qwen2.5-7B (base=1M) 切换到 base≈10K 模型，Qwen | — |


