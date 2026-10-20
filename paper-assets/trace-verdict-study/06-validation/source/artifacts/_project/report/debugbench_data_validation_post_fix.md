# DebugBench Exception Bug Fix — 落地验证报告
Date: 2026-05-16

## 1. 修复落地确认

**修复已 apply。** `format_sample()` 函数 (debugbench_format_data.py L148-159) 包含 `test_results.error` fallback 逻辑：
- 当 exception_only/vota 条件下 trace_raw 无 exception 事件时
- 从 `item["test_results"]["error"]` 提取错误信息
- 通过 `_parse_error_string()` (L98-102) 解析为 (type, message)
- 构造合成 exception 事件注入 trace_raw

原始数据: 2048 samples, 625/1006 fail 有空 trace_raw, 625/625 有 test_results.error → fallback 完全覆盖。

## 2. 全部 5 条件数据验证表

数据文件时间戳: 2026-05-16 07:12-07:13 (修复后重新生成)

| Condition | Train | Test | Mean tok | Median | Max | >2048 |
|-----------|-------|------|----------|--------|-----|-------|
| no_trace | 1622 | 426 | 274 | 226 | 1849 | 0/2048 (0.0%) |
| exception_only | 1622 | 426 | 377 | 299 | 1879 | 0/2048 (0.0%) |
| full_trace | 1622 | 426 | 1508 | 2048 | 2048 | 0/2048 (0.0%) |
| vota | 1622 | 426 | 1508 | 2047 | 2048 | 0/2048 (0.0%) |
| ae_only | 1622 | 426 | 754 | 731 | 2048 | 0/2048 (0.0%) |

所有条件 0% 超过 2048 token — label 截断问题已消除。

## 3. exception_only 修复效果

### 测试集
- Total: 426 (pass: 219, fail: 207)
- **Fail with exception signal: 207/207 (100.0%)**
- Pass with exception signal: 0/219 (0.0%)
- Pass with [No exception data in trace]: 219/219 (100.0%)

### 信号完美分离
- 所有 fail 样本都有 [ERROR] 异常信号
- 所有 pass 样本都没有异常信号（显示 "[No exception data in trace]"）
- **理论上限 = 100%**

### 示例 (fallback 生效)
`[ERROR] SyntaxError at line ?: invalid syntax (<solution>, line 14)` — 原 trace_raw 为空的 syntax error 样本，从 test_results.error 正确注入。

## 4. Registry 状态
- debugbench_exception_bug_fix: PENDING → **DONE** (success)
