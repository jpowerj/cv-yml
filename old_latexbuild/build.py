from latexbuild import build_pdf, build_html, build_docx, render_latex_template

PATH_JINJA2 = "./"
PATH_TEMPLATE_RELATIVE_TO_PATH_JINJA2 = "./template/template.tex"
PATH_OUTPUT_PDF = "./output.pdf"
PATH_OUTPUT_HTML = "./output.html"
PATH_OUTPUT_DOCX = "./output.docx"

# Build Jinja2 template, compile result latex, move compiled file to output path,
# and clean up all intermediate files
build_pdf(PATH_JINJA2, PATH_TEMPLATE_RELATIVE_TO_PATH_JINJA2, PATH_OUTPUT_PDF)

#build_html(PATH_JINJA2, PATH_TEMPLATE_RELATIVE_TO_PATH_JINJA2, PATH_OUTPUT_HTML)
#build_docx(PATH_JINJA2, PATH_TEMPLATE_RELATIVE_TO_PATH_JINJA2, PATH_OUTPUT_DOCX)

# If you just want the rendered template's text in a python variable,
# do the following (assuming you have no variables to pass):
#render_latex_template(PATH_JINJA2, PATH_TEMPLATE_RELATIVE_TO_PATH_JINJA2)

# If your template renders Jinja2 variables, most interfaces provide
# a dictionary parameter. See below for an example for simply
# rendering the template's text in Python
DICT_VALS = {
    'var1': 'my variable 1 value',
    'list_var': ['item 1 for analysis', 'item 2 for analysis']
    }
#render_latex_template(
#    PATH_JINJA2,
#    PATH_TEMPLATE_RELATIVE_TO_PATH_JINJA2,
#    DICT_VALS,
#    )
