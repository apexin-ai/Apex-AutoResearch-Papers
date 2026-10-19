# code de integration prep

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_de-integration-prep_20260523T062125_result.json`
- **Structured JSON:** [`0b6f7bce7d6780715f51.json`](../../sessions/0b/0b6f7bce7d6780715f51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

### 创建/修改的文件

| 文件 | 位置 | 说明 |
|------|------|------|
| `src/integrate_de_results.py` | 服务器 `/root/clkc_mech_interp/` | DE 结果集成脚本 |
| `figures/gen_fig3_asymmetry_forest.py` | 服务器 `/root/clkc_mech_interp/` | Fig 3 forest plot（DE 行已注释预留） |
| `artifacts/de_paper_patches.md` | 本地 artifacts 目录 | 两种 scenario 论文段落模板 |

### integrate_de_results.py dry-run (mock Scenario A)

```
4-Direction Bootstrap Summary (Llama-3.1, EN-DE, n=2000)
  EN->EN    L19   0.7508  [0.7169, 0.7831]
  DE->DE    L16   0.7102  [0.6654, 0.7511]
  EN->DE    L14   0.6250  [0.5588, 0.6912]
  DE->EN    L18   0.6380  [0.5735, 0.6985]

Δ_DE = +1.30pp  CI [-4.52, 7.12]  p=0.3312  (NOT significant)
→ Scenario A: Token overlap does not drive EN-ZH asymmetry
```

输出同时保存 `de_integration_summary.json`（含 scenario 判定）。

### Fig 3 DE placeholder 位置

`gen_fig3_asymmetry_forest.py` 第 22 行：
```python
# ("Llama-3.1 (DE)", DELTA_DE, CI_LO_DE, CI_HI_DE, "de"),
```
取消注释并填入实际值即可。y 轴、分隔线、section header 均已预留扩展点。

### 结果就绪后一行命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/clkc_mech_interp && \
python3 src/integrate_de_results.py --results_file data/llama31/de_bootstrap_n2000_results.json
```

---
