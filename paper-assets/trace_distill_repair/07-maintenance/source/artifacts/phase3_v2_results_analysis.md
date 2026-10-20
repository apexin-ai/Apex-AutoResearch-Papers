# Phase 3 v2 实验结果分析

**日期**: 2026-05-15  
**模型**: deepseek/deepseek-v4-pro  
**API endpoint**: http://47.94.22.126/v1  
**实验状态**: 进程已退出 (PID 130226)，未完成全部实例

---

## 1. 完成状况

| 状态 | 数量 | 实例 |
|------|------|------|
| 完成 | 5/14 | black_1, cookiecutter_1, cookiecutter_2, cookiecutter_3, fastapi_2 |
| 部分完成 | 1/14 | httpie_2 (2/4 conditions: no_trace, full_trace) |
| 未开始 | 8/14 | luigi_5, sanic_2, scrapy_2, scrapy_7, tornado_2, youtube-dl_1, youtube-dl_5, youtube-dl_20 |

进程在 22:31 处理 httpie_2/structural_filtered 的 API 调用时退出，原因不明（可能 SSH 超时或 API 连接中断）。

## 2. 完整结果表 (5 完成实例 × 4 条件)

| instance | condition | test_pass | diff_apply | judge | tokens_in | tokens_out |
|----------|-----------|-----------|------------|-------|-----------|------------|
| black_1 | no_trace | F | Y | 1 | 33314 | 1207 |
| black_1 | full_trace | F | N | 0 | 36003 | 2347 |
| black_1 | structural_filtered | F | N | 0 | 34175 | 4212 |
| black_1 | line_filtered | F | N | 1 | 33546 | 3484 |
| cookiecutter_1 | no_trace | F | N | 1 | 3415 | 4146 |
| cookiecutter_1 | full_trace | F | Y | 0 | 5859 | 3428 |
| cookiecutter_1 | structural_filtered | F | Y | 1 | 3747 | 3044 |
| cookiecutter_1 | line_filtered | F | Y | 1 | 4094 | 2155 |
| cookiecutter_2 | no_trace | F | Y | 1 | 1194 | 977 |
| cookiecutter_2 | full_trace | F | Y | 1 | 3637 | 163 |
| cookiecutter_2 | structural_filtered | F | Y | 0 | 1522 | 5267 |
| cookiecutter_2 | line_filtered | F | Y | 0 | 1772 | 3711 |
| cookiecutter_3 | no_trace | F | N | 0 | 1194 | 2199 |
| cookiecutter_3 | full_trace | F | Y | 1 | 3637 | 163 |
| cookiecutter_3 | structural_filtered | F | N | 0 | 2861 | 4468 |
| cookiecutter_3 | line_filtered | F | N | 1 | 2616 | 6581 |
| fastapi_2 | no_trace | F | Y | 0 | 8903 | 2215 |
| fastapi_2 | full_trace | F | N | 1 | 28654 | 4432 |
| fastapi_2 | structural_filtered | F | Y | 1 | 9126 | 2931 |
| fastapi_2 | line_filtered | F | Y | 0 | 10615 | 4812 |

**httpie_2 部分结果** (从日志提取):

| instance | condition | test_pass | diff_apply | judge |
|----------|-----------|-----------|------------|-------|
| httpie_2 | no_trace | F | N | 0 |
| httpie_2 | full_trace | F | N | 1 |

## 3. 条件汇总统计

| condition | n | test_pass | avg_judge | diff_apply_rate |
|-----------|---|-----------|-----------|-----------------|
| no_trace | 5 | 0/5 (0%) | 0.60 | 3/5 (60%) |
| full_trace | 5 | 0/5 (0%) | 0.60 | 3/5 (60%) |
| structural_filtered | 5 | 0/5 (0%) | 0.40 | 3/5 (60%) |
| line_filtered | 5 | 0/5 (0%) | 0.60 | 3/5 (60%) |

Judge score 范围: 0-1（理论上限 5）。所有条件的平均 judge 分不超过 0.6。

## 4. Head-to-Head 对比

| comparison | win | tie | loss | n |
|------------|-----|-----|------|---|
| structural_filtered vs no_trace | 1 | 2 | 2 | 5 |
| line_filtered vs no_trace | 1 | 3 | 1 | 5 |
| full_trace vs no_trace | 2 | 1 | 2 | 5 |
| structural_filtered vs line_filtered | 1 | 2 | 2 | 5 |

统计检验均不显著（p=1.000），样本太小且无差异。

## 5. Oracle Baseline

Oracle 测试（ground truth patch → test execution）：

| instance | oracle_pass | 说明 |
|----------|-------------|------|
| black_1 | F | test 找不到方法 (AttributeError: test_works_in_mono_process_only_environment) |
| fastapi_1 | N/A | instance not found |
| fastapi_2 | F | test 文件缺少目标测试 (test_router_ws_depends_with_override not found) |
| httpie_2 | **P** | 1 passed |

**Oracle 通过率: 1/4 (25%)**

仅 httpie_2 oracle 通过，但 httpie_2 的 v2 实验未完成（进程在第 3/4 个条件时退出）。

## 6. Kill Criteria C001 检查

> Kill criteria: (1) no_trace judge >= 3.0 (2) structural > no_trace (p<0.15) (3) >=1 条件 test pass > 0%

| 条件 | 要求 | 实际 | 结果 |
|------|------|------|------|
| no_trace avg judge >= 3.0 | >= 3.0 | 0.60 | **FAIL** |
| structural > no_trace (p<0.15) | p < 0.15 | p = 1.000 | **FAIL** |
| >= 1 condition test_pass > 0% | > 0% | 全部 0% | **FAIL** |

### **Overall: MVP FAIL — 三条 kill criteria 全部未通过**

## 7. 关键问题

1. **Judge 分数极低 (0-1/5)**：模型无法产出与 ground truth 语义相近的修复。大多数生成的 patch 完全偏离目标 bug（如 black_1 生成了 regex 编译函数，实际 bug 是 ProcessPoolExecutor 异常处理）。

2. **diff_apply 失败率 40%**：近一半生成的 diff 格式有误（malformed patch），无法应用。

3. **测试全部失败 (0/20)**：即使 diff 成功应用，生成的修复也不能通过测试。

4. **Oracle 自身有问题**：14 个 Tier 1 实例中只验证了 4 个 oracle，其中仅 1 个 (httpie_2) 通过。black_1 和 fastapi_2 的 oracle 测试因 BugsInPy 环境问题失败。

5. **实验未完成 (5/14)**：进程在 ~62 分钟后退出，可能是 API 超时或连接中断。

## 8. 分析脚本完整输出

```
# Phase 3 v2 Analysis

Source: /root/trace_distill_repair/pipeline_output/phase3_v2_checkpoint.json
Instances: 5 | Conditions: 4 | Total rows: 20

## 1. Per-instance Breakdown
| instance | no_trace | full_trace | structural_filtered | line_filtered |
|---|---|---|---|---|
| black_1 | F/1 | F/0 | F/0 | F/1 |
| cookiecutter_1 | F/1 | F/0 | F/1 | F/1 |
| cookiecutter_2 | F/1 | F/1 | F/0 | F/0 |
| cookiecutter_3 | F/0 | F/1 | F/0 | F/1 |
| fastapi_2 | F/0 | F/1 | F/1 | F/0 |

## 2. Condition Summary
| condition | n | test_pass_rate | avg_judge | diff_apply_rate |
|---|---|---|---|---|
| no_trace | 5 | 0/5 (0%) | 0.60 | 3/5 (60%) |
| full_trace | 5 | 0/5 (0%) | 0.60 | 3/5 (60%) |
| structural_filtered | 5 | 0/5 (0%) | 0.40 | 3/5 (60%) |
| line_filtered | 5 | 0/5 (0%) | 0.60 | 3/5 (60%) |

## 3. Head-to-Head
structural_filtered vs no_trace: 1W/2T/2L
line_filtered vs no_trace: 1W/3T/1L
full_trace vs no_trace: 2W/1T/2L
structural_filtered vs line_filtered: 1W/2T/2L

## 6. Kill Criteria (C001)
1. no_trace avg judge = 0.60 >= 3.0 -> FAIL
2. structural > no_trace: p=1.000 -> FAIL
3. >=1 condition test_pass > 0% -> FAIL

Overall: FAIL -- MVP kill criteria not met
```
