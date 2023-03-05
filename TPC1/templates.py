TEMPLATE_CITY = """
<a name="id">
<h3>nome</h3>
<p><b>Distrito:</b> distrito</p>
<p><b>População:</b> população</p>
<p><b>Descrição:</b> descrição</p>
</a>
<center>
    <hr width="80%"/>
</center>
"""

TEMPLATE_INDEX_CITY = '<li>\n\t<a href="#cod">nome</a>\n</li>'

TEMPLATE_PAGE = """
<!DOCTYPE html>
<html>
    <head>
        <title>Mapa Virtual</title>
        <meta charset="utf-8"/>
    </head>
    <body>
        <h1>Mapa Virtual</h1>
        <table>
            <tr>
                <!-- Coluna do índice -->
                <td width="30%" valign="top">
                    <h3>Índice</h3>
                    <ol>
                        inserir_index
                    </ol>
                </td>
                <!-- Coluna do conteúdo -->
                <td width="70%">
                    inserir_conteudo
                </td>
            </tr>
        </table>
    </body>
</html>
"""
