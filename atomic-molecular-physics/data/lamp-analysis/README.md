# Guarded candidate measurements and a conditional Ritz reconstruction

Reproduce these outputs from the repository root:

```sh
python3 atomic-molecular-physics/analysis/raw_spectrum_to_levels.py --no-plot --output-dir atomic-molecular-physics/data/lamp-analysis
```

`candidate-lines.csv` lists local maxima above a declared relative threshold, not a significance-selected list of atomic lines. `analysis-summary.json` records method settings, source checksum, fit diagnostics, seven reference candidates and conditional Ritz sums. The current threshold produces 38 maxima: 31 pass the limited core-fit guards and seven fail. Passing a guard does not prove an isolated line or provide a formal uncertainty.

The method fits a quadratic to the logarithm of positive core samples in an eleven-sample window. It rejects undersampled fits, nonnegative curvature, displaced vertices and widths outside the fitting window. A background residual, blend or non-Gaussian instrumental profile can still bias a retained estimate. No raw-count variance or calibration covariance is supplied, so the report does not invent centroid error bars.

Upstream normalization maxima at 10000 are included, with an informational flag; they are not masked as saturated samples. See the [source audit](../lamp-archive/README.md). Only seven imported Cd/Hg references are considered. Other maxima are **not compared against a complete line list**; they have not been demonstrated to be impurities or unidentified physical lines.

The Cd reconstruction uses four transitions connecting five levels, including the ground-state anchor. It has no independent closed cycle. The labels and shared-level assignments are reference inputs, and the wavelength axis already uses known lamp lines. The resulting numerical agreement is a reconstruction demonstration, not independent validation.
