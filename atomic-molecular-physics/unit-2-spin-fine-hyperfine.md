# Unit 2 · Spin, fine structure and hyperfine structure

## 2.1 What distinguishes the two hydrogen resonances?

In Unit 1, excitation from one prepared 2s state produced two separated resonances near the transition to 6p. The Coulomb model predicted one frequency. We begin with the same measured record:

![Measured hydrogen fluorescence counts against relative excitation wavenumber](figures/hydrogen-2s-6p-measured.svg)

*Figure 2.1. The measured 2s → 6p excitation scans used in Unit 1, reproduced here to guide the explanation. Points are fluorescence detector counts; the horizontal axis gives the exciting laser's relative wavenumber. The separation is about 405 MHz. The grey interval was not scanned. These are independently acquired frequency windows, not a continuous scan. Source: L. Maisenbacher's MPQ dataset, CC BY 4.0; acquisition details and provenance are preserved in the [local data record](data/hydrogen-2s-6p-mpq/README.md).*

With a common initial state, the two resonances reveal additional upper-state structure. What property distinguishes these states? A pair of peaks alone does not identify the cause. We need an independent way to investigate a degree of freedom that the Coulomb Hamiltonian omitted, and then an interaction that predicts the observed separation.

## 2.2 Can a magnetic probe reveal something that the optical spectrum does not?

Orbital angular momentum carries a magnetic moment. If the additional structure involves angular momentum, a measurement of magnetic response could help identify it. A uniform magnetic field changes a dipole's energy but does not separate a beam by a net force. A field gradient can convert different magnetic moments into different detector positions.

Consider a collimated beam of neutral atoms passing through a non-uniform magnetic field and then reaching a detector. Neutral atoms avoid the large Lorentz deflection of a charged beam. In a region where the field is approximately along $`z`$,

```math
U=-\boldsymbol{\mu}\cdot\mathbf B,
\qquad
F_z\simeq\mu_z\frac{\partial B_z}{\partial z}.
```

Compare the detector pattern with the field off and on. Does it merely broaden, or separate into distinct groups? How do their positions change with the gradient? Given the atomic mass, speed and flight distances, a deflection estimates the corresponding magnetic-moment projection.

This is the principle of the **Stern–Gerlach experiment**. Historically, silver supplied a practical neutral atomic beam. Its ground electronic state has zero total orbital angular momentum, while one outer electron determines its leading electronic magnetic response. Unit 3 will justify this reduction from a many-electron atom to an effective single outer electron.

> **TODO — Add the measured Stern–Gerlach detector record.**
>
> Show the field-off and field-on patterns before interpreting them. Include the field gradient, beam geometry and velocity information needed to infer a magnetic moment. Identify the experimental regime in which nuclear structure is unresolved. Do not replace the record with an illustration of two ideal spots.

The established result is two electronic deflection groups, corresponding approximately to moment projections $`\pm\mu_B`$. Orbital angular momentum alone does not explain this result. In particular, zero orbital angular momentum gives no orbital moment, and a fully populated orbital multiplet has $`2l+1`$ projections, with integer $`l`$.

The magnetic measurement therefore supplies evidence that was absent from the optical peak positions: an intrinsic electronic magnetic moment with two projections along the measurement axis.

## 2.3 Electron spin and the states it allows

We describe this intrinsic degree of freedom by **electron spin**, an angular momentum with $`s=\tfrac12`$:

```math
S^2=s(s+1)\hbar^2=\frac34\hbar^2,
\qquad
S_z=m_s\hbar,
\qquad m_s=\pm\frac12.
```

Its magnetic moment is

```math
\boldsymbol{\mu}_s=-g_s\mu_B\frac{\mathbf S}{\hbar},
\qquad
\mu_B=\frac{e\hbar}{2m_e},
\qquad g_s\simeq2.0023.
```

Thus its two moment projections are approximately $`\mp\mu_B`$. Spin is intrinsic; the equations do not describe a small charged sphere rotating about its axis. Nor do two measured projections mean that the spin has only two possible spatial directions.

Adding spin doubles the Coulomb state's multiplicity: a given $`n`$ now contains $`2n^2`$ electronic states. But a Hamiltonian independent of spin still gives them the same energy. Introducing a new state label does not itself split a spectral line. What interaction can distinguish the states?

The relevant angular momentum for a central, spin-dependent atom is

```math
\mathbf J=\mathbf L+\mathbf S,
\qquad
j=l\pm\frac12,
```

with only $`j=\tfrac12`$ when $`l=0`$. The labels 6p<sub>1/2</sub> and 6p<sub>3/2</sub>, for example, distinguish the two possible total angular momenta obtained from $`l=1`$ and $`s=\tfrac12`$. Each has $`2j+1`$ magnetic substates.

For one electron, the corresponding term symbols are $`{}^2P_{1/2}`$ and $`{}^2P_{3/2}`$. In $`{}^{2S+1}L_J`$, the superscript gives the spin multiplicity, the letter gives the orbital angular momentum, and the subscript gives total angular momentum. Here $`S=s`$, $`L=l`$ and $`J=j`$; Unit 3 extends the notation to several electrons.

## 2.4 Does the interaction predict the observed separation?

In the electron's instantaneous rest frame, the moving nucleus produces a magnetic field that couples to the spin moment. A consistent relativistic treatment, including the rotation of this accelerated frame, gives the **spin–orbit interaction**

```math
H_{\mathrm{so}}=
\frac{1}{2m_e^2c^2r}\frac{dV}{dr}\,\mathbf L\cdot\mathbf S,
\qquad
V(r)=-\frac{Ze^2}{4\pi\varepsilon_0r}.
```

This expression uses $`g_s=2`$ at leading order. The factor $`\tfrac12`$ includes the Thomas-precession correction. We need its consequence rather than a derivation of the moving-frame dynamics:

```math
\langle\mathbf L\cdot\mathbf S\rangle
=\frac{\hbar^2}{2}
\left[j(j+1)-l(l+1)-\frac34\right].
```

For a p state this is $`-\hbar^2`$ at $`j=\tfrac12`$ and $`+\hbar^2/2`$ at $`j=\tfrac32`$. Since the radial coefficient is positive, 6p<sub>3/2</sub> should lie above 6p<sub>1/2</sub>. Exciting it from the same 2s state should require a higher laser frequency. The splitting distinguishes different $`j`$ values; magnetic substates within a given $`j`$ remain degenerate in the absence of external fields.

Spin–orbit coupling belongs to a group of corrections of the same order. To calculate the complete leading **fine structure**, retain all three:

```math
H_{\mathrm{fs}}=
\underbrace{-\frac{p^4}{8m_e^3c^2}}_{\text{relativistic kinetic energy}}
+\underbrace{\frac{1}{2m_e^2c^2r}\frac{dV}{dr}\,
\mathbf L\cdot\mathbf S}_{\text{spin–orbit coupling}}
+\underbrace{\frac{\hbar^2}{8m_e^2c^2}\nabla^2V}_{\text{Darwin term}}.
```

The first term corrects the non-relativistic kinetic energy. The last is a short-range relativistic correction: for a point Coulomb potential it is concentrated at the nucleus and contributes to non-relativistic s states. It is distinct from the Lamb shift discussed below.

For this calculation, take an infinitely massive point nucleus and $`Z\alpha\ll1`$, where $`\alpha=e^2/(4\pi\varepsilon_0\hbar c)\simeq1/137`$. Unit 1 retained nuclear motion through the reduced mass; we temporarily omit it here to isolate the leading relativistic result. First-order perturbation theory gives

```math
\begin{aligned}
E_{nj}&\simeq E_n^{(0)}+\Delta E_{nj}^{\mathrm{fs}},\\
E_n^{(0)}&=-\frac{m_ec^2(Z\alpha)^2}{2n^2},\\
\Delta E_{nj}^{\mathrm{fs}}&=
-\frac{m_ec^2(Z\alpha)^4}{2n^3}
\left[\frac{1}{j+\tfrac12}-\frac{3}{4n}\right].
\end{aligned}
```

The sum depends on $`n,j`$, although individual contributions depend on $`l`$. It also follows by expanding the point-nucleus Dirac energy. The correction is smaller than the binding energy by a factor of order $`(Z\alpha)^2`$ for low-lying states, which explains why the original Coulomb calculation worked well at modest resolution.

For the two p levels at a fixed $`n`$,

```math
\Delta\nu_{np}
=\frac{E_{n,3/2}-E_{n,1/2}}{h}
\simeq\frac{m_ec^2(Z\alpha)^4}{4hn^3}.
```

For hydrogen at $`n=6`$, this predicts about **406 MHz**, close to the approximately **405 MHz** separation in Figure 2.1, without adjusting a splitting parameter. This agreement tests the scale of the explanation. It is not a precision comparison: recoil, radiative effects and the nuclear splitting introduced in section 2.6 must also be accounted for, as must experimental frequency shifts.

The formula predicts more than this one interval: p-level separations fall as $`n^{-3}`$ and, at fixed $`n`$, grow as $`Z^4`$ for one-electron ions within this approximation.

> **TODO — Add an independent fine-structure comparison.**
>
> Predict a second hydrogen p-level interval, or the corresponding interval in a one-electron ion, before showing its measured value. Identify the transitions used and separate nuclear hyperfine components from the electronic interval. Keep the leading fixed-nucleus calculation distinct from a precision prediction.

## 2.5 How could we test the degeneracy that remains?

The extended model makes another sharp prediction: states with the same $`n,j`$ still have equal energy even when their orbital angular momenta differ. In particular, 2s<sub>1/2</sub> and 2p<sub>1/2</sub> remain degenerate. This equality holds within the ideal point-nucleus Dirac model, not as a general symmetry requirement for a real atom.

How can we compare those two states directly? The electric-dipole selection rule permits a transition between s and p states. If a small energy difference exists, its frequency could lie in the microwave range. A microwave measurement would probe that small difference directly instead of subtracting two large optical frequencies.

Prepare a beam in the long-lived 2s state and apply a tunable microwave field. Population transferred to 2p quickly decays to 1s. A detector that counts surviving 2s atoms should therefore record a loss at resonance. Varying and characterizing the static magnetic field lets us separate field-induced shifts from the interval sought. This is the principle behind the Lamb–Retherford experiment.

Their [original 1947 paper](https://journals.aps.org/pr/abstract/10.1103/PhysRev.72.241) describes how Doppler broadening from atomic motion made earlier optical tests inconclusive. This gives a concrete reason for seeking a direct microwave measurement of the small interval.

> **TODO — Add the measured microwave-quenching record.**
>
> Plot surviving 2s signal against microwave frequency, with the field conditions and relevant state assignments. Explain how the measured resonances determine the zero-field electronic interval after accounting for nuclear hyperfine structure. Show the recorded depletion before giving its energy-level interpretation.

Established measurements place 2s<sub>1/2</sub> above 2p<sub>1/2</sub> by about **1058 MHz**. This quoted electronic interval accounts separately for the nuclear structure discussed next. The measured difference is called the **Lamb shift**. Its explanation requires radiative corrections from quantum electrodynamics, including the electron's interaction with the quantized electromagnetic field; a QED calculation is beyond this first pass.

![Schematic comparison of Coulomb, Dirac and experimentally established hydrogen n equals 2 levels](figures/hydrogen-n2-fine-structure.svg)

*Figure 2.2. Schematic energy-level reconstruction, not a measured spectrum; separations are not to scale. The Coulomb column includes spin but omits spin-dependent interactions. The electronic levels shown omit hyperfine splitting. The Dirac prediction of equal 2s<sub>1/2</sub> and 2p<sub>1/2</sub> energies provides the specific test above.*

## 2.6 Can the nucleus produce additional structure?

So far, the nucleus has supplied charge and mass. Could it also carry angular momentum and a magnetic moment? The 1s electron offers a useful test: it has $`l=0,j=\tfrac12`$, and the electronic fine-structure calculation gives one ground-state energy. A transition within that ground-state manifold would reveal further structure.

We should therefore look beyond optical excitation. Prepare ground-state hydrogen, apply a scanned oscillating magnetic field and detect whether atoms change their internal state. State-selective beam detection can convert that change into a count signal. A controlled static field helps identify field-dependent components and recover their zero-field separation.

> **TODO — Add a laboratory ground-state hyperfine resonance.**
>
> Show the measured state-transfer signal against microwave frequency, with the state preparation, detection method, calibration and magnetic-field dependence. Distinguish this laboratory record from a sky spectrum, whose frequency also contains Doppler information.

Laboratory measurements establish a ground-state interval of about **1420.406 MHz**. Its corresponding wavelength is about 21.1 cm. What can split the ground state when the electron has no orbital angular momentum?

The proton has spin $`I=\tfrac12`$ and magnetic moment

```math
\boldsymbol{\mu}_I=g_p\mu_N\frac{\mathbf I}{\hbar},
\qquad
\mu_N=\frac{e\hbar}{2m_p},
\qquad g_p\simeq5.586.
```

The nuclear magneton $`\mu_N`$ is smaller than $`\mu_B`$ by $`m_e/m_p`$. Coupling between nuclear and electronic moments therefore introduces a smaller energy scale, called **hyperfine structure**. Within an isolated electronic level, the leading magnetic-dipole interaction is

```math
H_{\mathrm{hf}}=A_{\mathrm{hf}}
\frac{\mathbf I\cdot\mathbf J}{\hbar^2},
\qquad
\mathbf F=\mathbf I+\mathbf J,
\qquad F=|I-j|,\ldots,I+j.
```

Here $`A_{\mathrm{hf}}`$ has energy units. The same angular-momentum identity used for spin–orbit coupling gives

```math
E_F=\frac{A_{\mathrm{hf}}}{2}
\left[F(F+1)-I(I+1)-j(j+1)\right].
```

For hydrogen 1s, $`I=j=\tfrac12`$, so $`F=0,1`$. Their shifts are $`-3A_{\mathrm{hf}}/4`$ and $`+A_{\mathrm{hf}}/4`$: the interval is $`A_{\mathrm{hf}}`$. Each level still contains $`2F+1`$ magnetic substates at zero field.

![Schematic hyperfine splitting of the hydrogen ground state](figures/hydrogen-21cm.svg)

*Figure 2.3. Model level diagram, not a detector record. Including the proton's magnetic coupling splits the hydrogen ground state. The magnetic-dipole transition F = 1 → F = 0 produces the 21 cm line; an optical electric-dipole measurement would not reveal this interval in the same way.*

Can the interaction predict its size? For a non-relativistic s electron, the leading **Fermi contact interaction** samples the probability density at the nucleus:

```math
A_{\mathrm{hf}}=
\frac{2\mu_0}{3}g_s\mu_Bg_p\mu_N|\psi_{ns}(0)|^2,
\qquad
|\psi_{ns}(0)|^2=\frac{1}{\pi n^3a_\mu^3},
\qquad
a_\mu=\frac{4\pi\varepsilon_0\hbar^2}{\mu e^2}.
```

Here $`\mu`$ is the electron–proton reduced mass. For 1s, this predicts $`A_{\mathrm{hf}}/h\simeq1.42\ \mathrm{GHz}`$, accounting for the observed scale. Precision comparisons require recoil, radiative and proton-structure corrections.

The density gives a further test: the contact interval should fall as $`n^{-3}`$. Using the measured 1s interval to set the scale predicts a 2s interval of $`1420.406/8\simeq177.551\ \mathrm{MHz}`$. The measured value is about $`177.557\ \mathrm{MHz}`$. This tests the state dependence of the coupling, independently of fitting its absolute scale. The simple magnetic-dipole model needs additional terms when nuclear electric quadrupole moments contribute.

We can now refine the interpretation of Figure 2.1. Its two resonances connect 2s<sub>1/2</sub>, F = 0 to 6p<sub>1/2</sub>, F = 1 and 6p<sub>3/2</sub>, F = 1. Their separation therefore includes hyperfine offsets as well as the electronic fine-structure interval. The common initial state remains essential, but the upper-state labels now contain more information than the Coulomb model supplied.

## 2.7 What should change when we replace the isotope?

Unit 1 proposed replacing hydrogen by deuterium to test the nuclear-mass dependence while retaining the same charge. We can now ask a more precise question: are we comparing corresponding hyperfine components, or the centres of the electronic levels?

Within the magnetic-dipole model, a hyperfine centroid is the average over levels weighted by their degeneracies $`2F+1`$. It recovers the unsplit electronic energy. An unresolved line's measured centre need not equal this centroid, because component strengths and populations determine its observed weighting.

For corresponding electronic transitions in a one-electron atom, reduced mass gives the leading prediction

```math
\nu_M\propto\mu_M,
\qquad
\frac{\nu_{M'}-\nu_M}{\nu_M}
\simeq m_e\left(\frac{1}{M}-\frac{1}{M'}\right),
\qquad M'>M\gg m_e.
```

The heavier isotope should have the higher frequency at this order. This explains the leading hydrogen–deuterium shift proposed in Unit 1. A change in nuclear spin also changes the hyperfine pattern: the deuteron has $`I=1`$, so a level with $`j=\tfrac12`$ has $`F=\tfrac12,\tfrac32`$, rather than hydrogen's $`F=0,1`$.

Nuclear charge is also spread over a finite volume. Replacing a point charge by an extended distribution weakens the attraction close to the origin. For a non-relativistic s state, the leading difference between isotopes is

```math
\delta E_{ns}^{\mathrm{size}}
\simeq\frac{Ze^2}{6\varepsilon_0}
|\psi_{ns}(0)|^2\,\delta\langle r_N^2\rangle.
```

A larger mean-square nuclear charge radius raises the s-state energy at this order. The shift of a transition is the difference of its upper- and lower-level shifts, so its sign requires both. This is the nuclear-size or **field shift**; it does not refer to an externally applied field. It can become important in heavier atoms. Many-electron atoms also have an additional, correlated mass shift, which belongs with Unit 3.

> **TODO — Extend the isotope comparison beyond the leading mass shift.**
>
> Use calibrated hydrogen and deuterium spectra to identify corresponding components or construct hyperfine centroids. First compare the separation with Unit 1's reduced-mass prediction. State what resolution and uncertainty would be needed to distinguish nuclear-size and other corrections; do not attribute an unexplained residual to nuclear size alone.

## 2.8 What changes when there is a second electron?

The original optical pattern led us to the Coulomb model. Its predicted degeneracies then suggested new measurements: magnetic deflection identified an electronic degree of freedom, resolved excitation tested its coupling to orbital motion, and microwave measurements probed remaining electronic and nuclear structure. Each probe answered a question that the preceding record left open.

Our quantitative model has still described only one electron. We can make a controlled change by comparing the one-electron ion He⁺ with neutral helium: the nuclear charge remains the same, but a second electron is added. It brings a mutual Coulomb repulsion, and the two electrons must be described as indistinguishable particles with spin. How do those facts change the allowed states and excitation spectrum? Can independent hydrogenic levels still provide a useful starting point?

[Unit 3](unit-3-many-electron-atoms.md) develops that comparison, leading to electron correlation, the Pauli principle and helium's singlet and triplet states.

---

## Sources and conventions

- **Scope:** electron spin, relativistic corrections to hydrogen energy levels, hyperfine structure and isotope shifts, as specified in Section VII of the supplied CSIR–UGC NET Physical Sciences syllabus. Full external-field patterns belong to Unit 4; transition rates and line strengths to Unit 5.
- Stern–Gerlach, spin and angular-momentum coupling: C. J. Foot, *Atomic Physics*; Haken and Wolf, *The Physics of Atoms and Quanta*. The detector record remains a TODO; the description of its established outcome is not a new plotted measurement.
- Figure 2.1: L. Maisenbacher, *Dataset for the hydrogen 2S–6P transition measurement at MPQ*, v1 (2026), doi:10.5281/zenodo.15874385, CC BY 4.0; L. Maisenbacher et al., *Nature* **650**, 845–851 (2026), doi:10.1038/s41586-026-10124-3. The [local provenance](data/hydrogen-2s-6p-mpq/README.md) and [plotting script](analysis/plot_hydrogen_fine_structure.py) accompany the measured scans.
- Fine structure, contact interaction and isotope shifts: Foot; B. H. Bransden and C. J. Joachain, *Physics of Atoms and Molecules*. The fine-structure formula here assumes an infinitely massive point nucleus and retains terms through order $`(Z\alpha)^4`$.
- Lamb-shift experiment: W. E. Lamb Jr. and R. C. Retherford, *Physical Review* **72**, 241–243 (1947), doi:10.1103/PhysRev.72.241. The rounded electronic interval quoted here is an established value, not the precision of the original experiment.
- Hydrogen 2s hyperfine interval: N. Kolachevsky et al., *Physical Review Letters* **102**, 213002 (2009), doi:10.1103/PhysRevLett.102.213002. Ground-state hyperfine reference: L. Essen et al., *Nature* **229**, 110–111 (1971), doi:10.1038/229110a0.
- Figures 2.2–2.3 are schematic level diagrams. Frequencies are ordinary frequencies $`\nu`$, not angular frequencies. $`A_{\mathrm{hf}}`$ denotes an energy; a hyperfine constant quoted in MHz means $`A_{\mathrm{hf}}/h`$. Constants use CODATA 2018; quoted comparisons are rounded to the accuracy appropriate to the model.
