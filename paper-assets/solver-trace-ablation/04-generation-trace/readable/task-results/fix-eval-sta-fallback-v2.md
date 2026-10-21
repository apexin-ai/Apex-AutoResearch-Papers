# fix eval sta fallback v2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval-sta-fallback-v2_20260515T013020_result.json`
- **Structured JSON:** [`8c178daf20d3b9183b35.json`](../../sessions/8c/8c178daf20d3b9183b35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. eval_sta.py 修复

修复前（lines 183-192）：
```python
    # Data path fallback
    data_path = args.data_path
    if not Path(data_path).exists():
        alt = Path(data_path).parent / "test_100.jsonl"
        if alt.exists():
            data_path = str(alt)
            print(f"Fallback data path: {data_path}")
        else:
            print(f"ERROR: {data_path} not found")
            sys.exit(1)
```

修复后：
```python
    data_path = args.data_path
    if not Path(data_path).exists():
        print(f"ERROR: data path {data_path} not found", file=sys.stderr)
        sys.exit(1)
```

验证：
- `grep test_100 scripts/eval_sta.py` → 无结果 ✅
- `ast.parse` → Syntax OK ✅

### 2. Git commit + push：**无法执行**

服务器上 `/root/solver-trace-ablation/` 没有 `.git` 目录，整个 `/root` 下 `find -maxdepth 3 -name .git -type d` 也无结果。该目录不是 git 工作树，无法 commit/push。修复仅在远程服务器文件系统上完成。**如需 sync 回本地 repo，请告知正确路径。**

### 3. classify_h7.py 分类结果（exp1-isr-b03-s44-r2 正确测试集 eval）

文件：`/root/autodl-tmp/outputs/eval_sta_exp1_isr_b03_s44_r2_correct.json`

```
Total: 100, Proved: 95
H7 strict (single premise == conclusion):     95/95 = 100.0%
H1 strict (multi-prem, concl in premises):     0/95 =   0.0%
H7+H1 (conclusion in premises):               95/95 = 100.0%
H7 relaxed (single_premise + ISR>=0.5):       94/95 =  99.0%
Single premise: 95/95 = 100.0%
ISR = 1.0:      0/95 =   0.0%
```

**所有 95 个 proved 样本都是 H7 strict（单 premise 复述 conclusion），ISR=0.75 居多，0 个 ISR=1.0。** 与之前对其他 exp1-isr run 的观察一致——high ISR 来自 Goodhart-style metric gaming（C006），不是真正的多步推理。

---
