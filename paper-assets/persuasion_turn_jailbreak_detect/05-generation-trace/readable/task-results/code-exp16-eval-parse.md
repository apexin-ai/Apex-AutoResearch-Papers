# code exp16 eval parse

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16-eval-parse_20260519T234317_result.json`
- **Structured JSON:** [`eef5ba52654815f154bd.json`](../../sessions/ee/eef5ba52654815f154bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data extracted. Here's the complete summary.

---

## Summary N/A 原因

`scripts/eval_exp16.py` 第 ~126 行 summary 打印代码：
```python
f1 = r.get("macro_f1", r.get("f1_macro"))
```
但实际 JSON 结构是嵌套的 `r["overall"]["f1_macro"]`，顶层没有 `macro_f1` 或 `f1_macro` 字段，所以全部返回 None → 显示 N/A。

**修复**：改为 `f1 = r.get("overall", {}).get("f1_macro")`

---

## Exp16 完整结果

### Per-seed Macro F1

| Variant | Seed | mixed_test | qwen_test | dd_ood | aa_ood | llama_dd | llama_aa | toxicchat |
|---------|------|-----------|----------|--------|--------|----------|----------|-----------|
| vanilla | 42 | 0.8146 | 0.9605 | 0.0244 | 0.1111 | 0.0000 | 0.0000 | 0.3449 |
| vanilla | 123 | 0.7895 | 0.9071 | 0.0361 | 0.1209 | 0.0000 | 0.0000 | 0.3343 |
| vanilla | 456 | 0.8023 | 0.9071 | 0.1753 | 0.2661 | 0.0000 | 0.0385 | 0.3526 |
| mlm_only | 42 | 0.8540 | 0.9737 | 0.0244 | 0.0000 | 0.0000 | 0.0000 | 0.2934 |
| mlm_only | 123 | **0.3619** | **0.3619** | **1.0000** | 0.4366 | 0.4949 | 0.4118 | 0.0775 |
| mlm_only | 456 | 0.8289 | 0.9208 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.1200 |
| 9class | 42 | 1.0000 | 1.0000 | 0.3798 | 0.1753 | 0.3243 | 0.0741 | 0.8646 |
| 9class | 123 | 1.0000 | 1.0000 | 0.4839 | 0.3277 | 0.4624 | 0.2424 | 0.8646 |
| 9class | 456 | 0.9868 | 1.0000 | 0.4030 | 0.1489 | 0.3421 | 0.0566 | 0.8540 |

### Mean ± Std (3 seeds)

| Variant | mixed_test | qwen_test | dd_ood | aa_ood | llama_dd | llama_aa | toxicchat |
|---------|-----------|----------|--------|--------|----------|----------|-----------|
| vanilla | .802±.010 | .925±.025 | .079±.069 | .166±.071 | .000±.000 | .013±.018 | .344±.008 |
| mlm_only | .681±.226 | .752±.277 | .341±.466 | .146±.206 | .165±.233 | .137±.194 | .164±.093 |
| 9class | **.996±.006** | **1.000±.000** | **.422±.045** | **.217±.079** | **.376±.061** | **.124±.084** | **.861±.005** |

### 关键发现

1. **9class 全面最优**：in-domain 接近完美（mixed .996, qwen 1.000），OOD 和 cross-LLM 也显著领先，toxicchat .861 远超其他。

2. **mlm_only seed123 是异常值**：in-domain 崩塌（mixed .36, qwen .36）但 dd_ood 达 1.00。该模型大概率将几乎所有样本预测为 jailbreak，导致 all-jailbreak OOD 集虚高、in-domain 暴跌。mlm_only 方差极大（std 0.2-0.5），训练不稳定。

3. **所有 variant 在 OOD 上都较弱**：即使最好的 9class，dd_ood 仅 .42，aa_ood .22，llama_aa .12，说明 OOD 泛化仍是主要瓶颈。

4. **vanilla 的 llama_dd/llama_aa 全为 0**：vanilla 模型完全无法检测 Llama 生成的攻击对话。

---
