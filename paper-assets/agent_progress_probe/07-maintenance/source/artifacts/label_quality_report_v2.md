## Phase 0.5 重跑结果

- 5K 数据下载: 5000/5000 条
- 窗口总数: 59,496
- 标签分布: PROGRESS 65.9% / STAGNATION 26.2% / ABSTAIN 7.9%
- 质量检查（100 样本）:
  - 原始一致率: 90/100 = 90% [PASS vs 80%]
  - 高置信度窗口一致率: 42/50 = 84%
  - 冲突窗口一致率: 48/50 = 96%
  - Uncertain 样本数: 46（计入 agree）
- PROGRESS-on-no-edit 排查结论: 缓存问题已解决（修复后 LF1 逻辑：edit=0 不可能返回 PROGRESS）

## 各 LF 单独 agree 率

| LF | Agree | Total | Rate |
|----|-------|-------|------|
| LF1 (file_diff_delta) | 65 | 100 | 65% |
| LF2 (command_repetition) | 70 | 100 | 70% |
| LF3 (outcome_backpropagation) | 63 | 100 | 63% |

## Disagree 案例

### 案例 1: django__asgiref-325__swe-agent-llama-70b  window 5
- **Majority label**: PROGRESS (confidence=2)
- **直觉判断**: STAGNATION
- **LF labels**: LF1=PROGRESS, LF2=PROGRESS, LF3=ABSTAIN
- **窗口摘要**: edits=0, searches=3, repetition=False, commands=[search_dir "def async_to_sync" asgiref; search_dir "def async_to_sync"; ls -F docs]
- **原因**: majority=PROGRESS 但内容显示应为 STAGNATION

### 案例 2: scrapy__w3lib-136__swe-agent-llama-70b  window 13
- **Majority label**: STAGNATION (confidence=2)
- **直觉判断**: PROGRESS
- **LF labels**: LF1=PROGRESS, LF2=STAGNATION, LF3=STAGNATION
- **窗口摘要**: edits=5, searches=0, repetition=True, commands=[edit 502:502
def canonicalize_url(
    url: Union[StrOrBytes; edit 502:502
def canonicalize_url(
    url: Union[StrOrBytes; edit 502:502
def canonicalize_url(
    url: Union[StrOrBytes]
- **原因**: majority=STAGNATION 但内容显示应为 PROGRESS

### 案例 3: iterative__dvc-7966__swe-agent-llama-70b  window 12
- **Majority label**: PROGRESS (confidence=2)
- **直觉判断**: STAGNATION
- **LF labels**: LF1=PROGRESS, LF2=PROGRESS, LF3=STAGNATION
- **窗口摘要**: edits=0, searches=0, repetition=True, commands=[mkdir.git; mkdir.git; mkdir.git]
- **原因**: majority=PROGRESS 但内容显示应为 STAGNATION

### 案例 4: ncclient__ncclient-314__swe-agent-llama-70b  window 7
- **Majority label**: STAGNATION (confidence=2)
- **直觉判断**: PROGRESS
- **LF labels**: LF1=PROGRESS, LF2=STAGNATION, LF3=STAGNATION
- **窗口摘要**: edits=5, searches=0, repetition=True, commands=[edit 92:100
def connect_ssh(*args, **kwds):
    """
    Init; edit 92:100
def connect_ssh(*args, **kwds):
    """
    Init; edit 92:100
def connect_ssh(*args, **kwds):
    """
    Init]
- **原因**: majority=STAGNATION 但内容显示应为 PROGRESS

### 案例 5: pvlib__pvlib-python-907__swe-agent-llama-70b  window 6
- **Majority label**: STAGNATION (confidence=2)
- **直觉判断**: PROGRESS
- **LF labels**: LF1=PROGRESS, LF2=STAGNATION, LF3=STAGNATION
- **窗口摘要**: edits=5, searches=0, repetition=True, commands=[edit 113:139
            data = parse_pvgis_tmy_csv(src)
end; edit 113:113
            data = parse_pvgis_tmy_csv(src)
end; edit 113:139
            data = parse_pvgis_tmy_csv(src)
end]
- **原因**: majority=STAGNATION 但内容显示应为 PROGRESS

