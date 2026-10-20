\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{corl_2026}[2026/01/01 CoRL 2026 paper style (minimal)]
\DeclareOption{conference}{\relax}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[10pt,letterpaper,twocolumn]{article}
\RequirePackage[margin=1in]{geometry}
\RequirePackage{times}
\RequirePackage[numbers,sort&compress]{natbib}
\setlength{\parindent}{1em}
\setlength{\parskip}{0pt}
