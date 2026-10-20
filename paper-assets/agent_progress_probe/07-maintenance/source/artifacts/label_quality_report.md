# Label Quality Report — Phase 0.5

## 1. 总体一致率

| 指标 | 值 |
|------|-----|
| 抽样总数 | 100 |
| Agree (审核与 LF 一致) | 53 (53.0%) |
| Disagree (审核与 LF 不一致) | 3 (3.0%) |
| Needs Human Review | 44 (44.0%) |
| **有效一致率 (agree / (agree+disagree))** | **94.6%** |

## 2. 分组一致率

| 组别 | 样本数 | Agree | Agree 率 |
|------|--------|-------|----------|
| 高置信度 (conf≥2) | 50 | 33 | 66.0% |
| 冲突/低置信度 | 50 | 20 | 40.0% |

## 3. 各 LF 单独投票时的准确率

| LF 名称 | 单独投票样本数 | Agree | Disagree | Needs Review | Agree/(Agree+Disagree) |
|---------|---------------|-------|----------|-------------|----------------------|

## 4. 典型 Disagree 案例

### Case 1: Azure__azure-functions-python-worker-890__swe-agent-llama-70b window 4
- **LF 标签**: stagnation (conf=2)
- **LF 投票**: {'file_diff_delta': 0, 'test_pass_rate_transition': -1, 'outcome_backpropagation': 0}
- **审核意见**: edit commands present but labeled stagnation
- **特征**: edit=True, repeated_cmd=False, search_only=False
- **窗口摘要**:
  - `[18] ai: The test script failed because the `Dispatcher` initialization requires a valid event loop. We should modify the test script to provide a valid event `
  - `[19] user: [File: /azure-functions-python-worker/test_threadpool.py (24 lines total)] 1:import os 2:import asyncio 3:from azure_functions_worker.dispatcher impor`
  - `[20] ai: The test script has been updated to use a valid event loop. Now, let's run the test script again to verify that the thread pool size can be set to a v`
  - `[21] user: Thread pool size: 64 Test passed  (Open file: /azure-functions-python-worker/test_threadpool.py) (Current directory: /azure-functions-python-worker) b`
  - `[22] ai: The test script ran successfully, and the thread pool size was correctly set to 64. This confirms that our changes worked as expected. Now, let's clea`

### Case 2: asottile__pyupgrade-142__swe-agent-llama-70b window 4
- **LF 标签**: stagnation (conf=2)
- **LF 投票**: {'file_diff_delta': 0, 'test_pass_rate_transition': -1, 'outcome_backpropagation': 0}
- **审核意见**: edit commands present but labeled stagnation
- **特征**: edit=True, repeated_cmd=False, search_only=False
- **窗口摘要**:
  - `[18] ai: I made an error in specifying the file to edit. Let me correct this by ensuring I edit the correct file, `pyupgrade.py`. I'll use the proper Unicode e`
  - `[19] user: Your proposed edit has introduced new syntax error(s). Please read this error message carefully and then retry editing the file.  ERRORS: - E999 Inden`
  - `[20] ai: It seems I have repeatedly attempted to edit the wrong file. I apologize for the confusion. Let me ensure I am editing the correct file, `pyupgrade.py`
  - `[21] user: [File: /pyupgrade/pyupgrade.py (1404 lines total)] 1:from __future__ import absolute_import 2:from __future__ import unicode_literals 3: 4:import argp`
  - `[22] ai: Now that we have the correct file open, let's proceed to edit the file to use the proper Unicode escape sequence in place of '\N'. This will ensure th`

### Case 3: TACC__agavepy-62__swe-agent-llama-70b window 8
- **LF 标签**: progress (conf=1)
- **LF 投票**: {'file_diff_delta': 1, 'test_pass_rate_transition': -1, 'outcome_backpropagation': 0}
- **审核意见**: search/find only but labeled progress
- **特征**: edit=False, repeated_cmd=False, search_only=True
- **窗口摘要**:
  - `[34] ai: It seems that the `switch_tenant` function is not found within the `agavepy` directory. It’s possible that the function is defined in a different modu`
  - `[35] user: Your command ran successfully and did not produce any output. (Open file: /agavepy/agavepy/utils/cachedir_helpers.py) (Current directory: /agavepy) ba`
  - `[36] ai: Since the `switch_tenant` function is not found within the `agavepy` directory or the entire repository, it’s possible that the function is not curren`
  - `[37] user: Your command ran successfully and did not produce any output. (Open file: /agavepy/agavepy/utils/cachedir_helpers.py) (Current directory: /agavepy) ba`
  - `[38] ai: Since the `switch_tenant` function is not found within the `utils` directory either, it’s possible that the function is not implemented in the code ye`

## 5. 典型 Needs Human Review 案例

### Case 1: ppizarror__pygame-menu-357__swe-agent-llama-8b window 12
- **LF 标签**: progress (conf=2)
- **LF 投票**: {'file_diff_delta': 1, 'test_pass_rate_transition': -1, 'outcome_backpropagation': 1}
- **特征**: edit=False, repeated_cmd=False, commands=[]
- **窗口摘要**:

### Case 2: Melevir__cognitive_complexity-15__swe-agent-llama-70b window 7
- **LF 标签**: progress (conf=2)
- **LF 投票**: {'file_diff_delta': 1, 'test_pass_rate_transition': -1, 'outcome_backpropagation': 1}
- **特征**: edit=False, repeated_cmd=False, commands=[]
- **窗口摘要**:

### Case 3: Melevir__cognitive_complexity-15__swe-agent-llama-70b window 17
- **LF 标签**: progress (conf=2)
- **LF 投票**: {'file_diff_delta': 1, 'test_pass_rate_transition': -1, 'outcome_backpropagation': 1}
- **特征**: edit=False, repeated_cmd=False, commands=[]
- **窗口摘要**:

### Case 4: hugovk__pypistats-41__swe-agent-llama-70b window 3
- **LF 标签**: progress (conf=2)
- **LF 投票**: {'file_diff_delta': 1, 'test_pass_rate_transition': -1, 'outcome_backpropagation': 1}
- **特征**: edit=False, repeated_cmd=False, commands=[]
- **窗口摘要**:

### Case 5: bihealth__biomedsheets-23__swe-agent-llama-70b window 13
- **LF 标签**: progress (conf=2)
- **LF 投票**: {'file_diff_delta': 1, 'test_pass_rate_transition': -1, 'outcome_backpropagation': 1}
- **特征**: edit=False, repeated_cmd=False, commands=[]
- **窗口摘要**:

## 6. 结论

**有效一致率 94.6% ≥ 80% 目标，标签质量达标。**

### 分析

- 高置信度窗口一致率 (66.0%) vs 冲突窗口 (40.0%)，差异 26.0pp

### 数据分布参考

| 类别 | 数量 |
|------|------|
| 高置信度 progress | 96 |
| 高置信度 stagnation | 998 |
| 冲突窗口 | 770 |
| 低置信度 (conf=1) | 9182 |
