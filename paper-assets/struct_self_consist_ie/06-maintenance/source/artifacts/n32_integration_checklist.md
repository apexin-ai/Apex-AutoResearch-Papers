# N=32 Integration Checklist

## Pre-flight ✅
- [x] analyze_n32.py: MV bug 修复 (strict `(start, end, type)` match), 服务器已部署
- [x] N=8 验证: MV Δ=+4.0pp (参考值 +3.9pp) ✓
- [x] 模板: 3 scenarios (A/B/C) 已准备
- [x] 输出路径: `/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_pretrained_n32_seed42/samples.jsonl`

## Step 1: 运行分析脚本
```bash
cd /root/autodl-tmp/struct_self_consist_ie/code
python analyze_n32.py --input /root/autodl-tmp/struct_self_consist_ie/output/fewnerd_pretrained_n32_seed42/samples.jsonl --compute_sj
```

## Step 2: 确定 Scenario
- A (plateau): MV Δ ∈ [3.0, 5.0) pp
- B (growth): MV Δ ≥ 5.0 pp
- C (decline): MV Δ < 3.0 pp

## Step 3: Table tab:pretrained_summary 插入 N=32 行
文件: `docs/paper/sections/appendix.tex`
插入位置: line 1654 之后（`Pretrained ($N{=}16$)` 行之后）

```latex
         & Pretrained ($N{=}32$) & .XXX & $+$X.X & X.X & XX\% & .XXX \\
```

## Step 4: Appendix 文本更新
文件: `docs/paper/sections/appendix.tex`
插入位置: line 1667 之后（N=16 段落末尾）

Scenario A:
```latex
$N{=}32$ confirms the plateau (MV $\Delta{=}+X.X$\,pp), with capture rate declining further to $XX$\%.
```

Scenario B/C: 见 `artifacts/n32_integration_templates.md`

## Step 5: Discussion 更新
文件: `docs/paper/sections/discussion.tex`
当前 line 6 已有: "MV gains plateau while oracle headroom expands"

- Scenario A: 不改
- Scenario B/C: 按模板替换

## Step 6: 编译验证
- Main text ≤ 8 pages
- 0 undefined refs
- N=32 数据在表格中正确显示

## Reference Values
| N | Greedy | MV Δ (pp) | Degen % | Oracle Δ (pp) | Capture % | ρ_SJ |
|---|--------|-----------|---------|---------------|-----------|------|
| 8 | .538 | +3.9±0.2 | 11.7 | +11.2 | 36% | .436 |
| 16 | .537 | +4.1 | 7.6 | +14.1 | 29% | .453 |
| 32 | .XXX | +X.X | X.X | +X.X | XX% | .XXX |
