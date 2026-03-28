# Stacked FTIR Plotter from Excel Files

A Python script that reads multi-sample FTIR transmission data from an Excel file and generates an interactive overlay plot of all spectra using Plotly.

---

## Author

**Nitish Kapur**<br>
GitHub: [github.com/nitish-kapur](https://github.com/nitish-kapur)

---

## Expected Input Format

The script expects an `.xls` or `.xlsx` Excel file named `FTIR Precursors.xls` in the same directory, structured as follows:

| Wavenumber | Sample 1 | Sample 2 | Sample 3 | ... |
|---|---|---|---|---|
| 400.296851 | 85.17 | 97.12 | 97.78 | ... |
| 401.731607 | 84.71 | 97.60 | 97.99 | ... |
| ... | ... | ... | ... | ... |

- **Column 1** — Wavenumber values (cm⁻¹)
- **Columns 2 onwards** — Transmission (%) for each sample; column headers are used as legend labels

---

## Requirements
```bash
pip install pandas plotly openpyxl xlrd
```

---

## Usage

1. Place `FTIR Precursors.xls` in the same directory as the script
2. Run:
```bash
python ftir-excel-multiple-stacked.py
```

The interactive plot will open automatically in your default web browser.

---

## Output

- An interactive Plotly overlay plot displayed in the browser
- X-axis: Wavenumber (cm⁻¹), inverted as per FTIR convention
- Y-axis: Averaged Transmission (%)
- Each sample is plotted as a separate coloured line
- Hovering over a trace displays the wavenumber and transmission value

---

## Notes

- The input filename is hard-coded as `FTIR Precursors.xls`. Update the `file_path` variable at the top of the script to change it.
- Up to 13 distinct colours are assigned to traces automatically; additional samples cycle through the same colours.
- The plot is displayed interactively only — to save it as an HTML file, add `fig.write_html("output.html")` before `fig.show()`.
