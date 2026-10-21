# data extract plan006 values

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_extract_plan006_values_20260521T000305_result.json`
- **Structured JSON:** [`d0c04a885dda52d822d4.json`](../../sessions/d0/d0c04a885dda52d822d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan006_exact_values.txt`（507 行，47081 字符）。

数据来源是本地已有的 `artifacts/plan006/asv_empirical_results.json`（121KB），无需远程读取。

提取内容：
- **Table 1**: 9 个 config 的 macro_f1 / weighted_f1（含 qwen3 few-shot-5 = 0.0 的异常行）
- **Table 1b**: 63 行 config × topology 完整 F1 + bias
- **Table 2**: 63 行 bias 详情（tau_hat / bias / bias_pct / sign_flip）
- **Table 3**: 189 行 ASV（magnitude / significance / sign_flip 三种 asv_type）
- **Table 4**: 63 行 Type I/II + ASV safety
- **Table 5**: Summary 统计
- **Table 6**: Per-topology unsafe 计数（exposure/frontdoor/iv 各 ~89% unsafe，confounding/collider/mbias = 0%）
- **Table 7**: Inter-model correlation（civil_comments/vast 全为 1.0/1.0/0.0；humaid 有实际变异）
- **Table 8**: 8 个 confusion matrix（10×10）完整数值
- **Table 9**: 总 63 scenarios，31 ASV-unsafe（49.2%）

所有数值保留 JSON 原始精度，无四舍五入。无 plan003 本地目录。

---
