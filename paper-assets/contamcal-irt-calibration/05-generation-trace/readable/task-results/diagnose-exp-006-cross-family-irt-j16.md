# diagnose exp 006 cross family irt j16

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_006_cross_family_irt_j16_20260517T134702_result.json`
- **Structured JSON:** [`7966104785b047853b05.json`](../../sessions/79/7966104785b047853b05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断报告

### 根因：CmdStan 采样进程被容器安全策略终止 ("Operation not permitted")

### 关键证据

1. **所有 8 个 per-domain IRT fits 成功完成**（20:07 - 21:29，共 82 分钟），结果已保存到 `/root/autodl-tmp/exp006/mmlu_domain_irt_j16_cross_family/*/irt_results.json`

2. **Pooled fit 在 60% sampling 时全部 4 条 chain 同时崩溃**：
   ```
   2026-05-17 21:35:41,983 ERROR Chain [1] error: code '1' Operation not permitted
   2026-05-17 21:35:42,008 ERROR Chain [4] error: code '1' Operation not permitted
   2026-05-17 21:35:42,088 ERROR Chain [3] error: code '1' Operation not permitted
   2026-05-17 21:35:42,147 ERROR Chain [2] error: code '1' Operation not permitted
   ```

3. **Python traceback**：`RuntimeError: Error during sampling` from `cmdstanpy/model.py:1180`，retcodes=[1, 1, 1, 1]

4. **非 OOM**：服务器有 1TB 内存，969GB 可用。也非磁盘满（/tmp 还有 10GB）

5. **4 条 chain 在同一秒同时死亡** → 外部事件（平台级 kill/seccomp），而非 Stan 内部错误

6. 总运行时间 ~88 分钟。SeetaCloud 容器环境（overlay fs），无法读取 dmesg。

### 根因分析
容器运行平台（SeetaCloud）可能对长时间运行的子进程组施加了安全策略限制（seccomp/cgroup timeout）。前 8 个 domain fit 每个 ~6-14 分钟独立运行无问题，但整个脚本累计运行 ~88 分钟后，pooled fit 的 Stan 子进程被平台终止。

### 建议修复

**立即可行**：脚本已支持 `--pooled_only` 参数。8 个 domain 结果已保存在磁盘，重新运行时加此参数即可跳过 domain fits，直接只跑 pooled fit（约 6-10 分钟）：

```bash
source /root/miniconda3/bin/activate && cd /root/contamcal-irt-calibration/exp006 && \
python run_mmlu_domain_gamma_j16_cross_family.py --pooled_only 2>&1 | tee j16_cross_family_pooled.log
```

**长期**：将脚本拆分为独立的 domain + pooled 子任务分别提交，避免单进程累计运行时间过长触发平台限制。

---
