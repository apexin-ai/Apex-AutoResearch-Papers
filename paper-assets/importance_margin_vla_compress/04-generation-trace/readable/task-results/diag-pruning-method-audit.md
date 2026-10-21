# diag pruning method audit

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_pruning_method_audit_20260518T150744_result.json`
- **Structured JSON:** [`a0364b76be3301dc73ec.json`](../../sessions/a0/a0364b76be3301dc73ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据到齐。以下是完整审计报告。

---

## 数据完整性审计报告

### 根因确认：cqa1 运行的是 BUGGY 版本

**cqa1-33015** `eval_success_rate_libero.py`（448行）和 **westd-27271** 的（498行）**不是同一版本**。

**cqa1 buggy 版本** — `register_acis_hook()` 第193行:
```python
if tokens.dim() != 3 or tokens.shape[1] != mask.shape[1]:
    return output  # 64 != 128 → pruning 从未执行
```
Connector 每个摄像头输出 64 tokens，ACIS mask 覆盖 128 tokens（双摄像头拼接）。`64 != 128` 永远为 True，hook 直接返回未修改的 output。

**westd 修复版本** — 使用 offset 追踪:
```python
state = {"offset": 0}
# ...
n = tokens.shape[1]           # 64
offset = state["offset"]       # 0 或 64
cam_mask = mask[:, offset:offset + n]  # 切片正确的 64-token 段
state["offset"] = offset + n   # 推进到下一个摄像头
```

---

### 逐条件审计

| 条件 | 实验 ID | 服务器 | 脚本 | pruning_method | 是否有 bug | SR | 有效性 |
|------|---------|--------|------|---------------|-----------|-----|--------|
| random k=0.95 | `eval_smolvla_random_prune_k095` | cqa1 | `eval_random_prune_smolvla.py` | **true_removal**（硬编码） | 无（不同脚本，无维度守卫） | **0%** (0/500) | **有效** |
| random k=0.5 (ACIS ckpt) | `eval_random_prune_k05` | westd | `eval_success_rate_libero.py`（修复版） | **zero_mask**（默认值） | 无 | **0%** (0/500) | **有效** |
| random k=0.5 (官方 ckpt) | `eval_official_smolvla_prune_k05_v2` | westd | `eval_official_libero.py` | **true_removal**（该脚本默认值） | 无 | **0%** (0/500) | **有效** |
| random k=0.3 | — | — | — | — | — | — | **不存在于 registry** |
| random k=0.7 | — | — | — | — | — | — | **不存在于 registry** |
| random k=0.9 | — | — | — | — | — | — | **不存在于 registry**（仅有 k=0.95） |
| ACIS k=0.5 tasks 0-5 (westd) | `eval_stage1only_object_v2_fixed` | westd | `eval_success_rate_libero.py`（修复版） | **zero_mask**（默认值，已正确执行） | 无 | **0%** (0/500, 全10个task) | **有效** |
| **ACIS k=0.5 tasks 6-9 (cqa1)** | `eval_acis_k05_supplement_200eps` | cqa1 | `eval_success_rate_libero.py`（**BUGGY**） | zero_mask（配置值，**但从未执行**） | **有 bug** | **47.5%** (95/200) | **无效 — 实为未剪枝 baseline** |
| ACIS k=0.5 true_removal | `eval_true_removal_k05` | westd | `eval_success_rate_libero.py`（修复版） | **true_removal**（显式指定） | 无 | **0%** (0/500) | **有效** |
| ACIS k=0.7 zero_mask | `eval_k07_zero_mask` | westd | `eval_success_rate_libero.py`（修复版） | **zero_mask**（显式指定） | 无 | **0%** (0/500) | **有效** |
| ACIS k=0.9 zero_mask | `eval_stage1only_k09` | westd | `eval_success_rate_libero.py`（修复版） | **zero_mask** | 无 | **0%** (0/500) | **有效** |
| ToMe/merge k=0.5 | `eval_merge_k05` | westd | `eval_success_rate_libero.py`（修复版） | **merge**（merge_alpha=1.0） | 无 | **0%** (0/500) | **有效** |
| Geometric k=0.5 | `eval_geometric_prior_k05` | cqa1 | `eval_geometric_prior_k05.py` | **true_removal**（硬编码） | 无（不同脚本） | **0%** | **有效** |
| Geometric k=0.7 | `eval_geometric_prior_k07` | cqa1 | `eval_geometric_prior.py` | **true_removal**（硬编码） | 无 | **0%** | **有效** |
| Geometric k=0.9 | `eval_geometric_prior_k09` | cqa1 | `eval_geometric_prior.py` | **true_removal**（硬编码） | 无 | **0%** | **有效** |

---

### 关键问题解答

**1. 每个条件用的是什么 pruning method?**

三个不同的 eval 脚本有不同的默认值：
- `eval_success_rate_libero.py` — 默认 **zero_mask**（可通过 `--pruning_method` 修改）
- `eval_random_prune_smolvla.py` — 硬编码 **true_removal**
- `eval_official_libero.py` — 默认 **true_removal**
- `eval_geometric_prior*.py` — 硬编码 **true_removal**

**2. ACIS tasks 0-5 和 tasks 6-9 的 pruning method 是否一致?**

**配置层面一致**（都是 zero_mask 默认值），**执行层面不一致**：
- Tasks 0-5（westd，修复版）：zero_mask 正确执行 → 0% SR
- Tasks 6-9（cqa1，buggy 版）：zero_mask 从未执行 → 47.5% SR = 未剪枝 baseline

佐证：westd 修复版已覆盖全部 10 个 task（包括 tasks 6-9），结果均为 0%。cqa1 supplement 的 47.5% 与该模型的 unpruned baseline（44.8% overall，其中 T6=62%, T7=38%, T8=50%, T9=52%）数值范围吻合。

**3. 如果不一致，哪个是正确的?**

westd 修复版（全 10 tasks = 0%）是正确的。cqa1 supplement（47.5%）应丢弃。

**4. 代码比较**

| | cqa1-33015 | westd-27271 |
|---|---|---|
| 文件 | `eval_success_rate_libero.py` | `eval_success_rate_libero.py` |
| 行数 | 448 | 498 |
| register_acis_hook | 维度守卫 `tokens.shape[1] != mask.shape[1]` | offset 追踪（正确切片 128→64+64） |
| random_prune mode | 不支持 | 支持 |
| compute_random_mask | 不存在 | 存在 |
| 日志输出 | 不含 PRUNING 字段 | 含 PRUNING 字段 |

---

### 结论

**Table 1 "6 pruning conditions all 0%" 的结论是正确的**，前提是基于 westd 修复版的结果。cqa1 supplement 的 47.5% SR 是由于运行了未修复的脚本，pruning 从未实际执行，该数据点应标记为无效。

**Director 的假设（true_removal vs zero_mask 差异导致结果不同）并非根因。** 真实原因是 cqa1 的脚本版本有维度守卫 bug，导致 pruning 整体失效。在修复版上，无论 zero_mask 还是 true_removal，结果都是 0% SR。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "offset": 0
  }
}
```

</details>

---
