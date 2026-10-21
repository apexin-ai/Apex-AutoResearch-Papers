# analysis conditional granger path fix v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_conditional_granger_path_fix_v2_20260521T051254_result.json`
- **Structured JSON:** [`cfd88779c8c03b20d7aa.json`](../../sessions/cf/cfd88779c8c03b20d7aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报对比：

## 新旧结果对比

| | 旧版 (19828) | 新版 (17855) |
|---|---|---|
| **实验数** | 11 | **31** |
| **总 pairs** | 44 | **124** |
| **覆盖范围** | 仅 α=0.50/0.55/0.75 + 4个模型 | 全 α sweep (0.00–1.00) + C4 + 4模型 + T=20 |

### Conditional Granger 显著率 (p<0.05, lag=1)

| 模式 | 旧版 | 新版 |
|---|---|---|
| entropy_only | 4/44 (9.1%) | 28/124 (22.6%) |
| ece_only | 11/44 (25.0%) | 18/124 (14.5%) |
| both | 12/44 (27.3%) | 41/124 (33.1%) |
| neither | 17/44 (38.6%) | 37/124 (29.8%) |
| **entropy 总显著** | **16/44 (36.4%)** | **69/124 (55.6%)** |
| **ECE 总显著** | **23/44 (52.3%)** | **59/124 (47.6%)** |

### 关键定性变化

1. **ECE 不再是 dominant channel。** 旧版中 ECE 显著率 (52.3%) 明显高于 entropy (36.4%)，新版反转为 entropy (55.6%) > ECE (47.6%)。

2. **原因：旧版样本偏差。** 旧版仅包含 α≥0.50 的实验，而高 α 区间 ECE 信号更强。新版加入低 α (0.00–0.45) 后，这些区间 entropy 是主导 channel（ECE 几乎无独立贡献），拉高了 entropy 的总显著率。

3. **两个 canary 互补而非单一主导。** 新版 "both" 占 33.1%，说明在 ~1/3 的 pair 中两者都有独立贡献。按 α 分段看：
   - **低 α (0.00–0.25)**: entropy 主导，ECE 几乎不显著
   - **中 α (0.30–0.50)**: 高度冗余（unconditional 都极显著，conditional 互相吸收）
   - **高 α (0.60–1.00)**: 开始分化，ECE 在部分 pair 贡献独立信息
   - **T=20**: ECE 恢复更强独立贡献（更长时间序列提升检验功效）

4. **Partial R² 方向不变。** 在跨模型实验中 ECE 的 partial R² 在部分模型（qwen, smollm3）仍然很高（>0.9），但 entropy 在 pythia410m 和 C4 corpus 上 partial R² 更高。

**结论：从 "ECE dominant" 修正为 "entropy 和 ECE 互补，主导权随 α 和模型而变"。**

---
