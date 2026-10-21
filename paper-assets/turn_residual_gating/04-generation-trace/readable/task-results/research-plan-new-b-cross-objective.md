# research plan new b cross objective

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan_new_b_cross_objective_20260520T062637_result.json`
- **Structured JSON:** [`6674743ee82c5419f75c.json`](../../sessions/66/6674743ee82c5419f75c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。基于代码结构、现有实验和文献调研，分析如下：

---

## 推荐方案

**选择**: 候选 A — Turn-level Representation Coherence (TRC)

**理由**:
1. **机制正交**：GAR 测量 attention 空间的 goal-token 注意力分配；TRC 测量 hidden state 空间的 turn 间表示一致性。两个不同的特征空间，reviewer 无法用"同一机制的变体"来驳回。
2. **exposure bias 预测清晰**：TF 下模型看到 gold context，相邻 turn 的 hidden state 应收敛到一致的表示流形；gen 下 context 漂移，hidden state 轨迹发散——预期 TRC 指标同样出现 TF/gen gap。
3. **文献无先例**：调研结果确认，现有论文（UBARv2, TA&AT, Adaptive Bridge）只研究主 loss 的 exposure bias 退化，**没有人展示过 auxiliary objective 在 autoregressive generation 下坍塌**。两个不同族的 objective 同时坍塌，这个 claim 很强。
4. **实现极简**：`detect_turn_boundaries()` 已返回 `assistant_last_token_positions`，`model(..., output_hidden_states=True)` 已可获取 hidden states，新增代码约 30-40 行。

**具体公式**:
```
TRC_i = cos_sim(h^L_t_i, h^L_t_{i+1})   # L = final layer, t_i = assistant turn i 的 last token position
L_TRC = (mean(TRC) - τ)²                  # MSE target mode, τ=0.85 (初始值，可调)
```

用 MSE target 与 GAR 保持一致的 loss mode（v7 的成功经验）。

**实现方案**:

| 修改文件 | 内容 |
|---------|------|
| `src/train_phase2.py` | 添加 `--lambda_trc`, `--trc_target` 参数；loss 计算处提取 `outputs.hidden_states[-1]` 在 `assistant_last_positions` 处的向量，计算相邻 pair 的 cos_sim，MSE loss |
| `src/eval_model_gen.py` | 在 model-gen eval 中同样测量 TRC（hidden state cos_sim），与 GAR 并列报告 |
| `src/train_phase2.py` (logging) | 添加 `trc/train`, `trc/mean_cos_sim` 到 wandb log |

**关键实现细节**:
- 只需 `outputs.hidden_states[-1]`（最后一层），不需要全层；`output_hidden_states=True` 在现有代码中已有条件使用
- 至少需要 2 个 assistant turn 才能计算 TRC，单 turn 样本跳过此 loss
- 不需要 GARMeasurer 或 attention hooks——纯粹从 hidden states 计算

**预估成本**: ~3 GPU-h（与 v7 训练等价，TRC 计算开销可忽略；额外开销仅来自 `output_hidden_states=True` 的内存占用，Qwen2.5-7B 28 层约多 ~2GB）

**风险**:
- 相邻 turn 的 cos_sim 初始值可能已经很高（同一 conversation 的 hidden states 本身就相似），导致 TRC 的 TF/gen gap 不够显著 → 缓解：先做 baseline 测量，调整 target τ
- 如果 hidden state 空间的 exposure bias 效应弱于 attention 空间 → 这本身也是有价值的阴性结果（说明 exposure bias 的影响是 mechanism-dependent）

---

## 备选方案

**选择**: 候选 C 变体 — Turn-Boundary Prediction Loss (TBP)

**理由**: 不作为训练 loss，而是作为**诊断指标**。测量 turn boundary token 位置上的 NTP cross-entropy，比较 TF 和 gen 两种 context 下的差异。

优势：零实现成本（只需在 eval 时过滤位置）；能直观展示 exposure bias 在 turn 切换点最严重。

劣势：不是 trainable auxiliary objective，说服力弱于 TRC。但可以作为 paper 中的 supplementary analysis。

---

**建议执行顺序**:
1. 先在 v7 checkpoint 上做 **baseline TRC 测量**（TF 和 gen），确认 gap 存在
2. 确认 gap 后再加 TRC loss 训练新版本（v10）
3. 同时收集 TBP 诊断数据作为 supplementary

需要我开始实现 TRC 的 baseline 测量代码吗？

---
