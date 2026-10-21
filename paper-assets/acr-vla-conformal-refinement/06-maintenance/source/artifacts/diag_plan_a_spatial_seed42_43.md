# Plan A Spatial seed42/43 诊断报告

**日期**: 2026-05-21  
**服务器**: bjb1-32546  
**结论**: **监控误报，实验实际已成功完成**

## 失败根因

**不是真正的失败。** failure_reason "process dead 5× with no sentinel/W&B — auto-resolved as failed" 是监控系统的误判。监控无法检测到进程存活标记或 W&B 心跳，但实验本身正常运行并输出了完整结果。

## 证据

### 三个 seed 全部正常完成

| seed | 成功率 | JSON 输出文件 | 文件时间 |
|------|--------|--------------|----------|
| 42 | 34.0% (34/100) | `logs/eval_plan_a_spatial_seed42.json` (1897B) | May 21 07:49 |
| 43 | 35.0% (35/100) | `logs/eval_plan_a_spatial_seed43.json` (1896B) | May 21 07:50 |
| 44 | 36.0% (36/100) | `logs/eval_plan_a_spatial_seed44.json` (1897B) | May 21 07:47 |

### 日志确认

- seed42 日志末尾: `Overall success rate (adaptive_conformal_crm): 34.0% (34/100)` → `Results saved to logs/eval_plan_a_spatial_seed42.json`
- seed43 日志末尾: `Overall success rate (adaptive_conformal_crm): 35.0% (35/100)` → `Results saved to logs/eval_plan_a_spatial_seed43.json`
- 两份日志均无 error/exception/traceback/OOM/killed 等异常关键词
- 唯一非标准输出: `DeprecationWarning: builtin type swigvarlink has no __module__ attribute`（无害）

### Conformal CRM 统计一致性

| seed | mean_unc | trigger_rate | total_steps | crm_applied |
|------|----------|-------------|-------------|-------------|
| 42 | 0.2679 | 97.6% | 23207 | 22651 |
| 43 | 0.2619 | 98.0% | 23037 | 22566 |
| 44 | 0.2661 | 97.8% | 22909 | 22416 |

三个 seed 的统计指标高度一致，确认实验行为正常。

## seed42/43 vs seed44 差异分析

**无差异。** 三个 seed 的成功率在 34-36% 窄范围内，per-task 分布也一致（同样的 task 成功/失败模式）。seed44 被标记为成功仅因为监控恰好检测到了它，不是因为它的实验结果有本质区别。

## 是否需要重试

**不需要。** 结果文件完整有效，可直接使用。需要做的是：
1. 将 seed42/43 的状态从 "failed" 更正为 "completed"
2. 排查监控系统为何对这两个进程产生误判（可能是进程名匹配、W&B 未配置、或检测时序问题）
