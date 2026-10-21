# research exp004 source verify

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_exp004-source-verify_20260518T060557_result.json`
- **Structured JSON:** [`26f3dc2620127dbb5325.json`](../../sessions/26/26f3dc2620127dbb5325.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

---

## Registry 条目

```yaml
exp_004_7b_crossscale:
  status: DONE
  conclusion: success
  retry_count: 1
  created_at: '2026-05-15T11:08:22.198Z'
  updated_at: '2026-05-15T23:37:24.772Z'
  completed_at: '2026-05-15T22:26:45.097Z'
  
  hypothesis: >
    K*=2 在 7B scale 下是否成立？Qwen2.5-7B continuation mode, 
    C4 5K seeds, scorer=Qwen2.5-1.5B。Reviewer R2 Critical: 现有实验仅 ≤1.5B

  spec:
    server: westc-26893
    model_name: Qwen/Qwen2.5-7B (fp16, 14.5GB) + Qwen2.5-1.5B-Instruct (scorer)
    data_count: 5000
    seed: 42
    gpu: [cuda:0]
    data_path: /root/autodl-tmp/gen-depth-contamination/data_exp004_qwen7b
    command: >
      bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base 
      && cd /root/autodl-tmp/gen-depth-contamination && bash scripts/exp004_resume_feat.sh"
    note: "Resume: data generation complete, rerunning feature extraction + classification 
      with corrected scorer path. PID 127516."

  metrics:
    k_star: 2
    pairwise_auc: {0v1: 0.9644, 1v2: 0.6178, 2v3: 0.546, 3v4: 0.5225, 4v5: 0.5091}
    pairwise_auc_std: {0v1: 0.0034, 1v2: 0.0081, 2v3: 0.0028, 3v4: 0.0113, 4v5: 0.0052}
    bootstrap_ci:
      0v1: {auc: 0.9638, ci: [0.9607, 0.9665], perm_p: 0.0001}
      1v2: {auc: 0.6168, ci: [0.6079, 0.6261], perm_p: 0.0001}
      2v3: {auc: 0.5492, ci: [0.5388, 0.5594], perm_p: 0.0001}
      3v4: {auc: 0.5276, ci: [0.517, 0.5375], perm_p: 0.0001}
      4v5: {auc: 0.5085, ci: [0.4988, 0.5191], perm_p: 0.0676}
    bootstrap_resamples: 1000
    permutation_resamples: 10000
    pairwise_jsd: {0v1: 0.1274, 1v2: 0.0101, 2v3: 0.0048, 3v4: 0.0048, 4v5: 0.0033}
    ordinal_mae: 1.2156
    ordinal_accuracy: 0.3523
    top_features: [freq_entropy, surp_d1_skew, surp_std, surp_d1_mean, surp_mean]
    key_finding: >
      K*=2 confirmed at 7B scale. 1v2 CI lower=0.6079>0.60 (robust). 
      2v3 CI upper=0.5594<0.60. FR-4 Warning resolved.

  checkpoint_path: /root/autodl-tmp/gen-depth-contamination/data_exp004_qwen7b/
  log_path: /root/runs/gen-depth-contamination/exp_004_7b_crossscale.log
  
  failure_reason: process dead 5× with no sentinel/W&B — auto-resolved as failed
  previous_failure:
    conclusion: failed
    notes: >
      进程 5 次死亡无 W&B metrics，cron 自动标记 failed。
      模型加载成功(14530MB)，C4 采样有进度，日志末尾异常出现 transformers 全量模型列表。
      诊断后 data generation 已完成，重跑 feature extraction + classification 后成功。
  notes: >
    初始运行因进程死亡 5 次被 cron 标记 failed。诊断 Worker 发现数据生成已完成，
    重跑 feature extraction + classification（exp004_resume_feat.sh）后成功。
    K*=2 在 7B scale 下确认成立。0v1 AUC=0.964 低于所有 1.5B 模型（>0.99），
    符合预期：更大模型生成更 human-like 文本。1v2=0.618 仍 >θ=0.60。
```

## 服务器文件搜索

### cqa1-22115
- `find` 搜索 exp_004 / 7b_crossscale：**无结果**
- `data_exp004_qwen7b` 目录：**不存在**
- `scripts/exp004*`：**不存在**
- `results/` 目录：无 exp_004 相关子目录
- `data/` 目录：无 exp_004 相关内容
- `/root/runs/` 搜索：**无结果**
- `git log` 搜索：**无匹配**

### westd-42896
- `find` 搜索 exp_004 / 7b_crossscale：**无结果**
- `results/` 目录：只有 exp_14b_c4 和 exp_32b_c4
- `data/` 目录：同上
- `/root/runs/` 搜索：**无结果**

## 结论

实验 **确实执行过并成功完成**（registry 记录完整 metrics 和 key finding），但：

1. **跑在第三台服务器 `westc-26893`** 上，不是 cqa1-22115 或 westd-42896。数据路径 `data_exp004_qwen7b` 和日志 `exp_004_7b_crossscale.log` 都指向 westc-26893。
2. cqa1 和 westd 上完全没有该实验的任何残留文件（数据、脚本、日志、results 均无）。
3. 如需访问原始数据/日志，需要连接 **westc-26893** 服务器查看 `/root/autodl-tmp/gen-depth-contamination/data_exp004_qwen7b/` 和 `/root/runs/gen-depth-contamination/exp_004_7b_crossscale.log`。

---
