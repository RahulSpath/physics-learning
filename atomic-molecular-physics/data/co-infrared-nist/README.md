# CO infrared transmission reference record

`original-spectrum.jdx` is the unchanged JCAMP-DX download of NIST Chemistry WebBook's gas-phase CO record, index 1: [source page](https://webbook.nist.gov/cgi/cbook.cgi?ID=C630080&Index=1&Type=IR-SPEC), [download](https://webbook.nist.gov/cgi/cbook.cgi?JCAMP=C630080&Index=1&Type=IR). It is a Coblentz Society reference spectrum originating at Dow Chemical Company, **Coblentz No. 8755 (1964)**. Its SHA-256 checksum and source metadata are recorded in `provenance.json`; the original file retains the source's owner and copyright notice.

The ordinate is **transmittance**, not emitted intensity, absorbance or molar absorptivity. The source gives 400 mmHg CO diluted with nitrogen to 600 mmHg total pressure, a 10 cm path, a Dow KBr-foreprism instrument and a listed resolution of 4 cm⁻¹. Temperature is not supplied.

NIST digitized this record from two hardcopy segments. The file explicitly states that congested rotational lines in **2000–2250 cm⁻¹ were smoothed upstream**. This matters: the band envelope is measured reference information, but individual line shapes and centres cannot be recovered from it as if it were a high-resolution scan. The source page also says concentration information sufficient for molar absorptivity is unavailable.

The [plotting script](../../analysis/plot_co_infrared.py) decodes all 3574 numerical points, using each source row's starting wavenumber and the listed within-row increment. Row anchors preserve the source coordinates; the header's last wavenumber is rounded. It plots the **1900–2300 cm⁻¹** window directly, with no new baseline correction, normalization, clipping, smoothing or peak fitting. No uncertainties are supplied, so none are invented.

Run `python3 atomic-molecular-physics/analysis/plot_co_infrared.py` from the repository root to reproduce [the figure](../../figures/co-infrared-measured.svg). The notes retain a separate TODO for high-resolution P/R-branch assignment and tests.
