# figures atlas figure fixes

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figures_atlas_figure_fixes_20260515T042151_result.json`
- **Structured JSON:** [`84c6578008a68c666cbc.json`](../../sessions/84/84c6578008a68c666cbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。汇报：

---

### 4 个 Bug 修复结果

| Bug | 修复内容 | 验证 |
|-----|---------|------|
| **Bug 1** EDD off-by-one | `edd_val = idx + 2` → `idx + 1` | Pythia topk/OLMo topk 均显示 EDD=3（idx=2 处 d2v3 AUC < 0.75），"7/9 configs" 统计正确 |
| **Bug 2** 解码策略不一致 | Pythia 无 nucleus 数据，改为标注策略：Pythia (temp=0.9)、OLMo (nucleus p=0.95)、GPT-2 XL (nucleus p=0.95) | `model_key` 保留用于颜色映射，`model` 含策略标签 |
| **Bug 3** 硬编码 accuracy | 标题改为 5-fold CV 计算：`cv_acc = np.trace(cm) / cm.sum() * 100` | GPT-2 XL/temp: **85.8%**（原硬编码 85.4%）；Pythia/top-k: **68.8%**（原 69.6%）。与 CM 对角线一致 |
| **Bug 4** OLMo RF 核对 | Registry 确认 cross_model_olmo_002: RF=0.788, LR=0.751 → 78.8% 是 RF | 全部 9 格值与 registry RF accuracy 匹配（Pythia temp 76.25% → 76.3% 为四舍五入差异，可接受） |

8 个文件（PDF+PNG）已重新生成到 `artifacts/figures/`。

---
