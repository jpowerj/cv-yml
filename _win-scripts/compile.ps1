# Sigh. First we need to copy the .yml data into the content.tex frontmatter
python gen_frontmatter.py
jtex freeform template.tex content.tex --output-tex output.tex
pdflatex.exe --shell-escape -synctex=1 -interaction=nonstopmode output.tex
$timestamp = Get-Date -UFormat "%Y-%m-%d"
$fname = "Jacobs_CV_" + $timestamp + ".pdf"
cp output.pdf $fname

