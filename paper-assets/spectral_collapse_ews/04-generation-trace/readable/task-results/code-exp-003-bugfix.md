# code exp 003 bugfix

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_003_bugfix_20260517T124617_result.json`
- **Structured JSON:** [`89a1e22c69de62e881d9.json`](../../sessions/89/89a1e22c69de62e881d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## 产出汇总

### 1. nvidia-smi
- GPU 0: PID 59365 (exp_001, phase0 resume Gen 4+) — 86% util, 65.9GB — **保留**
- GPU 1: PID 88161 (exp_003, phase1 adaptive) — 已 kill

### 2. exp_003 kill 确认
通过 `kill_job` 工具 force kill 成功。GPU 1 已释放。

### 3. Bug 修复 Diff

#### Bug #1: 预算扣减用实际值
**controller.py** — 新增 `report_actual()` 方法：
```python
def report_actual(self, actual_ratio):
    if not self.history:
        return
    last = self.history[-1]
    allocated = last["r"]
    correction = allocated - actual_ratio
    self.B_rem += correction
    last["r_actual"] = actual_ratio
    last["B_rem"] = self.B_rem
```
**pipeline.py** — 每代混合后调用 `controller.report_actual(actual_ratio)`

#### Bug #2: Gen 0 baseline 初始化
**controller.py** — 新增 `set_baseline()` 方法：
```python
def set_baseline(self, spectral_metrics):
    key = {"eff_rank": "effective_rank"}.get(self.signal, self.signal)
    S_0 = spectral_metrics[key]
    self.S_tilde_prev = S_0
    self.S_tilde_0 = S_0
```
**pipeline.py** — controller 创建后立即调用 `controller.set_baseline(results_all[0])`

#### Bug #3: 数据架构改为固定 total
**旧公式**（total 随 ratio 膨胀，ratio>0.5 被 pool cap）:
```python
num_real = int(len(synthetic_data) * current_ratio / (1 - current_ratio))
num_real = min(num_real, len(real_train_data))
train_data = synthetic_data + real_subset  # total = 50K + num_real
```
**新公式**（total=50K 恒定，ratio 直接控制占比）:
```python
num_real = int(total_per_gen * current_ratio)   # ratio=0.8 → 40K real
num_synth = total_per_gen - num_real             # ratio=0.8 → 10K synth
# 只生成 num_synth 条 synthetic，而非全量 50K
```

### 4. 数据方案
- **选择**: 固定 total=50K per gen，real/synth 比例由 ratio 直接控制
- **原因**: real pool=50K 可支持 ratio ≤ 1.0；消除了 total training volume 随 ratio 变化的混淆因子；不需要额外 real data

### 5. Dry-run 10 代模拟表格

```
Gen   S_t          S_tilde      delta      triggered  r_raw    r_clip   r_actual  B_rem    real    synth
1     (no input)   -            -          -          0.5000   0.5000   0.5000    4.5000   25000   25000
2     2464.7622    2415.7229    -0.020721  no         0.5000   0.5000   0.5000    4.0000   25000   25000
3     2469.9277    2442.8253    -0.011452  no         0.5000   0.5000   0.5000    3.5000   25000   25000
4     2440.5657    2441.6955    0.000477   no         0.5000   0.5000   0.5000    3.0000   25000   25000
5     2405.0498    2423.3727    0.007742   YES        0.5027   0.5027   0.5027    2.4973   25137   24863
6     2370.1726    2396.7726    0.011239   YES        0.5057   0.5057   0.5057    1.9916   25284   24716
7     2335.1653    2365.9690    0.013016   YES        0.5059   0.5059   0.5059    1.4857   25295   24705
8     2304.1904    2335.0797    0.013052   YES        0.5033   0.5033   0.5033    0.9824   25163   24837
9     2252.1189    2293.5993    0.017527   YES        0.5037   0.5037   0.5037    0.4787   25186   24814
10    2200.0474*   2246.8233    0.019764   YES        0.4935   0.4787   0.4787    0.0000   23934   26066
```
*Gen 9 metrics 外推（Phase 0 尚未跑到 Gen 9）

**验证结果**: ✓ Baseline 正确 | ✓ Gen 5 首次触发 | ✓ Budget 耗尽 (B_rem≈0) | ✓ 所有 ratio 可物理实现

### 6. Tau 建议
**tau=0.005 合适**。正向 delta 分布：min=0.000477, max=0.0198, mean=0.0118。tau=0.005 在 Gen 5 首次触发（delta 从 Gen 3→4 的明显下降开始累积），灵敏度合理。唯一未触发的正 delta (Gen 4, 0.000477) 是噪声级别，不应响应。

### 7. 建议启动命令

```bash
cd /root/spectral_collapse_ews && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1 python run_phase1.py --condition adaptive --seed 42 --k 1.0 --tau 0.005 --signal log_det --generations 10
```

等你确认后提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "eff_rank": "effective_rank"
  }
}
```

</details>

---
