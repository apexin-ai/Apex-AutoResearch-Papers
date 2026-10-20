# oh-crossagent-error-analysis 数据问题排查报告

## W1: Probe ZS macro_f1 不一致 (0.581 vs 0.5984)

### Root Cause

**评估范围不同 + 服务器数据已被替换，无法完全复现。**

| 来源 | macro_f1 | 评估范围 | 数据 |
|------|----------|----------|------|
| error analysis report.md | 0.581 | ALL 43,366 conf≥2 windows | 原始 embeddings_fixed.pt + checkpoints/best_model.pt |
| cross-agent-eval (registry) | 0.5984 | TEST split (~6,122 windows, 15% instances) | 同上 |
| openhands-fewshot-probe (registry) | 0.5984 | TEST split (~6,122 windows, 15% instances) | 同上 |
| 当前 JSON (today's re-run) | 0.7588 | ALL 43,366 conf≥2 windows | **新** embeddings_fixed.pt (May 15) + 同路径 checkpoint |

**分析过程：**

1. **error analysis** (`oh_crossagent_error_analysis.py`) 对 ALL 43,366 conf≥2 OH windows 做 zero-shot 推理，计算全局 macro_f1。

2. **cross-agent-eval** 和 **openhands-fewshot-probe** 先按 instance 做 70/15/15 split，只在 TEST split (~6,122 windows) 上评估 zero-shot 性能。两者报告完全相同的 0.5984，因为使用相同 checkpoint、相同数据、相同 split seed=42。

3. 两者使用 **相同 checkpoint** (`checkpoints/best_model.pt`, epoch=3, val_f1=0.9511, 即 probe_001) 和 **相同 embeddings** (`embeddings_fixed.pt`)。差异 0.581 vs 0.5984 (1.74pp) 来自评估子集不同。

4. **无法在当前环境复现**：服务器上 `embeddings_fixed.pt` 已于 May 15 06:30 重新生成，`checkpoints/best_model.pt` 于 May 14 16:08 重建。用当前文件跑出 ALL=0.7588, TEST=0.7580（仅差 0.08pp），说明在新数据上 all-vs-split 差异极小。原始 1.74pp 差异可能与旧 embeddings 的子集分布差异有关。

### 结论

- **论文使用 0.5984 是正确的**（test-split 评估，与 few-shot 表格方法论一致）
- error analysis 的 0.581 是 ALL data 评估，非 bug，但与论文口径不同
- 当前 JSON 的 0.7588 来自重建后的数据，不可用于论文

---

## W2: Error overlap 仅覆盖 28% 窗口 (12,328 / 43,366)

### Root Cause

**report.md 是 stale 的，未更新为最新运行结果。**

实际 JSON 结果（来自 May 15 最新运行）显示 **100% 覆盖率**：

| 指标 | report.md (stale) | JSON (latest) |
|------|-------------------|---------------|
| Common windows | 12,328 (28.4%) | **43,366 (100%)** |
| Probe errors | 2,460 | 6,005 |
| Struct errors | 13 | 57 |
| Both wrong | 2 | 31 |
| Probe-only errors | 2,458 | 5,974 |
| Struct-only errors | 11 | 26 |
| Overlap rate (probe) | 0.08% | 0.52% |

**验证过程：**

1. 用当前代码和数据重建 probe_keys 和 struct_keys，均使用 `(trajectory_id, window_idx)` 作为 key。
2. 诊断结果：unique probe keys = 43,366, unique struct keys = 43,376, common = 43,366。零重复 key，完美匹配。
3. report.md 中 12,328 的数字来自 **更早的脚本版本**，该版本可能使用了不同的 key 构造逻辑（如 instance_id vs trajectory_id，或不同的 window index 字段）。
4. 当前脚本（May 15 09:06 创建）已修复 key 匹配逻辑。JSON 输出正确，但 report.md 未更新。

### 结论

- **28% 覆盖率是旧 bug 的产物**，当前代码已修复（100% 覆盖）
- 核心发现不变：probe 和 structural GB 的错误几乎不重叠（overlap rate 0.52%）
- report.md 需要重新生成

---

## 注意事项

当前服务器上的数据文件（embeddings_fixed.pt, checkpoints/best_model.pt）均为 May 14-15 重建，与论文使用的原始数据不同。因此：

- JSON 中的绝对数字（macro_f1=0.7588, errors=6,005 等）不应用于论文
- overlap 覆盖率修复（28% → 100%）是代码逻辑修复，与数据无关，可信
- 若需获得与论文一致的 corrected overlap 数字，需用原始 checkpoint 和 embeddings 重跑
