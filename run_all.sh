#!/usr/bin/env bash
# Reproduce all datasets, estimates and figures. Run from the repository root.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p output
echo "1/6 building data";                         python3 code/build_data.py >/dev/null
echo "2/6 decomposition, ITS (first pass), bands"; python3 code/analyze1.py >/dev/null
echo "3/6 robustness, disease type, permutation, wild bootstrap (about 1 minute)"; python3 code/analyze2.py >/dev/null 2>&1
echo "4/6 main estimates, FY2009-2025 window";    python3 code/analyze4_unified.py >/dev/null 2>&1
echo "5/6 evaluation-period analyses and alternative inference (revision 1)"; python3 code/analyze6_revision1.py >/dev/null 2>&1
echo "6/6 figures (PNG and TIFF 600 dpi)";       python3 code/make_figures_en.py >/dev/null 2>&1
echo "done: see output/"
