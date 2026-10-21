# audit canonical data protocol

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_canonical-data-protocol_20260524T224440_result.json`
- **Structured JSON:** [`9fd70767ce75d864c6b9.json`](../../sessions/9f/9fd70767ce75d864c6b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

# 1. 审计矩阵（任务 A）

**关键发现**：注册表 `server` 字段不可靠（很多是 `harvest` 记录的服务器，不代表当前位置）。直接 SSH 5 台服务器抓取 JSON 元数据后，整体只有两类有效数据：

- **新 smolvla family**：`n_rollouts=20`，`baseline_mode="single"`，2026-05-23 之后产出
- **旧 openvla family**：`n_rollouts=10`，无 Adaptive 模式，与新数据**不可比较**（不参与 paired test）

⚠️ 还发现 **2 个 K=2 mean 文件被误命名为 `vla_only`**（`baseline_mode: "mean"`），如不区分会污染数据：
- `bjb2-28827/eval_spatial_vla_only_seed42.json`：实际是 K=2 mean，SR=0.815
- `cqa1-32758/eval_spatial_vla_only_seed44.json`：实际是 K=2 mean，SR=0.81
- `bjb1-32546/eval_spatial_k2mean_seed46.json`：正确命名，K=2 mean，SR=0.80

注：用户提到 "s46 K=2 异常" 其实更准确说是 **s44 在 cqa1-32758 的 vla_only 文件实为 K=2**（这是被误用作 baseline 的真隐患）。s46 真正的 vla_only K=1 文件在多服务器都存在且数值一致（0.805），是干净的。s46 的 -0.5pp Δ 是真实结果而非 K 错配。

**完整审计矩阵**（新 smolvla family + 老 openvla family）：

```
seed | server      | mode_actual    | baseline | n_roll | SR     | tau  | date       | notes
-----|-------------|----------------|----------|--------|--------|------|------------|------------------
42   | bjb1-18228  | vla_only       | single   | 20     | 0.800  |  -   | 2026-05-25 | new smolvla
42   | bjb1-32546  | adaptive_crm   | single   | 20     | 0.795  | 0.25 | 2026-05-25 | new smolvla
42   | bjb1-32546  | vla_only       | single   | 10     | 0.300  |  -   | 2026-05-19 | OLD openvla (incompat)
42   | bjb2-28827  | vla_mean_K2 ⚠️ | mean     | 20     | 0.815  |  -   | 2026-05-23 | K=2 mean (file misnamed)
42   | bjb2-40593  | adaptive_crm   | single   | 20     | 0.790  | 0.25 | 2026-05-25 | new smolvla
42   | cqa1-32758  | vla_only       | single   | 20     | 0.785  |  -   | 2026-05-25 | new smolvla
43   | bjb1-32546  | adaptive_crm   | single   | 20     | 0.800  | 0.25 | 2026-05-23 | new smolvla
43   | bjb2-28827  | vla_only       | single   | 20     | 0.805  |  -   | 2026-05-23 | new smolvla
43   | cqa1-32758  | vla_only       | single   | 20     | 0.790  |  -   | 2026-05-23 | new smolvla
44   | bjb1-32546  | adaptive_crm   | single   | 20     | 0.805  | 0.25 | 2026-05-23 | new smolvla
44   | bjb2-28827  | vla_only       | single   | 20     | 0.805  |  -   | 2026-05-23 | new smolvla
44   | bjb2-40593  | vla_only       | single   | 20     | 0.785  |  -   | 2026-05-23 | new smolvla
44   | cqa1-32758  | vla_mean_K2 ⚠️ | mean     | 20     | 0.810  |  -   | 2026-05-23 | K=2 mean (file misnamed)
45   | bjb2-28827  | adaptive_crm   | single   | 20     | 0.800  | 0.25 | 2026-05-24 | new smolvla
45   | bjb2-28827  | vla_only       | single   | 20     | 0.800  |  -   | 2026-05-24 | new smolvla  ✓ pair
45   | cqa1-32758  | adaptive_crm   | single   | 20     | 0.800  | 0.25 | 2026-05-24 | new smolvla
45   | cqa1-32758  | vla_only       | single   | 20     | 0.770  |  -   | 2026-05-24 | new smolvla  ✓ pair
46   | bjb1-32546  | k2mean         | mean     | 20     | 0.800  |  -   | 2026-05-24 | K=2 mean (correctly named)
46   | bjb2-28827  | vla_only       | single   | 20     | 0.805  |  -   | 2026-05-24 | new smolvla
46   | cqa1-32758  | adaptive_crm   | single   | 20     | 0.800  | 0.25 | 2026-05-24 | new smolvla  ✓ pair
46   | cqa1-32758  | vla_only       | single   | 20     | 0.805  |  -   | 2026-05-24 | new smolvla  ✓ pair
47   | cqa1-32758  | adaptive_crm   | single   | 20     | 0.815  | 0.25 | 2026-05-24 | new smolvla  ✓ pair
47   | cqa1-32758  | adaptive_crm   | single   | 20     | 0.790  | 0.25 | 2026-05-24 | duplicate file (different filename)
47   | cqa1-32758  | vla_only       | single   | 20     | 0.810  |  -   | 2026-05-24 | new smolvla  ✓ pair
48   | bjb2-28827  | adaptive_crm   | single   | 20     | 0.810  | 0.25 | 2026-05-25 | new smolvla
48   | cqa1-32758  | vla_only       | single   | 20     | 0.795  |  -   | 2026-05-25 | new smolvla
49   | bjb2-28827  | adaptive_crm   | single   | 20     | 0.820  | 0.25 | 2026-05-25 | new smolvla
49   | cqa1-32758  | vla_only       | single   | 20     | 0.785  |  -   | 2026-05-25 | new smolvla
50-54| bjb1-*      | vla_only       | single   | 10     | 0.27-0.33 | - | 2026-05-20 | OLD openvla (incompat)
```

**用户提问的具体核查**：
- s42 Adaptive K=10 原始数据**没有被 K=1 覆盖**：bjb1-32546 上 2026-05-25 有 `eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json`，SR=0.795；bjb2-40593 上也有 2026-05-25 的副本，SR=0.79
- s46 K=2 异常：用户混淆——s46 在 cqa1-32758/bjb2-28827 上的 vla_only 文件都是 `baseline_mode="single"`，**没问题**。真正的 K=2 误命名问题在 **s44 (cqa1-32758) 和 s42 (bjb2-28827)**

# 2. canonical_data_sources.yaml

```yaml
spatial_paired_data:
  selection_principle: |
    同服务器配对——每个 seed 的 VLA-only 和 Adaptive 必须来自同一台服务器，
    且必须满足 n_rollouts=20 + baseline_mode=single（排除 K=2 mean 误命名文件）。
    模型 family 固定为 smolvla (CRM checkpoint: crm_smolvla_3suite_v1)，
    Adaptive 参数固定为 mode=adaptive_conformal_crm, conformal_threshold=0.25, max_correction_norm=0.2。

  excluded_data:
    s46_k2_concern: "用户提及的 s46 K=2 异常实际不存在；bjb1-32546 的 k2mean_seed46.json 是单独的 K=2 实验文件，未被误用为 baseline"
    misnamed_k2_files:
      - file: bjb2-28827/eval_spatial_vla_only_seed42.json
        actual: vla_mean K=2 (baseline_mode=mean), SR=0.815
        action: 不得用作 s42 VLA-only baseline
      - file: cqa1-32758/eval_spatial_vla_only_seed44.json
        actual: vla_mean K=2 (baseline_mode=mean), SR=0.810
        action: 不得用作 s44 VLA-only baseline
    old_openvla_files:
      n_rollouts: 10
      seeds: [42-49, 50-54 on bjb1-32546/bjb1-18228]
      action: 与新 smolvla (n=20) 不可混用

  pairs:  # 严格同服务器
    s45_cqa:
      seed: 45
      server: cqa1-32758
      vla_only_file: logs/eval_spatial_vla_only_seed45.json
      vla_only_SR: 0.770
      adaptive_file: logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json
      adaptive_SR: 0.800
      adaptive_tau: 0.25
      delta_pp: +3.00
    s45_bjb2:  # 备选/冗余
      seed: 45
      server: bjb2-28827
      vla_only_SR: 0.800
      adaptive_SR: 0.800
      delta_pp: 0.00
      note: |
        与 s45_cqa 同 seed 跨服务器对比：VLA SR 0.77 vs 0.80，Adapt SR 0.80 vs 0.80。
        说明同 seed 在两台 4090 集群上结果不一致（环境/数值非确定性），
        正好印证 reviewer 关于"跨服务器方差与改进幅度同量级"的担忧。
    s46_cqa:
      seed: 46
      server: cqa1-32758
      vla_only_file: logs/eval_spatial_vla_only_seed46.json
      vla_only_SR: 0.805
      adaptive_file: logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json
      adaptive_SR: 0.800
      adaptive_tau: 0.25
      delta_pp: -0.50
    s47_cqa:
      seed: 47
      server: cqa1-32758
      vla_only_file: logs/eval_spatial_vla_only_seed47.json
      vla_only_SR: 0.810
      adaptive_file: logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed47.json
      adaptive_SR: 0.815
      adaptive_tau: 0.25
      delta_pp: +0.50
      note: 同目录另有 eval_spatial_adaptive_conformal_crm_tau0.25_seed47.json (SR=0.790)；
            选用带 norm0.2 命名的版本作为 canonical

  gaps:  # 需要补跑的实验
    - seed: 42
      has: ["adaptive on bjb1-32546", "adaptive on bjb2-40593",
            "vla_only on cqa1-32758", "vla_only on bjb1-18228"]
      needs: "vla_only on bjb1-32546 OR vla_only on bjb2-40593 OR adaptive on cqa1-32758/bjb1-18228"
      recommended: "Adaptive on cqa1-32758（与已有 VLA-only seed42 配对，cqa1 已有 GPU 空闲）"
    - seed: 43
      has: ["adaptive on bjb1-32546", "vla_only on bjb2-28827", "vla_only on cqa1-32758"]
      needs: "vla_only on bjb1-32546 OR adaptive on bjb2-28827/cqa1-32758"
      recommended: "Adaptive on cqa1-32758"
    - seed: 44
      has: ["adaptive on bjb1-32546", "vla_only on bjb2-28827", "vla_only on bjb2-40593"]
      needs: "vla_only on bjb1-32546 OR adaptive on bjb2-28827/bjb2-40593"
      recommended: "Adaptive on bjb2-28827（同服务器已有 vla_only s44）"
    - seed: 48
      has: ["adaptive on bjb2-28827", "vla_only on cqa1-32758"]
      needs: "vla_only on bjb2-28827 OR adaptive on cqa1-32758"
      recommended: "Adaptive on cqa1-32758"
    - seed: 49
      has: ["adaptive on bjb2-28827", "vla_only on cqa1-32758"]
      needs: "vla_only on bjb2-28827 OR adaptive on cqa1-32758"
      recommended: "Adaptive on cqa1-32758"

  statistics:
    n_valid_unique_seed_pairs: 3
    n_with_redundant_s45: 4
    mean_delta_pp: +1.00
    sd_delta_pp: 1.80
    ci95_pp: [-3.48, +5.48]
    paired_t_p_value: 0.4380   # n=3, df=2 → 统计功率不足
    wilcoxon_p_value: null     # n<6 不可靠
    cohens_dz: 0.55            # medium

  for_reference_cross_server:
    description: "spatial_per_task_breakdown.md 当前采用的 8-seed 跨服务器配对（违反 canonical 原则）"
    n: 8
    mean_delta_pp: +1.50
    paired_t_p_value: 0.0142
    wilcoxon_p_value: 0.0234
    warning: "5/8 pair 跨服务器，方差结构受服务器混淆影响；当前 p=0.0142 不能视为最终结果"
```

# 3. Final p-value 计算（任务 C）

**严格同服务器（n=3，cqa1-32758 only）：**

| 指标 | 值 |
|---|---|
| n（unique seeds） | 3 |
| Mean Δ | **+1.00pp** |
| SD Δ | 1.80pp |
| 95% CI | **[−3.48, +5.48] pp** |
| Paired t-test | t=0.961, df=2, **p=0.4380** |
| Wilcoxon | n<6，不可靠 |

**当前跨服务器 8-seed（违反 canonical 原则，仅供对照）：**

| 指标 | 值 |
|---|---|
| n | 8 |
| Mean Δ | +1.50pp |
| 95% CI | [+0.41, +2.60] pp |
| Paired t-test | t=3.240, df=7, **p=0.0142** |
| Wilcoxon | W=2.000, **p=0.0234** |

# 4. 缺口列表（补跑建议）

按优先级排列（每条都是单 GPU、~30min 任务）：

| 优先级 | seed | mode | server | 命令模板 |
|---|---|---|---|---|
| P0 | 42 | `adaptive_conformal_crm` | cqa1-32758 | `--mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25 --max_correction_norm 0.2` |
| P0 | 43 | `adaptive_conformal_crm` | cqa1-32758 | 同上，`--seed 43` |
| P0 | 44 | `adaptive_conformal_crm` | bjb2-28827 | 同上，`--seed 44`（同服务器已有 vla_only s44） |
| P0 | 48 | `adaptive_conformal_crm` | cqa1-32758 | 同上，`--seed 48` |
| P0 | 49 | `adaptive_conformal_crm` | cqa1-32758 | 同上，`--seed 49` |

**补跑后预期**：n=8 同服务器对（cqa1: 42,43,45,46,47,48,49 + bjb2-28827: 44），可用 paired t-test + Wilcoxon。基于现有数据外推（mean Δ ≈ +1.0~1.5pp，SD ≈ 1.5），8 个同服 pair 应能给出 p ≈ 0.01~0.05。

**重要修订**：当前 `spatial_per_task_breakdown.md` 的 p=0.0142 由 5/8 跨服务器对支撑，不能作为最终 reviewer response。必须补跑 P0 列表的 5 个 Adaptive 实验才能给出真正符合 canonical 原则的统计结论。

---
