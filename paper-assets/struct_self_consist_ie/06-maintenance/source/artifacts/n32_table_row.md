# N=32 Table 4 Row (fill after analysis)

## Table row (LaTeX):
```latex
         & Pretrained ($N{=}32$) & .XXX & $+$X.X & X.X & XX\% & .XXX \\
```

## N=8 vs N=16 vs N=32 comparison:
| N | Greedy | MV Δ (pp) | Degen % | Oracle Δ (pp) | Capture % | ρ_SJ |
|---|--------|-----------|---------|---------------|-----------|------|
| 8 | .538 | +3.9±0.2 | 11.7 | +11.2 | 36% | .436 |
| 16 | .537 | +4.1 | 7.6 | +14.1 | 29% | .453 |
| 32 | .XXX | +X.X | X.X | +X.X | XX% | .XXX |

## Scenario determination:
- A (plateau): MV Δ ~3.5-4.5pp → no Discussion change
- B (growth): MV Δ >5pp → update Discussion
- C (decline): MV Δ <3pp → update Discussion

## Run command:
```bash
cd /root/autodl-tmp/struct_self_consist_ie/code
python analyze_n32.py --input /root/autodl-tmp/struct_self_consist_ie/output/fewnerd_pretrained_n32_seed42/samples.jsonl
```
