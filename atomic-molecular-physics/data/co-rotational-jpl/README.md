# Experimental CO rotational line centres

`reference-lines.csv` transcribes the first three entries of the JPL catalogue for ground-vibrational-state **¹²C¹⁶O**, species 28001, version 4 (August 1997). These are tabulated experimental transition centres, not detector intensities or frequency-scan traces.

The [primary catalogue](https://spec.jpl.nasa.gov/ftp/pub/catalog/c028001.cat) lists frequencies and uncertainties in MHz. Each selected row carries the negative tag `-28001`. The [CDMS CO example](https://cdms.astro.uni-koeln.de/classic/predictions/pickett/beispiele/CO/) explains that negative tags identify experimental lines merged into a catalogue of predictions. The [JPL entry documentation](https://spec.jpl.nasa.gov/ftp/pub/catalog/doc/d028001.cat) identifies the measurements as those of G. Winnewisser, S. P. Belov, Th. Klaus and R. Schieder, *Sub-Doppler Measurements on the Rotational Transitions of Carbon Monoxide*, **J. Mol. Spectrosc. 184**, 468–472 (1997), [doi:10.1006/jmsp.1997.7341](https://doi.org/10.1006/jmsp.1997.7341).

The numeric fields and complete browser-view source rows are preserved in `provenance.json`. Upstream whitespace and line endings were not checked byte for byte.

For the rigid-rotor test, set the frequency-unit rotational constant using **only** the first centre: `B = frequency(1←0)/2`. The unused centres then test `frequency(J←J−1) = 2 B J`. Their measured-minus-predicted residuals are **−4.4036 MHz** and **−17.6155 MHz**. The first residual is zero by construction.

The plot's error bars show only the catalogue's listed frequency uncertainty, 0.0005 MHz per centre. The shared uncertainty of the first-line calibration and correlations are not propagated; this is not a full residual uncertainty budget or precision fit. The error bars are smaller than the plotted symbols.

Run `python3 atomic-molecular-physics/analysis/plot_co_rotational_test.py` from the repository root to reproduce [the figure](../../figures/co-rotational-test.svg). A measured frequency-scan record remains a separate TODO in the course.
