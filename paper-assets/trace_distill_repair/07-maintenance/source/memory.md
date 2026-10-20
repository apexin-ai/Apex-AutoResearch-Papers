# trace_distill_repair — Memory

## 经验教训

### 🔴 MVP 核心假设被否定 (2026-05-15)
- **两代模型一致否定**：deepseek-v4-pro (v2) + Claude Sonnet 4 (强模型) 均显示 structural_filtered 不优于 no_trace
- 排序：no_trace ≥ line ≥ structural ≥ full_trace（与假设完全相反）
- trace 信息总体为负面信号——diff_apply 率与 trace 量负相关（no_trace 85.7% vs full_trace 57.1%）
- C001 FAIL（1/3 criteria）：judge 太低 (1.29 << 3.0)、structural 输给 no_trace (0W-3L)
- **不是 pipeline 问题**——pipeline、评估框架、test infra 全部正常工作
- **项目需要 pivot**——等 Director 从 Option A/B/C 中选方向

### 🔴 提交实验前必须确认脚本文件名 (2026-05-15)
- v1 和 v2 共存时，提交命令中必须明确写 v2 脚本名
- **已踩坑**：用 v1 跑了 ~3 实例才发现

### 🔴 API key 加载方式 (2026-05-15)
- **正确**：`source /root/trace_distill_repair/.env && python ...`
- **错误**：`source /root/.bashrc`（non-interactive guard 会 return）

### 🔴 BugsInPy test execution 需要 bugsinpy conda env (2026-05-15)
- 测试在 `conda activate bugsinpy`（Python 3.8）中运行，v2 脚本已正确使用

### 🔴 get_buggy_code() 从 bug_patch.txt diff header 提取 (2026-05-15)
- BugsInPy bug.info 没有 buggy_file 字段，必须从 patch diff header 解析

### 🔴 Repair prompt 必须用 diff 格式输出 (2026-05-15)
- 完整文件输出会被 max_tokens 截断，用 unified diff + patch -p1

### 🔴 API 代理 timeout 设置 (2026-05-15)
- OpenAI client 必须设 httpx.Timeout(connect=30, read=120) + max_retries=3

### 🔴 BugsInPy 测试文件必须来自 fixed commit (2026-05-15)
- Bug fix 常包含新测试方法，buggy commit 没有 → pytest ERROR
- 两轮修复后 oracle 14/14（安装依赖 + 拷贝 fixed commit 测试文件）

### 🔴 LLM 生成 unified diff 的 hunk 行数不可靠 (2026-05-15)
- `recount_diff_hunks()` 后处理可修复，diff_apply ~54% → ~100%

### 🔴 cron exit file 残留导致误触发 (2026-05-15)
- D026：旧运行的 exit file 导致 cron 误判实验完成

### 🔴 youtube-dl_2 是数据集 bug (2026-05-15)
- oracle fail，从 Tier 1 移除

### Structural scoring v3 keep 分布 (2026-05-15)
- 33 实例中 18 个 keep=0（55%），15 个 keep>0

### Tier 1 最终定义 (2026-05-15)
- **14 实例**：black_1, cookiecutter_1/2/3, fastapi_2, httpie_2, luigi_5, sanic_2, scrapy_2/7, tornado_2, youtube-dl_1/5/20

## 决策记录

### D031: 强模型消歧实验 (2026-05-15)
- Claude Sonnet 4 重跑 14 实例 × 4 条件
- C001 FAIL：structural 0W-3L vs no_trace，judge 1.29 << 3.0
- 确认 trace 方向无望，需 pivot

### D020: 修复 repair pipeline confounds (2026-05-15)
- Diff-based prompt + target file 修正 + max_tokens=16000

### D018: 两阶段消歧 (2026-05-15)
- Option B（强模型）已执行完毕，结果 negative
- Option A（fault localization）仍可作为 pivot 方向
