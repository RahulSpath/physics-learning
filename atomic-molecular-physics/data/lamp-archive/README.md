# Provenance of the processed Hg–Cd–Ar calibration template

The existing [CSV](../hg-cd-ar-lamp-spectrum.csv) is an empirical **wavelength-calibration template**, not a raw CCD exposure. Its 7205 wavelength and signal samples exactly match the preserved PypeIt FITS `wave` and `flux` columns after rounding wavelengths to four decimal places and signal to three. Wavelengths are vacuum ångströms; signal values are arbitrary processed units. The inspected template release, checksums and preserved processing-source copies are recorded in `provenance.json`; the exact source-script commit was not retained.

`original-template.fits` preserves the upstream `ldt_deveny_1200_HgCdAr.fits`. The two `source-*.py` files preserve the inspected creation and builder code from the [PypeIt repository](https://github.com/pypeit/PypeIt). These source copies are evidence of processing, not extra programs needed to read the course.

The creation function `ldt_deveny_1200` uses four DV9 grating-angle calibration exposures, with nominal stitch cuts at 4300, 5300 and 6300 Å. It requests continuum subtraction, normalization and wavelength alignment. The builder scales each input snippet to a maximum of **10000**. Consequently, the four maxima at 10000 are normalization maxima; they do not establish clipping or detector saturation. Cross-segment heights are not on a common physical photon scale. A physically saturated original exposure would require separate detector evidence.

The original CSV header incorrectly describes the maxima as clipped. It is preserved unchanged as part of the archive, as is the older [line table](../measured-lines.csv), whose clipping flags, full-list assignments and some failed fits are superseded by the current analysis. Neither file should be used as a precision uncertainty budget.

The archive has a reference-calibrated wavelength scale. Agreement with those same reference lines is not an independent wavelength or atomic-model test. Raw variances, independent calibration residuals, intensity sensitivity and original segment scale factors are not supplied. The separate Hg, Cd and Ar control records proposed in Unit 8 also remain missing.

The PypeIt material retains its [BSD 3-clause licence](../PypeIt-LICENSE.txt). For the data-reduction project, see Prochaska et al., *PypeIt: The Python Spectroscopic Data Reduction Pipeline*, JOSS **5**, 2308 (2020), doi:10.21105/joss.02308.
