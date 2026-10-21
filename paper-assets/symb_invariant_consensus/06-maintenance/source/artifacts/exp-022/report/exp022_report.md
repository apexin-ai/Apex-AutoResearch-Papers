Exp-022: Oracle-SICA on ProofWriter OWA-D5 (600 problems)

Overall:
  Oracle-SICA accuracy: 86.67% (520/600)
  SC accuracy:          75.17% (451/600)
  SICA(self) accuracy:  75.50% (453/600)
  Delta (Oracle vs SC):   +11.50 pp
  Delta (Oracle vs SICA): +11.17 pp
  Z3 gold match rate: 577/594 = 97.14%
  Parse errors: 6/600, Solver errors: 0/7128

Per-subtype breakdown:
  AttNoneg (154): Oracle 96.10% vs SC 87.01% (+9.09pp)
  AttNeg   (160): Oracle 91.88% vs SC 85.00% (+6.87pp)
  RelNoneg (146): Oracle 79.45% vs SC 66.44% (+13.01pp)
  RelNeg   (140): Oracle 77.86% vs SC 60.00% (+17.86pp)

Statistical tests:
  McNemar p (Oracle vs SC):   9.21e-15
  McNemar p (Oracle vs SICA): 2.52e-14
  Bootstrap 95% CI Oracle: [0.8400, 0.8933]
  Bootstrap 95% CI SC:     [0.7167, 0.7850]

Comparison with FOLIO (exp-021):
  FOLIO:       Oracle 88.24% vs SC 79.41% (+8.82pp, p=6.15e-5)
  ProofWriter: Oracle 86.67% vs SC 75.17% (+11.50pp, p=9.21e-15)
  ProofWriter delta is larger (+11.50 vs +8.82pp) with stronger significance

Server files:
  Script: /root/symb_invariant_consensus/scripts/run_exp022_oracle_proofwriter.py
  Results: /root/symb_invariant_consensus/results/exp022_oracle_proofwriter.json
  Log: /root/symb_invariant_consensus/results/exp022_oracle_pw.log