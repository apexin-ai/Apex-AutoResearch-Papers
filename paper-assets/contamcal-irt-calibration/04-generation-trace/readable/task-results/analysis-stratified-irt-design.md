# analysis stratified irt design

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_stratified-irt-design_20260515T134139_result.json`
- **Structured JSON:** [`32a207624f638aa3bd74.json`](../../sessions/32/32a207624f638aa3bd74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功。以下是完整统计：

### Scheme A: by Dosage

| 分层 | N_models | mmlu | gsm8k | arc_challenge | humaneval |
|------|----------|------|-------|---------------|-----------|
| d000 | 6 | 4 OK | 0 SKIP (D044) | 4 OK | 6 OK |
| d005 | 4 | 1 SKIP | 4 OK | 1 SKIP | 4 OK |
| d025 | 4 | 1 SKIP | 4 OK | 1 SKIP | 4 OK |
| d100 | 4 | 4 OK | 4 OK | 4 OK | 4 OK |

### Scheme B: by Model Size

| 分层 | N_models | mmlu | gsm8k | arc_challenge | humaneval |
|------|----------|------|-------|---------------|-----------|
| 0.5B | 8 | 0 SKIP (D045) | 6 OK | 0 SKIP (D045) | 8 OK |
| 1.5B | 6 | 6 OK | 4 OK | 6 OK | 6 OK |
| 3B | 4 | 4 OK | 2 SKIP | 4 OK | 4 OK |

### 统计功效评估

**Scheme A 问题：**
- d005/d025 的 mmlu 和 arc_challenge 排除后只剩 1 个模型（0.5B 被 D045 排除），无法拟合
- 单 dosage 分层中 exposure 是常数，gamma 不可点识别（d000: exposure=0 → gamma=prior；其余 dosage: exposure=constant → gamma 与 b_j 混淆）
- 可跑的组合：gsm8k 全部 4 个分层 + humaneval 全部 4 个 + d000/d100 的 mmlu/arc

**Scheme B 是主力分析：**
- 1.5B 最完整：4 个 benchmark 全部 N≥4，dosages=[0,5,25,100]，gamma 可识别
- 0.5B 只有 gsm8k 和 humaneval 可用，但 dosages=[0,5,25,100]，gamma 可识别
- 3B gsm8k 不够（d000 被 D044 排除后只剩 2 个 d100），其余 3 个 benchmark OK，dosages=[0,100]

脚本已部署到 `/root/contamcal-irt-calibration/exp006/run_stratified_irt.py`，输出目录 `/root/autodl-tmp/exp006/results_stratified_irt/`。

---
