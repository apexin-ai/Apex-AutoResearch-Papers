# diag exp 006 mmlu domain gamma

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp_006_mmlu_domain_gamma_20260516T084836_result.json`
- **Structured JSON:** [`f3495ccfa5176cd2a88a.json`](../../sessions/f3/f3495ccfa5176cd2a88a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

grep 返回 1 表示没有匹配行——日志中**没有任何 ERROR、FAIL、Traceback 或 Exception**。

## 诊断报告

### 失败原因

**EXIT_CODE=1 不是来自 Python 脚本，而是来自 `tee` 命令。**

日志第一行：
```
tee: /root/autodl-tmp/contamcal-irt-calibration/exp_006_mmlu_domain_gamma.log: No such file or directory
```

启动命令用了管道 `python3 ... 2>&1 | tee &lt;path>`，目标目录 `/root/autodl-tmp/contamcal-irt-calibration/` 不存在。`tee` 无法打开文件，虽然仍然正常将 stdin 传递到 stdout（所以日志被 runs 框架捕获了），但 `tee` 自身以 exit code 1 退出。

Bash 管道默认取最后一个命令的退出码，即 `tee` 的 1，而非 `python3` 的 0。

### 根因

提交任务时 tee 的目标路径写错了——`/root/autodl-tmp/contamcal-irt-calibration/` 目录从未创建过。

### 实验本身的状态

**Python 脚本实际上成功完成了。** 全部 8 个域都已拟合：

| Domain | γ̂ | 95% CI | R̂ | Div |
|---|---|---|---|---|
| Other | 1.34 | [0.675, 2.029] | 1.008 | 0 |
| Business_Law | 0.61 | [0.215, 1.004] | 1.007 | 0 |
| Humanities | 0.47 | [0.202, 0.749] | 1.006 | 0 |
| STEM_Science | 0.36 | [-0.057, 0.814] | 1.008 | 0 |
| STEM_CS_Eng | 0.29 | [-0.496, 1.122] | 1.008 | 0 |
| Social_Sciences | 0.28 | [0.028, 0.524] | 1.007 | 0 |
| Medical | 0.27 | [-0.110, 0.645] | 1.007 | 0 |
| STEM_Math | -0.55 | [-1.266, 0.093] | 1.008 | 0 |

结果文件完整保存在 `/root/autodl-tmp/exp006/results_mmlu_domain_gamma/`。

### 修复建议

无需修复脚本或重跑实验。如果要避免未来同类问题：
1. 提交命令时确保 tee 目标目录存在，或用 `mkdir -p` 预创建
2. 或在 bash 中设置 `set -o pipefail` 时注意管道中每个命令的退出码
3. 可以直接将此实验标记为**成功**（结果完整、收敛良好、无 divergence）

---
