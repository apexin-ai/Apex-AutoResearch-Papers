# code prepare 7b postprocessing

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-7b-postprocessing_20260520T033218_result.json`
- **Structured JSON:** [`0165f8899afeb3208c08.json`](../../sessions/01/0165f8899afeb3208c08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 7B 后处理 Pipeline 审查报告

### 一、各脚本输入/输出/参数

#### 1. `compute_signals.py`
| 项 | 值 |
|---|---|
| 输入 | `--input-dir &lt;dir>` — 期望 `&lt;dir>/fewnerd/samples.jsonl` 或 `&lt;dir>/samples.jsonl` |
| 输出 | `full_signal_report.json` + `fewnerd_per_instance.json`（写入 input-dir 或 `--output-dir`） |
| 关键参数 | `--model-size 7 --regime ft` |
| 依赖 | `consistency.py`（通过 `STRUCT_CODE_DIR` 加载，默认 `/root/autodl-tmp/struct_self_consist_ie/code`） |

#### 2. `format_for_scaling.py`
| 项 | 值 |
|---|---|
| 输入 | `--report &lt;path>/full_signal_report.json --model-size 7 --regime ft` |
| 输出 | 打印到 stdout — 需手动 copy-paste 到 `plot_scaling_curve.py` DATA dict |
| 注意 | 接受多个 `--report`，但**无内置 multi-seed 平均**，每个 report 独立输出 |

#### 3. `bootstrap_construction.py`
| 项 | 值 |
|---|---|
| 输入 | `--per-instance &lt;path>/fewnerd_per_instance.json --dataset fewnerd` 或 `--input-dir` |
| 输出 | `fewnerd_paired_bootstrap_result.json` |
| 参数 | B=10000, seed=42, paired bootstrap |

#### 4. `plot_scaling_curve.py`
| 项 | 值 |
|---|---|
| 数据格式 | `DATA[(7, "ft", "FewNERD")] = {"lp_rho": ..., "sj_rho": ..., "degen": ..., ...}` |
| 当前状态 | 7B FewNERD 行已有 placeholder（全 None），需填入 3-seed 平均值 |

---

### 二、实际路径与服务器分布

| 服务器 | Seed | 路径 |
|--------|------|------|
| autodl-5090-c | 42 | `/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/fewnerd/samples.jsonl` |
| autodl-5090-b | 123 | `/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed123/fewnerd/samples.jsonl` |
| autodl-5090-b | 456 | `/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed456/fewnerd/samples.jsonl` |

**路径注意**：post_completion_checklist.md 写的是 `output/qwen25_7b_fewnerd_seed42`，但实际推理目录是 `output/fewnerd_7b/qwen25_7b_n8_seed42/`。checklist 中的路径**不准确**，执行时必须用实际路径。

---

### 三、跨服务器数据传输

**不需要提前汇集原始数据。** compute_signals.py 对每个 seed 独立运行，可在各自服务器上原地执行。最终只需传输 3 个 `full_signal_report.json` + 3 个 `fewnerd_per_instance.json`（小文件，几 KB）到同一台服务器做聚合。

---

### 四、需要修改/补充的地方

1. **缺少 3-seed 平均聚合步骤**：`format_for_scaling.py` 只处理单个 report，不做 multi-seed mean。需要手动算 3 个 report 的均值后填入 `plot_scaling_curve.py` DATA dict，或写一个简单聚合脚本。
2. **post_completion_checklist.md 路径错误**：`output/qwen25_7b_fewnerd_seedXXX` 应改为 `output/fewnerd_7b/qwen25_7b_n8_seedXXX`。
3. **consistency.py 必须在服务器 code/ 目录下**：compute_signals.py 通过 `STRUCT_CODE_DIR` 导入。如果 code/ 目录没有 `consistency.py`，SJ/FK 信号会被跳过（只打 WARNING，不报错）。需确认服务器上已部署。

---

### 五、完整执行计划

#### Phase 1: 各服务器独立执行 compute_signals（可并行）

```bash
# === Server C (autodl-5090-c): seed42 ===
cd /root/autodl-tmp/struct_self_consist_ie
python artifacts/compute_signals.py \
  --input-dir output/fewnerd_7b/qwen25_7b_n8_seed42 \
  --model-size 7 --regime ft

# === Server B (autodl-5090-b): seed123 ===
cd /root/autodl-tmp/struct_self_consist_ie
python artifacts/compute_signals.py \
  --input-dir output/fewnerd_7b/qwen25_7b_n8_seed123 \
  --model-size 7 --regime ft

# === Server B (autodl-5090-b): seed456 ===
cd /root/autodl-tmp/struct_self_consist_ie
python artifacts/compute_signals.py \
  --input-dir output/fewnerd_7b/qwen25_7b_n8_seed456 \
  --model-size 7 --regime ft
```

**可并行**：3 个 seed 完全独立，B 上两个可同时跑。

#### Phase 2: bootstrap_construction（可并行，与 Phase 1 在同一服务器顺序执行）

```bash
# === Server C: seed42 ===
python artifacts/bootstrap_construction.py \
  --per-instance output/fewnerd_7b/qwen25_7b_n8_seed42/fewnerd_per_instance.json \
  --dataset fewnerd \
  --output-dir output/fewnerd_7b/qwen25_7b_n8_seed42

# === Server B: seed123 ===
python artifacts/bootstrap_construction.py \
  --per-instance output/fewnerd_7b/qwen25_7b_n8_seed123/fewnerd_per_instance.json \
  --dataset fewnerd \
  --output-dir output/fewnerd_7b/qwen25_7b_n8_seed123

# === Server B: seed456 ===
python artifacts/bootstrap_construction.py \
  --per-instance output/fewnerd_7b/qwen25_7b_n8_seed456/fewnerd_per_instance.json \
  --dataset fewnerd \
  --output-dir output/fewnerd_7b/qwen25_7b_n8_seed456
```

#### Phase 3: 收集结果到一台服务器（Server B 或 A）

```bash
# 从 Server C 拉 seed42 的 report 到 Server B
scp autodl-5090-c:/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/full_signal_report.json \
    /root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/full_signal_report.json
```

或者直接在本地（control plane）收集 3 个 JSON。

#### Phase 4: format_for_scaling + 手动 3-seed 平均

```bash
# 各 seed 独立 format（查看各 seed 数值）
python artifacts/format_for_scaling.py \
  --report output/fewnerd_7b/qwen25_7b_n8_seed42/full_signal_report.json \
  --model-size 7 --regime ft

python artifacts/format_for_scaling.py \
  --report output/fewnerd_7b/qwen25_7b_n8_seed123/full_signal_report.json \
  --model-size 7 --regime ft

python artifacts/format_for_scaling.py \
  --report output/fewnerd_7b/qwen25_7b_n8_seed456/full_signal_report.json \
  --model-size 7 --regime ft
```

然后**手动计算 3-seed 均值**（lp_rho, sj_rho, vc_rho, degen, construction_lp_delta, greedy_f1, oracle_f1），填入 `plot_scaling_curve.py` 的 `(7, "ft", "FewNERD")` 条目。

#### Phase 5: 生成图表

```bash
python artifacts/plot_scaling_curve.py
# 输出: artifacts/scaling_signal_rho.pdf, scaling_degeneracy.pdf, scaling_construction_delta.pdf, scaling_curve_draft.pdf
```

---

### 六、并行性总结

| Phase | 步骤 | 并行度 |
|-------|------|--------|
| 1 | compute_signals ×3 | 3 并行（跨服务器） |
| 2 | bootstrap ×3 | 3 并行（Phase 1 各自完成后） |
| 3 | scp 收集 | 串行 |
| 4 | format + 手动平均 | 串行 |
| 5 | plot | 串行 |

总耗时估计：Phase 1 是瓶颈（FewNERD 4706 instances × SJ/FK 计算较重，单 seed 约 5-15 min），Phase 2 约 2 min/seed，Phase 3-5 < 1 min。

---
