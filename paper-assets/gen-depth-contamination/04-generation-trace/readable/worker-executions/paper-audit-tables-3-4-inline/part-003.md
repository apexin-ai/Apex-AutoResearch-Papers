# paper audit tables 3 4 inline — Part 3 of 3

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

[← Part 2](part-002.md) · [Transcript overview](../paper-audit-tables-3-4-inline.md) · [Structured JSON](../../../sessions/28/285101c88d431c3fe347.json)

## Round 5

### Tool call

_source line 639_

<details open><summary>🔧 Tool call — Bash · `toolu_01UEkRj2mGmL88HJwyVSMLTT`</summary>

```json
{
  "command": "python3 -c \"\n# Final comprehensive output\n\nprint('='*100)\nprint('COMPLETE CROSS-REFERENCE: PAPER vs REGISTRY')\nprint('='*100)\n\nprint()\nprint('--- TABLE 1 (tab:kstar_ci): 5 main models ---')\nprint()\nprint(f'{'Location':<28} {'Paper Value':<14} {'Registry exp_id':<40} {'Registry Value':<18} {'Match?'}')\nprint('-'*100)\n\nrows_t1 = [\n    # Qwen-rw\n    ('Tab1 Qwen-rw 0v1 AUC',    '.9956',             'exp_007_bootstrap_ci[qwen_rewrite]', '0.9956', 'MATCH'),\n    ('Tab1 Qwen-rw 1v2 AUC',    '.6955',             'exp_007_bootstrap_ci[qwen_rewrite]', '0.6955', 'MATCH'),\n    ('Tab1 Qwen-rw 1v2 CI',     '[.686,.704]',       'exp_007_bootstrap_ci[qwen_rewrite]', '[.6859,.7041]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-rw 2v3 AUC',    '.5893',             'exp_007_bootstrap_ci[qwen_rewrite]', '0.5893', 'MATCH'),\n    ('Tab1 Qwen-rw 2v3 CI',     '[.580,.599]',       'exp_007_bootstrap_ci[qwen_rewrite]', '[.5795,.5991]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-rw 3v4 AUC',    '.5435',             'exp_007_bootstrap_ci[qwen_rewrite]', '0.5435', 'MATCH'),\n    ('Tab1 Qwen-rw 4v5 AUC',    '.5340',             'exp_007_bootstrap_ci[qwen_rewrite]', '0.5340', 'MATCH'),\n    # Pythia\n    ('Tab1 Pythia 0v1 AUC',     '.9722',             'exp_001_pythia_depth',               '0.9722', 'MATCH'),\n    ('Tab1 Pythia 1v2 AUC',     '.6074',             'exp_001_pythia_depth',               '0.6074', 'MATCH'),\n    ('Tab1 Pythia 1v2 CI',      '[.598,.617]',       'exp_001_pythia_depth[bootstrap_ci]', '[.5975,.6172]', 'MATCH (rounding)'),\n    ('Tab1 Pythia 2v3 AUC',     '.5440',             'exp_001_pythia_depth',               '0.5440', 'MATCH'),\n    ('Tab1 Pythia 2v3 CI',      '[.534,.554]',       '(no registry record)',               'N/A', 'NOT IN REGISTRY'),\n    ('Tab1 Pythia 3v4 AUC',     '.5051',             'exp_001_pythia_depth',               '0.5051', 'MATCH'),\n    ('Tab1 Pythia 4v5 AUC',     '.5079',             'exp_001_pythia_depth',               '0.5079', 'MATCH'),\n    # OLMo\n    ('Tab1 OLMo 0v1 AUC',       '.9860',             'exp_002_olmo_depth',                 '0.9861', 'MATCH (rounding)'),\n    ('Tab1 OLMo 1v2 AUC',       '.5001',             'exp_002_olmo_depth',                 '0.5001', 'MATCH'),\n    ('Tab1 OLMo 1v2 CI',        '[.496,.519]',       '(no registry record)',               'N/A', 'NOT IN REGISTRY'),\n    ('Tab1 OLMo 2v3 AUC',       '.4973',             'exp_002_olmo_depth',                 '0.4972', 'MATCH (rounding)'),\n    ('Tab1 OLMo 2v3 CI',        '[.486,.509]',       '(no registry record)',               'N/A', 'NOT IN REGISTRY'),\n    ('Tab1 OLMo 3v4 AUC',       '.5024',             'exp_002_olmo_depth',                 '0.5034', 'MISMATCH (+0.001)'),\n    ('Tab1 OLMo 4v5 AUC',       '.4942',             'exp_002_olmo_depth',                 '0.4971', 'MISMATCH (+0.003)'),\n    # Qwen-cont\n    ('Tab1 Qwen-cont 0v1 AUC',  '.9971',             'exp_007_bootstrap_ci[qwen_cont]',    '0.9971', 'MATCH'),\n    ('Tab1 Qwen-cont 1v2 AUC',  '.6112',             'exp_007_bootstrap_ci[qwen_cont]',    '0.6112', 'MATCH'),\n    ('Tab1 Qwen-cont 1v2 CI',   '[.602,.621]',       'exp_007_bootstrap_ci[qwen_cont]',    '[.6015,.6213]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-cont 2v3 AUC',  '.5609',             'exp_007_bootstrap_ci[qwen_cont]',    '0.5609', 'MATCH'),\n    ('Tab1 Qwen-cont 2v3 CI',   '[.551,.571]',       'exp_007_bootstrap_ci[qwen_cont]',    '[.5511,.5712]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-cont 3v4 AUC',  '.5409',             'exp_007_bootstrap_ci[qwen_cont]',    '0.5409', 'MATCH'),\n    ('Tab1 Qwen-cont 4v5 AUC',  '.5141',             'exp_007_bootstrap_ci[qwen_cont]',    '0.5141', 'MATCH'),\n    # Qwen-7B\n    ('Tab1 Qwen-7B 0v1 AUC',    '.9638',             'exp_004_7b_crossscale[bootstrap_ci]','0.9638', 'MATCH'),\n    ('Tab1 Qwen-7B 0v1 CI',     '[.961,.967]',       'exp_004_7b_crossscale[bootstrap_ci]','[.9607,.9665]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-7B 1v2 AUC',    '.6168',             'exp_004_7b_crossscale[bootstrap_ci]','0.6168', 'MATCH'),\n    ('Tab1 Qwen-7B 1v2 CI',     '[.608,.626]',       'exp_004_7b_crossscale[bootstrap_ci]','[.6079,.6261]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-7B 2v3 AUC',    '.5492',             'exp_004_7b_crossscale[bootstrap_ci]','0.5492', 'MATCH'),\n    ('Tab1 Qwen-7B 2v3 CI',     '[.539,.559]',       'exp_004_7b_crossscale[bootstrap_ci]','[.5388,.5594]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-7B 3v4 AUC',    '.5276',             'exp_004_7b_crossscale[bootstrap_ci]','0.5276', 'MATCH'),\n    ('Tab1 Qwen-7B 4v5 AUC',    '.5085',             'exp_004_7b_crossscale[bootstrap_ci]','0.5085', 'MATCH'),\n]\n\nfor loc, pv, rid, rv, match in rows_t1:\n    flag = '' if 'MATCH' in match and 'NOT' not in match and 'MIS' not in match else ' ***'\n    print(f'{loc:<28} {pv:<14} {rid:<40} {rv:<18} {match}{flag}')\n\nprint()\nprint('--- EXTENDED TABLE (tab:kstar_ci_extended): 5 additional models ---')\nprint()\nprint(f'{'Location':<30} {'Paper Value':<14} {'Registry exp_id':<38} {'Registry Value':<18} {'Match?'}')\nprint('-'*100)\n\nrows_ext = [\n    # Qwen-base\n    ('Ext Qwen-base 0v1 AUC',    '.987',   'exp_016_base_vs_instruct',  '0.9870', 'MATCH'),\n    ('Ext Qwen-base 0v1 CI',     '[.985,.989]', 'exp_016[bootstrap_ci]','[.9853,.9885]', 'MATCH (rounding)'),\n    ('Ext Qwen-base 1v2 AUC',    '.626',   'exp_016_base_vs_instruct',  '0.6260', 'MATCH'),\n    ('Ext Qwen-base 1v2 CI',     '[.617,.635]', 'exp_016[bootstrap_ci]','[.6168,.6353]', 'MATCH (rounding)'),\n    ('Ext Qwen-base 2v3 AUC',    '.550',   'exp_016_base_vs_instruct',  '0.5496', 'MATCH (rounding)'),\n    ('Ext Qwen-base 2v3 CI',     '[.540,.560]', 'exp_016[bootstrap_ci]','[.5397,.5600]', 'MATCH (rounding)'),\n    ('Ext Qwen-base 3v4 AUC',    '.529',   'exp_016_base_vs_instruct',  '0.5293', 'MATCH (rounding)'),\n    ('Ext Qwen-base 3v4 CI',     '[.519,.540]', 'exp_016[bootstrap_ci]','[.5188,.5399]', 'MATCH (rounding)'),\n    ('Ext Qwen-base 4v5 AUC',    '.518',   'exp_016_base_vs_instruct',  '0.5181', 'MATCH (rounding)'),\n    ('Ext Qwen-base 4v5 CI',     '[.508,.529]', 'exp_016[bootstrap_ci]','[.5075,.5288]', 'MATCH (rounding)'),\n    # LLaMA-8B\n    ('Ext LLaMA-8B 0v1 AUC',    '.9224',  'exp_018_llama8b_depth',     '0.9224', 'MATCH'),\n    ('Ext LLaMA-8B 0v1 CI',     '[.917,.927]', 'exp_018[bootstrap_ci]','[.9174,.9272]', 'MATCH (rounding)'),\n    ('Ext LLaMA-8B 1v2 AUC',    '.6123',  'exp_018_llama8b_depth',     '0.6123', 'MATCH'),\n    ('Ext LLaMA-8B 1v2 CI',     '[.603,.622]', 'exp_018[bootstrap_ci]','[.6028,.6216]', 'MATCH (rounding)'),\n    ('Ext LLaMA-8B 2v3 AUC',    '.5273',  'exp_018_llama8b_depth',     '0.5273', 'MATCH'),\n    ('Ext LLaMA-8B 2v3 CI',     '[.517,.538]', 'exp_018[bootstrap_ci]','[.5169,.5378]', 'MATCH (rounding)'),\n    ('Ext LLaMA-8B 3v4 AUC',    '.5168',  'exp_018_llama8b_depth',     '0.5168', 'MATCH'),\n    ('Ext LLaMA-8B 3v4 CI',     '[.506,.528]', 'exp_018[bootstrap_ci]','[.5062,.5275]', 'MATCH (rounding)'),\n    ('Ext LLaMA-8B 4v5 AUC',    '.5159',  'exp_018_llama8b_depth',     '0.5159', 'MATCH'),\n    ('Ext LLaMA-8B 4v5 CI',     '[.505,.527]', 'exp_018[bootstrap_ci]','[.5052,.5268]', 'MATCH (rounding)'),\n    # Mistral-7B\n    ('Ext Mistral-7B 0v1 AUC',  '.9170',  'exp_019_mistral7b_depth',   '0.9843', 'MISMATCH (self-scorer)'),\n    ('Ext Mistral-7B 0v1 AUC',  '.9170',  'exp_019b_mistral_cross',     '0.9209', 'MISMATCH (cross-scorer)'),\n    ('Ext Mistral-7B 1v2 AUC',  '.5750',  'exp_019_mistral7b_depth',   '0.5935', 'MISMATCH (self-scorer)'),\n    ('Ext Mistral-7B 1v2 AUC',  '.5750',  'exp_019b_mistral_cross',     '0.5695', 'MISMATCH (cross-scorer)'),\n    ('Ext Mistral-7B 2v3 AUC',  '.5369',  'exp_019_mistral7b_depth',   '0.5402', 'MISMATCH (self=.5402)'),\n    ('Ext Mistral-7B 2v3 AUC',  '.5369',  'exp_019b_mistral_cross',     '0.5335', 'MISMATCH (cross=.5335)'),\n    ('Ext Mistral-7B 3v4 AUC',  '.5174',  'exp_019_mistral7b_depth',   '0.5232', 'MISMATCH (self=.5232)'),\n    ('Ext Mistral-7B 3v4 AUC',  '.5174',  'exp_019b_mistral_cross',     '0.5140', 'MISMATCH (cross=.5140)'),\n    ('Ext Mistral-7B 4v5 AUC',  '.5175',  'exp_019_mistral7b_depth',   '0.5181', 'MATCH (~rounding)'),\n    ('Ext Mistral-7B 4v5 AUC',  '.5175',  'exp_019b_mistral_cross',     '0.5184', 'MATCH (~rounding)'),\n    # Pythia-6.9B\n    ('Ext Pythia-6.9B 0v1 AUC', '.9599',  'exp_pythia69b_c4_nuc',      '0.9599', 'MATCH'),\n    ('Ext Pythia-6.9B 1v2 AUC', '.5955',  'exp_pythia69b_c4_nuc',      '0.5955', 'MATCH'),\n    ('Ext Pythia-6.9B 2v3 AUC', '.5298',  'exp_pythia69b_c4_nuc',      '0.5298', 'MATCH'),\n    ('Ext Pythia-6.9B 3v4 AUC', '.5135',  'exp_pythia69b_c4_nuc',      '0.5135', 'MATCH'),\n    ('Ext Pythia-6.9B 4v5 AUC', '---',    'exp_pythia69b_c4_nuc',      'not measured', 'CONSISTENT'),\n    # Gemma-2B\n    ('Ext Gemma-2B 0v1 AUC',    '.953',   'exp_gemma2b_depth',         '0.9534', 'MATCH (rounding)'),\n    ('Ext Gemma-2B 0v1 CI',     '[.949,.957]', '(no registry record)',  'N/A', 'NOT IN REGISTRY'),\n    ('Ext Gemma-2B 1v2 AUC',    '.5981',  'exp_gemma2b_depth',         '0.5981', 'MATCH'),\n    ('Ext Gemma-2B 1v2 CI',     '[.588,.608]', 'exp_gemma2b_depth[bci]','[.5882,.6076]', 'MATCH (rounding)'),\n    ('Ext Gemma-2B 2v3 AUC',    '.534',   'exp_gemma2b_depth',         '0.5342', 'MATCH (rounding)'),\n    ('Ext Gemma-2B 2v3 CI',     '[.523,.545]', '(no registry record)',  'N/A', 'NOT IN REGISTRY'),\n    ('Ext Gemma-2B 3v4 AUC',    '.5033',  'exp_gemma2b_depth',         '0.5030', 'MATCH (rounding)'),\n    ('Ext Gemma-2B 3v4 CI',     '[.492,.514]', '(no registry record)',  'N/A', 'NOT IN REGISTRY'),\n    ('Ext Gemma-2B 4v5 AUC',    '.5025',  'exp_gemma2b_depth',         '0.5026', 'MATCH (rounding)'),\n    ('Ext Gemma-2B 4v5 CI',     '[.492,.514]', '(no registry record)',  'N/A', 'NOT IN REGISTRY'),\n]\n\nfor loc, pv, rid, rv, match in rows_ext:\n    flag = ' ***' if ('MISMATCH' in match or 'NOT IN REGISTRY' in match) else ''\n    print(f'{loc:<30} {pv:<14} {rid:<38} {rv:<18} {match}{flag}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Tys8zmeAdca2dUXMfUjbtC",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "c6f41bf3-5634-4da0-b41f-95147e295036",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SBiVBRfikweaKkuymvbJQU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1254,
      "cache_read_input_tokens": 80386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1254,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 640 · 2026-05-23T11:32:53.798Z_

<details><summary>↩ Tool result · `toolu_01UEkRj2mGmL88HJwyVSMLTT`</summary>

```text
====================================================================================================
COMPLETE CROSS-REFERENCE: PAPER vs REGISTRY
====================================================================================================

--- TABLE 1 (tab:kstar_ci): 5 main models ---

Location                     Paper Value    Registry exp_id                          Registry Value     Match?
----------------------------------------------------------------------------------------------------
Tab1 Qwen-rw 0v1 AUC         .9956          exp_007_bootstrap_ci[qwen_rewrite]       0.9956             MATCH
Tab1 Qwen-rw 1v2 AUC         .6955          exp_007_bootstrap_ci[qwen_rewrite]       0.6955             MATCH
Tab1 Qwen-rw 1v2 CI          [.686,.704]    exp_007_bootstrap_ci[qwen_rewrite]       [.6859,.7041]      MATCH (rounding)
Tab1 Qwen-rw 2v3 AUC         .5893          exp_007_bootstrap_ci[qwen_rewrite]       0.5893             MATCH
Tab1 Qwen-rw 2v3 CI          [.580,.599]    exp_007_bootstrap_ci[qwen_rewrite]       [.5795,.5991]      MATCH (rounding)
Tab1 Qwen-rw 3v4 AUC         .5435          exp_007_bootstrap_ci[qwen_rewrite]       0.5435             MATCH
Tab1 Qwen-rw 4v5 AUC         .5340          exp_007_bootstrap_ci[qwen_rewrite]       0.5340             MATCH
Tab1 Pythia 0v1 AUC          .9722          exp_001_pythia_depth                     0.9722             MATCH
Tab1 Pythia 1v2 AUC          .6074          exp_001_pythia_depth                     0.6074             MATCH
Tab1 Pythia 1v2 CI           [.598,.617]    exp_001_pythia_depth[bootstrap_ci]       [.5975,.6172]      MATCH (rounding)
Tab1 Pythia 2v3 AUC          .5440          exp_001_pythia_depth                     0.5440             MATCH
Tab1 Pythia 2v3 CI           [.534,.554]    (no registry record)                     N/A                NOT IN REGISTRY ***
Tab1 Pythia 3v4 AUC          .5051          exp_001_pythia_depth                     0.5051             MATCH
Tab1 Pythia 4v5 AUC          .5079          exp_001_pythia_depth                     0.5079             MATCH
Tab1 OLMo 0v1 AUC            .9860          exp_002_olmo_depth                       0.9861             MATCH (rounding)
Tab1 OLMo 1v2 AUC            .5001          exp_002_olmo_depth                       0.5001             MATCH
Tab1 OLMo 1v2 CI             [.496,.519]    (no registry record)                     N/A                NOT IN REGISTRY ***
Tab1 OLMo 2v3 AUC            .4973          exp_002_olmo_depth                       0.4972             MATCH (rounding)
Tab1 OLMo 2v3 CI             [.486,.509]    (no registry record)                     N/A                NOT IN REGISTRY ***
Tab1 OLMo 3v4 AUC            .5024          exp_002_olmo_depth                       0.5034             MISMATCH (+0.001) ***
Tab1 OLMo 4v5 AUC            .4942          exp_002_olmo_depth                       0.4971             MISMATCH (+0.003) ***
Tab1 Qwen-cont 0v1 AUC       .9971          exp_007_bootstrap_ci[qwen_cont]          0.9971             MATCH
Tab1 Qwen-cont 1v2 AUC       .6112          exp_007_bootstrap_ci[qwen_cont]          0.6112             MATCH
Tab1 Qwen-cont 1v2 CI        [.602,.621]    exp_007_bootstrap_ci[qwen_cont]          [.6015,.6213]      MATCH (rounding)
Tab1 Qwen-cont 2v3 AUC       .5609          exp_007_bootstrap_ci[qwen_cont]          0.5609             MATCH
Tab1 Qwen-cont 2v3 CI        [.551,.571]    exp_007_bootstrap_ci[qwen_cont]          [.5511,.5712]      MATCH (rounding)
Tab1 Qwen-cont 3v4 AUC       .5409          exp_007_bootstrap_ci[qwen_cont]          0.5409             MATCH
Tab1 Qwen-cont 4v5 AUC       .5141          exp_007_bootstrap_ci[qwen_cont]          0.5141             MATCH
Tab1 Qwen-7B 0v1 AUC         .9638          exp_004_7b_crossscale[bootstrap_ci]      0.9638             MATCH
Tab1 Qwen-7B 0v1 CI          [.961,.967]    exp_004_7b_crossscale[bootstrap_ci]      [.9607,.9665]      MATCH (rounding)
Tab1 Qwen-7B 1v2 AUC         .6168          exp_004_7b_crossscale[bootstrap_ci]      0.6168             MATCH
Tab1 Qwen-7B 1v2 CI          [.608,.626]    exp_004_7b_crossscale[bootstrap_ci]      [.6079,.6261]      MATCH (rounding)
Tab1 Qwen-7B 2v3 AUC         .5492          exp_004_7b_crossscale[bootstrap_ci]      0.5492             MATCH
Tab1 Qwen-7B 2v3 CI          [.539,.559]    exp_004_7b_crossscale[bootstrap_ci]      [.5388,.5594]      MATCH (rounding)
Tab1 Qwen-7B 3v4 AUC         .5276          exp_004_7b_crossscale[bootstrap_ci]      0.5276             MATCH
Tab1 Qwen-7B 4v5 AUC         .5085          exp_004_7b_crossscale[bootstrap_ci]      0.5085             MATCH

--- EXTENDED TABLE (tab:kstar_ci_extended): 5 additional models ---

Location                       Paper Value    Registry exp_id                        Registry Value     Match?
----------------------------------------------------------------------------------------------------
Ext Qwen-base 0v1 AUC          .987           exp_016_base_vs_instruct               0.9870             MATCH
Ext Qwen-base 0v1 CI           [.985,.989]    exp_016[bootstrap_ci]                  [.9853,.9885]      MATCH (rounding)
Ext Qwen-base 1v2 AUC          .626           exp_016_base_vs_instruct               0.6260             MATCH
Ext Qwen-base 1v2 CI           [.617,.635]    exp_016[bootstrap_ci]                  [.6168,.6353]      MATCH (rounding)
Ext Qwen-base 2v3 AUC          .550           exp_016_base_vs_instruct               0.5496             MATCH (rounding)
Ext Qwen-base 2v3 CI           [.540,.560]    exp_016[bootstrap_ci]                  [.5397,.5600]      MATCH (rounding)
Ext Qwen-base 3v4 AUC          .529           exp_016_base_vs_instruct               0.5293             MATCH (rounding)
Ext Qwen-base 3v4 CI           [.519,.540]    exp_016[bootstrap_ci]                  [.5188,.5399]      MATCH (rounding)
Ext Qwen-base 4v5 AUC          .518           exp_016_base_vs_instruct               0.5181             MATCH (rounding)
Ext Qwen-base 4v5 CI           [.508,.529]    exp_016[bootstrap_ci]                  [.5075,.5288]      MATCH (rounding)
Ext LLaMA-8B 0v1 AUC           .9224          exp_018_llama8b_depth                  0.9224             MATCH
Ext LLaMA-8B 0v1 CI            [.917,.927]    exp_018[bootstrap_ci]                  [.9174,.9272]      MATCH (rounding)
Ext LLaMA-8B 1v2 AUC           .6123          exp_018_llama8b_depth                  0.6123             MATCH
Ext LLaMA-8B 1v2 CI            [.603,.622]    exp_018[bootstrap_ci]                  [.6028,.6216]      MATCH (rounding)
Ext LLaMA-8B 2v3 AUC           .5273          exp_018_llama8b_depth                  0.5273             MATCH
Ext LLaMA-8B 2v3 CI            [.517,.538]    exp_018[bootstrap_ci]                  [.5169,.5378]      MATCH (rounding)
Ext LLaMA-8B 3v4 AUC           .5168          exp_018_llama8b_depth                  0.5168             MATCH
Ext LLaMA-8B 3v4 CI            [.506,.528]    exp_018[bootstrap_ci]                  [.5062,.5275]      MATCH (rounding)
Ext LLaMA-8B 4v5 AUC           .5159          exp_018_llama8b_depth                  0.5159             MATCH
Ext LLaMA-8B 4v5 CI            [.505,.527]    exp_018[bootstrap_ci]                  [.5052,.5268]      MATCH (rounding)
Ext Mistral-7B 0v1 AUC         .9170          exp_019_mistral7b_depth                0.9843             MISMATCH (self-scorer) ***
Ext Mistral-7B 0v1 AUC         .9170          exp_019b_mistral_cross                 0.9209             MISMATCH (cross-scorer) ***
Ext Mistral-7B 1v2 AUC         .5750          exp_019_mistral7b_depth                0.5935             MISMATCH (self-scorer) ***
Ext Mistral-7B 1v2 AUC         .5750          exp_019b_mistral_cross                 0.5695             MISMATCH (cross-scorer) ***
Ext Mistral-7B 2v3 AUC         .5369          exp_019_mistral7b_depth                0.5402             MISMATCH (self=.5402) ***
Ext Mistral-7B 2v3 AUC         .5369          exp_019b_mistral_cross                 0.5335             MISMATCH (cross=.5335) ***
Ext Mistral-7B 3v4 AUC         .5174          exp_019_mistral7b_depth                0.5232             MISMATCH (self=.5232) ***
Ext Mistral-7B 3v4 AUC         .5174          exp_019b_mistral_cross                 0.5140             MISMATCH (cross=.5140) ***
Ext Mistral-7B 4v5 AUC         .5175          exp_019_mistral7b_depth                0.5181             MATCH (~rounding)
Ext Mistral-7B 4v5 AUC         .5175          exp_019b_mistral_cross                 0.5184             MATCH (~rounding)
Ext Pythia-6.9B 0v1 AUC        .9599          exp_pythia69b_c4_nuc                   0.9599             MATCH
Ext Pythia-6.9B 1v2 AUC        .5955          exp_pythia69b_c4_nuc                   0.5955             MATCH
Ext Pythia-6.9B 2v3 AUC        .5298          exp_pythia69b_c4_nuc                   0.5298             MATCH
Ext Pythia-6.9B 3v4 AUC        .5135          exp_pythia69b_c4_nuc                   0.5135             MATCH
Ext Pythia-6.9B 4v5 AUC        ---            exp_pythia69b_c4_nuc                   not measured       CONSISTENT
Ext Gemma-2B 0v1 AUC           .953           exp_gemma2b_depth                      0.9534             MATCH (rounding)
Ext Gemma-2B 0v1 CI            [.949,.957]    (no registry record)                   N/A                NOT IN REGISTRY ***
Ext Gemma-2B 1v2 AUC           .5981          exp_gemma2b_depth                      0.5981             MATCH
Ext Gemma-2B 1v2 CI            [.588,.608]    exp_gemma2b_depth[bci]                 [.5882,.6076]      MATCH (rounding)
Ext Gemma-2B 2v3 AUC           .534           exp_gemma2b_depth                      0.5342             MATCH (rounding)
Ext Gemma-2B 2v3 CI            [.523,.545]    (no registry record)                   N/A                NOT IN REGISTRY ***
Ext Gemma-2B 3v4 AUC           .5033          exp_gemma2b_depth                      0.5030             MATCH (rounding)
Ext Gemma-2B 3v4 CI            [.492,.514]    (no registry record)                   N/A                NOT IN REGISTRY ***
Ext Gemma-2B 4v5 AUC           .5025          exp_gemma2b_depth                      0.5026             MATCH (rounding)
Ext Gemma-2B 4v5 CI            [.492,.514]    (no registry record)                   N/A                NOT IN REGISTRY ***
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Tys8zmeAdca2dUXMfUjbtC",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "75ccbaf8-4c77-469c-8f36-03a1702af2d6"
}
```

</details>

---


### System

_source line 641_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a409a6aeb060f7eee",
  "tool_use_id": "toolu_01VA6RDVEYrmJqYoJVqwAcxJ",
  "description": "Running python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.c…",
  "usage": {
    "total_tokens": 82372,
    "tool_uses": 46,
    "duration_ms": 561054
  },
  "last_tool_name": "Bash",
  "uuid": "b61a8c35-de15-4754-84eb-b76fdcb4e9a4",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff"
}
```

---


### Tool call

_source line 642_

<details open><summary>🔧 Tool call — Bash · `toolu_01SPLBWY43SdS7Tg3v9Jqoxm`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# Let me check if there's a separate analysis file or exp that has exactly these 6 values\n# Maybe from feature ranking Spearman rho per depth pair across configs\n\n# Try searching for 0.600 as spearman-related value, and also 0.532 and 0.668 as Spearman\n# (not just any AUC value)\n# The task says Table S2 has 'Spearman rho values: 0.600, 0.782, 0.914, 0.893, 0.532, 0.668'\n# These 6 values for Table S2 which has 4 decoding configs × 5 depth pairs = 20 AUC values\n# The Spearman values don't fit the 4×5 structure directly\n\n# Actually rethinking: maybe Spearman rho between depth (1,2,3,4,5) and AUC for each config\n# but using 0-indexed means only 5 points, always monotonic = always -1\n# Unless there are more depth pairs? 0v1,1v2,2v3,3v4,4v5 = 5 pairs, all decreasing -> rho=-1\n\n# OR: these are Spearman rho of the 15 OBD features' individual AUCs across depth pairs\n# for each model-config combination\n\n# I conclude these 6 Spearman values are NOT in the registry at all.\n# The closest match: \n# 0.914 -> exp_005 Pythia_vs_Qwen_cont feature ranking Spearman = 0.9143\n# The others (0.600, 0.782, 0.893, 0.532, 0.668) are not in the registry as Spearman values\n\n# Final check: look for any 'spearman' stored in artifact-style data that I might have missed\nfor exp_id, exp in exps.items():\n    s = json.dumps(exp)\n    if '0.782' in s or '0.600' in s:\n        # Only print if surrounded by context suggesting it's a Spearman value\n        import re\n        for m in re.finditer(r'.{50}(0\\.782|0\\.600).{50}', s):\n            context = m.group(0)\n            if 'spearman' in context.lower() or 'rho' in context.lower():\n                print(f'{exp_id}: {context}')\n\" 2>&1\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VA6RDVEYrmJqYoJVqwAcxJ",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "5a052232-5033-4e86-85cd-6122d17a9601",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012wVULnXxjeWQpbBNw4JdAN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 846,
      "cache_read_input_tokens": 79304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 846,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-23T11:33:03.333Z_

<details><summary>↩ Tool result · `toolu_01SPLBWY43SdS7Tg3v9Jqoxm`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VA6RDVEYrmJqYoJVqwAcxJ",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "7fe2166a-89ca-4bdc-adba-ececdd7603a1"
}
```

</details>

---


### System

_source line 644_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acccdabc14ba72457",
  "tool_use_id": "toolu_01VV28GHoAcAmcY7y7PyWkcR",
  "description": "Running python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.c…",
  "usage": {
    "total_tokens": 120280,
    "tool_uses": 48,
    "duration_ms": 583002
  },
  "last_tool_name": "Bash",
  "uuid": "40599713-23c8-419f-a924-a2cf98a37fa2",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff"
}
```

---


### Tool call

_source line 645_

<details open><summary>🔧 Tool call — Bash · `toolu_01XjDUHHFcjJQ6MaEaYNYKft`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# The 0v1 JSD claim: '0.077 at 8B vs 0.15-0.27 at <=1.5B'\n# Let's see if this is specifically about the arXiv domain context\n# Discussion paragraph 'Boundary cases and scale effect':\n# 'Larger models reduce 0v1 JSD (0.077 at 8B vs. 0.15-0.27 at ≤1.5B)'\n# This is about ALL domains, specifically noting scale effect\n\n# 8B LLaMA C4: 0.077 ✓\n# What about 8B on arXiv? LLaMA-8B arXiv: 0.1296, LLaMA-8B wiki: 0.06169\n# These vary by domain\n\n# For <=1.5B: they likely mean main C4 (or combined) results\n# Qwen-1.5B variants: 0.164 and 0.286\n# OLMo-1B: 0.230\n# Pythia-1.4B: 0.110\n\n# The range 0.15-0.27 excludes Pythia (0.11) and Qwen-instruct (0.286)\n# Perhaps 'typical' range or excluding outliers\n# Qwen-base 0.164 ≈ 0.15, OLMo 0.230, Qwen-instruct 0.286 ≈ 0.27?\n# Qwen-instruct rounds down from 0.286 to 0.27? (imprecise)\n\nprint('JSD range analysis:')\nprint('Qwen-1.5B-Base 0v1 JSD: 0.164 -> paper says lower bound 0.15 (diff: 0.014)')\nprint('Qwen-1.5B-Instruct 0v1 JSD: 0.286 -> paper says upper bound 0.27 (diff: 0.016)')\nprint()\nprint('The range 0.15-0.27 is INACCURATE by ~0.01-0.02 based on registry data.')\nprint('Actual range of <=1.5B models on C4: 0.110-0.286 (including Pythia and Qwen-instruct)')\nprint('Or excluding Pythia and Qwen-instruct: 0.164-0.230')\nprint()\n\n# Let me also see what values the 0v1 JSD is for the rewrite mode (mvp_pilot = Qwen-rewrite)\nprint('Qwen rewrite mvp_pilot 0v1 JSD:', exps['mvp_pilot_sat_v1']['metrics']['pairwise_jsd']['0v1'])\n# = 0.2669\n\n# So the <=1.5B C4 models range:\n# Pythia-1.4B: 0.110\n# Qwen-1.5B-Base: 0.164\n# OLMo-1B: 0.230\n# Qwen-rewrite (MVP/1.5B): 0.267\n# Qwen-1.5B-Instruct: 0.286\n\n# If paper excludes Pythia (0.11) and takes the main continuation mode models:\n# Qwen-base: 0.164, OLMo-1B: 0.230, Qwen-instruct: 0.286\n# Lower: 0.16 (not 0.15), upper: 0.29 (not 0.27)\n\n# OR maybe paper uses Qwen-rewrite 0.267 as upper ≈ 0.27 and Qwen-base 0.164 ≈ 0.15?\n# That would give 0.164-0.267 ≈ '0.15-0.27'\n# This interpretation: rounds 0.164->0.15 and 0.267->0.27\nprint()\nprint('If using Qwen-base (0.164) and Qwen-rewrite (0.267):')\nprint('  Rounded: 0.16 -> 0.15, 0.27 -> 0.27')\nprint('  Upper is exact match; lower is off by 0.014')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VV28GHoAcAmcY7y7PyWkcR",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "9b7156a0-4232-49be-a27f-d0252beeec56",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HSaxMefTFCYivXWvDAQhNp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1198,
      "cache_read_input_tokens": 117196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1198,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 646 · 2026-05-23T11:33:05.361Z_

<details><summary>↩ Tool result · `toolu_01XjDUHHFcjJQ6MaEaYNYKft`</summary>

```text
JSD range analysis:
Qwen-1.5B-Base 0v1 JSD: 0.164 -> paper says lower bound 0.15 (diff: 0.014)
Qwen-1.5B-Instruct 0v1 JSD: 0.286 -> paper says upper bound 0.27 (diff: 0.016)

The range 0.15-0.27 is INACCURATE by ~0.01-0.02 based on registry data.
Actual range of <=1.5B models on C4: 0.110-0.286 (including Pythia and Qwen-instruct)
Or excluding Pythia and Qwen-instruct: 0.164-0.230

Qwen rewrite mvp_pilot 0v1 JSD: 0.2669

If using Qwen-base (0.164) and Qwen-rewrite (0.267):
  Rounded: 0.16 -> 0.15, 0.27 -> 0.27
  Upper is exact match; lower is off by 0.014
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VV28GHoAcAmcY7y7PyWkcR",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "87c9805b-3baa-4b99-9ee6-ab6b816601a2"
}
```

</details>

---


### System

_source line 647_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acccdabc14ba72457",
  "tool_use_id": "toolu_01VV28GHoAcAmcY7y7PyWkcR",
  "description": "Running python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.c…",
  "usage": {
    "total_tokens": 121846,
    "tool_uses": 49,
    "duration_ms": 597221
  },
  "last_tool_name": "Bash",
  "uuid": "2d66fab1-139f-446b-ae78-b9a29278664a",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff"
}
```

---


### Tool call

_source line 648_

<details open><summary>🔧 Tool call — Bash · `toolu_01DooMKYjg9hLuSGV9Rdot51`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Also check the OLMo self-scored 1v2 value (before update)\n# exp_002 notes: 'Self-scored 1v2=0.6145, Qwen-scored 1v2=0.5001'\n# But the self-scored value of 0.6145 - where does it come from?\n# It was a previous run of exp_002 before cross-scoring was applied\n\ne002 = exps['exp_002_olmo_depth']\nprint('exp_002 full metrics:')\nprint(json.dumps(e002['metrics'], indent=2))\nprint()\nprint('exp_002 notes:', e002.get('notes', '')[:400])\n\n# The self-scored OLMo value 0.6145 appears to be from old runs\n# Qwen cross-scored: 0.5001 (the updated result)\n# Gap = 0.6145 - 0.5001 = 0.1144 = 11.44pp\n# Paper says +11.5pp: rounds 11.44 to 11.5 (difference of 0.06pp - acceptable rounding)\n\nprint()\nprint('OLMo gap computation: 11.44 pp vs paper 11.5pp - rounding OK')\nprint('Pythia gap: 4.65pp vs paper 4.7pp - rounding OK')\nprint('OLMo: self=0.6145, cross=0.5001 -> delta=11.44pp (rounds to 11.5pp)')\nprint('Pythia: self=0.6539, cross=0.6074 -> delta=4.65pp (rounds to 4.7pp)')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VV28GHoAcAmcY7y7PyWkcR",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "9a10d765-f12f-4381-b70b-8e78ba3910cb",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019pxrBdvjfWA1qthN8gzuzL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1526,
      "cache_read_input_tokens": 118394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1526,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-23T11:33:19.580Z_

<details><summary>↩ Tool result · `toolu_01DooMKYjg9hLuSGV9Rdot51`</summary>

```text
exp_002 full metrics:
{
  "k_star": 1,
  "pairwise_auc": {
    "0v1": 0.9861,
    "1v2": 0.5001,
    "2v3": 0.4972,
    "3v4": 0.5034,
    "4v5": 0.4971
  },
  "scorer": "Qwen2.5-1.5B-Instruct",
  "note": "Updated to Qwen cross-scoring (D107). Self-scored 1v2=0.6145 K*=2, Qwen-scored 1v2=0.5001 K*=1."
}

exp_002 notes: 

OLMo gap computation: 11.44 pp vs paper 11.5pp - rounding OK
Pythia gap: 4.65pp vs paper 4.7pp - rounding OK
OLMo: self=0.6145, cross=0.5001 -> delta=11.44pp (rounds to 11.5pp)
Pythia: self=0.6539, cross=0.6074 -> delta=4.65pp (rounds to 4.7pp)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VV28GHoAcAmcY7y7PyWkcR",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "b4ea6139-55c4-40b2-a374-705ecc634641"
}
```

</details>

---


### System

_source line 650_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8202b98a7a15f0",
  "tool_use_id": "toolu_018tQpraGEn5S4TsCg74MpUC",
  "description": "Running python3 -c \"\nfrom decimal import Decimal, ROUND_HA…",
  "usage": {
    "total_tokens": 84231,
    "tool_uses": 56,
    "duration_ms": 614139
  },
  "last_tool_name": "Bash",
  "uuid": "87a6e9db-14a3-4f0a-9a32-afd0d1f42596",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff"
}
```

---


### Tool call

_source line 651_

<details open><summary>🔧 Tool call — Bash · `toolu_01GVBiQ9WtsRsUEMf3ueyk8Q`</summary>

```json
{
  "command": "python3 -c \"\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\n# S12 arXiv 4v5: paper=.530, registry=0.5294 -> rounds to 0.529\n# But paper shows .530 which requires 0.5295+\nprint('S12 arXiv 4v5:')\nprint(f'  0.5294 rounds to {round_standard(0.5294, 3)}')\nprint(f'  For .530: need value in [0.5295, 0.5305)')\nprint()\n\n# Note: Table 4 also shows arXiv/Qwen-1.5B but there's no 4v5 in Table 4 (not shown)\n# S12 uses the same exp_024 data, so the 4v5 issue propagates\n\n# Summary of all mismatches:\nprint('='*70)\nprint('FINAL MISMATCH SUMMARY')\nprint('='*70)\nprint()\nprint('Table 4 mismatches:')\nprint('  1. arXiv/Qwen-1.5B 2v3: paper=.644, registry=0.6427 (rounds to .643)')\nprint('  2. Code/LLaMA-8B 2v3: paper=.510, registry=0.5112 (rounds to .511)')\nprint()\nprint('Table S12 mismatches:')\nprint('  3. arXiv col, 2v3: paper=.644, registry=0.6427 (rounds to .643)  [same as #1]')\nprint('  4. arXiv col, 4v5: paper=.530, registry=0.5294 (rounds to .529)')\nprint('  (Wiki 0v1, 3v4, 4v5: UNVERIFIABLE - exp_023 has incomplete registry metrics)')\nprint()\nprint('Inline claim mismatches:')\nprint('  5. Qwen arXiv 2v3 inline: paper=0.644, registry=0.6427 (rounds to 0.643) [same as #1]')\nprint('  6. LLaMA-8B arXiv 2v3 inline: paper=0.620, registry=0.6215 (rounds to 0.622)')\nprint('  7. Pythia arXiv CI lower: paper=0.640, registry=0.6401 (rounds to 0.640) -- BORDERLINE')\nprint('     (0.6401 -> actually rounds to 0.640 with ROUND_HALF_UP: OK)')\nprint(f'     round_standard(0.6401, 3) = {round_standard(0.6401, 3)}')\nprint()\nprint('JSD claim:')\nprint('  8. arXiv 1v2 JSD = 0.077: no registry experiment has exactly 0.077 for arXiv 1v2 JSD')\nprint('     Nearest: Mistral arXiv=0.0762, LLaMA arXiv=0.0785')\nprint('     C4 JSD ~0.01: exp_016=0.01081 -- OK (matches ~0.01)')\nprint()\nprint('Not a mismatch (verifiable OK):')\nprint('  - arXiv/Pythia 2v3: 0.6545 rounds to 0.655 -- OK')\nprint('  - Pythia CI [0.640, 0.669]: registry [0.6401, 0.6688] -- OK')\nprint('  - Qwen arXiv CI [0.628, 0.658]: registry [0.6275, 0.6575] -- OK')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018tQpraGEn5S4TsCg74MpUC",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "4b67faa6-6581-4483-87c2-9073a11e283d",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012jFrXxvoSAGbsbRXgiidFv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1522,
      "cache_read_input_tokens": 80106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1522,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 652 · 2026-05-23T11:33:22.990Z_

<details><summary>↩ Tool result · `toolu_01GVBiQ9WtsRsUEMf3ueyk8Q`</summary>

```text
S12 arXiv 4v5:
  0.5294 rounds to 0.529
  For .530: need value in [0.5295, 0.5305)

======================================================================
FINAL MISMATCH SUMMARY
======================================================================

Table 4 mismatches:
  1. arXiv/Qwen-1.5B 2v3: paper=.644, registry=0.6427 (rounds to .643)
  2. Code/LLaMA-8B 2v3: paper=.510, registry=0.5112 (rounds to .511)

Table S12 mismatches:
  3. arXiv col, 2v3: paper=.644, registry=0.6427 (rounds to .643)  [same as #1]
  4. arXiv col, 4v5: paper=.530, registry=0.5294 (rounds to .529)
  (Wiki 0v1, 3v4, 4v5: UNVERIFIABLE - exp_023 has incomplete registry metrics)

Inline claim mismatches:
  5. Qwen arXiv 2v3 inline: paper=0.644, registry=0.6427 (rounds to 0.643) [same as #1]
  6. LLaMA-8B arXiv 2v3 inline: paper=0.620, registry=0.6215 (rounds to 0.622)
  7. Pythia arXiv CI lower: paper=0.640, registry=0.6401 (rounds to 0.640) -- BORDERLINE
     (0.6401 -> actually rounds to 0.640 with ROUND_HALF_UP: OK)
     round_standard(0.6401, 3) = 0.64

JSD claim:
  8. arXiv 1v2 JSD = 0.077: no registry experiment has exactly 0.077 for arXiv 1v2 JSD
     Nearest: Mistral arXiv=0.0762, LLaMA arXiv=0.0785
     C4 JSD ~0.01: exp_016=0.01081 -- OK (matches ~0.01)

Not a mismatch (verifiable OK):
  - arXiv/Pythia 2v3: 0.6545 rounds to 0.655 -- OK
  - Pythia CI [0.640, 0.669]: registry [0.6401, 0.6688] -- OK
  - Qwen arXiv CI [0.628, 0.658]: registry [0.6275, 0.6575] -- OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018tQpraGEn5S4TsCg74MpUC",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "45c923fb-7b76-4fae-8579-5d72552fb6da"
}
```

</details>

---


### System

_source line 653_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a409a6aeb060f7eee",
  "tool_use_id": "toolu_01VA6RDVEYrmJqYoJVqwAcxJ",
  "description": "Running python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.c…",
  "usage": {
    "total_tokens": 83262,
    "tool_uses": 47,
    "duration_ms": 582425
  },
  "last_tool_name": "Bash",
  "uuid": "a99f8ab9-e3c2-4155-8626-d0891cf17c15",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff"
}
```

---


### Tool call

_source line 654_

<details open><summary>🔧 Tool call — Bash · `toolu_01BJHrkyD2p8u9N4Kqwc66aV`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# Double-check OLMo Table S8 CI bounds (paper has CI but exp_002 only has point estimates)\n# Also need to check if there's a separate bootstrap experiment for OLMo cross-scored\n# or if the CIs come from somewhere else\n\n# Check: does exp_007 olmo_cont match paper exactly except it's self-scored vs cross-scored?\nexp007 = exps['exp_007_bootstrap_ci']\nexp007_olmo = exp007['metrics']['olmo_cont']\nexp002 = exps['exp_002_olmo_depth']\nexp002_auc = exp002['metrics']['pairwise_auc']\n\nprint('exp_007 olmo_cont (self-scored):')\nfor pair in ['0v1','1v2','2v3','3v4','4v5']:\n    e = exp007_olmo[pair]\n    print(f'  {pair}: auc={e[\\\"auc\\\"]:.4f} ci=[{e[\\\"ci_lower\\\"]:.4f},{e[\\\"ci_upper\\\"]:.4f}]')\n\nprint()\nprint('exp_002 olmo_depth (Qwen cross-scored, no CI):')\nfor pair in ['0v1','1v2','2v3','3v4','4v5']:\n    print(f'  {pair}: auc={exp002_auc[pair]:.4f}')\n\nprint()\nprint('Paper Table S8 OLMo:')\npaper_olmo = {\n    '0v1': (.986, .984, .988),\n    '1v2': (.500, .496, .519),\n    '2v3': (.497, .486, .509),\n    '3v4': (.502, .491, .513),\n    '4v5': (.494, .483, .506),\n}\nfor pair, (auc, lo, hi) in paper_olmo.items():\n    print(f'  {pair}: auc={auc:.3f} ci=[{lo:.3f},{hi:.3f}]')\n\" 2>&1\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VA6RDVEYrmJqYoJVqwAcxJ",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "b5a86da8-af7d-424d-856f-83e2f586b841",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Q5W2bMdjGn8QjHeJAJVqR5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 80150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 818,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-23T11:33:24.684Z_

<details><summary>↩ Tool result · `toolu_01BJHrkyD2p8u9N4Kqwc66aV`</summary>

```text
exp_007 olmo_cont (self-scored):
  0v1: auc=0.9970 ci=[0.9964,0.9975]
  1v2: auc=0.6145 ci=[0.6045,0.6247]
  2v3: auc=0.5496 ci=[0.5399,0.5596]
  3v4: auc=0.5091 ci=[0.4973,0.5200]
  4v5: auc=0.5045 ci=[0.4932,0.5150]

exp_002 olmo_depth (Qwen cross-scored, no CI):
  0v1: auc=0.9861
  1v2: auc=0.5001
  2v3: auc=0.4972
  3v4: auc=0.5034
  4v5: auc=0.4971

Paper Table S8 OLMo:
  0v1: auc=0.986 ci=[0.984,0.988]
  1v2: auc=0.500 ci=[0.496,0.519]
  2v3: auc=0.497 ci=[0.486,0.509]
  3v4: auc=0.502 ci=[0.491,0.513]
  4v5: auc=0.494 ci=[0.483,0.506]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VA6RDVEYrmJqYoJVqwAcxJ",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "32a6505c-6815-4603-bd49-0b62de8d8679"
}
```

</details>

---


### System

_source line 656_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8202b98a7a15f0",
  "tool_use_id": "toolu_018tQpraGEn5S4TsCg74MpUC",
  "description": "Running python3 -c \"\nfrom decimal import Decimal, ROUND_HA…",
  "usage": {
    "total_tokens": 85953,
    "tool_uses": 57,
    "duration_ms": 623747
  },
  "last_tool_name": "Bash",
  "uuid": "6d159f2f-c71b-4646-b6a9-63b914579c33",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff"
}
```

---


### Tool call

_source line 657_

<details open><summary>🔧 Tool call — Bash · `toolu_01DmSZwqA6KvT4cDMhBb6hhq`</summary>

```json
{
  "command": "python3 -c \"\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\n# Double-check: Pythia CI lower 0.6401 -> 0.640? Using ROUND_HALF_UP\nprint('Pythia CI lower 0.6401 ->',round_standard(0.6401, 3))\n# 0.6401: 4th decimal is 1, so we round down -> 0.640 OK\n\n# Let me also confirm CI for Qwen arXiv: [0.628, 0.658]\n# 0.6275 -> 0.628 (standard half-up: 4th decimal is 5, rounds up the 3rd: 7->8 -> 0.628) WAIT\n# 0.6275: d=0.627|5 so 3rd decimal=7, 4th decimal=5 -> round up 7->8 -> NO WAIT\n# 0.6275 means: 0.6 2 7 5 -> 3dp means we look at 4th dp=5 -> round up 3rd dp (7->8? no, that's not right)\n# 0.6275 in 3dp: floor is 0.627, next is 0.628\n# The digit at 4th decimal position is 5 -> rounds up -> 0.628 \nprint('Qwen arXiv CI lower 0.6275 ->', round_standard(0.6275, 3))  # should be 0.628\n\n# 0.6575: 4th decimal is 5 -> rounds up -> 0.658\nprint('Qwen arXiv CI upper 0.6575 ->', round_standard(0.6575, 3))  # should be 0.658\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018tQpraGEn5S4TsCg74MpUC",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "f5d81e6c-672d-4b45-9680-c7ab0b3613b6",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01ULk2TE2VG2MadvTJQCJhe3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1680,
      "cache_read_input_tokens": 81628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1680,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 658 · 2026-05-23T11:33:32.607Z_

<details><summary>↩ Tool result · `toolu_01DmSZwqA6KvT4cDMhBb6hhq`</summary>

```text
Pythia CI lower 0.6401 -> 0.64
Qwen arXiv CI lower 0.6275 -> 0.628
Qwen arXiv CI upper 0.6575 -> 0.658
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018tQpraGEn5S4TsCg74MpUC",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "678b864d-5303-4291-854f-ca1daf276add"
}
```

</details>

---


### System

_source line 659_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acccdabc14ba72457",
  "tool_use_id": "toolu_01VV28GHoAcAmcY7y7PyWkcR",
  "description": "Running python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.c…",
  "usage": {
    "total_tokens": 122820,
    "tool_uses": 50,
    "duration_ms": 611233
  },
  "last_tool_name": "Bash",
  "uuid": "51d8b240-47ce-4aae-b28e-a25e62e8993c",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff"
}
```

---


### Tool call

_source line 660_

<details open><summary>🔧 Tool call — Bash · `toolu_01EkEGziEZhMLEuNyjxQTfH9`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Check if Mistral ~1.9pp is a different comparison\n# The paper says 'LLaMA-8B and Mistral-7B (~+1.9 pp each)'\n# For Mistral: self=0.5935, cross=0.5695 => 2.4pp (from exp_019 self vs exp_019b cross)\n# \n# But wait - do these two experiments use the same data?\n# exp_019 self-scored = Mistral scoring its own Mistral-generated text\n# exp_019b cross-scored = Qwen scoring Mistral-generated text\n# The data IS the same (Mistral-generated C4 text)\n# So the gap is valid: 2.4pp\n# \n# Paper says ~1.9pp - which is off by 0.5pp\n# This could be because the paper average includes LLaMA, and LLaMA gap is smaller\n# OR the Mistral self-scored value might be different (maybe not from exp_019)\n#\n# Let me check if there's another Mistral self-scored experiment\nprint('Mistral experiments:')\nfor k, v in exps.items():\n    if 'mistral' in k.lower():\n        m = v.get('metrics', {})\n        auc_1v2 = m.get('pairwise_auc', {}).get('1v2') or m.get('auc_1v2')\n        scorer = v.get('spec', {}).get('eval_data', '') or v.get('metrics', {}).get('scorer', '')\n        print(f'  {k}: 1v2={auc_1v2}, conclusion={v.get(\\\"conclusion\\\")}')\n\nprint()\nprint('The key issue: paper says LLaMA/Mistral ~+1.9pp each')\nprint('From registry: Mistral self=0.5935, cross=0.5695 => 2.4pp')\nprint('For LLaMA: no self-scorer experiment exists')\nprint('If LLaMA gap ~1.4pp and Mistral ~2.4pp, average ~ 1.9pp')\nprint('But paper says each is ~1.9pp, not average')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VV28GHoAcAmcY7y7PyWkcR",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "60cbb3ae-e6bb-4dd4-9b3f-b18142d6d171",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014xok2SkM3Xiw4EziGu9w6L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 910,
      "cache_read_input_tokens": 119920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 910,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-23T11:33:33.628Z_

<details><summary>↩ Tool result · `toolu_01EkEGziEZhMLEuNyjxQTfH9`</summary>

```text
Mistral experiments:
  exp_code_mistral7b: 1v2=0.6152, conclusion=success
  exp_arXiv_mistral7b_crossscorer: 1v2=0.8141, conclusion=success
  exp_wiki_mistral7b: 1v2=0.5552, conclusion=success
  exp_arXiv_mistral7b: 1v2=0.8201, conclusion=success
  exp_019b_mistral_cross_scorer: 1v2=0.5695, conclusion=success
  exp_019_mistral7b_depth: 1v2=0.5935, conclusion=success

The key issue: paper says LLaMA/Mistral ~+1.9pp each
From registry: Mistral self=0.5935, cross=0.5695 => 2.4pp
For LLaMA: no self-scorer experiment exists
If LLaMA gap ~1.4pp and Mistral ~2.4pp, average ~ 1.9pp
But paper says each is ~1.9pp, not average
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VV28GHoAcAmcY7y7PyWkcR",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "4c664113-2cba-42a9-a7d9-44a662908e43"
}
```

</details>

---


### System

_source line 662_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a1e61486c7d1a5661",
  "tool_use_id": "toolu_01Tys8zmeAdca2dUXMfUjbtC",
  "status": "completed",
  "output_file": "",
  "summary": "Audit Table 1 + extended table AUC values",
  "usage": {
    "total_tokens": 91779,
    "tool_uses": 38,
    "duration_ms": 650357
  },
  "uuid": "8818e5fa-bfd0-4415-9093-5574152e0bcd",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff"
}
```

---


### Tool result

_source line 663 · 2026-05-23T11:33:39.984Z_

<details><summary>↩ Tool result · `toolu_01Tys8zmeAdca2dUXMfUjbtC`</summary>

```text
Here is the complete audit result.

---

## Cross-Reference: Paper Tables vs Registry

**Registry source file:** `/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt`

**Paper source:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex` (Table 1) and `docs/paper/appendix.tex` (Extended Table)

---

### Table 1 (tab:kstar_ci) — 5 Main Models

| Location | Paper Value | Registry exp_id | Registry Value | Match? |
|---|---|---|---|---|
| Qwen-rw 0v1 AUC | .9956 | exp_007_bootstrap_ci[qwen_rewrite] | 0.9956 | MATCH |
| Qwen-rw 1v2 AUC | .6955 | exp_007_bootstrap_ci[qwen_rewrite] | 0.6955 | MATCH |
| Qwen-rw 1v2 CI | [.686,.704] | exp_007_bootstrap_ci[qwen_rewrite] | [.6859,.7041] | MATCH (rounding) |
| Qwen-rw 2v3 AUC | .5893 | exp_007_bootstrap_ci[qwen_rewrite] | 0.5893 | MATCH |
| Qwen-rw 2v3 CI | [.580,.599] | exp_007_bootstrap_ci[qwen_rewrite] | [.5795,.5991] | MATCH (rounding) |
| Qwen-rw 3v4 AUC | .5435 | exp_007_bootstrap_ci[qwen_rewrite] | 0.5435 | MATCH |
| Qwen-rw 4v5 AUC | .5340 | exp_007_bootstrap_ci[qwen_rewrite] | 0.5340 | MATCH |
| Pythia 0v1 AUC | .9722 | exp_001_pythia_depth | 0.9722 | MATCH |
| Pythia 1v2 AUC | .6074 | exp_001_pythia_depth | 0.6074 | MATCH |
| Pythia 1v2 CI | [.598,.617] | exp_001_pythia_depth[bootstrap_ci] | [.5975,.6172] | MATCH (rounding) |
| Pythia 2v3 AUC | .5440 | exp_001_pythia_depth | 0.5440 | MATCH |
| **Pythia 2v3 CI** | **[.534,.554]** | **(no registry record)** | **N/A** | **NOT IN REGISTRY** |
| Pythia 3v4 AUC | .5051 | exp_001_pythia_depth | 0.5051 | MATCH |
| Pythia 4v5 AUC | .5079 | exp_001_pythia_depth | 0.5079 | MATCH |
| OLMo 0v1 AUC | .9860 | exp_002_olmo_depth | 0.9861 | MATCH (rounding) |
| OLMo 1v2 AUC | .5001 | exp_002_olmo_depth | 0.5001 | MATCH |
| **OLMo 1v2 CI** | **[.496,.519]** | **(no registry record)** | **N/A** | **NOT IN REGISTRY** |
| OLMo 2v3 AUC | .4973 | exp_002_olmo_depth | 0.4972 | MATCH (rounding) |
| **OLMo 2v3 CI** | **[.486,.509]** | **(no registry record)** | **N/A** | **NOT IN REGISTRY** |
| **OLMo 3v4 AUC** | **.5024** | **exp_002_olmo_depth** | **0.5034** | **MISMATCH (+0.001)** |
| **OLMo 4v5 AUC** | **.4942** | **exp_002_olmo_depth** | **0.4971** | **MISMATCH (+0.003)** |
| Qwen-cont 0v1 AUC | .9971 | exp_007_bootstrap_ci[qwen_cont] | 0.9971 | MATCH |
| Qwen-cont 1v2 AUC | .6112 | exp_007_bootstrap_ci[qwen_cont] | 0.6112 | MATCH |
| Qwen-cont 1v2 CI | [.602,.621] | exp_007_bootstrap_ci[qwen_cont] | [.6015,.6213] | MATCH (rounding) |
| Qwen-cont 2v3 AUC | .5609 | exp_007_bootstrap_ci[qwen_cont] | 0.5609 | MATCH |
| Qwen-cont 2v3 CI | [.551,.571] | exp_007_bootstrap_ci[qwen_cont] | [.5511,.5712] | MATCH (rounding) |
| Qwen-cont 3v4 AUC | .5409 | exp_007_bootstrap_ci[qwen_cont] | 0.5409 | MATCH |
| Qwen-cont 4v5 AUC | .5141 | exp_007_bootstrap_ci[qwen_cont] | 0.5141 | MATCH |
| Qwen-7B 0v1 AUC | .9638 | exp_004_7b_crossscale[bootstrap_ci] | 0.9638 | MATCH |
| Qwen-7B 0v1 CI | [.961,.967] | exp_004_7b_crossscale[bootstrap_ci] | [.9607,.9665] | MATCH (rounding) |
| Qwen-7B 1v2 AUC | .6168 | exp_004_7b_crossscale[bootstrap_ci] | 0.6168 | MATCH |
| Qwen-7B 1v2 CI | [.608,.626] | exp_004_7b_crossscale[bootstrap_ci] | [.6079,.6261] | MATCH (rounding) |
| Qwen-7B 2v3 AUC | .5492 | exp_004_7b_crossscale[bootstrap_ci] | 0.5492 | MATCH |
| Qwen-7B 2v3 CI | [.539,.559] | exp_004_7b_crossscale[bootstrap_ci] | [.5388,.5594] | MATCH (rounding) |
| Qwen-7B 3v4 AUC | .5276 | exp_004_7b_crossscale[bootstrap_ci] | 0.5276 | MATCH |
| Qwen-7B 4v5 AUC | .5085 | exp_004_7b_crossscale[bootstrap_ci] | 0.5085 | MATCH |

---

### Extended Table (tab:kstar_ci_extended) — 5 Additional Models

All Qwen-base (exp_016_base_vs_instruct) and LLaMA-8B (exp_018_llama8b_depth) values — both AUC and all 5 CI pairs — match exactly (within 3-decimal rounding). All Pythia-6.9B (exp_pythia69b_c4_nuc) AUC values match. Gemma-2B (exp_gemma2b_depth) all AUC values match; only 1v2 CI is in the registry and it matches.

**Mismatches and gaps in the extended table:**

| Location | Paper Value | Registry exp_id | Registry Value | Match? |
|---|---|---|---|---|
| **Mistral-7B 0v1 AUC** | **.9170** | exp_019_mistral7b_depth (self) | 0.9843 | **MISMATCH (−0.067)** |
| **Mistral-7B 0v1 AUC** | **.9170** | exp_019b_mistral_cross_scorer | 0.9209 | **MISMATCH (−0.004)** |
| **Mistral-7B 1v2 AUC** | **.5750** | exp_019_mistral7b_depth (self) | 0.5935 | **MISMATCH (−0.019)** |
| **Mistral-7B 1v2 AUC** | **.5750** | exp_019b_mistral_cross_scorer | 0.5695 | **MISMATCH (−0.006)** |
| **Mistral-7B 2v3 AUC** | **.5369** | exp_019_mistral7b_depth (self) | 0.5402 | **MISMATCH (−0.003)** |
| **Mistral-7B 2v3 AUC** | **.5369** | exp_019b_mistral_cross_scorer | 0.5335 | **MISMATCH (+0.003)** |
| **Mistral-7B 3v4 AUC** | **.5174** | exp_019_mistral7b_depth (self) | 0.5232 | **MISMATCH (−0.006)** |
| **Mistral-7B 3v4 AUC** | **.5174** | exp_019b_mistral_cross_scorer | 0.5140 | **MISMATCH (+0.003)** |
| Mistral-7B 4v5 AUC | .5175 | both exp_019/019b | .5181/.5184 | MATCH (~rounding) |
| **Gemma-2B 0v1 CI** | **[.949,.957]** | **(no registry record)** | **N/A** | **NOT IN REGISTRY** |
| Gemma-2B 1v2 CI | [.588,.608] | exp_gemma2b_depth | [.5882,.6076] | MATCH (rounding) |
| **Gemma-2B 2v3 CI** | **[.523,.545]** | **(no registry record)** | **N/A** | **NOT IN REGISTRY** |
| **Gemma-2B 3v4 CI** | **[.492,.514]** | **(no registry record)** | **N/A** | **NOT IN REGISTRY** |
| **Gemma-2B 4v5 CI** | **[.492,.514]** | **(no registry record)** | **N/A** | **NOT IN REGISTRY** |

---

### Summary of All Issues

**Genuine mismatches (AUC values differ from all registry experiments):**

1. **OLMo 3v4 AUC**: paper=.5024, registry=0.5034 (diff=+0.001). Discrepancy is small but consistent — the registry was updated 2026-05-22 with cross-scored values (D107 update), and the paper number may be from an earlier snapshot.

2. **OLMo 4v5 AUC**: paper=.4942, registry=0.4971 (diff=+0.003). Same root cause as OLMo 3v4.

3. **Mistral-7B 0v1 AUC**: paper=.9170. Self-scorer experiment (exp_019) gives 0.9843; cross-scorer experiment (exp_019b) gives 0.9209. Neither matches. The paper value .9170 does not correspond to any registry experiment. This is the largest unexplained discrepancy.

4. **Mistral-7B 1v2 AUC**: paper=.5750. Self-scorer=0.5935, cross-scorer=0.5695. Neither matches. No registry entry has this value.

5. **Mistral-7B 2v3–3v4 AUC**: paper values (.5369, .5174) coincidentally equal the arithmetic average of self+cross-scorer for 2v3 (exactly: (0.5402+0.5335)/2=0.5369) but not for 3v4 (avg=0.5186 vs paper=0.5174). There is no registry experiment that produced these values directly.

**CIs in paper with no matching registry record (bootstrap was run but not logged):**

- Pythia 2v3 CI [.534,.554] — exp_001 only has bootstrap_ci for 1v2, not 2v3
- OLMo 1v2 CI [.496,.519] — exp_002 has no bootstrap_ci at all
- OLMo 2v3 CI [.486,.509] — same
- Gemma-2B 0v1 CI [.949,.957], 2v3 CI [.523,.545], 3v4 CI [.492,.514], 4v5 CI [.492,.514] — exp_gemma2b_depth only logged bootstrap_ci_1v2

These CI values are internally plausible (the AUC point estimates match), but the bootstrap runs that produced them are not recorded in the registry.

agentId: a1e61486c7d1a5661 (use SendMessage with to: 'a1e61486c7d1a5661' to continue this agent)
&lt;usage>total_tokens: 93670
tool_uses: 38
duration_ms: 650361&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "28c0b19f-e40f-44e1-b5a8-98cc79e4b8d7",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are auditing numerical data in a research paper against experiment registry records.\n\nThe registry data is saved as JSON at:\n/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt\n\nThe format is `{\"result\": \"&lt;JSON string>\"}` — parse the inner JSON string to get experiment records.\n\nYour task: extract all experiments related to pairwise AUC / K* boundary results. Look for exp_ids containing keywords like \"kstar\", \"boundary\", \"pairwise\", \"bootstrap\", \"auc\", \"depth\", \"core\", \"model\", or any experiment that has pairwise AUC metrics for depth pairs (0v1, 1v2, 2v3, 3v4, 4v5).\n\nThen cross-reference against these paper values from Table 1 (tab:kstar_ci) in experiments_c1.tex:\n\n**Table 1 values (5 models × 5 depth pairs)**:\n- Qwen-rw: 0v1=.9956, 1v2=.6955 [.686,.704], 2v3=.5893 [.580,.599], 3v4=.5435, 4v5=.5340\n- Pythia: 0v1=.9722, 1v2=.6074 [.598,.617], 2v3=.5440 [.534,.554], 3v4=.5051, 4v5=.5079\n- OLMo: 0v1=.9860, 1v2=.5001 [.496,.519], 2v3=.4973 [.486,.509], 3v4=.5024, 4v5=.4942\n- Qwen-cont: 0v1=.9971, 1v2=.6112 [.602,.621], 2v3=.5609 [.551,.571], 3v4=.5409, 4v5=.5141\n- Qwen-7B: 0v1=.9638 [.961,.967], 1v2=.6168 [.608,.626], 2v3=.5492 [.539,.559], 3v4=.5276, 4v5=.5085\n\n**Extended table (tab:kstar_ci_extended) additional models**:\n- Qwen-base: 0v1=.987 [.985,.989], 1v2=.626 [.617,.635], 2v3=.550 [.540,.560], 3v4=.529 [.519,.540], 4v5=.518 [.508,.529]\n- LLaMA-8B: 0v1=.9224 [.917,.927], 1v2=.6123 [.603,.622], 2v3=.5273 [.517,.538], 3v4=.5168 [.506,.528], 4v5=.5159 [.505,.527]\n- Mistral-7B: 0v1=.9170, 1v2=.5750, 2v3=.5369, 3v4=.5174, 4v5=.5175\n- Pythia-6.9B: 0v1=.9599, 1v2=.5955, 2v3=.5298, 3v4=.5135, 4v5=---\n- Gemma-2B: 0v1=.953 [.949,.957], 1v2=.5981 [.588,.608], 2v3=.534 [.523,.545], 3v4=.5033 [.492,.514], 4v5=.5025 [.492,.514]\n\nFor each value, output a row:\n| Location | Paper Value | Registry exp_id | Registry Value | Match? |\n\nUse jq or python to parse the registry. Report all mismatches explicitly. Be thorough — check every single number.",
    "agentId": "a1e61486c7d1a5661",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete audit result.\n\n---\n\n## Cross-Reference: Paper Tables vs Registry\n\n**Registry source file:** `/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt`\n\n**Paper source:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex` (Table 1) and `docs/paper/appendix.tex` (Extended Table)\n\n---\n\n### Table 1 (tab:kstar_ci) — 5 Main Models\n\n| Location | Paper Value | Registry exp_id | Registry Value | Match? |\n|---|---|---|---|---|\n| Qwen-rw 0v1 AUC | .9956 | exp_007_bootstrap_ci[qwen_rewrite] | 0.9956 | MATCH |\n| Qwen-rw 1v2 AUC | .6955 | exp_007_bootstrap_ci[qwen_rewrite] | 0.6955 | MATCH |\n| Qwen-rw 1v2 CI | [.686,.704] | exp_007_bootstrap_ci[qwen_rewrite] | [.6859,.7041] | MATCH (rounding) |\n| Qwen-rw 2v3 AUC | .5893 | exp_007_bootstrap_ci[qwen_rewrite] | 0.5893 | MATCH |\n| Qwen-rw 2v3 CI | [.580,.599] | exp_007_bootstrap_ci[qwen_rewrite] | [.5795,.5991] | MATCH (rounding) |\n| Qwen-rw 3v4 AUC | .5435 | exp_007_bootstrap_ci[qwen_rewrite] | 0.5435 | MATCH |\n| Qwen-rw 4v5 AUC | .5340 | exp_007_bootstrap_ci[qwen_rewrite] | 0.5340 | MATCH |\n| Pythia 0v1 AUC | .9722 | exp_001_pythia_depth | 0.9722 | MATCH |\n| Pythia 1v2 AUC | .6074 | exp_001_pythia_depth | 0.6074 | MATCH |\n| Pythia 1v2 CI | [.598,.617] | exp_001_pythia_depth[bootstrap_ci] | [.5975,.6172] | MATCH (rounding) |\n| Pythia 2v3 AUC | .5440 | exp_001_pythia_depth | 0.5440 | MATCH |\n| **Pythia 2v3 CI** | **[.534,.554]** | **(no registry record)** | **N/A** | **NOT IN REGISTRY** |\n| Pythia 3v4 AUC | .5051 | exp_001_pythia_depth | 0.5051 | MATCH |\n| Pythia 4v5 AUC | .5079 | exp_001_pythia_depth | 0.5079 | MATCH |\n| OLMo 0v1 AUC | .9860 | exp_002_olmo_depth | 0.9861 | MATCH (rounding) |\n| OLMo 1v2 AUC | .5001 | exp_002_olmo_depth | 0.5001 | MATCH |\n| **OLMo 1v2 CI** | **[.496,.519]** | **(no registry record)** | **N/A** | **NOT IN REGISTRY** |\n| OLMo 2v3 AUC | .4973 | exp_002_olmo_depth | 0.4972 | MATCH (rounding) |\n| **OLMo 2v3 CI** | **[.486,.509]** | **(no registry record)** | **N/A** | **NOT IN REGISTRY** |\n| **OLMo 3v4 AUC** | **.5024** | **exp_002_olmo_depth** | **0.5034** | **MISMATCH (+0.001)** |\n| **OLMo 4v5 AUC** | **.4942** | **exp_002_olmo_depth** | **0.4971** | **MISMATCH (+0.003)** |\n| Qwen-cont 0v1 AUC | .9971 | exp_007_bootstrap_ci[qwen_cont] | 0.9971 | MATCH |\n| Qwen-cont 1v2 AUC | .6112 | exp_007_bootstrap_ci[qwen_cont] | 0.6112 | MATCH |\n| Qwen-cont 1v2 CI | [.602,.621] | exp_007_bootstrap_ci[qwen_cont] | [.6015,.6213] | MATCH (rounding) |\n| Qwen-cont 2v3 AUC | .5609 | exp_007_bootstrap_ci[qwen_cont] | 0.5609 | MATCH |\n| Qwen-cont 2v3 CI | [.551,.571] | exp_007_bootstrap_ci[qwen_cont] | [.5511,.5712] | MATCH (rounding) |\n| Qwen-cont 3v4 AUC | .5409 | exp_007_bootstrap_ci[qwen_cont] | 0.5409 | MATCH |\n| Qwen-cont 4v5 AUC | .5141 | exp_007_bootstrap_ci[qwen_cont] | 0.5141 | MATCH |\n| Qwen-7B 0v1 AUC | .9638 | exp_004_7b_crossscale[bootstrap_ci] | 0.9638 | MATCH |\n| Qwen-7B 0v1 CI | [.961,.967] | exp_004_7b_crossscale[bootstrap_ci] | [.9607,.9665] | MATCH (rounding) |\n| Qwen-7B 1v2 AUC | .6168 | exp_004_7b_crossscale[bootstrap_ci] | 0.6168 | MATCH |\n| Qwen-7B 1v2 CI | [.608,.626] | exp_004_7b_crossscale[bootstrap_ci] | [.6079,.6261] | MATCH (rounding) |\n| Qwen-7B 2v3 AUC | .5492 | exp_004_7b_crossscale[bootstrap_ci] | 0.5492 | MATCH |\n| Qwen-7B 2v3 CI | [.539,.559] | exp_004_7b_crossscale[bootstrap_ci] | [.5388,.5594] | MATCH (rounding) |\n| Qwen-7B 3v4 AUC | .5276 | exp_004_7b_crossscale[bootstrap_ci] | 0.5276 | MATCH |\n| Qwen-7B 4v5 AUC | .5085 | exp_004_7b_crossscale[bootstrap_ci] | 0.5085 | MATCH |\n\n---\n\n### Extended Table (tab:kstar_ci_extended) — 5 Additional Models\n\nAll Qwen-base (exp_016_base_vs_instruct) and LLaMA-8B (exp_018_llama8b_depth) values — both AUC and all 5 CI pairs — match exactly (within 3-decimal rounding). All Pythia-6.9B (exp_pythia69b_c4_nuc) AUC values match. Gemma-2B (exp_gemma2b_depth) all AUC values match; only 1v2 CI is in the registry and it matches.\n\n**Mismatches and gaps in the extended table:**\n\n| Location | Paper Value | Registry exp_id | Registry Value | Match? |\n|---|---|---|---|---|\n| **Mistral-7B 0v1 AUC** | **.9170** | exp_019_mistral7b_depth (self) | 0.9843 | **MISMATCH (−0.067)** |\n| **Mistral-7B 0v1 AUC** | **.9170** | exp_019b_mistral_cross_scorer | 0.9209 | **MISMATCH (−0.004)** |\n| **Mistral-7B 1v2 AUC** | **.5750** | exp_019_mistral7b_depth (self) | 0.5935 | **MISMATCH (−0.019)** |\n| **Mistral-7B 1v2 AUC** | **.5750** | exp_019b_mistral_cross_scorer | 0.5695 | **MISMATCH (−0.006)** |\n| **Mistral-7B 2v3 AUC** | **.5369** | exp_019_mistral7b_depth (self) | 0.5402 | **MISMATCH (−0.003)** |\n| **Mistral-7B 2v3 AUC** | **.5369** | exp_019b_mistral_cross_scorer | 0.5335 | **MISMATCH (+0.003)** |\n| **Mistral-7B 3v4 AUC** | **.5174** | exp_019_mistral7b_depth (self) | 0.5232 | **MISMATCH (−0.006)** |\n| **Mistral-7B 3v4 AUC** | **.5174** | exp_019b_mistral_cross_scorer | 0.5140 | **MISMATCH (+0.003)** |\n| Mistral-7B 4v5 AUC | .5175 | both exp_019/019b | .5181/.5184 | MATCH (~rounding) |\n| **Gemma-2B 0v1 CI** | **[.949,.957]** | **(no registry record)** | **N/A** | **NOT IN REGISTRY** |\n| Gemma-2B 1v2 CI | [.588,.608] | exp_gemma2b_depth | [.5882,.6076] | MATCH (rounding) |\n| **Gemma-2B 2v3 CI** | **[.523,.545]** | **(no registry record)** | **N/A** | **NOT IN REGISTRY** |\n| **Gemma-2B 3v4 CI** | **[.492,.514]** | **(no registry record)** | **N/A** | **NOT IN REGISTRY** |\n| **Gemma-2B 4v5 CI** | **[.492,.514]** | **(no registry record)** | **N/A** | **NOT IN REGISTRY** |\n\n---\n\n### Summary of All Issues\n\n**Genuine mismatches (AUC values differ from all registry experiments):**\n\n1. **OLMo 3v4 AUC**: paper=.5024, registry=0.5034 (diff=+0.001). Discrepancy is small but consistent — the registry was updated 2026-05-22 with cross-scored values (D107 update), and the paper number may be from an earlier snapshot.\n\n2. **OLMo 4v5 AUC**: paper=.4942, registry=0.4971 (diff=+0.003). Same root cause as OLMo 3v4.\n\n3. **Mistral-7B 0v1 AUC**: paper=.9170. Self-scorer experiment (exp_019) gives 0.9843; cross-scorer experiment (exp_019b) gives 0.9209. Neither matches. The paper value .9170 does not correspond to any registry experiment. This is the largest unexplained discrepancy.\n\n4. **Mistral-7B 1v2 AUC**: paper=.5750. Self-scorer=0.5935, cross-scorer=0.5695. Neither matches. No registry entry has this value.\n\n5. **Mistral-7B 2v3–3v4 AUC**: paper values (.5369, .5174) coincidentally equal the arithmetic average of self+cross-scorer for 2v3 (exactly: (0.5402+0.5335)/2=0.5369) but not for 3v4 (avg=0.5186 vs paper=0.5174). There is no registry experiment that produced these values directly.\n\n**CIs in paper with no matching registry record (bootstrap was run but not logged):**\n\n- Pythia 2v3 CI [.534,.554] — exp_001 only has bootstrap_ci for 1v2, not 2v3\n- OLMo 1v2 CI [.496,.519] — exp_002 has no bootstrap_ci at all\n- OLMo 2v3 CI [.486,.509] — same\n- Gemma-2B 0v1 CI [.949,.957], 2v3 CI [.523,.545], 3v4 CI [.492,.514], 4v5 CI [.492,.514] — exp_gemma2b_depth only logged bootstrap_ci_1v2\n\nThese CI values are internally plausible (the AUC point estimates match), but the bootstrap runs that produced them are not recorded in the registry."
      }
    ],
    "totalDurationMs": 650361,
    "totalTokens": 93670,
    "totalToolUseCount": 38,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8572,
      "cache_read_input_tokens": 81640,
      "output_tokens": 3457,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8572
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3457,
          "cache_read_input_tokens": 81640,
          "cache_creation_input_tokens": 8572,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8572,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 1,
      "bashCount": 35,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---


### System

_source line 664_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf8202b98a7a15f0",
  "tool_use_id": "toolu_018tQpraGEn5S4TsCg74MpUC",
  "description": "Running python3 -c \"\nfrom decimal import Decimal, ROUND_HA…",
  "usage": {
    "total_tokens": 86624,
    "tool_uses": 58,
    "duration_ms": 636460
  },
  "last_tool_name": "Bash",
  "uuid": "b57abe04-ef3f-4b12-954b-362f5f049c00",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff"
}
```

---


### Tool call

_source line 665_

<details open><summary>🔧 Tool call — Bash · `toolu_01H8DAAHMtUX1pbQayocuVBw`</summary>

```json
{
  "command": "python3 -c \"\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\n# The paper displays 0.640 for Pythia CI lower (3 decimal places shown as .640)\n# But round_standard(0.6401, 3) = 0.640 (displayed without trailing zero: 0.64)\n# In the paper context 0.640 = 0.64 -- they're the same\n\n# Now let's verify: is the CI lower 0.640 in the paper exact?\n# Inline: '0.655 [0.640, 0.669]'\n# Registry: ci_lower=0.6401, ci_upper=0.6688\n# 0.6401 -> 0.640 OK, 0.6688 -> 0.669 OK -- MATCH\n\n# Final verification table for all inline claims:\nprint('=== INLINE CLAIMS FINAL VERIFICATION ===')\nprint()\nprint('Claim 1: Qwen arXiv 2v3 = 0.644 [0.628, 0.658]')\nprint('  Registry (exp_024): auc=0.6427, CI=[0.6275, 0.6575]')\nprint(f'  AUC: 0.6427 rounds to {round_standard(0.6427, 3)} -- paper says 0.644 -- MISMATCH')\nprint(f'  CI lower: 0.6275 -> {round_standard(0.6275, 3)} -- paper says 0.628 -- OK')\nprint(f'  CI upper: 0.6575 -> {round_standard(0.6575, 3)} -- paper says 0.658 -- OK')\nprint()\nprint('Claim 2: Pythia arXiv 2v3 = 0.655 [0.640, 0.669]')\nprint('  Registry (exp_025): auc=0.6545, CI=[0.6401, 0.6688]')\nprint(f'  AUC: 0.6545 rounds to {round_standard(0.6545, 3)} -- paper says 0.655 -- OK')\nprint(f'  CI lower: 0.6401 -> {round_standard(0.6401, 3)} -- paper says 0.640 -- OK')\nprint(f'  CI upper: 0.6688 -> {round_standard(0.6688, 3)} -- paper says 0.669 -- OK')\nprint()\nprint('Claim 3: LLaMA-8B arXiv 2v3 = 0.620 [0.605, 0.635]')\nprint('  Registry (exp_arXiv_llama8b): auc=0.6215, CI=NOT STORED')\nprint(f'  AUC: 0.6215 rounds to {round_standard(0.6215, 3)} -- paper says 0.620 -- MISMATCH')\nprint('  CI: not verifiable (no bootstrap CI in registry)')\nprint()\nprint('Claim 4: arXiv 1v2 JSD = 0.077 vs ~0.01 for C4')\nprint('  Registry arXiv 1v2 JSD values: LLaMA=0.0785, Mistral=0.0762, Pythia=0.0573')\nprint('  No single experiment has JSD=0.077 for arXiv 1v2')\nprint('  Closest: Mistral 0.0762 (rounds to 0.076 NOT 0.077)')\nprint('  C4 JSD ~0.01: exp_016=0.01081 -- OK')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018tQpraGEn5S4TsCg74MpUC",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "e0d99d87-c807-48fb-b0b4-87039f123930",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019tBFXjAbrt9T7JR8rJiFRj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 607,
      "cache_read_input_tokens": 83308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 607,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 666 · 2026-05-23T11:33:45.318Z_

<details><summary>↩ Tool result · `toolu_01H8DAAHMtUX1pbQayocuVBw`</summary>

```text
=== INLINE CLAIMS FINAL VERIFICATION ===

Claim 1: Qwen arXiv 2v3 = 0.644 [0.628, 0.658]
  Registry (exp_024): auc=0.6427, CI=[0.6275, 0.6575]
  AUC: 0.6427 rounds to 0.643 -- paper says 0.644 -- MISMATCH
  CI lower: 0.6275 -> 0.628 -- paper says 0.628 -- OK
  CI upper: 0.6575 -> 0.658 -- paper says 0.658 -- OK

Claim 2: Pythia arXiv 2v3 = 0.655 [0.640, 0.669]
  Registry (exp_025): auc=0.6545, CI=[0.6401, 0.6688]
  AUC: 0.6545 rounds to 0.655 -- paper says 0.655 -- OK
  CI lower: 0.6401 -> 0.64 -- paper says 0.640 -- OK
  CI upper: 0.6688 -> 0.669 -- paper says 0.669 -- OK

Claim 3: LLaMA-8B arXiv 2v3 = 0.620 [0.605, 0.635]
  Registry (exp_arXiv_llama8b): auc=0.6215, CI=NOT STORED
  AUC: 0.6215 rounds to 0.622 -- paper says 0.620 -- MISMATCH
  CI: not verifiable (no bootstrap CI in registry)

Claim 4: arXiv 1v2 JSD = 0.077 vs ~0.01 for C4
  Registry arXiv 1v2 JSD values: LLaMA=0.0785, Mistral=0.0762, Pythia=0.0573
  No single experiment has JSD=0.077 for arXiv 1v2
  Closest: Mistral 0.0762 (rounds to 0.076 NOT 0.077)
  C4 JSD ~0.01: exp_016=0.01081 -- OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018tQpraGEn5S4TsCg74MpUC",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "da70ee1f-7970-4f85-9b26-5b04c0cfa832"
}
```

</details>

---


### System

_source line 667_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acccdabc14ba72457",
  "tool_use_id": "toolu_01VV28GHoAcAmcY7y7PyWkcR",
  "description": "Running python3 -c \"\n# Summary of all findings for final r…",
  "usage": {
    "total_tokens": 123868,
    "tool_uses": 51,
    "duration_ms": 627682
  },
  "last_tool_name": "Bash",
  "uuid": "5c561848-4e6e-4d21-9bcb-9736b01b1e51",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff"
}
```

---


### Tool call

_source line 668_

<details open><summary>🔧 Tool call — Bash · `toolu_01Rsy5MQ49ATLRY7k4WTR6a7`</summary>

```json
{
  "command": "python3 -c \"\n# Summary of all findings for final report\nprint('='*80)\nprint('AUDIT SUMMARY')\nprint('='*80)\nprint()\nprint('TASK 1: Filtering results (experiments_c3.tex)')\nprint('-'*50)\nprint()\nprint('Tab filtering_main.tex: ALL entries MATCH registry (exp_006_graduated_filtering)')\nprint()\nprint('Inline numbers:')\nprint()\nprint('1. -1.53 pp (no-filter MMLU degradation from base):')\nprint('   Base=0.6018, no_filter=0.5865 => (0.5865-0.6018)*100 = -1.53 pp')\nprint('   Registry: exact match ✓')\nprint()\nprint('2. -0.77 pp (binary-ours MMLU degradation):')\nprint('   Base=0.6018, binary_ours=0.5941 => (0.5941-0.6018)*100 = -0.77 pp')\nprint('   Registry: exact match ✓')\nprint()\nprint('3. ~50% reduction:')\nprint('   (1.53-0.77)/1.53 = 49.7% ≈ 50%')\nprint('   Registry: matches ✓')\nprint()\nprint('4. p_corr < 0.05 vs all alternatives (binary-ours MMLU):')\nprint('   exp_E_paired_stats: binary_ours_vs_all_mmlu=all significant')\nprint('   tab_pairwise_significance: all p < .05 for binary-ours vs all ✓')\nprint()\nprint('5. p_corr = 1.00 (graduated a=0.9 vs binary-ours on HellaSwag):')\nprint('   tab_pairwise_significance: HellaSwag delta=0.00, p=1.00 ✓')\nprint()\nprint('6. p_corr = 0.011 (graduated a=0.9 vs binary-ours on MMLU):')\nprint('   tab_pairwise_significance: MMLU p=.011 ✓')\nprint()\nprint()\nprint('TASK 2: Introduction numbers')\nprint('-'*50)\nprint()\nprint('1. MMLU 0.5941 vs base 0.6018:')\nprint('   Registry binary_ours MMLU: 0.5941 ✓')\nprint('   Registry base_model MMLU: 0.6018 ✓')\nprint()\nprint('2. p <= 0.002 for K*=2 configurations:')\nprint('   exp_007_bootstrap_ci: all K*=2 perm_p = 0.002 ✓')\nprint()\nprint()\nprint('TASK 3: Discussion numbers')\nprint('-'*50)\nprint()\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VV28GHoAcAmcY7y7PyWkcR",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "ebaf779b-903c-4a74-8a5d-58b4dc815160",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YbfAafi6jq3yxXyXEMgWph",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 120830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1006,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-23T11:33:50.022Z_

<details><summary>↩ Tool result · `toolu_01Rsy5MQ49ATLRY7k4WTR6a7`</summary>

```text
================================================================================
AUDIT SUMMARY
================================================================================

TASK 1: Filtering results (experiments_c3.tex)
--------------------------------------------------

Tab filtering_main.tex: ALL entries MATCH registry (exp_006_graduated_filtering)

Inline numbers:

1. -1.53 pp (no-filter MMLU degradation from base):
   Base=0.6018, no_filter=0.5865 => (0.5865-0.6018)*100 = -1.53 pp
   Registry: exact match ✓

2. -0.77 pp (binary-ours MMLU degradation):
   Base=0.6018, binary_ours=0.5941 => (0.5941-0.6018)*100 = -0.77 pp
   Registry: exact match ✓

3. ~50% reduction:
   (1.53-0.77)/1.53 = 49.7% ≈ 50%
   Registry: matches ✓

4. p_corr < 0.05 vs all alternatives (binary-ours MMLU):
   exp_E_paired_stats: binary_ours_vs_all_mmlu=all significant
   tab_pairwise_significance: all p < .05 for binary-ours vs all ✓

5. p_corr = 1.00 (graduated a=0.9 vs binary-ours on HellaSwag):
   tab_pairwise_significance: HellaSwag delta=0.00, p=1.00 ✓

6. p_corr = 0.011 (graduated a=0.9 vs binary-ours on MMLU):
   tab_pairwise_significance: MMLU p=.011 ✓


TASK 2: Introduction numbers
--------------------------------------------------

1. MMLU 0.5941 vs base 0.6018:
   Registry binary_ours MMLU: 0.5941 ✓
   Registry base_model MMLU: 0.6018 ✓

2. p <= 0.002 for K*=2 configurations:
   exp_007_bootstrap_ci: all K*=2 perm_p = 0.002 ✓


TASK 3: Discussion numbers
--------------------------------------------------
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VV28GHoAcAmcY7y7PyWkcR",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "5793e9fd-e94d-4ef5-a058-967a2b72fc2a"
}
```

</details>

---


### System

_source line 670_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a409a6aeb060f7eee",
  "tool_use_id": "toolu_01VA6RDVEYrmJqYoJVqwAcxJ",
  "description": "Running python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.c…",
  "usage": {
    "total_tokens": 84372,
    "tool_uses": 48,
    "duration_ms": 614059
  },
  "last_tool_name": "Bash",
  "uuid": "f87467b9-5820-4ae5-ad29-31399d6c4d6c",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff"
}
```

---


### Tool call

_source line 671_

<details open><summary>🔧 Tool call — Bash · `toolu_01NV1mVQ1wGx2TBXFnhnEPJn`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# exp_007 OLMo values are self-scored, paper Table S8 shows Qwen cross-scored values (matching exp_002)\n# The CIs in Table S8 for OLMo must come from a bootstrap run not captured in the registry\n\n# Now let's compile the complete audit table for final output\n# Including all tasks with clear verdicts\n\nprint('=== COMPLETE AUDIT TABLE ===')\nprint()\n\nrows = []\n\n# TASK 1: Table S2 (exp_003) - all 20 values matched\nrows.append(('Task 1 summary', 'S2 AUC (all 20 cells)', 'All match', 'exp_003', 'All match', 'OK'))\n\n# TASK 2: Table S8 (exp_007 for Qwen-rw, Qwen-cont; exp_002 for OLMo AUC; mixed for Pythia)\nrows.append(('Task 2', 'S8 Qwen-rw all 5 pairs', 'All match exp_007', 'exp_007', 'All match', 'OK'))\nrows.append(('Task 2', 'S8 Pythia 0v1=.993', '0.993[.992,.994]', 'exp_007', '0.9932[0.9921,0.9943]', 'OK'))\nrows.append(('Task 2', 'S8 Pythia 1v2=.607', '0.607[.598,.617]', 'exp_007', '0.6539[0.6454,0.6630]', 'MISMATCH'))\nrows.append(('Task 2', 'S8 Pythia 1v2=.607 vs exp_001', '0.607[.598,.617]', 'exp_001 cross-scored', '0.6074 (no CI stored)', 'PARTIAL MATCH (AUC only)'))\nrows.append(('Task 2', 'S8 Pythia 2v3=.551', '0.551[.542,.563]', 'exp_007', '0.5514[0.5417,0.5628]', 'OK'))\nrows.append(('Task 2', 'S8 Pythia 3v4=.515', '0.515[.504,.526]', 'exp_007', '0.5152[0.5041,0.5260]', 'OK'))\nrows.append(('Task 2', 'S8 Pythia 4v5=.514', '0.514[.502,.525]', 'exp_007', '0.5136[0.5021,0.5249]', 'OK'))\nrows.append(('Task 2', 'S8 OLMo 0v1=.986', '.986[.984,.988]', 'exp_007', '0.9970[0.9964,0.9975]', 'MISMATCH'))\nrows.append(('Task 2', 'S8 OLMo 0v1=.986', '.986[.984,.988]', 'exp_002 cross-scored', '0.9861 (no CI)', 'AUC matches, CI unverified'))\nrows.append(('Task 2', 'S8 OLMo 1v2=.500', '.500[.496,.519]', 'exp_007', '0.6145[0.6045,0.6247]', 'MISMATCH'))\nrows.append(('Task 2', 'S8 OLMo 1v2=.500', '.500[.496,.519]', 'exp_002 cross-scored', '0.5001 (no CI)', 'AUC matches, CI unverified'))\nrows.append(('Task 2', 'S8 OLMo 2v3=.497', '.497[.486,.509]', 'exp_002 cross-scored', '0.4972 (no CI)', 'AUC matches, CI unverified'))\nrows.append(('Task 2', 'S8 OLMo 3v4=.502', '.502[.491,.513]', 'exp_002 cross-scored', '0.5034 (no CI)', 'AUC matches, CI unverified'))\nrows.append(('Task 2', 'S8 OLMo 4v5=.494', '.494[.483,.506]', 'exp_002 cross-scored', '0.4971 (no CI)', 'AUC matches, CI unverified'))\nrows.append(('Task 2', 'S8 Qwen-cont all 5 pairs', 'All match', 'exp_007', 'All match', 'OK'))\n\n# TASK 3: Neural probe (exp_015)\nrows.append(('Task 3', 'Qwen 2v3 AUC=0.6159', '0.6159', 'exp_015', '0.616', 'OK'))\nrows.append(('Task 3', 'Qwen K*=3', 'K*=3', 'exp_015', 'k_star_neural=3', 'OK'))\nrows.append(('Task 3', 'Pythia 2v3 AUC=0.5963', '0.5963', 'exp_015', '0.596', 'OK'))\nrows.append(('Task 3', 'Pythia K*=2', 'K*=2', 'exp_015', 'k_star_neural=2', 'OK'))\nrows.append(('Task 3', 'OLMo 2v3 AUC=0.5056', '0.5056', 'exp_015', '0.589', 'MISMATCH'))\nrows.append(('Task 3', 'OLMo 1v2=0.5054', '0.5054', 'exp_015', '0.657', 'MISMATCH'))\nrows.append(('Task 3', 'OLMo K*=1', 'K*=1', 'exp_015', 'k_star_neural=2', 'MISMATCH'))\n\n# Task 3 CI bounds from exp_015 - note that registry has no CI for neural probe\nrows.append(('Task 3', 'Qwen 2v3 CI [0.610,0.622]', '[0.610,0.622]', 'exp_015', 'No CI stored', 'UNVERIFIABLE'))\nrows.append(('Task 3', 'Pythia 2v3 CI [0.589,0.603]', '[0.589,0.603]', 'exp_015', 'No CI stored', 'UNVERIFIABLE'))\nrows.append(('Task 3', 'OLMo 2v3 CI [0.497,0.516]', '[0.497,0.516]', 'exp_015', 'No CI stored', 'UNVERIFIABLE'))\n\nprint(f'{'Location':<40} {'Paper Value':<30} {'Exp ID':<20} {'Registry Value':<35} Match')\nprint('-' * 130)\nfor task, loc, paper, exp_id, reg, match in rows:\n    print(f'{loc:<40} {paper:<30} {exp_id:<20} {reg:<35} {match}')\n\" 2>&1\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VA6RDVEYrmJqYoJVqwAcxJ",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "dd74954e-aeb8-46b9-865c-ae7191dfca84",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LGDZjNTHiu8yjSqBQtRpJV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 80968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1070,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 672 · 2026-05-23T11:33:56.374Z_

<details><summary>↩ Tool result · `toolu_01NV1mVQ1wGx2TBXFnhnEPJn`</summary>

```text
=== COMPLETE AUDIT TABLE ===

Location                                 Paper Value                    Exp ID               Registry Value                      Match
----------------------------------------------------------------------------------------------------------------------------------
S2 AUC (all 20 cells)                    All match                      exp_003              All match                           OK
S8 Qwen-rw all 5 pairs                   All match exp_007              exp_007              All match                           OK
S8 Pythia 0v1=.993                       0.993[.992,.994]               exp_007              0.9932[0.9921,0.9943]               OK
S8 Pythia 1v2=.607                       0.607[.598,.617]               exp_007              0.6539[0.6454,0.6630]               MISMATCH
S8 Pythia 1v2=.607 vs exp_001            0.607[.598,.617]               exp_001 cross-scored 0.6074 (no CI stored)               PARTIAL MATCH (AUC only)
S8 Pythia 2v3=.551                       0.551[.542,.563]               exp_007              0.5514[0.5417,0.5628]               OK
S8 Pythia 3v4=.515                       0.515[.504,.526]               exp_007              0.5152[0.5041,0.5260]               OK
S8 Pythia 4v5=.514                       0.514[.502,.525]               exp_007              0.5136[0.5021,0.5249]               OK
S8 OLMo 0v1=.986                         .986[.984,.988]                exp_007              0.9970[0.9964,0.9975]               MISMATCH
S8 OLMo 0v1=.986                         .986[.984,.988]                exp_002 cross-scored 0.9861 (no CI)                      AUC matches, CI unverified
S8 OLMo 1v2=.500                         .500[.496,.519]                exp_007              0.6145[0.6045,0.6247]               MISMATCH
S8 OLMo 1v2=.500                         .500[.496,.519]                exp_002 cross-scored 0.5001 (no CI)                      AUC matches, CI unverified
S8 OLMo 2v3=.497                         .497[.486,.509]                exp_002 cross-scored 0.4972 (no CI)                      AUC matches, CI unverified
S8 OLMo 3v4=.502                         .502[.491,.513]                exp_002 cross-scored 0.5034 (no CI)                      AUC matches, CI unverified
S8 OLMo 4v5=.494                         .494[.483,.506]                exp_002 cross-scored 0.4971 (no CI)                      AUC matches, CI unverified
S8 Qwen-cont all 5 pairs                 All match                      exp_007              All match                           OK
Qwen 2v3 AUC=0.6159                      0.6159                         exp_015              0.616                               OK
Qwen K*=3                                K*=3                           exp_015              k_star_neural=3                     OK
Pythia 2v3 AUC=0.5963                    0.5963                         exp_015              0.596                               OK
Pythia K*=2                              K*=2                           exp_015              k_star_neural=2                     OK
OLMo 2v3 AUC=0.5056                      0.5056                         exp_015              0.589                               MISMATCH
OLMo 1v2=0.5054                          0.5054                         exp_015              0.657                               MISMATCH
OLMo K*=1                                K*=1                           exp_015              k_star_neural=2                     MISMATCH
Qwen 2v3 CI [0.610,0.622]                [0.610,0.622]                  exp_015              No CI stored                        UNVERIFIABLE
Pythia 2v3 CI [0.589,0.603]              [0.589,0.603]                  exp_015              No CI stored                        UNVERIFIABLE
OLMo 2v3 CI [0.497,0.516]                [0.497,0.516]                  exp_015              No CI stored                        UNVERIFIABLE
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VA6RDVEYrmJqYoJVqwAcxJ",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "c91bb984-c1d4-4687-99aa-6e9798d1e4f5"
}
```

</details>

---


### System

_source line 673_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a409a6aeb060f7eee",
  "tool_use_id": "toolu_01VA6RDVEYrmJqYoJVqwAcxJ",
  "description": "Running python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.c…",
  "usage": {
    "total_tokens": 87595,
    "tool_uses": 49,
    "duration_ms": 632705
  },
  "last_tool_name": "Bash",
  "uuid": "450461a8-c700-4bc0-a2c8-5dd2d36df718",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff"
}
```

---


### Tool call

_source line 674_

<details open><summary>🔧 Tool call — Bash · `toolu_01FDwU3NTGigGQTK3VWFzvV2`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# Final check: Task 2 note about Pythia 2v3\n# Task says: 'Table S8 Pythia 2v3 says .551 but Table 1 says .5440. Check which is in registry.'\n# Answer: registry has TWO different values:\n# exp_007 (self-scored): 2v3=0.5514 -> this rounds to .551 (Table S8)\n# exp_001 (Qwen cross-scored): 2v3=0.544 -> this rounds to .544 (Table 1)\n# Both are in the registry, but for different scorer setups\n\nprint('Pythia 2v3 disambiguation:')\nprint(f'  exp_007 (self-scored): 2v3_auc = {exps[\\\"exp_007_bootstrap_ci\\\"][\\\"metrics\\\"][\\\"pythia_cont\\\"][\\\"2v3\\\"][\\\"auc\\\"]:.4f} -> rounds to .551 (Table S8)')\nprint(f'  exp_001 (Qwen cross-scored): 2v3_auc = {exps[\\\"exp_001_pythia_depth\\\"][\\\"metrics\\\"][\\\"pairwise_auc\\\"][\\\"2v3\\\"]:.4f} -> rounds to .544 (Table 1)')\nprint()\nprint('=> Table S8 uses exp_007 self-scored data (consistent for 0v1, 2v3, 3v4, 4v5)')\nprint('=> Table 1 uses exp_001 Qwen cross-scored data')\nprint('=> BUT Table S8 Pythia 1v2=.607 comes from cross-scored data (exp_001), NOT exp_007')\nprint()\n\n# Also verify the exp_020 vs S10 patterns more carefully\n# The issue is that multiple values in S10 are off by 1-8 thousandths from exp_020\n# This could indicate: (a) a different run of exp020, (b) post-hoc correction, \n# or (c) the paper uses bootstrap mean vs OOF AUC\nexp020 = exps['exp_020_pythia_decoding']\nprint('exp020 notes excerpt:')\nnotes = exp020.get('notes', '')\nprint(notes[:500])\n\" 2>&1\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01VA6RDVEYrmJqYoJVqwAcxJ",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "462d8c19-0ef1-401b-8c34-b5fac5af9bf6",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LBEfhQdxenGi8Qq598zg1U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3221,
      "cache_read_input_tokens": 82038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3221,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-23T11:34:14.983Z_

<details><summary>↩ Tool result · `toolu_01FDwU3NTGigGQTK3VWFzvV2`</summary>

```text
Pythia 2v3 disambiguation:
  exp_007 (self-scored): 2v3_auc = 0.5514 -> rounds to .551 (Table S8)
  exp_001 (Qwen cross-scored): 2v3_auc = 0.5440 -> rounds to .544 (Table 1)

=> Table S8 uses exp_007 self-scored data (consistent for 0v1, 2v3, 3v4, 4v5)
=> Table 1 uses exp_001 Qwen cross-scored data
=> BUT Table S8 Pythia 1v2=.607 comes from cross-scored data (exp_001), NOT exp_007

exp020 notes excerpt:
greedy 1v2 AUC=0.8838 调查完成：根因为 Pythia-1.4B greedy 级联重复坍塌（4-gram repeat rate: d0=0.01→d1=0.72→d2=0.81; TTR: d0=0.72→d1=0.19→d2=0.14）。hapax_ratio (d=1.06) 和 low_freq_ratio (d=1.03) 是 top 贡献特征。非 bug，参数正确，无数据泄漏。K*=2 不受影响。建议论文标注为 repetition-dominated regime。| Bootstrap CI (10000 iter): t07 2v3 AUC=0.5939 CI [0.5855, 0.6025] BORDERLINE (CI upper crosses θ); t12 1v2 AUC=0.6170 CI [0.6071, 0.6270] PASS。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01VA6RDVEYrmJqYoJVqwAcxJ",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "6f16eb19-a97e-49e7-8b34-17dcd3b0dba9"
}
```

</details>

---


### System

_source line 676_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "acf8202b98a7a15f0",
  "tool_use_id": "toolu_018tQpraGEn5S4TsCg74MpUC",
  "status": "completed",
  "output_file": "",
  "summary": "Audit Table 4 domain + code experiments",
  "usage": {
    "total_tokens": 88215,
    "tool_uses": 58,
    "duration_ms": 671213
  },
  "uuid": "5ee4c649-5db1-4a0c-9f8f-d08a9b9bdff4",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff"
}
```

---


### Tool result

_source line 677 · 2026-05-23T11:34:19.996Z_

<details><summary>↩ Tool result · `toolu_018tQpraGEn5S4TsCg74MpUC`</summary>

```text
Here is the complete audit report.

---

## Audit Report: Domain Ablation / Cross-Domain Evaluation

### Registry Experiments Found

| Paper Row | Registry exp_id | Status |
|---|---|---|
| arXiv / Qwen-1.5B | `exp_024_arxiv_domain` | DONE |
| arXiv / Pythia-1.4B | `exp_025_pythia_arxiv` | DONE |
| C4 / Qwen-1.5B | `exp_016_base_vs_instruct` | DONE |
| Wiki / Qwen-1.5B | `exp_023_domain_ablation` | DONE (incomplete metrics) |
| Code / Qwen-1.5B | `exp_code_qwen1b5` | DONE |
| Code / LLaMA-8B | `exp_code_llama8b` | DONE |
| LLaMA-8B arXiv inline | `exp_arXiv_llama8b` | DONE (no CI stored) |
| Table S12 C4 | `exp_017_qwen_continuation` | DONE |

---

### Table 4 (tab:domain_kstar) Verification

| Location | Paper Value | Registry exp_id | Registry Value | Match? |
|---|---|---|---|---|
| Tab4 arXiv/Qwen-1.5B 1v2 AUC | .858 | exp_024 | 0.858 | OK |
| Tab4 arXiv/Qwen-1.5B 2v3 AUC | .644 | exp_024 | 0.6427 (rounds to .643) | **MISMATCH** |
| Tab4 arXiv/Qwen-1.5B K* | 3 | exp_024 | 3 | OK |
| Tab4 arXiv/Pythia-1.4B 1v2 AUC | .805 | exp_025 | 0.8047 (rounds to .805) | OK |
| Tab4 arXiv/Pythia-1.4B 2v3 AUC | .655 | exp_025 | 0.6545 (rounds to .655) | OK |
| Tab4 arXiv/Pythia-1.4B K* | 3 | exp_025 | 3 | OK |
| Tab4 C4/Qwen-1.5B 1v2 AUC | .626 | exp_016 | 0.6262 (rounds to .626) | OK |
| Tab4 C4/Qwen-1.5B 2v3 AUC | .550 | exp_016 | 0.5496 (rounds to .550) | OK |
| Tab4 C4/Qwen-1.5B K* | 2 | exp_016 | 2 | OK |
| Tab4 Wiki/Qwen-1.5B 1v2 AUC | .619 | exp_023 | 0.6193 (rounds to .619) | OK |
| Tab4 Wiki/Qwen-1.5B 2v3 AUC | .550 | exp_023 | 0.5498 (rounds to .550) | OK |
| Tab4 Wiki/Qwen-1.5B K* | 2 | exp_023 | 2 | OK |
| Tab4 Code/Qwen-1.5B 1v2 AUC | .738 | exp_code_qwen1b5 | 0.7382 (rounds to .738) | OK |
| Tab4 Code/Qwen-1.5B 2v3 AUC | .530 | exp_code_qwen1b5 | 0.53 | OK |
| Tab4 Code/Qwen-1.5B K* | 2 | exp_code_qwen1b5 | 2 | OK |
| Tab4 Code/LLaMA-8B 1v2 AUC | .739 | exp_code_llama8b | 0.7394 (rounds to .739) | OK |
| Tab4 Code/LLaMA-8B 2v3 AUC | .510 | exp_code_llama8b | 0.5112 (rounds to .511) | **MISMATCH** |
| Tab4 Code/LLaMA-8B K* | 2 | exp_code_llama8b | 2 | OK |

---

### Table S12 (tab:s12_domain_ablation) Verification

Table S12 uses `exp_017` (Qwen-1.5B-**Instruct** continuation) for the C4 column and `exp_024` for arXiv. Note: the S12 caption calls the model "Qwen-cont" but `exp_017` is the Instruct variant, whereas Table 4's C4/Qwen row uses `exp_016` (base variant). This is internally consistent with the paper labeling, not a numerical error.

| Location | Paper Value | Registry exp_id | Registry Value | Match? |
|---|---|---|---|---|
| S12 C4 0v1 | .997 | exp_017 | 0.9972 (rounds to .997) | OK |
| S12 C4 1v2 | .611 | exp_017 | 0.6114 (rounds to .611) | OK |
| S12 C4 2v3 | .561 | exp_017 | 0.5609 (rounds to .561) | OK |
| S12 C4 3v4 | .541 | exp_017 | 0.5408 (rounds to .541) | OK |
| S12 C4 4v5 | .514 | exp_017 | 0.5139 (rounds to .514) | OK |
| S12 Wiki 0v1 | .996 | exp_023 | NOT IN REGISTRY | UNVERIFIABLE |
| S12 Wiki 1v2 | .619 | exp_023 | 0.6193 (rounds to .619) | OK |
| S12 Wiki 2v3 | .550 | exp_023 | 0.5498 (rounds to .550) | OK |
| S12 Wiki 3v4 | .523 | exp_023 | NOT IN REGISTRY | UNVERIFIABLE |
| S12 Wiki 4v5 | .514 | exp_023 | NOT IN REGISTRY | UNVERIFIABLE |
| S12 arXiv 0v1 | .995 | exp_024 | 0.9946 (rounds to .995) | OK |
| S12 arXiv 1v2 | .858 | exp_024 | 0.858 | OK |
| S12 arXiv 2v3 | .644 | exp_024 | 0.6427 (rounds to .643) | **MISMATCH** |
| S12 arXiv 3v4 | .544 | exp_024 | 0.5437 (rounds to .544) | OK |
| S12 arXiv 4v5 | .530 | exp_024 | 0.5294 (rounds to .529) | **MISMATCH** |

---

### Inline Claims Verification

| Location | Paper Value | Registry exp_id | Registry Value | Match? |
|---|---|---|---|---|
| Inline: Qwen arXiv 2v3 AUC | 0.644 | exp_024 | 0.6427 (rounds to .643) | **MISMATCH** |
| Inline: Qwen arXiv 2v3 CI lower | 0.628 | exp_024 | 0.6275 (rounds to .628) | OK |
| Inline: Qwen arXiv 2v3 CI upper | 0.658 | exp_024 | 0.6575 (rounds to .658) | OK |
| Inline: Pythia arXiv 2v3 AUC | 0.655 | exp_025 | 0.6545 (rounds to .655) | OK |
| Inline: Pythia arXiv 2v3 CI lower | 0.640 | exp_025 | 0.6401 (rounds to .640) | OK |
| Inline: Pythia arXiv 2v3 CI upper | 0.669 | exp_025 | 0.6688 (rounds to .669) | OK |
| Inline: LLaMA-8B arXiv 2v3 AUC | 0.620 | exp_arXiv_llama8b | 0.6215 (rounds to .622) | **MISMATCH** |
| Inline: LLaMA-8B arXiv 2v3 CI | [0.605, 0.635] | exp_arXiv_llama8b | NOT STORED | UNVERIFIABLE |
| Inline: arXiv 1v2 JSD | 0.077 | (none) | No experiment stores 0.077; nearest are Mistral=0.0762, LLaMA=0.0785 | **UNRESOLVED** |
| Inline: C4 1v2 JSD | ~0.01 | exp_016 | 0.01081 | OK |

---

### Confirmed Mismatches (4 numerical, 1 unresolved)

1. **arXiv/Qwen-1.5B 2v3 AUC**: Paper says `.644`, registry `exp_024` stores `0.6427` which rounds to `.643`. Appears in Table 4, Table S12, and twice in inline text. Delta = 0.001.

2. **Code/LLaMA-8B 2v3 AUC**: Paper says `.510`, registry `exp_code_llama8b` stores `0.5112` which rounds to `.511`. Delta = 0.001.

3. **S12 arXiv 4v5 AUC**: Paper says `.530`, registry `exp_024` stores `0.5294` which rounds to `.529`. Delta = 0.001.

4. **Inline LLaMA-8B arXiv 2v3 AUC**: Paper says `0.620`, registry `exp_arXiv_llama8b` stores `0.6215` which rounds to `0.622`. Delta = 0.002. Bootstrap CI for this claim is not stored in the registry and cannot be verified.

5. **arXiv 1v2 JSD = 0.077**: No registry experiment stores exactly 0.077 for arXiv 1v2 JSD. The nearest single values are `exp_arXiv_mistral7b` (0.0762) and `exp_arXiv_llama8b` (0.0785). The 0.077 figure may be an informal average or rounded estimate; its exact provenance is unresolved.

**Unverifiable (registry incomplete)**: Wiki 0v1, 3v4, 4v5 for S12 (exp_023 only stores 1v2 and 2v3); LLaMA-8B arXiv CI bounds.

agentId: acf8202b98a7a15f0 (use SendMessage with to: 'acf8202b98a7a15f0' to continue this agent)
&lt;usage>total_tokens: 88327
tool_uses: 58
duration_ms: 671228&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "a1e3f79e-6edc-45ac-917e-d2b6635ca135",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are auditing numerical data in a research paper against experiment registry records.\n\nThe registry data is saved as JSON at:\n/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt\n\nThe format is `{\"result\": \"&lt;JSON string>\"}` — parse the inner JSON string to get experiment records.\n\nYour task: find experiments related to domain ablation / cross-domain evaluation. Look for exp_ids containing \"domain\", \"arxiv\", \"wiki\", \"code\", \"c4\". Relevant exp_ids may include: exp_024_arxiv_domain, exp_025_pythia_arxiv, exp_023_domain_ablation, exp_code_qwen1b5, exp_code_llama8b, or similar.\n\nCross-reference against Table 4 (tab:domain_kstar) in experiments_c1.tex:\n\n**Table 4 values**:\n| Domain | Model | 1v2 AUC | 2v3 AUC | K* |\n| arXiv | Qwen-1.5B | .858 | .644 | 3 |\n| arXiv | Pythia-1.4B | .805 | .655 | 3 |\n| C4 | Qwen-1.5B | .626 | .550 | 2 |\n| Wiki | Qwen-1.5B | .619 | .550 | 2 |\n| Code | Qwen-1.5B | .738 | .530 | 2 |\n| Code | LLaMA-8B | .739 | .510 | 2 |\n\nAlso verify Table S12 (tab:s12_domain_ablation) from appendix.tex:\n| | C4 | Wiki | arXiv |\n| 0v1 | .997 | .996 | .995 |\n| 1v2 | .611 | .619 | .858 |\n| 2v3 | .561 | .550 | .644 |\n| 3v4 | .541 | .523 | .544 |\n| 4v5 | .514 | .514 | .530 |\n(These are for Qwen-cont model)\n\nAlso check inline claims:\n- \"2v3 AUC = 0.644 [0.628, 0.658]\" for Qwen arXiv\n- \"0.655 [0.640, 0.669]\" for Pythia arXiv\n- \"0.620 [0.605, 0.635]\" for LLaMA-8B arXiv\n- \"1v2 JSD = 0.077 vs ~0.01 for C4\"\n\nFor each value, output a row:\n| Location | Paper Value | Registry exp_id | Registry Value | Match? |\n\nUse jq or python to parse the registry. Report all mismatches.",
    "agentId": "acf8202b98a7a15f0",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete audit report.\n\n---\n\n## Audit Report: Domain Ablation / Cross-Domain Evaluation\n\n### Registry Experiments Found\n\n| Paper Row | Registry exp_id | Status |\n|---|---|---|\n| arXiv / Qwen-1.5B | `exp_024_arxiv_domain` | DONE |\n| arXiv / Pythia-1.4B | `exp_025_pythia_arxiv` | DONE |\n| C4 / Qwen-1.5B | `exp_016_base_vs_instruct` | DONE |\n| Wiki / Qwen-1.5B | `exp_023_domain_ablation` | DONE (incomplete metrics) |\n| Code / Qwen-1.5B | `exp_code_qwen1b5` | DONE |\n| Code / LLaMA-8B | `exp_code_llama8b` | DONE |\n| LLaMA-8B arXiv inline | `exp_arXiv_llama8b` | DONE (no CI stored) |\n| Table S12 C4 | `exp_017_qwen_continuation` | DONE |\n\n---\n\n### Table 4 (tab:domain_kstar) Verification\n\n| Location | Paper Value | Registry exp_id | Registry Value | Match? |\n|---|---|---|---|---|\n| Tab4 arXiv/Qwen-1.5B 1v2 AUC | .858 | exp_024 | 0.858 | OK |\n| Tab4 arXiv/Qwen-1.5B 2v3 AUC | .644 | exp_024 | 0.6427 (rounds to .643) | **MISMATCH** |\n| Tab4 arXiv/Qwen-1.5B K* | 3 | exp_024 | 3 | OK |\n| Tab4 arXiv/Pythia-1.4B 1v2 AUC | .805 | exp_025 | 0.8047 (rounds to .805) | OK |\n| Tab4 arXiv/Pythia-1.4B 2v3 AUC | .655 | exp_025 | 0.6545 (rounds to .655) | OK |\n| Tab4 arXiv/Pythia-1.4B K* | 3 | exp_025 | 3 | OK |\n| Tab4 C4/Qwen-1.5B 1v2 AUC | .626 | exp_016 | 0.6262 (rounds to .626) | OK |\n| Tab4 C4/Qwen-1.5B 2v3 AUC | .550 | exp_016 | 0.5496 (rounds to .550) | OK |\n| Tab4 C4/Qwen-1.5B K* | 2 | exp_016 | 2 | OK |\n| Tab4 Wiki/Qwen-1.5B 1v2 AUC | .619 | exp_023 | 0.6193 (rounds to .619) | OK |\n| Tab4 Wiki/Qwen-1.5B 2v3 AUC | .550 | exp_023 | 0.5498 (rounds to .550) | OK |\n| Tab4 Wiki/Qwen-1.5B K* | 2 | exp_023 | 2 | OK |\n| Tab4 Code/Qwen-1.5B 1v2 AUC | .738 | exp_code_qwen1b5 | 0.7382 (rounds to .738) | OK |\n| Tab4 Code/Qwen-1.5B 2v3 AUC | .530 | exp_code_qwen1b5 | 0.53 | OK |\n| Tab4 Code/Qwen-1.5B K* | 2 | exp_code_qwen1b5 | 2 | OK |\n| Tab4 Code/LLaMA-8B 1v2 AUC | .739 | exp_code_llama8b | 0.7394 (rounds to .739) | OK |\n| Tab4 Code/LLaMA-8B 2v3 AUC | .510 | exp_code_llama8b | 0.5112 (rounds to .511) | **MISMATCH** |\n| Tab4 Code/LLaMA-8B K* | 2 | exp_code_llama8b | 2 | OK |\n\n---\n\n### Table S12 (tab:s12_domain_ablation) Verification\n\nTable S12 uses `exp_017` (Qwen-1.5B-**Instruct** continuation) for the C4 column and `exp_024` for arXiv. Note: the S12 caption calls the model \"Qwen-cont\" but `exp_017` is the Instruct variant, whereas Table 4's C4/Qwen row uses `exp_016` (base variant). This is internally consistent with the paper labeling, not a numerical error.\n\n| Location | Paper Value | Registry exp_id | Registry Value | Match? |\n|---|---|---|---|---|\n| S12 C4 0v1 | .997 | exp_017 | 0.9972 (rounds to .997) | OK |\n| S12 C4 1v2 | .611 | exp_017 | 0.6114 (rounds to .611) | OK |\n| S12 C4 2v3 | .561 | exp_017 | 0.5609 (rounds to .561) | OK |\n| S12 C4 3v4 | .541 | exp_017 | 0.5408 (rounds to .541) | OK |\n| S12 C4 4v5 | .514 | exp_017 | 0.5139 (rounds to .514) | OK |\n| S12 Wiki 0v1 | .996 | exp_023 | NOT IN REGISTRY | UNVERIFIABLE |\n| S12 Wiki 1v2 | .619 | exp_023 | 0.6193 (rounds to .619) | OK |\n| S12 Wiki 2v3 | .550 | exp_023 | 0.5498 (rounds to .550) | OK |\n| S12 Wiki 3v4 | .523 | exp_023 | NOT IN REGISTRY | UNVERIFIABLE |\n| S12 Wiki 4v5 | .514 | exp_023 | NOT IN REGISTRY | UNVERIFIABLE |\n| S12 arXiv 0v1 | .995 | exp_024 | 0.9946 (rounds to .995) | OK |\n| S12 arXiv 1v2 | .858 | exp_024 | 0.858 | OK |\n| S12 arXiv 2v3 | .644 | exp_024 | 0.6427 (rounds to .643) | **MISMATCH** |\n| S12 arXiv 3v4 | .544 | exp_024 | 0.5437 (rounds to .544) | OK |\n| S12 arXiv 4v5 | .530 | exp_024 | 0.5294 (rounds to .529) | **MISMATCH** |\n\n---\n\n### Inline Claims Verification\n\n| Location | Paper Value | Registry exp_id | Registry Value | Match? |\n|---|---|---|---|---|\n| Inline: Qwen arXiv 2v3 AUC | 0.644 | exp_024 | 0.6427 (rounds to .643) | **MISMATCH** |\n| Inline: Qwen arXiv 2v3 CI lower | 0.628 | exp_024 | 0.6275 (rounds to .628) | OK |\n| Inline: Qwen arXiv 2v3 CI upper | 0.658 | exp_024 | 0.6575 (rounds to .658) | OK |\n| Inline: Pythia arXiv 2v3 AUC | 0.655 | exp_025 | 0.6545 (rounds to .655) | OK |\n| Inline: Pythia arXiv 2v3 CI lower | 0.640 | exp_025 | 0.6401 (rounds to .640) | OK |\n| Inline: Pythia arXiv 2v3 CI upper | 0.669 | exp_025 | 0.6688 (rounds to .669) | OK |\n| Inline: LLaMA-8B arXiv 2v3 AUC | 0.620 | exp_arXiv_llama8b | 0.6215 (rounds to .622) | **MISMATCH** |\n| Inline: LLaMA-8B arXiv 2v3 CI | [0.605, 0.635] | exp_arXiv_llama8b | NOT STORED | UNVERIFIABLE |\n| Inline: arXiv 1v2 JSD | 0.077 | (none) | No experiment stores 0.077; nearest are Mistral=0.0762, LLaMA=0.0785 | **UNRESOLVED** |\n| Inline: C4 1v2 JSD | ~0.01 | exp_016 | 0.01081 | OK |\n\n---\n\n### Confirmed Mismatches (4 numerical, 1 unresolved)\n\n1. **arXiv/Qwen-1.5B 2v3 AUC**: Paper says `.644`, registry `exp_024` stores `0.6427` which rounds to `.643`. Appears in Table 4, Table S12, and twice in inline text. Delta = 0.001.\n\n2. **Code/LLaMA-8B 2v3 AUC**: Paper says `.510`, registry `exp_code_llama8b` stores `0.5112` which rounds to `.511`. Delta = 0.001.\n\n3. **S12 arXiv 4v5 AUC**: Paper says `.530`, registry `exp_024` stores `0.5294` which rounds to `.529`. Delta = 0.001.\n\n4. **Inline LLaMA-8B arXiv 2v3 AUC**: Paper says `0.620`, registry `exp_arXiv_llama8b` stores `0.6215` which rounds to `0.622`. Delta = 0.002. Bootstrap CI for this claim is not stored in the registry and cannot be verified.\n\n5. **arXiv 1v2 JSD = 0.077**: No registry experiment stores exactly 0.077 for arXiv 1v2 JSD. The nearest single values are `exp_arXiv_mistral7b` (0.0762) and `exp_arXiv_llama8b` (0.0785). The 0.077 figure may be an informal average or rounded estimate; its exact provenance is unresolved.\n\n**Unverifiable (registry incomplete)**: Wiki 0v1, 3v4, 4v5 for S12 (exp_023 only stores 1v2 and 2v3); LLaMA-8B arXiv CI bounds."
      }
    ],
    "totalDurationMs": 671228,
    "totalTokens": 88327,
    "totalToolUseCount": 58,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1590,
      "cache_read_input_tokens": 83915,
      "output_tokens": 2821,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1590
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2821,
          "cache_read_input_tokens": 83915,
          "cache_creation_input_tokens": 1590,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1590,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 1,
      "bashCount": 55,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---


### System

_source line 678_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "acccdabc14ba72457",
  "tool_use_id": "toolu_01VV28GHoAcAmcY7y7PyWkcR",
  "status": "completed",
  "output_file": "",
  "summary": "Audit filtering + inline numbers",
  "usage": {
    "total_tokens": 125212,
    "tool_uses": 51,
    "duration_ms": 671192
  },
  "uuid": "72371c89-594b-4b35-9ae3-3be5e7da7de7",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff"
}
```

---


### Tool result

_source line 679 · 2026-05-23T11:34:33.463Z_

<details><summary>↩ Tool result · `toolu_01VV28GHoAcAmcY7y7PyWkcR`</summary>

```text
Now I have all the data needed to produce the complete audit report. Let me compile the final table:

---

## Audit Report

### TASK 1: Filtering (experiments_c3.tex + tab_filtering_main.tex)

**Table tab_filtering_main.tex** — all cells verified against `exp_006_graduated_filtering`:

| Row | MMLU (paper) | MMLU (registry) | HellaSwag (paper) | HellaSwag (registry) | Match? |
|---|---|---|---|---|---|
| Base model | 0.6018 | 0.6018 | 0.6821 | 0.6821 | MATCH |
| Binary-ours | 0.5941±0.0008 | 0.5941±0.0008 | 0.6701±0.0006 | 0.6701±0.0006 | MATCH |
| Binary-Drayson | 0.5913±0.0009 | 0.5913±0.0009 | 0.6691±0.0004 | 0.6691±0.0004 | MATCH |
| Surprisal | 0.5894±0.0009 | 0.5894±0.0009 | 0.6641±0.0006 | 0.6641±0.0006 | MATCH |
| Graduated (α=0.9) | 0.5892±0.0008 | 0.5892±0.0008 | 0.6701±0.0007 | 0.6701±0.0007 | MATCH |
| DSIR | 0.5869±0.0003 | 0.5869±0.0003 | 0.6631±0.0007 | 0.6631±0.0007 | MATCH |
| No filter | 0.5865±0.0010 | 0.5865±0.0010 | 0.6638±0.0008 | 0.6638±0.0008 | MATCH |

**Inline numbers in experiments_c3.tex:**

| Location | Paper Value | Registry exp_id | Registry Value | Match? |
|---|---|---|---|---|
| experiments_c3.tex | -1.53 pp (no-filter MMLU degradation) | exp_006_graduated_filtering | (0.5865−0.6018)×100 = −1.53 pp | MATCH |
| experiments_c3.tex | -0.77 pp (binary-ours MMLU degradation) | exp_006_graduated_filtering | (0.5941−0.6018)×100 = −0.77 pp | MATCH |
| experiments_c3.tex | ~50% reduction | exp_006_graduated_filtering | (1.53−0.77)/1.53 = 49.7% | MATCH |
| experiments_c3.tex | p_corr < 0.05 vs all alternatives | exp_E_paired_stats | all 5 binary-ours MMLU pairs significant | MATCH |
| experiments_c3.tex | p_corr = 1.00 (graduated α=0.9 vs binary-ours, HellaSwag) | exp_E_paired_stats / tab_pairwise_significance | p=1.00, Δ=0.00 | MATCH |
| experiments_c3.tex | p_corr = 0.011 (graduated α=0.9 vs binary-ours, MMLU) | exp_E_paired_stats / tab_pairwise_significance | p=.011 | MATCH |

---

### TASK 2: Introduction numbers

| Location | Paper Value | Registry exp_id | Registry Value | Match? |
|---|---|---|---|---|
| introduction.tex | MMLU 0.5941 (binary-ours) | exp_006_graduated_filtering | 0.5941 | MATCH |
| introduction.tex | base 0.6018 | exp_006_graduated_filtering | 0.6018 | MATCH |
| introduction.tex | p ≤ 0.002 for K*=2 configurations | exp_007_bootstrap_ci | all 4 K*=2 configs perm_p = 0.002 | MATCH |

---

### TASK 3: Discussion numbers

| Location | Paper Value | Registry exp_id | Registry Value | Match? |
|---|---|---|---|---|
| discussion.tex | AUC ≥ 0.92 for 0v1 (web text) | exp_016/017/018/019/001/002/004 | Min 0v1=0.9225 (LLaMA-8B C4) | MATCH |
| discussion.tex | 96% depth-0 recall (OBD) | exp_D_obd_n500 | d0=0.96 | MATCH |
| discussion.tex | 14–22% for depths 2–4 (OBD) | exp_D_obd_n500 | d2=0.14, d3=0.19, d4=0.22 → range 14–22% | MATCH |
| discussion.tex | 8–38% for LLM depths 2–4 | exp_011_llm_zeroshot | GPT: d2=38%, d3=24%, d4=8%; Claude: d2=28%, d3=10%, d4=37% → range 8–38% | MATCH |
| discussion.tex | η²_p = .166 (Scorer main effect) | **NOT IN REGISTRY** | No ANOVA experiment recorded | UNVERIFIABLE |
| discussion.tex | η²_p = .146 (Generator×Scorer interaction) | **NOT IN REGISTRY** | No ANOVA experiment recorded | UNVERIFIABLE |
| discussion.tex | +11.5 pp OLMo self vs cross-scoring gap | exp_002_olmo_depth (note) | self=0.6145, cross=0.5001 → 11.44 pp | MATCH (rounding) |
| discussion.tex | +4.7 pp Pythia gap | exp_001_pythia_depth (note) | self=0.6539, cross=0.6074 → 4.65 pp | MATCH (rounding) |
| discussion.tex | ≈+1.9 pp LLaMA/Mistral gap (each) | exp_019/exp_019b_mistral_cross_scorer | Mistral: self=0.5935, cross=0.5695 → **2.4 pp** (registry); LLaMA: no self-scored experiment | **MISMATCH for Mistral** (2.4 pp vs 1.9 pp); LLaMA gap **UNVERIFIABLE** |
| discussion.tex | 3v4 AUC = 0.68–0.80 (retrain chain) | exp_008_retrain_chain_v2, exp_qwen_retrain_chain, exp_olmo_retrain_v3, exp_pythia_retrain_depth7 | 0.6817, 0.7624, 0.7982, 0.7977, 0.7999 → range 0.68–0.80 | MATCH |
| discussion.tex | 6v7 AUC = 0.634–0.641 (retrain chain extended) | exp_pythia_retrain_depth7, exp_qwen_retrain_depth7 | Pythia: 0.634, Qwen: 0.641 | MATCH |
| discussion.tex | 0.077 at 8B (0v1 JSD) | exp_018_llama8b_depth | 0.077 | MATCH |
| discussion.tex | 0.15–0.27 at ≤1.5B (0v1 JSD) | exp_016/017/mvp_pilot/exp_olmo1b_10k | Qwen-1.5B-Base: 0.164, Qwen-1.5B-Instruct: 0.286, OLMo-1B: 0.230, Qwen-rewrite: 0.267 | **MISMATCH**: actual range is 0.164–0.286 (or 0.164–0.267 if rewrite is upper bound); paper understates both bounds |
| discussion.tex | 1v2 JSD = 0.077 (arXiv) vs ~0.01 (C4) | exp_arXiv_mistral7b, exp_arXiv_llama8b | Mistral arXiv: 0.076, LLaMA arXiv: 0.079; C4 1v2 JSD: 0.005–0.012 | APPROXIMATE MATCH (closest exp: Mistral arXiv 0.076 ≈ 0.077; primary exp_024 has no JSD stored) |
| discussion.tex | 2v3 Δauc = −0.021 (LaTeX stripping) | exp_027_latex_ablation | auc_delta[2v3] = −0.021 | MATCH |

---

### Summary of Issues

**Confirmed mismatches requiring correction:**

1. **"≈+1.9 pp LLaMA/Mistral gap" (discussion.tex)** — MISMATCH for Mistral. Registry shows Mistral self (exp_019: 0.5935) vs cross-scored (exp_019b: 0.5695) = **2.40 pp**, not 1.9 pp. The LLaMA gap is entirely unverifiable from registry because no LLaMA self-scored C4 experiment exists (all LLaMA experiments use Qwen as scorer). The paper may be computing an average or using a different baseline definition.

2. **"0.15–0.27 at ≤1.5B" 0v1 JSD (discussion.tex)** — The actual registry values are: Qwen-1.5B-Base = 0.164, Qwen-1.5B-Instruct = 0.286, OLMo-1B = 0.230, Qwen-rewrite (mvp_pilot) = 0.267. The range is 0.164–0.286 (or 0.164–0.267 if using rewrite as the top bound). The paper's stated range of 0.15–0.27 understates both the lower bound by ~0.014 and the upper bound by up to ~0.016.

**Unverifiable (not in registry):**

3. **η²_p = .166 and η²_p = .146 (ANOVA, discussion.tex)** — These partial eta-squared values from the ANOVA of the cross-scorer matrix are not recorded in any registry experiment. The cross-scorer data exists in `exp_022_cross_scorer_matrix` but the ANOVA itself was never registered as a separate experiment with metrics.

**All other values verified as correct** (19 of 22 checked values match exactly or within acceptable rounding).

agentId: acccdabc14ba72457 (use SendMessage with to: 'acccdabc14ba72457' to continue this agent)
&lt;usage>total_tokens: 125926
tool_uses: 51
duration_ms: 671194&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "0289e3ec-3d1f-4ad5-9e1a-3fd0b95914a4",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are auditing numerical data in a research paper against experiment registry records.\n\nThe registry data is saved as JSON at:\n/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt\n\nThe format is `{\"result\": \"&lt;JSON string>\"}` — parse the inner JSON string to get experiment records.\n\n**TASK 1: Filtering results (experiments_c3.tex)**\n\nFind experiments related to filtering / downstream / MMLU / HellaSwag. Look for exp_ids containing \"filter\", \"downstream\", \"mmlu\", \"lora\", \"finetune\", or similar.\n\nVerify these inline numbers from experiments_c3.tex:\n- \"-1.53 pp\" (no-filter MMLU degradation from base)\n- \"-0.77 pp\" (binary-ours MMLU degradation)\n- \"~50% reduction\"\n- \"p_corr < 0.05 vs all alternatives\"\n- \"p_corr = 1.00\" (graduated α=0.9 vs binary-ours on HellaSwag)\n- \"p_corr = 0.011\" (graduated α=0.9 vs binary-ours on MMLU)\n\nAlso the filtering table is loaded from `tables/tab_filtering_main.tex` — read that file at:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_filtering_main.tex\n\nAnd verify all numbers in that table against registry.\n\n**TASK 2: Introduction numbers (introduction.tex)**\n\nVerify:\n- \"MMLU 0.5941 vs base 0.6018\" — these should come from filtering experiment\n- \"p ≤ 0.002\" for K*=2 configurations\n\n**TASK 3: Discussion numbers (discussion.tex)**\n\nVerify these inline numbers:\n- \"AUC ≥ 0.92\" for 0v1\n- \"96% depth-0 recall\" and \"14-22%\" for depths 2-4 (OBD)\n- \"8-38%\" for LLM depths 2-4\n- \"η²_p = .166\" and \"η²_p = .146\" — look for ANOVA experiment\n- \"+11.5 pp\" OLMo self vs cross-scoring gap\n- \"+4.7 pp\" Pythia gap\n- \"≈+1.9 pp\" LLaMA/Mistral gap\n- \"3v4 AUC = 0.68-0.80\" retrain chain\n- \"6v7 AUC = 0.634-0.641\" retrain chain extended\n- \"0.077 at 8B vs 0.15-0.27 at ≤1.5B\" (0v1 JSD)\n- \"2v3 Δauc = -0.021\" for LaTeX stripping\n\nFor each value, output a row:\n| Location | Paper Value | Registry exp_id | Registry Value | Match? |\n\nUse jq or python to parse the registry. Report ALL mismatches.",
    "agentId": "acccdabc14ba72457",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the data needed to produce the complete audit report. Let me compile the final table:\n\n---\n\n## Audit Report\n\n### TASK 1: Filtering (experiments_c3.tex + tab_filtering_main.tex)\n\n**Table tab_filtering_main.tex** — all cells verified against `exp_006_graduated_filtering`:\n\n| Row | MMLU (paper) | MMLU (registry) | HellaSwag (paper) | HellaSwag (registry) | Match? |\n|---|---|---|---|---|---|\n| Base model | 0.6018 | 0.6018 | 0.6821 | 0.6821 | MATCH |\n| Binary-ours | 0.5941±0.0008 | 0.5941±0.0008 | 0.6701±0.0006 | 0.6701±0.0006 | MATCH |\n| Binary-Drayson | 0.5913±0.0009 | 0.5913±0.0009 | 0.6691±0.0004 | 0.6691±0.0004 | MATCH |\n| Surprisal | 0.5894±0.0009 | 0.5894±0.0009 | 0.6641±0.0006 | 0.6641±0.0006 | MATCH |\n| Graduated (α=0.9) | 0.5892±0.0008 | 0.5892±0.0008 | 0.6701±0.0007 | 0.6701±0.0007 | MATCH |\n| DSIR | 0.5869±0.0003 | 0.5869±0.0003 | 0.6631±0.0007 | 0.6631±0.0007 | MATCH |\n| No filter | 0.5865±0.0010 | 0.5865±0.0010 | 0.6638±0.0008 | 0.6638±0.0008 | MATCH |\n\n**Inline numbers in experiments_c3.tex:**\n\n| Location | Paper Value | Registry exp_id | Registry Value | Match? |\n|---|---|---|---|---|\n| experiments_c3.tex | -1.53 pp (no-filter MMLU degradation) | exp_006_graduated_filtering | (0.5865−0.6018)×100 = −1.53 pp | MATCH |\n| experiments_c3.tex | -0.77 pp (binary-ours MMLU degradation) | exp_006_graduated_filtering | (0.5941−0.6018)×100 = −0.77 pp | MATCH |\n| experiments_c3.tex | ~50% reduction | exp_006_graduated_filtering | (1.53−0.77)/1.53 = 49.7% | MATCH |\n| experiments_c3.tex | p_corr < 0.05 vs all alternatives | exp_E_paired_stats | all 5 binary-ours MMLU pairs significant | MATCH |\n| experiments_c3.tex | p_corr = 1.00 (graduated α=0.9 vs binary-ours, HellaSwag) | exp_E_paired_stats / tab_pairwise_significance | p=1.00, Δ=0.00 | MATCH |\n| experiments_c3.tex | p_corr = 0.011 (graduated α=0.9 vs binary-ours, MMLU) | exp_E_paired_stats / tab_pairwise_significance | p=.011 | MATCH |\n\n---\n\n### TASK 2: Introduction numbers\n\n| Location | Paper Value | Registry exp_id | Registry Value | Match? |\n|---|---|---|---|---|\n| introduction.tex | MMLU 0.5941 (binary-ours) | exp_006_graduated_filtering | 0.5941 | MATCH |\n| introduction.tex | base 0.6018 | exp_006_graduated_filtering | 0.6018 | MATCH |\n| introduction.tex | p ≤ 0.002 for K*=2 configurations | exp_007_bootstrap_ci | all 4 K*=2 configs perm_p = 0.002 | MATCH |\n\n---\n\n### TASK 3: Discussion numbers\n\n| Location | Paper Value | Registry exp_id | Registry Value | Match? |\n|---|---|---|---|---|\n| discussion.tex | AUC ≥ 0.92 for 0v1 (web text) | exp_016/017/018/019/001/002/004 | Min 0v1=0.9225 (LLaMA-8B C4) | MATCH |\n| discussion.tex | 96% depth-0 recall (OBD) | exp_D_obd_n500 | d0=0.96 | MATCH |\n| discussion.tex | 14–22% for depths 2–4 (OBD) | exp_D_obd_n500 | d2=0.14, d3=0.19, d4=0.22 → range 14–22% | MATCH |\n| discussion.tex | 8–38% for LLM depths 2–4 | exp_011_llm_zeroshot | GPT: d2=38%, d3=24%, d4=8%; Claude: d2=28%, d3=10%, d4=37% → range 8–38% | MATCH |\n| discussion.tex | η²_p = .166 (Scorer main effect) | **NOT IN REGISTRY** | No ANOVA experiment recorded | UNVERIFIABLE |\n| discussion.tex | η²_p = .146 (Generator×Scorer interaction) | **NOT IN REGISTRY** | No ANOVA experiment recorded | UNVERIFIABLE |\n| discussion.tex | +11.5 pp OLMo self vs cross-scoring gap | exp_002_olmo_depth (note) | self=0.6145, cross=0.5001 → 11.44 pp | MATCH (rounding) |\n| discussion.tex | +4.7 pp Pythia gap | exp_001_pythia_depth (note) | self=0.6539, cross=0.6074 → 4.65 pp | MATCH (rounding) |\n| discussion.tex | ≈+1.9 pp LLaMA/Mistral gap (each) | exp_019/exp_019b_mistral_cross_scorer | Mistral: self=0.5935, cross=0.5695 → **2.4 pp** (registry); LLaMA: no self-scored experiment | **MISMATCH for Mistral** (2.4 pp vs 1.9 pp); LLaMA gap **UNVERIFIABLE** |\n| discussion.tex | 3v4 AUC = 0.68–0.80 (retrain chain) | exp_008_retrain_chain_v2, exp_qwen_retrain_chain, exp_olmo_retrain_v3, exp_pythia_retrain_depth7 | 0.6817, 0.7624, 0.7982, 0.7977, 0.7999 → range 0.68–0.80 | MATCH |\n| discussion.tex | 6v7 AUC = 0.634–0.641 (retrain chain extended) | exp_pythia_retrain_depth7, exp_qwen_retrain_depth7 | Pythia: 0.634, Qwen: 0.641 | MATCH |\n| discussion.tex | 0.077 at 8B (0v1 JSD) | exp_018_llama8b_depth | 0.077 | MATCH |\n| discussion.tex | 0.15–0.27 at ≤1.5B (0v1 JSD) | exp_016/017/mvp_pilot/exp_olmo1b_10k | Qwen-1.5B-Base: 0.164, Qwen-1.5B-Instruct: 0.286, OLMo-1B: 0.230, Qwen-rewrite: 0.267 | **MISMATCH**: actual range is 0.164–0.286 (or 0.164–0.267 if rewrite is upper bound); paper understates both bounds |\n| discussion.tex | 1v2 JSD = 0.077 (arXiv) vs ~0.01 (C4) | exp_arXiv_mistral7b, exp_arXiv_llama8b | Mistral arXiv: 0.076, LLaMA arXiv: 0.079; C4 1v2 JSD: 0.005–0.012 | APPROXIMATE MATCH (closest exp: Mistral arXiv 0.076 ≈ 0.077; primary exp_024 has no JSD stored) |\n| discussion.tex | 2v3 Δauc = −0.021 (LaTeX stripping) | exp_027_latex_ablation | auc_delta[2v3] = −0.021 | MATCH |\n\n---\n\n### Summary of Issues\n\n**Confirmed mismatches requiring correction:**\n\n1. **\"≈+1.9 pp LLaMA/Mistral gap\" (discussion.tex)** — MISMATCH for Mistral. Registry shows Mistral self (exp_019: 0.5935) vs cross-scored (exp_019b: 0.5695) = **2.40 pp**, not 1.9 pp. The LLaMA gap is entirely unverifiable from registry because no LLaMA self-scored C4 experiment exists (all LLaMA experiments use Qwen as scorer). The paper may be computing an average or using a different baseline definition.\n\n2. **\"0.15–0.27 at ≤1.5B\" 0v1 JSD (discussion.tex)** — The actual registry values are: Qwen-1.5B-Base = 0.164, Qwen-1.5B-Instruct = 0.286, OLMo-1B = 0.230, Qwen-rewrite (mvp_pilot) = 0.267. The range is 0.164–0.286 (or 0.164–0.267 if using rewrite as the top bound). The paper's stated range of 0.15–0.27 understates both the lower bound by ~0.014 and the upper bound by up to ~0.016.\n\n**Unverifiable (not in registry):**\n\n3. **η²_p = .166 and η²_p = .146 (ANOVA, discussion.tex)** — These partial eta-squared values from the ANOVA of the cross-scorer matrix are not recorded in any registry experiment. The cross-scorer data exists in `exp_022_cross_scorer_matrix` but the ANOVA itself was never registered as a separate experiment with metrics.\n\n**All other values verified as correct** (19 of 22 checked values match exactly or within acceptable rounding)."
      }
    ],
    "totalDurationMs": 671194,
    "totalTokens": 125926,
    "totalToolUseCount": 51,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1343,
      "cache_read_input_tokens": 121836,
      "output_tokens": 2746,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1343
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2746,
          "cache_read_input_tokens": 121836,
          "cache_creation_input_tokens": 1343,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1343,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 6,
      "searchCount": 1,
      "bashCount": 44,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---


### System

_source line 680_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a409a6aeb060f7eee",
  "tool_use_id": "toolu_01VA6RDVEYrmJqYoJVqwAcxJ",
  "status": "completed",
  "output_file": "",
  "summary": "Audit decoding + bootstrap + neural probe",
  "usage": {
    "total_tokens": 88808,
    "tool_uses": 49,
    "duration_ms": 701666
  },
  "uuid": "1bb80f3b-17f6-451b-8850-7390d61201e9",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff"
}
```

---


### Tool result

_source line 681 · 2026-05-23T11:35:23.845Z_

<details><summary>↩ Tool result · `toolu_01VA6RDVEYrmJqYoJVqwAcxJ`</summary>

```text
Here is the complete audit report.

---

## Numerical Audit Report

### TASK 1: Decoding Ablation AUC — Table S2 (exp_003_decoding_ablation)

All 20 AUC point estimates and confidence intervals in Table S2 match exp_003 within rounding tolerance (±0.001).

| Location | Paper Value | Registry exp_id | Registry Value | Match? |
|---|---|---|---|---|
| S2 0v1 Greedy | .980 [.977,.982] | exp_003 | 0.9796 [0.9772,0.9820] | OK |
| S2 0v1 Nuc p=0.9 T=1.0 | .995 [.993,.996] | exp_003 | 0.9945 [0.9934,0.9956] | OK |
| S2 0v1 Nuc p=0.95 T=0.7 | .988 [.986,.990] | exp_003 | 0.9877 [0.9857,0.9896] | OK |
| S2 0v1 Nuc p=0.95 T=1.2 | .998 [.998,.999] | exp_003 | 0.9982 [0.9975,0.9987] | OK |
| S2 1v2 Greedy | .689 [.680,.698] | exp_003 | 0.6892 [0.6802,0.6982] | OK |
| S2 1v2 Nuc p=0.9 T=1.0 | .687 [.677,.695] | exp_003 | 0.6862 [0.6774,0.6951] | OK |
| S2 1v2 Nuc p=0.95 T=0.7 | .689 [.680,.697] | exp_003 | 0.6885 [0.6797,0.6970] | OK |
| S2 1v2 Nuc p=0.95 T=1.2 | .704 [.695,.713] | exp_003 | 0.7037 [0.6945,0.7126] | OK |
| S2 2v3 Greedy | .561 [.552,.571] | exp_003 | 0.5612 [0.5517,0.5705] | OK |
| S2 2v3 Nuc p=0.9 T=1.0 | .592 [.582,.601] | exp_003 | 0.5917 [0.5824,0.6010] | OK |
| S2 2v3 Nuc p=0.95 T=0.7 | .590 [.581,.600] | exp_003 | 0.5901 [0.5806,0.5996] | OK |
| S2 2v3 Nuc p=0.95 T=1.2 | .582 [.572,.592] | exp_003 | 0.5820 [0.5722,0.5917] | OK |
| S2 3v4 Greedy | .540 [.531,.550] | exp_003 | 0.5405 [0.5308,0.5502] | OK |
| S2 3v4 Nuc p=0.9 T=1.0 | .547 [.537,.557] | exp_003 | 0.5468 [0.5369,0.5568] | OK |
| S2 3v4 Nuc p=0.95 T=0.7 | .539 [.529,.549] | exp_003 | 0.5390 [0.5288,0.5493] | OK |
| S2 3v4 Nuc p=0.95 T=1.2 | .529 [.519,.540] | exp_003 | 0.5293 [0.5185,0.5399] | OK |
| S2 4v5 Greedy | .514 [.503,.524] | exp_003 | 0.5137 [0.5033,0.5238] | OK |
| S2 4v5 Nuc p=0.9 T=1.0 | .507 [.496,.517] | exp_003 | 0.5066 [0.4959,0.5173] | OK |
| S2 4v5 Nuc p=0.95 T=0.7 | .535 [.524,.545] | exp_003 | 0.5348 [0.5243,0.5454] | OK |
| S2 4v5 Nuc p=0.95 T=1.2 | .524 [.513,.535] | exp_003 | 0.5237 [0.5132,0.5347] | OK |

**Table S2 Spearman ρ values (0.600, 0.782, 0.914, 0.893, 0.532, 0.668): NOT IN REGISTRY.** The value 0.782 is completely absent from the registry (nearest value is 0.7779 in an unrelated exp_wiki_multi_source metric). The others appear only as AUC or threshold values in unrelated contexts. exp_003 stores no Spearman ρ in its metrics at all. These 6 values cannot be verified.

---

### TASK 2: Bootstrap CI — Table S8 (tab:s8_cv_folds)

**Critical finding: Table S8 mixes data from two incompatible scorer setups.** exp_007_bootstrap_ci ran bootstrap on self-scored data (before the D107 Qwen cross-scorer update). exp_001 and exp_002 were later updated to Qwen cross-scoring.

| Location | Paper Value | Registry exp_id | Registry Value | Match? |
|---|---|---|---|---|
| S8 Qwen-rw 0v1 | .996 [.995,.997] | exp_007 | 0.9956 [0.9946,0.9965] | OK |
| S8 Qwen-rw 1v2 | .696 [.686,.704] | exp_007 | 0.6955 [0.6859,0.7041] | OK |
| S8 Qwen-rw 2v3 | .589 [.580,.599] | exp_007 | 0.5893 [0.5795,0.5991] | OK |
| S8 Qwen-rw 3v4 | .544 [.533,.555] | exp_007 | 0.5435 [0.5333,0.5551] | OK |
| S8 Qwen-rw 4v5 | .534 [.524,.545] | exp_007 | 0.5340 [0.5238,0.5448] | OK |
| S8 Pythia 0v1 | .993 [.992,.994] | exp_007 | 0.9932 [0.9921,0.9943] | OK |
| **S8 Pythia 1v2** | **.607 [.598,.617]** | **exp_007** | **0.6539 [0.6454,0.6630]** | **MISMATCH** |
| S8 Pythia 2v3 | .551 [.542,.563] | exp_007 | 0.5514 [0.5417,0.5628] | OK |
| S8 Pythia 3v4 | .515 [.504,.526] | exp_007 | 0.5152 [0.5041,0.5260] | OK |
| S8 Pythia 4v5 | .514 [.502,.525] | exp_007 | 0.5136 [0.5021,0.5249] | OK |
| **S8 OLMo 0v1** | **.986 [.984,.988]** | **exp_007** | **0.9970 [0.9964,0.9975]** | **MISMATCH** |
| **S8 OLMo 1v2** | **.500 [.496,.519]** | **exp_007** | **0.6145 [0.6045,0.6247]** | **MISMATCH** |
| **S8 OLMo 2v3** | **.497 [.486,.509]** | **exp_007** | **0.5496 [0.5399,0.5596]** | **MISMATCH** |
| **S8 OLMo 3v4** | **.502 [.491,.513]** | **exp_007** | **0.5091 [0.4973,0.5200]** | **MISMATCH** |
| **S8 OLMo 4v5** | **.494 [.483,.506]** | **exp_007** | **0.5045 [0.4932,0.5150]** | **MISMATCH** |
| S8 Qwen-cont 0v1 | .997 [.996,.998] | exp_007 | 0.9971 [0.9963,0.9978] | OK |
| S8 Qwen-cont 1v2 | .611 [.602,.621] | exp_007 | 0.6112 [0.6015,0.6213] | OK |
| S8 Qwen-cont 2v3 | .561 [.551,.571] | exp_007 | 0.5609 [0.5511,0.5712] | OK |
| S8 Qwen-cont 3v4 | .541 [.531,.551] | exp_007 | 0.5409 [0.5308,0.5508] | OK |
| S8 Qwen-cont 4v5 | .514 [.504,.526] | exp_007 | 0.5141 [0.5035,0.5255] | OK |

**Diagnosis of mismatches:**

- **OLMo all 5 pairs**: Paper Table S8 OLMo values (0v1=.986, 1v2=.500, ...) match exp_002_olmo_depth (Qwen cross-scored point estimates: 0.9861, 0.5001, 0.4972, 0.5034, 0.4971) to within 0.001. The CI intervals are NOT in the registry — exp_002 has no bootstrap CI, and exp_007 used the pre-update self-scored data. The paper's OLMo CIs cannot be traced to any registry experiment.

- **Pythia 1v2 = .607**: exp_007 gives 0.6539 (self-scored). The paper value 0.607 matches exp_001_pythia_depth Qwen cross-scored AUC of 0.6074, but exp_001 has no CI stored. The paper appears to mix: exp_007 self-scored data for Pythia 0v1/2v3/3v4/4v5 but Qwen cross-scored for Pythia 1v2. This is an internal inconsistency in Table S8.

**Pythia 2v3 disambiguation:** exp_007 self-scored = 0.5514 → rounds to .551 (Table S8 value). exp_001 Qwen cross-scored = 0.544 → rounds to .544 (Table 1 value). Both are in registry, different scorer setups. The cross-scorer update changed this value.

---

### TASK 3: Neural Probe — exp_015_neural_probe

| Location | Paper Value | Registry exp_id | Registry Value | Match? |
|---|---|---|---|---|
| Qwen 2v3 AUC | 0.6159 | exp_015 | 0.616 | OK |
| Qwen K* | K*=3 | exp_015 | k_star_neural=3 | OK |
| Pythia 2v3 AUC | 0.5963 | exp_015 | 0.596 | OK |
| Pythia K* | K*=2 | exp_015 | k_star_neural=2 | OK |
| **OLMo 2v3 AUC** | **0.5056** | **exp_015** | **0.589** | **MISMATCH** |
| **OLMo 1v2 AUC** | **0.5054** | **exp_015** | **0.657** | **MISMATCH** |
| **OLMo K*** | **K*=1** | **exp_015** | **k_star_neural=2** | **MISMATCH** |
| All CIs | [0.610,0.622], [0.589,0.603], [0.497,0.516] | exp_015 | No CI stored | UNVERIFIABLE |

**OLMo neural probe mismatch is severe.** exp_015 notes explicitly state "OLMo K*_neural=2" and the 1v2 AUC=0.657 implies strong discriminability, whereas the paper claims K*=1 with 1v2=0.5054. The paper's OLMo values (1v2≈0.505) closely resemble the Qwen cross-scored 15D OBD AUC (exp_002: 1v2=0.5001), suggesting the paper may have accidentally used the cross-scored 15D results instead of the neural probe results for OLMo.

---

### TASK 4: Pythia Decoding — Table S10 (exp_020_pythia_decoding)

| Location | Paper Value | Registry exp_id | Registry Value | Match? |
|---|---|---|---|---|
| S10 Pythia 0v1 Greedy | .999 | exp_020 | 0.9992 | OK |
| S10 Pythia 0v1 nuc09 | .995 | exp_020 | 0.9948 | OK |
| S10 Pythia 0v1 t07 | .996 | exp_020 | 0.9965 | OK |
| S10 Pythia 0v1 t12 | .994 | exp_020 | 0.9933 | OK |
| S10 Pythia 1v2 Greedy | .884 | exp_020 | 0.8838 | OK |
| **S10 Pythia 1v2 nuc09** | **.675** | **exp_020** | **0.6770** | **MISMATCH** (+0.002) |
| S10 Pythia 1v2 t07 | .728 | exp_020 | 0.7265 | OK |
| S10 Pythia 1v2 t12 | .618 | exp_020 | 0.6172 | OK |
| **S10 Pythia 2v3 Greedy** | **.531** | **exp_020** | **0.5342** | **MISMATCH** (-0.003) |
| **S10 Pythia 2v3 nuc09** | **.559** | **exp_020** | **0.5549** | **MISMATCH** (+0.004) |
| **S10 Pythia 2v3 t07** | **.598** | **exp_020** | **0.5941** | **MISMATCH** (+0.004) |
| **S10 Pythia 2v3 t12** | **.531** | **exp_020** | **0.5226** | **MISMATCH** (+0.008) |
| S10 Pythia 3v4 Greedy | .522 | exp_020 | 0.5228 | OK |
| **S10 Pythia 3v4 nuc09** | **.524** | **exp_020** | **0.5299** | **MISMATCH** (-0.006) |
| **S10 Pythia 3v4 t07** | **.563** | **exp_020** | **0.5698** | **MISMATCH** (-0.007) |
| **S10 Pythia 3v4 t12** | **.520** | **exp_020** | **0.5170** | **MISMATCH** (+0.003) |
| **S10 Pythia 4v5 Greedy** | **.514** | **exp_020** | **0.5162** | **MISMATCH** (-0.002) |
| S10 Pythia 4v5 nuc09 | .501 | exp_020 | 0.5013 | OK |
| S10 Pythia 4v5 t07 | .527 | exp_020 | 0.5284 | OK |
| **S10 Pythia 4v5 t12** | **.510** | **exp_020** | **0.5051** | **MISMATCH** (+0.005) |

10 out of 20 values mismatch. Discrepancies range from 0.002 to 0.008 and are not systematic in sign, ruling out simple rounding. The registry stores the original OOF AUC; the paper may use bootstrap-mean AUC or values from a rerun not reflected in the registry.

---

### TASK 5: Length Ablation — Table S11 (exp_021_length_ablation)

| Location | Paper Value | Registry exp_id | Registry Value | Match? |
|---|---|---|---|---|
| S11 1v2 128tok | .622 | exp_021 | 0.6219 | OK |
| S11 1v2 256tok | .628 | exp_021 | 0.6282 | OK |
| S11 1v2 512tok | .607 | exp_021 | 0.6073 | OK |
| S11 0v1 (all lengths) | .979 / .991 / .992 | exp_021 | Not stored | UNVERIFIABLE |
| S11 2v3 (all lengths) | .529 / .556 / .572 | exp_021 | Not stored | UNVERIFIABLE |
| S11 3v4 (all lengths) | .535 / .530 / .530 | exp_021 | Not stored | UNVERIFIABLE |
| S11 4v5 (all lengths) | .501 / .514 / .518 | exp_021 | Not stored | UNVERIFIABLE |

The 1v2 row matches perfectly. The registry for exp_021 only stores `1v2_auc` for each length; the remaining 4 depth-pair rows of Table S11 have no corresponding registry entries and cannot be audited.

---

## Summary of Confirmed Mismatches

| # | Location | Paper Value | Registry Value | Severity |
|---|---|---|---|---|
| 1 | S8 Pythia 1v2 | .607 [.598,.617] | exp_007: 0.6539 [0.6454,0.6630] | High — paper uses cross-scored AUC with self-scored CIs from a different run |
| 2 | S8 OLMo all 5 pairs | .986/.500/.497/.502/.494 (+ CIs) | exp_007 self-scored (0.997/0.614/0.550/0.509/0.505); exp_002 cross-scored matches AUC only, no CI | High — CIs not in registry at all |
| 3 | Neural probe OLMo 2v3 | 0.5056 | exp_015: 0.589 | Critical — off by 0.083 |
| 4 | Neural probe OLMo 1v2 | 0.5054 | exp_015: 0.657 | Critical — off by 0.152 |
| 5 | Neural probe OLMo K* | K*=1 | exp_015: k_star_neural=2 | Critical |
| 6 | Table S10 Pythia 10/20 cells | various | exp_020: differs by 0.002–0.008 | Moderate — non-systematic, possible rerun discrepancy |
| 7 | Table S2 Spearman ρ (6 values) | 0.600, 0.782, 0.914, 0.893, 0.532, 0.668 | Not present in registry | Cannot verify |

agentId: a409a6aeb060f7eee (use SendMessage with to: 'a409a6aeb060f7eee' to continue this agent)
&lt;usage>total_tokens: 91684
tool_uses: 49
duration_ms: 701667&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "2a9cbe44-5804-4d04-b3bb-c7c07b1abcb5",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are auditing numerical data in a research paper against experiment registry records.\n\nThe registry data is saved as JSON at:\n/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt\n\nThe format is `{\"result\": \"&lt;JSON string>\"}` — parse the inner JSON string to get experiment records.\n\n**TASK 1: Decoding ablation (Table S2, tab:s2_decoding)**\n\nFind exp-003 or similar decoding ablation experiments. Verify all AUC values in Table S2:\n| Depth Pair | Greedy | Nuc p=0.9 T=1.0 | Nuc p=0.95 T=0.7 | Nuc p=0.95 T=1.2 |\n| 0v1 | .980 [.977,.982] | .995 [.993,.996] | .988 [.986,.990] | .998 [.998,.999] |\n| 1v2 | .689 [.680,.698] | .687 [.677,.695] | .689 [.680,.697] | .704 [.695,.713] |\n| 2v3 | .561 [.552,.571] | .592 [.582,.601] | .590 [.581,.600] | .582 [.572,.592] |\n| 3v4 | .540 [.531,.550] | .547 [.537,.557] | .539 [.529,.549] | .529 [.519,.540] |\n| 4v5 | .514 [.503,.524] | .507 [.496,.517] | .535 [.524,.545] | .524 [.513,.535] |\n\nAnd the Spearman ρ values: 0.600, 0.782, 0.914, 0.893, 0.532, 0.668\n\n**TASK 2: Bootstrap CI (Table S8, tab:s8_cv_folds)**\n\nFind exp-007 or bootstrap/cv experiments. Verify:\n- Qwen-rw: 0v1=.996[.995,.997], 1v2=.696[.686,.704], 2v3=.589[.580,.599], 3v4=.544[.533,.555], 4v5=.534[.524,.545]\n- Pythia: 0v1=.993[.992,.994], 1v2=.607[.598,.617], 2v3=.551[.542,.563], 3v4=.515[.504,.526], 4v5=.514[.502,.525]\n- OLMo: 0v1=.986[.984,.988], 1v2=.500[.496,.519], 2v3=.497[.486,.509], 3v4=.502[.491,.513], 4v5=.494[.483,.506]\n- Qwen-cont: 0v1=.997[.996,.998], 1v2=.611[.602,.621], 2v3=.561[.551,.571], 3v4=.541[.531,.551], 4v5=.514[.504,.526]\n\nNote: Table S8 Pythia 2v3 says .551 but Table 1 says .5440. Check which is in registry.\n\n**TASK 3: Neural probe (exp-015 or similar)**\n\nVerify neural probe values:\n- Qwen: 2v3 AUC = 0.6159 [0.610, 0.622], K*=3\n- Pythia: 2v3 AUC = 0.5963 [0.589, 0.603], K*=2\n- OLMo: 2v3 AUC = 0.5056 [0.497, 0.516], K*=1 (also 1v2=0.5054)\n\n**TASK 4: Pythia decoding (Table S10, exp-020)**\n\nVerify:\n| | Greedy | p=0.9 | T=0.7 | T=1.2 |\n| 0v1 | .999 | .995 | .996 | .994 |\n| 1v2 | .884 | .675 | .728 | .618 |\n| 2v3 | .531 | .559 | .598 | .531 |\n| 3v4 | .522 | .524 | .563 | .520 |\n| 4v5 | .514 | .501 | .527 | .510 |\n\n**TASK 5: Length ablation (Table S11, exp-021)**\n\nVerify:\n| | 128 | 256 | 512 |\n| 0v1 | .979 | .991 | .992 |\n| 1v2 | .622 | .628 | .607 |\n| 2v3 | .529 | .556 | .572 |\n| 3v4 | .535 | .530 | .530 |\n| 4v5 | .501 | .514 | .518 |\n\nFor each value, output a row:\n| Location | Paper Value | Registry exp_id | Registry Value | Match? |\n\nUse jq or python to parse the registry. Report ALL mismatches.",
    "agentId": "a409a6aeb060f7eee",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete audit report.\n\n---\n\n## Numerical Audit Report\n\n### TASK 1: Decoding Ablation AUC — Table S2 (exp_003_decoding_ablation)\n\nAll 20 AUC point estimates and confidence intervals in Table S2 match exp_003 within rounding tolerance (±0.001).\n\n| Location | Paper Value | Registry exp_id | Registry Value | Match? |\n|---|---|---|---|---|\n| S2 0v1 Greedy | .980 [.977,.982] | exp_003 | 0.9796 [0.9772,0.9820] | OK |\n| S2 0v1 Nuc p=0.9 T=1.0 | .995 [.993,.996] | exp_003 | 0.9945 [0.9934,0.9956] | OK |\n| S2 0v1 Nuc p=0.95 T=0.7 | .988 [.986,.990] | exp_003 | 0.9877 [0.9857,0.9896] | OK |\n| S2 0v1 Nuc p=0.95 T=1.2 | .998 [.998,.999] | exp_003 | 0.9982 [0.9975,0.9987] | OK |\n| S2 1v2 Greedy | .689 [.680,.698] | exp_003 | 0.6892 [0.6802,0.6982] | OK |\n| S2 1v2 Nuc p=0.9 T=1.0 | .687 [.677,.695] | exp_003 | 0.6862 [0.6774,0.6951] | OK |\n| S2 1v2 Nuc p=0.95 T=0.7 | .689 [.680,.697] | exp_003 | 0.6885 [0.6797,0.6970] | OK |\n| S2 1v2 Nuc p=0.95 T=1.2 | .704 [.695,.713] | exp_003 | 0.7037 [0.6945,0.7126] | OK |\n| S2 2v3 Greedy | .561 [.552,.571] | exp_003 | 0.5612 [0.5517,0.5705] | OK |\n| S2 2v3 Nuc p=0.9 T=1.0 | .592 [.582,.601] | exp_003 | 0.5917 [0.5824,0.6010] | OK |\n| S2 2v3 Nuc p=0.95 T=0.7 | .590 [.581,.600] | exp_003 | 0.5901 [0.5806,0.5996] | OK |\n| S2 2v3 Nuc p=0.95 T=1.2 | .582 [.572,.592] | exp_003 | 0.5820 [0.5722,0.5917] | OK |\n| S2 3v4 Greedy | .540 [.531,.550] | exp_003 | 0.5405 [0.5308,0.5502] | OK |\n| S2 3v4 Nuc p=0.9 T=1.0 | .547 [.537,.557] | exp_003 | 0.5468 [0.5369,0.5568] | OK |\n| S2 3v4 Nuc p=0.95 T=0.7 | .539 [.529,.549] | exp_003 | 0.5390 [0.5288,0.5493] | OK |\n| S2 3v4 Nuc p=0.95 T=1.2 | .529 [.519,.540] | exp_003 | 0.5293 [0.5185,0.5399] | OK |\n| S2 4v5 Greedy | .514 [.503,.524] | exp_003 | 0.5137 [0.5033,0.5238] | OK |\n| S2 4v5 Nuc p=0.9 T=1.0 | .507 [.496,.517] | exp_003 | 0.5066 [0.4959,0.5173] | OK |\n| S2 4v5 Nuc p=0.95 T=0.7 | .535 [.524,.545] | exp_003 | 0.5348 [0.5243,0.5454] | OK |\n| S2 4v5 Nuc p=0.95 T=1.2 | .524 [.513,.535] | exp_003 | 0.5237 [0.5132,0.5347] | OK |\n\n**Table S2 Spearman ρ values (0.600, 0.782, 0.914, 0.893, 0.532, 0.668): NOT IN REGISTRY.** The value 0.782 is completely absent from the registry (nearest value is 0.7779 in an unrelated exp_wiki_multi_source metric). The others appear only as AUC or threshold values in unrelated contexts. exp_003 stores no Spearman ρ in its metrics at all. These 6 values cannot be verified.\n\n---\n\n### TASK 2: Bootstrap CI — Table S8 (tab:s8_cv_folds)\n\n**Critical finding: Table S8 mixes data from two incompatible scorer setups.** exp_007_bootstrap_ci ran bootstrap on self-scored data (before the D107 Qwen cross-scorer update). exp_001 and exp_002 were later updated to Qwen cross-scoring.\n\n| Location | Paper Value | Registry exp_id | Registry Value | Match? |\n|---|---|---|---|---|\n| S8 Qwen-rw 0v1 | .996 [.995,.997] | exp_007 | 0.9956 [0.9946,0.9965] | OK |\n| S8 Qwen-rw 1v2 | .696 [.686,.704] | exp_007 | 0.6955 [0.6859,0.7041] | OK |\n| S8 Qwen-rw 2v3 | .589 [.580,.599] | exp_007 | 0.5893 [0.5795,0.5991] | OK |\n| S8 Qwen-rw 3v4 | .544 [.533,.555] | exp_007 | 0.5435 [0.5333,0.5551] | OK |\n| S8 Qwen-rw 4v5 | .534 [.524,.545] | exp_007 | 0.5340 [0.5238,0.5448] | OK |\n| S8 Pythia 0v1 | .993 [.992,.994] | exp_007 | 0.9932 [0.9921,0.9943] | OK |\n| **S8 Pythia 1v2** | **.607 [.598,.617]** | **exp_007** | **0.6539 [0.6454,0.6630]** | **MISMATCH** |\n| S8 Pythia 2v3 | .551 [.542,.563] | exp_007 | 0.5514 [0.5417,0.5628] | OK |\n| S8 Pythia 3v4 | .515 [.504,.526] | exp_007 | 0.5152 [0.5041,0.5260] | OK |\n| S8 Pythia 4v5 | .514 [.502,.525] | exp_007 | 0.5136 [0.5021,0.5249] | OK |\n| **S8 OLMo 0v1** | **.986 [.984,.988]** | **exp_007** | **0.9970 [0.9964,0.9975]** | **MISMATCH** |\n| **S8 OLMo 1v2** | **.500 [.496,.519]** | **exp_007** | **0.6145 [0.6045,0.6247]** | **MISMATCH** |\n| **S8 OLMo 2v3** | **.497 [.486,.509]** | **exp_007** | **0.5496 [0.5399,0.5596]** | **MISMATCH** |\n| **S8 OLMo 3v4** | **.502 [.491,.513]** | **exp_007** | **0.5091 [0.4973,0.5200]** | **MISMATCH** |\n| **S8 OLMo 4v5** | **.494 [.483,.506]** | **exp_007** | **0.5045 [0.4932,0.5150]** | **MISMATCH** |\n| S8 Qwen-cont 0v1 | .997 [.996,.998] | exp_007 | 0.9971 [0.9963,0.9978] | OK |\n| S8 Qwen-cont 1v2 | .611 [.602,.621] | exp_007 | 0.6112 [0.6015,0.6213] | OK |\n| S8 Qwen-cont 2v3 | .561 [.551,.571] | exp_007 | 0.5609 [0.5511,0.5712] | OK |\n| S8 Qwen-cont 3v4 | .541 [.531,.551] | exp_007 | 0.5409 [0.5308,0.5508] | OK |\n| S8 Qwen-cont 4v5 | .514 [.504,.526] | exp_007 | 0.5141 [0.5035,0.5255] | OK |\n\n**Diagnosis of mismatches:**\n\n- **OLMo all 5 pairs**: Paper Table S8 OLMo values (0v1=.986, 1v2=.500, ...) match exp_002_olmo_depth (Qwen cross-scored point estimates: 0.9861, 0.5001, 0.4972, 0.5034, 0.4971) to within 0.001. The CI intervals are NOT in the registry — exp_002 has no bootstrap CI, and exp_007 used the pre-update self-scored data. The paper's OLMo CIs cannot be traced to any registry experiment.\n\n- **Pythia 1v2 = .607**: exp_007 gives 0.6539 (self-scored). The paper value 0.607 matches exp_001_pythia_depth Qwen cross-scored AUC of 0.6074, but exp_001 has no CI stored. The paper appears to mix: exp_007 self-scored data for Pythia 0v1/2v3/3v4/4v5 but Qwen cross-scored for Pythia 1v2. This is an internal inconsistency in Table S8.\n\n**Pythia 2v3 disambiguation:** exp_007 self-scored = 0.5514 → rounds to .551 (Table S8 value). exp_001 Qwen cross-scored = 0.544 → rounds to .544 (Table 1 value). Both are in registry, different scorer setups. The cross-scorer update changed this value.\n\n---\n\n### TASK 3: Neural Probe — exp_015_neural_probe\n\n| Location | Paper Value | Registry exp_id | Registry Value | Match? |\n|---|---|---|---|---|\n| Qwen 2v3 AUC | 0.6159 | exp_015 | 0.616 | OK |\n| Qwen K* | K*=3 | exp_015 | k_star_neural=3 | OK |\n| Pythia 2v3 AUC | 0.5963 | exp_015 | 0.596 | OK |\n| Pythia K* | K*=2 | exp_015 | k_star_neural=2 | OK |\n| **OLMo 2v3 AUC** | **0.5056** | **exp_015** | **0.589** | **MISMATCH** |\n| **OLMo 1v2 AUC** | **0.5054** | **exp_015** | **0.657** | **MISMATCH** |\n| **OLMo K*** | **K*=1** | **exp_015** | **k_star_neural=2** | **MISMATCH** |\n| All CIs | [0.610,0.622], [0.589,0.603], [0.497,0.516] | exp_015 | No CI stored | UNVERIFIABLE |\n\n**OLMo neural probe mismatch is severe.** exp_015 notes explicitly state \"OLMo K*_neural=2\" and the 1v2 AUC=0.657 implies strong discriminability, whereas the paper claims K*=1 with 1v2=0.5054. The paper's OLMo values (1v2≈0.505) closely resemble the Qwen cross-scored 15D OBD AUC (exp_002: 1v2=0.5001), suggesting the paper may have accidentally used the cross-scored 15D results instead of the neural probe results for OLMo.\n\n---\n\n### TASK 4: Pythia Decoding — Table S10 (exp_020_pythia_decoding)\n\n| Location | Paper Value | Registry exp_id | Registry Value | Match? |\n|---|---|---|---|---|\n| S10 Pythia 0v1 Greedy | .999 | exp_020 | 0.9992 | OK |\n| S10 Pythia 0v1 nuc09 | .995 | exp_020 | 0.9948 | OK |\n| S10 Pythia 0v1 t07 | .996 | exp_020 | 0.9965 | OK |\n| S10 Pythia 0v1 t12 | .994 | exp_020 | 0.9933 | OK |\n| S10 Pythia 1v2 Greedy | .884 | exp_020 | 0.8838 | OK |\n| **S10 Pythia 1v2 nuc09** | **.675** | **exp_020** | **0.6770** | **MISMATCH** (+0.002) |\n| S10 Pythia 1v2 t07 | .728 | exp_020 | 0.7265 | OK |\n| S10 Pythia 1v2 t12 | .618 | exp_020 | 0.6172 | OK |\n| **S10 Pythia 2v3 Greedy** | **.531** | **exp_020** | **0.5342** | **MISMATCH** (-0.003) |\n| **S10 Pythia 2v3 nuc09** | **.559** | **exp_020** | **0.5549** | **MISMATCH** (+0.004) |\n| **S10 Pythia 2v3 t07** | **.598** | **exp_020** | **0.5941** | **MISMATCH** (+0.004) |\n| **S10 Pythia 2v3 t12** | **.531** | **exp_020** | **0.5226** | **MISMATCH** (+0.008) |\n| S10 Pythia 3v4 Greedy | .522 | exp_020 | 0.5228 | OK |\n| **S10 Pythia 3v4 nuc09** | **.524** | **exp_020** | **0.5299** | **MISMATCH** (-0.006) |\n| **S10 Pythia 3v4 t07** | **.563** | **exp_020** | **0.5698** | **MISMATCH** (-0.007) |\n| **S10 Pythia 3v4 t12** | **.520** | **exp_020** | **0.5170** | **MISMATCH** (+0.003) |\n| **S10 Pythia 4v5 Greedy** | **.514** | **exp_020** | **0.5162** | **MISMATCH** (-0.002) |\n| S10 Pythia 4v5 nuc09 | .501 | exp_020 | 0.5013 | OK |\n| S10 Pythia 4v5 t07 | .527 | exp_020 | 0.5284 | OK |\n| **S10 Pythia 4v5 t12** | **.510** | **exp_020** | **0.5051** | **MISMATCH** (+0.005) |\n\n10 out of 20 values mismatch. Discrepancies range from 0.002 to 0.008 and are not systematic in sign, ruling out simple rounding. The registry stores the original OOF AUC; the paper may use bootstrap-mean AUC or values from a rerun not reflected in the registry.\n\n---\n\n### TASK 5: Length Ablation — Table S11 (exp_021_length_ablation)\n\n| Location | Paper Value | Registry exp_id | Registry Value | Match? |\n|---|---|---|---|---|\n| S11 1v2 128tok | .622 | exp_021 | 0.6219 | OK |\n| S11 1v2 256tok | .628 | exp_021 | 0.6282 | OK |\n| S11 1v2 512tok | .607 | exp_021 | 0.6073 | OK |\n| S11 0v1 (all lengths) | .979 / .991 / .992 | exp_021 | Not stored | UNVERIFIABLE |\n| S11 2v3 (all lengths) | .529 / .556 / .572 | exp_021 | Not stored | UNVERIFIABLE |\n| S11 3v4 (all lengths) | .535 / .530 / .530 | exp_021 | Not stored | UNVERIFIABLE |\n| S11 4v5 (all lengths) | .501 / .514 / .518 | exp_021 | Not stored | UNVERIFIABLE |\n\nThe 1v2 row matches perfectly. The registry for exp_021 only stores `1v2_auc` for each length; the remaining 4 depth-pair rows of Table S11 have no corresponding registry entries and cannot be audited.\n\n---\n\n## Summary of Confirmed Mismatches\n\n| # | Location | Paper Value | Registry Value | Severity |\n|---|---|---|---|---|\n| 1 | S8 Pythia 1v2 | .607 [.598,.617] | exp_007: 0.6539 [0.6454,0.6630] | High — paper uses cross-scored AUC with self-scored CIs from a different run |\n| 2 | S8 OLMo all 5 pairs | .986/.500/.497/.502/.494 (+ CIs) | exp_007 self-scored (0.997/0.614/0.550/0.509/0.505); exp_002 cross-scored matches AUC only, no CI | High — CIs not in registry at all |\n| 3 | Neural probe OLMo 2v3 | 0.5056 | exp_015: 0.589 | Critical — off by 0.083 |\n| 4 | Neural probe OLMo 1v2 | 0.5054 | exp_015: 0.657 | Critical — off by 0.152 |\n| 5 | Neural probe OLMo K* | K*=1 | exp_015: k_star_neural=2 | Critical |\n| 6 | Table S10 Pythia 10/20 cells | various | exp_020: differs by 0.002–0.008 | Moderate — non-systematic, possible rerun discrepancy |\n| 7 | Table S2 Spearman ρ (6 values) | 0.600, 0.782, 0.914, 0.893, 0.532, 0.668 | Not present in registry | Cannot verify |"
      }
    ],
    "totalDurationMs": 701667,
    "totalTokens": 91684,
    "totalToolUseCount": 49,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1212,
      "cache_read_input_tokens": 85259,
      "output_tokens": 5212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1212
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5212,
          "cache_read_input_tokens": 85259,
          "cache_creation_input_tokens": 1212,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1212,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 49,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---


### Assistant

_source line 682_

<details><summary>Logged reasoning block</summary>

```text
Let me compile all the audit results from the agents and create a comprehensive summary. Let me identify the key issues:

**Critical mismatches:**

1. **Neural probe OLMo** — Paper says 1v2=0.5054, 2v3=0.5056, K*=1. Registry exp_015 says 1v2=0.657, 2v3=0.589, K*=2. This is a severe mismatch. The agent suspects the paper accidentally used cross-scored 15D OBD values instead of neural probe values.

2. **Mistral-7B all AUC values** — Paper values don't match either self-scored (exp_019) or cross-scored (exp_019b) registry experiments. 

3. **Table S8 OLMo & Pythia** — The 2v3 value of .5369 appears to be averaging the self-scored and cross-scored results together, which isn't a methodologically sound approach. Table S8 also mixes self-scored (exp_007) and cross-scored data inconsistently—OLMo uses cross-scored AUC but lacks a CI source, while Pythia's 1v2 uses cross-scored AUC (.607) even though exp_007 self-scored gives .6539.

4. **OLMo 3v4 and 4v5 in Table 1** — Small discrepancies (.5024 vs .5034, .4942 vs .4971) appear here.

5. **Table S10 Pythia decoding** — About half the values show minor discrepancies ranging from 0.002 to 0.008.

6. **Moderate mismatches across multiple tables** — Qwen's 2v3 AUC shows .644 in the paper versus .6427 in the registry (rounds to .643), appearing in Table 4, Table S12, and inline text. LLaMA-8B's 2v3 AUC is .510 in the paper but .5112 in the registry (rounds to .511). Table S12's arXiv 4v5 shows .530 versus .5294 (rounds to .529).

7. **Additional moderate discrepancies** — LLaMA-8B's arXiv 2v3 inline value is 0.620 in the paper while the registry shows 0.6215 (rounds to 0.622). The Discussion mentions a Mistral gap of "≈+1.9 pp" but the registry indicates 2.4 pp. The JSD range cited as "0.15-0.27" doesn't match the registry's 0.164-0.286.

8. **Values I can't verify** — The η²_p values, Table S2 Spearman correlations, various confidence intervals, and non-1v2 rows from Table S11 don't appear in the registry, so I can't confirm those. For the ones with clear registry sources, I should fix the rounding discrepancies.

9. **Prioritizing fixes** — The straightforward rounding errors are fixable: Qwen's 2v3 AUC should be .643 not .644, LLaMA-8B's Code 2v3 should be .511 not .510, the S12 arXiv 4v5 should be .529 not .530, and the inline LLaMA-8B value should be .622 not .620. But the neural probe OLMo issue, the Mistral discrepancy, and the Table S8 mixing problem need human review since the sources are unclear and the gaps are substantial.

10. **Re-examining the neural probe OLMo values** — The paper shows OLMo-1B at 0.5056 with a confidence interval, but the registry has completely different numbers (0.589 and 0.657) with a different K* value. The paper's values actually align with the 15D OBD cross-scored results, suggesting someone may have accidentally pulled the wrong experiment's data into the neural probe table.

11. **Flagging the OLMo discrepancy for manual review** — This is too inconsistent to resolve without understanding which source is correct, so I'm marking it as needing human verification.

12. **Checking Table S10 Pythia values** — About half the decoding results differ from the registry by small amounts (0.002-0.008), which could indicate a rerun that wasn't logged, but I can't determine which version is authoritative.

13. **Mistral values remain unresolved** — Neither the self-scored nor cross-scored versions match what's in the paper, so this also needs clarification.

14. **Table S8 mixing issues** — The self-scored and cross-scored data are blended in ways that are too complex to untangle automatically.

Now I'm focusing on the clear rounding errors I can fix with confidence: Qwen 2v3 should be 0.643 instead of 0.644, LLaMA-8B 2v3 needs to be 0.511 not 0.510, the S12 arXiv 4v5 value should be 0.529 not 0.530, and the inline mention of LLaMA-8B in the experiments file needs updating from 0.620 to 0.622. Let me verify these against the source files to make sure I'm catching all instances. Looking at the rounding more carefully—0.6215 should round to 0.622 at three decimal places, not 0.620, so there's definitely a discrepancy there.

Let me trace through the actual data sources. The LLaMA-8B arXiv result isn't in Table 4 itself, only mentioned inline. For the arXiv 2v3 row in Table S12, the footnote gives a CI of [.628, .658], and the registry value is [0.6275, 0.6575]—so the lower bound 0.6275 rounds to 0.628, which matches the table.

Now I need to investigate the OLMo discrepancies more carefully. The registry shows exp_002 values that differ slightly from the paper values—OLMo 3v4 has a +0.001 difference and OLMo 4v5 has a +0.003 difference—which suggests they might be using different scorer configurations, possibly related to the cross-scoring issue I noticed in Table S8. So the cross-scored values in the registry differ from what's in the paper, likely because the paper captured an earlier snapshot before those updates were applied. Let me focus on the concrete fixes I can make with confidence. For the Qwen 2v3 AUC discrepancy, I need to update .644 to .643 across three locations in the LaTeX files—the main text reference, Table 4, and Table S12—while keeping the confidence interval as-is since it aligns with the registry values.

For the Code/LLaMA-8B 2v3 entry, the registry rounds 0.5112 up to .511, so that needs updating. The arXiv 4v5 value in Table S12 should shift from .530 to .529 based on the registry's 0.5294. And for the LLaMA-8B arXiv 2v3 inline value, 0.6215 rounds to 0.622 at three decimal places, not 0.620.

Looking at the paper's rounding pattern across other values—0.6545 displays as .655, 0.8047 as .805—it's consistently using standard rounding rules, which confirms these corrections are needed.

Now I need to verify the registry value of 0.6215 is correct and check whether updating the point estimate from .644 to .643 affects the confidence interval footnote. The CI [0.6275, 0.6575] rounds to [.628, .658], which matches what's already in the paper, so that's consistent. Let me locate where these values appear in the document and make the necessary corrections. Looking at the neural probe results table, I need to understand what's happening with the OLMo-1B entry — the row appears to be cut off, but I can see the AUC value of 0.5056 with its confidence interval. Let me trace through what values are actually reported across the paper and identify any inconsistencies before deciding what needs fixing. I'm seeing major discrepancies between the registry values and what the paper reports for OLMo—the paper shows values around 0.50, while the registry indicates neural probe scores closer to 0.59-0.66 with K*=2. I need to flag these inconsistencies for human review rather than assuming which source is correct, and I should do the same for the Mistral and other table mismatches. I also notice the JSD range cited in the discussion (0.15-0.27) doesn't match the registry values (0.164-0.286), which suggests a substantive error beyond simple rounding.

Now I'm going through the clear rounding corrections I can make with confidence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "21d06ece-ccff-4b9a-a587-346daa95e2a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155tfT5Rh3rtnA99H19Naqt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22473,
      "cache_read_input_tokens": 49522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22473
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 683_

All four agents have returned. Let me compile the results and fix the clear rounding errors.

**Fixing 4 clear rounding mismatches** where registry value is unambiguous:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "34ae908c-bd74-421b-a461-898fce8e7c3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155tfT5Rh3rtnA99H19Naqt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22473,
      "cache_read_input_tokens": 49522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22473
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 684_

<details open><summary>🔧 Tool call — Edit · `toolu_01LaVkc3BHYYKL7NcspUoVb6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "old_string": "2v3 $\\auc = 0.644\\;[0.628,\\,0.658]$, $0.655\\;[0.640,\\,0.669]$, and $0.620\\;[0.605,\\,0.635]$",
  "new_string": "2v3 $\\auc = 0.643\\;[0.628,\\,0.658]$, $0.655\\;[0.640,\\,0.669]$, and $0.622\\;[0.605,\\,0.635]$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "89b4e684-1aad-406c-bcad-9e6589da1873",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155tfT5Rh3rtnA99H19Naqt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22473,
      "cache_read_input_tokens": 49522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22473
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-23T11:37:05.372Z_

<details><summary>↩ Tool result · `toolu_01LaVkc3BHYYKL7NcspUoVb6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "2b38fcd3-61db-4c86-932f-f1e180b9f3c9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "oldString": "2v3 $\\auc = 0.644\\;[0.628,\\,0.658]$, $0.655\\;[0.640,\\,0.669]$, and $0.620\\;[0.605,\\,0.635]$",
    "newString": "2v3 $\\auc = 0.643\\;[0.628,\\,0.658]$, $0.655\\;[0.640,\\,0.669]$, and $0.622\\;[0.605,\\,0.635]$",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate generational depth estimation on ten model configurations spanning six architecture families:\nPythia-1.4B, Pythia-6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B, all in continuation mode except where noted.\nAll experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).\n\n%% ====================================================================\n\\subsection{$\\Kempirical \\leq 2$ Across Model Configurations (C4)}\n\\label{sec:kstar_boundary}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Pairwise $\\auc$ for adjacent depth pairs with bootstrap 95\\% CIs and permutation $p$-values for boundary rows.\n$\\Kempirical = 2$ requires 1v2 $\\auc > \\theta{=}0.60$ and 2v3 $\\auc < \\theta$; CIs quantify boundary uncertainty.\nExtended results (all models) in Table~\\ref{tab:kstar_ci_extended}.}\n\\label{tab:kstar_ci}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{lcccccccccc}\n\\toprule\n & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\n & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n\\midrule\n0v1 & .9956 & & .9722 & & .9860 & & .9971 & & .9638 & [.961,\\,.967] \\\\\n1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6074 & [.598,\\,.617]\\rlap{$^*$} & .5001 & [.496,\\,.519] & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} \\\\\n2v3 & .5893 & [.580,\\,.599] & .5440 & [.534,\\,.554] & .4973 & [.486,\\,.509] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] \\\\\n3v4 & .5435 & & .5051 & & .5024\\rlap{$^\\S$} & & .5409 & & .5276 & \\\\\n4v5 & .5340 & & .5079 & & .4942 & & .5141 & & .5085 & \\\\\n\\bottomrule\n\\multicolumn{11}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all starred boundary comparisons ($\\auc > \\theta$).} \\\\\n\\multicolumn{11}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.} \\\\\n\\multicolumn{11}{l}{\\footnotesize $^\\S$OLMo 2v3 (0.497) $<$ 3v4 (0.502): non-monotonic reversal within noise ($\\Delta = 0.005$).} \\\\\n\\multicolumn{11}{l}{\\footnotesize Full results for all 10 configurations (including LLaMA-8B, Mistral-7B, Qwen-base, Gemma-2-2B, and Pythia-6.9B) in Table~\\ref{tab:kstar_ci_extended}.}\n\\end{tabular}}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_auc_decay.pdf}\n\\caption{Pairwise $\\auc$ decay across adjacent depth pairs (0v1, 1v2, \\ldots, 4v5) for model-mode configurations (solid) and decoding strategies (dashed); shaded bands show bootstrap 95\\% confidence intervals. The horizontal dashed line marks $\\theta = 0.60$.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:kstar_ci} and Figure~\\ref{fig:auc_decay} show $\\Kempirical \\leq 2$ across all 10 configurations: 6/10 yield $\\Kempirical{=}2$ (Qwen$\\times$4, LLaMA-8B, Pythia-1.4B; 1v2 $\\auc$: 0.607--0.696; $p < 0.001$), while OLMo-1B, Mistral-7B, Pythia-6.9B, and Gemma-2-2B yield $\\Kempirical{=}1$ (1v2 $\\auc$: 0.500--0.598; Section~\\ref{sec:boundary_cases}).\nUnder Bonferroni correction (99.5\\% CIs), three of six $\\Kempirical{=}2$ configurations retain significance; the three marginal cases (Pythia-1.4B, Qwen-cont, LLaMA-8B; CI lower bounds 0.593--0.599) reflect narrow effect sizes rather than classification failure.\nBy architecture family: Qwen (4/4) and LLaMA (1/1) yield $\\Kempirical{\\geq}2$ at nominal significance; OLMo (1/1), Mistral (1/1), and Gemma (1/1) yield $\\Kempirical{=}1$; Pythia exhibits a scale-dependent split (1.4B: $\\Kempirical{=}2$, 6.9B: $\\Kempirical{=}1$).\nLLaMA-3.1-8B confirms $\\Kempirical{=}2$ (0v1 $\\auc = 0.9224$, 1v2 $\\auc = 0.6123\\;[0.603,\\,0.622]$; CI lower bound above $\\theta$; Table~\\ref{tab:kstar_ci_extended}).\nAll four decoding strategies likewise yield $\\Kempirical{=}2$ (Table~\\ref{tab:s2_decoding}).\nThe 1v2 spread due to generation mode ($\\Delta = 8.4$\\,pp within Qwen) exceeds the spread across $\\Kempirical{=}2$ continuation models ($\\Delta = 1.9$\\,pp).\n\n\\paragraph{Scale and instruction-tuning invariance.}\n$\\Kempirical{=}2$ persists from 1.5B through 8B: Qwen-7B (1v2 $\\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\\auc = 0.6123$) both exceed $\\theta$, despite progressively reduced 0v1 signal (0.9638 and 0.9224 vs.\\ $> 0.99$ at $\\leq$1.5B).\nA base-vs.-instruct ablation at 1.5B likewise yields $\\Kempirical = 2$ (1v2 $\\auc = 0.626$), confirming the boundary is not an instruction-tuning artifact.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/fig_kstar_theta.pdf}\n\\caption{$\\Kempirical(\\theta)$ sensitivity curve for five configurations. $\\Kempirical$: maximum discriminable depth; $\\theta$: AUC decision threshold. Four of five configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (dashed line); OLMo yields $\\Kempirical{=}1$. At $\\theta{=}0.70$, all drop to $\\Kempirical{=}1$.}\n\\label{fig:kstar_theta}\n\\end{figure*}\n\nFigure~\\ref{fig:kstar_theta} displays the sensitivity surface across $\\theta \\in [0.55, 0.70]$: four of five configurations shown yield $\\Kempirical = 2$ within $\\theta \\in [0.51, 0.61]$ (OLMo: $\\Kempirical = 1$ throughout); at $\\theta{=}0.55$, two Qwen configurations reach $\\Kempirical = 3$; at $\\theta{=}0.70$, all drop to $\\Kempirical = 1$.\n\n%% ====================================================================\n\\subsection{Cross-Model Transfer}\n\\label{sec:transfer}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3_transfer_heatmap.pdf}\n\\caption{Cross-model transfer heatmap (continuation-mode models). Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\\leftrightarrow$OLMo: 90--92\\%.}\n\\label{fig:transfer_heatmap}\n\\end{figure}\n\nContinuation-mode classifiers transfer well across generators (Figure~\\ref{fig:transfer_heatmap}; full matrix in Table~\\ref{tab:s1_transfer}): Pythia$\\leftrightarrow$OLMo retains 90--92\\%, Qwen-cont$\\leftrightarrow$Pythia 84--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\% (0v1 cross-model $\\auc > 0.96$ for all pairs).\nQwen-rewrite classifiers transfer poorly (61--63\\%), confirming reliance on mode-specific artifacts rather than generalizable depth features.\n\n\\paragraph{Cross-scorer validation.}\nReplacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\\ref{tab:crossscorer}).\nFeature ranking independence is a strong result: the same features dominate under all scorers.\n$\\Kempirical$ agreement, however, is signal-strength dependent: Qwen-rewrite (strong signal, 1v2 $\\auc = 0.696$) retains $\\Kempirical{=}2$ under all scorers, but Qwen-continuation (marginal, 1v2 $\\auc = 0.611$, only 0.011 above $\\theta$) drops to $\\Kempirical{=}1$ (Pythia: $0.5923$; OLMo: $0.5858$).\nA three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair; Table~\\ref{tab:anova_crossscorer}) confirms a statistically significant but modest Scorer main effect ($\\eta^2_p{=}.166$, $p < .001$) and a significant Generator$\\times$Scorer interaction ($\\eta^2_p{=}.146$), indicating that absolute AUC values are scorer-dependent even when $\\Kempirical$ classifications largely agree.\n\n%% ====================================================================\n\\subsection{Feature Ordering and Generation Mode}\n\\label{sec:feature_degradation}\n\\label{sec:generation_mode}\n\nAmong continuation-mode models, single-feature $\\auc$ rankings are highly correlated ($\\rho \\geq 0.85$; Table~\\ref{tab:top_features}).\nThe top-3 features (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std}, \\texttt{surp\\_d2\\_std}) are shared across all three families, revealing that autoregressive generation progressively damps surprisal variability.\nQwen-rewrite diverges (\\texttt{freq\\_entropy} dominates), consistent with its poor cross-model transfer (61--63\\%).\nWithin Qwen, rewrite yields 1v2 $\\auc = 0.6955$ vs.\\ continuation's $0.6112$ ($\\Delta = +8.4$\\,pp); continuation mode is therefore recommended as the canonical condition.\n\n%% ====================================================================\n\\subsection{Neural Probe}\n\\label{sec:neural_probe}\n\nReplacing the 15D features with frozen encoder hidden states (MLP probe; Table~\\ref{tab:neural_probe_crossmodel}), Qwen achieves $\\Kempirical^{\\text{neural}} = 3$ (2v3 $\\auc = 0.6159$), while Pythia remains at $\\Kempirical^{\\text{neural}} = 2$ ($\\auc_{2v3} = 0.5963$); OLMo yields $\\Kempirical^{\\text{neural}} = 1$ (1v2 $\\auc = 0.5054$, consistent with its 15D boundary).\nWe hypothesize that the Qwen-only elevation reflects self-familiarity artifacts, consistent with the poor transfer observed in Section~\\ref{sec:transfer}; the 15D features yield $\\Kempirical = 2$ for most families (OLMo: $\\Kempirical = 1$).\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\\ $d{+}1$ text. $\\Kempirical^{\\text{neural}}$: maximum depth where AUC exceeds $\\theta = 0.60$.}\n\\label{tab:neural_probe_crossmodel}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & $\\Kempirical^{\\text{neural}}$ \\\\\n\\midrule\nQwen-1.5B  & 0.6159 & $[0.610,\\,0.622]$ & 3 \\\\\nPythia-1.4B & 0.5963 & $[0.589,\\,0.603]$ & 2 \\\\\nOLMo-1B    & 0.5056 & $[0.497,\\,0.516]$ & 1\\rlap{$^\\dagger$} \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$OLMo 1v2 $\\auc = 0.5054$ (below $\\theta$); $\\Kempirical^{\\text{neural}} = 1$.}\n\\end{tabular}}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Cross-Domain Variation}\n\\label{sec:cross_domain}\n\nThe preceding experiments use C4 (general web text).\nTo test domain dependence, we evaluate on Wikipedia ($n{=}5{,}000$) and arXiv abstracts ($n{=}2{,}200$) across three architecture families.\nWikipedia yields $\\Kempirical{=}2$ (1v2 $\\auc = 0.619$, 2v3 $\\auc = 0.550$; Table~\\ref{tab:domain_kstar}), matching the C4 baseline.\nQwen-1.5B, Pythia-1.4B, and LLaMA-3.1-8B yield $\\Kempirical{=}3$ for arXiv (Table~\\ref{tab:domain_kstar}): 2v3 $\\auc = 0.644\\;[0.628,\\,0.658]$, $0.655\\;[0.640,\\,0.669]$, and $0.620\\;[0.605,\\,0.635]$ respectively (bootstrap CI lower bounds above $\\theta$; permutation $p < 0.001$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.\nThe elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\\ ${\\sim}0.01$ for C4), as formulaic structure amplifies deviation from domain norms.\nWe additionally evaluate on CodeSearchNet Python ($n{=}5{,}000$, continuation mode); all four tested models (Qwen-1.5B, Qwen-7B, LLaMA-8B, Mistral-7B) yield $\\Kempirical{=}2$ (Table~\\ref{tab:domain_kstar}), matching the C4 baseline.\n\n\\begin{table}[t]\n\\centering\n\\footnotesize\n\\caption{Cross-domain $\\Kempirical$ comparison. $\\Kempirical{=}2$ for C4, Wikipedia, and Code; $\\Kempirical{=}3$ for arXiv (three families confirmed in text; representative rows shown).}\n\\label{tab:domain_kstar}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Model} & \\textbf{1v2 $\\auc$} & \\textbf{2v3 $\\auc$} & $\\Kempirical$ \\\\\n\\midrule\narXiv & Qwen-1.5B\\rlap{$^\\dagger$}  & .858 & .644 & 3 \\\\\narXiv & Pythia-1.4B & .805 & .655 & 3 \\\\\nC4    & Qwen-1.5B\\rlap{$^\\dagger$}  & .626 & .550 & 2 \\\\\nWiki  & Qwen-1.5B\\rlap{$^\\dagger$}  & .619 & .550 & 2 \\\\\nCode  & Qwen-1.5B\\rlap{$^\\dagger$}  & .738 & .530 & 2 \\\\\nCode  & LLaMA-8B   & .739 & .510 & 2 \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$Qwen2.5-1.5B (base, continuation mode).}\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Robustness.}\n\\label{sec:robustness}\n$\\Kempirical{=}2$ holds across segment lengths of 128, 256, and 512 tokens (Table~\\ref{tab:s11_length_ablation}); at 512 tokens the 1v2 CI lower bound falls marginally below $\\theta$ but 2v3 remains well below $\\theta$ at all lengths ($\\leq 0.572$).\nSeed robustness testing (seed $= 123$ vs.\\ primary $= 42$; Table~\\ref{tab:seed_robustness}) confirms $\\Kempirical$ stability in 2/3 configurations; the one marginal shift (Qwen-Wikipedia $\\Kempirical{=}2 \\to 3$, 2v3 $\\auc = 0.607$) has one of five folds below $\\theta$.\nThe ${\\pm}9$\\,pp absolute AUC variation across seeds strengthens the case for threshold-based $\\Kempirical$ over raw AUC comparisons.\n\n%% ====================================================================\n\\subsection{Binary Detector Confidence}\n\\label{sec:binary_confidence}\n\nBinary detectors (DivEye~\\cite{basani2026diveye}, Binoculars~\\cite{hans2024binoculars}) remain effective for human-vs.-machine classification but provide no usable depth signal beyond this binary boundary.\nPairwise $\\auc$ yields $\\Kempirical^{\\text{binary}} \\leq 1$; moderate rank correlations with depth ($|\\rho| = 0.06$--$0.46$; Table~\\ref{tab:s9_binary_spearman}) are driven entirely by the 0v1 gap rather than fine-grained depth discrimination, and multiple conditions exhibit non-monotonic AUC at deeper pairs.\n",
    "structuredPatch": [
      {
        "oldStart": 125,
        "oldLines": 7,
        "newStart": 125,
        "newLines": 7,
        "lines": [
          " The preceding experiments use C4 (general web text).",
          " To test domain dependence, we evaluate on Wikipedia ($n{=}5{,}000$) and arXiv abstracts ($n{=}2{,}200$) across three architecture families.",
          " Wikipedia yields $\\Kempirical{=}2$ (1v2 $\\auc = 0.619$, 2v3 $\\auc = 0.550$; Table~\\ref{tab:domain_kstar}), matching the C4 baseline.",
          "-Qwen-1.5B, Pythia-1.4B, and LLaMA-3.1-8B yield $\\Kempirical{=}3$ for arXiv (Table~\\ref{tab:domain_kstar}): 2v3 $\\auc = 0.644\\;[0.628,\\,0.658]$, $0.655\\;[0.640,\\,0.669]$, and $0.620\\;[0.605,\\,0.635]$ respectively (bootstrap CI lower bounds above $\\theta$; permutation $p < 0.001$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.",
          "+Qwen-1.5B, Pythia-1.4B, and LLaMA-3.1-8B yield $\\Kempirical{=}3$ for arXiv (Table~\\ref{tab:domain_kstar}): 2v3 $\\auc = 0.643\\;[0.628,\\,0.658]$, $0.655\\;[0.640,\\,0.669]$, and $0.622\\;[0.605,\\,0.635]$ respectively (bootstrap CI lower bounds above $\\theta$; permutation $p < 0.001$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.",
          " The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\\ ${\\sim}0.01$ for C4), as formulaic structure amplifies deviation from domain norms.",
          " We additionally evaluate on CodeSearchNet Python ($n{=}5{,}000$, continuation mode); all four tested models (Qwen-1.5B, Qwen-7B, LLaMA-8B, Mistral-7B) yield $\\Kempirical{=}2$ (Table~\\ref{tab:domain_kstar}), matching the C4 baseline.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 686_

<details open><summary>🔧 Tool call — Edit · `toolu_01579zdyS2GJiQRw6fyJACuK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "old_string": "arXiv & Qwen-1.5B\\rlap{$^\\dagger$}  & .858 & .644 & 3 \\\\",
  "new_string": "arXiv & Qwen-1.5B\\rlap{$^\\dagger$}  & .858 & .643 & 3 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "5ec4da6e-484f-4834-9dce-e95799bf3ef2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155tfT5Rh3rtnA99H19Naqt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22473,
      "cache_read_input_tokens": 49522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22473
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-23T11:37:07.006Z_

<details><summary>↩ Tool result · `toolu_01579zdyS2GJiQRw6fyJACuK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "6dcb93cd-9da1-4657-9808-f616be021b65",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "oldString": "arXiv & Qwen-1.5B\\rlap{$^\\dagger$}  & .858 & .644 & 3 \\\\",
    "newString": "arXiv & Qwen-1.5B\\rlap{$^\\dagger$}  & .858 & .643 & 3 \\\\",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate generational depth estimation on ten model configurations spanning six architecture families:\nPythia-1.4B, Pythia-6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B, all in continuation mode except where noted.\nAll experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).\n\n%% ====================================================================\n\\subsection{$\\Kempirical \\leq 2$ Across Model Configurations (C4)}\n\\label{sec:kstar_boundary}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Pairwise $\\auc$ for adjacent depth pairs with bootstrap 95\\% CIs and permutation $p$-values for boundary rows.\n$\\Kempirical = 2$ requires 1v2 $\\auc > \\theta{=}0.60$ and 2v3 $\\auc < \\theta$; CIs quantify boundary uncertainty.\nExtended results (all models) in Table~\\ref{tab:kstar_ci_extended}.}\n\\label{tab:kstar_ci}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{lcccccccccc}\n\\toprule\n & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\n & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n\\midrule\n0v1 & .9956 & & .9722 & & .9860 & & .9971 & & .9638 & [.961,\\,.967] \\\\\n1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6074 & [.598,\\,.617]\\rlap{$^*$} & .5001 & [.496,\\,.519] & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} \\\\\n2v3 & .5893 & [.580,\\,.599] & .5440 & [.534,\\,.554] & .4973 & [.486,\\,.509] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] \\\\\n3v4 & .5435 & & .5051 & & .5024\\rlap{$^\\S$} & & .5409 & & .5276 & \\\\\n4v5 & .5340 & & .5079 & & .4942 & & .5141 & & .5085 & \\\\\n\\bottomrule\n\\multicolumn{11}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all starred boundary comparisons ($\\auc > \\theta$).} \\\\\n\\multicolumn{11}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.} \\\\\n\\multicolumn{11}{l}{\\footnotesize $^\\S$OLMo 2v3 (0.497) $<$ 3v4 (0.502): non-monotonic reversal within noise ($\\Delta = 0.005$).} \\\\\n\\multicolumn{11}{l}{\\footnotesize Full results for all 10 configurations (including LLaMA-8B, Mistral-7B, Qwen-base, Gemma-2-2B, and Pythia-6.9B) in Table~\\ref{tab:kstar_ci_extended}.}\n\\end{tabular}}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_auc_decay.pdf}\n\\caption{Pairwise $\\auc$ decay across adjacent depth pairs (0v1, 1v2, \\ldots, 4v5) for model-mode configurations (solid) and decoding strategies (dashed); shaded bands show bootstrap 95\\% confidence intervals. The horizontal dashed line marks $\\theta = 0.60$.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:kstar_ci} and Figure~\\ref{fig:auc_decay} show $\\Kempirical \\leq 2$ across all 10 configurations: 6/10 yield $\\Kempirical{=}2$ (Qwen$\\times$4, LLaMA-8B, Pythia-1.4B; 1v2 $\\auc$: 0.607--0.696; $p < 0.001$), while OLMo-1B, Mistral-7B, Pythia-6.9B, and Gemma-2-2B yield $\\Kempirical{=}1$ (1v2 $\\auc$: 0.500--0.598; Section~\\ref{sec:boundary_cases}).\nUnder Bonferroni correction (99.5\\% CIs), three of six $\\Kempirical{=}2$ configurations retain significance; the three marginal cases (Pythia-1.4B, Qwen-cont, LLaMA-8B; CI lower bounds 0.593--0.599) reflect narrow effect sizes rather than classification failure.\nBy architecture family: Qwen (4/4) and LLaMA (1/1) yield $\\Kempirical{\\geq}2$ at nominal significance; OLMo (1/1), Mistral (1/1), and Gemma (1/1) yield $\\Kempirical{=}1$; Pythia exhibits a scale-dependent split (1.4B: $\\Kempirical{=}2$, 6.9B: $\\Kempirical{=}1$).\nLLaMA-3.1-8B confirms $\\Kempirical{=}2$ (0v1 $\\auc = 0.9224$, 1v2 $\\auc = 0.6123\\;[0.603,\\,0.622]$; CI lower bound above $\\theta$; Table~\\ref{tab:kstar_ci_extended}).\nAll four decoding strategies likewise yield $\\Kempirical{=}2$ (Table~\\ref{tab:s2_decoding}).\nThe 1v2 spread due to generation mode ($\\Delta = 8.4$\\,pp within Qwen) exceeds the spread across $\\Kempirical{=}2$ continuation models ($\\Delta = 1.9$\\,pp).\n\n\\paragraph{Scale and instruction-tuning invariance.}\n$\\Kempirical{=}2$ persists from 1.5B through 8B: Qwen-7B (1v2 $\\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\\auc = 0.6123$) both exceed $\\theta$, despite progressively reduced 0v1 signal (0.9638 and 0.9224 vs.\\ $> 0.99$ at $\\leq$1.5B).\nA base-vs.-instruct ablation at 1.5B likewise yields $\\Kempirical = 2$ (1v2 $\\auc = 0.626$), confirming the boundary is not an instruction-tuning artifact.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/fig_kstar_theta.pdf}\n\\caption{$\\Kempirical(\\theta)$ sensitivity curve for five configurations. $\\Kempirical$: maximum discriminable depth; $\\theta$: AUC decision threshold. Four of five configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (dashed line); OLMo yields $\\Kempirical{=}1$. At $\\theta{=}0.70$, all drop to $\\Kempirical{=}1$.}\n\\label{fig:kstar_theta}\n\\end{figure*}\n\nFigure~\\ref{fig:kstar_theta} displays the sensitivity surface across $\\theta \\in [0.55, 0.70]$: four of five configurations shown yield $\\Kempirical = 2$ within $\\theta \\in [0.51, 0.61]$ (OLMo: $\\Kempirical = 1$ throughout); at $\\theta{=}0.55$, two Qwen configurations reach $\\Kempirical = 3$; at $\\theta{=}0.70$, all drop to $\\Kempirical = 1$.\n\n%% ====================================================================\n\\subsection{Cross-Model Transfer}\n\\label{sec:transfer}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3_transfer_heatmap.pdf}\n\\caption{Cross-model transfer heatmap (continuation-mode models). Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\\leftrightarrow$OLMo: 90--92\\%.}\n\\label{fig:transfer_heatmap}\n\\end{figure}\n\nContinuation-mode classifiers transfer well across generators (Figure~\\ref{fig:transfer_heatmap}; full matrix in Table~\\ref{tab:s1_transfer}): Pythia$\\leftrightarrow$OLMo retains 90--92\\%, Qwen-cont$\\leftrightarrow$Pythia 84--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\% (0v1 cross-model $\\auc > 0.96$ for all pairs).\nQwen-rewrite classifiers transfer poorly (61--63\\%), confirming reliance on mode-specific artifacts rather than generalizable depth features.\n\n\\paragraph{Cross-scorer validation.}\nReplacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\\ref{tab:crossscorer}).\nFeature ranking independence is a strong result: the same features dominate under all scorers.\n$\\Kempirical$ agreement, however, is signal-strength dependent: Qwen-rewrite (strong signal, 1v2 $\\auc = 0.696$) retains $\\Kempirical{=}2$ under all scorers, but Qwen-continuation (marginal, 1v2 $\\auc = 0.611$, only 0.011 above $\\theta$) drops to $\\Kempirical{=}1$ (Pythia: $0.5923$; OLMo: $0.5858$).\nA three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair; Table~\\ref{tab:anova_crossscorer}) confirms a statistically significant but modest Scorer main effect ($\\eta^2_p{=}.166$, $p < .001$) and a significant Generator$\\times$Scorer interaction ($\\eta^2_p{=}.146$), indicating that absolute AUC values are scorer-dependent even when $\\Kempirical$ classifications largely agree.\n\n%% ====================================================================\n\\subsection{Feature Ordering and Generation Mode}\n\\label{sec:feature_degradation}\n\\label{sec:generation_mode}\n\nAmong continuation-mode models, single-feature $\\auc$ rankings are highly correlated ($\\rho \\geq 0.85$; Table~\\ref{tab:top_features}).\nThe top-3 features (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std}, \\texttt{surp\\_d2\\_std}) are shared across all three families, revealing that autoregressive generation progressively damps surprisal variability.\nQwen-rewrite diverges (\\texttt{freq\\_entropy} dominates), consistent with its poor cross-model transfer (61--63\\%).\nWithin Qwen, rewrite yields 1v2 $\\auc = 0.6955$ vs.\\ continuation's $0.6112$ ($\\Delta = +8.4$\\,pp); continuation mode is therefore recommended as the canonical condition.\n\n%% ====================================================================\n\\subsection{Neural Probe}\n\\label{sec:neural_probe}\n\nReplacing the 15D features with frozen encoder hidden states (MLP probe; Table~\\ref{tab:neural_probe_crossmodel}), Qwen achieves $\\Kempirical^{\\text{neural}} = 3$ (2v3 $\\auc = 0.6159$), while Pythia remains at $\\Kempirical^{\\text{neural}} = 2$ ($\\auc_{2v3} = 0.5963$); OLMo yields $\\Kempirical^{\\text{neural}} = 1$ (1v2 $\\auc = 0.5054$, consistent with its 15D boundary).\nWe hypothesize that the Qwen-only elevation reflects self-familiarity artifacts, consistent with the poor transfer observed in Section~\\ref{sec:transfer}; the 15D features yield $\\Kempirical = 2$ for most families (OLMo: $\\Kempirical = 1$).\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\\ $d{+}1$ text. $\\Kempirical^{\\text{neural}}$: maximum depth where AUC exceeds $\\theta = 0.60$.}\n\\label{tab:neural_probe_crossmodel}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & $\\Kempirical^{\\text{neural}}$ \\\\\n\\midrule\nQwen-1.5B  & 0.6159 & $[0.610,\\,0.622]$ & 3 \\\\\nPythia-1.4B & 0.5963 & $[0.589,\\,0.603]$ & 2 \\\\\nOLMo-1B    & 0.5056 & $[0.497,\\,0.516]$ & 1\\rlap{$^\\dagger$} \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$OLMo 1v2 $\\auc = 0.5054$ (below $\\theta$); $\\Kempirical^{\\text{neural}} = 1$.}\n\\end{tabular}}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Cross-Domain Variation}\n\\label{sec:cross_domain}\n\nThe preceding experiments use C4 (general web text).\nTo test domain dependence, we evaluate on Wikipedia ($n{=}5{,}000$) and arXiv abstracts ($n{=}2{,}200$) across three architecture families.\nWikipedia yields $\\Kempirical{=}2$ (1v2 $\\auc = 0.619$, 2v3 $\\auc = 0.550$; Table~\\ref{tab:domain_kstar}), matching the C4 baseline.\nQwen-1.5B, Pythia-1.4B, and LLaMA-3.1-8B yield $\\Kempirical{=}3$ for arXiv (Table~\\ref{tab:domain_kstar}): 2v3 $\\auc = 0.643\\;[0.628,\\,0.658]$, $0.655\\;[0.640,\\,0.669]$, and $0.622\\;[0.605,\\,0.635]$ respectively (bootstrap CI lower bounds above $\\theta$; permutation $p < 0.001$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.\nThe elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\\ ${\\sim}0.01$ for C4), as formulaic structure amplifies deviation from domain norms.\nWe additionally evaluate on CodeSearchNet Python ($n{=}5{,}000$, continuation mode); all four tested models (Qwen-1.5B, Qwen-7B, LLaMA-8B, Mistral-7B) yield $\\Kempirical{=}2$ (Table~\\ref{tab:domain_kstar}), matching the C4 baseline.\n\n\\begin{table}[t]\n\\centering\n\\footnotesize\n\\caption{Cross-domain $\\Kempirical$ comparison. $\\Kempirical{=}2$ for C4, Wikipedia, and Code; $\\Kempirical{=}3$ for arXiv (three families confirmed in text; representative rows shown).}\n\\label{tab:domain_kstar}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Model} & \\textbf{1v2 $\\auc$} & \\textbf{2v3 $\\auc$} & $\\Kempirical$ \\\\\n\\midrule\narXiv & Qwen-1.5B\\rlap{$^\\dagger$}  & .858 & .644 & 3 \\\\\narXiv & Pythia-1.4B & .805 & .655 & 3 \\\\\nC4    & Qwen-1.5B\\rlap{$^\\dagger$}  & .626 & .550 & 2 \\\\\nWiki  & Qwen-1.5B\\rlap{$^\\dagger$}  & .619 & .550 & 2 \\\\\nCode  & Qwen-1.5B\\rlap{$^\\dagger$}  & .738 & .530 & 2 \\\\\nCode  & LLaMA-8B   & .739 & .510 & 2 \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$Qwen2.5-1.5B (base, continuation mode).}\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Robustness.}\n\\label{sec:robustness}\n$\\Kempirical{=}2$ holds across segment lengths of 128, 256, and 512 tokens (Table~\\ref{tab:s11_length_ablation}); at 512 tokens the 1v2 CI lower bound falls marginally below $\\theta$ but 2v3 remains well below $\\theta$ at all lengths ($\\leq 0.572$).\nSeed robustness testing (seed $= 123$ vs.\\ primary $= 42$; Table~\\ref{tab:seed_robustness}) confirms $\\Kempirical$ stability in 2/3 configurations; the one marginal shift (Qwen-Wikipedia $\\Kempirical{=}2 \\to 3$, 2v3 $\\auc = 0.607$) has one of five folds below $\\theta$.\nThe ${\\pm}9$\\,pp absolute AUC variation across seeds strengthens the case for threshold-based $\\Kempirical$ over raw AUC comparisons.\n\n%% ====================================================================\n\\subsection{Binary Detector Confidence}\n\\label{sec:binary_confidence}\n\nBinary detectors (DivEye~\\cite{basani2026diveye}, Binoculars~\\cite{hans2024binoculars}) remain effective for human-vs.-machine classification but provide no usable depth signal beyond this binary boundary.\nPairwise $\\auc$ yields $\\Kempirical^{\\text{binary}} \\leq 1$; moderate rank correlations with depth ($|\\rho| = 0.06$--$0.46$; Table~\\ref{tab:s9_binary_spearman}) are driven entirely by the 0v1 gap rather than fine-grained depth discrimination, and multiple conditions exhibit non-monotonic AUC at deeper pairs.\n",
    "structuredPatch": [
      {
        "oldStart": 139,
        "oldLines": 7,
        "newStart": 139,
        "newLines": 7,
        "lines": [
          " \\toprule",
          " \\textbf{Domain} & \\textbf{Model} & \\textbf{1v2 $\\auc$} & \\textbf{2v3 $\\auc$} & $\\Kempirical$ \\\\",
          " \\midrule",
          "-arXiv & Qwen-1.5B\\rlap{$^\\dagger$}  & .858 & .644 & 3 \\\\",
          "+arXiv & Qwen-1.5B\\rlap{$^\\dagger$}  & .858 & .643 & 3 \\\\",
          " arXiv & Pythia-1.4B & .805 & .655 & 3 \\\\",
          " C4    & Qwen-1.5B\\rlap{$^\\dagger$}  & .626 & .550 & 2 \\\\",
          " Wiki  & Qwen-1.5B\\rlap{$^\\dagger$}  & .619 & .550 & 2 \\\\"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 688_

<details open><summary>🔧 Tool call — Edit · `toolu_01FWivCd83irhpbXA5A9vNCA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "old_string": "Code  & LLaMA-8B   & .739 & .510 & 2 \\\\",
  "new_string": "Code  & LLaMA-8B   & .739 & .511 & 2 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "2f4f5af6-cb5c-47cb-b630-c802638aae87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155tfT5Rh3rtnA99H19Naqt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22473,
      "cache_read_input_tokens": 49522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22473
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-23T11:37:07.698Z_

<details><summary>↩ Tool result · `toolu_01FWivCd83irhpbXA5A9vNCA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "43e7ed95-1e9e-424d-87d2-bf638eb96e15",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "oldString": "Code  & LLaMA-8B   & .739 & .510 & 2 \\\\",
    "newString": "Code  & LLaMA-8B   & .739 & .511 & 2 \\\\",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate generational depth estimation on ten model configurations spanning six architecture families:\nPythia-1.4B, Pythia-6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B, all in continuation mode except where noted.\nAll experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).\n\n%% ====================================================================\n\\subsection{$\\Kempirical \\leq 2$ Across Model Configurations (C4)}\n\\label{sec:kstar_boundary}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Pairwise $\\auc$ for adjacent depth pairs with bootstrap 95\\% CIs and permutation $p$-values for boundary rows.\n$\\Kempirical = 2$ requires 1v2 $\\auc > \\theta{=}0.60$ and 2v3 $\\auc < \\theta$; CIs quantify boundary uncertainty.\nExtended results (all models) in Table~\\ref{tab:kstar_ci_extended}.}\n\\label{tab:kstar_ci}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{lcccccccccc}\n\\toprule\n & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\n & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n\\midrule\n0v1 & .9956 & & .9722 & & .9860 & & .9971 & & .9638 & [.961,\\,.967] \\\\\n1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6074 & [.598,\\,.617]\\rlap{$^*$} & .5001 & [.496,\\,.519] & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} \\\\\n2v3 & .5893 & [.580,\\,.599] & .5440 & [.534,\\,.554] & .4973 & [.486,\\,.509] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] \\\\\n3v4 & .5435 & & .5051 & & .5024\\rlap{$^\\S$} & & .5409 & & .5276 & \\\\\n4v5 & .5340 & & .5079 & & .4942 & & .5141 & & .5085 & \\\\\n\\bottomrule\n\\multicolumn{11}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all starred boundary comparisons ($\\auc > \\theta$).} \\\\\n\\multicolumn{11}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.} \\\\\n\\multicolumn{11}{l}{\\footnotesize $^\\S$OLMo 2v3 (0.497) $<$ 3v4 (0.502): non-monotonic reversal within noise ($\\Delta = 0.005$).} \\\\\n\\multicolumn{11}{l}{\\footnotesize Full results for all 10 configurations (including LLaMA-8B, Mistral-7B, Qwen-base, Gemma-2-2B, and Pythia-6.9B) in Table~\\ref{tab:kstar_ci_extended}.}\n\\end{tabular}}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_auc_decay.pdf}\n\\caption{Pairwise $\\auc$ decay across adjacent depth pairs (0v1, 1v2, \\ldots, 4v5) for model-mode configurations (solid) and decoding strategies (dashed); shaded bands show bootstrap 95\\% confidence intervals. The horizontal dashed line marks $\\theta = 0.60$.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:kstar_ci} and Figure~\\ref{fig:auc_decay} show $\\Kempirical \\leq 2$ across all 10 configurations: 6/10 yield $\\Kempirical{=}2$ (Qwen$\\times$4, LLaMA-8B, Pythia-1.4B; 1v2 $\\auc$: 0.607--0.696; $p < 0.001$), while OLMo-1B, Mistral-7B, Pythia-6.9B, and Gemma-2-2B yield $\\Kempirical{=}1$ (1v2 $\\auc$: 0.500--0.598; Section~\\ref{sec:boundary_cases}).\nUnder Bonferroni correction (99.5\\% CIs), three of six $\\Kempirical{=}2$ configurations retain significance; the three marginal cases (Pythia-1.4B, Qwen-cont, LLaMA-8B; CI lower bounds 0.593--0.599) reflect narrow effect sizes rather than classification failure.\nBy architecture family: Qwen (4/4) and LLaMA (1/1) yield $\\Kempirical{\\geq}2$ at nominal significance; OLMo (1/1), Mistral (1/1), and Gemma (1/1) yield $\\Kempirical{=}1$; Pythia exhibits a scale-dependent split (1.4B: $\\Kempirical{=}2$, 6.9B: $\\Kempirical{=}1$).\nLLaMA-3.1-8B confirms $\\Kempirical{=}2$ (0v1 $\\auc = 0.9224$, 1v2 $\\auc = 0.6123\\;[0.603,\\,0.622]$; CI lower bound above $\\theta$; Table~\\ref{tab:kstar_ci_extended}).\nAll four decoding strategies likewise yield $\\Kempirical{=}2$ (Table~\\ref{tab:s2_decoding}).\nThe 1v2 spread due to generation mode ($\\Delta = 8.4$\\,pp within Qwen) exceeds the spread across $\\Kempirical{=}2$ continuation models ($\\Delta = 1.9$\\,pp).\n\n\\paragraph{Scale and instruction-tuning invariance.}\n$\\Kempirical{=}2$ persists from 1.5B through 8B: Qwen-7B (1v2 $\\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\\auc = 0.6123$) both exceed $\\theta$, despite progressively reduced 0v1 signal (0.9638 and 0.9224 vs.\\ $> 0.99$ at $\\leq$1.5B).\nA base-vs.-instruct ablation at 1.5B likewise yields $\\Kempirical = 2$ (1v2 $\\auc = 0.626$), confirming the boundary is not an instruction-tuning artifact.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/fig_kstar_theta.pdf}\n\\caption{$\\Kempirical(\\theta)$ sensitivity curve for five configurations. $\\Kempirical$: maximum discriminable depth; $\\theta$: AUC decision threshold. Four of five configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (dashed line); OLMo yields $\\Kempirical{=}1$. At $\\theta{=}0.70$, all drop to $\\Kempirical{=}1$.}\n\\label{fig:kstar_theta}\n\\end{figure*}\n\nFigure~\\ref{fig:kstar_theta} displays the sensitivity surface across $\\theta \\in [0.55, 0.70]$: four of five configurations shown yield $\\Kempirical = 2$ within $\\theta \\in [0.51, 0.61]$ (OLMo: $\\Kempirical = 1$ throughout); at $\\theta{=}0.55$, two Qwen configurations reach $\\Kempirical = 3$; at $\\theta{=}0.70$, all drop to $\\Kempirical = 1$.\n\n%% ====================================================================\n\\subsection{Cross-Model Transfer}\n\\label{sec:transfer}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3_transfer_heatmap.pdf}\n\\caption{Cross-model transfer heatmap (continuation-mode models). Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\\leftrightarrow$OLMo: 90--92\\%.}\n\\label{fig:transfer_heatmap}\n\\end{figure}\n\nContinuation-mode classifiers transfer well across generators (Figure~\\ref{fig:transfer_heatmap}; full matrix in Table~\\ref{tab:s1_transfer}): Pythia$\\leftrightarrow$OLMo retains 90--92\\%, Qwen-cont$\\leftrightarrow$Pythia 84--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\% (0v1 cross-model $\\auc > 0.96$ for all pairs).\nQwen-rewrite classifiers transfer poorly (61--63\\%), confirming reliance on mode-specific artifacts rather than generalizable depth features.\n\n\\paragraph{Cross-scorer validation.}\nReplacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\\ref{tab:crossscorer}).\nFeature ranking independence is a strong result: the same features dominate under all scorers.\n$\\Kempirical$ agreement, however, is signal-strength dependent: Qwen-rewrite (strong signal, 1v2 $\\auc = 0.696$) retains $\\Kempirical{=}2$ under all scorers, but Qwen-continuation (marginal, 1v2 $\\auc = 0.611$, only 0.011 above $\\theta$) drops to $\\Kempirical{=}1$ (Pythia: $0.5923$; OLMo: $0.5858$).\nA three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair; Table~\\ref{tab:anova_crossscorer}) confirms a statistically significant but modest Scorer main effect ($\\eta^2_p{=}.166$, $p < .001$) and a significant Generator$\\times$Scorer interaction ($\\eta^2_p{=}.146$), indicating that absolute AUC values are scorer-dependent even when $\\Kempirical$ classifications largely agree.\n\n%% ====================================================================\n\\subsection{Feature Ordering and Generation Mode}\n\\label{sec:feature_degradation}\n\\label{sec:generation_mode}\n\nAmong continuation-mode models, single-feature $\\auc$ rankings are highly correlated ($\\rho \\geq 0.85$; Table~\\ref{tab:top_features}).\nThe top-3 features (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std}, \\texttt{surp\\_d2\\_std}) are shared across all three families, revealing that autoregressive generation progressively damps surprisal variability.\nQwen-rewrite diverges (\\texttt{freq\\_entropy} dominates), consistent with its poor cross-model transfer (61--63\\%).\nWithin Qwen, rewrite yields 1v2 $\\auc = 0.6955$ vs.\\ continuation's $0.6112$ ($\\Delta = +8.4$\\,pp); continuation mode is therefore recommended as the canonical condition.\n\n%% ====================================================================\n\\subsection{Neural Probe}\n\\label{sec:neural_probe}\n\nReplacing the 15D features with frozen encoder hidden states (MLP probe; Table~\\ref{tab:neural_probe_crossmodel}), Qwen achieves $\\Kempirical^{\\text{neural}} = 3$ (2v3 $\\auc = 0.6159$), while Pythia remains at $\\Kempirical^{\\text{neural}} = 2$ ($\\auc_{2v3} = 0.5963$); OLMo yields $\\Kempirical^{\\text{neural}} = 1$ (1v2 $\\auc = 0.5054$, consistent with its 15D boundary).\nWe hypothesize that the Qwen-only elevation reflects self-familiarity artifacts, consistent with the poor transfer observed in Section~\\ref{sec:transfer}; the 15D features yield $\\Kempirical = 2$ for most families (OLMo: $\\Kempirical = 1$).\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\\ $d{+}1$ text. $\\Kempirical^{\\text{neural}}$: maximum depth where AUC exceeds $\\theta = 0.60$.}\n\\label{tab:neural_probe_crossmodel}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & $\\Kempirical^{\\text{neural}}$ \\\\\n\\midrule\nQwen-1.5B  & 0.6159 & $[0.610,\\,0.622]$ & 3 \\\\\nPythia-1.4B & 0.5963 & $[0.589,\\,0.603]$ & 2 \\\\\nOLMo-1B    & 0.5056 & $[0.497,\\,0.516]$ & 1\\rlap{$^\\dagger$} \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$OLMo 1v2 $\\auc = 0.5054$ (below $\\theta$); $\\Kempirical^{\\text{neural}} = 1$.}\n\\end{tabular}}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Cross-Domain Variation}\n\\label{sec:cross_domain}\n\nThe preceding experiments use C4 (general web text).\nTo test domain dependence, we evaluate on Wikipedia ($n{=}5{,}000$) and arXiv abstracts ($n{=}2{,}200$) across three architecture families.\nWikipedia yields $\\Kempirical{=}2$ (1v2 $\\auc = 0.619$, 2v3 $\\auc = 0.550$; Table~\\ref{tab:domain_kstar}), matching the C4 baseline.\nQwen-1.5B, Pythia-1.4B, and LLaMA-3.1-8B yield $\\Kempirical{=}3$ for arXiv (Table~\\ref{tab:domain_kstar}): 2v3 $\\auc = 0.643\\;[0.628,\\,0.658]$, $0.655\\;[0.640,\\,0.669]$, and $0.622\\;[0.605,\\,0.635]$ respectively (bootstrap CI lower bounds above $\\theta$; permutation $p < 0.001$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.\nThe elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\\ ${\\sim}0.01$ for C4), as formulaic structure amplifies deviation from domain norms.\nWe additionally evaluate on CodeSearchNet Python ($n{=}5{,}000$, continuation mode); all four tested models (Qwen-1.5B, Qwen-7B, LLaMA-8B, Mistral-7B) yield $\\Kempirical{=}2$ (Table~\\ref{tab:domain_kstar}), matching the C4 baseline.\n\n\\begin{table}[t]\n\\centering\n\\footnotesize\n\\caption{Cross-domain $\\Kempirical$ comparison. $\\Kempirical{=}2$ for C4, Wikipedia, and Code; $\\Kempirical{=}3$ for arXiv (three families confirmed in text; representative rows shown).}\n\\label{tab:domain_kstar}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Model} & \\textbf{1v2 $\\auc$} & \\textbf{2v3 $\\auc$} & $\\Kempirical$ \\\\\n\\midrule\narXiv & Qwen-1.5B\\rlap{$^\\dagger$}  & .858 & .643 & 3 \\\\\narXiv & Pythia-1.4B & .805 & .655 & 3 \\\\\nC4    & Qwen-1.5B\\rlap{$^\\dagger$}  & .626 & .550 & 2 \\\\\nWiki  & Qwen-1.5B\\rlap{$^\\dagger$}  & .619 & .550 & 2 \\\\\nCode  & Qwen-1.5B\\rlap{$^\\dagger$}  & .738 & .530 & 2 \\\\\nCode  & LLaMA-8B   & .739 & .510 & 2 \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$Qwen2.5-1.5B (base, continuation mode).}\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Robustness.}\n\\label{sec:robustness}\n$\\Kempirical{=}2$ holds across segment lengths of 128, 256, and 512 tokens (Table~\\ref{tab:s11_length_ablation}); at 512 tokens the 1v2 CI lower bound falls marginally below $\\theta$ but 2v3 remains well below $\\theta$ at all lengths ($\\leq 0.572$).\nSeed robustness testing (seed $= 123$ vs.\\ primary $= 42$; Table~\\ref{tab:seed_robustness}) confirms $\\Kempirical$ stability in 2/3 configurations; the one marginal shift (Qwen-Wikipedia $\\Kempirical{=}2 \\to 3$, 2v3 $\\auc = 0.607$) has one of five folds below $\\theta$.\nThe ${\\pm}9$\\,pp absolute AUC variation across seeds strengthens the case for threshold-based $\\Kempirical$ over raw AUC comparisons.\n\n%% ====================================================================\n\\subsection{Binary Detector Confidence}\n\\label{sec:binary_confidence}\n\nBinary detectors (DivEye~\\cite{basani2026diveye}, Binoculars~\\cite{hans2024binoculars}) remain effective for human-vs.-machine classification but provide no usable depth signal beyond this binary boundary.\nPairwise $\\auc$ yields $\\Kempirical^{\\text{binary}} \\leq 1$; moderate rank correlations with depth ($|\\rho| = 0.06$--$0.46$; Table~\\ref{tab:s9_binary_spearman}) are driven entirely by the 0v1 gap rather than fine-grained depth discrimination, and multiple conditions exhibit non-monotonic AUC at deeper pairs.\n",
    "structuredPatch": [
      {
        "oldStart": 144,
        "oldLines": 7,
        "newStart": 144,
        "newLines": 7,
        "lines": [
          " C4    & Qwen-1.5B\\rlap{$^\\dagger$}  & .626 & .550 & 2 \\\\",
          " Wiki  & Qwen-1.5B\\rlap{$^\\dagger$}  & .619 & .550 & 2 \\\\",
          " Code  & Qwen-1.5B\\rlap{$^\\dagger$}  & .738 & .530 & 2 \\\\",
          "-Code  & LLaMA-8B   & .739 & .510 & 2 \\\\",
          "+Code  & LLaMA-8B   & .739 & .511 & 2 \\\\",
          " \\bottomrule",
          " \\multicolumn{5}{l}{\\footnotesize $^\\dagger$Qwen2.5-1.5B (base, continuation mode).}",
          " \\end{tabular}}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 690_

<details open><summary>🔧 Tool call — Edit · `toolu_01EFvYd9yG4wGTHkwzJwFkmt`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "old_string": "2v3 & .561 & .550 & .644$^*$ \\\\",
  "new_string": "2v3 & .561 & .550 & .643$^*$ \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "4d3e5fcb-165f-4fc1-bd05-1a68cb5f6187",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155tfT5Rh3rtnA99H19Naqt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22473,
      "cache_read_input_tokens": 49522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22473
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-23T11:37:09.137Z_

<details><summary>↩ Tool result · `toolu_01EFvYd9yG4wGTHkwzJwFkmt`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "8430e1ca-2ab3-4578-962e-914038bdd7c6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "oldString": "2v3 & .561 & .550 & .644$^*$ \\\\",
    "newString": "2v3 & .561 & .550 & .643$^*$ \\\\",
    "originalFile": "\\appendix\n\\section{Supplementary Materials}\n\\label{sec:appendix}\n\nThis appendix provides supplementary figures, detailed experimental tables, dataset statistics, and complete feature descriptions referenced in the main text.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_filtering_strategies.pdf}\n\\caption{Downstream performance of all filtering strategies (5 seeds, $\\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}\n\\label{fig:filtering_strategies}\n\\end{figure}\n\n\\paragraph{Feature ranking and cross-model consistency.}\nTable~\\ref{tab:top_features} reports per-model single-feature AUC rankings.\nSurprisal derivative features (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_d2\\_std}) consistently rank among the top three across all continuation-mode models (Pythia, OLMo, Qwen-cont), with pairwise Spearman $\\rho \\geq 0.85$.\nThe rewrite-mode model (Qwen-rw) diverges by placing \\texttt{freq\\_entropy} first, reflecting a distributional shift that is lexical rather than surprisal-driven.\nThis scorer-invariant ranking supports the use of a fixed 15-dimensional feature set across generators without per-model feature selection.\n\n%%% Feature ranking table (moved from main text)\n\\begin{table}[!htbp]\n\\centering\n\\small\n\\caption{Top-3 features by single-feature $\\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}\n\\label{tab:top_features}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{cllll}\n\\toprule\nRank & Pythia & OLMo & Qwen-rw & Qwen-cont \\\\\n\\midrule\n1 & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_std}} & \\texttt{freq\\_entropy} & \\textbf{\\texttt{surp\\_d1\\_std}} \\\\\n2 & \\textbf{\\texttt{surp\\_d2\\_std}} & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_std}} & \\textbf{\\texttt{surp\\_std}} \\\\\n3 & \\textbf{\\texttt{surp\\_std}} & \\textbf{\\texttt{surp\\_d2\\_std}} & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_d2\\_std}} \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\nTable~\\ref{tab:s1_transfer} reports the cross-model transfer accuracy matrix.\nClassifiers trained on continuation-mode generators (Pythia, OLMo, Qwen-cont) transfer well to each other, with off-diagonal accuracy retaining 80--92\\% of in-distribution performance.\nThe asymmetry between rewrite-mode and continuation-mode transfer (61--63\\%) confirms that generation mode, rather than model family, is the primary axis of distributional variation (Section~\\ref{sec:discussion}).\n\n%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)\n\\begin{table}[!htbp]\n  \\centering\n  \\small\n  \\caption{Cross-model transfer accuracy matrix. Diagonal (\\textbf{bold}): within-model; off-diagonal: cross-model. Retention: Pythia$\\leftrightarrow$OLMo 91--92\\%, Qwen-cont$\\leftrightarrow$Pythia 83--85\\%, Qwen-rw$\\to$others 61--63\\%.}\n  \\label{tab:s1_transfer}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Train} & Qwen-rw & Pythia & OLMo & Qwen-cont \\\\\n    \\midrule\n    Qwen-rw   & \\textbf{.423} & .259 & .265 & .347 \\\\\n    Pythia    & .272 & \\textbf{.386} & .353 & .329 \\\\\n    OLMo      & .277 & .345 & \\textbf{.382} & .324 \\\\\n    Qwen-cont & .344 & .328 & .311 & \\textbf{.388} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n\\paragraph{Dataset construction.}\nTable~\\ref{tab:s4_dataset_stats} summarizes the generational depth corpus.\nEach depth level contains 5{,}000 passages, yielding 30{,}000 total samples across six depths (0--5).\nDepth~0 consists of human-written seed texts from the C4 English validation split, truncated to 256 subword tokens.\nSubsequent depths are generated recursively: each depth-$k$ passage is produced by prompting the generator with the corresponding depth-$(k{-}1)$ passage.\nThe four model-mode configurations (Qwen-rw, Pythia-cont, OLMo-cont, Qwen-cont) share identical depth-0 seeds and generation pipeline, differing only in generator identity and prompting strategy (rewrite vs.\\ continuation).\n\n%%% Table S4: Dataset Statistics\n\\begin{table}[!htbp]\n  \\centering\n  \\small\n  \\caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}\n  \\label{tab:s4_dataset_stats}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{clrl}\n    \\toprule\n    \\textbf{Depth} & \\textbf{$N$ samples} & \\textbf{Mean tokens} & \\textbf{Source} \\\\\n    \\midrule\n    0 & 5{,}000 & 147.8 & C4 validation (human) \\\\\n    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\\\\n    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\\\\n    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\\\\n    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Total} & \\multicolumn{2}{l}{30{,}000 samples} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S2: Decoding Ablation AUC (exp-003)\n\\begin{table*}[t]\n  \\centering\n  \\caption{Pairwise AUC with bootstrap 95\\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\\,vs.\\,2 and 2\\,vs.\\,3 marks the empirical detectability boundary $\\Kempirical=2$. Bottom rows report cross-configuration Spearman $\\rho$ on per-feature discriminative-power rankings.}\n  \\label{tab:s2_decoding}\n  \\footnotesize\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{Greedy} & \\textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \\textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \\textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\\\\n    \\midrule\n    0 vs.\\ 1 & $.980\\;[.977,\\,.982]$ & $.995\\;[.993,\\,.996]$ & $.988\\;[.986,\\,.990]$ & $.998\\;[.998,\\,.999]$ \\\\\n    1 vs.\\ 2 & $.689\\;[.680,\\,.698]$ & $.687\\;[.677,\\,.695]$ & $.689\\;[.680,\\,.697]$ & $.704\\;[.695,\\,.713]$ \\\\\n    \\cmidrule(lr){1-5}\n    2 vs.\\ 3 & $.561\\;[.552,\\,.571]$ & $.592\\;[.582,\\,.601]$\\rlap{$^\\dagger$} & $.590\\;[.581,\\,.600]$ & $.582\\;[.572,\\,.592]$ \\\\\n    3 vs.\\ 4 & $.540\\;[.531,\\,.550]$ & $.547\\;[.537,\\,.557]$ & $.539\\;[.529,\\,.549]$ & $.529\\;[.519,\\,.540]$ \\\\\n    4 vs.\\ 5 & $.514\\;[.503,\\,.524]$ & $.507\\;[.496,\\,.517]^{\\ddagger}$ & $.535\\;[.524,\\,.545]$ & $.524\\;[.513,\\,.535]$ \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textbf{Cross-config feature Spearman $\\rho$}} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Greedy vs.\\ Nuc $p{=}0.9$} & 0.600 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}0.7$} & 0.782 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}0.7$} & 0.914 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}1.2$} & 0.893 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}1.2$} & 0.532 &\n    \\multicolumn{1}{l}{$T{=}0.7$ vs.\\ $T{=}1.2$} & 0.668 \\\\\n    \\bottomrule\n    \\multicolumn{5}{l}{${}^{\\dagger}$\\,CI upper bound (0.601) marginally exceeds $\\theta{=}0.60$ by 0.001.} \\\\\n    \\multicolumn{5}{l}{${}^{\\ddagger}$\\,Permutation $p = 0.12$ (not significant). All other pairs $p < 0.01$.}\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S2b: Extended K* CI (all models including new additions)\n\\begin{table*}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Extended pairwise $\\auc$ with bootstrap 95\\% CIs for all model configurations including new additions.\n  This table extends Table~\\ref{tab:kstar_ci} in the main text with Qwen-base, LLaMA-8B, Mistral-7B, Pythia-6.9B (nucleus), and Gemma-2-2B configurations.\n  $\\Kempirical = 2$ holds for 6/10 conditions at $\\theta{=}0.60$ (OLMo-1B, Mistral-7B, Pythia-6.9B, Gemma-2-2B: $\\Kempirical{=}1$).}\n  \\label{tab:kstar_ci_extended}\n  \\resizebox{\\textwidth}{!}{%\n  \\begin{tabular}{lcccccccccccccccccccc}\n    \\toprule\n     & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} & \\multicolumn{2}{c}{Qwen-base} & \\multicolumn{2}{c}{LLaMA-8B} & \\multicolumn{2}{c}{Mistral-7B} & \\multicolumn{2}{c}{Pythia-6.9B\\rlap{$^\\S$}} & \\multicolumn{2}{c}{Gemma-2B} \\\\\n    \\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\\cmidrule(lr){12-13}\\cmidrule(lr){14-15}\\cmidrule(lr){16-17}\\cmidrule(lr){18-19}\\cmidrule(lr){20-21}\n     & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n    \\midrule\n    0v1 & .9956 & & .9722 & & .9860 & & .9971 & & .9638 & [.961,\\,.967] & .987 & [.985,\\,.989] & .9224 & [.917,\\,.927] & .9170 & & .9599 & & .953 & [.949,\\,.957] \\\\\n    1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6074 & [.598,\\,.617]\\rlap{$^*$} & .5001 & [.496,\\,.519] & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} & .626 & [.617,\\,.635]\\rlap{$^*$} & .6123 & [.603,\\,.622]\\rlap{$^*$} & .5750 & & .5955 & & .5981 & [.588,\\,.608] \\\\\n    2v3 & .5893 & [.580,\\,.599] & .5440 & [.534,\\,.554] & .4973 & [.486,\\,.509] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] & .550 & [.540,\\,.560] & .5273 & [.517,\\,.538] & .5369 & & .5298 & & .534 & [.523,\\,.545] \\\\\n    3v4 & .5435 & & .5051 & & .5024 & & .5409 & & .5276 & & .529 & [.519,\\,.540] & .5168 & [.506,\\,.528] & .5174 & & .5135 & & .5033 & [.492,\\,.514] \\\\\n    4v5 & .5340 & & .5079 & & .4942 & & .5141 & & .5085 & & .518 & [.508,\\,.529] & .5159 & [.505,\\,.527] & .5175 & & ---\\rlap{$^\\|$} & & .5025 & [.492,\\,.514] \\\\\n    \\bottomrule\n    \\multicolumn{21}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all boundary comparisons.} \\\\\n    \\multicolumn{21}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.} \\\\\n    \\multicolumn{21}{l}{\\footnotesize $^\\|$$\\Kempirical{=}1$; 4v5 not required for boundary determination.} \\\\\n    \\multicolumn{21}{l}{\\footnotesize $^\\S$Pythia-6.9B evaluated separately; nucleus sampling ($p{=}0.95$, $T{=}1.0$), same as all other models.}\n  \\end{tabular}}% end resizebox\n\\end{table*}\n\n%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{LLM zero-shot depth classification: $5{\\times}5$ confusion matrices (Exp-011). Both frontier LLMs achieve high binary detection accuracy (GPT-5.5: 0.878; Claude Opus~4.6: 0.882) but near-chance 5-class accuracy (${\\sim}$0.33 vs.\\ OBD-LightGBM 0.386). Per-depth recall in Table~\\ref{tab:s3c_perdepth}.}\n  \\label{tab:s3_llm_zeroshot}\n\n  \\vspace{0.3em}\n  \\textbf{(a)} GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)\n  \\vspace{1pt}\n\n  \\begin{tabular}{lcccccc}\n    \\toprule\n    & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n    \\cmidrule(lr){2-6}\n    True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n    \\midrule\n    0 & \\textbf{77} & 18 &  4 &  0 &  1 & .770 \\\\\n    1 &  9 & \\textbf{19} & 36 & 24 & 12 & .190 \\\\\n    2 &  8 & 10 & \\textbf{38} & 35 &  9 & .380 \\\\\n    3 & 10 & 16 & 35 & \\textbf{24} & 15 & .240 \\\\\n    4 & 11 & 13 & 50 & 18 &  \\textbf{8} & .080 \\\\\n    \\bottomrule\n  \\end{tabular}\n\n  \\vspace{4pt}\n  \\textbf{(b)} Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)\n  \\vspace{1pt}\n\n  \\begin{tabular}{lcccccc}\n    \\toprule\n    & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n    \\cmidrule(lr){2-6}\n    True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n    \\midrule\n    0 & \\textbf{69} & 26 &  3 &  0 &  2 & .690 \\\\\n    1 &  8 & \\textbf{21} & 32 & 11 & 28 & .210 \\\\\n    2 &  6 & 36 & \\textbf{28} &  5 & 25 & .280 \\\\\n    3 &  7 & 20 & 31 & \\textbf{10} & 31 & .100 \\\\\n    4 &  7 & 28 & 22 &  6 & \\textbf{37} & .370 \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Per-depth recall (\\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\\geq 2$, consistent with $\\Kempirical = 2$.}\n  \\label{tab:s3c_perdepth}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lccccc}\n    \\toprule\n    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\\\\n    \\midrule\n    OBD-LightGBM & \\textbf{96} & \\textbf{39} & 14 & 19 & 22 \\\\\n    GPT-5.5      & 77 & 19 & \\textbf{38} & \\textbf{24} &  8 \\\\\n    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \\textbf{37} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n%%% Table: Token Length and EOS Truncation Analysis\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Mean subword token count per depth and EOS truncation rate (\\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend; the 0v1 length asymmetry (human texts shorter) makes detection \\emph{more conservative}, not inflated. See Section~\\ref{sec:length_confound}.}\n  \\label{tab:token_length}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccccccc}\n    \\toprule\n    & \\multicolumn{6}{c}{\\textbf{Mean Token Count}} & & \\\\\n    \\cmidrule(lr){2-7}\n    \\textbf{Model} & D0 & D1 & D2 & D3 & D4 & D5 & \\textbf{EOS\\%} & \\textbf{Sev.} \\\\\n    \\midrule\n    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\\\\n    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\\\\n    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negl. \\\\\n    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Mod. \\\\\n    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\\\\n    \\midrule\n    \\multicolumn{9}{l}{\\textit{Decoding ablation (Qwen-rw 1.5B)}} \\\\\n    \\quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\\\\n    \\quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\\\\n    \\quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\\\\n    \\quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\\\\n    \\bottomrule\n    \\multicolumn{9}{l}{EOS\\%: generation terminated via EOS before 256-token limit. Ranges span depths 1--5.}\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S5: Complete 15-D Feature Descriptions\n\\begin{table*}[t]\n  \\centering\n  \\caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}\n  \\label{tab:s5_features}\n  \\begin{tabular}{llp{0.45\\textwidth}l}\n    \\toprule\n    \\textbf{Group} & \\textbf{Feature} & \\textbf{Description} & \\textbf{Range} \\\\\n    \\midrule\n    \\multirow{9}{*}{\\rotatebox[origin=c]{90}{\\textsc{Surprisal}}}\n    & \\texttt{surp\\_mean}   & Mean token surprisal $\\frac{1}{T}\\sum_t -\\log p(x_t \\mid x_{&lt;t})$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_std}    & Standard deviation of token surprisal & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_skew}   & Skewness of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_kurt}   & Excess kurtosis of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_mean} & Mean of first-order surprisal differences $\\Delta s_t = s_{t+1} - s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_std}  & Std of first-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_d1\\_skew} & Skewness of first-order surprisal differences & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_mean} & Mean of second-order differences $\\Delta^2 s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_std}  & Std of second-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Lex}}}\n    & \\texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\\\\n    & \\texttt{hapax\\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\\\\n    & \\texttt{self\\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Freq}}}\n    & \\texttt{freq\\_kurtosis}  & Excess kurtosis of word frequency distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{freq\\_entropy}   & Shannon entropy of word frequencies: $-\\sum p_w \\log_2 p_w$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{low\\_freq\\_ratio} & Proportion of vocabulary with count $\\leq 2$ & $[0, 1]$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap\n\\begin{table*}[t]\n\\begin{minipage}[t]{0.45\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \\texttt{doc\\_id} to prevent data leakage from the same seed document appearing in both train and test.}\n  \\label{tab:s6_lgbm_params}\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Parameter} & \\textbf{Value} \\\\\n    \\midrule\n    \\texttt{n\\_estimators}      & 200 \\\\\n    \\texttt{learning\\_rate}     & 0.05 \\\\\n    \\texttt{max\\_depth}         & 6 \\\\\n    \\texttt{num\\_leaves}        & 31 \\\\\n    \\texttt{verbose}            & $-1$ \\\\\n    \\texttt{n\\_jobs}            & $-1$ (all cores) \\\\\n    Cross-validation            & 5-fold GroupKFold \\\\\n    Grouping key                & \\texttt{doc\\_id} \\\\\n    Objective                   & Binary (per depth pair) \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{minipage}\\hfill\n\\begin{minipage}[t]{0.52\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}\n  \\label{tab:s7_neural_probe}\n  \\resizebox{\\textwidth}{!}{%\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Component} & \\textbf{Details} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Embedding extraction}} \\\\\n    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\\\\n    Representation    & Last hidden state, attention-masked avg pool \\\\\n    Embedding dim     & 1536 / 2048 / 2048 \\\\\n    Max sequence len   & 512 tokens \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{MLP classifier}} \\\\\n    Architecture      & $d_{\\text{emb}} \\to 512 \\to 256 \\to 6$ \\\\\n    Activations       & ReLU \\\\\n    Dropout           & 0.1 (after each hidden layer) \\\\\n    Output            & 6-class softmax \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Training}} \\\\\n    Optimizer         & Adam ($\\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\\\\n    Loss              & Cross-entropy \\\\\n    Batch size        & 256 \\\\\n    Max epochs        & 20 \\\\\n    Early stopping    & Patience = 5 (validation loss) \\\\\n    Cross-validation  & 5-fold GroupKFold \\\\\n    \\bottomrule\n  \\end{tabular}%\n  }\n\\end{minipage}\n\\end{table*}\n\n%%% Table S8: Per-Model Bootstrap CI Results (exp-007)\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Pairwise AUC with bootstrap 95\\% CIs for four model-mode configurations (1{,}000 resamples). All boundary pairs ($\\auc > \\theta$) $p < 0.01$; OLMo 1v2--4v5 non-significant ($p > 0.09$).}\n  \\label{tab:s8_cv_folds}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Qwen-rw} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    0v1 & $.996\\;[.995,.997]$ & $.993\\;[.992,.994]$ & $.986\\;[.984,.988]$ & $.997\\;[.996,.998]$ \\\\\n    1v2 & $.696\\;[.686,.704]$ & $.607\\;[.598,.617]$ & $.500\\;[.496,.519]$ & $.611\\;[.602,.621]$ \\\\\n    \\cmidrule(lr){1-5}\n    2v3 & $.589\\;[.580,.599]$ & $.551\\;[.542,.563]$ & $.497\\;[.486,.509]$ & $.561\\;[.551,.571]$ \\\\\n    3v4 & $.544\\;[.533,.555]$ & $.515\\;[.504,.526]$ & $.502\\;[.491,.513]$ & $.541\\;[.531,.551]$ \\\\\n    4v5 & $.534\\;[.524,.545]$ & $.514\\;[.502,.525]$ & $.494\\;[.483,.506]$ & $.514\\;[.504,.526]$ \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S9: Binary Detector Spearman ρ (exp-012)\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Spearman $\\rho$ between binary detector scores and true depth, and 6-class accuracy. Correlations driven by 0v1; scores do not track depth beyond generation~1. Qwen-rw exhibits reversed sign ($\\rho > 0$).}\n  \\label{tab:s9_binary_spearman}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Qwen-rw} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textit{Spearman $\\rho$}} \\\\\n    \\quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\\\\n    \\quad log-PPL (obs.)     & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\\\\n    \\quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\\\\n    \\midrule\n    6-class acc.              & 0.199    & 0.130    & 0.127    & 0.183 \\\\\n    \\bottomrule\n    \\multicolumn{5}{l}{Random baseline: 0.167} \\\\\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S10: Pythia Decoding Ablation (exp-020)\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Pythia-1.4B pairwise $\\auc$ under four decoding configs (10K bootstrap). $^\\dagger$Greedy triggers repetition collapse (4-gram repeat: $d_0{=}0.01 \\to d_1{=}0.72$).}\n  \\label{tab:s10_pythia_decoding}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Greedy}$^\\dagger$ & \\textbf{$p{=}0.9$} & \\textbf{$T{=}0.7$} & \\textbf{$T{=}1.2$} \\\\\n    \\midrule\n    0v1 & $.999$ & $.995$ & $.996$ & $.994$ \\\\\n    1v2 & $.884$ & $.675$ & $.728$ & $.618$ \\\\\n    \\cmidrule(lr){1-5}\n    2v3 & $.531$ & $.559$ & $.598^\\ddagger$ & $.531$ \\\\\n    3v4 & $.522$ & $.524$ & $.563$ & $.520$ \\\\\n    4v5 & $.514$ & $.501$ & $.527$ & $.510$ \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 2 & 2 \\\\\n    \\bottomrule\n    \\multicolumn{5}{l}{${}^{\\ddagger}$CI upper 0.606 $> \\theta$; point est.\\ below.} \\\\\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S11: Length Ablation (exp-021)\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Pairwise $\\auc$ for three segment lengths (Qwen-base, cont.\\ mode). $\\Kempirical{=}2$ at 128/256; 512 marginal ($^\\dagger$CI lower $< \\theta$).}\n  \\label{tab:s11_length_ablation}\n  \\begin{tabular}{lccc}\n    \\toprule\n    & \\textbf{128} & \\textbf{256} & \\textbf{512} \\\\\n    \\midrule\n    0v1 & .979 & .991 & .992 \\\\\n    1v2 & .622 & .628 & .607$^\\dagger$ \\\\\n    \\cmidrule(lr){1-4}\n    2v3 & .529 & .556 & .572 \\\\\n    3v4 & .535 & .530 & .530 \\\\\n    4v5 & .501 & .514 & .518 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 2$^\\dagger$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table}\n\n%%% Table S12: Domain Ablation\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Pairwise $\\auc$ for three text domains (Qwen-cont). arXiv yields $\\Kempirical{=}3$; C4 and Wikipedia $\\Kempirical{=}2$.}\n  \\label{tab:s12_domain_ablation}\n  \\begin{tabular}{lccc}\n    \\toprule\n    & \\textbf{C4} & \\textbf{Wiki} & \\textbf{arXiv} \\\\\n    \\midrule\n    0v1 & .997 & .996 & .995 \\\\\n    1v2 & .611 & .619 & .858 \\\\\n    \\cmidrule(lr){1-4}\n    2v3 & .561 & .550 & .644$^*$ \\\\\n    3v4 & .541 & .523 & .544 \\\\\n    4v5 & .514 & .514 & .530 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 3 \\\\\n    \\bottomrule\n    \\multicolumn{4}{l}{\\footnotesize $^*$CI $[.628,.658]$; $p < 0.001$.}\n  \\end{tabular}\n\\end{table}\n\n%%% Table S13: Scorer Sensitivity Analysis\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Scorer sensitivity: $\\Kempirical$ under self- vs.\\ cross-scoring. Cross-scoring reduces $\\Kempirical$ only for marginal Qwen-cont.}\n  \\label{tab:s13_scorer_sensitivity}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{llcccc}\n    \\toprule\n    \\textbf{Generator} & \\textbf{Mode} & \\textbf{Self} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Agr.} \\\\\n    \\midrule\n    Qwen-Inst & Rewrite & 2 & 2 & 2 & \\checkmark \\\\\n    Qwen-Inst & Cont.   & 2 & 1 & 1 & $\\times$ \\\\\n    Qwen-base & Cont.   & 2 & 2 & 2 & \\checkmark \\\\\n    Pythia    & Cont.   & 2 & 2 & 2 & \\checkmark \\\\\n    OLMo      & Cont.   & 1 & -- & -- & -- \\\\\n    Qwen-7B   & Cont.   & 2 & -- & -- & -- \\\\\n    Mistral   & Cont.   & 1 & -- & -- & -- \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n\\clearpage\n",
    "structuredPatch": [
      {
        "oldStart": 431,
        "oldLines": 7,
        "newStart": 431,
        "newLines": 7,
        "lines": [
          "     0v1 & .997 & .996 & .995 \\\\",
          "     1v2 & .611 & .619 & .858 \\\\",
          "     \\cmidrule(lr){1-4}",
          "-    2v3 & .561 & .550 & .644$^*$ \\\\",
          "+    2v3 & .561 & .550 & .643$^*$ \\\\",
          "     3v4 & .541 & .523 & .544 \\\\",
          "     4v5 & .514 & .514 & .530 \\\\",
          "     \\midrule"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 692_

<details open><summary>🔧 Tool call — Edit · `toolu_01N2iubBHv4oq92H2KEjk5JP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "old_string": "4v5 & .514 & .514 & .530 \\\\",
  "new_string": "4v5 & .514 & .514 & .529 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "9e89179e-6e83-477c-ac89-322e71efb449",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155tfT5Rh3rtnA99H19Naqt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22473,
      "cache_read_input_tokens": 49522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22473
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-23T11:37:09.878Z_

<details><summary>↩ Tool result · `toolu_01N2iubBHv4oq92H2KEjk5JP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "f6f4d707-7285-42c2-88f6-4048a12b73f5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "oldString": "4v5 & .514 & .514 & .530 \\\\",
    "newString": "4v5 & .514 & .514 & .529 \\\\",
    "originalFile": "\\appendix\n\\section{Supplementary Materials}\n\\label{sec:appendix}\n\nThis appendix provides supplementary figures, detailed experimental tables, dataset statistics, and complete feature descriptions referenced in the main text.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_filtering_strategies.pdf}\n\\caption{Downstream performance of all filtering strategies (5 seeds, $\\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}\n\\label{fig:filtering_strategies}\n\\end{figure}\n\n\\paragraph{Feature ranking and cross-model consistency.}\nTable~\\ref{tab:top_features} reports per-model single-feature AUC rankings.\nSurprisal derivative features (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_d2\\_std}) consistently rank among the top three across all continuation-mode models (Pythia, OLMo, Qwen-cont), with pairwise Spearman $\\rho \\geq 0.85$.\nThe rewrite-mode model (Qwen-rw) diverges by placing \\texttt{freq\\_entropy} first, reflecting a distributional shift that is lexical rather than surprisal-driven.\nThis scorer-invariant ranking supports the use of a fixed 15-dimensional feature set across generators without per-model feature selection.\n\n%%% Feature ranking table (moved from main text)\n\\begin{table}[!htbp]\n\\centering\n\\small\n\\caption{Top-3 features by single-feature $\\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}\n\\label{tab:top_features}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{cllll}\n\\toprule\nRank & Pythia & OLMo & Qwen-rw & Qwen-cont \\\\\n\\midrule\n1 & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_std}} & \\texttt{freq\\_entropy} & \\textbf{\\texttt{surp\\_d1\\_std}} \\\\\n2 & \\textbf{\\texttt{surp\\_d2\\_std}} & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_std}} & \\textbf{\\texttt{surp\\_std}} \\\\\n3 & \\textbf{\\texttt{surp\\_std}} & \\textbf{\\texttt{surp\\_d2\\_std}} & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_d2\\_std}} \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\nTable~\\ref{tab:s1_transfer} reports the cross-model transfer accuracy matrix.\nClassifiers trained on continuation-mode generators (Pythia, OLMo, Qwen-cont) transfer well to each other, with off-diagonal accuracy retaining 80--92\\% of in-distribution performance.\nThe asymmetry between rewrite-mode and continuation-mode transfer (61--63\\%) confirms that generation mode, rather than model family, is the primary axis of distributional variation (Section~\\ref{sec:discussion}).\n\n%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)\n\\begin{table}[!htbp]\n  \\centering\n  \\small\n  \\caption{Cross-model transfer accuracy matrix. Diagonal (\\textbf{bold}): within-model; off-diagonal: cross-model. Retention: Pythia$\\leftrightarrow$OLMo 91--92\\%, Qwen-cont$\\leftrightarrow$Pythia 83--85\\%, Qwen-rw$\\to$others 61--63\\%.}\n  \\label{tab:s1_transfer}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Train} & Qwen-rw & Pythia & OLMo & Qwen-cont \\\\\n    \\midrule\n    Qwen-rw   & \\textbf{.423} & .259 & .265 & .347 \\\\\n    Pythia    & .272 & \\textbf{.386} & .353 & .329 \\\\\n    OLMo      & .277 & .345 & \\textbf{.382} & .324 \\\\\n    Qwen-cont & .344 & .328 & .311 & \\textbf{.388} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n\\paragraph{Dataset construction.}\nTable~\\ref{tab:s4_dataset_stats} summarizes the generational depth corpus.\nEach depth level contains 5{,}000 passages, yielding 30{,}000 total samples across six depths (0--5).\nDepth~0 consists of human-written seed texts from the C4 English validation split, truncated to 256 subword tokens.\nSubsequent depths are generated recursively: each depth-$k$ passage is produced by prompting the generator with the corresponding depth-$(k{-}1)$ passage.\nThe four model-mode configurations (Qwen-rw, Pythia-cont, OLMo-cont, Qwen-cont) share identical depth-0 seeds and generation pipeline, differing only in generator identity and prompting strategy (rewrite vs.\\ continuation).\n\n%%% Table S4: Dataset Statistics\n\\begin{table}[!htbp]\n  \\centering\n  \\small\n  \\caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}\n  \\label{tab:s4_dataset_stats}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{clrl}\n    \\toprule\n    \\textbf{Depth} & \\textbf{$N$ samples} & \\textbf{Mean tokens} & \\textbf{Source} \\\\\n    \\midrule\n    0 & 5{,}000 & 147.8 & C4 validation (human) \\\\\n    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\\\\n    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\\\\n    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\\\\n    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Total} & \\multicolumn{2}{l}{30{,}000 samples} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S2: Decoding Ablation AUC (exp-003)\n\\begin{table*}[t]\n  \\centering\n  \\caption{Pairwise AUC with bootstrap 95\\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\\,vs.\\,2 and 2\\,vs.\\,3 marks the empirical detectability boundary $\\Kempirical=2$. Bottom rows report cross-configuration Spearman $\\rho$ on per-feature discriminative-power rankings.}\n  \\label{tab:s2_decoding}\n  \\footnotesize\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{Greedy} & \\textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \\textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \\textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\\\\n    \\midrule\n    0 vs.\\ 1 & $.980\\;[.977,\\,.982]$ & $.995\\;[.993,\\,.996]$ & $.988\\;[.986,\\,.990]$ & $.998\\;[.998,\\,.999]$ \\\\\n    1 vs.\\ 2 & $.689\\;[.680,\\,.698]$ & $.687\\;[.677,\\,.695]$ & $.689\\;[.680,\\,.697]$ & $.704\\;[.695,\\,.713]$ \\\\\n    \\cmidrule(lr){1-5}\n    2 vs.\\ 3 & $.561\\;[.552,\\,.571]$ & $.592\\;[.582,\\,.601]$\\rlap{$^\\dagger$} & $.590\\;[.581,\\,.600]$ & $.582\\;[.572,\\,.592]$ \\\\\n    3 vs.\\ 4 & $.540\\;[.531,\\,.550]$ & $.547\\;[.537,\\,.557]$ & $.539\\;[.529,\\,.549]$ & $.529\\;[.519,\\,.540]$ \\\\\n    4 vs.\\ 5 & $.514\\;[.503,\\,.524]$ & $.507\\;[.496,\\,.517]^{\\ddagger}$ & $.535\\;[.524,\\,.545]$ & $.524\\;[.513,\\,.535]$ \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textbf{Cross-config feature Spearman $\\rho$}} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Greedy vs.\\ Nuc $p{=}0.9$} & 0.600 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}0.7$} & 0.782 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}0.7$} & 0.914 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}1.2$} & 0.893 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}1.2$} & 0.532 &\n    \\multicolumn{1}{l}{$T{=}0.7$ vs.\\ $T{=}1.2$} & 0.668 \\\\\n    \\bottomrule\n    \\multicolumn{5}{l}{${}^{\\dagger}$\\,CI upper bound (0.601) marginally exceeds $\\theta{=}0.60$ by 0.001.} \\\\\n    \\multicolumn{5}{l}{${}^{\\ddagger}$\\,Permutation $p = 0.12$ (not significant). All other pairs $p < 0.01$.}\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S2b: Extended K* CI (all models including new additions)\n\\begin{table*}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Extended pairwise $\\auc$ with bootstrap 95\\% CIs for all model configurations including new additions.\n  This table extends Table~\\ref{tab:kstar_ci} in the main text with Qwen-base, LLaMA-8B, Mistral-7B, Pythia-6.9B (nucleus), and Gemma-2-2B configurations.\n  $\\Kempirical = 2$ holds for 6/10 conditions at $\\theta{=}0.60$ (OLMo-1B, Mistral-7B, Pythia-6.9B, Gemma-2-2B: $\\Kempirical{=}1$).}\n  \\label{tab:kstar_ci_extended}\n  \\resizebox{\\textwidth}{!}{%\n  \\begin{tabular}{lcccccccccccccccccccc}\n    \\toprule\n     & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} & \\multicolumn{2}{c}{Qwen-base} & \\multicolumn{2}{c}{LLaMA-8B} & \\multicolumn{2}{c}{Mistral-7B} & \\multicolumn{2}{c}{Pythia-6.9B\\rlap{$^\\S$}} & \\multicolumn{2}{c}{Gemma-2B} \\\\\n    \\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\\cmidrule(lr){12-13}\\cmidrule(lr){14-15}\\cmidrule(lr){16-17}\\cmidrule(lr){18-19}\\cmidrule(lr){20-21}\n     & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n    \\midrule\n    0v1 & .9956 & & .9722 & & .9860 & & .9971 & & .9638 & [.961,\\,.967] & .987 & [.985,\\,.989] & .9224 & [.917,\\,.927] & .9170 & & .9599 & & .953 & [.949,\\,.957] \\\\\n    1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6074 & [.598,\\,.617]\\rlap{$^*$} & .5001 & [.496,\\,.519] & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} & .626 & [.617,\\,.635]\\rlap{$^*$} & .6123 & [.603,\\,.622]\\rlap{$^*$} & .5750 & & .5955 & & .5981 & [.588,\\,.608] \\\\\n    2v3 & .5893 & [.580,\\,.599] & .5440 & [.534,\\,.554] & .4973 & [.486,\\,.509] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] & .550 & [.540,\\,.560] & .5273 & [.517,\\,.538] & .5369 & & .5298 & & .534 & [.523,\\,.545] \\\\\n    3v4 & .5435 & & .5051 & & .5024 & & .5409 & & .5276 & & .529 & [.519,\\,.540] & .5168 & [.506,\\,.528] & .5174 & & .5135 & & .5033 & [.492,\\,.514] \\\\\n    4v5 & .5340 & & .5079 & & .4942 & & .5141 & & .5085 & & .518 & [.508,\\,.529] & .5159 & [.505,\\,.527] & .5175 & & ---\\rlap{$^\\|$} & & .5025 & [.492,\\,.514] \\\\\n    \\bottomrule\n    \\multicolumn{21}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all boundary comparisons.} \\\\\n    \\multicolumn{21}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.} \\\\\n    \\multicolumn{21}{l}{\\footnotesize $^\\|$$\\Kempirical{=}1$; 4v5 not required for boundary determination.} \\\\\n    \\multicolumn{21}{l}{\\footnotesize $^\\S$Pythia-6.9B evaluated separately; nucleus sampling ($p{=}0.95$, $T{=}1.0$), same as all other models.}\n  \\end{tabular}}% end resizebox\n\\end{table*}\n\n%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{LLM zero-shot depth classification: $5{\\times}5$ confusion matrices (Exp-011). Both frontier LLMs achieve high binary detection accuracy (GPT-5.5: 0.878; Claude Opus~4.6: 0.882) but near-chance 5-class accuracy (${\\sim}$0.33 vs.\\ OBD-LightGBM 0.386). Per-depth recall in Table~\\ref{tab:s3c_perdepth}.}\n  \\label{tab:s3_llm_zeroshot}\n\n  \\vspace{0.3em}\n  \\textbf{(a)} GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)\n  \\vspace{1pt}\n\n  \\begin{tabular}{lcccccc}\n    \\toprule\n    & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n    \\cmidrule(lr){2-6}\n    True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n    \\midrule\n    0 & \\textbf{77} & 18 &  4 &  0 &  1 & .770 \\\\\n    1 &  9 & \\textbf{19} & 36 & 24 & 12 & .190 \\\\\n    2 &  8 & 10 & \\textbf{38} & 35 &  9 & .380 \\\\\n    3 & 10 & 16 & 35 & \\textbf{24} & 15 & .240 \\\\\n    4 & 11 & 13 & 50 & 18 &  \\textbf{8} & .080 \\\\\n    \\bottomrule\n  \\end{tabular}\n\n  \\vspace{4pt}\n  \\textbf{(b)} Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)\n  \\vspace{1pt}\n\n  \\begin{tabular}{lcccccc}\n    \\toprule\n    & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n    \\cmidrule(lr){2-6}\n    True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n    \\midrule\n    0 & \\textbf{69} & 26 &  3 &  0 &  2 & .690 \\\\\n    1 &  8 & \\textbf{21} & 32 & 11 & 28 & .210 \\\\\n    2 &  6 & 36 & \\textbf{28} &  5 & 25 & .280 \\\\\n    3 &  7 & 20 & 31 & \\textbf{10} & 31 & .100 \\\\\n    4 &  7 & 28 & 22 &  6 & \\textbf{37} & .370 \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Per-depth recall (\\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\\geq 2$, consistent with $\\Kempirical = 2$.}\n  \\label{tab:s3c_perdepth}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lccccc}\n    \\toprule\n    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\\\\n    \\midrule\n    OBD-LightGBM & \\textbf{96} & \\textbf{39} & 14 & 19 & 22 \\\\\n    GPT-5.5      & 77 & 19 & \\textbf{38} & \\textbf{24} &  8 \\\\\n    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \\textbf{37} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n%%% Table: Token Length and EOS Truncation Analysis\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Mean subword token count per depth and EOS truncation rate (\\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend; the 0v1 length asymmetry (human texts shorter) makes detection \\emph{more conservative}, not inflated. See Section~\\ref{sec:length_confound}.}\n  \\label{tab:token_length}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccccccc}\n    \\toprule\n    & \\multicolumn{6}{c}{\\textbf{Mean Token Count}} & & \\\\\n    \\cmidrule(lr){2-7}\n    \\textbf{Model} & D0 & D1 & D2 & D3 & D4 & D5 & \\textbf{EOS\\%} & \\textbf{Sev.} \\\\\n    \\midrule\n    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\\\\n    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\\\\n    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negl. \\\\\n    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Mod. \\\\\n    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\\\\n    \\midrule\n    \\multicolumn{9}{l}{\\textit{Decoding ablation (Qwen-rw 1.5B)}} \\\\\n    \\quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\\\\n    \\quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\\\\n    \\quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\\\\n    \\quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\\\\n    \\bottomrule\n    \\multicolumn{9}{l}{EOS\\%: generation terminated via EOS before 256-token limit. Ranges span depths 1--5.}\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S5: Complete 15-D Feature Descriptions\n\\begin{table*}[t]\n  \\centering\n  \\caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}\n  \\label{tab:s5_features}\n  \\begin{tabular}{llp{0.45\\textwidth}l}\n    \\toprule\n    \\textbf{Group} & \\textbf{Feature} & \\textbf{Description} & \\textbf{Range} \\\\\n    \\midrule\n    \\multirow{9}{*}{\\rotatebox[origin=c]{90}{\\textsc{Surprisal}}}\n    & \\texttt{surp\\_mean}   & Mean token surprisal $\\frac{1}{T}\\sum_t -\\log p(x_t \\mid x_{&lt;t})$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_std}    & Standard deviation of token surprisal & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_skew}   & Skewness of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_kurt}   & Excess kurtosis of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_mean} & Mean of first-order surprisal differences $\\Delta s_t = s_{t+1} - s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_std}  & Std of first-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_d1\\_skew} & Skewness of first-order surprisal differences & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_mean} & Mean of second-order differences $\\Delta^2 s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_std}  & Std of second-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Lex}}}\n    & \\texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\\\\n    & \\texttt{hapax\\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\\\\n    & \\texttt{self\\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Freq}}}\n    & \\texttt{freq\\_kurtosis}  & Excess kurtosis of word frequency distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{freq\\_entropy}   & Shannon entropy of word frequencies: $-\\sum p_w \\log_2 p_w$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{low\\_freq\\_ratio} & Proportion of vocabulary with count $\\leq 2$ & $[0, 1]$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap\n\\begin{table*}[t]\n\\begin{minipage}[t]{0.45\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \\texttt{doc\\_id} to prevent data leakage from the same seed document appearing in both train and test.}\n  \\label{tab:s6_lgbm_params}\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Parameter} & \\textbf{Value} \\\\\n    \\midrule\n    \\texttt{n\\_estimators}      & 200 \\\\\n    \\texttt{learning\\_rate}     & 0.05 \\\\\n    \\texttt{max\\_depth}         & 6 \\\\\n    \\texttt{num\\_leaves}        & 31 \\\\\n    \\texttt{verbose}            & $-1$ \\\\\n    \\texttt{n\\_jobs}            & $-1$ (all cores) \\\\\n    Cross-validation            & 5-fold GroupKFold \\\\\n    Grouping key                & \\texttt{doc\\_id} \\\\\n    Objective                   & Binary (per depth pair) \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{minipage}\\hfill\n\\begin{minipage}[t]{0.52\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}\n  \\label{tab:s7_neural_probe}\n  \\resizebox{\\textwidth}{!}{%\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Component} & \\textbf{Details} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Embedding extraction}} \\\\\n    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\\\\n    Representation    & Last hidden state, attention-masked avg pool \\\\\n    Embedding dim     & 1536 / 2048 / 2048 \\\\\n    Max sequence len   & 512 tokens \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{MLP classifier}} \\\\\n    Architecture      & $d_{\\text{emb}} \\to 512 \\to 256 \\to 6$ \\\\\n    Activations       & ReLU \\\\\n    Dropout           & 0.1 (after each hidden layer) \\\\\n    Output            & 6-class softmax \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Training}} \\\\\n    Optimizer         & Adam ($\\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\\\\n    Loss              & Cross-entropy \\\\\n    Batch size        & 256 \\\\\n    Max epochs        & 20 \\\\\n    Early stopping    & Patience = 5 (validation loss) \\\\\n    Cross-validation  & 5-fold GroupKFold \\\\\n    \\bottomrule\n  \\end{tabular}%\n  }\n\\end{minipage}\n\\end{table*}\n\n%%% Table S8: Per-Model Bootstrap CI Results (exp-007)\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Pairwise AUC with bootstrap 95\\% CIs for four model-mode configurations (1{,}000 resamples). All boundary pairs ($\\auc > \\theta$) $p < 0.01$; OLMo 1v2--4v5 non-significant ($p > 0.09$).}\n  \\label{tab:s8_cv_folds}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Qwen-rw} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    0v1 & $.996\\;[.995,.997]$ & $.993\\;[.992,.994]$ & $.986\\;[.984,.988]$ & $.997\\;[.996,.998]$ \\\\\n    1v2 & $.696\\;[.686,.704]$ & $.607\\;[.598,.617]$ & $.500\\;[.496,.519]$ & $.611\\;[.602,.621]$ \\\\\n    \\cmidrule(lr){1-5}\n    2v3 & $.589\\;[.580,.599]$ & $.551\\;[.542,.563]$ & $.497\\;[.486,.509]$ & $.561\\;[.551,.571]$ \\\\\n    3v4 & $.544\\;[.533,.555]$ & $.515\\;[.504,.526]$ & $.502\\;[.491,.513]$ & $.541\\;[.531,.551]$ \\\\\n    4v5 & $.534\\;[.524,.545]$ & $.514\\;[.502,.525]$ & $.494\\;[.483,.506]$ & $.514\\;[.504,.526]$ \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S9: Binary Detector Spearman ρ (exp-012)\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Spearman $\\rho$ between binary detector scores and true depth, and 6-class accuracy. Correlations driven by 0v1; scores do not track depth beyond generation~1. Qwen-rw exhibits reversed sign ($\\rho > 0$).}\n  \\label{tab:s9_binary_spearman}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Qwen-rw} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textit{Spearman $\\rho$}} \\\\\n    \\quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\\\\n    \\quad log-PPL (obs.)     & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\\\\n    \\quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\\\\n    \\midrule\n    6-class acc.              & 0.199    & 0.130    & 0.127    & 0.183 \\\\\n    \\bottomrule\n    \\multicolumn{5}{l}{Random baseline: 0.167} \\\\\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S10: Pythia Decoding Ablation (exp-020)\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Pythia-1.4B pairwise $\\auc$ under four decoding configs (10K bootstrap). $^\\dagger$Greedy triggers repetition collapse (4-gram repeat: $d_0{=}0.01 \\to d_1{=}0.72$).}\n  \\label{tab:s10_pythia_decoding}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Greedy}$^\\dagger$ & \\textbf{$p{=}0.9$} & \\textbf{$T{=}0.7$} & \\textbf{$T{=}1.2$} \\\\\n    \\midrule\n    0v1 & $.999$ & $.995$ & $.996$ & $.994$ \\\\\n    1v2 & $.884$ & $.675$ & $.728$ & $.618$ \\\\\n    \\cmidrule(lr){1-5}\n    2v3 & $.531$ & $.559$ & $.598^\\ddagger$ & $.531$ \\\\\n    3v4 & $.522$ & $.524$ & $.563$ & $.520$ \\\\\n    4v5 & $.514$ & $.501$ & $.527$ & $.510$ \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 2 & 2 \\\\\n    \\bottomrule\n    \\multicolumn{5}{l}{${}^{\\ddagger}$CI upper 0.606 $> \\theta$; point est.\\ below.} \\\\\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S11: Length Ablation (exp-021)\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Pairwise $\\auc$ for three segment lengths (Qwen-base, cont.\\ mode). $\\Kempirical{=}2$ at 128/256; 512 marginal ($^\\dagger$CI lower $< \\theta$).}\n  \\label{tab:s11_length_ablation}\n  \\begin{tabular}{lccc}\n    \\toprule\n    & \\textbf{128} & \\textbf{256} & \\textbf{512} \\\\\n    \\midrule\n    0v1 & .979 & .991 & .992 \\\\\n    1v2 & .622 & .628 & .607$^\\dagger$ \\\\\n    \\cmidrule(lr){1-4}\n    2v3 & .529 & .556 & .572 \\\\\n    3v4 & .535 & .530 & .530 \\\\\n    4v5 & .501 & .514 & .518 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 2$^\\dagger$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table}\n\n%%% Table S12: Domain Ablation\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Pairwise $\\auc$ for three text domains (Qwen-cont). arXiv yields $\\Kempirical{=}3$; C4 and Wikipedia $\\Kempirical{=}2$.}\n  \\label{tab:s12_domain_ablation}\n  \\begin{tabular}{lccc}\n    \\toprule\n    & \\textbf{C4} & \\textbf{Wiki} & \\textbf{arXiv} \\\\\n    \\midrule\n    0v1 & .997 & .996 & .995 \\\\\n    1v2 & .611 & .619 & .858 \\\\\n    \\cmidrule(lr){1-4}\n    2v3 & .561 & .550 & .643$^*$ \\\\\n    3v4 & .541 & .523 & .544 \\\\\n    4v5 & .514 & .514 & .530 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 3 \\\\\n    \\bottomrule\n    \\multicolumn{4}{l}{\\footnotesize $^*$CI $[.628,.658]$; $p < 0.001$.}\n  \\end{tabular}\n\\end{table}\n\n%%% Table S13: Scorer Sensitivity Analysis\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Scorer sensitivity: $\\Kempirical$ under self- vs.\\ cross-scoring. Cross-scoring reduces $\\Kempirical$ only for marginal Qwen-cont.}\n  \\label{tab:s13_scorer_sensitivity}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{llcccc}\n    \\toprule\n    \\textbf{Generator} & \\textbf{Mode} & \\textbf{Self} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Agr.} \\\\\n    \\midrule\n    Qwen-Inst & Rewrite & 2 & 2 & 2 & \\checkmark \\\\\n    Qwen-Inst & Cont.   & 2 & 1 & 1 & $\\times$ \\\\\n    Qwen-base & Cont.   & 2 & 2 & 2 & \\checkmark \\\\\n    Pythia    & Cont.   & 2 & 2 & 2 & \\checkmark \\\\\n    OLMo      & Cont.   & 1 & -- & -- & -- \\\\\n    Qwen-7B   & Cont.   & 2 & -- & -- & -- \\\\\n    Mistral   & Cont.   & 1 & -- & -- & -- \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n\\clearpage\n",
    "structuredPatch": [
      {
        "oldStart": 433,
        "oldLines": 7,
        "newStart": 433,
        "newLines": 7,
        "lines": [
          "     \\cmidrule(lr){1-4}",
          "     2v3 & .561 & .550 & .643$^*$ \\\\",
          "     3v4 & .541 & .523 & .544 \\\\",
          "-    4v5 & .514 & .514 & .530 \\\\",
          "+    4v5 & .514 & .514 & .529 \\\\",
          "     \\midrule",
          "     $\\Kempirical$ & 2 & 2 & 3 \\\\",
          "     \\bottomrule"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Assistant

_source line 694_

<details><summary>Logged reasoning block</summary>

```text
Good, all 5 edits are done. Now let me also check if there's an extended table in appendix_extended.tex that might also have the .644 value. Let me check.

Also, let me verify the discussion.tex inline for arXiv 2v3 mentions. Looking at the discussion text I read earlier:
Line 27: "Web text (C4, Wikipedia) and Code (Python) consistently yield $\Kempirical{=}2$, while structured academic text (arXiv) yields $\Kempirical{=}3$ across three independent architecture families (Section~\ref{sec:cross_domain}), as formulaic structure (citations, math notation, section conventions) creates larger per-generation distributional shifts (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4)."


No .644 in discussion.tex. Now checking the extended appendix for that same value.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "cea8d0cf-8735-49bf-9e0c-4f5a9a1aefaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RubQDdyVbVdD6eXbT6qoBW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6296,
      "cache_read_input_tokens": 71995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6296
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 695_

Let me check if the extended appendix also references the .644 value.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "4ec0d486-9cdb-403f-a85b-91ae4ba8dae2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RubQDdyVbVdD6eXbT6qoBW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6296,
      "cache_read_input_tokens": 71995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6296
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 696_

<details open><summary>🔧 Tool call — Grep · `toolu_016TQs9Sk4p8BiY46gkHfurE`</summary>

```json
{
  "pattern": "\\.644",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "673ab04d-a495-4879-8329-d997ba0f48ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RubQDdyVbVdD6eXbT6qoBW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6296,
      "cache_read_input_tokens": 71995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6296
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 697 · 2026-05-23T11:37:22.668Z_

<details><summary>↩ Tool result · `toolu_016TQs9Sk4p8BiY46gkHfurE`</summary>

```text
docs/paper/appendix_extended.tex:253:arXiv   & 3 & 0.644~(2v3) & 4 & 0.624~(3v4) \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "16e320ba-5f88-49de-9e51-f5c88f1b04ed",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/appendix_extended.tex:253:arXiv   & 3 & 0.644~(2v3) & 4 & 0.624~(3v4) \\\\",
    "numLines": 1
  }
}
```

</details>

---


### Tool call

_source line 698_

<details open><summary>🔧 Tool call — Grep · `toolu_01XP7W4E6B7Eh2FFeCpNpzbk`</summary>

```json
{
  "pattern": "\\.620",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "9ca21c7a-f318-4d03-afd1-4ed49cd2747c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RubQDdyVbVdD6eXbT6qoBW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6296,
      "cache_read_input_tokens": 71995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6296
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-23T11:37:23.012Z_

<details><summary>↩ Tool result · `toolu_01XP7W4E6B7Eh2FFeCpNpzbk`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "73b5f562-4afa-4203-b59a-8da8001aacd4",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---


### Tool call

_source line 700_

<details open><summary>🔧 Tool call — Read · `toolu_01WFaNkGfdvwsNAQUqXRDppm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": 250,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "c8b97b31-939d-4b7a-8d3e-c31bd9e92ecd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VteW2ML1gAxx7t8nj663XZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 593,
      "cache_read_input_tokens": 78291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 593
      },
      "output_tokens": 53,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-23T11:37:27.495Z_

<details><summary>↩ Tool result · `toolu_01WFaNkGfdvwsNAQUqXRDppm`</summary>

```text
250	\textbf{Domain} & $\Kempirical$ & boundary $\auc$ & $\Kempirical$ & boundary $\auc$ \\
251	\midrule
252	C4      & 2 & 0.626~(1v2) & 2 & 0.705~(1v2) \\
253	arXiv   & 3 & 0.644~(2v3) & 4 & 0.624~(3v4) \\
254	Code    & 2 & 0.738~(1v2) & 2 & 0.808~(1v2) \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "2f52638e-f406-44ac-aa5a-d90cd7a08f89",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
      "content": "\\textbf{Domain} & $\\Kempirical$ & boundary $\\auc$ & $\\Kempirical$ & boundary $\\auc$ \\\\\n\\midrule\nC4      & 2 & 0.626~(1v2) & 2 & 0.705~(1v2) \\\\\narXiv   & 3 & 0.644~(2v3) & 4 & 0.624~(3v4) \\\\\nCode    & 2 & 0.738~(1v2) & 2 & 0.808~(1v2) \\\\",
      "numLines": 5,
      "startLine": 250,
      "totalLines": 258
    }
  }
}
```

</details>

---


### Tool call

_source line 702_

<details open><summary>🔧 Tool call — Edit · `toolu_01KMKaifm2sp2CZf4KNG2L9o`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "old_string": "arXiv   & 3 & 0.644~(2v3) & 4 & 0.624~(3v4) \\\\",
  "new_string": "arXiv   & 3 & 0.643~(2v3) & 4 & 0.624~(3v4) \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "ec46ecad-8365-4618-9574-b03111833494",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FmTncDsWLAWo4MQKXwoQZB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 78884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-23T11:37:37.263Z_

<details><summary>↩ Tool result · `toolu_01KMKaifm2sp2CZf4KNG2L9o`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "c6bc6cf6-df68-4183-bb1d-c7acc18112a5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "oldString": "arXiv   & 3 & 0.644~(2v3) & 4 & 0.624~(3v4) \\\\",
    "newString": "arXiv   & 3 & 0.643~(2v3) & 4 & 0.624~(3v4) \\\\",
    "originalFile": "\\section{Extended Discussion}\n\\label{sec:extended_discussion}\n\n\\subsection{Theoretical Implications of $\\Kempirical = 2$}\n\nThe DPI guarantees a finite $\\Ktheory$; for general web text, $\\Kempirical \\leq 2$ across all 10 configurations (1B--8B, 6 families), while structured domains (arXiv) yield $\\Kempirical{=}3$, aligning with model collapse convergence~\\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.\nDecoding strategy modestly affects signal strength (1v2 $\\auc \\in [0.6866, 0.7039]$) but does not shift the boundary.\n\n\\subsection{Cross-Model Transfer Implications}\n\nCross-model classification retains 80--100\\% accuracy with scorer-invariant feature rankings ($\\rho > 0.90$), enabling single-classifier deployment across generators.\nAbsolute discriminability at the $\\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\\Kempirical$ from 2 to 1, while rewrite-mode $\\Kempirical = 2$ is preserved.\nModel family similarity modulates transfer (Pythia$\\leftrightarrow$OLMo: 90--92\\% vs.\\ Qwen-cont$\\leftrightarrow$OLMo: 80--85\\%).\n\n\\begin{minipage}{\\columnwidth}\n\\centering\n\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1.}\n\\label{tab:crossscorer}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_crossscorer}}\n\\end{minipage}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair) on per-fold pairwise $\\auc$ values. DV = per-fold AUC; $N{=}300$ (12 cells $\\times$ 5 folds $\\times$ 5 depth-pairs). Scorer is statistically significant but explains modest variance ($\\eta^2_p{=}.166$) relative to Depth-Pair ($\\eta^2_p{=}.997$), supporting near-scorer-independence of depth discrimination.}\n\\label{tab:anova_crossscorer}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Source} & \\textbf{df} & $F$ & $p$ & $\\eta^2_p$ \\\\\n\\midrule\nGenerator     & 2  & 851.91  & ${<}.001$  & .866 \\\\\nScorer        & 3  & 17.48  & ${<}.001$  & .166 \\\\\nDepth-Pair    & 4  & 22737.70  & ${<}.001$  & .997 \\\\\nGen$\\times$Scorer & 6 & 7.50 & ${<}.001$ & .146 \\\\\nGen$\\times$Depth  & 8 & 913.41 & ${<}.001$ & .965 \\\\\nScorer$\\times$Depth & 12 & 2.25 & $.010$ & .093 \\\\\nResidual      & 264 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Feature Importance Across Decoding Strategies}\n\nFeature importance ordering varies across decoding strategies: greedy and $T{=}0.7$ share highly correlated rankings ($\\rho = 0.914$), while greedy vs.\\ $T{=}1.2$ yields lower correlation ($\\rho = 0.53$, nonsignificant after Bonferroni).\nThe depth boundary is robust but the optimal feature subset is strategy-dependent.\n\n\\subsection{Scale and Neural Probe}\n\\label{sec:extended_neural_probe}\n\nCross-scale validation confirms $\\Kempirical = 2$ from 1.5B through 8B: Qwen-7B (1v2 $\\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\\auc = 0.6123$, 0v1 $= 0.9224$) both exceed $\\theta$, with progressively lower 0v1 signal consistent with larger models generating more human-like text.\nGemma-2-27B (C4 continuation, Qwen cross-scored) yields $\\Kempirical{=}1$ (1v2 $\\auc = 0.5894$), consistent with Gemma-2-2B at 5K ($\\Kempirical{=}1$, 1v2 $\\auc = 0.5981$). The Gemma family produces $\\Kempirical{=}1$ at both 2B and 27B, suggesting $\\Kempirical$ is model-family-dependent rather than scale-dependent.\n\nThe neural probe yields model-dependent $\\Kempirical^{\\text{neural}}$: $3$ for Qwen (self-familiarity effect from instruction-tuned representations) but $2$ for Pythia; OLMo yields $\\Kempirical^{\\text{neural}} = 1$ (1v2 $\\auc = 0.5054$), consistent with the 15D LightGBM boundary.\nThe 15D generator-agnostic features yield $\\Kempirical = 2$ for Pythia and Qwen, while OLMo yields $\\Kempirical = 1$ under the standardized pipeline.\n\n\\subsection{LLM Zero-Shot Baseline}\n\\label{sec:extended_llm}\n\nGPT-5.5 achieves 33.2\\% accuracy (MAE = 1.10) and Claude Opus~4.6 33.1\\% (MAE = 1.15) on a balanced 500-sample test set, comparable to OBD-LightGBM's 38.0\\% (95\\% CI: $[0.340, 0.422]$; McNemar $p = 0.081$, $0.069$; Table~\\ref{tab:s3_llm_zeroshot}).\nPer-depth recall confirms convergent failure at depths $\\geq 2$ (Section~\\ref{sec:why_kstar}).\nWhen 6-class probabilities are marginalized to 5 classes ($P(d{\\geq}4)$), accuracy rises to 44.4\\% but concentrates in depth-4 (recall: 22\\%$\\to$80\\%) while depths 2--3 collapse to 2--8\\%; we report raw 6-class results.\n\n\\subsection{Practical Considerations}\n\nAll filtering strategies degrade general capabilities (MMLU: 0.6018 $\\to$ 0.5865--0.5941; HellaSwag: 0.6821 $\\to$ 0.6638--0.6701); our 100\\% synthetic setting is an upper bound; in mixed corpora, degradation scales with contamination fraction~\\cite{shumailov2024collapse, dohmatob2024model}.\n$\\Kstar$-aware binary filtering reduces MMLU degradation by ${\\sim}$50\\% ($-$1.53\\,pp $\\to$ $-$0.77\\,pp), requires no per-model calibration, and is combinable with distribution-matching methods (DSIR, DoReMi).\n\n\\subsection{Additional Scope Analysis}\n\\label{sec:extended_limitations}\n\n\\emph{Prompt-chain versus retrain-chain.}\nRetrain-chain validation (Pythia-1.4B LoRA, 5 generations) yields $\\Kempirical{\\geq}4$ (1v2 $\\auc = 0.9484$, 2v3 $= 0.8888$, 3v4 $= 0.7982$), far exceeding prompt-chain $\\Kempirical{=}2$.\nThe elevated signal arises from cumulative model-adaptation artifacts rather than text-intrinsic degradation; prompt-chain $\\Kempirical$ is the operationally relevant boundary for data curation.\n\n\\emph{Threshold sensitivity.}\nAt $\\theta = 0.55$, $\\Kempirical = 3$ for Qwen-rewrite/continuation; at $\\theta = 0.70$, $\\Kempirical = 1$ across all configurations (Figure~\\ref{fig:kstar_theta}).\nQwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp; all ten boundary comparisons yield permutation $p < 0.001$.\n\n\\emph{Structural confound: token length.}\nIn continuation mode the generation prompt is discarded, so all depths $\\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\\ machine-generated prompt), not structural composition.\nDepth~0 texts average ${\\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\\ref{tab:token_length}).\nThis asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.\nWithin depths 1--5, mean token counts are stable (within-model range $\\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\\Kempirical{=}2$ are unaffected by length.\nEOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\\%, Pythia 34--36\\%, OLMo $<$1\\%, Qwen-continuation 17--20\\%, Qwen-7B 45--47\\%.\nModels with the highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.\n\n\\emph{Graduated filtering.}\nAll $\\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\\alpha{=}0.1$: 0.5873; $\\alpha{=}0.9$: 0.5892 vs.\\ 0.5941); at $\\alpha{=}0.9$, HellaSwag matches exactly (0.6701).\nBinary-ours significantly outperforms all alternatives on MMLU ($p_{\\text{corr}} \\leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\\text{corr}} = 0.011$).\n\\label{tab:pairwise_significance}\n\n\\subsection{Dose-Response: Contamination Ratio Effect}\n\\label{sec:dose_response}\n\nThe main filtering experiments (Section~\\ref{sec:filtering}) use 100\\% synthetic data to maximize effect size.\nTo characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\\%, 30\\%, and 50\\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\\ref{tab:dose_response}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MMLU accuracy by contamination ratio (fraction of synthetic data in training set) and filtering strategy. Base model (no fine-tuning): 0.6018. Mean $\\pm$ std over 5 seeds.}\n\\label{tab:dose_response}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{10\\%} & \\textbf{30\\%} & \\textbf{50\\%} \\\\\n\\midrule\nNo-filter   & $0.6009 \\pm .003$ & $0.5978 \\pm .004$ & $0.5932 \\pm .004$ \\\\\nBinary-ours & $0.6011 \\pm .003$ & $0.5988 \\pm .003$ & $0.5956 \\pm .004$ \\\\\nGraduated   & $0.6008 \\pm .003$ & $0.5982 \\pm .004$ & $0.5944 \\pm .004$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n{\\sloppy At 10\\% contamination, no-filter MMLU ($0.6009$) remains within noise of the base model ($0.6018$, $\\Delta = -0.09$\\,pp), and all three strategies are indistinguishable ($\\Delta_{\\max} = 0.03$\\,pp between strategies, $p > 0.8$).\nAt 30\\%, differences emerge directionally ($\\Delta = 0.10$\\,pp, binary vs.\\ no-filter) but remain non-significant ($p > 0.3$).\nAt 50\\%, binary-ours shows a 0.24\\,pp advantage over no-filter, approaching but not reaching significance ($p = 0.12$).\nThe strategy ordering (binary $>$ graduated $>$ no-filter) is consistent with the 100\\% setting, but effect sizes scale linearly with contamination fraction.\nThis demonstrates that $\\Kstar$-aware curation provides practical benefit primarily when contamination is severe enough to cause measurable quality degradation.\\par}\n\n\\subsection{Seed Robustness}\n\\label{sec:seed_robustness}\n\nBecause the random seed governs both corpus sampling and generation quality (not merely CV splits), absolute AUC values are seed-dependent.\nWe re-run three configurations with seed$\\,{=}\\,123$ (primary: seed$\\,{=}\\,42$; Table~\\ref{tab:seed_robustness}).\n$\\Kempirical$ is stable in 2/3 cases: Pythia-1.4B on Wikipedia yields $\\Kempirical{=}1$ under both seeds (1v2 $\\Delta = -0.8$\\,pp), and Qwen-1.5B on C4 yields $\\Kempirical{=}2$ (1v2 $\\Delta = +9.0$\\,pp, both seeds above $\\theta$).\nQwen-1.5B on Wikipedia shifts from $\\Kempirical{=}2$ to $\\Kempirical{=}3$ under seed$\\,{=}\\,123$, but the 2v3 AUC ($0.6067$) is marginal: one of five folds falls below $\\theta$ (fold~5 $= 0.595$), so this does not constitute strong evidence for $\\Kempirical{=}3$.\nThe ${\\pm}9$\\,pp absolute AUC variation across seeds strengthens the methodological case for threshold-based $\\Kempirical$ over raw AUC comparisons: the qualitative boundary is robust even when point estimates shift.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Seed robustness: $\\Kempirical$ under two random seeds. 1v2 $\\Delta$: change in 1v2 AUC from seed 42 to seed 123. $\\Kempirical$ is stable in 2/3 configurations; the Qwen-Wiki shift to $\\Kempirical{=}3$ is marginal (2v3 fold variance crosses $\\theta$).}\n\\label{tab:seed_robustness}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Domain} & \\multicolumn{2}{c}{$\\Kempirical$} & \\textbf{1v2 $\\Delta$} & \\textbf{Stable?} \\\\\n\\cmidrule(lr){3-4}\n & & seed=42 & seed=123 & & \\\\\n\\midrule\nPythia-1.4B & Wikipedia & 1 & 1 & $-0.8$\\,pp & \\checkmark \\\\\nQwen-1.5B  & C4        & 2 & 2 & $+9.0$\\,pp & \\checkmark \\\\\nQwen-1.5B  & Wikipedia & 2 & 3$^\\dagger$ & $+8.7$\\,pp & $\\times$ \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$2v3 $\\auc = 0.6067$; fold 5 $= 0.595 < \\theta$. Marginal boundary.}\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Bonferroni-Corrected Confidence Intervals}\n\\label{sec:bonferroni_ci}\n\nTo control the family-wise error rate across all 10 model configurations, we apply Bonferroni correction: $\\alpha_{\\text{corr}} = 0.05 / 10 = 0.005$, yielding 99.5\\% confidence intervals ($z = 2.807$).\nTable~\\ref{tab:bonferroni_ci} reports the corrected intervals for each configuration's $\\Kempirical$ boundary pair.\nSeven of ten configurations retain CI lower bounds above $\\theta{=}0.60$; three marginal $\\Kempirical{=}2$ configurations (Pythia-1.4B, Qwen-cont, LLaMA-8B) see their lower bounds dip below $\\theta$ under the stricter criterion ($0.5934$, $0.5976$, and $0.5988$, respectively).\nThese near-misses reflect narrow effect sizes ($\\auc - \\theta < 0.013$) rather than classification failure: all three retain point estimates above $\\theta$, and Qwen-cont and LLaMA-8B retain uncorrected 95\\% CI lower bounds above $\\theta$ (Pythia-1.4B falls marginally below at $0.5976$).\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Bonferroni-corrected 99.5\\% confidence intervals for $\\Kempirical$ boundary pairs across all 10 configurations. $\\alpha_{\\text{corr}} = 0.005$; CI computed as $\\auc \\pm 2.807 \\times \\hat{\\sigma}_{\\text{boot}}$. ``Pass $\\theta$'': CI lower bound $> 0.60$.}\n\\label{tab:bonferroni_ci}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Configuration} & \\textbf{Boundary} & $\\auc$ & $\\hat{\\sigma}_{\\text{boot}}$ & \\textbf{99.5\\% CI} & \\textbf{Pass $\\theta$} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$\\Kempirical = 2$ configurations}} \\\\\nQwen-rw (Instruct)       & 1v2 & .6955 & .0046 & $[.683,\\,.708]$ & \\checkmark \\\\\nPythia-1.4B               & 1v2 & .6074 & .0050 & $[.593,\\,.621]$ & $\\times$ \\\\\nQwen-base                 & 1v2 & .6260 & .0047 & $[.613,\\,.639]$ & \\checkmark \\\\\nQwen-7B$^\\ddagger$        & 1v2 & .6168 & .0046 & $[.604,\\,.630]$ & \\checkmark \\\\\nLLaMA-8B                  & 1v2 & .6123 & .0048 & $[.599,\\,.626]$ & $\\times$ \\\\\nQwen-cont (Instruct)     & 1v2 & .6112 & .0049 & $[.598,\\,.625]$ & $\\times$ \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$\\Kempirical = 1$ configurations}} \\\\\nOLMo-1B                   & 0v1 & .9860 & .0009 & $[.983,\\,.989]$ & \\checkmark \\\\\nMistral-7B                & 0v1 & .9170 & .0030$^\\dagger$ & $[.909,\\,.925]$ & \\checkmark \\\\\nPythia-6.9B$^\\S$          & 0v1 & .9599 & .0015$^\\dagger$ & $[.956,\\,.964]$ & \\checkmark \\\\\nGemma-2-2B                & 0v1 & .9530 & .0018 & $[.948,\\,.958]$ & \\checkmark \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B; scorer: Qwen2.5-1.5B.} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\S$Nucleus sampling ($p{=}0.95$, $T{=}1.0$).} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$Estimated from analogous configurations (no separate bootstrap JSON).}\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Cross-Sample Robustness: 5K vs.\\ 10K}\n\\label{sec:robustness_10k}\n\nThe preceding analyses fix the sample pool at $N{=}5{,}000$ passages per depth.\nTo assess between-sample variability, we re-draw an independent $N{=}10{,}000$ sample from C4 using a different random seed and repeat the full OBD pipeline.\nIf $\\Kempirical$ and the boundary AUC are driven by the underlying distributional shift rather than by idiosyncrasies of a particular sample, both quantities should remain stable across draws.\n\nTable~\\ref{tab:robustness_10k} reports the results.\nFor Pythia-1.4B (continuation, C4), the 5K and 10K samples agree on $\\Kempirical{=}2$: the 0v1 AUC is nearly identical ($0.9722$ vs.\\ $0.9712$), and the boundary 1v2 AUC shifts from $0.6074$ to $0.6175$ ($\\Delta = +0.010$).\nThis narrow shift is consistent with natural sampling variability across C4 subsets and does not alter the qualitative depth boundary.\nThe 2v3 pair remains near chance in both draws ($0.54$, $0.54$), confirming that depths $\\geq 2$ are indistinguishable regardless of sample.\nQwen-1.5B (continuation, C4) replicates the same pattern ($\\Kempirical{=}2$, 1v2 $\\auc = 0.6346$).\nLLaMA-3.1-8B (continuation, C4) is the sole $\\Kempirical{=}2$ configuration where the 10K OOF AUC drops below $\\theta$ ($0.5880$; pipeline AUC $= 0.6148$; Bonferroni 99.5\\% CI $[0.5776, 0.5978]$), yielding $\\Kempirical{=}1$ under the stricter criterion.\nOLMo-1B (continuation, C4) is the only configuration that yields $\\Kempirical{=}1$ at both 5K and 10K, with virtually identical depth profiles (0v1 $\\auc = 0.9871$ vs.\\ $0.9860$; 1v2 $\\auc = 0.4984$ vs.\\ $0.5001$); the 1v2 AUC at random level is consistent with Qwen cross-scoring, which places OLMo well below the discrimination boundary.\nGemma-2-2B is the sole configuration where $\\Kempirical$ increases from 5K ($\\Kempirical{=}1$, 1v2 $\\auc = 0.5981$) to 10K ($\\Kempirical{=}2$, 1v2 $\\auc = 0.6099$), but the 10K boundary AUC exceeds $\\theta$ by only $0.010$, placing this model at the precise $\\Kempirical{=}1/2$ boundary.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Cross-sample robustness: pairwise AUC and $\\Kempirical$ under 5K and 10K C4 samples drawn with different random seeds. All configurations use continuation mode. $\\Kempirical$ is determined by the $\\theta{=}0.60$ threshold on 1v2 AUC.}\n\\label{tab:robustness_10k}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & $N$ & \\textbf{AUC(0v1)} & \\textbf{AUC(1v2)} & \\textbf{AUC(2v3)} & $\\Kempirical$ \\\\\n\\midrule\nPythia-1.4B cont & 5K  & \\multicolumn{3}{c}{(see Table~\\ref{tab:bonferroni_ci})} & 2 \\\\\nPythia-1.4B cont & 10K & 0.9712 & 0.6175 & 0.5364 & 2 \\\\\n\\midrule\nQwen-1.5B cont  & 5K  & \\multicolumn{3}{c}{(see Table~\\ref{tab:bonferroni_ci})} & 2 \\\\\nQwen-1.5B cont  & 10K & 0.9875 & 0.6346 & 0.5616 & 2 \\\\\n\\midrule\nLLaMA-8B cont   & 5K  & \\multicolumn{3}{c}{(see Table~\\ref{tab:bonferroni_ci})} & 2 \\\\\nLLaMA-8B cont   & 10K & 0.9282 & 0.5880$^\\dagger$ & 0.5247 & 1$^\\dagger$ \\\\\n\\midrule\nOLMo-1B cont    & 5K  & \\multicolumn{3}{c}{(see Table~\\ref{tab:bonferroni_ci})} & 1 \\\\\nOLMo-1B cont    & 10K & 0.9871 & 0.4984 & 0.5059 & 1 \\\\\n\\midrule\nGemma-2-2B cont & 5K  & \\multicolumn{3}{c}{(see Table~\\ref{tab:kstar_ci_extended})} & 1 \\\\\nGemma-2-2B cont & 10K & 0.9534 & 0.6099$^\\ddagger$ & 0.5409 & 2$^\\ddagger$ \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$OOF AUC (pipeline AUC $= 0.6148$); Bonferroni 99.5\\% CI $[0.5776, 0.5978]$ does not pass $\\theta$.} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\ddagger$Borderline: Bonferroni 99.5\\% CI $[0.600,\\,0.619]$ (percentile); CI lower $0.0002$ below $\\theta$. Sole config where $\\Kempirical$ increases from 5K to 10K.} \\\\\n\\end{tabular}}\n\\end{table}\n\n\\subsection{DeBERTa Upper-Bound Comparison}\n\\label{sec:deberta_upperbound}\n\nTo assess how much of the theoretical discrimination boundary the 15-feature OBD classifier captures, we fine-tune DeBERTa-v3-base on raw text as an upper-bound probe.\nTable~\\ref{tab:deberta_vs_obd} compares $\\Kempirical$ across three domains.\nDeBERTa matches OBD on C4 and Code ($\\Kempirical{=}2$) but extends $\\Kempirical$ to~4 on arXiv (3v4 $\\auc = 0.624$, CI $[0.613, 0.635]$), one depth beyond the 15-feature boundary.\nThe gap quantifies the cost of generator-agnostic features: one depth level on structured text, zero on general web text.\n\n\\begin{table}[t]\n\\centering\n\\caption{$\\Kempirical$ comparison: 15-feature OBD vs.\\ DeBERTa-v3-base (Qwen-1.5B generation, $\\theta{=}0.60$). DeBERTa extends $\\Kempirical$ by one depth on arXiv but not on C4 or Code.}\n\\label{tab:deberta_vs_obd}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{OBD (15D)}} & \\multicolumn{2}{c}{\\textbf{DeBERTa}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Domain} & $\\Kempirical$ & boundary $\\auc$ & $\\Kempirical$ & boundary $\\auc$ \\\\\n\\midrule\nC4      & 2 & 0.626~(1v2) & 2 & 0.705~(1v2) \\\\\narXiv   & 3 & 0.644~(2v3) & 4 & 0.624~(3v4) \\\\\nCode    & 2 & 0.738~(1v2) & 2 & 0.808~(1v2) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 250,
        "oldLines": 7,
        "newStart": 250,
        "newLines": 7,
        "lines": [
          " \\textbf{Domain} & $\\Kempirical$ & boundary $\\auc$ & $\\Kempirical$ & boundary $\\auc$ \\\\",
          " \\midrule",
          " C4      & 2 & 0.626~(1v2) & 2 & 0.705~(1v2) \\\\",
          "-arXiv   & 3 & 0.644~(2v3) & 4 & 0.624~(3v4) \\\\",
          "+arXiv   & 3 & 0.643~(2v3) & 4 & 0.624~(3v4) \\\\",
          " Code    & 2 & 0.738~(1v2) & 2 & 0.808~(1v2) \\\\",
          " \\bottomrule",
          " \\end{tabular}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Assistant

_source line 704_

All clear rounding errors fixed. Here is the complete audit report:

---

## 全文数据审计报告

### 已修复（来源明确的舍入错误）

| 位置 | 论文原值 | Registry值 | 修正后 |
|------|---------|-----------|--------|
| Tab4 arXiv/Qwen 2v3 AUC | .644 | 0.6427→.643 | **.643** |
| Tab S12 arXiv 2v3 | .644 | 同上 | **.643** |
| experiments_c1 inline arXiv 2v3 | 0.644 | 同上 | **0.643** |
| appendix_extended DeBERTa table | 0.644 | 同上 | **0.643** |
| experiments_c1 inline LLaMA arXiv 2v3 | 0.620 | 0.6215→.622 | **0.622** |
| Tab4 Code/LLaMA 2v3 AUC | .510 | 0.5112→.511 | **.511** |
| Tab S12 arXiv 4v5 | .530 | 0.5294→.529 | **.529** |

### 需要人工确认的不匹配（严重度从高到低）

#### CRITICAL: Neural probe OLMo (experiments_c1.tex Table neural_probe_crossmodel)

| 位置 | 论文值 | Registry exp_id | Registry值 |
|------|--------|----------------|-----------|
| OLMo 1v2 AUC | 0.5054 | exp_015 | **0.657** |
| OLMo 2v3 AUC | 0.5056 | exp_015 | **0.589** |
| OLMo K* | 1 | exp_015 | **2** |

论文值（0.505x）酷似 15D OBD cross-scored 结果（exp_002: 1v2=0.5001），疑似误用了 OBD 值替代 neural probe 值。如果 registry 正确，则 OLMo neural probe K*=2，论文中 K*=1 的结论需修改，连带 discussion.tex 中引用此结果的段落。

#### HIGH: Mistral-7B 全部 AUC (Tab kstar_ci_extended)

| 位置 | 论文值 | exp_019 (self) | exp_019b (cross) |
|------|--------|---------------|-----------------|
| 0v1 | .9170 | 0.9843 | 0.9209 |
| 1v2 | .5750 | 0.5935 | 0.5695 |
| 2v3 | .5369 | 0.5402 | 0.5335 |
| 3v4 | .5174 | 0.5232 | 0.5140 |

论文值既不等于 self-scored 也不等于 cross-scored。2v3 值恰好等于两者均值 (0.5402+0.5335)/2=0.5369，但其他行不符合此规律。来源不明。

#### HIGH: Table S8 Pythia/OLMo 混用 self/cross-scored 数据

| 位置 | 论文值 | exp_007 (self) | exp_001/002 (cross) |
|------|--------|---------------|-------------------|
| S8 Pythia 1v2 | .607 | 0.6539 | 0.6074 (exp_001) |
| S8 OLMo 全5行 | .986/.500/.497/.502/.494 | .997/.614/.550/.509/.505 | ≈matches AUC only, CI无来源 |

Table S8 标注为 exp-007 bootstrap CI，但 OLMo 行使用了 cross-scored AUC（无对应 CI），Pythia 1v2 同样混用。CIs 无法追溯到任何 registry 实验。

#### HIGH: Table S10 Pythia Decoding (10/20 cells mismatch)

10个值与 exp_020 相差 0.002–0.008，非系统性偏差，可能来自 rerun 或 bootstrap-mean vs OOF-AUC 的差异。涉及行：1v2/nuc09, 2v3全行, 3v4/nuc09+t07+t12, 4v5/greedy+t12。

#### MODERATE: OLMo 3v4/4v5 (Table 1)

| 位置 | 论文值 | exp_002 |
|------|--------|---------|
| 3v4 | .5024 | 0.5034 |
| 4v5 | .4942 | 0.4971 |

差异 0.001–0.003，可能来自 scorer 更新前的旧值。

#### MODERATE: Discussion inline 数字

| 位置 | 论文值 | Registry值 |
|------|--------|-----------|
| "≈+1.9 pp" Mistral gap | 1.9 pp | 2.4 pp (0.5935−0.5695) |
| "0.15–0.27" JSD (≤1.5B) | 0.15–0.27 | 0.164–0.286 (registry range) |

### 匹配确认（所有其他值）

- **Table 1 (tab:kstar_ci)**: Qwen-rw/Pythia/Qwen-cont/Qwen-7B 全部 25 个 AUC + CI 值 ✓（OLMo 0v1/1v2/2v3 也 ✓）
- **Extended table**: Qwen-base 全 5 行 ✓, LLaMA-8B 全 5 行 ✓, Pythia-6.9B 全 ✓, Gemma-2B 全 ✓
- **Table S1 (transfer matrix)**: 16/16 cells ✓, retention% inline claims ✓
- **Table S2 (decoding ablation)**: 20/20 AUC + CI cells ✓（Spearman ρ 6个值不在 registry，无法验证）
- **Table 4 (domain)**: 其余 10/12 cells ✓
- **Filtering table**: 7/7 rows 全 ✓
- **experiments_c3.tex inline**: −1.53pp ✓, −0.77pp ✓, ~50% ✓, p 值全 ✓
- **introduction.tex**: MMLU 0.5941 ✓, base 0.6018 ✓, p≤0.002 ✓
- **discussion.tex**: 0v1 AUC≥0.92 ✓, 96% recall ✓, 14–22% ✓, 8–38% ✓, retrain chain 0.68–0.80 ✓, 6v7 0.634–0.641 ✓, Δauc −0.021 ✓

### 无法验证（registry 未存储）

- η²_p = .166 / .146（ANOVA 未单独注册实验）
- Table S2 Spearman ρ 6 个值（exp_003 未存储）
- Table S11 除 1v2 外的 12 个值（exp_021 仅存 1v2）
- Table S12 Wiki 0v1/3v4/4v5（exp_023 仅存 1v2/2v3）
- 部分 CI（Pythia 2v3, OLMo 全部, Gemma 多数）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "uuid": "dfb2f8df-56cb-4297-8c45-427e07419c9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hrcz9QvWAEZVFgNh9mnEqc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 275,
      "cache_read_input_tokens": 79286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 275
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 705_

All clear rounding errors fixed. Here is the complete audit report:

---

## 全文数据审计报告

### 已修复（来源明确的舍入错误）

| 位置 | 论文原值 | Registry值 | 修正后 |
|------|---------|-----------|--------|
| Tab4 arXiv/Qwen 2v3 AUC | .644 | 0.6427→.643 | **.643** |
| Tab S12 arXiv 2v3 | .644 | 同上 | **.643** |
| experiments_c1 inline arXiv 2v3 | 0.644 | 同上 | **0.643** |
| appendix_extended DeBERTa table | 0.644 | 同上 | **0.643** |
| experiments_c1 inline LLaMA arXiv 2v3 | 0.620 | 0.6215→.622 | **0.622** |
| Tab4 Code/LLaMA 2v3 AUC | .510 | 0.5112→.511 | **.511** |
| Tab S12 arXiv 4v5 | .530 | 0.5294→.529 | **.529** |

### 需要人工确认的不匹配（严重度从高到低）

#### CRITICAL: Neural probe OLMo (experiments_c1.tex Table neural_probe_crossmodel)

| 位置 | 论文值 | Registry exp_id | Registry值 |
|------|--------|----------------|-----------|
| OLMo 1v2 AUC | 0.5054 | exp_015 | **0.657** |
| OLMo 2v3 AUC | 0.5056 | exp_015 | **0.589** |
| OLMo K* | 1 | exp_015 | **2** |

论文值（0.505x）酷似 15D OBD cross-scored 结果（exp_002: 1v2=0.5001），疑似误用了 OBD 值替代 neural probe 值。如果 registry 正确，则 OLMo neural probe K*=2，论文中 K*=1 的结论需修改，连带 discussion.tex 中引用此结果的段落。

#### HIGH: Mistral-7B 全部 AUC (Tab kstar_ci_extended)

| 位置 | 论文值 | exp_019 (self) | exp_019b (cross) |
|------|--------|---------------|-----------------|
| 0v1 | .9170 | 0.9843 | 0.9209 |
| 1v2 | .5750 | 0.5935 | 0.5695 |
| 2v3 | .5369 | 0.5402 | 0.5335 |
| 3v4 | .5174 | 0.5232 | 0.5140 |

论文值既不等于 self-scored 也不等于 cross-scored。2v3 值恰好等于两者均值 (0.5402+0.5335)/2=0.5369，但其他行不符合此规律。来源不明。

#### HIGH: Table S8 Pythia/OLMo 混用 self/cross-scored 数据

| 位置 | 论文值 | exp_007 (self) | exp_001/002 (cross) |
|------|--------|---------------|-------------------|
| S8 Pythia 1v2 | .607 | 0.6539 | 0.6074 (exp_001) |
| S8 OLMo 全5行 | .986/.500/.497/.502/.494 | .997/.614/.550/.509/.505 | ≈matches AUC only, CI无来源 |

Table S8 标注为 exp-007 bootstrap CI，但 OLMo 行使用了 cross-scored AUC（无对应 CI），Pythia 1v2 同样混用。CIs 无法追溯到任何 registry 实验。

#### HIGH: Table S10 Pythia Decoding (10/20 cells mismatch)

10个值与 exp_020 相差 0.002–0.008，非系统性偏差，可能来自 rerun 或 bootstrap-mean vs OOF-AUC 的差异。涉及行：1v2/nuc09, 2v3全行, 3v4/nuc09+t07+t12, 4v5/greedy+t12。

#### MODERATE: OLMo 3v4/4v5 (Table 1)

| 位置 | 论文值 | exp_002 |
|------|--------|---------|
| 3v4 | .5024 | 0.5034 |
| 4v5 | .4942 | 0.4971 |

差异 0.001–0.003，可能来自 scorer 更新前的旧值。

#### MODERATE: Discussion inline 数字

| 位置 | 论文值 | Registry值 |
|------|--------|-----------|
| "≈+1.9 pp" Mistral gap | 1.9 pp | 2.4 pp (0.5935−0.5695) |
| "0.15–0.27" JSD (≤1.5B) | 0.15–0.27 | 0.164–0.286 (registry range) |

### 匹配确认（所有其他值）

- **Table 1 (tab:kstar_ci)**: Qwen-rw/Pythia/Qwen-cont/Qwen-7B 全部 25 个 AUC + CI 值 ✓（OLMo 0v1/1v2/2v3 也 ✓）
- **Extended table**: Qwen-base 全 5 行 ✓, LLaMA-8B 全 5 行 ✓, Pythia-6.9B 全 ✓, Gemma-2B 全 ✓
- **Table S1 (transfer matrix)**: 16/16 cells ✓, retention% inline claims ✓
- **Table S2 (decoding ablation)**: 20/20 AUC + CI cells ✓（Spearman ρ 6个值不在 registry，无法验证）
- **Table 4 (domain)**: 其余 10/12 cells ✓
- **Filtering table**: 7/7 rows 全 ✓
- **experiments_c3.tex inline**: −1.53pp ✓, −0.77pp ✓, ~50% ✓, p 值全 ✓
- **introduction.tex**: MMLU 0.5941 ✓, base 0.6018 ✓, p≤0.002 ✓
- **discussion.tex**: 0v1 AUC≥0.92 ✓, 96% recall ✓, 14–22% ✓, 8–38% ✓, retrain chain 0.68–0.80 ✓, 6v7 0.634–0.641 ✓, Δauc −0.021 ✓

### 无法验证（registry 未存储）

- η²_p = .166 / .146（ANOVA 未单独注册实验）
- Table S2 Spearman ρ 6 个值（exp_003 未存储）
- Table S11 除 1v2 外的 12 个值（exp_021 仅存 1v2）
- Table S12 Wiki 0v1/3v4/4v5（exp_023 仅存 1v2/2v3）
- 部分 CI（Pythia 2v3, OLMo 全部, Gemma 多数）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1008962,
  "duration_api_ms": 3136697,
  "num_turns": 23,
  "stop_reason": "end_turn",
  "session_id": "17947013-ea3d-4507-b0e3-f06dfa8892ff",
  "total_cost_usd": 8.18067905,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 67720,
    "cache_read_input_tokens": 418964,
    "output_tokens": 15897,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 67720,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2085,
        "cache_read_input_tokens": 79286,
        "cache_creation_input_tokens": 275,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 275
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1478,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001553,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 15897,
      "cacheReadInputTokens": 418964,
      "cacheCreationInputTokens": 67720,
      "webSearchRequests": 0,
      "costUSD": 1.030227,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    },
    "claude-sonnet-4-6": {
      "inputTokens": 222,
      "outputTokens": 144945,
      "cacheReadInputTokens": 11772506,
      "cacheCreationInputTokens": 384615,
      "webSearchRequests": 0,
      "costUSD": 7.14889905,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "bd37f75a-2e16-4d9e-a740-7f876b7365d2"
}
```

</details>

---
