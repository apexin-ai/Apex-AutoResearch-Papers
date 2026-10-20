"""Batch-patch all chart scripts to add pdf.fonttype=42 / ps.fonttype=42."""
import re, os

SCRIPTS = [
    "/root/gen-depth-fingerprint/charts/gen_fig1.py",
    "/root/gen-depth-fingerprint/charts/gen_fig3.py",
    "/root/gen-depth-fingerprint/charts/fig_appendix_cross_temp.py",
    "/root/gen-depth-fingerprint/scripts/plot_nll_distribution.py",
    "/root/gen-depth-fingerprint/scripts/plot_instruct_ddr_comparison.py",
    "/root/gen-depth-fingerprint/scripts/plot_umap_appendix.py",
    "/root/gen-depth-fingerprint/paper/figures/gen_fig2_framework.py",
]

FONTTYPE_LINES = "    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n"
FONTTYPE_STANDALONE = (
    "import matplotlib\n"
    "matplotlib.rcParams['pdf.fonttype'] = 42\n"
    "matplotlib.rcParams['ps.fonttype'] = 42\n"
)

for path in SCRIPTS:
    if not os.path.exists(path):
        print(f"SKIP (not found): {path}")
        continue
    code = open(path).read()
    if 'pdf.fonttype' in code:
        print(f"SKIP (already has fonttype): {path}")
        continue

    if 'rcParams.update({' in code:
        code = code.replace(
            "rcParams.update({",
            "rcParams.update({\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,",
            1
        )
        open(path, 'w').write(code)
        print(f"PATCHED (rcParams block): {path}")
    elif 'import matplotlib' in code:
        code = code.replace(
            "import matplotlib\n",
            "import matplotlib\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\n",
            1
        )
        open(path, 'w').write(code)
        print(f"PATCHED (standalone): {path}")
    else:
        code = FONTTYPE_STANDALONE + code
        open(path, 'w').write(code)
        print(f"PATCHED (prepended): {path}")

print("\nDone patching.")
