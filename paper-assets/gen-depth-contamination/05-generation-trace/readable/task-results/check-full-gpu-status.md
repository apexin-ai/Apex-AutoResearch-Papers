# check full gpu status

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_full_gpu_status_20260516T112818_result.json`
- **Structured JSON:** [`39786ca13104cf7668f1.json`](../../sessions/39/39786ca13104cf7668f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

| 实验 | GPU | PID 状态 | 结果 | K* | 1v2 AUC | 关键发现 |
|------|-----|----------|------|-----|---------|----------|
| exp-018 LLaMA-8B | 0 (96%, 16GB) | 10403 RUNNING 6h27m | 无结果，仍在生成 | — | — | 进展慢，结果目录仍空 |
| exp-019b Mistral cross | 1 (0%, 4.5GB) | 36365 RUNNING 5m | Feature extraction 中 | — | — | 生成已完成，正在 VocabDiv d=1 (60%) |
| exp-020 Pythia greedy | 2 (100%, 16.5GB) | ✅ **DONE** | K*=2 | **2** | **0.8838** | Pythia greedy K*=2，与 Qwen 一致 |
| exp-020 Pythia nuc09 | 2 | 27042/27742/28604 RUNNING | depth 5 gen ~20% | — | — | ⚠️ 3个重复进程写同一目录 |
| exp-020 Pythia t07/t12 | — | NOT_STARTED | — | — | — | |
| exp-021 length_128 | — | ✅ **DONE** | K*=2 | **2** | **0.6219** | 短文本 AUC 略低 |
| exp-021 length_256 | — | ✅ **DONE** | K*=2 | **2** | **0.6282** | 与 128 一致 |
| exp-021 length_512 | 3 (88%, 3.9GB) | 32175 RUNNING 1h22m | depth 3 gen (18%) | — | — | 预计 ~2h 完成 |

---

### 已完成实验数据

**exp-020 Pythia greedy** (`results_exp020_pythia_greedy/pairwise_auc.json`):
```json
{"mean": {"0v1": 0.9992, "1v2": 0.8838, "2v3": 0.5342, "3v4": 0.5228, "4v5": 0.5162}}
```

**exp-021 length_128** (`results/exp_021_length_128/pairwise_auc.json`):
```json
{"mean": {"0v1": 0.9791, "1v2": 0.6219, "2v3": 0.5291, "3v4": 0.5349, "4v5": 0.5012}}
```

**exp-021 length_256** (`results/exp_021_length_256/pairwise_auc.json`):
```json
{"mean": {"0v1": 0.9914, "1v2": 0.6282, "2v3": 0.5556, "3v4": 0.5298, "4v5": 0.5137}}
```

---

### ⚠️ 问题：exp-020 nuc09 有 3 个重复进程

GPU2 上有 3 个 python 进程 (PID 27042, 27742, 28604) 全部写入同一个 `results_exp020_pythia_nuc09/` 目录，参数完全相同。这可能导致数据竞争/文件损坏。可能是 `exp020_pythia_decoding.sh` 脚本重复启动了。要不要我 kill 多余进程只保留一个？

---

### 关键发现

1. **Pythia greedy K\*=2 且 1v2 AUC=0.88** — 比 Qwen-1.5B (K\*=2, 1v2≈0.63) 高很多，说明 Pythia 在 greedy 下更容易被检测（可能因为 greedy 缺乏多样性导致特征区分度更高）
2. **Length ablation: K\*=2 对 128/256 都成立**，1v2 AUC 分别 0.62 和 0.63，差异极小。说明在这个范围内文本长度对 depth boundary 影响不大
3. exp-019b 的 cross-scorer 实验已经到 feature extraction 阶段，预计 ~30-40min 出结果

---

由于 exp-020 和 exp-021 都只是部分完成（子配置级别），暂不更新 registry 为 DONE。等全部子配置完成后再统一收割。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "mean": {
      "0v1": 0.9914,
      "1v2": 0.6282,
      "2v3": 0.5556,
      "3v4": 0.5298,
      "4v5": 0.5137
    }
  }
}
```

</details>

---
