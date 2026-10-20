# ops mistral baseline audit

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mistral-baseline-audit_20260523T150325_result.json`
- **Structured JSON:** [`af85ed6d35de61ea715b.json`](../../sessions/af/af85ed6d35de61ea715b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是完整结果。

---

## Mistral Clean Baseline 审计报告

### 1. Baseline 来源确认

**mean=4.024, SD=2.052** 来自 `bca_bootstrap.py` 第 88 行的 10 个 hardcoded free-theta lz* 值：

```python
mistral_free = [5.4175, -1.0456, 3.2792, 3.9558, 4.4910, 5.5030, 5.8982, 5.7996, 3.5214, 3.4159]
```

mean(10 values) = 4.0236 ≈ 4.024 ✓

### 2. Eval 版本：**V1（Snijders 2001 corrected）**

`eval_lz.py` 第 116-150 行的 `compute_lz_star` 实现包含完整的 Snijders 校正：
```python
Var_star = Var_l0 - C_theta ** 2 / I_theta
return (l0 - E_l0) / np.sqrt(Var_star)
```

**与 Llama 不同，Mistral 不存在 V0/V1 问题。** eval 从一开始就是 V1。

### 3. 6 个 result 文件 vs hardcoded 值对比

| Seed | Result file lz* | bca hardcoded | 匹配 |
|------|----------------|---------------|------|
| clean (s1) | 5.4175 | 5.4175 | ✓ |
| clean_s2 | -1.0456 | -1.0456 | ✓ |
| clean_s3 | 3.2792 | 3.2792 | ✓ |
| clean_s8 | 5.7996 | 5.7996 | ✓ |
| clean_s9 | 3.5214 | 3.5214 | ✓ |
| clean_s10 | 3.4159 | 3.4159 | ✓ |

6 个可验证的值全部一致。

### 4. Checkpoint 路径（6 个存活）

```
/root/autodl-tmp/ctrl_contam_mistral/checkpoints/clean/
/root/autodl-tmp/ctrl_contam_mistral/checkpoints/clean_s2/
/root/autodl-tmp/ctrl_contam_mistral/checkpoints/clean_s3/
/root/autodl-tmp/ctrl_contam_mistral/checkpoints/clean_s8/
/root/autodl-tmp/ctrl_contam_mistral/checkpoints/clean_s9/
/root/autodl-tmp/ctrl_contam_mistral/checkpoints/clean_s10/
```

每个 checkpoint 下有 3 个子 checkpoint（313/626/939）+ 最终 adapter。

### 5. 丢失的 s4-s7

- **Checkpoints**: 不在此服务器，随旧服务器 19912 丢失
- **Result files**: 不在此服务器，同样丢失
- **theta_MLE 值**：在 `theta_fixed_n10_recompute.py` 中有 hardcoded 保留（s4=-1.169, s5=-1.100, s6=-1.141, s7=-1.075）
- **lz* 值**：在 `bca_bootstrap.py` 中有 hardcoded 保留（s4=3.9558, s5=4.4910, s6=5.5030, s7=5.8982）
- 这 4 个 lz* 值无法独立验证

### 6. 结论

| 问题 | 状态 |
|------|------|
| Mistral 是否存在 V0→V1 问题？ | **否**，eval_lz.py 始终是 V1 |
| hardcoded 值与 result 文件一致？ | **是**（6/6 匹配） |
| 需要 re-eval Mistral clean seeds？ | **不需要**（eval 版本正确） |
| s4-s7 可恢复？ | **不可**（checkpoint 和 result 均丢失） |

---
