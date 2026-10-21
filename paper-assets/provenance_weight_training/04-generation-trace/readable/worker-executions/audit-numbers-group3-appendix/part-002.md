# audit numbers group3 appendix — Part 2 of 2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../audit-numbers-group3-appendix.md) · [Structured JSON](../../../sessions/7e/7eb11a7da3fbe1204f2f.json)

## Before a recorded user message

### Task result

_source line 83_

两处修复已生效。下面是完整审计报告。

---

## Appendix 数字真实性审计报告

**审计范围**: `appendix.tex` 全部 12 张表 + 行间数字，共约 **260 个数字**

### 一、已修复问题（2 处）

| 文件:行号 | 数字 | 问题 | 处理 |
|-----------|------|------|------|
| appendix.tex:397 | Δ=−0.60pp | HellaSwag 72.49−73.08=−0.59，非−0.60 | 已改为 −0.59pp |
| appendix.tex:363 | ECE "to 0.05" | 全文其他位置（experiments.tex, tab:detector）均用 0.048，此处精度不一致 | 已改为 0.048 |

### 二、出处存疑 / 需人工确认的数字（4 处）

#### 1. **[严重]** Tab:detector TF-IDF PPL 与 Tab:tau τ=0.80 不一致

- Tab:detector（L344）: TF-IDF+LR, τ=0.8, 3 seeds → **17.650 ± .010**, Δ=−0.044
- Tab:tau（L120）: τ=0.80, 3 from-scratch seeds → **17.683 ± .006**, Δ=−0.011
- 差值 **0.033**，超过 SD
- Registry 交叉验证：`adaptive_fix` 系列（τ=0.8, n_min=2）3-seed mean ≈ 17.651，与 tab:detector 吻合；tab:tau 的 17.683 可能来自另一批 from-scratch 训练
- **疑因**: Tab:detector 可能混入了 checkpoint-resumed seed 42 结果（resume artifact section 已警告此问题），或两表使用了不同实验批次
- **建议**: 确认 tab:detector 的 TF-IDF 行是否使用纯 from-scratch seeds；若是，更新为与 tab:tau 一致的 17.683±.006（Δ=−0.011）

#### 2. **[轻微]** Tab:hybrid ρ=0.6 Hybrid PPL

- 论文（L172）: 17.530
- Registry `hybrid_rho06_seed42`: **17.526**
- 差值 0.004，需确认是否有更新版本的实验

#### 3. **[轻微]** Tab:rho06 ESS-only seeds 123/456

- 论文: 两个都写 **17.760**
- Registry: seed 123 = **17.763**, seed 456 = **17.762**
- 影响: 若用 registry 值，mean 从 17.763 变为 17.765（仍与 Uniform 17.763 接近，但不完全相等）

#### 4. **[标注]** Tab:dr_threshold q>0.5 可能是 3-seed 均值

- 表中 q>0.5 Raw PPL = 17.28，caption 写 "seed 42 unless noted"
- Registry seed 42: 17.291 (v1) / 17.285 (v2)，均 ≠ 17.28
- Registry 3-seed v2 均值: (17.285+17.272+17.277)/3 = **17.278 ≈ 17.28** ✓
- 建议: 如确实是 3-seed mean，应像 q>0.3 一样加 † 脚注

### 三、正文 ↔ Appendix 交叉一致性验证

| 交叉项 | Appendix | 正文 (results/experiments/discussion) | 一致? |
|--------|----------|---------------------------------------|-------|
| Adaptive τ=0.7 5-seed holdout | 17.674±.006 (tab:tau) | 17.674±.006 (tab:main) | ✓ |
| Uniform 3-seed baseline | 17.694 (tab:tau caption) | (17.694+17.686+17.702)/3=17.694 | ✓ |
| Δ_H at τ=0.7 vs 3-seed unif | −0.020 | (17.674−17.694=−0.020) | ✓ |
| Δ at 5-seed (tab:main) | −0.023 (caption note) | 17.674−17.697=−0.023 | ✓ |
| τ=0.7 OWT Δ | −0.028 | −0.028 (results L147) | ✓ |
| τ=0.7 Wiki Δ | −0.029 | −0.029 (results L147) | ✓ |
| τ=0.8 OWT Δ | −0.005 | −0.005 (results L147) | ✓ |
| τ=0.8 Wiki Δ | −0.009 | −0.009 (results L147) | ✓ |
| ρ=0.6 adaptive mean | 17.731±.004 | 17.731±0.004 (results L81) | ✓ |
| ρ=0.6 uniform mean | 17.763±.008 | 17.763±0.008 (results L81) | ✓ |
| ρ=0.6 hierarchy | Grid < Adaptive < Uniform ≈ ESS < Random | Same (results L82) | ✓ |
| ρ=0.6 paired t (3dp) | t=−9.95, p=0.010 | t=−9.95, p_BH=0.064 (results L81) | ✓ |
| p_BH=0.011 at ρ=0.4 | app:power L476 | results L31 | ✓ |
| p_BH=0.064 at ρ=0.6 | app:power L477 | results L81 | ✓ |
| Grid b=0.3 3-seed mean | 17.620±.033 (tab:aux via cross-ref) | 17.620±.033 (tab:aux) | ✓ |
| b=1.0 ≈ uniform | 17.692 (tab:grid_full) | 17.692 vs 17.694 (results L34) | ✓ |
| D&R q>0.3 3-seed | 17.250±.001 | 17.250±.001 (tab:epoch_match) | ✓ |
| D&R q>0.7 raw | 17.32 | 17.32 (tab:epoch_match) | ✓ |
| ESS-only gap at ρ=0.4 | 0.043 (L271) | 0.043 (results L38) | ✓ |
| B=16 Δ amplification | 3.0×, −0.068±0.005 (L76) | 3.0×, −0.068±0.005 (results L155) | ✓ |
| Spearman r B=4 | 0.699 (tab:alpha_corr & L76) | 0.699 | ✓ |
| ρ=0.2 Δ | +0.046 (L374) | +0.046 (discussion L6) | ✓ |
| ρ=0.3 Δ | +0.002 (L461) | Within [0.3,0.4] boundary (discussion L6) | ✓ |
| Cross-model MMLU | +1.57pp (tab:cross_model) | +1.6pp (results L115, rounded) | ✓ |
| Cohen's d | 3.83 = 0.023/0.006 (L469) | — (arithmetic ✓) | ✓ |
| Downstream mean | 0.5414 (tab:downstream caption) | 0.5414 (discussion L31) | ✓ |
| ECE gap 2.7× | 0.131/0.048=2.73 (L332) | 2.7× (results L122) | ✓ |
| τ-ρ paired t | −4.70 (fig caption L149) | −4.70 (results L147) | ✓ |
| Training steps | 6,103 (L72) | 6,103 (experiments tab:config) | ✓ |

### 四、Registry 交叉验证

| 数据 | 论文 | Registry | 一致? |
|------|------|----------|-------|
| Grid b=0.1–5.0 seed 42 | 9 values | 9 values exact match | ✓ |
| Grid b=0.3 3-seed mean | 17.620 | (17.64+17.579+17.64)/3=17.620 | ✓ |
| ρ=0.6 Adaptive 3 seeds | 17.735/17.727/17.732 | 17.735/17.727/17.732 | ✓ |
| ρ=0.6 Uniform 3 seeds | 17.766/17.754/17.770 | 17.766/17.754/17.77 | ✓ |
| ρ=0.6 Random 3 seeds | 17.832/17.870/17.880 | 17.832/17.87/17.88 | ✓ |
| ρ=0.6 Grid b=0.3 | 17.634 | 17.634 | ✓ |
| ρ=0.3 all 6 holdout values | match | match exactly | ✓ |
| D&R q>0.3 3-seed | 17.250 | 17.25/17.25/17.2509 → 17.250 | ✓ |
| D&R q>0.7 3-seed | 17.32 | 17.32/17.32/17.32 | ✓ |
| Epoch-matched all 5 values | match | match exactly | ✓ |
| Hybrid ρ=0.4 | 17.514 | 17.514 | ✓ |
| GPT-2 detector 3-seed PPL | 17.792 | (17.79+17.788+17.797)/3=17.792 | ✓ |
| N-gram detector 3-seed PPL | 17.823 | (17.820+17.823+17.826)/3=17.823 | ✓ |
| Golden Ratio seed 42 | 17.654 (tab:aux) | 17.654 | ✓ |
| ρ=0.2 Δ=+0.046 | 17.382−17.336=0.046 | 17.382−17.336=0.046 | ✓ |
| Detector AUC=0.94, ECE=0.048, T=0.204 | match | AUC=0.939≈0.94, ECE=0.048, T=0.204 | ✓ |
| α_eff correlation, per-seed stats | — | NOT in registry (separate analysis script) | 无法验证 |
| Cross-model MMLU/HellaSwag | — | NOT in registry | 无法验证 |
| Detector hyperparams (50k, C=1.0) | — | Registry 记录不同值 (10k, C=0.01)，可能是旧版配置 | 无法验证 |

### 五、算术抽检（全部通过）

- Tab:rho06 所有 mean/SD: 手动重算均一致 ✓
- Tab:tau 所有 Δ: 手动重算均一致 ✓
- Tab:detector Δ: 17.650−17.694=−0.044 ✓ (算术正确，但基数可能有问题，见第二节)
- Tab:rho03 Δ: (17.427−17.425)/=+0.002 ✓
- Cohen's d: 0.023/0.006=3.83 ✓; λ=3.83×√5=8.56 ✓
- Tab:alpha_corr_perseed spread: max−min 算术 ✓
- Cross-model MMLU Δ: 53.42−51.85=1.57 ✓

### 总结

- **审计数字**: ~260
- **已修复**: 2（HellaSwag Δ 算术、ECE 精度）
- **需确认**: 4（detector table 最重要，其余为小数点级精度问题）
- **无法从 registry 验证**: 3 类（α_eff 相关分析、Llama MMLU/HellaSwag、detector 超参细节）
- **正文-附录一致性**: 全部 30+ 项交叉引用一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1142043,
  "duration_api_ms": 1561156,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "b883e8c8-4e70-4c1d-86d0-e21cb1b9cee9",
  "total_cost_usd": 3.8348272499999996,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 82294,
    "cache_read_input_tokens": 366296,
    "output_tokens": 48167,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 82294,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 3501,
        "cache_read_input_tokens": 103283,
        "cache_creation_input_tokens": 987,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 987
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1421,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001516,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 34,
      "outputTokens": 78237,
      "cacheReadInputTokens": 1351770,
      "cacheCreationInputTokens": 192213,
      "webSearchRequests": 0,
      "costUSD": 3.8333112499999995,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "1b7ce474-5171-4523-a2b2-6199e5d306f2"
}
```

</details>

---
