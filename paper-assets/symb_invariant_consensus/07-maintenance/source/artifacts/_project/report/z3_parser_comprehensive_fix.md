## Z3 Parser 全面修复报告

### Parse 成功率对比

| 问题 | 修复前 | 修复后 | 变化 |
|------|--------|--------|------|
| P1 | 100% (8/8) | 100% (8/8) | — |
| P3 | 60% (6/10) | **100%** (10/10) | +40% |
| P4 | 62% (8/13) | **100%** (13/13) | +38% |
| P5 | 100% (5/5) | 100% (5/5) | — |
| P6 | 71% (12/17) | 71% (12/17) | — |
| P7 | 36% (16/45) | **96%** (43/45) | +60% |
| **总计** | **56.1%** | **92.9%** | **+36.8%** |

### P7 Failure Patterns

| Pattern | 频次(估) | 修复状态 |
|---------|---------|---------|
| chained_cmp (`0 <= d1 <= 9`) | ~15/72 | ✅ |
| python_logic (`d1 >= 0 and d1 <= 9`) | ~15/72 | ✅ |
| modulo (`N % 7 == 0`) | ~20/72 | ✅ |
| int_div (`Q == N // 7`) | ~5/72 | ✅ |
| nl_prefix (`We need N % 7 == 0`) | ~5/72 | ✅ |
| latex/divmod | ~2/72 | ❌ Z3无法表示 |

### 代码改动
文件：`sica/z3_maxsat.py`

新增4个函数：
- `_strip_nl_prefix()` — NL前缀去除
- `_needs_int_vars()` — 自动检测整数上下文切换z3.Int
- `_ast_rewrite()` — 链式比较→And()、Python逻辑→Z3逻辑、逗号→And()
- `_try_eval()` — 核心eval抽取，支持is_bool参数

增强命名空间：floor/ceil/log/log2/gcd作为Z3 uninterpreted functions

### 未修复（需extraction prompt改进）
- 集合/列表字面量 (`A == [11,10,9...]`)
- `in` 算子 (`a1 in range(1,20)`)
- `len()` (`len(A) == 7`)
- `divmod()` tuple比较
- 纯LaTeX (`N \equiv 0 \pmod{7}`)